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
            self?.handleListResponse(data: data, response: response, error: error, session: session, span: span, completion: completion)
        }
    }

    private func handleListResponse(data: Data?, response: URLResponse?, error: Error?, session: AuthTransientSession, span: DiagnosticsSpan, completion: @escaping (ProtocolReadState) -> Void) {
        if let error {
            diagnostics.error(category: "protocol", name: "conversationList.failed", traceID: span.traceID, error: error)
            finish(.failed, session: session, span: span, fields: ["stage": "list"], completion: completion)
            return
        }
        guard let response = response as? HTTPURLResponse, let data else {
            finish(.failed, session: session, span: span, fields: ["stage": "list", "reason": "non_http_response"], completion: completion)
            return
        }
        guard (200..<300).contains(response.statusCode) else {
            finish(.listNotAvailable, session: session, span: span, fields: ["stage": "list", "httpStatus": String(response.statusCode)], completion: completion)
            return
        }
        guard let payload = try? JSONSerialization.jsonObject(with: data) as? [String: Any], let items = payload["items"] as? [Any] else {
            finish(.listNotAvailable, session: session, span: span, fields: ["stage": "list", "httpStatus": String(response.statusCode), "reason": "missing_items"], completion: completion)
            return
        }

        var fields = ["httpStatus": String(response.statusCode), "byteCount": String(data.count), "itemCount": String(items.count)]
        Self.copyIntegerField("total", from: payload, to: "totalCount", fields: &fields)
        Self.copyIntegerField("limit", from: payload, to: "responseLimit", fields: &fields)
        Self.copyIntegerField("offset", from: payload, to: "responseOffset", fields: &fields)
        diagnostics.info(category: "protocol", name: "conversationList.response", traceID: span.traceID, fields: fields)

        var conversationID: String?
        for item in items {
            guard let item = item as? [String: Any], let id = item["id"] as? String, !id.isEmpty else { continue }
            conversationID = id
            break
        }
        guard let conversationID else {
            fields["stage"] = "detail"
            fields["reason"] = "missing_conversation_id"
            finish(.detailNotAvailable, session: session, span: span, fields: fields, completion: completion)
            return
        }
        requestDetail(conversationID: conversationID, session: session, span: span, listFields: fields, completion: completion)
    }

    private func requestDetail(conversationID: String, session: AuthTransientSession, span: DiagnosticsSpan, listFields: [String: String], completion: @escaping (ProtocolReadState) -> Void) {
        let baseURL = URL(string: "https://chatgpt.com/backend-api/conversation")!
        let detailURL = baseURL.appendingPathComponent(conversationID)
        diagnostics.info(category: "protocol", name: "conversationDetail.request", traceID: span.traceID, fields: ["method": "GET", "route": "conversation_detail", "selection": "first_list_item"])
        var request = URLRequest(url: detailURL)
        request.httpMethod = "GET"
        session.dataTask(with: request) { [weak self] data, response, error in
            self?.handleDetailResponse(data: data, response: response, error: error, conversationID: conversationID, session: session, span: span, listFields: listFields, completion: completion)
        }
    }

    private func handleDetailResponse(data: Data?, response: URLResponse?, error: Error?, conversationID: String, session: AuthTransientSession, span: DiagnosticsSpan, listFields: [String: String], completion: @escaping (ProtocolReadState) -> Void) {
        if let error {
            diagnostics.error(category: "protocol", name: "conversationDetail.failed", traceID: span.traceID, error: error)
            finish(.failed, session: session, span: span, fields: ["stage": "detail"], completion: completion)
            return
        }
        guard let response = response as? HTTPURLResponse, let data else {
            finish(.failed, session: session, span: span, fields: ["stage": "detail", "reason": "non_http_response"], completion: completion)
            return
        }
        guard (200..<300).contains(response.statusCode) else {
            finish(.detailNotAvailable, session: session, span: span, fields: ["stage": "detail", "httpStatus": String(response.statusCode)], completion: completion)
            return
        }
        guard let payload = try? JSONSerialization.jsonObject(with: data) as? [String: Any], let mapping = payload["mapping"] as? [String: Any] else {
            finish(.detailNotAvailable, session: session, span: span, fields: ["stage": "detail", "httpStatus": String(response.statusCode), "reason": "missing_mapping"], completion: completion)
            return
        }

        let summary = summarize(mapping: mapping)
        let currentNode = payload["current_node"] as? String
        let returnedConversationID = payload["conversation_id"] as? String
        var fields = [
            "httpStatus": String(response.statusCode),
            "byteCount": String(data.count),
            "mappingCount": String(mapping.count),
            "messageNodeCount": String(summary.messageNodeCount),
            "nullMessageNodeCount": String(summary.nullMessageNodeCount),
            "rootNodeCount": String(summary.rootNodeCount),
            "branchingNodeCount": String(summary.branchingNodeCount),
            "maxChildrenCount": String(summary.maxChildrenCount),
            "userRoleCount": String(summary.userRoleCount),
            "assistantRoleCount": String(summary.assistantRoleCount),
            "systemRoleCount": String(summary.systemRoleCount),
            "toolRoleCount": String(summary.toolRoleCount),
            "otherRoleCount": String(summary.otherRoleCount),
            "contentTypeCount": String(summary.contentTypeCount),
            "currentNodePresent": String(currentNode?.isEmpty == false),
            "currentNodeMapped": String(currentNode.map { mapping[$0] != nil } ?? false),
            "conversationIdentityPresent": String(returnedConversationID?.isEmpty == false),
            "conversationIdentityMatches": String(returnedConversationID == conversationID)
        ]
        for (key, value) in listFields { fields["list_\(key)"] = value }
        diagnostics.info(category: "protocol", name: "conversationDetail.response", traceID: span.traceID, fields: fields)
        finish(.verified, session: session, span: span, fields: ["stage": "detail", "listItemCount": listFields["itemCount"] ?? "unknown", "mappingCount": String(mapping.count), "messageNodeCount": String(summary.messageNodeCount)], completion: completion)
    }

    private func summarize(mapping: [String: Any]) -> DetailSummary {
        var summary = DetailSummary()
        var contentTypes = Set<String>()
        for value in mapping.values {
            guard let node = value as? [String: Any] else { continue }
            let parent = node["parent"]
            if parent == nil || parent is NSNull { summary.rootNodeCount += 1 }
            let childrenCount = (node["children"] as? [Any])?.count ?? 0
            if childrenCount > 1 { summary.branchingNodeCount += 1 }
            summary.maxChildrenCount = max(summary.maxChildrenCount, childrenCount)

            guard let message = node["message"] as? [String: Any] else {
                summary.nullMessageNodeCount += 1
                continue
            }
            summary.messageNodeCount += 1
            let author = message["author"] as? [String: Any]
            let role = author?["role"] as? String ?? ""
            switch role {
            case "user": summary.userRoleCount += 1
            case "assistant": summary.assistantRoleCount += 1
            case "system": summary.systemRoleCount += 1
            case "tool": summary.toolRoleCount += 1
            default: summary.otherRoleCount += 1
            }
            let content = message["content"] as? [String: Any]
            if let contentType = content?["content_type"] as? String, !contentType.isEmpty { contentTypes.insert(contentType) }
        }
        summary.contentTypeCount = contentTypes.count
        return summary
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

private struct DetailSummary {
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
    var contentTypeCount = 0
}
