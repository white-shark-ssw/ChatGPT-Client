# Official iOS Sync / Reload Inspector

Research-only runtime inspector for `DEV-official-sync-reload`.

## v0.1 purpose

v0.1 does **not** invoke Sync, Reload, refresh, polling, Send, regenerate or Stop. It only records privacy-safe runtime structure needed to identify the official app's real current-conversation owner before a mutating control is added.

The inspector checks availability and Objective-C runtime metadata for the current exact official binary's candidate types, including:

- `ChatGPTConversation.ConversationViewModel`
- `ChatGPTHistory.HistoryViewController`
- `Conversations.DefaultConversationRepository`
- `Conversations.DefaultConversationCoordinatorProvider`
- `Conversations.ConversationPollingManager`

It also records controller/view class names around the active official UI. It does not record conversation IDs, titles, prompts, response text, request headers, cookies, tokens or URLs.

## Build

```sh
bash scripts/research/official_ios_sync_reload/build_inspector.sh build/sync-reload-inspector
```

Output:

- `ChatGPTSyncReloadInspector.dylib`
- `ChatGPTSyncReloadInspector.dylib.sha256`

The build is arm64 / iOS 17.0+ and uses only Foundation/UIKit plus the Objective-C runtime available from the system toolchain.

## Research package chaining

The exact supplied official package already has `Assets.framework` weak-loading:

`@rpath/ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib`

For a task-local research package only:

1. keep the original enhancer bytes as `ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.original.dylib`;
2. place the inspector dylib at the original enhancer filename so the existing weak-load entry loads it;
3. `EnhancerChain.m` loads the backup original enhancer first;
4. preserve the official bundle identity/version/build unless a later evidenced reason requires otherwise.

Do not use the parallel `official_ios_realtime_probe` dylib as this task's state owner or overwrite its research artifact. Each research IPA must have its own exact hash/identity.

## Runtime procedure

1. Fully launch the research package.
2. Open a normal existing conversation so the official conversation UI is live.
3. Tap the floating `SR` control.
4. Choose `检查运行时` once.
5. Choose `导出日志` and provide `ChatGPTSyncReloadInspector.jsonl` for analysis.

The decisive v0.1 evidence is whether the candidate official types are present in the Objective-C runtime, which relevant selectors are actually exposed, and which official controller/view classes are live around the selected conversation.

Only after that evidence identifies a real owner should a later version add `同步` / `重载` mutations. Static Swift symbol strings alone are not sufficient evidence to call a method safely.
