# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable for tested scope** | `AppDelegate.swift`, `RootViewController.swift`; `DEV-native-read-path-0.1.0-b9` | Split sidebar/detail shell and two selected conversation reads were real-device accepted on iPhone/iOS 17.0. PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`. Compact-width breadth beyond tested path remains Unverified. Not Frozen. |
| Build/runtime metadata | Stable | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | b9 runtime identity was accepted. b10 package inspection verifies `0.1.0 (10)`, candidate `DEV-conversation-recovery-0.1.0-b10`, source `89129913cb29`, minimum OS 14.0 and arm64; b10 runtime remains pending. Not Frozen. |
| Diagnostics / logging | Stable | `Diagnostics.swift` | Structured OSLog + bounded JSONL + redacted export + clear control. b10 reuses privacy-safe conversation hash/list position and adds recovery count/diff/state spans; new recovery events are not yet real-device accepted. Not Frozen. |
| IPA build / CI packaging | Stable | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml` | b10 source `89129913cb29a35db9dec7a6d5670d1b3b76bc23` run `32982836557` passed; artifact ID `9612167843`; IPA SHA-256 `6e600f829fa24cdeb705e9ab104ebb780a8c70dd06871285d06fa30521aecb7e`. Packaging capability remains Stable; b10 feature runtime is separately pending. Not Frozen. |
| Embedded web login | Stable | `AuthWebViewController.swift`; b2+ | Embedded Google login remains accepted. b9 began with 0/0 WebKit cookies and required explicit login verification, so install/update auth persistence remains Unverified. b10 does not change auth. Not Frozen. |
| Authentication/account context | Stable | `AuthSessionStore.swift`; b6/b7 + b9 production reuse evidence | Plus/personal account context verified in b9 after explicit login; b10 reuses the same owner without auth/header/endpoint changes. No automatic retry. Not Frozen. |
| Protocol-read diagnostic transport | **Stable for accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; `DEV-protocol-read-0.1.0-b7` | **Code + CI + Artifact + real-device tested.** Diagnostic-only; not production state owner. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable for tested scope** | b7 diagnostic + b9 production runtime evidence | b9 confirms current production list/detail transport can succeed for two distinct Plus/personal conversations. b10 recovery uses the same detail path but has no new runtime protocol evidence yet. Not Frozen. |
| Native conversation read path | **Stable for tested scope** | `ConversationRepository` + sidebar/detail/message UI; `DEV-native-read-path-0.1.0-b9` | **Code + CI + Artifact + real-device tested** for shell/list/two-detail/current visible branch on iPhone/iOS 17.0. Position 1: 1.53 MB / 337 mapping / 154 visible / 5.67 s; position 13: 7.50 MB / 2023 mapping / 843 visible / 20.74 s. PR #9 merged. Not Frozen. |
| Manual conversation recovery | **Candidate** | `ConversationRepository` + `ConversationDetailViewController`; `DEV-conversation-recovery-0.1.0-b10` | **Code written + CI passed + Artifact produced.** Adds explicit `同步最新消息`, authoritative clear-then-fetch `重载当前会话`, loaded-state overflow entries and recovery count/diff/state diagnostics. No retry/watchdog/timer/resend or second store. PR #10 open; real-device/manual acceptance pending. Not Frozen. |
| Streaming / send / attachments | Unknown / Unverified | Future development tasks | Not proven by b7-b10 read/recovery work. |

## Allowed statuses

Use concise statuses such as Active, Candidate, Accepted Candidate, Stable, Frozen, Experimental, Deprecated, or Unknown / Unverified.

## Frozen rule

Before changing a Frozen or Stable core module for an unrelated task, verify the task truly requires it and record the evidence. Stable does not mean Frozen.

## Current acceptance boundary

- `DEV-app-foundation-0.1.0-b1`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; foundation Stable, not Frozen.
- `DEV-auth-bootstrap-0.1.0-b6`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; auth/account context Stable for tested iPhone/iOS 17.0 scope.
- `DEV-protocol-read-0.1.0-b7`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; Plus/personal list + one-detail diagnostic protocol accepted.
- `DEV-native-read-path-0.1.0-b8`: **Code + CI + Artifact + real-device tested, partial/failing acceptance**; historical predecessor with one detail HTTP 500 before parse/render.
- `DEV-native-read-path-0.1.0-b9`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** for native shell/list/two-detail/current-branch message rendering; merged and Stable for tested scope.
- `DEV-conversation-recovery-0.1.0-b10`: **Code written + CI passed + Artifact produced** for manual latest-message sync/full current-conversation reload and recovery diagnostics; **Runtime/manual/real-device tested = pending**, so it is Candidate, not Stable.

Runtime compatibility below iOS 17.0, iPad, non-personal workspace behavior, send/streaming and attachments remain unverified.

## Auto-refresh rule

Update this matrix when modules are added, ownership changes, a module becomes stable/frozen, a frozen decision is reopened, or a new candidate supersedes an old baseline.
