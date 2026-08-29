# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap/routing/checkpoint rules remain authoritative. |
| Native application shell | **Stable b38 baseline; b44 trial not accepted as final UX** | `AppDelegate.swift`, `RootViewController.swift`; Stable b38 behavior retained | b44 added Root-owned `发送消息…` + Web-return reconciliation trial. Runtime showed the full-page hybrid interaction is product-rejected; do not treat b44 Root trial as accepted Send UX. Frozen No. |
| Build/runtime metadata | **Stable b38 + reserved b44 trial** | Xcode settings / `Info.plist` | b44 `DEV-send-stream-0.1.0-b44`, `0.1.0 (44)`, source `f1503cf7121512a84e5c55a3642181c17324d791` is permanently reserved. No b45 allocated. |
| Diagnostics / logging | Stable baseline + safe hybrid fields | `DiagnosticsLogger` | Hybrid diagnostics use route class / targetMatch / timing only; no prompt/body/raw ID/auth/challenge values. |
| IPA build / CI packaging | **Capability Stable; b44 CI/Artifact valid** | `scripts/build_ipa.sh`, workflow | Push Run `33245105815`, Job `99081114295`, Artifact `9712583513`, ZIP `sha256:33ba4a99fe933241ce8023e811f15d55dfa0d95cac2693f039bb6138d813face`, IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`. Artifact validity does not imply product acceptance. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| User-visible official-Web Send surface | **Feasibility accepted; full-page integrated form rejected** | `AuthWebViewController.hybridChat`; TD-024 | b43 showed visible Web can be smooth/resident enough. b44 showed full-page Native->Web->Native flow duplicates conversation loading and cannot immediately reconcile assistant output through Native read. Architecture gate reopened. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner; unchanged. |
| Protocol-read diagnostic transport | Stable accepted diagnostic scope | `AuthTransientSession` + `ProtocolReadProbe.swift` | Diagnostic-only. |
| Native conversation read/recovery | **Stable merged baseline; eventual post-Web-Send visibility observed** | `ConversationRepository` | Sole native conversation authority. b44 Runtime showed immediate explicit Sync can surface user message while assistant output remains temporarily unreadable; later Sync can see it. Do not add polling/retry without a real readiness signal. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Existing cache contracts retained. |
| Native message presentation geometry | **Stable merged b38 performance baseline** | `ConversationMessagePresentationProjection` + `ConversationMessageCell` | b44 did not modify `ConversationFeature.swift`; bounded chunks/deterministic geometry/manual layout retained. |
| Conversation metadata / Preferences / round navigation | Stable merged b38 | `AppPreferences` + detail presentation | Existing preference/round-navigation semantics retained. |
| Conversation message rich rendering | Planned | Future `DEV-message-rendering` | Current native body remains plain string. |
| Streaming / send | **Blocked — architecture decision reopened after b44 Runtime rejection** | `DEV-send-stream`; PR #29 | Pure-native ChatGPT-account Send remains blocked by b42 browser-challenge evidence. b43 visible-Web feasibility is useful; b44 full-page integrated UX rejected. No b45 until explicit architecture choice. |
| Attachments | **High priority; iOS17 Web chooser limitation evidenced** | Future `DEV-attachments`; `ATTACHMENT_TRANSFER_PLAN.md` | b43 Web `+` latency ~100–200ms accepted, but photo chooser filtered videos. Public WebKit upload-panel override is iOS18.4+, so native iOS17 photo+video support requires an evidenced native attachment upload/handoff path. |

## Current acceptance boundary

- Stable merged native baseline remains exact b38 for its recorded scope.
- b42 remains accepted security/transport-boundary evidence; legitimate Artifact `9709824510`.
- Accidental Artifact `9710515489` with stale b42 identity is permanently rejected.
- Exact b43 source `f602d68...` / Artifact `9711364573`: visible-Web smoothness/residency feasibility largely accepted on iPhone/iOS17; standalone Web-chat product UX not accepted; video-selection limitation retained.
- Exact b44 source `f1503cf...` / Artifact `9712583513`: Code/CI/Artifact/package identity valid. Runtime accepted same-conversation route mapping and eventual native read visibility observations, but **rejected the integrated full-page hybrid product interaction**.
- b44 observed immediate `返回并同步`/Native Sync may miss assistant output already visible in Web; a later Sync can surface it. No fixed delay or readiness signal is established.
- The user's proposed fully covered Web + Native composer forwarding would require hidden/shadow Web automation under current evidence and is outside TD-023/TD-024.
- Current architecture gate: (A) visible embedded Web composer/live-response panel for existing ChatGPT-account continuity, (B) separate officially supported API product for truly Native Send/stream, or (C) defer account Send.
- b39-b44 identities are permanently reserved; no b45 allocated.
- Still Unverified where applicable: lower iOS/iPad, non-personal workspace/account switch, supported Native attachment upload/handoff, and any immediate Native response owner for ChatGPT-account Web Send.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.
