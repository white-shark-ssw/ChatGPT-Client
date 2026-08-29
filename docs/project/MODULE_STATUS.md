# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap/routing/checkpoint rules remain authoritative. |
| Native application shell | **Stable multi-conversation read-state baseline** | `AppDelegate.swift`, `RootViewController.swift`; merged b21 | Compact startup/list-detail navigation and title lifecycle accepted for recorded scope. Frozen No. |
| Build/runtime metadata | **Stable merged b38 baseline** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | Exact accepted package is `0.1.0 (38)`, Candidate `DEV-conversation-round-count-0.1.0-b38`, source `0d1801137e4e`, iOS14 minimum, arm64. b24-b38 identities remain reserved. |
| Diagnostics / logging | Stable baseline | `DiagnosticsLogger` + call sites | Privacy-safe round/list/auth/network diagnostics retained. b38 round diagnostics use presentation mode, row/role, offsets, travel distance, retargeting and landing error; no body/secret logging. Frozen No. |
| IPA build / CI packaging | **Stable capability + accepted b38 Runtime Artifact** | `scripts/build_ipa.sh`, workflow | Exact push Run `33230823568`, Job `99043233637`, Artifact `9708425762`, ZIP `sha256:50f77adb71bfce20a9fad4b63e4b879db04e23deb257c3810d157e6214730bf6`, IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift` | Visible Login remains fallback only. No hidden/shadow WebView. Frozen No. |
| Authentication/account context | **Stable baseline** | `AuthSessionStore.swift`; b6 + merged consumers | Sole auth/account owner; unchanged by Phase 8. Supported account-switch/non-personal workspace boundaries remain Unverified. Frozen No. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only. Frozen No. |
| Native conversation read path | **Stable merged read/cache + Phase 8 baseline** | `ConversationRepository`; b21 + b23 + merged Phase 8 | Sole authority. b26 authoritative-total cap and b29 right-top refresh correction are merged accepted behavior. Frozen No. |
| Manual conversation recovery | **Stable / merged baseline** | `ConversationRepository` + detail UI | Sync/Reload semantics unchanged; presentation projections/anchors re-derive after authoritative replacement. Frozen No. |
| Multi-conversation state ownership | **Stable / merged for tested scope** | b21; PR #23 | Resident/coalescing/historical-scroll/title/replacement scope accepted. Conditional account/workspace/failure paths remain Unverified. Frozen No. |
| Conversation-list persistent cache | **Stable merged b23 + Phase 8 reconcile/presentation corrections** | `ConversationRepository` + `ConversationListCacheStore` | b23 cache core Stable; b26 accepted `30 -> 29` bound; b29 accepted right-top refresh blank-region fix. No second list/account owner. |
| Conversation entry / reading position | **Stable merged historical-anchor + first-entry-latest baseline** | `ConversationDetailViewController`; b18 + Phase 8 | A/B historical anchors remain independent; first no-anchor entry shows latest/bottom; b38 retains accepted behavior. Frozen No. |
| Conversation message presentation geometry | **Stable merged performance baseline** | `ConversationMessagePresentationProjection` + `ConversationMessageCell`; b37/b38 | b36 proved giant deferred self-sizing geometry caused severe stutter. b37 bounded chunks + deterministic row metrics/prefix offsets + manual frame layout removed the reported long-conversation/scroll-indicator stutter. b38 preserves this architecture. Frozen No. |
| Conversation metadata / Preferences / round navigation | **Stable / merged b38** | `AppPreferences` + `ConversationRoundProjection` + detail/message/sidebar presentation; PR #27 | Exact b38 Runtime accepted. Continuous 0.35s ease-in-out navigation uses O(1) deterministic target offsets and preserves b37 no-stutter baseline. PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`. Frozen No. |
| Conversation message rich rendering | **Planned / not implemented** | Future `DEV-message-rendering` | Current body remains plain string. Markdown/code/table/link/citation rendering remains separate future Work. |
| Streaming / send | **Next planned phase, not Active** | Future `DEV-send-stream` | Must evidence current send/stream protocol and use per-conversation response ownership. No global stream owner. |
| Attachments | Planned after accepted Send/Stream | Future `DEV-attachments` | Follow `ATTACHMENT_TRANSFER_PLAN.md`; private transfer protocol must be evidenced. |

## Current acceptance boundary

- b1/b6/b7/b9, b15, b21, b23 and exact b38 Phase 8 are Stable/accepted merged baselines for their recorded scopes.
- Phase 8 exact tested product source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`, Runtime Artifact `9708425762`, PR #27 merge `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- b37/b38 establish the Stable long-conversation presentation baseline: deterministic derived geometry + bounded display chunks + continuous full-distance round animation.
- Exact b24-b38 identities remain permanently reserved; Frozen No.
- Still unverified as applicable: iPad, iOS below 17, non-personal workspace, supported real account switch, provisional-row Detail-block path, corrupt/schema rejection and other explicitly untested branches.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.
