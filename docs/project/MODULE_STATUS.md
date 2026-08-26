# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable for tested scope** | `AppDelegate.swift`, `RootViewController.swift`; `DEV-native-read-path-0.1.0-b9` | Split sidebar/detail shell and two selected conversation reads were real-device accepted on iPhone/iOS 17.0. PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`. Compact-width breadth beyond tested path remains Unverified. Not Frozen. |
| Build/runtime metadata | Stable | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | b9 exact version/build/source/runtime identity matched exported diagnostics. Not Frozen. |
| Diagnostics / logging | Stable | `Diagnostics.swift` | Structured OSLog + bounded JSONL + redacted export + clear control. b9 `conversationHash` + list position correlated two distinct real-device selections without raw conversation IDs/bodies. Not Frozen. |
| IPA build / CI packaging | Stable | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml` | b9 source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7` run `32978476582` passed; artifact ID `9610449216`; IPA SHA-256 `16168a9db6f03e4ab00ddae4149451563a31fe2862cfb7ab18320329d186b99e`. Not Frozen. |
| Embedded web login | Stable | `AuthWebViewController.swift`; b2+ | Embedded Google login remains accepted. b9 began with 0/0 WebKit cookies and required explicit login verification, so install/update auth persistence remains Unverified. Not Frozen. |
| Authentication/account context | Stable | `AuthSessionStore.swift`; b6/b7 + b9 production reuse evidence | Plus/personal account context verified in b9 after explicit login; native reads reused the same owner. No automatic retry. Not Frozen. |
| Protocol-read diagnostic transport | **Stable for accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; `DEV-protocol-read-0.1.0-b7` | **Code + CI + Artifact + real-device tested.** Diagnostic-only; not production state owner. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable for tested scope** | b7 diagnostic + b9 production runtime evidence | b9 confirms current production list/detail transport can succeed for two distinct Plus/personal conversations. Earlier b8 one-off HTTP 500 is not evidence of a systematic current failure. Not Frozen. |
| Native conversation read path | **Stable for tested scope** | `ConversationRepository` + sidebar/detail/message UI; `DEV-native-read-path-0.1.0-b9` | **Code + CI + Artifact + real-device tested** for shell/list/two-detail/current visible branch on iPhone/iOS 17.0. Position 1: 1.53 MB / 337 mapping / 154 visible / 5.67 s; position 13: 7.50 MB / 2023 mapping / 843 visible / 20.74 s. PR #9 merged. Terminal manual reload was not triggered; its failure-path runtime behavior remains Unverified. Not Frozen. |
| Streaming / send / attachments | Unknown / Unverified | Future development tasks | Not proven by b7-b9 read work. |

## Allowed statuses

Use concise statuses such as Active, Candidate, Accepted Candidate, Stable, Frozen, Experimental, Deprecated, or Unknown / Unverified.

## Frozen rule

Before changing a Frozen or Stable core module for an unrelated task, verify the task truly requires it and record the evidence. Stable does not mean Frozen.

## Current acceptance boundary

- `DEV-app-foundation-0.1.0-b1`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; foundation Stable, not Frozen.
- `DEV-auth-bootstrap-0.1.0-b6`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; auth/account context Stable for tested iPhone/iOS 17.0 scope.
- `DEV-protocol-read-0.1.0-b7`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; Plus/personal list + one-detail diagnostic protocol accepted.
- `DEV-native-read-path-0.1.0-b8`: **Code + CI + Artifact + real-device tested, partial/failing acceptance**; historical predecessor with one detail HTTP 500 before parse/render.
- `DEV-native-read-path-0.1.0-b9`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** for native shell/list/two-detail/current-branch message rendering; merged and Stable for tested scope. Terminal detail reload and install/update auth persistence remain separately Unverified.

Runtime compatibility below iOS 17.0, iPad, non-personal workspace behavior, send/streaming and attachments remain unverified.

## Auto-refresh rule

Update this matrix when modules are added, ownership changes, a module becomes stable/frozen, a frozen decision is reopened, or a new candidate supersedes an old baseline.
