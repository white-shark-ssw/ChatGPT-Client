# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap/routing/checkpoint rules remain authoritative. |
| Native application shell | **Stable baseline + b44 trial integration** | `AppDelegate.swift`, `RootViewController.swift`; Stable b38 behavior retained | b44 adds Root-owned native `发送消息…` toolbar entry and explicit Web-return reconciliation wiring. Exact-device regression pending. Frozen No. |
| Build/runtime metadata | **Stable b38 + active b44 Candidate** | Xcode settings / `Info.plist` | Current test Candidate `DEV-send-stream-0.1.0-b44`, `0.1.0 (44)`, exact source `f1503cf7121512a84e5c55a3642181c17324d791`; Runtime pending. |
| Diagnostics / logging | Stable baseline + safe hybrid fields | `DiagnosticsLogger` | Hybrid diagnostics use route class / targetMatch / timing only; no prompt/body/raw ID/auth/challenge values. |
| IPA build / CI packaging | **Capability Stable; b44 CI/Artifact valid** | `scripts/build_ipa.sh`, workflow | Push Run `33245105815`, Job `99081114295`, Artifact `9712583513`, ZIP `sha256:33ba4a99fe933241ce8023e811f15d55dfa0d95cac2693f039bb6138d813face`, IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| User-visible official-Web Send surface | **b43 feasibility Runtime largely accepted; b44 integrated Runtime pending** | `AuthWebViewController.hybridChat` + Root navigation | b43 smoothness/residency sequence had no material reported problem. b44 scopes visible Web to selected native conversation trial and removes ordinary standalone Settings entry. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner; unchanged. |
| Protocol-read diagnostic transport | Stable accepted diagnostic scope | `AuthTransientSession` + `ProtocolReadProbe.swift` | Diagnostic-only. |
| Native conversation read/recovery | **Stable merged baseline** | `ConversationRepository` | Sole native conversation authority. b44 only invokes the existing explicit Sync API after user taps `返回并同步`; no second store. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Existing cache contracts retained. |
| Native message presentation geometry | **Stable merged b38 performance baseline** | `ConversationMessagePresentationProjection` + `ConversationMessageCell` | b44 does not modify `ConversationFeature.swift`; bounded chunks/deterministic geometry/manual layout retained. |
| Conversation metadata / Preferences / round navigation | Stable merged b38 | `AppPreferences` + detail presentation | b44 removes standalone hybrid Settings UX only; existing preference semantics retained. |
| Conversation message rich rendering | Planned | Future `DEV-message-rendering` | Current native body remains plain string. |
| Streaming / send | **Integrated hybrid trial active — b44 Artifact ready / Runtime pending** | `DEV-send-stream`; PR #29 | Pure-native account-session Send remains blocked by b42 browser-challenge evidence. b44: native detail -> visible same-conversation Web trial -> explicit return/sync. Stable/Frozen No. |
| Attachments | **High priority; iOS17 Web chooser limitation evidenced** | Future `DEV-attachments`; `ATTACHMENT_TRANSFER_PLAN.md` | b43 Web `+` latency ~100–200ms accepted, but photo chooser filtered videos. Public WebKit upload-panel override is iOS18.4+, so b44 does not claim a video fix on iOS17. Native attachment protocol/handoff remains to be evidenced. |

## Current acceptance boundary

- Stable merged native baseline remains exact b38 for its recorded scope.
- b42 remains accepted security/transport-boundary evidence; legitimate Artifact `9709824510`.
- Accidental Artifact `9710515489` with stale b42 identity is permanently rejected.
- Exact b43 source `f602d68...` / Artifact `9711364573`: visible-Web feasibility and smoothness sequence **largely accepted on iPhone/iOS17**, with video-selection limitation retained.
- Exact b44 source `f1503cf...` / Artifact `9712583513`: Code/CI/Artifact/package identity valid; integrated same-conversation Runtime pending.
- b39-b44 identities are permanently reserved; corrected b44 product code requires b45+.
- Still Unverified where applicable: b44 `/c/<id>` same-conversation mapping, explicit return reconciliation on device, lower iOS/iPad, non-personal workspace/account switch, native iOS17 video attachment upload/handoff.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.
