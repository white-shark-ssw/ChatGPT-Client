from pathlib import Path
import re

ROOT = Path("ChatGPTClient/RootViewController.swift")
CONVERSATION = Path("ChatGPTClient/Conversation/ConversationFeature.swift")
PROJECT = Path("ChatGPTClient.xcodeproj/project.pbxproj")


def once(path: Path, old: str, new: str) -> None:
    text = path.read_text()
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected one exact match, found {count}: {old[:160]!r}")
    path.write_text(text.replace(old, new, 1))


def regex_once(path: Path, pattern: str, replacement: str) -> None:
    text = path.read_text()
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f"{path}: expected one regex match, found {count}: {pattern[:160]!r}")
    path.write_text(updated)


def exact_count(path: Path, old: str, new: str, expected: int) -> None:
    text = path.read_text()
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{path}: expected {expected} matches for {old!r}, found {count}")
    path.write_text(text.replace(old, new))


once(
    ROOT,
    """enum CoveredWebSendEvent {
    case externalResumeObserved
    case composerReady""",
    """enum CoveredWebSendEvent {
    case externalResumeObserved
    case externalStreamingObserved
    case externalConversationSnapshot(messages: [[String: Any]], complete: Bool)
    case composerReady""",
)

once(
    ROOT,
    """    private var observationEvents: ((CoveredWebSendEvent) -> Void)?
    private var activeEvents: ((CoveredWebSendEvent) -> Void)?
    private var responseActive = false""",
    """    private var observationEvents: ((CoveredWebSendEvent) -> Void)?
    private var activeEvents: ((CoveredWebSendEvent) -> Void)?
    private var responseActive = false
    private var observingExternalResponse = false""",
)

once(
    ROOT,
    """        observationEvents = events
        if currentConversationID == conversationID {""",
    """        observationEvents = events
        observingExternalResponse = true
        if currentConversationID == conversationID {""",
)

once(
    ROOT,
    """        pendingSend = PendingSend(conversationID: conversationID, text: trimmed, events: events)
        activeEvents = events""",
    """        observingExternalResponse = false
        pendingSend = PendingSend(conversationID: conversationID, text: trimmed, events: events)
        activeEvents = events""",
)

once(
    ROOT,
    """        responseActive = false
        currentConversationID = nil""",
    """        responseActive = false
        observingExternalResponse = false
        currentConversationID = nil""",
)

regex_once(
    ROOT,
    r'''        case "external_resume_observed":\n.*?        case "composer_state":''',
    '''        case "external_resume_observed":
            guard observingExternalResponse else { return }
            observationEvents?(.externalResumeObserved)
            diagnostics.info(category: "webSend", name: "coveredExecutor.externalResumeObserved", fields: ["target": "existing_conversation"])
        case "external_streaming":
            guard observingExternalResponse else { return }
            if activeEvents == nil { activeEvents = observationEvents }
            activeEvents?(.externalStreamingObserved)
            diagnostics.info(category: "webSend", name: "coveredExecutor.externalStreamingObserved", fields: ["target": "existing_conversation"])
        case "external_snapshot":
            guard observingExternalResponse, let messages = body["messages"] as? [[String: Any]] else { return }
            if activeEvents == nil { activeEvents = observationEvents }
            let complete = (body["complete"] as? NSNumber)?.boolValue ?? false
            activeEvents?(.externalConversationSnapshot(messages: messages, complete: complete))
            diagnostics.info(category: "webSend", name: "coveredExecutor.externalSnapshot", fields: ["serviceMessageCount": String(messages.count), "complete": complete ? "true" : "false"])
        case "resume_response":
            let status = (body["status"] as? NSNumber)?.intValue ?? 0
            let contentType = body["contentType"] as? String ?? ""
            diagnostics.info(category: "webSend", name: "coveredExecutor.resumeResponse", fields: ["httpStatus": String(status), "contentType": Self.safeToken(contentType)])
            if status == 200 && contentType == "text/event-stream" {
                if activeEvents == nil, observingExternalResponse { activeEvents = observationEvents }
                responseActive = true
                activeEvents?(.responseAccepted)
            } else if activeEvents != nil, !observingExternalResponse {
                failCurrent("resume_not_sse")
            } else if observingExternalResponse {
                diagnostics.info(category: "webSend", name: "coveredExecutor.resumeFallback", fields: ["state": "page_owned_read_path", "httpStatus": String(status)])
            }
        case "composer_state":''',
)

once(
    ROOT,
    """      let activeSend = false;
      let lastComposer = null;""",
    """      let activeSend = false;
      let lastComposer = null;
      const externalStreamingState = { active: false, completePending: false, resumeSSE: false };""",
)

regex_once(
    ROOT,
    r'''        const chatHost = !!url && isChatGPTHost\(url\.hostname\.toLowerCase\(\)\);\n        const isSend = chatHost && url\.pathname === '/backend-api/f/conversation';\n        const isResume = chatHost && url\.pathname === '/backend-api/f/conversation/resume';\n.*?        if \(!isSend \|\| !activeSend\) return originalFetch\(input, init\);''',
    '''        const chatHost = !!url && isChatGPTHost(url.hostname.toLowerCase());
        const method = String(init && init.method || input && input.method || 'GET').toUpperCase();
        const pageConversationID = currentConversationID();
        const isSend = chatHost && url.pathname === '/backend-api/f/conversation';
        const isResume = chatHost && url.pathname === '/backend-api/f/conversation/resume';
        const streamStatusMatch = chatHost ? url.pathname.match(/^\\/backend-api\\/conversation\\/([^/]+)\\/stream_status$/) : null;
        const pluralConversationMatch = chatHost ? url.pathname.match(/^\\/backend-api\\/conversations\\/([^/]+)$/) : null;
        const decodedPathID = match => {
          if (!match) return null;
          try { return decodeURIComponent(match[1]); } catch (_) { return null; }
        };
        const isStreamStatus = !activeSend && method === 'GET' && pageConversationID && decodedPathID(streamStatusMatch) === pageConversationID;
        const isPluralConversation = !activeSend && method === 'GET' && pageConversationID && decodedPathID(pluralConversationMatch) === pageConversationID;
        if (isResume) {
          let resumeConversationID = null;
          if (init && typeof init.body === 'string') {
            try {
              const resumeBody = JSON.parse(init.body);
              if (resumeBody && typeof resumeBody === 'object' && !Array.isArray(resumeBody) && typeof resumeBody.conversation_id === 'string') resumeConversationID = resumeBody.conversation_id;
            } catch (_) {}
          }
          if (resumeConversationID && resumeConversationID === pageConversationID) {
            post({ kind: 'external_resume_observed' });
            try {
              const response = await originalFetch(input, init);
              const contentType = String(response.headers.get('content-type') || '').split(';')[0].trim().toLowerCase();
              post({ kind: 'resume_response', status: response.status, contentType });
              if (response.status === 200 && contentType === 'text/event-stream') {
                externalStreamingState.resumeSSE = true;
                observedResponse(response);
              }
              return response;
            } catch (error) {
              post({ kind: 'stream_error', state: 'resume_transport_error' });
              throw error;
            }
          }
        }
        if (isStreamStatus && !externalStreamingState.resumeSSE) {
          const response = await originalFetch(input, init);
          if (response.status === 200) {
            try {
              const payload = await response.clone().json();
              if (payload && payload.status === 'IS_STREAMING') {
                externalStreamingState.completePending = false;
                if (!externalStreamingState.active) {
                  externalStreamingState.active = true;
                  post({ kind: 'external_streaming' });
                }
              } else if (payload && payload.status === 'COMPLETE' && externalStreamingState.active) {
                externalStreamingState.completePending = true;
              }
            } catch (_) {}
          }
          return response;
        }
        if (isPluralConversation && !externalStreamingState.resumeSSE) {
          const response = await originalFetch(input, init);
          if (response.status === 200 && (externalStreamingState.active || externalStreamingState.completePending)) {
            try {
              const payload = await response.clone().json();
              if (payload && payload.conversation_id === pageConversationID && Array.isArray(payload.messages)) {
                let latestUserIndex = -1;
                for (let index = 0; index < payload.messages.length; index += 1) {
                  const serviceMessage = payload.messages[index];
                  if (serviceMessage && serviceMessage.author && serviceMessage.author.role === 'user') latestUserIndex = index;
                }
                if (latestUserIndex >= 0) {
                  const serviceMessages = payload.messages.slice(latestUserIndex + 1);
                  post({ kind: 'external_snapshot', complete: externalStreamingState.completePending, messages: serviceMessages });
                  if (externalStreamingState.completePending) {
                    externalStreamingState.active = false;
                    externalStreamingState.completePending = false;
                  }
                }
              }
            } catch (_) {}
          }
          return response;
        }
        if (!isSend || !activeSend) return originalFetch(input, init);''',
)

once(ROOT, '        fields["source"] = "external_resume"', '        fields["source"] = "external_page_owned"')

projection_code = r'''    private struct ExternalPageProjection {
        let timeline: [ConversationResponseTimelineItem]
        let finalText: String
        let reasoningEnded: Bool
        let reasoningDurationSeconds: Int?
        let hasFinalMessage: Bool
    }

    private static func externalPageVisibleText(_ content: [String: Any]) -> String {
        var parts: [String] = []
        if let text = content["text"] as? String, !text.isEmpty { parts.append(text) }
        if let values = content["parts"] as? [Any] {
            for value in values {
                if let text = value as? String, !text.isEmpty { parts.append(text) }
                else if let object = value as? [String: Any], let text = object["text"] as? String, !text.isEmpty { parts.append(text) }
            }
        }
        return parts.joined(separator: "\n").trimmingCharacters(in: .whitespacesAndNewlines)
    }

    private static func projectExternalPageMessages(_ rawMessages: [[String: Any]]) -> ExternalPageProjection {
        var timeline: [ConversationResponseTimelineItem] = []
        var finalText = ""
        var reasoningEnded = false
        var reasoningDurationSeconds: Int?
        var hasFinalMessage = false
        var toolIndexByServiceID: [String: Int] = [:]
        var toolRecipientByServiceID: [String: String] = [:]
        var toolInputByServiceID: [String: String] = [:]

        for message in rawMessages {
            guard let author = message["author"] as? [String: Any], let rawRole = author["role"] as? String else { continue }
            let metadata = message["metadata"] as? [String: Any]
            if rawRole == "tool" {
                if message["status"] as? String == "finished_successfully", message["recipient"] as? String == "all", let parentID = metadata?["parent_id"] as? String, let index = toolIndexByServiceID[parentID], timeline.indices.contains(index), timeline[index].kind == .tool {
                    timeline[index].completed = true
                    if toolRecipientByServiceID[parentID] == "api_tool.call_tool", let inputJSON = toolInputByServiceID[parentID], !inputJSON.isEmpty, let invokedResource = metadata?["invoked_resource"] as? [String: Any], invokedResource["app_name"] as? String == "GitHub", let resultContent = message["content"] as? [String: Any], JSONSerialization.isValidJSONObject(resultContent), let data = try? JSONSerialization.data(withJSONObject: resultContent), let outputJSON = String(data: data, encoding: .utf8) {
                        timeline[index].toolInputJSON = inputJSON
                        timeline[index].toolOutputJSON = outputJSON
                        timeline[index].toolIconKind = .github
                    }
                }
                continue
            }
            guard rawRole == "assistant", let content = message["content"] as? [String: Any] else { continue }
            if let recipient = message["recipient"] as? String {
                let normalizedRecipient = recipient.trimmingCharacters(in: .whitespacesAndNewlines)
                if !normalizedRecipient.isEmpty, normalizedRecipient != "all" {
                    if message["status"] as? String == "finished_successfully", content["content_type"] as? String == "code", (metadata?["is_complete"] as? Bool) == true {
                        let rawTitle = (metadata?["reasoning_title"] as? String)?.trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
                        let title = rawTitle.isEmpty ? "工具调用" : String(rawTitle.prefix(160))
                        let slot = timeline.count
                        let iconKind: ConversationToolIconKind = normalizedRecipient == "api_tool.call_tool" ? .connector : .code
                        timeline.append(.tool(slot: slot, title: title, completed: false, iconKind: iconKind))
                        if let serviceID = message["id"] as? String, !serviceID.isEmpty {
                            toolIndexByServiceID[serviceID] = timeline.count - 1
                            toolRecipientByServiceID[serviceID] = normalizedRecipient
                            if normalizedRecipient == "api_tool.call_tool", let connectorPayload = metadata?["connector_tool_payload"] as? String, !connectorPayload.isEmpty { toolInputByServiceID[serviceID] = connectorPayload }
                        }
                    }
                    continue
                }
            }
            if content["content_type"] as? String == "reasoning_recap", message["status"] as? String == "finished_successfully", let summary = content["content"] as? String, let metadata, metadata["reasoning_status"] as? String == "reasoning_ended", metadata["reasoning_recap_type"] as? String == "collapse" {
                let normalized = summary.trimmingCharacters(in: .whitespacesAndNewlines)
                if !normalized.isEmpty, !timeline.contains(where: { $0.kind == .reasoning }) { timeline.append(.reasoning(normalized)) }
                reasoningEnded = true
                if let duration = metadata["finished_duration_sec"] as? NSNumber {
                    let seconds = Int(duration.doubleValue.rounded())
                    if seconds >= 0 { reasoningDurationSeconds = seconds }
                }
                continue
            }
            if (metadata?["is_thinking_preamble_message"] as? Bool) == true {
                let reasoning = externalPageVisibleText(content)
                if !reasoning.isEmpty { timeline.append(.reasoning(reasoning)) }
                continue
            }
            if let contentType = content["content_type"] as? String, contentType == "thoughts" || contentType == "inline_cot_expandable_content" { continue }
            if content["content_type"] as? String == "text" {
                hasFinalMessage = true
                finalText = externalPageVisibleText(content)
            }
        }
        return ExternalPageProjection(timeline: timeline, finalText: finalText, reasoningEnded: reasoningEnded, reasoningDurationSeconds: reasoningDurationSeconds, hasFinalMessage: hasFinalMessage)
    }

    func consumeExternalConversationSnapshot(_ serviceMessages: [[String: Any]], conversationID: String, generation: Int) {
        precondition(Thread.isMainThread)
        guard var snapshot = responseRuntime.snapshots[conversationID], snapshot.generation == generation, snapshot.phase.isActive else {
            var fields = diagnosticsFields(for: conversationID)
            fields["responseGeneration"] = String(generation)
            fields["reason"] = "generation_mismatch_missing_or_terminal"
            DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.externalSnapshotDiscarded", fields: fields)
            return
        }
        let projection = Self.projectExternalPageMessages(serviceMessages)
        let nextPhase: ConversationLiveResponsePhase
        if projection.hasFinalMessage || projection.reasoningEnded { nextPhase = .final }
        else if !projection.timeline.isEmpty { nextPhase = .reasoning }
        else { nextPhase = .thinking }
        let changed = snapshot.phase != nextPhase || snapshot.timeline != projection.timeline || snapshot.finalText != projection.finalText || snapshot.reasoningEnded != projection.reasoningEnded || snapshot.reasoningDurationSeconds != projection.reasoningDurationSeconds
        snapshot.phase = nextPhase
        snapshot.timeline = projection.timeline
        snapshot.finalText = projection.finalText
        snapshot.reasoningEnded = projection.reasoningEnded
        snapshot.reasoningDurationSeconds = projection.reasoningDurationSeconds
        snapshot.failureReason = nil
        responseRuntime.snapshots[conversationID] = snapshot
        var fields = diagnosticsFields(for: conversationID)
        fields["responseGeneration"] = String(generation)
        fields["serviceMessageCount"] = String(serviceMessages.count)
        fields["phase"] = snapshot.phase.rawValue
        fields["changed"] = changed ? "true" : "false"
        fields["reasoningCharacters"] = String(snapshot.timeline.filter { $0.kind == .reasoning }.reduce(0) { $0 + $1.text.count })
        fields["finalCharacters"] = String(snapshot.finalText.count)
        fields["toolCount"] = String(snapshot.timeline.filter { $0.kind == .tool }.count)
        DiagnosticsLogger.shared.info(category: "conversation", name: "liveResponse.externalSnapshot", fields: fields)
        if changed { responseRuntime.onChange?(conversationID) }
    }

'''
once(ROOT, "    func consumeLiveResponseEvent(_ event: CoveredWebSendEvent, conversationID: String, generation: Int) {", projection_code + "    func consumeLiveResponseEvent(_ event: CoveredWebSendEvent, conversationID: String, generation: Int) {")

once(
    ROOT,
    '''    case .externalResumeObserved: eventName = "external_resume_observed"
    case .composerReady:''',
    '''    case .externalResumeObserved: eventName = "external_resume_observed"
    case .externalStreamingObserved: eventName = "external_streaming_observed"
    case .externalConversationSnapshot(_, _): eventName = "external_conversation_snapshot"
    case .composerReady:''',
)

regex_once(
    ROOT,
    r'''    private func observeExternalResponseIfNeeded\(conversationID: String\) \{\n.*?\n    \}\n\n    private func startValidationSend''',
    '''    private func observeExternalResponseIfNeeded(conversationID: String) {
        guard repository.selectedConversationID == conversationID, !repository.isLiveResponseActive(for: conversationID) else { return }
        let sendExecutor = executor(for: conversationID)
        var externalGeneration: Int?
        sendExecutor.observeExistingConversation(conversationID: conversationID) { [weak self, weak sendExecutor] event in
            guard let self, let sendExecutor else { return }
            func ensureGeneration() -> Int? {
                if let externalGeneration { return externalGeneration }
                guard !self.repository.isLiveResponseActive(for: conversationID) else {
                    self.releaseExecutor(for: conversationID, expected: sendExecutor)
                    return nil
                }
                switch self.repository.beginExternalLiveResponse(conversationID: conversationID) {
                case .success(let generation):
                    externalGeneration = generation
                    self.updateLivePresentation()
                    return generation
                case .failure:
                    self.releaseExecutor(for: conversationID, expected: sendExecutor)
                    return nil
                }
            }
            switch event {
            case .externalResumeObserved:
                return
            case .externalStreamingObserved:
                guard let generation = ensureGeneration() else { return }
                self.repository.consumeLiveResponseEvent(.thinkingActive, conversationID: conversationID, generation: generation)
            case .externalConversationSnapshot(let messages, let complete):
                guard let generation = ensureGeneration() else { return }
                self.repository.consumeExternalConversationSnapshot(messages, conversationID: conversationID, generation: generation)
                if complete {
                    self.repository.consumeLiveResponseEvent(.terminal, conversationID: conversationID, generation: generation)
                    self.releaseExecutor(for: conversationID, expected: sendExecutor)
                    self.reconcileTerminalResponse(conversationID: conversationID, generation: generation)
                }
            case .responseAccepted:
                guard let generation = ensureGeneration() else { return }
                self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation)
            case .terminal:
                guard let generation = externalGeneration else {
                    self.releaseExecutor(for: conversationID, expected: sendExecutor)
                    return
                }
                self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation)
                self.releaseExecutor(for: conversationID, expected: sendExecutor)
                self.reconcileTerminalResponse(conversationID: conversationID, generation: generation)
            case .failed:
                if let generation = externalGeneration { self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation) }
                self.releaseExecutor(for: conversationID, expected: sendExecutor)
            default:
                guard let generation = externalGeneration else { return }
                self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation)
            }
        }
    }

    private func startValidationSend''',
)

once(ROOT, "        pendingSend = nil\n        responseActive = false\n        activeEvents = nil", "        pendingSend = nil\n        responseActive = false\n        observingExternalResponse = false\n        activeEvents = nil")

once(CONVERSATION, "    private static let toolLineHeight: CGFloat = 26", "    private static let toolLineHeight: CGFloat = 30")
exact_count(PROJECT, "CURRENT_PROJECT_VERSION = 75;", "CURRENT_PROJECT_VERSION = 76;", 2)
exact_count(PROJECT, 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b75";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b76";', 2)
