from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


project = Path("ChatGPTClient.xcodeproj/project.pbxproj")
ptext = project.read_text()
if ptext.count("CURRENT_PROJECT_VERSION = 102;") != 2:
    raise SystemExit("unexpected Build102 count")
if ptext.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b102";') != 2:
    raise SystemExit("unexpected b102 candidate count")
ptext = ptext.replace("CURRENT_PROJECT_VERSION = 102;", "CURRENT_PROJECT_VERSION = 103;")
ptext = ptext.replace('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b102";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b103";')
project.write_text(ptext)

probe = Path("ChatGPTClient/Protocol/CoveredWebProcessKillProbe.swift")
probe_text = probe.read_text()
probe_text = replace_once(probe_text, 'private static let candidate = "DEV-send-stream-0.1.0-b102"', 'private static let candidate = "DEV-send-stream-0.1.0-b103"', "probe candidate")
probe_text = probe_text.replace("b102_evaluateJavaScript", "b103_evaluateJavaScript")
if "b102_evaluateJavaScript" in probe_text:
    raise SystemExit("stale b102 probe selector remains")
probe.write_text(probe_text)

source = Path("ChatGPTClient/RootViewController.swift")
text = source.read_text()

text = replace_once(
    text,
    '''    case sendObserved\n    case responseAccepted\n    case thinkingActive''',
    '''    case sendObserved\n    case responseAccepted\n    case acceptedClientWebProcessInterrupted\n    case thinkingActive''',
    "event enum",
)

text = replace_once(
    text,
    '''    private var activeEvents: ((CoveredWebSendEvent) -> Void)?\n    private var responseActive = false\n    private var observingExternalResponse = false\n    private var manualSyncFocusProbePending = false\n\n    var isBusy: Bool { activeEvents != nil }''',
    '''    private var activeEvents: ((CoveredWebSendEvent) -> Void)?\n    private var responseActive = false\n    private var clientSendAccepted = false\n    private var observingExternalResponse = false\n    private var manualSyncFocusProbePending = false\n\n    var isBusy: Bool { activeEvents != nil }''',
    "executor state",
)

text = replace_once(
    text,
    '''        manualSyncFocusProbePending = false\n        observingExternalResponse = false\n        pendingSend = PendingSend(conversationID: conversationID, text: trimmed, events: events)''',
    '''        manualSyncFocusProbePending = false\n        observingExternalResponse = false\n        clientSendAccepted = false\n        pendingSend = PendingSend(conversationID: conversationID, text: trimmed, events: events)''',
    "new send reset",
)

text = replace_once(
    text,
    '''        activeEvents = nil\n        responseActive = false\n        observingExternalResponse = false\n        manualSyncFocusProbePending = false''',
    '''        activeEvents = nil\n        responseActive = false\n        clientSendAccepted = false\n        observingExternalResponse = false\n        manualSyncFocusProbePending = false''',
    "account reset accepted state",
)

old_termination = '''    func webViewWebContentProcessDidTerminate(_ webView: WKWebView) {\n        manualSyncFocusProbePending = false\n        diagnostics.error(category: "webSend", name: "coveredExecutor.webProcess", fields: ["state": "terminated", "mode": observingExternalResponse ? "external_observation" : "client_send_or_idle"])\n        if observingExternalResponse {\n            composerReadyConversationID = nil\n            if UIApplication.shared.applicationState == .active {\n                diagnostics.warning(category: "webSend", name: "coveredExecutor.externalWebProcessRecovery", fields: ["state": "immediate_rebootstrap"])\n                rebootstrapExternalObservationPageOnForeground()\n            } else {\n                diagnostics.warning(category: "webSend", name: "coveredExecutor.externalWebProcessRecovery", fields: ["state": "deferred_to_foreground"])\n            }\n            return\n        }\n        failCurrent("web_process_terminated")\n    }'''
new_termination = '''    func webViewWebContentProcessDidTerminate(_ webView: WKWebView) {\n        manualSyncFocusProbePending = false\n        diagnostics.error(category: "webSend", name: "coveredExecutor.webProcess", fields: ["state": "terminated", "mode": observingExternalResponse ? "external_observation" : "client_send_or_idle"])\n        if observingExternalResponse {\n            composerReadyConversationID = nil\n            if UIApplication.shared.applicationState == .active {\n                diagnostics.warning(category: "webSend", name: "coveredExecutor.externalWebProcessRecovery", fields: ["state": "immediate_rebootstrap"])\n                rebootstrapExternalObservationPageOnForeground()\n            } else {\n                diagnostics.warning(category: "webSend", name: "coveredExecutor.externalWebProcessRecovery", fields: ["state": "deferred_to_foreground"])\n            }\n            return\n        }\n        if clientSendAccepted, responseActive, let interruptedEvents = activeEvents {\n            pendingSend = nil\n            responseActive = false\n            clientSendAccepted = false\n            activeEvents = nil\n            composerReadyConversationID = nil\n            let state = UIApplication.shared.applicationState == .active ? "handoff_requested" : "deferred_to_foreground"\n            diagnostics.warning(category: "webSend", name: "coveredExecutor.acceptedClientWebProcessRecovery", fields: ["state": state, "policy": "no_resend_same_generation"])\n            interruptedEvents(.acceptedClientWebProcessInterrupted)\n            return\n        }\n        failCurrent("web_process_terminated")\n    }'''
text = replace_once(text, old_termination, new_termination, "hard termination behavior")

text = replace_once(
    text,
    '''            diagnostics.info(category: "webSend", name: "coveredExecutor.sendResponse", fields: ["httpStatus": String(status), "contentType": Self.safeToken(contentType)])\n            if status == 200 && contentType == "text/event-stream" { activeEvents?(.responseAccepted) }\n            else { failCurrent("send_not_sse") }''',
    '''            diagnostics.info(category: "webSend", name: "coveredExecutor.sendResponse", fields: ["httpStatus": String(status), "contentType": Self.safeToken(contentType)])\n            if status == 200 && contentType == "text/event-stream" {\n                clientSendAccepted = true\n                activeEvents?(.responseAccepted)\n            } else { failCurrent("send_not_sse") }''',
    "send acceptance",
)

text = replace_once(
    text,
    '''        case "terminal":\n            let terminalEvents = activeEvents\n            responseActive = false\n            pendingSend = nil\n            activeEvents = nil''',
    '''        case "terminal":\n            let terminalEvents = activeEvents\n            responseActive = false\n            clientSendAccepted = false\n            pendingSend = nil\n            activeEvents = nil''',
    "terminal accepted reset",
)

text = replace_once(
    text,
    '''        pendingSend = nil\n        responseActive = false\n        observingExternalResponse = false\n        activeEvents = nil''',
    '''        pendingSend = nil\n        responseActive = false\n        clientSendAccepted = false\n        observingExternalResponse = false\n        activeEvents = nil''',
    "failure accepted reset",
)

text = replace_once(
    text,
    '''    case .sendObserved: eventName = "send_observed"\n    case .responseAccepted:\n        snapshot.phase = .thinking\n        eventName = "response_accepted"\n    case .thinkingActive:''',
    '''    case .sendObserved: eventName = "send_observed"\n    case .responseAccepted:\n        snapshot.phase = .thinking\n        eventName = "response_accepted"\n    case .acceptedClientWebProcessInterrupted: eventName = "accepted_client_web_process_interrupted"\n    case .thinkingActive:''',
    "repository event switch",
)

text = replace_once(
    text,
    '''        let snapshot = repository.liveResponse(for: conversationID)\n        if let snapshot, snapshot.phase.isActive, !snapshot.promptText.isEmpty { return }\n        let hadActiveExternalResponse = snapshot?.phase.isActive == true && snapshot?.promptText.isEmpty == true''',
    '''        let snapshot = repository.liveResponse(for: conversationID)\n        if let snapshot, snapshot.phase.isActive, !snapshot.promptText.isEmpty {\n            if sendExecutors[conversationID] == nil {\n                diagnostics.info(category: "webSend", name: "foregroundAcceptedClientRecovery.requested", fields: repository.diagnosticsFields(for: conversationID))\n                recoverAcceptedClientResponse(conversationID: conversationID, generation: snapshot.generation, trigger: "foreground")\n            }\n            return\n        }\n        let hadActiveExternalResponse = snapshot?.phase.isActive == true && snapshot?.promptText.isEmpty == true''',
    "foreground accepted recovery",
)

text = replace_once(
    text,
    '''    private func observeExternalResponseIfNeeded(conversationID: String, forcePageReload: Bool = false) {\n        guard repository.selectedConversationID == conversationID else { return }\n        let existingSnapshot = repository.liveResponse(for: conversationID)\n        guard existingSnapshot?.phase.isActive != true || existingSnapshot?.promptText.isEmpty == true else { return }\n        let sendExecutor = executor(for: conversationID)\n        var externalGeneration: Int? = existingSnapshot?.phase.isActive == true ? existingSnapshot?.generation : nil''',
    '''    private func observeExternalResponseIfNeeded(conversationID: String, forcePageReload: Bool = false, preservedClientGeneration: Int? = nil) {\n        guard repository.selectedConversationID == conversationID else { return }\n        let existingSnapshot = repository.liveResponse(for: conversationID)\n        if let preservedClientGeneration {\n            guard let existingSnapshot, existingSnapshot.phase.isActive, !existingSnapshot.promptText.isEmpty, existingSnapshot.generation == preservedClientGeneration else { return }\n        } else {\n            guard existingSnapshot?.phase.isActive != true || existingSnapshot?.promptText.isEmpty == true else { return }\n        }\n        let sendExecutor = executor(for: conversationID)\n        var externalGeneration: Int? = preservedClientGeneration ?? (existingSnapshot?.phase.isActive == true ? existingSnapshot?.generation : nil)''',
    "observer preserved generation",
)

marker = '''    private func startValidationSend(text: String, conversationID: String) {'''
helper = '''    private func recoverAcceptedClientResponse(conversationID: String, generation: Int, trigger: String) {\n        guard repository.selectedConversationID == conversationID, sendExecutors[conversationID] == nil else {\n            diagnostics.info(category: "webSend", name: "acceptedClientRecovery.skipped", fields: ["reason": "selection_or_executor_state", "trigger": trigger])\n            return\n        }\n        guard let snapshot = repository.liveResponse(for: conversationID), snapshot.phase.isActive, !snapshot.promptText.isEmpty, snapshot.generation == generation else {\n            diagnostics.info(category: "webSend", name: "acceptedClientRecovery.skipped", fields: ["reason": "live_generation_not_active", "trigger": trigger])\n            return\n        }\n        var fields = repository.diagnosticsFields(for: conversationID)\n        fields["responseGeneration"] = String(generation)\n        fields["trigger"] = trigger\n        fields["policy"] = "fresh_observer_no_resend"\n        diagnostics.info(category: "webSend", name: "acceptedClientRecovery.started", fields: fields)\n        observeExternalResponseIfNeeded(conversationID: conversationID, forcePageReload: true, preservedClientGeneration: generation)\n    }\n\n'''
text = replace_once(text, marker, helper + marker, "accepted recovery helper")

old_send_closure = '''        sendExecutor.sendExistingConversation(text: trimmed, conversationID: conversationID) { [weak self, weak sendExecutor] event in\n            guard let self, let sendExecutor else { return }\n            self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation)\n            switch event {\n            case .terminal:\n                self.releaseExecutor(for: conversationID, expected: sendExecutor)\n                self.reconcileTerminalResponse(conversationID: conversationID, generation: generation)\n            case .failed:\n                self.releaseExecutor(for: conversationID, expected: sendExecutor)\n            default: break\n            }\n        }'''
new_send_closure = '''        sendExecutor.sendExistingConversation(text: trimmed, conversationID: conversationID) { [weak self, weak sendExecutor] event in\n            guard let self, let sendExecutor else { return }\n            if case .acceptedClientWebProcessInterrupted = event {\n                self.releaseExecutor(for: conversationID, expected: sendExecutor)\n                var fields = self.repository.diagnosticsFields(for: conversationID)\n                fields["responseGeneration"] = String(generation)\n                fields["applicationState"] = UIApplication.shared.applicationState == .active ? "active" : "inactive_or_background"\n                self.diagnostics.warning(category: "webSend", name: "acceptedClientRecovery.interrupted", fields: fields)\n                if UIApplication.shared.applicationState == .active { self.recoverAcceptedClientResponse(conversationID: conversationID, generation: generation, trigger: "web_process_terminated") }\n                return\n            }\n            self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation)\n            switch event {\n            case .terminal:\n                self.releaseExecutor(for: conversationID, expected: sendExecutor)\n                self.reconcileTerminalResponse(conversationID: conversationID, generation: generation)\n            case .failed:\n                self.releaseExecutor(for: conversationID, expected: sendExecutor)\n            default: break\n            }\n        }'''
text = replace_once(text, old_send_closure, new_send_closure, "client send event closure")

source.write_text(text)
