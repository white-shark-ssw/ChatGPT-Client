from pathlib import Path


script_path = Path("scripts/staging/b105_new_chat_first_send.py")
source = script_path.read_text()
old_call = '''text = replace_once(text, \'\'\'        composerReadyConversationID = nil\n        currentConversationID = conversationID\n\'\'\', \'\'\'        composerReadyConversationID = nil\n        rootComposerReady = false\n        currentConversationID = conversationID\n\'\'\', "observe clears root composer")'''
new_call = '''old_observe_target = \'\'\'        composerReadyConversationID = nil\n        currentConversationID = conversationID\n\'\'\'\nnew_observe_target = \'\'\'        composerReadyConversationID = nil\n        rootComposerReady = false\n        currentConversationID = conversationID\n\'\'\'\nobserve_start = text.index("    func observeExistingConversation(")\nobserve_end = text.index("    func reactivateExternalObservationFocus()", observe_start)\nobserve_chunk = text[observe_start:observe_end]\nif observe_chunk.count(old_observe_target) != 1:\n    raise SystemExit(f"observe clears root composer: expected one scoped match, found {observe_chunk.count(old_observe_target)}")\ntext = text[:observe_start] + observe_chunk.replace(old_observe_target, new_observe_target, 1) + text[observe_end:]'''
if source.count(old_call) != 1:
    raise SystemExit(f"runner patch: expected one source call, found {source.count(old_call)}")
corrected = source.replace(old_call, new_call, 1)
exec(compile(corrected, str(script_path), "exec"))
