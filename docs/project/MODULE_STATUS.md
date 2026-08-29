# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap/routing/checkpoint rules remain authoritative. |
| Native application shell | **Stable multi-conversation read-state baseline** | `AppDelegate.swift`, `RootViewController.swift`; merged b21 | Compact startup/list-detail navigation and title lifecycle accepted for recorded scope. b43 does not modify Root. Frozen No. |
| Build/runtime metadata | **Stable b38 baseline + active b43 Candidate** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | Stable accepted product remains b38. Current test Candidate is `DEV-send-stream-0.1.0-b43`, `0.1.0 (43)`, exact source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`; Runtime pending. |
| Diagnostics / logging | Stable baseline + b43 safe hybrid events | `DiagnosticsLogger` + call sites | b43 adds privacy-safe `webSend` presentation/navigation timing/reuse fields only; no prompt/body/raw ID/auth/challenge values. Frozen No. |
| IPA build / CI packaging | **Capability Stable; b43 CI/Artifact valid** | `scripts/build_ipa.sh`, workflow | b43 push Run `33241032864`, Job `99070294478`, Artifact `9711364573`, ZIP `sha256:1a9516221ec5ece59741f9f2af2483815f09fa47f051ff6a97a67a12d40d4c23`, IPA SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`; Runtime pending. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift` | Visible Login remains a supported fallback. Default persistent WebKit store remains persistent auth-secret authority. Frozen No. |
| User-visible official-Web Send surface | **b43 Artifact produced / Runtime pending** | `AuthWebViewController.hybridChat` + Settings entry | Explicit Option-2 architecture. Shared resident visible `WKWebView`; no hidden challenge harvesting, DOM mirroring or token/proof capture. Functional/smoothness acceptance requires exact-device Runtime. |
| Authentication/account context | **Stable baseline** | `AuthSessionStore.swift`; b6 + merged consumers | Sole native auth/account owner; hybrid surface uses the same default persistent WebKit data store without adding another persistent credential owner. Frozen No. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only. Frozen No. |
| Native conversation read path | **Stable merged read/cache + Phase 8 baseline** | `ConversationRepository`; b21 + b23 + merged Phase 8 | Sole native conversation authority. b43 does not change it. Frozen No. |
| Manual conversation recovery | **Stable / merged baseline** | `ConversationRepository` + detail UI | Sync/Reload semantics unchanged; never resend/regenerate. Frozen No. |
| Multi-conversation state ownership | **Stable / merged for tested scope** | b21; PR #23 | Resident/coalescing/historical-scroll/title/replacement scope accepted. Conditional account/workspace/failure paths remain Unverified. Frozen No. |
| Conversation-list persistent cache | **Stable merged b23 + Phase 8 corrections** | `ConversationRepository` + `ConversationListCacheStore` | b23 cache core Stable; b26 `30 -> 29` bound; b29 right-top refresh fix. No second list/account owner. |
| Conversation entry / reading position | **Stable merged historical-anchor + first-entry-latest baseline** | `ConversationDetailViewController`; b18 + Phase 8 | A/B historical anchors remain independent; b43 hybrid surface does not replace this native read owner. Frozen No. |
| Conversation message presentation geometry | **Stable merged performance baseline** | `ConversationMessagePresentationProjection` + `ConversationMessageCell`; b37/b38 | Deterministic bounded chunks/manual layout remain the accepted no-stutter native read baseline. b43 does not touch these files. Frozen No. |
| Conversation metadata / Preferences / round navigation | **Stable / merged b38** | `AppPreferences` + `ConversationRoundProjection` + detail/message/sidebar presentation; PR #27 | Exact b38 Runtime accepted; b43 only adds a Settings entry and does not alter accepted round/navigation semantics. Frozen No. |
| Conversation message rich rendering | **Planned / not implemented** | Future `DEV-message-rendering` | Current native body remains plain string. |
| Streaming / send | **Hybrid path active; b43 Artifact produced, Runtime not yet accepted** | `DEV-send-stream`; b40-b42 protocol evidence + b43 visible-Web surface; PR #29 | Pure-native account-session Send remains blocked by browser anti-abuse challenge requirements. User explicitly selected visible official-Web Send; b43 is the first test Candidate. Stable/Frozen No. |
| Attachments | **Dependency narrowed: hybrid interaction Runtime pending** | Future `DEV-attachments`; `ATTACHMENT_TRANSFER_PLAN.md` | Architecture choice is made, but native-picker→official-Web handoff remains Unknown/Unverified. `+` responsiveness is a b43 UX gate; production attachment transfer remains future Work. |

## Current acceptance boundary

- b1/b6/b7/b9, b15, b21, b23 and exact b38 Phase 8 remain Stable/accepted merged baselines for their recorded scopes.
- Exact b24-b42 identities remain permanently reserved. Legitimate b42 Artifact is `9709824510`; accidental newer-code Artifact `9710515489` carrying b42 identity is permanently rejected and must never be used for Runtime.
- Exact valid b43 source is `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`; push/PR CI succeeded and Artifact `9711364573` was independently identity-verified as `0.1.0 (43)`, Candidate b43, source marker `f602d68ae95d`, iOS14 minimum, `[1,2]`, arm64.
- **b43 is not Runtime accepted yet.** The next gate is exact-device hybrid smoothness/Send/scroll/attachment-entry testing.
- Still Unverified as applicable: iPad, iOS below 17, non-personal workspace, supported real account switch, native-to-Web attachment handoff and other explicitly untested branches.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.
