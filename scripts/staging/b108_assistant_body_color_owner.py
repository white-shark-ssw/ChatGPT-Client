from pathlib import Path

project = Path("ChatGPTClient.xcodeproj/project.pbxproj")
conversation = Path("ChatGPTClient/Conversation/ConversationFeature.swift")

project_text = project.read_text()
old_build = "CURRENT_PROJECT_VERSION = 107;"
old_candidate = 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b107";'
if project_text.count(old_build) != 2:
    raise SystemExit(f"expected 2 Build107 settings, got {project_text.count(old_build)}")
if project_text.count(old_candidate) != 2:
    raise SystemExit(f"expected 2 b107 candidate settings, got {project_text.count(old_candidate)}")
project_text = project_text.replace(old_build, "CURRENT_PROJECT_VERSION = 108;")
project_text = project_text.replace(old_candidate, 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b108";')
project.write_text(project_text)

text = conversation.read_text()
old = '''    switch message.role {
    case .assistant: messageLabel.attributedText = Self.assistantBodyAttributedText(text)
    case .user: messageLabel.attributedText = Self.userBodyAttributedText(text)
    }
'''
new = '''    switch message.role {
    case .assistant: messageLabel.attributedText = Self.assistantBodyAttributedText(text); messageLabel.textColor = .label
    case .user: messageLabel.attributedText = Self.userBodyAttributedText(text)
    }
'''
if text.count(old) != 1:
    raise SystemExit(f"expected one assistant body configure switch, got {text.count(old)}")
text = text.replace(old, new)
conversation.write_text(text)

print("b108 assistant body final UILabel color owner applied")
