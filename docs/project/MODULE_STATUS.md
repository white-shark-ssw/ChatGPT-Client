# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable for tested scope** | `AppDelegate.swift`, `RootViewController.swift`; `DEV-native-read-path-0.1.0-b9` | Split sidebar/detail shell and two selected conversation reads were real-device accepted on iPhone/iOS 17.0. PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`. Compact-width breadth beyond tested path remains Unverified. Not Frozen. |
| Build/runtime metadata | Stable capability / **b11 candidate identity active** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | Final b11 artifact verifies `0.1.0 (11)`, candidate `DEV-conversation-recovery-0.1.0-b11`, source `7fe8ca7693e9`, minimum OS 14.0, arm64. Not Frozen. |
| Diagnostics / logging | Stable | `Diagnostics.swift` | Structured OSLog + bounded JSONL + redacted export + clear control. b10 recovery count/diff/state spans were exercised on device without raw IDs/message bodies. b11 adds no diagnostics-owner change. Not Frozen. |
| IPA build / CI packaging | Stable capability; **b11 produced** | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml` | Final run `32988700796` passed; artifact `9613806931`; IPA SHA-256 `6c99a2b34ac5312b82930d1eeaeefb2a373e351325c92b7df7ad37a068316b33`; PR head and tested merge share exact tree `80cd8e60977bbcc8dc2dc83881a58afb29a51bde`. Intermediate run `32987959118` is rejected due inconsistent b10 build/b11 candidate identity. Not Frozen. |
| Embedded web login | Stable | `AuthWebViewController.swift`; b2+ | Embedded Google login remains accepted. b10 diagnostics give concrete cold-start 0/0 WebKit-cookie evidence and show real WKWebView navigation hydrates the default store. Background auth-resume is separate future work; b11 does not change auth. Not Frozen. |
| Authentication/account context | Stable | `AuthSessionStore.swift`; b6/b7 + b9/b10 production reuse evidence | Plus/personal account context verified after explicit web-session hydration. b11 reuses auth unchanged. Separate auth-resume experiment will require its own Work/branch/candidate after recovery. No automatic retry. Not Frozen. |
| Protocol-read diagnostic transport | **Stable for accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; `DEV-protocol-read-0.1.0-b7` | **Code + CI + Artifact + real-device tested.** Diagnostic-only; not production state owner. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable for tested scope** | b7 diagnostic + b9/b10 production runtime evidence | b9 confirms production list/detail transport for two conversations; b10 confirms the same detail path supports two manual latest-syncs and two full reloads. b11 changes only presentation feedback. Not Frozen. |
| Native conversation read path | **Stable for tested scope** | `ConversationRepository` + sidebar/detail/message UI; `DEV-native-read-path-0.1.0-b9` | **Code + CI + Artifact + real-device tested** for shell/list/two-detail/current visible branch on iPhone/iOS 17.0. PR #9 merged. Not Frozen. |
| Manual conversation recovery | **Candidate; b11 artifact ready** | `ConversationRepository` + `ConversationDetailViewController`; b10 runtime + `DEV-conversation-recovery-0.1.0-b11` | b10 = **Code + CI + Artifact + real-device tested** for loaded-state sync/full reload; no resend/duplicate observed. b11 = **Code + static review + CI + Artifact**, only adds non-blocking `正在同步最新消息…` → `已是最新` / `已同步最新消息` feedback; quick real-device feedback check pending. PR #10 open. Not Frozen. |
| Streaming / send / attachments | Unknown / Unverified | Future development tasks | Not proven by b7-b11 read/recovery work. |

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
- `DEV-conversation-recovery-0.1.0-b10`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** for loaded-state latest-sync/full reload core behavior. Runtime exposed only the lack of visible sync completion feedback.
- `DEV-conversation-recovery-0.1.0-b11`: **Code written + static/source diff reviewed + CI passed + Artifact produced; Runtime/manual/real-device feedback check pending**. Active final UX candidate, not Stable yet.

Runtime compatibility below iOS 17.0, iPad, non-personal workspace behavior, send/streaming and attachments remain unverified.

## Auto-refresh rule

Update this matrix when modules are added, ownership changes, a module becomes stable/frozen, a frozen decision is reopened, or a new candidate supersedes an old baseline.
