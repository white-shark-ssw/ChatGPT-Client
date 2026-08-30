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
    private let reasoningStack = UIStackView()
    private let thinkingLabel = UILabel()
    private let reasoningButton = UIButton(type: .system)
    private let reasoningTextView = UITextView()
    private let toolStack = UIStackView()
    private let toolHeaderLabel = UILabel()
    private let toolTextView = UITextView()
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
    private var reasoningDeltaCount = 0
    private var reasoningCharacterCount = 0
    private var answerDeltaCount = 0
    private var answerCharacterCount = 0
    private var reasoningEndMarkerCount = 0
    private var reasoningExpanded = false
    private var reasoningFallbackPromoted = false
    private var toolPresentationCount = 0
    private var thinkingPresentationCount = 0
    private var reasoningSegmentBreakCount = 0
    private var thinkingVisible = false

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
        explanationLabel.text = "b60 诊断：b59 已确认 thinking preamble、思考流、工具活动和最终回答完整。本版保持 b59 文本解析不变，只保留后续 thinking preamble 的段落边界，按 response lifecycle / exact reasoning_status=is_reasoning 显示“正在思考”，并增加不含 raw ID/正文的工具 parent 关联计数；工具阶段完全按真实事件可选，不展示 raw 参数/结果或 assistant:thoughts。"

        statusLabel.font = .monospacedSystemFont(ofSize: 11, weight: .regular)
        statusLabel.textColor = .secondaryLabel
        statusLabel.numberOfLines = 0

        thinkingLabel.text = "正在思考…"
        thinkingLabel.font = .preferredFont(forTextStyle: .subheadline)
        thinkingLabel.textColor = .secondaryLabel
        thinkingLabel.isHidden = true

        reasoningButton.setTitle("思考过程 ▸", for: .normal)
        reasoningButton.titleLabel?.font = .preferredFont(forTextStyle: .subheadline)
        reasoningButton.contentHorizontalAlignment = .leading
        reasoningButton.addTarget(self, action: #selector(toggleReasoningProcess), for: .touchUpInside)

        reasoningTextView.isEditable = false
        reasoningTextView.isSelectable = true
        reasoningTextView.alwaysBounceVertical = true
        reasoningTextView.font = .preferredFont(forTextStyle: .subheadline)
        reasoningTextView.textColor = .secondaryLabel
        reasoningTextView.backgroundColor = .secondarySystemBackground
        reasoningTextView.layer.cornerRadius = 10
        reasoningTextView.textContainerInset = UIEdgeInsets(top: 9, left: 8, bottom: 9, right: 8)
        reasoningTextView.isHidden = true
        let reasoningHeight = reasoningTextView.heightAnchor.constraint(equalToConstant: 150)
        reasoningHeight.priority = .defaultHigh
        reasoningHeight.isActive = true

        reasoningStack.axis = .vertical
        reasoningStack.spacing = 4
        reasoningStack.addArrangedSubview(thinkingLabel)
        reasoningStack.addArrangedSubview(reasoningButton)
        reasoningStack.addArrangedSubview(reasoningTextView)
        reasoningStack.isHidden = true

        toolHeaderLabel.text = "工具调用"
        toolHeaderLabel.font = .preferredFont(forTextStyle: .subheadline)
        toolHeaderLabel.textColor = .secondaryLabel

        toolTextView.isEditable = false
        toolTextView.isSelectable = true
        toolTextView.alwaysBounceVertical = true
        toolTextView.font = .preferredFont(forTextStyle: .footnote)
        toolTextView.textColor = .secondaryLabel
        toolTextView.backgroundColor = .tertiarySystemBackground
        toolTextView.layer.cornerRadius = 10
        toolTextView.textContainerInset = UIEdgeInsets(top: 7, left: 8, bottom: 7, right: 8)
        toolTextView.heightAnchor.constraint(greaterThanOrEqualToConstant: 44).isActive = true
        let toolHeight = toolTextView.heightAnchor.constraint(lessThanOrEqualToConstant: 90)
        toolHeight.priority = .defaultHigh
        toolHeight.isActive = true

        toolStack.axis = .vertical
        toolStack.spacing = 4
        toolStack.addArrangedSubview(toolHeaderLabel)
        toolStack.addArrangedSubview(toolTextView)
        toolStack.isHidden = true

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

        let stack = UIStackView(arrangedSubviews: [explanationLabel, statusLabel, reasoningStack, toolStack, outputTextView, composerRow])
        stack.axis = .vertical
        stack.spacing = 10
        stack.translatesAutoresizingMaskIntoConstraints = false
        nativeSurface.addSubview(stack)

        var constraints = [
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
            outputTextView.heightAnchor.constraint(greaterThanOrEqualToConstant: 160)
        ]
        if #available(iOS 15.0, *) { constraints.append(stack.bottomAnchor.constraint(equalTo: nativeSurface.keyboardLayoutGuide.topAnchor, constant: -10)) }
        else { constraints.append(stack.bottomAnchor.constraint(equalTo: nativeSurface.safeAreaLayoutGuide.bottomAnchor, constant: -10)) }
        NSLayoutConstraint.activate(constraints)

        webView.isUserInteractionEnabled = false
        updateStatusLabel(detail: "正在加载官方 Web…")
        diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.opened", fields: ["mode": "b60_ordered_reasoning_tool_lifecycle", "surface": "native_over_fullsize_web", "scope": "segment_thinking_tool_parent"])
        webView.load(URLRequest(url: Self.chatURL))
    }

    deinit {
        webView?.configuration.userContentController.removeScriptMessageHandler(forName: Self.handlerName)
    }

    func textViewDidChange(_ textView: UITextView) { updateSendButtonState() }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.page", fields: ["state": "loaded", "pageKind": Self.pageKind(for: webView.url)])
        webView.evaluateJavaScript("window.__nativeWebSendEngineProbe && window.__nativeWebSendEngineProbe.probeComposer(true);", completionHandler: nil)
    }

    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) { logNavigationFailure(error) }

    func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) { logNavigationFailure(error) }

    func webViewWebContentProcessDidTerminate(_ webView: WKWebView) {
        diagnostics.error(category: "protocol", name: "nativeWebSendEngineProbe.webProcess", fields: ["state": "terminated"])
        updateStatusLabel(detail: "WebContent 已终止；本轮诊断失败")
        hideThinkingPresentation()
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

    @objc private func toggleReasoningProcess() {
        guard !reasoningStack.isHidden, reasoningCharacterCount > 0 else { return }
        reasoningExpanded.toggle()
        updateReasoningPresentation()
        diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.reasoningPresentation", fields: ["state": reasoningExpanded ? "expanded" : "collapsed", "characters": String(reasoningCharacterCount)])
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
        reasoningDeltaCount = 0
        reasoningCharacterCount = 0
        answerDeltaCount = 0
        answerCharacterCount = 0
        reasoningEndMarkerCount = 0
        reasoningFallbackPromoted = false
        toolPresentationCount = 0
        thinkingPresentationCount = 0
        reasoningSegmentBreakCount = 0
        thinkingVisible = false
        resetReasoningPresentation()
        resetToolActivity()
        updateSendButtonState()
        if sendCount == 1 { outputTextView.text = "" }
        appendNativeText(sendCount == 1 ? "你：\(text)\n\nChatGPT：" : "\n\n────────\n你：\(text)\n\nChatGPT：")
        composerTextView.text = ""
        diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.nativeSubmit", fields: ["attempt": String(sendCount), "promptCharacters": String(text.count)])
        updateStatusLabel(detail: "正在交给官方 Web Send…")
        webView.evaluateJavaScript("window.__nativeWebSendEngineProbe && window.__nativeWebSendEngineProbe.submit(\(literal));") { [weak self] _, error in
            guard let self, let error else { return }
            let nsError = error as NSError
            self.diagnostics.warning(category: "protocol", name: "nativeWebSendEngineProbe.bridge", fields: ["state": "evaluate_failed", "errorDomain": Self.safeToken(nsError.domain), "errorCode": String(nsError.code)])
            self.hideThinkingPresentation()
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
                hideThinkingPresentation()
                responseActive = false
                updateSendButtonState()
                updateStatusLabel(detail: "Web composer 提交失败：\(state)")
            }
        case "send_observed":
            diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.sendObserved", fields: ["pageKind": Self.safeToken(body["pageKind"] as? String)])
            updateStatusLabel(detail: "官方 protected Send 已发出")
        case "send_response":
            let status = (body["status"] as? NSNumber)?.intValue ?? 0
            let filtered = (body["filtered"] as? NSNumber)?.boolValue ?? false
            diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.sendResponse", fields: ["httpStatus": Self.safeNumberString(body["status"]), "contentType": Self.safeToken(body["contentType"] as? String), "filtered": filtered ? "true" : "false"])
            if status == 200 && filtered && responseActive { showThinkingPresentation(source: "lifecycle_send_accepted") }
        case "native_reasoning_preamble":
            guard let text = body["text"] as? String, !text.isEmpty else { return }
            if (body["segmentStart"] as? NSNumber)?.boolValue == true, reasoningCharacterCount > 0 { appendReasoningParagraphBreak() }
            nativeDeltaCount += 1
            nativeCharacterCount += text.count
            reasoningDeltaCount += 1
            reasoningCharacterCount += text.count
            appendReasoningText(text)
        case "native_reasoning_delta":
            guard let text = body["text"] as? String, !text.isEmpty else { return }
            nativeDeltaCount += 1
            nativeCharacterCount += text.count
            reasoningDeltaCount += 1
            reasoningCharacterCount += text.count
            appendReasoningText(text)
        case "native_answer_delta":
            guard let text = body["text"] as? String, !text.isEmpty else { return }
            hideThinkingPresentation()
            nativeDeltaCount += 1
            nativeCharacterCount += text.count
            answerDeltaCount += 1
            answerCharacterCount += text.count
            appendNativeText(text)
        case "native_reasoning_phase":
            let state = Self.safeToken(body["state"] as? String)
            if state == "active" {
                showThinkingPresentation(source: "service_reasoning_active")
                diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.reasoningPhase", fields: ["state": "active", "reasoningCharacters": String(reasoningCharacterCount)])
                return
            }
            guard state == "ended" else { return }
            reasoningEndMarkerCount += 1
            hideThinkingPresentation()
            if !reasoningStack.isHidden {
                reasoningExpanded = false
                updateReasoningPresentation()
            }
            diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.reasoningPhase", fields: ["state": "ended", "recapCharacters": Self.safeNumberString(body["recapCharacters"]), "reasoningCharacters": String(reasoningCharacterCount)])
            updateStatusLabel(detail: "官方 reasoning_ended；后续文本进入最终回答")
        case "native_tool_activity":
            let state = Self.safeToken(body["state"] as? String)
            let titleCharacters = Self.safeNumberString(body["titleCharacters"])
            if state == "invoked" {
                let title = (body["title"] as? String)?.trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
                appendToolActivity(title.isEmpty ? "工具调用" : title)
                toolPresentationCount += 1
            }
            diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.toolActivity", fields: ["state": state, "titleCharacters": titleCharacters, "presented": state == "invoked" ? "true" : "false"])
        case "stream_structure":
            let fields = [
                "eventIndex": Self.safeNumberString(body["eventIndex"]),
                "signature": Self.safeToken(body["signature"] as? String),
                "eventType": Self.safeToken(body["eventType"] as? String),
                "operation": Self.safeToken(body["operation"] as? String),
                "patchPath": Self.safeToken(body["patchPath"] as? String),
                "messageRole": Self.safeToken(body["messageRole"] as? String),
                "messageContentType": Self.safeToken(body["messageContentType"] as? String),
                "messageStatus": Self.safeToken(body["messageStatus"] as? String),
                "endTurn": Self.safeBoolString(body["endTurn"]),
                "payloadKeys": Self.safeTokenArray(body["payloadKeys"]),
                "valueKeys": Self.safeTokenArray(body["valueKeys"]),
                "nestedPatches": Self.safeTokenArray(body["nestedPatches"]),
                "messageKeys": Self.safeTokenArray(body["messageKeys"]),
                "authorKeys": Self.safeTokenArray(body["authorKeys"]),
                "contentKeys": Self.safeTokenArray(body["contentKeys"]),
                "metadataKeys": Self.safeTokenArray(body["metadataKeys"]),
                "recipient": Self.safeToken(body["recipient"] as? String),
                "authorName": Self.safeToken(body["authorName"] as? String),
                "contentStringFields": Self.safeTokenArray(body["contentStringFields"]),
                "contentArrayFields": Self.safeTokenArray(body["contentArrayFields"]),
                "metadataBooleanFields": Self.safeTokenArray(body["metadataBooleanFields"]),
                "metadataEnumFields": Self.safeTokenArray(body["metadataEnumFields"]),
                "textPhase": Self.safeToken(body["textPhase"] as? String)
            ]
            diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.streamStructure", fields: fields)
        case "stream_metrics":
            let terminal = (body["terminal"] as? NSNumber)?.boolValue ?? false
            let markerCount = (body["reasoningEndMarkerCount"] as? NSNumber)?.intValue ?? 0
            if terminal && markerCount == 0 && reasoningCharacterCount > 0 { promotePendingReasoningToAnswer() }
            let fields = [
                "frameCount": Self.safeNumberString(body["frameCount"]),
                "removedTextPatchCount": Self.safeNumberString(body["removedTextPatchCount"]),
                "removedTextCharacters": Self.safeNumberString(body["removedTextCharacters"]),
                "explicitTextPatchCount": Self.safeNumberString(body["explicitTextPatchCount"]),
                "exactTopLevelTextPatchCount": Self.safeNumberString(body["exactTopLevelTextPatchCount"]),
                "rootNonExactTextPatchCount": Self.safeNumberString(body["rootNonExactTextPatchCount"]),
                "nestedTextPatchCount": Self.safeNumberString(body["nestedTextPatchCount"]),
                "contextualValueStringCount": Self.safeNumberString(body["contextualValueStringCount"]),
                "contextualValueStringCharacters": Self.safeNumberString(body["contextualValueStringCharacters"]),
                "inactiveValueStringCount": Self.safeNumberString(body["inactiveValueStringCount"]),
                "inactiveValueStringCharacters": Self.safeNumberString(body["inactiveValueStringCharacters"]),
                "continuationResetWhileActiveCount": Self.safeNumberString(body["continuationResetWhileActiveCount"]),
                "firstInactiveValueContext": Self.safeToken(body["firstInactiveValueContext"] as? String),
                "titleGenerationWhileContinuationCount": Self.safeNumberString(body["titleGenerationWhileContinuationCount"]),
                "structureSignatureCount": Self.safeNumberString(body["structureSignatureCount"]),
                "structureSignatureOverflowCount": Self.safeNumberString(body["structureSignatureOverflowCount"]),
                "specialStructureSignatureCount": Self.safeNumberString(body["specialStructureSignatureCount"]),
                "specialStructureSignatureOverflowCount": Self.safeNumberString(body["specialStructureSignatureOverflowCount"]),
                "phaseTextStructureSignatureCount": Self.safeNumberString(body["phaseTextStructureSignatureCount"]),
                "phaseTextStructureSignatureOverflowCount": Self.safeNumberString(body["phaseTextStructureSignatureOverflowCount"]),
                "assistantTextMessageCount": Self.safeNumberString(body["assistantTextMessageCount"]),
                "assistantTextBeforeReasoningEndCount": Self.safeNumberString(body["assistantTextBeforeReasoningEndCount"]),
                "assistantTextAfterReasoningEndCount": Self.safeNumberString(body["assistantTextAfterReasoningEndCount"]),
                "reasoningEndMarkerCount": Self.safeNumberString(body["reasoningEndMarkerCount"]),
                "reasoningPreambleCount": Self.safeNumberString(body["reasoningPreambleCount"]),
                "reasoningPreambleCharacters": Self.safeNumberString(body["reasoningPreambleCharacters"]),
                "reasoningActiveSignalCount": Self.safeNumberString(body["reasoningActiveSignalCount"]),
                "reasoningSegmentBreakCount": Self.safeNumberString(body["reasoningSegmentBreakCount"]),
                "toolInvocationIdentityCount": Self.safeNumberString(body["toolInvocationIdentityCount"]),
                "toolInvocationCount": Self.safeNumberString(body["toolInvocationCount"]),
                "toolInvocationWithTitleCount": Self.safeNumberString(body["toolInvocationWithTitleCount"]),
                "toolResultCount": Self.safeNumberString(body["toolResultCount"]),
                "toolResultWithTitleCount": Self.safeNumberString(body["toolResultWithTitleCount"]),
                "toolResultParentPresentCount": Self.safeNumberString(body["toolResultParentPresentCount"]),
                "toolResultParentMatchCount": Self.safeNumberString(body["toolResultParentMatchCount"]),
                "toolResultParentUnmatchedCount": Self.safeNumberString(body["toolResultParentUnmatchedCount"]),
                "toolResultParentMissingCount": Self.safeNumberString(body["toolResultParentMissingCount"]),
                "toolResultAuthorRecipientMatchCount": Self.safeNumberString(body["toolResultAuthorRecipientMatchCount"]),
                "webMessageNodes": Self.safeNumberString(body["webMessageNodes"]),
                "webAssistantTextCharacters": Self.safeNumberString(body["webAssistantTextCharacters"]),
                "webElementCount": Self.safeNumberString(body["webElementCount"]),
                "terminal": terminal ? "true" : "false",
                "nativeDeltaCount": String(nativeDeltaCount),
                "nativeCharacters": String(nativeCharacterCount),
                "nativeReasoningDeltaCount": String(reasoningDeltaCount),
                "nativeReasoningCharacters": String(reasoningCharacterCount),
                "nativeAnswerDeltaCount": String(answerDeltaCount),
                "nativeAnswerCharacters": String(answerCharacterCount),
                "nativeToolPresentationCount": String(toolPresentationCount),
                "nativeThinkingPresentationCount": String(thinkingPresentationCount),
                "nativeReasoningSegmentBreakCount": String(reasoningSegmentBreakCount),
                "reasoningFallbackPromoted": reasoningFallbackPromoted ? "true" : "false"
            ]
            diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.streamMetrics", fields: fields)
            hideThinkingPresentation()
            responseActive = false
            if terminal { updateStatusLabel(detail: "本轮完成；Web composer 恢复后可继续第二轮") }
            else { updateStatusLabel(detail: "SSE 已结束但没有 [DONE]；本轮按失败处理") }
            updateSendButtonState()
            webView.evaluateJavaScript("window.__nativeWebSendEngineProbe && window.__nativeWebSendEngineProbe.probeComposer(true);", completionHandler: nil)
        case "stream_error":
            diagnostics.warning(category: "protocol", name: "nativeWebSendEngineProbe.stream", fields: ["state": Self.safeToken(body["state"] as? String)])
            hideThinkingPresentation()
            responseActive = false
            updateSendButtonState()
            updateStatusLabel(detail: "SSE interception 失败")
        default:
            break
        }
    }

    private func resetReasoningPresentation() {
        thinkingVisible = false
        thinkingLabel.isHidden = true
        reasoningExpanded = false
        reasoningTextView.text = ""
        reasoningTextView.isHidden = true
        reasoningButton.isHidden = false
        reasoningStack.isHidden = true
        reasoningButton.setTitle("思考过程 ▸", for: .normal)
    }

    private func updateReasoningPresentation() {
        reasoningButton.isHidden = reasoningCharacterCount == 0
        reasoningTextView.isHidden = reasoningCharacterCount == 0 || !reasoningExpanded
        reasoningButton.setTitle(reasoningExpanded ? "思考过程 ▾" : "思考过程 ▸", for: .normal)
    }

    private func showThinkingPresentation(source: String) {
        guard responseActive, reasoningEndMarkerCount == 0 else { return }
        reasoningStack.isHidden = false
        reasoningButton.isHidden = reasoningCharacterCount == 0
        if !thinkingVisible {
            thinkingVisible = true
            thinkingPresentationCount += 1
            thinkingLabel.isHidden = false
            diagnostics.info(category: "protocol", name: "nativeWebSendEngineProbe.thinkingPresentation", fields: ["state": "active", "source": source, "reasoningCharacters": String(reasoningCharacterCount)])
        }
    }

    private func hideThinkingPresentation() {
        guard thinkingVisible else { return }
        thinkingVisible = false
        thinkingLabel.isHidden = true
    }

    private func appendReasoningParagraphBreak() {
        guard reasoningTextView.textStorage.length > 0, !reasoningTextView.text.hasSuffix("\n\n") else { return }
        let attributes: [NSAttributedString.Key: Any] = [.font: UIFont.preferredFont(forTextStyle: .subheadline), .foregroundColor: UIColor.secondaryLabel]
        reasoningTextView.textStorage.append(NSAttributedString(string: "\n\n", attributes: attributes))
        reasoningSegmentBreakCount += 1
    }

    private func appendReasoningText(_ text: String) {
        hideThinkingPresentation()
        if reasoningStack.isHidden { reasoningStack.isHidden = false }
        if !reasoningExpanded {
            reasoningExpanded = true
            updateReasoningPresentation()
        }
        reasoningButton.isHidden = false
        let attributes: [NSAttributedString.Key: Any] = [.font: UIFont.preferredFont(forTextStyle: .subheadline), .foregroundColor: UIColor.secondaryLabel]
        reasoningTextView.textStorage.append(NSAttributedString(string: text, attributes: attributes))
        let location = max(0, reasoningTextView.textStorage.length - 1)
        reasoningTextView.scrollRangeToVisible(NSRange(location: location, length: 1))
    }

    private func promotePendingReasoningToAnswer() {
        let text = reasoningTextView.text ?? ""
        guard !text.isEmpty else { return }
        appendNativeText(text)
        answerDeltaCount += reasoningDeltaCount
        answerCharacterCount += reasoningCharacterCount
        reasoningFallbackPromoted = true
        hideThinkingPresentation()
        reasoningStack.isHidden = true
        reasoningExpanded = false
        updateReasoningPresentation()
    }

    private func resetToolActivity() {
        toolTextView.text = ""
        toolStack.isHidden = true
    }

    private func appendToolActivity(_ title: String) {
        if toolStack.isHidden { toolStack.isHidden = false }
        let line = toolTextView.textStorage.length == 0 ? "• \(title)" : "\n• \(title)"
        let attributes: [NSAttributedString.Key: Any] = [.font: UIFont.preferredFont(forTextStyle: .footnote), .foregroundColor: UIColor.secondaryLabel]
        toolTextView.textStorage.append(NSAttributedString(string: line, attributes: attributes))
        let location = max(0, toolTextView.textStorage.length - 1)
        toolTextView.scrollRangeToVisible(NSRange(location: location, length: 1))
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

    private static func safeTokenArray(_ value: Any?) -> String {
        guard let values = value as? [Any] else { return "none" }
        let tokens = values.prefix(24).map { safeToken($0 as? String) }
        return tokens.isEmpty ? "none" : tokens.joined(separator: ",")
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
      const safeStructuralKey = value => {
        const s = String(value || '');
        return /^[A-Za-z_][A-Za-z0-9_.:-]{0,63}$/.test(s) ? s : '{key}';
      };
      const safeProtocolValue = value => {
        if (typeof value !== 'string') return 'none';
        const s = value.trim();
        return /^[A-Za-z][A-Za-z0-9_.:+-]{0,63}$/.test(s) ? s : 'other_or_redacted';
      };
      const safePatchPath = value => {
        if (typeof value !== 'string' || !value) return 'none';
        return /^\/[A-Za-z0-9_./:{}+-]{1,159}$/.test(value) ? value : 'other_or_redacted';
      };
      const directKeys = value => value && typeof value === 'object' && !Array.isArray(value) ? Object.keys(value).slice(0, 32).map(safeStructuralKey).sort() : [];
      const primitiveType = value => value === null ? 'null' : (Array.isArray(value) ? 'array' : typeof value);
      const summarizeContentFields = content => {
        const stringFields = [];
        const arrayFields = [];
        if (!content || typeof content !== 'object' || Array.isArray(content)) return { stringFields, arrayFields };
        for (const [rawKey, value] of Object.entries(content).slice(0, 24)) {
          const key = safeStructuralKey(rawKey);
          if (typeof value === 'string') {
            stringFields.push(key + ':' + value.length);
            continue;
          }
          if (!Array.isArray(value)) continue;
          const types = Array.from(new Set(value.slice(0, 8).map(primitiveType))).slice(0, 6);
          const stringCharacters = value.reduce((sum, item) => sum + (typeof item === 'string' ? item.length : 0), 0);
          const firstObject = value.find(item => item && typeof item === 'object' && !Array.isArray(item));
          const itemKeys = firstObject ? Object.keys(firstObject).slice(0, 12).map(safeStructuralKey).sort() : [];
          let summary = key + ':' + value.length + ':' + (types.length ? types.join('+') : 'empty') + ':chars' + stringCharacters;
          if (itemKeys.length) summary += ':keys' + itemKeys.join('+');
          arrayFields.push(summary.slice(0, 180));
        }
        return { stringFields: stringFields.slice(0, 24), arrayFields: arrayFields.slice(0, 24) };
      };
      const summarizeMetadataFields = metadata => {
        const booleanFields = [];
        const enumFields = [];
        if (!metadata || typeof metadata !== 'object' || Array.isArray(metadata)) return { booleanFields, enumFields };
        for (const [rawKey, value] of Object.entries(metadata).slice(0, 32)) {
          const key = safeStructuralKey(rawKey);
          if (typeof value === 'boolean') {
            booleanFields.push(key + ':' + (value ? 'true' : 'false'));
            continue;
          }
          if (typeof value !== 'string' || !/(visible|visibility|hidden|display|presentation|status|type|kind|category|mode|phase|result)/i.test(rawKey)) continue;
          const token = safeProtocolValue(value);
          if (token !== 'none' && token !== 'other_or_redacted') enumFields.push((key + ':' + token).slice(0, 180));
        }
        return { booleanFields: booleanFields.slice(0, 24), enumFields: enumFields.slice(0, 24) };
      };

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

      const probeComposer = (force = false) => {
        installRenderSuppression();
        const found = findComposer();
        const composer = found && found.element;
        if (force || composer !== lastComposer) post({ kind: 'composer_state', ready: !!composer && !activeSend, strategy: found ? found.strategy : 'none' });
        lastComposer = composer || null;
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
        const found = probeComposer(true);
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

      const findMessage = (node, depth = 0) => {
        if (!node || typeof node !== 'object' || depth > 5) return null;
        if (!Array.isArray(node) && node.message && typeof node.message === 'object') return node.message;
        if (!Array.isArray(node) && node.author && node.content && typeof node.author === 'object' && typeof node.content === 'object') return node;
        const children = Array.isArray(node) ? node : Object.values(node);
        for (const child of children) {
          const message = findMessage(child, depth + 1);
          if (message) return message;
        }
        return null;
      };

      const collectNestedPatches = (node, output = [], depth = 0) => {
        if (!node || typeof node !== 'object' || depth > 5 || output.length >= 16) return output;
        if (depth > 0 && !Array.isArray(node) && typeof node.o === 'string' && typeof node.p === 'string') output.push(safeProtocolValue(node.o) + ':' + safePatchPath(node.p));
        const children = Array.isArray(node) ? node : Object.values(node);
        for (const child of children) {
          collectNestedPatches(child, output, depth + 1);
          if (output.length >= 16) break;
        }
        return output;
      };

      const summarizeStructure = (payload, aggregate) => {
        const payloadObject = payload && typeof payload === 'object' && !Array.isArray(payload) ? payload : null;
        if (!payloadObject) return { signature: 'non_object', eventType: 'none', operation: 'none', patchPath: 'none', messageRole: 'none', messageContentType: 'none', messageStatus: 'none', endTurn: false, payloadKeys: [], valueKeys: [], nestedPatches: [], messageKeys: [], authorKeys: [], contentKeys: [], metadataKeys: [], recipient: 'none', authorName: 'none', contentStringFields: [], contentArrayFields: [], metadataBooleanFields: [], metadataEnumFields: [], textPhase: 'none' };
        const valueObject = payloadObject.v && typeof payloadObject.v === 'object' && !Array.isArray(payloadObject.v) ? payloadObject.v : null;
        const eventType = safeProtocolValue(payloadObject.type);
        const operation = safeProtocolValue(payloadObject.o);
        const patchPath = safePatchPath(payloadObject.p);
        const message = findMessage(payloadObject);
        const messageRole = safeProtocolValue(message && message.author && message.author.role);
        const messageContentType = safeProtocolValue(message && message.content && message.content.content_type);
        const messageStatus = safeProtocolValue(message && message.status);
        const endTurn = !!(message && message.end_turn === true);
        const payloadKeys = Object.keys(payloadObject).slice(0, 32).map(safeStructuralKey).sort();
        const valueKeys = valueObject ? Object.keys(valueObject).slice(0, 32).map(safeStructuralKey).sort() : [];
        const nestedPatches = collectNestedPatches(payloadObject).slice(0, 16);
        const specialMessage = !!message && ((messageRole === 'assistant' && (messageContentType === 'reasoning_recap' || messageContentType === 'thoughts' || messageContentType === 'code')) || messageRole === 'tool');
        const phaseTextMessage = !!message && messageRole === 'assistant' && messageContentType === 'text';
        const detailedMessage = specialMessage || phaseTextMessage;
        const author = detailedMessage && message.author && typeof message.author === 'object' && !Array.isArray(message.author) ? message.author : null;
        const content = detailedMessage && message.content && typeof message.content === 'object' && !Array.isArray(message.content) ? message.content : null;
        const metadata = detailedMessage && message.metadata && typeof message.metadata === 'object' && !Array.isArray(message.metadata) ? message.metadata : null;
        const contentFields = summarizeContentFields(content);
        const metadataFields = summarizeMetadataFields(metadata);
        const messageKeys = detailedMessage ? directKeys(message) : [];
        const authorKeys = directKeys(author);
        const contentKeys = directKeys(content);
        const metadataKeys = directKeys(metadata);
        const recipient = detailedMessage ? safeProtocolValue(message.recipient) : 'none';
        const authorName = detailedMessage ? safeProtocolValue(author && author.name) : 'none';
        const textPhase = phaseTextMessage ? (aggregate.reasoningEnded ? 'after_reasoning_end' : 'before_reasoning_end') : 'none';
        let signature = 'keys:' + payloadKeys.join('+');
        if (typeof payloadObject.type === 'string') signature = 'type:' + eventType;
        else if (typeof payloadObject.o === 'string') signature = 'patch:' + operation + ':' + patchPath;
        else if (message) signature = 'message:' + messageRole + ':' + messageContentType + ':' + messageStatus;
        else if (typeof payloadObject.v === 'string') signature = 'value_string_patch';
        return { signature: signature.slice(0, 180), eventType, operation, patchPath, messageRole, messageContentType, messageStatus, endTurn, payloadKeys, valueKeys, nestedPatches, messageKeys, authorKeys, contentKeys, metadataKeys, recipient, authorName, contentStringFields: contentFields.stringFields, contentArrayFields: contentFields.arrayFields, metadataBooleanFields: metadataFields.booleanFields, metadataEnumFields: metadataFields.enumFields, textPhase };
      };

      const postStructure = summary => post({ kind: 'stream_structure', eventIndex: summary.eventIndex, signature: summary.signature, eventType: summary.eventType, operation: summary.operation, patchPath: summary.patchPath, messageRole: summary.messageRole, messageContentType: summary.messageContentType, messageStatus: summary.messageStatus, endTurn: summary.endTurn, payloadKeys: summary.payloadKeys, valueKeys: summary.valueKeys, nestedPatches: summary.nestedPatches, messageKeys: summary.messageKeys, authorKeys: summary.authorKeys, contentKeys: summary.contentKeys, metadataKeys: summary.metadataKeys, recipient: summary.recipient, authorName: summary.authorName, contentStringFields: summary.contentStringFields, contentArrayFields: summary.contentArrayFields, metadataBooleanFields: summary.metadataBooleanFields, metadataEnumFields: summary.metadataEnumFields, textPhase: summary.textPhase });

      const observeStructure = (payload, aggregate) => {
        const summary = summarizeStructure(payload, aggregate);
        summary.eventIndex = aggregate.frameCount;
        const evidenceKey = JSON.stringify([summary.signature, summary.eventType, summary.operation, summary.patchPath, summary.messageRole, summary.messageContentType, summary.messageStatus, summary.endTurn, summary.payloadKeys, summary.valueKeys, summary.nestedPatches, summary.messageKeys, summary.authorKeys, summary.contentKeys, summary.metadataKeys, summary.recipient, summary.authorName, summary.contentStringFields, summary.contentArrayFields, summary.metadataBooleanFields, summary.metadataEnumFields, summary.textPhase]);
        const specialMessage = (summary.messageRole === 'assistant' && (summary.messageContentType === 'reasoning_recap' || summary.messageContentType === 'thoughts' || summary.messageContentType === 'code')) || summary.messageRole === 'tool';
        const phaseTextMessage = summary.messageRole === 'assistant' && summary.messageContentType === 'text';
        let specialPosted = false;
        let phasePosted = false;
        if (specialMessage) {
          const specialEvidenceKey = JSON.stringify([summary.messageRole, summary.messageContentType, summary.messageStatus, summary.recipient, summary.authorName, summary.contentKeys, summary.metadataKeys, summary.metadataBooleanFields, summary.metadataEnumFields]);
          if (!aggregate.specialStructureSeen.has(specialEvidenceKey)) {
            if (aggregate.specialStructureSeen.size >= 24) aggregate.specialStructureSignatureOverflowCount += 1;
            else {
              aggregate.specialStructureSeen.add(specialEvidenceKey);
              postStructure(summary);
              specialPosted = true;
            }
          }
        }
        if (phaseTextMessage) {
          aggregate.assistantTextMessageCount += 1;
          if (aggregate.reasoningEnded) aggregate.assistantTextAfterReasoningEndCount += 1;
          else aggregate.assistantTextBeforeReasoningEndCount += 1;
          const phaseEvidenceKey = JSON.stringify([summary.messageStatus, summary.recipient, summary.contentKeys, summary.contentStringFields, summary.contentArrayFields, summary.metadataKeys, summary.metadataBooleanFields, summary.metadataEnumFields, summary.textPhase]);
          if (!aggregate.phaseTextStructureSeen.has(phaseEvidenceKey)) {
            if (aggregate.phaseTextStructureSeen.size >= 12) aggregate.phaseTextStructureSignatureOverflowCount += 1;
            else {
              aggregate.phaseTextStructureSeen.add(phaseEvidenceKey);
              postStructure(summary);
              phasePosted = true;
            }
          }
        }
        if (aggregate.structureSeen.has(evidenceKey)) return;
        if (aggregate.structureSeen.size >= 32) {
          aggregate.structureSignatureOverflowCount += 1;
          return;
        }
        aggregate.structureSeen.add(evidenceKey);
        if (!specialPosted && !phasePosted) postStructure(summary);
      };

      const postTextDelta = (text, aggregate) => {
        if (!text) return;
        post({ kind: aggregate.reasoningEnded ? 'native_answer_delta' : 'native_reasoning_delta', text });
      };

      const observeReasoningActive = (payload, aggregate) => {
        if (aggregate.reasoningEnded) return;
        const message = findMessage(payload);
        if (!message || !message.author || message.author.role !== 'assistant' || message.status !== 'finished_successfully' || message.recipient !== 'all' || typeof message.id !== 'string' || !message.id) return;
        if (aggregate.reasoningActiveSeen.has(message.id)) return;
        const content = message.content && typeof message.content === 'object' && !Array.isArray(message.content) ? message.content : null;
        const metadata = message.metadata && typeof message.metadata === 'object' && !Array.isArray(message.metadata) ? message.metadata : null;
        if (!content || content.content_type !== 'thoughts' || !metadata || metadata.reasoning_status !== 'is_reasoning') return;
        aggregate.reasoningActiveSeen.add(message.id);
        aggregate.reasoningActiveSignalCount += 1;
        post({ kind: 'native_reasoning_phase', state: 'active' });
      };

      const observeReasoningPreamble = (payload, aggregate) => {
        if (aggregate.reasoningEnded) return;
        const message = findMessage(payload);
        if (!message || !message.author || message.author.role !== 'assistant' || message.status !== 'in_progress' || message.recipient !== 'all' || typeof message.id !== 'string' || !message.id) return;
        if (aggregate.reasoningPreambleSeen.has(message.id)) return;
        const content = message.content && typeof message.content === 'object' && !Array.isArray(message.content) ? message.content : null;
        const metadata = message.metadata && typeof message.metadata === 'object' && !Array.isArray(message.metadata) ? message.metadata : null;
        if (!content || content.content_type !== 'text' || !metadata || metadata.is_thinking_preamble_message !== true) return;
        if (!Array.isArray(content.parts) || content.parts.length !== 1 || typeof content.parts[0] !== 'string' || !content.parts[0]) return;
        const segmentStart = aggregate.reasoningPreambleCount > 0;
        aggregate.reasoningPreambleSeen.add(message.id);
        aggregate.reasoningPreambleCount += 1;
        aggregate.reasoningPreambleCharacters += content.parts[0].length;
        if (segmentStart) aggregate.reasoningSegmentBreakCount += 1;
        post({ kind: 'native_reasoning_preamble', text: content.parts[0], segmentStart });
      };

      const observeReasoningEnd = (payload, aggregate) => {
        const message = findMessage(payload);
        if (!message || !message.author || message.author.role !== 'assistant' || message.status !== 'finished_successfully' || message.recipient !== 'all') return;
        const content = message.content && typeof message.content === 'object' && !Array.isArray(message.content) ? message.content : null;
        const metadata = message.metadata && typeof message.metadata === 'object' && !Array.isArray(message.metadata) ? message.metadata : null;
        if (!content || content.content_type !== 'reasoning_recap' || typeof content.content !== 'string' || !content.content.trim()) return;
        if (!metadata || metadata.reasoning_status !== 'reasoning_ended' || metadata.reasoning_recap_type !== 'collapse') return;
        if (aggregate.reasoningEnded) return;
        aggregate.reasoningEnded = true;
        aggregate.reasoningEndMarkerCount += 1;
        post({ kind: 'native_reasoning_phase', state: 'ended', recapCharacters: content.content.length });
      };

      const observeToolActivity = (payload, aggregate) => {
        const message = findMessage(payload);
        if (!message || !message.author || typeof message.id !== 'string' || !message.id) return;
        const content = message.content && typeof message.content === 'object' && !Array.isArray(message.content) ? message.content : null;
        const metadata = message.metadata && typeof message.metadata === 'object' && !Array.isArray(message.metadata) ? message.metadata : null;
        const role = message.author.role;
        const contentType = content && content.content_type;
        const rawTitle = metadata && typeof metadata.reasoning_title === 'string' ? metadata.reasoning_title.trim() : '';
        const title = rawTitle.slice(0, 160);

        if (role === 'assistant' && contentType === 'code' && typeof message.recipient === 'string' && message.recipient && message.recipient !== 'all') {
          if (!aggregate.toolInvocationIdentityByID.has(message.id)) aggregate.toolInvocationIdentityByID.set(message.id, message.recipient);
          if (message.status !== 'finished_successfully' || !metadata || metadata.is_complete !== true || aggregate.toolActivitySeen.has(message.id)) return;
          aggregate.toolActivitySeen.add(message.id);
          aggregate.toolInvocationCount += 1;
          if (rawTitle) aggregate.toolInvocationWithTitleCount += 1;
          post({ kind: 'native_tool_activity', state: 'invoked', title, titleCharacters: rawTitle.length });
          return;
        }

        if (role !== 'tool' || message.recipient !== 'all' || message.status !== 'finished_successfully' || aggregate.toolActivitySeen.has(message.id)) return;
        aggregate.toolActivitySeen.add(message.id);
        aggregate.toolResultCount += 1;
        if (rawTitle) aggregate.toolResultWithTitleCount += 1;
        const parentID = metadata && typeof metadata.parent_id === 'string' && metadata.parent_id ? metadata.parent_id : '';
        if (!parentID) aggregate.toolResultParentMissingCount += 1;
        else {
          aggregate.toolResultParentPresentCount += 1;
          const invocationRecipient = aggregate.toolInvocationIdentityByID.get(parentID);
          if (invocationRecipient) {
            aggregate.toolResultParentMatchCount += 1;
            if (message.author && message.author.name === invocationRecipient) aggregate.toolResultAuthorRecipientMatchCount += 1;
          } else aggregate.toolResultParentUnmatchedCount += 1;
        }
        post({ kind: 'native_tool_activity', state: 'result', titleCharacters: rawTitle.length });
      };

      const scrubTextPatches = (node, aggregate) => {
        if (Array.isArray(node)) {
          const output = [];
          let removedTextPatchCount = 0;
          let removedTextCharacters = 0;
          for (const item of node) {
            const result = scrubTextPatches(item, aggregate);
            removedTextPatchCount += result.removedTextPatchCount;
            removedTextCharacters += result.removedTextCharacters;
            if (!result.skip) output.push(result.value);
          }
          return { value: output, skip: false, removedTextPatchCount, removedTextCharacters };
        }
        if (node && typeof node === 'object') {
          if (node.o === 'append' && node.p === '/message/content/parts/0' && typeof node.v === 'string') {
            postTextDelta(node.v, aggregate);
            return { value: null, skip: true, removedTextPatchCount: 1, removedTextCharacters: node.v.length };
          }
          const output = {};
          let removedTextPatchCount = 0;
          let removedTextCharacters = 0;
          for (const [key, child] of Object.entries(node)) {
            const result = scrubTextPatches(child, aggregate);
            removedTextPatchCount += result.removedTextPatchCount;
            removedTextCharacters += result.removedTextCharacters;
            if (!result.skip) output[key] = result.value;
          }
          return { value: output, skip: false, removedTextPatchCount, removedTextCharacters };
        }
        return { value: node, skip: false, removedTextPatchCount: 0, removedTextCharacters: 0 };
      };

      const streamMetrics = aggregate => ({
        frameCount: aggregate.frameCount,
        removedTextPatchCount: aggregate.removedTextPatchCount,
        removedTextCharacters: aggregate.removedTextCharacters,
        explicitTextPatchCount: aggregate.explicitTextPatchCount,
        exactTopLevelTextPatchCount: aggregate.exactTopLevelTextPatchCount,
        rootNonExactTextPatchCount: aggregate.rootNonExactTextPatchCount,
        nestedTextPatchCount: aggregate.nestedTextPatchCount,
        contextualValueStringCount: aggregate.contextualValueStringCount,
        contextualValueStringCharacters: aggregate.contextualValueStringCharacters,
        inactiveValueStringCount: aggregate.inactiveValueStringCount,
        inactiveValueStringCharacters: aggregate.inactiveValueStringCharacters,
        continuationResetWhileActiveCount: aggregate.continuationResetWhileActiveCount,
        firstInactiveValueContext: aggregate.firstInactiveValueContext,
        titleGenerationWhileContinuationCount: aggregate.titleGenerationWhileContinuationCount,
        structureSignatureCount: aggregate.structureSeen.size,
        structureSignatureOverflowCount: aggregate.structureSignatureOverflowCount,
        specialStructureSignatureCount: aggregate.specialStructureSeen.size,
        specialStructureSignatureOverflowCount: aggregate.specialStructureSignatureOverflowCount,
        phaseTextStructureSignatureCount: aggregate.phaseTextStructureSeen.size,
        phaseTextStructureSignatureOverflowCount: aggregate.phaseTextStructureSignatureOverflowCount,
        assistantTextMessageCount: aggregate.assistantTextMessageCount,
        assistantTextBeforeReasoningEndCount: aggregate.assistantTextBeforeReasoningEndCount,
        assistantTextAfterReasoningEndCount: aggregate.assistantTextAfterReasoningEndCount,
        reasoningEndMarkerCount: aggregate.reasoningEndMarkerCount,
        reasoningPreambleCount: aggregate.reasoningPreambleCount,
        reasoningPreambleCharacters: aggregate.reasoningPreambleCharacters,
        reasoningActiveSignalCount: aggregate.reasoningActiveSignalCount,
        reasoningSegmentBreakCount: aggregate.reasoningSegmentBreakCount,
        toolInvocationIdentityCount: aggregate.toolInvocationIdentityByID.size,
        toolInvocationCount: aggregate.toolInvocationCount,
        toolInvocationWithTitleCount: aggregate.toolInvocationWithTitleCount,
        toolResultCount: aggregate.toolResultCount,
        toolResultWithTitleCount: aggregate.toolResultWithTitleCount,
        toolResultParentPresentCount: aggregate.toolResultParentPresentCount,
        toolResultParentMatchCount: aggregate.toolResultParentMatchCount,
        toolResultParentUnmatchedCount: aggregate.toolResultParentUnmatchedCount,
        toolResultParentMissingCount: aggregate.toolResultParentMissingCount,
        toolResultAuthorRecipientMatchCount: aggregate.toolResultAuthorRecipientMatchCount
      });

      const filterFrame = (frame, aggregate) => {
        const lines = String(frame || '').split('\n');
        const dataLines = lines.filter(line => line.startsWith('data:'));
        if (!dataLines.length) return frame + '\n\n';
        const data = dataLines.map(line => line.slice(5).trimStart()).join('\n');
        aggregate.frameCount += 1;
        if (data.trim() === '[DONE]') {
          aggregate.terminal = true;
          aggregate.textContinuationActive = false;
          activeSend = false;
          const metrics = webMetrics();
          queueMicrotask(() => {
            probeComposer(true);
            post(Object.assign({ kind: 'stream_metrics', terminal: true }, streamMetrics(aggregate), metrics));
          });
          return frame + '\n\n';
        }
        let payload;
        try { payload = JSON.parse(data); }
        catch (_) {
          if (aggregate.textContinuationActive) {
            aggregate.continuationResetWhileActiveCount += 1;
            aggregate.inactiveContext = 'after_parse_failure';
          }
          aggregate.textContinuationActive = false;
          return frame + '\n\n';
        }

        observeStructure(payload, aggregate);
        observeReasoningActive(payload, aggregate);
        observeReasoningPreamble(payload, aggregate);
        observeToolActivity(payload, aggregate);
        observeReasoningEnd(payload, aggregate);
        const payloadKeys = payload && typeof payload === 'object' && !Array.isArray(payload) ? Object.keys(payload) : [];
        const rootTextAppend = payload && typeof payload === 'object' && !Array.isArray(payload) && payload.o === 'append' && payload.p === '/message/content/parts/0' && typeof payload.v === 'string';
        const exactTopLevelTextAppend = payloadKeys.length === 3 && payloadKeys.includes('o') && payloadKeys.includes('p') && payloadKeys.includes('v') && rootTextAppend;
        if (exactTopLevelTextAppend) {
          aggregate.textContinuationActive = true;
          aggregate.inactiveContext = 'after_exact_root';
          aggregate.removedTextPatchCount += 1;
          aggregate.removedTextCharacters += payload.v.length;
          aggregate.explicitTextPatchCount += 1;
          aggregate.exactTopLevelTextPatchCount += 1;
          postTextDelta(payload.v, aggregate);
          return '';
        }

        const contextualValueString = aggregate.textContinuationActive && payloadKeys.length === 1 && payloadKeys[0] === 'v' && typeof payload.v === 'string';
        if (contextualValueString) {
          aggregate.removedTextPatchCount += 1;
          aggregate.removedTextCharacters += payload.v.length;
          aggregate.contextualValueStringCount += 1;
          aggregate.contextualValueStringCharacters += payload.v.length;
          postTextDelta(payload.v, aggregate);
          return '';
        }

        const titleGenerationWhileContinuation = aggregate.textContinuationActive && payload && typeof payload === 'object' && !Array.isArray(payload) && payload.type === 'title_generation' && !Object.prototype.hasOwnProperty.call(payload, 'o') && !Object.prototype.hasOwnProperty.call(payload, 'p');
        if (titleGenerationWhileContinuation) {
          aggregate.titleGenerationWhileContinuationCount += 1;
          const nonDataLines = lines.filter(line => !line.startsWith('data:'));
          return nonDataLines.concat(['data: ' + JSON.stringify(payload)]).join('\n') + '\n\n';
        }

        const inactiveValueString = !aggregate.textContinuationActive && payloadKeys.length === 1 && payloadKeys[0] === 'v' && typeof payload.v === 'string';
        if (inactiveValueString) {
          aggregate.inactiveValueStringCount += 1;
          aggregate.inactiveValueStringCharacters += payload.v.length;
          if (aggregate.firstInactiveValueContext === 'none') aggregate.firstInactiveValueContext = aggregate.inactiveContext || 'unknown';
        }

        const continuationWasActive = aggregate.textContinuationActive;
        if (continuationWasActive) {
          aggregate.continuationResetWhileActiveCount += 1;
          aggregate.inactiveContext = 'after_reset';
        }
        aggregate.textContinuationActive = false;
        const result = scrubTextPatches(payload, aggregate);
        aggregate.removedTextPatchCount += result.removedTextPatchCount;
        aggregate.removedTextCharacters += result.removedTextCharacters;
        aggregate.explicitTextPatchCount += result.removedTextPatchCount;
        if (result.removedTextPatchCount > 0) {
          if (rootTextAppend) {
            aggregate.rootNonExactTextPatchCount += 1;
            aggregate.inactiveContext = 'after_nonexact_root';
          } else {
            aggregate.nestedTextPatchCount += result.removedTextPatchCount;
            aggregate.inactiveContext = 'after_nested';
          }
        }
        if (result.skip) return '';
        const nonDataLines = lines.filter(line => !line.startsWith('data:'));
        return nonDataLines.concat(['data: ' + JSON.stringify(result.value)]).join('\n') + '\n\n';
      };

      const filteredResponse = response => {
        if (!response.body || typeof response.body.getReader !== 'function' || typeof ReadableStream !== 'function') return response;
        const reader = response.body.getReader();
        const aggregate = {
          frameCount: 0,
          removedTextPatchCount: 0,
          removedTextCharacters: 0,
          explicitTextPatchCount: 0,
          exactTopLevelTextPatchCount: 0,
          rootNonExactTextPatchCount: 0,
          nestedTextPatchCount: 0,
          contextualValueStringCount: 0,
          contextualValueStringCharacters: 0,
          inactiveValueStringCount: 0,
          inactiveValueStringCharacters: 0,
          continuationResetWhileActiveCount: 0,
          firstInactiveValueContext: 'none',
          inactiveContext: 'no_prior_text',
          titleGenerationWhileContinuationCount: 0,
          textContinuationActive: false,
          structureSeen: new Set(),
          structureSignatureOverflowCount: 0,
          specialStructureSeen: new Set(),
          specialStructureSignatureOverflowCount: 0,
          phaseTextStructureSeen: new Set(),
          phaseTextStructureSignatureOverflowCount: 0,
          assistantTextMessageCount: 0,
          assistantTextBeforeReasoningEndCount: 0,
          assistantTextAfterReasoningEndCount: 0,
          reasoningEnded: false,
          reasoningEndMarkerCount: 0,
          reasoningPreambleSeen: new Set(),
          reasoningPreambleCount: 0,
          reasoningPreambleCharacters: 0,
          reasoningActiveSeen: new Set(),
          reasoningActiveSignalCount: 0,
          reasoningSegmentBreakCount: 0,
          toolActivitySeen: new Set(),
          toolInvocationIdentityByID: new Map(),
          toolInvocationCount: 0,
          toolInvocationWithTitleCount: 0,
          toolResultCount: 0,
          toolResultWithTitleCount: 0,
          toolResultParentPresentCount: 0,
          toolResultParentMatchCount: 0,
          toolResultParentUnmatchedCount: 0,
          toolResultParentMissingCount: 0,
          toolResultAuthorRecipientMatchCount: 0,
          terminal: false
        };
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
                    aggregate.textContinuationActive = false;
                    activeSend = false;
                    const metrics = webMetrics();
                    probeComposer(true);
                    post(Object.assign({ kind: 'stream_metrics', terminal: false }, streamMetrics(aggregate), metrics));
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
              aggregate.textContinuationActive = false;
              activeSend = false;
              post({ kind: 'stream_error', state: 'reader_failed' });
              try { controller.error(new Error('native_web_send_engine_stream_failed')); } catch (_) {}
            }
          },
          cancel(reason) { aggregate.textContinuationActive = false; try { reader.cancel(reason); } catch (_) {} }
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
        probeComposer(true);
        try {
          const response = await originalFetch(input, init);
          const contentType = String(response.headers.get('content-type') || '').split(';')[0].trim().toLowerCase();
          const filtered = response.status === 200 && contentType === 'text/event-stream';
          post({ kind: 'send_response', status: response.status, contentType, filtered });
          if (!filtered) {
            activeSend = false;
            probeComposer(true);
            post({ kind: 'stream_error', state: 'send_not_sse' });
            return response;
          }
          return filteredResponse(response);
        } catch (error) {
          activeSend = false;
          probeComposer(true);
          post({ kind: 'stream_error', state: 'send_transport_error' });
          throw error;
        }
      };

      const observer = new MutationObserver(() => probeComposer(false));
      const start = () => {
        installRenderSuppression();
        probeComposer(true);
        observer.observe(document.documentElement || document, { childList: true, subtree: true });
        post({ kind: 'probe_ready' });
      };
      if (document.documentElement) start();
      else document.addEventListener('DOMContentLoaded', start, { once: true });

      window.__nativeWebSendEngineProbe = { submit, probeComposer };
    })();
    """#
}
