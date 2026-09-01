from pathlib import Path


def replace_exact(path: Path, old: str, new: str, expected: int = 1) -> None:
    text = path.read_text()
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{path}: expected {expected} matches, got {count}: {old[:120]!r}")
    path.write_text(text.replace(old, new, expected))


root = Path("ChatGPTClient/RootViewController.swift")

replace_exact(
    root,
    "    case externalStreamingObserved\n    case externalConversationSnapshot(messages: [[String: Any]], complete: Bool)",
    "    case externalStreamingObserved\n    case externalAcquisitionHint\n    case externalConversationSnapshot(messages: [[String: Any]], complete: Bool)",
)

replace_exact(
    root,
    "    private var sendExecutors: [String: CoveredWebSendExecutor] = [:]\n    private let validationSendButton = UIButton(type: .system)",
    "    private var sendExecutors: [String: CoveredWebSendExecutor] = [:]\n    private var externalAcquisitionSyncs: Set<String> = []\n    private let validationSendButton = UIButton(type: .system)",
)

replace_exact(
    root,
    "            self.sendExecutors.removeAll()\n            for executor in executors { executor.resetForAccountChange() }",
    "            self.sendExecutors.removeAll()\n            self.externalAcquisitionSyncs.removeAll()\n            for executor in executors { executor.resetForAccountChange() }",
)

replace_exact(
    root,
    "            diagnostics.info(category: \"webSend\", name: \"coveredExecutor.webSocketStructure\", fields: [\"state\": state, \"host\": host, \"path\": path, \"dataType\": dataType, \"length\": String(length), \"topKeys\": topKeys, \"nestedKeys\": nestedKeys, \"typeToken\": typeToken, \"eventToken\": eventToken, \"kindToken\": kindToken, \"actionToken\": actionToken, \"topicToken\": topicToken, \"nameToken\": nameToken, \"hasConversationKey\": hasConversationKey ? \"true\" : \"false\", \"targetMatch\": targetMatch ? \"true\" : \"false\"])\n        case \"resume_response\":",
    "            diagnostics.info(category: \"webSend\", name: \"coveredExecutor.webSocketStructure\", fields: [\"state\": state, \"host\": host, \"path\": path, \"dataType\": dataType, \"length\": String(length), \"topKeys\": topKeys, \"nestedKeys\": nestedKeys, \"typeToken\": typeToken, \"eventToken\": eventToken, \"kindToken\": kindToken, \"actionToken\": actionToken, \"topicToken\": topicToken, \"nameToken\": nameToken, \"hasConversationKey\": hasConversationKey ? \"true\" : \"false\", \"targetMatch\": targetMatch ? \"true\" : \"false\"])\n            if state == \"message\", targetMatch, activeEvents == nil {\n                observationEvents?(.externalAcquisitionHint)\n                diagnostics.info(category: \"webSend\", name: \"coveredExecutor.externalAcquisitionHint\", fields: [\"source\": \"websocket_target_match\", \"target\": \"existing_conversation\"])\n            }\n        case \"resume_response\":",
)

replace_exact(
    root,
    "    case .externalStreamingObserved: eventName = \"external_streaming_observed\"\n    case .externalConversationSnapshot(_, _): eventName = \"external_conversation_snapshot\"",
    "    case .externalStreamingObserved: eventName = \"external_streaming_observed\"\n    case .externalAcquisitionHint: eventName = \"external_acquisition_hint\"\n    case .externalConversationSnapshot(_, _): eventName = \"external_conversation_snapshot\"",
)

replace_exact(
    root,
    "            switch event {\n            case .externalResumeObserved:\n                return",
    "            switch event {\n            case .externalAcquisitionHint:\n                guard externalGeneration == nil else { return }\n                self.handleExternalAcquisitionHint(conversationID: conversationID, sendExecutor: sendExecutor)\n                return\n            case .externalResumeObserved:\n                return",
)

anchor = "    private func startValidationSend(text: String, conversationID: String) {"
helper = '''    private func handleExternalAcquisitionHint(conversationID: String, sendExecutor: CoveredWebSendExecutor) {
        guard repository.selectedConversationID == conversationID else {
            diagnostics.info(category: "webSend", name: "externalAcquisitionSync.skipped", fields: ["reason": "conversation_not_selected"])
            return
        }
        guard !repository.isLiveResponseActive(for: conversationID) else {
            diagnostics.info(category: "webSend", name: "externalAcquisitionSync.skipped", fields: ["reason": "live_response_active"])
            return
        }
        guard !externalAcquisitionSyncs.contains(conversationID) else {
            diagnostics.info(category: "webSend", name: "externalAcquisitionSync.skipped", fields: ["reason": "sync_in_flight"])
            return
        }
        guard repository.detailOperationSnapshot(for: conversationID) == nil else {
            diagnostics.info(category: "webSend", name: "externalAcquisitionSync.skipped", fields: ["reason": "detail_operation_in_flight"])
            return
        }

        let previousLatestUserID = repository.selectedConversation?.messages.last(where: { $0.role == .user })?.id
        externalAcquisitionSyncs.insert(conversationID)
        diagnostics.info(category: "webSend", name: "externalAcquisitionSync.started", fields: repository.diagnosticsFields(for: conversationID))
        repository.syncLatestMessages(id: conversationID) { [weak self, weak sendExecutor] result in
            guard let self else { return }
            self.externalAcquisitionSyncs.remove(conversationID)
            guard let sendExecutor else { return }
            switch result {
            case .success(let detail):
                let latestUserID = detail.messages.last(where: { $0.role == .user })?.id
                let latestUserChanged = latestUserID != nil && latestUserID != previousLatestUserID
                _ = self.repository.clearTerminalExternalLiveResponseAfterAuthoritativeRefresh(conversationID: conversationID)
                var fields = self.repository.diagnosticsFields(for: conversationID)
                fields["latestUserChanged"] = latestUserChanged ? "true" : "false"
                fields["visibleMessageCount"] = String(detail.messages.count)
                self.diagnostics.info(category: "webSend", name: "externalAcquisitionSync.completed", fields: fields)
                if self.repository.selectedConversationID == conversationID { self.detailViewController.showConversation(id: conversationID) }
                guard latestUserChanged, self.repository.selectedConversationID == conversationID, !self.repository.isLiveResponseActive(for: conversationID), self.sendExecutors[conversationID] === sendExecutor else { return }
                self.observeExternalResponseIfNeeded(conversationID: conversationID, forcePageReload: true)
            case .failure(let error):
                self.diagnostics.error(category: "webSend", name: "externalAcquisitionSync.failed", error: error, fields: self.repository.diagnosticsFields(for: conversationID))
            }
        }
    }

'''
replace_exact(root, anchor, helper + anchor)

pbx = Path("ChatGPTClient.xcodeproj/project.pbxproj")
text = pbx.read_text()
if text.count("CURRENT_PROJECT_VERSION = 81;") != 2:
    raise SystemExit("unexpected Build 81 count")
if text.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b81";') != 2:
    raise SystemExit("unexpected b81 candidate count")
text = text.replace("CURRENT_PROJECT_VERSION = 81;", "CURRENT_PROJECT_VERSION = 82;")
text = text.replace('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b81";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b82";')
pbx.write_text(text)
