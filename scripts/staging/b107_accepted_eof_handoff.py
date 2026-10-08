from pathlib import Path


def replace_exact(path: str, old: str, new: str, expected: int = 1) -> None:
    p = Path(path)
    text = p.read_text()
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{path}: expected {expected} matches, found {count}: {old[:100]!r}")
    p.write_text(text.replace(old, new))

project = "ChatGPTClient.xcodeproj/project.pbxproj"
replace_exact(project, "CURRENT_PROJECT_VERSION = 106;", "CURRENT_PROJECT_VERSION = 107;", expected=2)
replace_exact(project, 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b106";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b107";', expected=2)

root = "ChatGPTClient/RootViewController.swift"
replace_exact(
    root,
    "    case acceptedClientWebProcessInterrupted\n    case thinkingActive\n",
    "    case acceptedClientWebProcessInterrupted\n    case acceptedClientStreamEndedWithoutTerminal\n    case thinkingActive\n",
)

replace_exact(
    root,
    '        case "stream_error": failCurrent(body["state"] as? String ?? "stream_error")\n',
    '''        case "stream_error":\n            let state = body["state"] as? String ?? "stream_error"\n            if state == "stream_ended_without_done", clientSendAccepted, responseActive, currentConversationID != nil, let interruptedEvents = activeEvents {\n                pendingSend = nil\n                responseActive = false\n                clientSendAccepted = false\n                activeEvents = nil\n                composerReadyConversationID = nil\n                diagnostics.warning(category: "webSend", name: "coveredExecutor.acceptedClientStreamEndRecovery", fields: ["state": UIApplication.shared.applicationState == .active ? "handoff_requested" : "deferred_to_foreground", "policy": "no_resend_same_generation"])\n                interruptedEvents(.acceptedClientStreamEndedWithoutTerminal)\n                return\n            }\n            failCurrent(state)\n''',
)

replace_exact(
    root,
    '    case .acceptedClientWebProcessInterrupted: eventName = "accepted_client_web_process_interrupted"\n    case .thinkingActive:\n',
    '    case .acceptedClientWebProcessInterrupted: eventName = "accepted_client_web_process_interrupted"\n    case .acceptedClientStreamEndedWithoutTerminal: eventName = "accepted_client_stream_ended_without_terminal"\n    case .thinkingActive:\n',
)

replace_exact(
    root,
    '''        detailViewController.onManualLatestSyncApplied = { [weak self] id, _ in\n            guard let self, self.repository.selectedConversationID == id else { return }\n            if let snapshot = self.repository.liveResponse(for: id), snapshot.phase.isActive, !snapshot.promptText.isEmpty { return }\n            self.observeExternalResponseIfNeeded(conversationID: id, forcePageReload: true)\n        }\n''',
    '''        detailViewController.onManualLatestSyncApplied = { [weak self] id, _ in\n            guard let self, self.repository.selectedConversationID == id else { return }\n            if let snapshot = self.repository.liveResponse(for: id), !snapshot.phase.isActive, !snapshot.promptText.isEmpty {\n                let authoritativeVisibleMessageCount = self.repository.selectedConversation?.messages.count ?? 0\n                let cleared = self.repository.clearLiveResponseAfterAuthoritativeReconcile(conversationID: id, generation: snapshot.generation, authoritativeVisibleMessageCount: authoritativeVisibleMessageCount)\n                var fields = self.repository.diagnosticsFields(for: id)\n                fields["responseGeneration"] = String(snapshot.generation)\n                fields["authoritativeVisibleMessageCount"] = String(authoritativeVisibleMessageCount)\n                fields["liveSnapshotCleared"] = cleared ? "true" : "false"\n                self.diagnostics.info(category: "conversation", name: "manualSync.clientLiveReconciled", fields: fields)\n                if cleared { self.updateLivePresentation() }\n            }\n            if let snapshot = self.repository.liveResponse(for: id), snapshot.phase.isActive, !snapshot.promptText.isEmpty { return }\n            self.observeExternalResponseIfNeeded(conversationID: id, forcePageReload: true)\n        }\n''',
)

replace_exact(
    root,
    '''            case .acceptedClientWebProcessInterrupted:\n                guard let conversationID = authoritativeConversationID, let generation else { return }\n                self.releaseExecutor(for: conversationID, expected: sendExecutor)\n                var fields = self.repository.diagnosticsFields(for: conversationID)\n                fields["responseGeneration"] = String(generation)\n                fields["applicationState"] = UIApplication.shared.applicationState == .active ? "active" : "inactive_or_background"\n                self.diagnostics.warning(category: "webSend", name: "acceptedClientRecovery.interrupted", fields: fields)\n                if UIApplication.shared.applicationState == .active { self.recoverAcceptedClientResponse(conversationID: conversationID, generation: generation, trigger: "web_process_terminated") }\n            case .failed(let reason):\n''',
    '''            case .acceptedClientWebProcessInterrupted:\n                guard let conversationID = authoritativeConversationID, let generation else { return }\n                self.releaseExecutor(for: conversationID, expected: sendExecutor)\n                var fields = self.repository.diagnosticsFields(for: conversationID)\n                fields["responseGeneration"] = String(generation)\n                fields["applicationState"] = UIApplication.shared.applicationState == .active ? "active" : "inactive_or_background"\n                self.diagnostics.warning(category: "webSend", name: "acceptedClientRecovery.interrupted", fields: fields)\n                if UIApplication.shared.applicationState == .active { self.recoverAcceptedClientResponse(conversationID: conversationID, generation: generation, trigger: "web_process_terminated") }\n            case .acceptedClientStreamEndedWithoutTerminal:\n                guard let conversationID = authoritativeConversationID, let generation else { return }\n                self.releaseExecutor(for: conversationID, expected: sendExecutor)\n                var fields = self.repository.diagnosticsFields(for: conversationID)\n                fields["responseGeneration"] = String(generation)\n                fields["applicationState"] = UIApplication.shared.applicationState == .active ? "active" : "inactive_or_background"\n                fields["trigger"] = "stream_ended_without_done"\n                self.diagnostics.warning(category: "webSend", name: "acceptedClientRecovery.interrupted", fields: fields)\n                if UIApplication.shared.applicationState == .active { self.recoverAcceptedClientResponse(conversationID: conversationID, generation: generation, trigger: "stream_ended_without_done") }\n            case .failed(let reason):\n''',
)

replace_exact(
    root,
    '''            if case .acceptedClientWebProcessInterrupted = event {\n                self.releaseExecutor(for: conversationID, expected: sendExecutor)\n                var fields = self.repository.diagnosticsFields(for: conversationID)\n                fields["responseGeneration"] = String(generation)\n                fields["applicationState"] = UIApplication.shared.applicationState == .active ? "active" : "inactive_or_background"\n                self.diagnostics.warning(category: "webSend", name: "acceptedClientRecovery.interrupted", fields: fields)\n                if UIApplication.shared.applicationState == .active { self.recoverAcceptedClientResponse(conversationID: conversationID, generation: generation, trigger: "web_process_terminated") }\n                return\n            }\n            self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation)\n''',
    '''            if case .acceptedClientWebProcessInterrupted = event {\n                self.releaseExecutor(for: conversationID, expected: sendExecutor)\n                var fields = self.repository.diagnosticsFields(for: conversationID)\n                fields["responseGeneration"] = String(generation)\n                fields["applicationState"] = UIApplication.shared.applicationState == .active ? "active" : "inactive_or_background"\n                self.diagnostics.warning(category: "webSend", name: "acceptedClientRecovery.interrupted", fields: fields)\n                if UIApplication.shared.applicationState == .active { self.recoverAcceptedClientResponse(conversationID: conversationID, generation: generation, trigger: "web_process_terminated") }\n                return\n            }\n            if case .acceptedClientStreamEndedWithoutTerminal = event {\n                self.releaseExecutor(for: conversationID, expected: sendExecutor)\n                var fields = self.repository.diagnosticsFields(for: conversationID)\n                fields["responseGeneration"] = String(generation)\n                fields["applicationState"] = UIApplication.shared.applicationState == .active ? "active" : "inactive_or_background"\n                fields["trigger"] = "stream_ended_without_done"\n                self.diagnostics.warning(category: "webSend", name: "acceptedClientRecovery.interrupted", fields: fields)\n                if UIApplication.shared.applicationState == .active { self.recoverAcceptedClientResponse(conversationID: conversationID, generation: generation, trigger: "stream_ended_without_done") }\n                return\n            }\n            self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation)\n''',
)

print("b107 product patch prepared")
