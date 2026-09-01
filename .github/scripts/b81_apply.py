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
    '''        case "external_dom_structure":
            guard observingExternalResponse else { return }
            let assistantNodeCount = (body["assistantNodeCount"] as? NSNumber)?.intValue ?? 0
            let textCharacters = (body["textCharacters"] as? NSNumber)?.intValue ?? 0
            diagnostics.info(category: "webSend", name: "coveredExecutor.externalDOMStructure", fields: ["assistantNodeCount": String(assistantNodeCount), "textCharacters": String(textCharacters)])
        case "resume_response":''',
    '''        case "external_dom_structure":
            guard observingExternalResponse else { return }
            let assistantNodeCount = (body["assistantNodeCount"] as? NSNumber)?.intValue ?? 0
            let textCharacters = (body["textCharacters"] as? NSNumber)?.intValue ?? 0
            diagnostics.info(category: "webSend", name: "coveredExecutor.externalDOMStructure", fields: ["assistantNodeCount": String(assistantNodeCount), "textCharacters": String(textCharacters)])
        case "websocket_structure":
            guard observingExternalResponse else { return }
            let state = Self.safeToken(body["state"] as? String ?? "unknown")
            let host = Self.safeToken(body["host"] as? String ?? "")
            let path = Self.safeToken(body["path"] as? String ?? "")
            let dataType = Self.safeToken(body["dataType"] as? String ?? "none")
            let topKeys = Self.safeToken(body["topKeys"] as? String ?? "")
            let nestedKeys = Self.safeToken(body["nestedKeys"] as? String ?? "")
            let typeToken = Self.safeToken(body["typeToken"] as? String ?? "")
            let eventToken = Self.safeToken(body["eventToken"] as? String ?? "")
            let kindToken = Self.safeToken(body["kindToken"] as? String ?? "")
            let actionToken = Self.safeToken(body["actionToken"] as? String ?? "")
            let topicToken = Self.safeToken(body["topicToken"] as? String ?? "")
            let nameToken = Self.safeToken(body["nameToken"] as? String ?? "")
            let length = (body["length"] as? NSNumber)?.intValue ?? 0
            let hasConversationKey = (body["hasConversationKey"] as? NSNumber)?.boolValue ?? false
            let targetMatch = (body["targetMatch"] as? NSNumber)?.boolValue ?? false
            diagnostics.info(category: "webSend", name: "coveredExecutor.webSocketStructure", fields: ["state": state, "host": host, "path": path, "dataType": dataType, "length": String(length), "topKeys": topKeys, "nestedKeys": nestedKeys, "typeToken": typeToken, "eventToken": eventToken, "kindToken": kindToken, "actionToken": actionToken, "topicToken": topicToken, "nameToken": nameToken, "hasConversationKey": hasConversationKey ? "true" : "false", "targetMatch": targetMatch ? "true" : "false"])
        case "resume_response":'''
)

replace_exact(
    root,
    '''      const currentConversationID = () => {
        const match = location.pathname.match(/^\\/c\\/([^/?#]+)/);
        return match ? decodeURIComponent(match[1]) : null;
      };
      const isChatGPTHost = host => host === 'chatgpt.com' || host.endsWith('.chatgpt.com');
      const installRenderSuppression = () => {''',
    '''      const currentConversationID = () => {
        const match = location.pathname.match(/^\\/c\\/([^/?#]+)/);
        return match ? decodeURIComponent(match[1]) : null;
      };
      const isChatGPTHost = host => host === 'chatgpt.com' || host.endsWith('.chatgpt.com');
      const safeStructureToken = value => typeof value === 'string' && value.length <= 64 && /^[A-Za-z][A-Za-z0-9_.:/-]{0,63}$/.test(value) ? value : '';
      const scrubSocketPath = value => String(value || '').split('/').map(segment => /^[A-Za-z0-9_-]{20,}$/.test(segment) ? '{id}' : segment).join('/').slice(0, 150);
      const containsExactTarget = value => {
        const target = currentConversationID();
        if (!target) return false;
        const visit = (node, depth) => {
          if (depth > 5) return false;
          if (typeof node === 'string') return node === target;
          if (Array.isArray(node)) return node.slice(0, 40).some(item => visit(item, depth + 1));
          if (!node || typeof node !== 'object') return false;
          return Object.values(node).slice(0, 40).some(item => visit(item, depth + 1));
        };
        return visit(value, 0);
      };
      const socketFrameShape = data => {
        let dataType = typeof data;
        let length = 0;
        let parsed = null;
        if (typeof data === 'string') {
          dataType = 'string';
          length = data.length;
          if (length <= 65536) { try { parsed = JSON.parse(data); } catch (_) {} }
        } else if (data instanceof ArrayBuffer) {
          dataType = 'arraybuffer';
          length = data.byteLength;
        } else if (ArrayBuffer.isView(data)) {
          dataType = 'typed_array';
          length = data.byteLength;
        } else if (typeof Blob !== 'undefined' && data instanceof Blob) {
          dataType = 'blob';
          length = data.size;
        }
        if (!parsed || typeof parsed !== 'object') return { dataType, length, topKeys: '', nestedKeys: '', typeToken: '', eventToken: '', kindToken: '', actionToken: '', topicToken: '', nameToken: '', hasConversationKey: false, targetMatch: false };
        const topKeysArray = Array.isArray(parsed) ? [] : Object.keys(parsed).sort().slice(0, 24);
        const nested = [];
        if (!Array.isArray(parsed)) {
          for (const key of ['payload', 'data', 'body', 'message', 'detail']) {
            const value = parsed[key];
            if (value && typeof value === 'object' && !Array.isArray(value)) nested.push(...Object.keys(value));
          }
        }
        const nestedKeysArray = [...new Set(nested)].sort().slice(0, 24);
        const hasConversationKey = [...topKeysArray, ...nestedKeysArray].some(key => key === 'conversation_id' || key === 'conversationId' || key === 'conversation');
        const token = key => !Array.isArray(parsed) ? safeStructureToken(parsed[key]) : '';
        return { dataType: Array.isArray(parsed) ? 'json_array' : 'json_object', length, topKeys: topKeysArray.join(',').slice(0, 150), nestedKeys: nestedKeysArray.join(',').slice(0, 150), typeToken: token('type'), eventToken: token('event'), kindToken: token('kind'), actionToken: token('action'), topicToken: token('topic'), nameToken: token('name'), hasConversationKey, targetMatch: containsExactTarget(parsed) };
      };
      const NativeWebSocket = window.WebSocket;
      if (NativeWebSocket) {
        let structuralMessageBudget = 200;
        window.WebSocket = new Proxy(NativeWebSocket, {
          construct(target, args) {
            const socket = Reflect.construct(target, args, target);
            let parsedURL = null;
            try { parsedURL = new URL(String(args[0] || ''), location.href); } catch (_) {}
            const host = parsedURL ? parsedURL.hostname.toLowerCase() : '';
            const path = parsedURL ? scrubSocketPath(parsedURL.pathname) : '';
            const interesting = host === 'ws.chatgpt.com' || isChatGPTHost(host);
            if (interesting) post({ kind: 'websocket_structure', state: 'created', host, path, dataType: 'none', length: 0, topKeys: '', nestedKeys: '', typeToken: '', eventToken: '', kindToken: '', actionToken: '', topicToken: '', nameToken: '', hasConversationKey: false, targetMatch: false });
            if (interesting) socket.addEventListener('open', () => post({ kind: 'websocket_structure', state: 'open', host, path, dataType: 'none', length: 0, topKeys: '', nestedKeys: '', typeToken: '', eventToken: '', kindToken: '', actionToken: '', topicToken: '', nameToken: '', hasConversationKey: false, targetMatch: false }));
            if (interesting) socket.addEventListener('message', event => {
              if (structuralMessageBudget <= 0) return;
              structuralMessageBudget -= 1;
              const shape = socketFrameShape(event.data);
              post({ kind: 'websocket_structure', state: 'message', host, path, ...shape });
            });
            if (interesting) socket.addEventListener('close', event => post({ kind: 'websocket_structure', state: 'close', host, path, dataType: 'none', length: Number(event.code) || 0, topKeys: '', nestedKeys: '', typeToken: '', eventToken: '', kindToken: '', actionToken: '', topicToken: '', nameToken: '', hasConversationKey: false, targetMatch: false }));
            if (interesting) socket.addEventListener('error', () => post({ kind: 'websocket_structure', state: 'error', host, path, dataType: 'none', length: 0, topKeys: '', nestedKeys: '', typeToken: '', eventToken: '', kindToken: '', actionToken: '', topicToken: '', nameToken: '', hasConversationKey: false, targetMatch: false }));
            return socket;
          }
        });
      }
      const installRenderSuppression = () => {'''
)

pbx = Path("ChatGPTClient.xcodeproj/project.pbxproj")
text = pbx.read_text()
if text.count("CURRENT_PROJECT_VERSION = 80;") != 2:
    raise SystemExit("unexpected b80 build identity count")
if text.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b80";') != 2:
    raise SystemExit("unexpected b80 candidate identity count")
text = text.replace("CURRENT_PROJECT_VERSION = 80;", "CURRENT_PROJECT_VERSION = 81;")
text = text.replace('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b80";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b81";')
pbx.write_text(text)
