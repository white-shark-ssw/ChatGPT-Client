from pathlib import Path

BASE = "367e9588d10dcf164b2982729a663ac0cde91d9c"
conversation_path = Path("ChatGPTClient/Conversation/ConversationFeature.swift")
project_path = Path("ChatGPTClient.xcodeproj/project.pbxproj")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly 1 anchor, found {count}")
    return text.replace(old, new, 1)


text = conversation_path.read_text()

text = replace_once(
    text,
    "    static func visibleToolItems(_ timeline: [ConversationResponseTimelineItem]) -> [ConversationResponseTimelineItem] {\n        timeline.filter { item in\n            guard item.kind == .tool else { return false }\n            let title = item.text.trimmingCharacters(in: .whitespacesAndNewlines)\n            guard !title.isEmpty else { return false }\n            return !(title == \"工具调用\" && item.toolInputJSON.isEmpty && item.toolOutputJSON.isEmpty)\n        }\n    }",
    "    static func toolListItems(_ timeline: [ConversationResponseTimelineItem]) -> [ConversationResponseTimelineItem] {\n        timeline.filter { item in\n            guard item.kind == .tool else { return false }\n            return !item.text.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty\n        }\n    }\n\n    static func inlineToolItems(_ timeline: [ConversationResponseTimelineItem]) -> [ConversationResponseTimelineItem] {\n        toolListItems(timeline).filter { $0.text.trimmingCharacters(in: .whitespacesAndNewlines) != \"工具调用\" }\n    }",
    "tool selectors",
)

text = text.replace("for item in visibleToolItems(timeline) {", "for item in inlineToolItems(timeline) {")
text = text.replace("ConversationReasoningPresentation.visibleToolItems([item]).isEmpty", "ConversationReasoningPresentation.inlineToolItems([item]).isEmpty")
text = text.replace("let tools = ConversationReasoningPresentation.visibleToolItems(message.responseTimeline)", "let tools = ConversationReasoningPresentation.toolListItems(message.responseTimeline)")
text = text.replace("!ConversationReasoningPresentation.visibleToolItems(responseTimeline).isEmpty", "!ConversationReasoningPresentation.inlineToolItems(responseTimeline).isEmpty")
text = text.replace("for item in ConversationReasoningPresentation.visibleToolItems(timeline) {", "for item in ConversationReasoningPresentation.toolListItems(timeline) {")
if "visibleToolItems" in text:
    raise SystemExit("visibleToolItems reference remains after split")

text = replace_once(
    text,
    "    private static let bodyFont = UIFont.preferredFont(forTextStyle: .body)\n    private static let reasoningFont = UIFont.preferredFont(forTextStyle: .subheadline)\n    private static let toolFont = UIFont.systemFont(ofSize: reasoningFont.pointSize, weight: .medium)",
    "    private static let bodyFont = UIFont.preferredFont(forTextStyle: .body)\n    private static let reasoningFont = bodyFont\n    private static let toolFont = UIFont.systemFont(ofSize: bodyFont.pointSize, weight: .regular)",
    "main reasoning fonts",
)

text = replace_once(
    text,
    "        let reasoningParagraph = NSMutableParagraphStyle()\n        reasoningParagraph.paragraphSpacing = 5\n        let toolParagraph = NSMutableParagraphStyle()\n        toolParagraph.paragraphSpacing = 5\n        let reasoningAttributes: [NSAttributedString.Key: Any] = [.font: reasoningFont, .foregroundColor: UIColor.secondaryLabel, .paragraphStyle: reasoningParagraph]\n        let toolAttributes: [NSAttributedString.Key: Any] = [.font: toolFont, .foregroundColor: UIColor.secondaryLabel, .paragraphStyle: toolParagraph]",
    "        let reasoningParagraph = NSMutableParagraphStyle()\n        reasoningParagraph.minimumLineHeight = 26\n        reasoningParagraph.lineSpacing = 2\n        reasoningParagraph.paragraphSpacing = 8\n        let toolParagraph = NSMutableParagraphStyle()\n        toolParagraph.minimumLineHeight = 30\n        toolParagraph.paragraphSpacing = 9\n        let reasoningAttributes: [NSAttributedString.Key: Any] = [.font: reasoningFont, .foregroundColor: UIColor.label, .paragraphStyle: reasoningParagraph]\n        let toolAttributes: [NSAttributedString.Key: Any] = [.font: toolFont, .foregroundColor: UIColor.secondaryLabel, .paragraphStyle: toolParagraph]",
    "inline reasoning typography",
)

text = replace_once(
    text,
    "    private var expandedReasoningMessageIDsByConversationID: [String: Set<String>] = [:]",
    "    private var expandedReasoningMessageIDsByConversationID: [String: Set<String>] = [:]\n    private var autoOpenedLiveReasoningMessageIDsByConversationID: [String: Set<String>] = [:]\n    private var autoCollapsedLiveReasoningMessageIDsByConversationID: [String: Set<String>] = [:]",
    "live disclosure state",
)

text = replace_once(
    text,
    "        expandedReasoningMessageIDsByConversationID.removeAll()",
    "        expandedReasoningMessageIDsByConversationID.removeAll()\n        autoOpenedLiveReasoningMessageIDsByConversationID.removeAll()\n        autoCollapsedLiveReasoningMessageIDsByConversationID.removeAll()",
    "live disclosure reset",
)

text = replace_once(
    text,
    "    let userMessage = ConversationMessage(id: \"local-live-user-\\(snapshot.generation)\", role: .user, text: snapshot.promptText, responseTimeline: [], reasoningDurationSeconds: nil, createTime: nil)\n    let assistantMessage = ConversationMessage(id: \"local-live-response-\\(snapshot.generation)\", role: .assistant, text: bodyText, responseTimeline: snapshot.timeline, reasoningDurationSeconds: snapshot.reasoningDurationSeconds, createTime: nil)\n    livePresentationMessages = [userMessage, assistantMessage]",
    "    let userMessage = ConversationMessage(id: \"local-live-user-\\(snapshot.generation)\", role: .user, text: snapshot.promptText, responseTimeline: [], reasoningDurationSeconds: nil, createTime: nil)\n    let assistantMessage = ConversationMessage(id: \"local-live-response-\\(snapshot.generation)\", role: .assistant, text: bodyText, responseTimeline: snapshot.timeline, reasoningDurationSeconds: snapshot.reasoningDurationSeconds, createTime: nil)\n    synchronizeLiveReasoningDisclosure(snapshot: snapshot, messageID: assistantMessage.id, conversationID: id)\n    livePresentationMessages = [userMessage, assistantMessage]",
    "live disclosure sync call",
)

text = replace_once(
    text,
    "    private func isReasoningExpanded(messageID: String, conversationID: String) -> Bool {\n        expandedReasoningMessageIDsByConversationID[conversationID]?.contains(messageID) == true\n    }",
    "    private func synchronizeLiveReasoningDisclosure(snapshot: ConversationLiveResponseSnapshot, messageID: String, conversationID: String) {\n        guard !snapshot.timeline.isEmpty else { return }\n        var autoOpened = autoOpenedLiveReasoningMessageIDsByConversationID[conversationID] ?? []\n        var autoCollapsed = autoCollapsedLiveReasoningMessageIDsByConversationID[conversationID] ?? []\n        var expanded = expandedReasoningMessageIDsByConversationID[conversationID] ?? []\n        var expansionChanged = false\n        if !snapshot.reasoningEnded, !autoOpened.contains(messageID) {\n            autoOpened.insert(messageID)\n            expanded.insert(messageID)\n            expansionChanged = true\n        }\n        if snapshot.reasoningEnded, !autoCollapsed.contains(messageID) {\n            autoCollapsed.insert(messageID)\n            expanded.remove(messageID)\n            expansionChanged = true\n        }\n        autoOpenedLiveReasoningMessageIDsByConversationID[conversationID] = autoOpened\n        autoCollapsedLiveReasoningMessageIDsByConversationID[conversationID] = autoCollapsed\n        if expansionChanged { expandedReasoningMessageIDsByConversationID[conversationID] = expanded }\n    }\n\n    private func isReasoningExpanded(messageID: String, conversationID: String) -> Bool {\n        expandedReasoningMessageIDsByConversationID[conversationID]?.contains(messageID) == true\n    }",
    "live disclosure synchronizer",
)

conversation_path.write_text(text)

project = project_path.read_text()
if project.count("CURRENT_PROJECT_VERSION = 72;") != 2:
    raise SystemExit("expected two Build72 project-version anchors")
if project.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b72";') != 2:
    raise SystemExit("expected two b72 diagnostics candidate anchors")
project = project.replace("CURRENT_PROJECT_VERSION = 72;", "CURRENT_PROJECT_VERSION = 73;")
project = project.replace('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b72";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b73";')
project_path.write_text(project)

if "sendExecutors:" not in Path("ChatGPTClient/RootViewController.swift").read_text():
    raise SystemExit("b72 per-conversation executor baseline missing")

print("b73 presentation patch applied")
