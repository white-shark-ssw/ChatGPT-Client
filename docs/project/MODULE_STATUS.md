# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Candidate** | `AppDelegate.swift`, `RootViewController.swift`; `DEV-native-read-path-0.1.0-b8` | Diagnostic landing screen replaced by native UIKit split sidebar/detail shell. b8 CI/artifact passed; compact-width/iPad runtime behavior remains unverified. Not Frozen. |
| Build/runtime metadata | Stable | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | Exact candidate/source/deployment/runtime identity is embedded. Current active test candidate is b8/build 8; accepted runtime baseline remains b7 until b8 real-device acceptance. Not Frozen. |
| Diagnostics / logging | Stable | `Diagnostics.swift` | Structured OSLog + bounded JSONL + redacted export + clear control. Native read path records route/status/bytes/count lifecycle evidence without chat bodies or secrets. Not Frozen. |
| IPA build / CI packaging | Stable | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml` | b8 source `e312acc3dd17cdcdb01746bb76f70556510a0304` run `32976656499` passed; artifact ID `9609766005`; IPA SHA-256 `50bfb7453443c41de8661c1ffc3e2a7076fd939fe62453aceacb599371862acd`. Not Frozen. |
| Embedded web login | Stable | `AuthWebViewController.swift`; b2+ | Continue with Google and persistent default `WKWebsiteDataStore` authentication accepted. Not Frozen. |
| Authentication/account context | Stable | `AuthSessionStore.swift`; b6 + b7 regression evidence | Ordered plus/personal account context accepted. No automatic retry. Native repository reuses this owner rather than duplicating auth state. Not Frozen. |
| Protocol-read diagnostic transport | **Stable for accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; `DEV-protocol-read-0.1.0-b7` | **Code + CI + Artifact + real-device tested.** Diagnostic-only; untouched by b8 and not a production repository. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable for tested scope** | `DEV-protocol-read-0.1.0-b7` | List/detail protocol evidence accepted on iPhone / iOS 17.0 for Plus/personal. Not Frozen. |
| Native conversation read path | **Candidate** | `ConversationRepository` + sidebar/detail/message UI; `DEV-native-read-path-0.1.0-b8` | **Code written + CI passed + Artifact produced.** Owns production list, selected conversation identity, loaded detail and current visible user/assistant branch. Walks `current_node -> parent` and virtualizes rendering. Runtime/manual/real-device acceptance pending. |
| Streaming / send / attachments | Unknown / Unverified | Future development tasks | Not proven by b7/b8 read work. |

## Allowed statuses

Use concise statuses such as Active, Candidate, Stable, Frozen, Experimental, Deprecated, or Unknown / Unverified.

## Frozen rule

Before changing a Frozen or Stable core module for an unrelated task, verify the task truly requires it and record the evidence. Stable does not mean Frozen.

## Current acceptance boundary

- `DEV-app-foundation-0.1.0-b1`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; foundation Stable, not Frozen.
- `DEV-auth-bootstrap-0.1.0-b6`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; auth/account context Stable for the tested iPhone / iOS 17.0 scope.
- `DEV-protocol-read-0.1.0-b7`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; current Plus/personal conversation-list + one-detail protocol accepted on iPhone / iOS 17.0.
- `DEV-native-read-path-0.1.0-b8`: **Code written + CI passed + Artifact produced**; production native conversation owner/shell is Candidate only. Runtime/manual/real-device testing pending; not Stable/Frozen.

Runtime compatibility below iOS 17.0, iPad, non-personal workspace behavior, send/streaming and attachments remain unverified.

## Auto-refresh rule

Update this matrix when modules are added, ownership changes, a module becomes stable/frozen, a frozen decision is reopened, or a new candidate supersedes an old baseline.
