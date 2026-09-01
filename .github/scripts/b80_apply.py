from pathlib import Path


def replace_exact(path, old, new, expected=1):
    text = path.read_text()
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{path}: expected {expected} matches, got {count}: {old[:120]!r}")
    path.write_text(text.replace(old, new, expected))


feature = Path("ChatGPTClient/Conversation/ConversationFeature.swift")
replace_exact(feature, "Self.responseTimelineAttributedText(responseTimeline, disclosureState: toolDisclosureState)", "Self.responseTimelineAttributedText(responseTimeline, disclosureState: toolDisclosureState, trailingSeparator: showsReasoningDivider)")
replace_exact(feature, "measuredTimelineSize(responseTimeline, maxWidth: maxTextWidth, disclosureState: toolDisclosureState)", "measuredTimelineSize(responseTimeline, maxWidth: maxTextWidth, disclosureState: toolDisclosureState, trailingSeparator: showsReasoningDivider)")
replace_exact(feature, "    private static func responseTimelineAttributedText(_ timeline: [ConversationResponseTimelineItem], disclosureState: ConversationToolDisclosureState) -> NSAttributedString {", "    private static func responseTimelineAttributedText(_ timeline: [ConversationResponseTimelineItem], disclosureState: ConversationToolDisclosureState, trailingSeparator: Bool) -> NSAttributedString {")
replace_exact(feature, "        return output\n    }\n\n    private static func appendToolIcon", "        if trailingSeparator, output.length > 0 { output.append(NSAttributedString(string: \"\\n\\u{200B}\\n\", attributes: separatorAttributes)) }\n        return output\n    }\n\n    private static func appendToolIcon")
replace_exact(feature, "    private static func measuredTimelineSize(_ timeline: [ConversationResponseTimelineItem], maxWidth: CGFloat, disclosureState: ConversationToolDisclosureState) -> CGSize {\n        let attributed = responseTimelineAttributedText(timeline, disclosureState: disclosureState)", "    private static func measuredTimelineSize(_ timeline: [ConversationResponseTimelineItem], maxWidth: CGFloat, disclosureState: ConversationToolDisclosureState, trailingSeparator: Bool) -> CGSize {\n        let attributed = responseTimelineAttributedText(timeline, disclosureState: disclosureState, trailingSeparator: trailingSeparator)")
replace_exact(feature, "        if showsReasoningDivider {\n            bubbleY += 12\n            reasoningDividerFrame = CGRect(x: contentInset, y: bubbleY, width: maxTextWidth, height: 1 / UIScreen.main.scale)", "        if showsReasoningDivider {\n            reasoningDividerFrame = CGRect(x: contentInset, y: bubbleY, width: maxTextWidth, height: 1 / UIScreen.main.scale)")

root = Path("ChatGPTClient/RootViewController.swift")
replace_exact(root, "                  if (externalStreamingState.completePending) {\n                    externalStreamingState.active = false;\n                    externalStreamingState.completePending = false;\n                  }\n", "")
replace_exact(root, "                if complete {\n                    self.repository.consumeLiveResponseEvent(.terminal, conversationID: conversationID, generation: generation)\n                    self.releaseExecutor(for: conversationID, expected: sendExecutor)\n                    self.reconcileTerminalResponse(conversationID: conversationID, generation: generation)\n                }", "                if complete {\n                    guard let snapshot = self.repository.liveResponse(for: conversationID), snapshot.generation == generation else { return }\n                    if snapshot.reasoningEnded && snapshot.finalText.isEmpty {\n                        var fields = self.repository.diagnosticsFields(for: conversationID)\n                        fields[\"responseGeneration\"] = String(generation)\n                        fields[\"reason\"] = \"final_not_materialized\"\n                        self.diagnostics.info(category: \"webSend\", name: \"coveredExecutor.externalCompletionDeferred\", fields: fields)\n                        return\n                    }\n                    self.repository.consumeLiveResponseEvent(.terminal, conversationID: conversationID, generation: generation)\n                    self.releaseExecutor(for: conversationID, expected: sendExecutor)\n                    self.reconcileTerminalResponse(conversationID: conversationID, generation: generation)\n                }")

pbx = Path("ChatGPTClient.xcodeproj/project.pbxproj")
text = pbx.read_text()
if text.count("CURRENT_PROJECT_VERSION = 79;") != 2 or text.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b79";') != 2:
    raise SystemExit("unexpected b79 Xcode identity count")
text = text.replace("CURRENT_PROJECT_VERSION = 79;", "CURRENT_PROJECT_VERSION = 80;")
text = text.replace('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b79";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b80";')
pbx.write_text(text)

workflow = Path(".github/workflows/ios-foundation.yml")
text = workflow.read_text()
if text.count("DEV-send-stream-0.1.0-b79") != 2:
    raise SystemExit("unexpected b79 workflow identity count")
workflow.write_text(text.replace("DEV-send-stream-0.1.0-b79", "DEV-send-stream-0.1.0-b80"))
