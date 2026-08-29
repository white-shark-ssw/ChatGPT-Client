import UIKit
import WebKit

private final class WeakNativeWebSendEngineHandler: NSObject, WKScriptMessageHandler {
    weak var target: WKScriptMessageHandler?

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        target?.userContentController(userContentController, didReceive: message)
    }
}

final class NativeWebSendEngineProbeViewController: UIViewController, WKNavigationDelegate, WKScriptMessageHandler, UITextViewDelegate {
    private static let handlerName = "nativeWebSendEngineProbe"
    private static let chatURL = URL(string: "https://chatgpt.com/")!

    private let diagnostics = DiagnosticsLogger.shared
    private let scriptHandler = WeakNativeWebSendEngineHandler()
    private let nativeSurface = UIView()
    private let statusLabel = UILabel()
    private let outputTextView = UITextView()
    private let composerTextView = UITextView()
    private let sendButton = UIButton(type: .system)
    private var webView: WKWebView!
    private var webComposerReady = false
    private var responseActive = false
    private var nativeSurfaceVisible = true
    private var sendCount = 0
    private var nativeDeltaCount = 0
    private var nativeCharacterCount = 0

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "Native 输入 / Web Send"
        view.backgroundColor = .systemBackground
        navigationItem.rightBarButtonItem = UIBarButtonItem(title: "显示 Web", style: .plain, target: self, action: #selector(toggleWebSurface))

        let configuration = WKWebViewConfiguration()
        configuration.websiteDataStore = .default()
        scriptHandler.target = self
        configuration.userContentController.add(scriptHandler, name: Self.handlerName)
        configuration.userContentController.addUserScript(WKUserScript(source: Self.probeScript, injectionTime: .atDocumentStart, forMainFrameOnly: true))

        webView = WKWebView(frame: .zero, configuration: configuration)
        webView.navigationDelegate = self
        webView.allowsBackForwardNavigationGestures = false
        webView.scrollView.keyboardDismissMode = .interactive
        webView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(webView)

        nativeSurface.backgroundColor = .systemBackground
        nativeSurface.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(nativeSurface)

        let explanationLabel = UILabel()
        explanationLabel.font = .preferredFont(forTextStyle: .footnote)
        explanationLabel.textColor = .secondaryLabel
        explanationLabel.numberOfLines = 0
        explanationLabel.text = "b48 诊断：正常情况下只操作这里的原生输入框。底层官方 ChatGPT Web 仍负责自己的登录、浏览器挑战和 protected Send；回答正文 SSE 在进入 Web React 前过滤并仅在内存中转给此 Native 视图。不会把提示词/回答写入诊断日志。首版只验证新会话与连续两轮，不代表生产架构已接受。"

        statusLabel.font = .monospacedSystemFont(ofSize: 11, weight: .regular)
        statusLabel.textColor = .secondaryLabel
        statusLabel.numberOfLines = 0

        outputTextView.isEditable = false
        outputTextView.isSelectable = true
        outputTextView.alwaysBounceVertical = true
        outputTextView.font = .preferredFont(forTextStyle: .body)
        outputTextView.backgroundColor = .secondarySystemBackground
        outputTextView.layer.cornerRadius = 12
        outputTextView.textContainerInset = UIEdgeInsets(top: 12, left: 10, bottom: 12, right: 10)
        outputTextView.text = "等待 Web composer 就绪…"

        composerTextView.delegate = self
        composerTextView.font = .preferredFont(forTextStyle: .body)
        composerTextView.backgroundColor = .secondarySystemBackground
        composerTextView.layer.cornerRadius = 12
        composerTextView.textContainerInset = UIEdgeInsets(top: 9, left: 8, bottom: 9, right: 8)
        composerTextView.returnKeyType = .default
        composerTextView.keyboardDismissMode = .interactive
        composerTextView.setContentHuggingPriority(.defaultLow, for: .horizontal)
        composerTextView.heightAnchor.constraint(greaterThanOrEqualToConstant: 44).isActive = true
        composerTextView.heightAnchor.constraint(lessThanOrEqualToConstant: 110).isActive = true

        sendButton.setTitle("发送", for: .normal)
        sendButton.titleLabel?.font = .preferredFont(forTextStyle: .headline)
        sendButton.isEnabled = false
        sendButton.addTarget(self, action: #selector(sendNativeText), for: .touchUpInside)
        sendButton.widthAnchor.constraint(equalToConstant: 64).isActive = true

        let composerRow = UIStackView(arrangedSubviews: [composerTextView, sendButton])
        composerRow.axis = .horizontal
        composerRow.alignment = .bottom
        composerRow.spacing = 10

        let stack = UIStackView(arrangedSubviews: [explanationLabel, statusLabel, outputTextView, composerRow])
        stack.axis = .vertical
        stack.spacing = 10
        stack.translatesAutoresizingMaskIntoConstraints = false
        nativeSurface.addSubview(stack)

        NSLayoutConstraint.activate([
            webView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            webView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            webView.topAnchor.constraint(equalTo: view.topAnchor),
            webView.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            nativeSurface.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            nativeSurface.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            nativeSurface.topAnchor.constraint(equalTo: view.topAnchor),
            nativeSurface.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            stack.leadingAnchor.constraint(equalTo: nativeSurface.safeAreaLayoutGuide.leadingAnchor, constant: 12),
            stack.trailingAnchor.constraint(equalTo: nativeSurface.safeAreaLayoutGuide.trailingAnchor, constant: -12),
            stack.topAnchor.constraint(equalTo: nativeSurface.safeAreaLayoutGuide.topAnchor, constant: 8),
            stack.bottomAnchor.constraint(equalTo: nativeSurface.keyboardLayoutGuide.topAnchor, constant: -10),
            outputTextView.heightAnchor.constraint(greaterThanOrEqualToConstant: 180)
        ])

        webView.isUserInteractionEnabled = false
        updateStatusLabel(detail: "正在加载官方 Web…")
        diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.opened", fields: ["mode": "b48_native_composer_filtered_send_sse", "surface": "native_over_fullsize_web", "scope": "new_chat_diagnostic"])
        webView.load(URLRequest(url: Self.chatURL))
    }

    deinit {
        webView?.configuration.userContentController.removeScriptMessageHandler(forName: Self.handlerName)
    }

    func textViewDidChange(_ textView: UITextView) { updateSendButtonState() }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.page", fields: ["state": "loaded", "pageKind": Self.pageKind(for: webView.url)])
        webView.evaluateJavaScript("window.__nativeWebSendEngineProbe && window.__nativeWebSendEngineProbe.probeComposer();", completionHandler: nil)
    }

    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) { logNavigationFailure(error) }

    func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) { logNavigationFailure(error) }

    func webViewWebContentProcessDidTerminate(_ webView: WKWebView) {
        diagnostics.error(category: "protocol", name: "nativeWebSendEngineProbe.webProcess", fields: ["state": "terminated"])
        updateStatusLabel(detail: "WebContent 已终止；本轮诊断失败")
        webComposerReady = false
        responseActive = false
        updateSendButtonState()
    }

    private func logNavigationFailure(_ error: Error) {
        let nsError = error as NSError
        diagnostics.warning(category: "protocol", name: "nativeWebSendEngineProbe.page", fields: ["state": "failed", "errorDomain": Self.safeToken(nsError.domain), "errorCode": String(nsError.code)])
        updateStatusLabel(detail: "Web 导航失败：\(nsError.code)")
    }

    @objc private func toggleWebSurface() {
        nativeSurfaceVisible.toggle()
        nativeSurface.isHidden = !nativeSurfaceVisible
        webView.isUserInteractionEnabled = !nativeSurfaceVisible
        navigationItem.rightBarButtonItem?.title = nativeSurfaceVisible ? "显示 Web" : "返回 Native"
        diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.surface", fields: ["visible": nativeSurfaceVisible ? "native" : "official_web"])
    }

    @objc private func sendNativeText() {
        let text = composerTextView.text.trimmingCharacters(in: .whitespacesAndNewlines)
        guard webComposerReady, !responseActive, !text.isEmpty else { return }
        guard let data = try? JSONSerialization.data(withJSONObject: text, options: [.fragmentsAllowed]), let literal = String(data: data, encoding: .utf8) else {
            updateStatusLabel(detail: "Native 输入编码失败")
            return
        }

        responseActive = true
        webComposerReady = false
        sendCount += 1
        nativeDeltaCount = 0
        nativeCharacterCount = 0
        updateSendButtonState()
        appendNativeText(sendCount == 1 ? "\n\n你：\(text)\n\nChatGPT：" : "\n\n────────\n你：\(text)\n\nChatGPT：")
        composerTextView.text = ""
        diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.nativeSubmit", fields: ["attempt": String(sendCount), "promptCharacters": String(text.count)])
        updateStatusLabel(detail: "正在交给官方 Web Send…")
        webView.evaluateJavaScript("window.__nativeWebSendEngineProbe && window.__nativeWebSendEngineProbe.submit(\(literal));") { [weak self] _, error in
            guard let self, let error else { return }
            let nsError = error as NSError
            self.diagnostics.warning(category: "protocol", name: "nativeWebSendEngineProbe.bridge", fields: ["state": "evaluate_failed", "errorDomain": Self.safeToken(nsError.domain), "errorCode": String(nsError.code)])
            self.responseActive = false
            self.updateSendButtonState()
            self.updateStatusLabel(detail: "Native→Web bridge 调用失败")
        }
    }

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        guard message.name == Self.handlerName, let body = message.body as? [String: Any], let kind = body["kind"] as? String else { return }
        switch kind {
        case "probe_ready":
            diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.script", fields: ["state": "ready"])
        case "composer_state":
            let ready = (body["ready"] as? NSNumber)?.boolValue ?? false
            webComposerReady = ready && !responseActive
            updateSendButtonState()
            let strategy = Self.safeToken(body["strategy"] as? String)
            diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.composer", fields: ["ready": ready ? "true" : "false", "strategy": strategy])
            if ready && !responseActive { updateStatusLabel(detail: "Web Send engine 已就绪") }
        case "native_submit_result":
            let state = Self.safeToken(body["state"] as? String)
            diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.submitResult", fields: ["state": state])
            if state != "submitted" {
                responseActive = false
                updateSendButtonState()
                updateStatusLabel(detail: "Web composer 提交失败：\(state)")
            }
        case "send_observed":
            diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.sendObserved", fields: ["pageKind": Self.safeToken(body["pageKind"] as? String)])
            updateStatusLabel(detail: "官方 protected Send 已发出")
        case "send_response":
            diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.sendResponse", fields: ["httpStatus": Self.safeNumberString(body["status"]), "contentType": Self.safeToken(body["contentType"] as? String), "filtered": Self.safeBoolString(body["filtered"])])
        case "native_delta":
            guard let text = body["text"] as? String, !text.isEmpty else { return }
            nativeDeltaCount += 1
            nativeCharacterCount += text.count
            appendNativeText(text)
        case "stream_metrics":
            let terminal = (body["terminal"] as? NSNumber)?.boolValue ?? false
            let fields = [
                "frameCount": Self.safeNumberString(body["frameCount"]),
                "removedTextPatchCount": Self.safeNumberString(body["removedTextPatchCount"]),
                "removedTextCharacters": Self.safeNumberString(body["removedTextCharacters"]),
                "webMessageNodes": Self.safeNumberString(body["webMessageNodes"]),
                "webAssistantTextCharacters": Self.safeNumberString(body["webAssistantTextCharacters"]),
                "webElementCount": Self.safeNumberString(body["webElementCount"]),
                "terminal": terminal ? "true" : "false",
                "nativeDeltaCount": String(nativeDeltaCount),
                "nativeCharacters": String(nativeCharacterCount)
            ]
            diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.streamMetrics", fields: fields)
            if terminal {
                responseActive = false
                updateStatusLabel(detail: "本轮完成；等待 Web composer 恢复后可继续第二轮")
                updateSendButtonState()
                webView.evaluateJavaScript("window.__nativeWebSendEngineProbe && window.__nativeWebSendEngineProbe.probeComposer();", completionHandler: nil)
            }
        case "stream_error":
            diagnostics.warning(category: "protocol", name: "nativeWebSendEngineProbe.stream", fields: ["state": Self.safeToken(body["state"] as? String)])
            responseActive = false
            updateSendButtonState()
            updateStatusLabel(detail: "SSE interception 失败")
        default:
            break
        }
    }

    private func appendNativeText(_ text: String) {
        let attributes: [NSAttributedString.Key: Any] = [.font: UIFont.preferredFont(forTextStyle: .body), .foregroundColor: UIColor.label]
        outputTextView.textStorage.append(NSAttributedString(string: text, attributes: attributes))
        let location = max(0, outputTextView.textStorage.length - 1)
        outputTextView.scrollRangeToVisible(NSRange(location: location, length: 1))
    }

    private func updateSendButtonState() {
        let hasText = !composerTextView.text.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty
        sendButton.isEnabled = webComposerReady && !responseActive && hasText
    }

    private func updateStatusLabel(detail: String) {
        statusLabel.text = "Send \(sendCount) · Web composer \(webComposerReady ? "ready" : "not-ready") · response \(responseActive ? "active" : "idle")\n\(detail)"
    }

    private static func pageKind(for url: URL?) -> String {
        guard let url, let host = url.host?.lowercased(), host == "chatgpt.com" || host.hasSuffix(".chatgpt.com") else { return "external_or_unknown" }
        if url.path.hasPrefix("/c/") { return "existing_conversation" }
        if url.path.hasPrefix("/auth") { return "authentication" }
        return "new_or_other"
    }

    private static let safeTokenCharacters = CharacterSet(charactersIn: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_./:{}-+,")

    private static func safeToken(_ value: String?) -> String {
        guard let value, !value.isEmpty, value.count <= 180, value.unicodeScalars.allSatisfy({ safeTokenCharacters.contains($0) }) else { return "none_or_redacted" }
        return value
    }

    private static func safeNumberString(_ value: Any?) -> String {
        guard let number = value as? NSNumber else { return "none" }
        return number.stringValue
    }

    private static func safeBoolString(_ value: Any?) -> String {
        guard let number = value as? NSNumber else { return "false" }
        return number.boolValue ? "true" : "false"
    }

    private static let probeScript = #"""
    (() => {
      if (window.__nativeWebSendEngineProbeInstalled) return;
      window.__nativeWebSendEngineProbeInstalled = true;
      const bridge = window.webkit && window.webkit.messageHandlers && window.webkit.messageHandlers.nativeWebSendEngineProbe;
      if (!bridge) return;
      const post = value => { try { bridge.postMessage(value); } catch (_) {} };
      const originalFetch = window.fetch.bind(window);
      const encoder = new TextEncoder();
      const decoder = new TextDecoder();
      let activeSend = false;
      let lastComposer = null;

      const pageKind = () => location.pathname.startsWith('/c/') ? 'existing_conversation' : (location.pathname.startsWith('/auth') ? 'authentication' : 'new_or_other');
      const isChatGPTHost = host => host === 'chatgpt.com' || host.endsWith('.chatgpt.com');

      const installRenderSuppression = () => {
        if (document.getElementById('__native_web_send_engine_render_suppression')) return;
        const style = document.createElement('style');
        style.id = '__native_web_send_engine_render_suppression';
        style.textContent = '[data-message-author-role="user"],[data-message-author-role="assistant"]{display:none!important;}';
        (document.head || document.documentElement || document).appendChild(style);
      };

      const findComposer = () => {
        const byID = document.querySelector('#prompt-textarea');
        if (byID) return { element: byID, strategy: 'prompt_textarea' };
        const editable = document.querySelector('[contenteditable="true"][role="textbox"]');
        if (editable) return { element: editable, strategy: 'contenteditable_role_textbox' };
        const textarea = document.querySelector('textarea:not([disabled])');
        if (textarea) return { element: textarea, strategy: 'textarea' };
        return null;
      };

      const probeComposer = () => {
        installRenderSuppression();
        const found = findComposer();
        const composer = found && found.element;
        if (composer !== lastComposer) {
          lastComposer = composer || null;
          post({ kind: 'composer_state', ready: !!composer, strategy: found ? found.strategy : 'none' });
        } else if (composer) {
          post({ kind: 'composer_state', ready: true, strategy: found.strategy });
        }
        return found;
      };

      const setComposerText = (element, text) => {
        element.focus();
        if (element instanceof HTMLTextAreaElement || element instanceof HTMLInputElement) {
          const prototype = element instanceof HTMLTextAreaElement ? HTMLTextAreaElement.prototype : HTMLInputElement.prototype;
          const descriptor = Object.getOwnPropertyDescriptor(prototype, 'value');
          if (!descriptor || !descriptor.set) return false;
          descriptor.set.call(element, text);
          element.dispatchEvent(new InputEvent('input', { bubbles: true, inputType: 'insertText', data: text }));
          return true;
        }
        if (element.isContentEditable) {
          const selection = window.getSelection();
          const range = document.createRange();
          range.selectNodeContents(element);
          selection.removeAllRanges();
          selection.addRange(range);
          let inserted = false;
          try { inserted = document.execCommand('insertText', false, text); } catch (_) {}
          if (!inserted) {
            element.textContent = text;
            element.dispatchEvent(new InputEvent('input', { bubbles: true, inputType: 'insertText', data: text }));
          }
          selection.removeAllRanges();
          return true;
        }
        return false;
      };

      const submit = text => {
        const found = probeComposer();
        if (!found || typeof text !== 'string' || !text.trim()) {
          post({ kind: 'native_submit_result', state: 'composer_not_ready' });
          return;
        }
        if (!setComposerText(found.element, text)) {
          post({ kind: 'native_submit_result', state: 'input_state_failed' });
          return;
        }
        queueMicrotask(() => {
          const form = found.element.closest('form');
          const submitButton = form && form.querySelector('button[type="submit"]:not([disabled])');
          if (form && typeof form.requestSubmit === 'function') {
            try {
              submitButton ? form.requestSubmit(submitButton) : form.requestSubmit();
              post({ kind: 'native_submit_result', state: 'submitted' });
              return;
            } catch (_) {}
          }
          const sendButton = document.querySelector('button[data-testid="send-button"]:not([disabled])');
          if (sendButton) {
            sendButton.click();
            post({ kind: 'native_submit_result', state: 'submitted' });
            return;
          }
          post({ kind: 'native_submit_result', state: 'submit_control_missing' });
        });
      };

      const webMetrics = () => {
        const nodes = Array.from(document.querySelectorAll('[data-message-author-role]'));
        const assistantTextCharacters = nodes.filter(node => node.getAttribute('data-message-author-role') === 'assistant').reduce((sum, node) => sum + String(node.textContent || '').length, 0);
        return { webMessageNodes: nodes.length, webAssistantTextCharacters: assistantTextCharacters, webElementCount: document.getElementsByTagName('*').length };
      };

      const scrubTextPatches = node => {
        if (Array.isArray(node)) {
          const output = [];
          let removedTextPatchCount = 0;
          let removedTextCharacters = 0;
          for (const item of node) {
            const result = scrubTextPatches(item);
            removedTextPatchCount += result.removedTextPatchCount;
            removedTextCharacters += result.removedTextCharacters;
            if (!result.skip) output.push(result.value);
          }
          return { value: output, skip: false, removedTextPatchCount, removedTextCharacters };
        }
        if (node && typeof node === 'object') {
          if (node.op === 'append' && node.path === '/message/content/parts/0' && typeof node.value === 'string') {
            if (node.value) post({ kind: 'native_delta', text: node.value });
            return { value: null, skip: true, removedTextPatchCount: 1, removedTextCharacters: node.value.length };
          }
          const output = {};
          let removedTextPatchCount = 0;
          let removedTextCharacters = 0;
          for (const [key, child] of Object.entries(node)) {
            const result = scrubTextPatches(child);
            removedTextPatchCount += result.removedTextPatchCount;
            removedTextCharacters += result.removedTextCharacters;
            if (!result.skip) output[key] = result.value;
          }
          return { value: output, skip: false, removedTextPatchCount, removedTextCharacters };
        }
        return { value: node, skip: false, removedTextPatchCount: 0, removedTextCharacters: 0 };
      };

      const filterFrame = (frame, aggregate) => {
        const lines = String(frame || '').split('\n');
        const dataLines = lines.filter(line => line.startsWith('data:'));
        if (!dataLines.length) return frame + '\n\n';
        const data = dataLines.map(line => line.slice(5).trimStart()).join('\n');
        aggregate.frameCount += 1;
        if (data.trim() === '[DONE]') {
          aggregate.terminal = true;
          const metrics = webMetrics();
          queueMicrotask(() => post(Object.assign({ kind: 'stream_metrics', frameCount: aggregate.frameCount, removedTextPatchCount: aggregate.removedTextPatchCount, removedTextCharacters: aggregate.removedTextCharacters, terminal: true }, metrics)));
          return frame + '\n\n';
        }
        let payload;
        try { payload = JSON.parse(data); } catch (_) { return frame + '\n\n'; }
        const result = scrubTextPatches(payload);
        aggregate.removedTextPatchCount += result.removedTextPatchCount;
        aggregate.removedTextCharacters += result.removedTextCharacters;
        if (result.skip) return '';
        const nonDataLines = lines.filter(line => !line.startsWith('data:'));
        return nonDataLines.concat(['data: ' + JSON.stringify(result.value)]).join('\n') + '\n\n';
      };

      const filteredResponse = response => {
        if (!response.body || typeof response.body.getReader !== 'function' || typeof ReadableStream !== 'function') return response;
        const reader = response.body.getReader();
        const aggregate = { frameCount: 0, removedTextPatchCount: 0, removedTextCharacters: 0, terminal: false };
        let buffer = '';
        const body = new ReadableStream({
          async pull(controller) {
            try {
              while (true) {
                const result = await reader.read();
                if (result.done) {
                  buffer = (buffer + decoder.decode()).replace(/\r\n/g, '\n');
                  if (buffer.trim()) {
                    const filtered = filterFrame(buffer, aggregate);
                    if (filtered) controller.enqueue(encoder.encode(filtered));
                    buffer = '';
                  }
                  if (!aggregate.terminal) {
                    const metrics = webMetrics();
                    post(Object.assign({ kind: 'stream_metrics', frameCount: aggregate.frameCount, removedTextPatchCount: aggregate.removedTextPatchCount, removedTextCharacters: aggregate.removedTextCharacters, terminal: false }, metrics));
                  }
                  controller.close();
                  return;
                }
                buffer = (buffer + decoder.decode(result.value || new Uint8Array(), { stream: true })).replace(/\r\n/g, '\n');
                let output = '';
                let boundary;
                while ((boundary = buffer.indexOf('\n\n')) >= 0) {
                  const frame = buffer.slice(0, boundary);
                  buffer = buffer.slice(boundary + 2);
                  output += filterFrame(frame, aggregate);
                }
                if (output) {
                  controller.enqueue(encoder.encode(output));
                  return;
                }
              }
            } catch (_) {
              post({ kind: 'stream_error', state: 'reader_failed' });
              try { controller.error(new Error('native_web_send_engine_stream_failed')); } catch (_) {}
            }
          },
          cancel(reason) { try { reader.cancel(reason); } catch (_) {} }
        });
        return new Response(body, { status: response.status, statusText: response.statusText, headers: response.headers });
      };

      window.fetch = async function(input, init) {
        let url = null;
        try { url = new URL(typeof input === 'string' ? input : input && input.url || '', location.href); } catch (_) {}
        const isSend = !!url && isChatGPTHost(url.hostname.toLowerCase()) && url.pathname === '/backend-api/f/conversation';
        if (!isSend) return originalFetch(input, init);

        activeSend = true;
        post({ kind: 'send_observed', pageKind: pageKind() });
        try {
          const response = await originalFetch(input, init);
          const contentType = String(response.headers.get('content-type') || '').split(';')[0].trim().toLowerCase();
          const filtered = response.status === 200 && contentType === 'text/event-stream';
          post({ kind: 'send_response', status: response.status, contentType, filtered });
          return filtered ? filteredResponse(response) : response;
        } catch (error) {
          activeSend = false;
          post({ kind: 'stream_error', state: 'send_transport_error' });
          throw error;
        }
      };

      const observer = new MutationObserver(() => probeComposer());
      const start = () => {
        installRenderSuppression();
        probeComposer();
        observer.observe(document.documentElement || document, { childList: true, subtree: true });
        post({ kind: 'probe_ready' });
      };
      if (document.documentElement) start();
      else document.addEventListener('DOMContentLoaded', start, { once: true });

      window.__nativeWebSendEngineProbe = { submit, probeComposer };
    })();
    """#
}
