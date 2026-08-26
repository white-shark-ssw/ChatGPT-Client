import Foundation

enum ProtocolReadState {
    case verified
    case listNotAvailable
    case detailNotAvailable
    case failed
}

final class ProtocolReadProbe {
    private static let listURL: URL = {
        var components = URLComponents(string: "https://chatgpt.com/backend-api/conversations")!
        components.queryItems = [
            URLQueryItem(name: "offset", value: "0"),
            URLQueryItem(name: "limit", value: "28"),
            URLQueryItem(name: "order", value: "updated")
        ]
        return components.url!
    }()

    private let diagnostics = DiagnosticsLogger.shared

    func run(using session: AuthTransientSession, completion: @escaping (ProtocolReadState) -> Void) {
        let span = diagnostics.startSpan(category: "protocol", name: "conversationReadProbe")
        diagnostics.info(category: "protocol", name: "conversationList.request", traceID: span.traceID, fields: ["method": "GET", "route": "conversation_list", "offset": "0", "limit": "28", "order": "updated"])
        var request = URLRequest(url: Self.listURL)
        request.httpMethod = "GET"
        session.dataTask(with: request) { [weak self] data, response, error in
            guard let self else { return }
            if let error {
                self.diagnostics.error(category: "protocol", name: "conversationList.failed", traceID: span.traceID, error: error)
                self.finish(.failed, session: session, span: span, fields: ["stage": "list"], completion: completion)
                return
            }
            guard let response = response as? HTTPURLResponse, let data else {
                self.finish(.failed, session: session, span: span, fields: ["stage": "list", "reason": "non_http_response"], completion: completion)
                return
            }
            guard (200..<300).contains(response.statusCode) else {
                self.finish(.listNotAvailable, session: session, span: span, fields: ["stage": "list", "httpStatus": String(response.statusCode)], completion: completion)
                return
            }
            guard let payload = try? JSONSerialization.jsonObject(with: data) as? [String: Any], let items = payload["items"] as? [Any] else {
                self.finish(.listNotAvailable, session: session, span: span, fields: ["stage": "list", "httpStatus": String(response.statusCode), "reason": "missing_items"], completion: completion)
                return
            }

            var fields = ["httpStatus": String(response.statusCode), "byteCount": String(data.count), "itemCount": String(items.count)]
            Self.copyIntegerField("total", from: payload, to: "totalCount", fields: &fields)
            Self.copyIntegerField("limit", from: payload, to: "responseLimit", fields: &fields)
            Self.copyIntegerField("offset", from: payload, to: "responseOffset", fields: &fields)
            self.diagnostics.info(category: "protocol", name: "conversationList.response", traceID: span.traceID, fields: fields)

            guard let conversationID = items.compactMap({ ($0 as? [String: Any])?["id"] as? String }).first(where: { !$0.isEmpty }) else {
                fields["stage"] = "detail"
                fields["reason"] = "missing_conversation_id"
                self.finish(.detailNotAvailable, session: session, span: span, fields: fields, completion: completion)
                return
            }
            self.requestDetail(conversationID: conversationID, session: session, span: span, listFields: fields, completion: completion)
        }
    }

    private func requestDetail(conversationID: String, session: AuthTransientSession, span: DiagnosticsSpan, listFields: [String: String], completion: @escaping (ProtocolReadState) -> Void) {
        let baseURL = URL(string: "https://chatgpt.com/backend-api/conversation")!
        let detailURL = baseURL.appendingPathComponent(conversationID)
        diagnostics.info(category: "protocol", name: "conversationDetail.request", traceID: span.traceID, fields: ["method": "GET", "route": "conversation_detail", "selection": "first_list_item"])
        var request = URLRequest(url: detailURL)
        request.httpMethod = "GET"
        session.dataTask(with: request) { [weak self] data, response, error in
            guard let self else { return }
            if let error {
                self.diagnostics.error(category: "protocol", name: "conversationDetail.failed", traceID: span.traceID, error: error)
                self.finish(.failed, session: session, span: span, fields: ["stage": "detail"], completion: completion)
                return
            }
            guard let response = response as? HTTPURLResponse, let data else {
                self.finish(.failed, session: session, span: span, fields: ["stage": "detail", "reason": "non_http_response"], completion: completion)
                return
            }
            guard (200..<300).contains(response.statusCode) else {
                self.finish(.detailNotAvailable, session: session, span: span, fields: ["stage": "detail", "httpStatus": String(response.statusCode)], completion: completion)
                return
            }
            guard let payload = try? JSONSerialization.jsonObject(with: data) as? [String: Any], let mapping = payload["mapping"] as? [String: Any] else {
                self.finish(.detailNotAvailable, session: session, span: span, fields: ["stage": "detail", "httpStatus": String(response.statusCode), "reason": "missing_mapping"], completion: completion)
                return
            }

            let currentNode = payload["current_node"] as? String
            let returnedConversationID = payload["conversation_id"] as? String
            var messageNodeCount = 0
            var nullMessageNodeCount = 0
            var rootNodeCount = 0
            var branchingNodeCount = 0
            var maxChildrenCount = 0
            var userRoleCount = 0
            var assistantRoleCount = 0
            var systemRoleCount = 0
            var toolRoleCount = 0
            var otherRoleCount = 0
            var contentTypes = Set<String>()

            for value in mapping.values {
                guard let node = value as? [String: Any] else { continue }
                let parent = node["parent"]
                if parent == nil || parent is NSNull { rootNodeCount += 1 }
                let childrenCount = (node["children"] as? [Any])?.count ?? 0
                if childrenCount > 1 { branchingNodeCount += 1 }
                maxChildrenCount = max(maxChildrenCount, childrenCount)

                guard let message = node["message"] as? [String: Any] else {
                    nullMessageNodeCount += 1
                    continue
                }
                messageNodeCount += 1
                let role = ((message["author"] as? [String: Any])?["role"] as? String) ?? ""
                switch role {
                case "user": userRoleCount += 1
                case "assistant": assistantRoleCount += 1
                case "system": systemRoleCount += 1
                case "tool": toolRoleCount += 1
                default: otherRoleCount += 1
                }
                if let contentType = (message["content"] as? [String: Any])?["content_type"] as? String, !contentType.isEmpty { contentTypes.insert(contentType) }
            }

            var fields = [
                "httpStatus": String(response.statusCode),
                "byteCount": String(data.count),
                "mappingCount": String(mapping.count),
                "messageNodeCount": String(messageNodeCount),
                "nullMessageNodeCount": String(nullMessageNodeCount),
                "rootNodeCount": String(rootNodeCount),
                "branchingNodeCount": String(branchingNodeCount),
                "maxChildrenCount": String(maxChildrenCount),
                "userRoleCount": String(userRoleCount),
                "assistantRoleCount": String(assistantRoleCount),
                "systemRoleCount": String(systemRoleCount),
                "toolRoleCount": String(toolRoleCount),
                "otherRoleCount": String(otherRoleCount),
                "contentTypeCount": String(contentTypes.count),
                "currentNodePresent": String(currentNode?.isEmpty == false),
                "currentNodeMapped": String(currentNode.map { mapping[$0] != nil } ?? false),
                "conversationIdentityPresent": String(returnedConversationID?.isEmpty == false),
                "conversationIdentityMatches": String(returnedConversationID == conversationID)
            ]
            for (key, value) in listFields { fields["list_\(key)"] = value }
            self.diagnostics.info(category: "protocol", name: "conversationDetail.response", traceID: span.traceID, fields: fields)
            self.finish(.verified, session: session, span: span, fields: ["stage": "detail", "listItemCount": listFields["itemCount"] ?? "unknown", "mappingCount": String(mapping.count), "messageNodeCount": String(messageNodeCount)], completion: completion)
        }
    }

    private func finish(_ state: ProtocolReadState, session: AuthTransientSession, span: DiagnosticsSpan, fields: [String: String], completion: @escaping (ProtocolReadState) -> Void) {
        session.finishTasksAndInvalidate()
        let status: String
        switch state {
        case .verified: status = "ok"
        case .listNotAvailable, .detailNotAvailable: status = "not_available"
        case .failed: status = "failed"
        }
        span.end(status: status, fields: fields)
        completion(state)
    }

    private static func copyIntegerField(_ sourceKey: String, from payload: [String: Any], to destinationKey: String, fields: inout [String: String]) {
        if let value = payload[sourceKey] as? NSNumber { fields[destinationKey] = value.stringValue }
    }
}
