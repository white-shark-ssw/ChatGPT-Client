from pathlib import Path

root_path = Path("ChatGPTClient/RootViewController.swift")
project_path = Path("ChatGPTClient.xcodeproj/project.pbxproj")
root = root_path.read_text()
project = project_path.read_text()

if 'CURRENT_PROJECT_VERSION = 86;' in project and 'DEV-send-stream-0.1.0-b86' in project:
    print('b86 identity already staged; no-op')
    raise SystemExit(0)

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 match, got {count}')
    return text.replace(old, new, 1)

root = replace_once(root, '''        switch kind {
        case "external_resume_observed":''', '''        switch kind {
        case "external_stream_status_request":
            guard observingExternalResponse else { return }
            diagnostics.info(category: "webSend", name: "coveredExecutor.externalStreamStatusRequest", fields: ["target": "existing_conversation"])
        case "external_stream_status_response":
            guard observingExternalResponse else { return }
            let status = (body["status"] as? NSNumber)?.intValue ?? 0
            let streamState = Self.safeToken(body["streamState"] as? String ?? "")
            diagnostics.info(category: "webSend", name: "coveredExecutor.externalStreamStatusResponse", fields: ["httpStatus": String(status), "streamState": streamState])
        case "external_resume_request":
            guard observingExternalResponse else { return }
            let hasOffset = (body["hasOffset"] as? NSNumber)?.boolValue ?? false
            let offsetType = Self.safeToken(body["offsetType"] as? String ?? "missing")
            let offsetValue = (body["offsetValue"] as? NSNumber)?.intValue ?? -1
            diagnostics.info(category: "webSend", name: "coveredExecutor.externalResumeRequest", fields: ["hasOffset": hasOffset ? "true" : "false", "offsetType": offsetType, "offsetValue": String(offsetValue)])
        case "external_resume_observed":''', 'Swift diagnostics cases')

root = replace_once(root, '''        if (isResume) {
          let resumeConversationID = null;
          if (init && typeof init.body === 'string') {
            try {
              const resumeBody = JSON.parse(init.body);
              if (resumeBody && typeof resumeBody === 'object' && !Array.isArray(resumeBody) && typeof resumeBody.conversation_id === 'string') resumeConversationID = resumeBody.conversation_id;
            } catch (_) {}
          }
          if (resumeConversationID && resumeConversationID === pageConversationID) {
            post({ kind: 'external_resume_observed' });''', '''        if (isResume) {
          let resumeConversationID = null;
          let resumeOffsetType = 'missing';
          let resumeOffsetValue = -1;
          if (init && typeof init.body === 'string') {
            try {
              const resumeBody = JSON.parse(init.body);
              if (resumeBody && typeof resumeBody === 'object' && !Array.isArray(resumeBody)) {
                if (typeof resumeBody.conversation_id === 'string') resumeConversationID = resumeBody.conversation_id;
                if (Object.prototype.hasOwnProperty.call(resumeBody, 'offset')) {
                  resumeOffsetType = typeof resumeBody.offset;
                  if (typeof resumeBody.offset === 'number' && Number.isSafeInteger(resumeBody.offset)) resumeOffsetValue = resumeBody.offset;
                  else if (typeof resumeBody.offset === 'string' && /^\\d+$/.test(resumeBody.offset)) resumeOffsetValue = Number(resumeBody.offset);
                }
              }
            } catch (_) {}
          }
          if (resumeConversationID && resumeConversationID === pageConversationID) {
            post({ kind: 'external_resume_request', hasOffset: resumeOffsetType !== 'missing', offsetType: resumeOffsetType, offsetValue: resumeOffsetValue });
            post({ kind: 'external_resume_observed' });''', 'resume request structure')

root = replace_once(root, '''        if (isStreamStatus && !externalStreamingState.resumeSSE) {
          const response = await originalFetch(input, init);
          if (response.status === 200) {
            try {
              const payload = await response.clone().json();
              if (payload && payload.status === 'IS_STREAMING') {
                externalStreamingState.completePending = false;
                if (!externalStreamingState.active) {
                  externalStreamingState.active = true;
                  lastExternalAssistantTextCharacters = -1;
                  post({ kind: 'external_streaming' });
                  reportExternalAssistantDOM();
                }
              } else if (payload && payload.status === 'COMPLETE' && externalStreamingState.active) {
                externalStreamingState.completePending = true;
              }
            } catch (_) {}
          }
          return response;''', '''        if (isStreamStatus && !externalStreamingState.resumeSSE) {
          post({ kind: 'external_stream_status_request' });
          const response = await originalFetch(input, init);
          let streamState = '';
          if (response.status === 200) {
            try {
              const payload = await response.clone().json();
              if (payload && typeof payload.status === 'string') streamState = payload.status;
              if (payload && payload.status === 'IS_STREAMING') {
                externalStreamingState.completePending = false;
                if (!externalStreamingState.active) {
                  externalStreamingState.active = true;
                  lastExternalAssistantTextCharacters = -1;
                  post({ kind: 'external_streaming' });
                  reportExternalAssistantDOM();
                }
              } else if (payload && payload.status === 'COMPLETE' && externalStreamingState.active) {
                externalStreamingState.completePending = true;
              }
            } catch (_) {}
          }
          post({ kind: 'external_stream_status_response', status: response.status, streamState });
          return response;''', 'stream status diagnostics')

for old, new, label in [
    ('CURRENT_PROJECT_VERSION = 85;', 'CURRENT_PROJECT_VERSION = 86;', 'build number'),
    ('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b85";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b86";', 'candidate')
]:
    count = project.count(old)
    if count != 2:
        raise SystemExit(f'{label}: expected 2 matches, got {count}')
    project = project.replace(old, new)

root_path.write_text(root)
project_path.write_text(project)
