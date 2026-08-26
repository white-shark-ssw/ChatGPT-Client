# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable for tested b9 scope / b12 candidate sequencing change** | `AppDelegate.swift`, `RootViewController.swift`; b9 baseline + b12 | b9 split shell is accepted. b12 changes only startup sequencing: default WebKit data-store warm-up completes before installing sidebar/detail controllers. Runtime effect is pending. Not Frozen. |
| Build/runtime metadata | Stable capability / **b12 candidate active** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | b12 package verifies `0.1.0 (12)`, candidate `DEV-conversation-recovery-0.1.0-b12`, source `4a7380b913ff`, minimum OS 14.0, arm64. Not Frozen. |
| Diagnostics / logging | Stable | `Diagnostics.swift` + auth/recovery event call sites | Existing structured/redacted diagnostics retained. b12 adds only safe WebKit warm-up counts/record count/duration; no Cookie values or auth secrets. Not Frozen. |
| IPA build / CI packaging | Stable capability; **b12 produced** | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml` | Run `32993589071` passed; artifact `9615588166`; IPA SHA-256 `2bd24e1dff89d2c04c82e838b44bf9e584d1587534ab6338b33b23bde0861aab`; PR head and tested merge share tree `81c801284b1e83f68043c30b9c75f47e76640128`. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible embedded login remains the explicit fallback only. b12 does not create hidden/shadow WebViews or auto-open the login UI. Not Frozen. |
| Authentication/account context | Stable baseline / **b12 recovery experiment** | `AuthSessionStore.swift`; b6/b7 + b9/b10 runtime evidence | Existing session/accounts parser and transient native session remain unchanged. b12 adds public-API default `WKWebsiteDataStore` warm-up before the first native list probe. Runtime effectiveness pending; no retry/watchdog or copied persistent secrets. Not Frozen. |
| Protocol-read diagnostic transport | **Stable for accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Code + CI + Artifact + real-device tested for accepted diagnostic scope. Diagnostic-only, not production owner. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable for tested scope** | b7 diagnostic + b9/b10/b11 production evidence | b9 confirms production list/detail transport; b10/b11 confirm manual sync/reload requests can succeed. b12 does not change detail/list endpoints or request semantics. Not Frozen. |
| Native conversation read path | **Stable for tested b9 scope** | `ConversationRepository` + sidebar/detail/message UI; b9 | Code + CI + Artifact + real-device accepted for shell/list/two-detail/current-branch message rendering. Not Frozen. |
| Manual conversation recovery | **Candidate — b12 Artifact ready** | `ConversationRepository` + `ConversationDetailViewController` + cold-start auth sequencing; b10 runtime + b11 rejected feedback + b12 | b10 core sync/full reload runtime accepted. b11 request path runtime worked but nav prompt feedback was not visible. b12 uses a centered progress/result toast with 2-second success display and adds cold-start background WebKit warm-up. b12 = Code + static review + CI + Artifact; Runtime pending. PR #10 open. Not Frozen. |
| Multi-conversation state ownership | Planned / Unverified | future `DEV-multi-conversation-state` | Latest project plan schedules this immediately after recovery and before round-count/send-stream. |
| Streaming / send / attachments | Unknown / Unverified | Future development tasks | Not proven by b7-b12 read/recovery work. |

## Allowed statuses

Use concise statuses such as Active, Candidate, Accepted Candidate, Stable, Frozen, Experimental, Deprecated, or Unknown / Unverified.

## Frozen rule

Before changing a Frozen or Stable core module for an unrelated task, verify the task truly requires it and record the evidence. Stable does not mean Frozen.

## Current acceptance boundary

- `DEV-app-foundation-0.1.0-b1`: Code + CI + Artifact + real-device; Stable foundation.
- `DEV-auth-bootstrap-0.1.0-b6`: Code + CI + Artifact + real-device; Stable auth/account-context baseline for tested iPhone/iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: Code + CI + Artifact + real-device; accepted diagnostic protocol scope.
- `DEV-native-read-path-0.1.0-b9`: Code + CI + Artifact + real-device; merged Stable native-read scope.
- `DEV-conversation-recovery-0.1.0-b10`: Code + CI + Artifact + real-device; accepted loaded-state sync/full-reload core behavior.
- `DEV-conversation-recovery-0.1.0-b11`: Code + static review + CI + Artifact + Runtime; sync request path worked, but required feedback presentation was rejected because the user saw no prompt.
- `DEV-conversation-recovery-0.1.0-b12`: **Code written + static/source review + CI passed + Artifact produced; Runtime/manual/real-device pending**. Active recovery candidate, not Stable.

Runtime compatibility below iOS 17.0, iPad, non-personal workspace behavior, cold-start b12 recovery, multi-conversation ownership, send/streaming and attachments remain unverified.

## Auto-refresh rule

Update this matrix when modules are added, ownership changes, a module becomes stable/frozen, a frozen decision is reopened, or a new candidate supersedes an old baseline.
