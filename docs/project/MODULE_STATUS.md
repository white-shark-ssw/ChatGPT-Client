# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Candidate** | `AppDelegate.swift`, `RootViewController.swift`; `DEV-native-read-path-0.1.0-b9` | UIKit split sidebar/detail shell launched successfully in b8 real-device testing. b9 retains the shell and adds only detail diagnostics/reload. Compact-width detail UX still needs acceptance. Not Frozen. |
| Build/runtime metadata | Stable | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | Exact candidate/source/deployment/runtime identity is embedded. Current active test candidate is b9/build 9; accepted stable runtime read baseline remains b7. Not Frozen. |
| Diagnostics / logging | Stable | `Diagnostics.swift` | Structured OSLog + bounded JSONL + redacted export + clear control. b9 computes privacy-safe selected-conversation hash before logging and records list position; no raw conversation ID/body added. Not Frozen. |
| IPA build / CI packaging | Stable | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml` | b9 product/config source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7` run `32978476582` passed; artifact ID `9610449216`; IPA SHA-256 `16168a9db6f03e4ab00ddae4149451563a31fe2862cfb7ab18320329d186b99e`. Not Frozen. |
| Embedded web login | Stable | `AuthWebViewController.swift`; b2+ | Continue with Google and persistent default `WKWebsiteDataStore` authentication accepted in prior tested scope. b8 fresh install/update began with 0/0 cookies, so install/update persistence remains Unverified. Not Frozen. |
| Authentication/account context | Stable | `AuthSessionStore.swift`; b6/b7 accepted + b8 production reuse evidence | Ordered plus/personal account context accepted. b8 production repository reused this owner successfully after explicit login verification. No automatic retry. Not Frozen. |
| Protocol-read diagnostic transport | **Stable for accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; `DEV-protocol-read-0.1.0-b7` | **Code + CI + Artifact + real-device tested.** Diagnostic-only; untouched by b8/b9 and not a production repository. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable for tested scope** | `DEV-protocol-read-0.1.0-b7` | b7 list/detail protocol evidence accepted on iPhone/iOS 17.0 for Plus/personal. b8 later observed one selected production detail HTTP 500; this does not revoke b7 but requires conversation-specific/systematic discrimination. Not Frozen. |
| Native conversation read path | **Candidate** | `ConversationRepository` + sidebar/detail/message UI; `DEV-native-read-path-0.1.0-b9` | b8: shell + production list real-device proven after explicit login, but one detail failed HTTP 500 after 30.9 s before parse/render. b9: **Code written + CI passed + Artifact produced**, adds safe hash/list-position diagnostics and terminal explicit one-shot `重新加载`; runtime pending. Not Stable/Frozen. |
| Streaming / send / attachments | Unknown / Unverified | Future development tasks | Not proven by b7-b9 read work. |

## Allowed statuses

Use concise statuses such as Active, Candidate, Stable, Frozen, Experimental, Deprecated, or Unknown / Unverified.

## Frozen rule

Before changing a Frozen or Stable core module for an unrelated task, verify the task truly requires it and record the evidence. Stable does not mean Frozen.

## Current acceptance boundary

- `DEV-app-foundation-0.1.0-b1`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; foundation Stable, not Frozen.
- `DEV-auth-bootstrap-0.1.0-b6`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; auth/account context Stable for tested iPhone/iOS 17.0 scope.
- `DEV-protocol-read-0.1.0-b7`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; Plus/personal conversation-list + one-detail diagnostic protocol accepted on iPhone/iOS 17.0.
- `DEV-native-read-path-0.1.0-b8`: **Code + CI + Artifact + real-device tested, partial/failing acceptance**; shell/list passed after explicit login, one detail returned HTTP 500 before parse/render.
- `DEV-native-read-path-0.1.0-b9`: **Code written + CI passed + Artifact produced**; current candidate for discriminating detail failures. Runtime pending; not Stable/Frozen.

Runtime compatibility below iOS 17.0, iPad, non-personal workspace behavior, send/streaming and attachments remain unverified.

## Auto-refresh rule

Update this matrix when modules are added, ownership changes, a module becomes stable/frozen, a frozen decision is reopened, or a new candidate supersedes an old baseline.
