# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap/routing/checkpoint rules remain authoritative. |
| Native application shell | **Stable b38 baseline; b44 full-page trial rejected** | `AppDelegate.swift`, `RootViewController.swift`; Stable b38 behavior retained | b44 Root-owned `发送消息…` trial is not accepted final Send UX. b45 does not change the ordinary native conversation shell. Frozen No. |
| Build/runtime metadata | **Stable b38 + exact b45 diagnostic Candidate** | Xcode settings / `Info.plist` | b45 `DEV-send-stream-0.1.0-b45`, `0.1.0 (45)`, exact source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072` is permanently reserved. Any corrected product code requires b46+. |
| Diagnostics / logging | Stable baseline + b45 handoff structural diagnostics | `DiagnosticsLogger` | b45 records route/transport/status/header-name/query-name/structural identity-presence evidence only; no prompt/answer/reasoning/raw IDs/auth/challenge values. |
| IPA build / CI packaging | **Capability Stable; b45 CI/Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33248952646` / Job `99091176390`, PR `33248954018` / Job `99091179731`, Artifact `9713774868`, ZIP digest `17843765...7626d`, IPA SHA `9fc53543...ec136`. Artifact validity is not Runtime handoff proof. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| User-visible official-Web Send surface | **Legal Send feasibility accepted; realtime ownership targeted for Native** | TD-024/TD-025 + b45 handoff probe | b43 proved visible Web smooth enough to perform official Send; b44 full-page interaction rejected. Current target keeps Web responsibility to legal user-visible Send initiation only if Native can attach to the same response. Hidden/shadow Web Send remains prohibited. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner; unchanged. |
| Protocol-read diagnostic transport | Stable accepted diagnostic scope | `AuthTransientSession` + `ProtocolReadProbe.swift` | Diagnostic-only native reads. Existing completion-handler transport is not an incremental stream owner. |
| Realtime handoff protocol probe | **b45 Code/CI/Artifact passed; Runtime pending** | `ProtocolHandoffProbeViewController` | Observes original Send SSE plus post-Send fetch/XHR/EventSource/WebSocket continuation candidates. Observation-only: no token replay, guessed route, duplicate Send or answer scraping. |
| Native conversation read/recovery | **Stable merged baseline; eventual post-Web-Send visibility observed** | `ConversationRepository` | Sole native conversation authority. b44 immediate Sync may lag Web assistant output; no polling/retry without a readiness signal. A future accepted Native stream must extend this authority rather than form a second store. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Existing cache contracts retained. |
| Native message presentation geometry | **Stable merged b38 performance baseline** | `ConversationMessagePresentationProjection` + `ConversationMessageCell` | b45 does not modify `ConversationFeature.swift`; bounded chunks/deterministic geometry/manual layout retained. |
| Conversation metadata / Preferences / round navigation | Stable merged b38 | `AppPreferences` + detail presentation | Existing preference/round-navigation semantics retained. |
| Conversation message rich rendering | Planned | Future `DEV-message-rendering` | Current native body remains plain string. |
| Streaming / Send | **Active evidence gate — Native same-response continuation must be proven** | `DEV-send-stream`; PR #29 | b42 blocks pure-native protected Send. User rejects separate API product. Desired architecture is visible official Web legal Send -> Native no-resend attach/resume to same response. b45 probes whether that continuation path actually exists. |
| Background execution / completion | **Hard requirement; implementation deferred behind b45/b46 handoff feasibility** | `BACKGROUND_EXECUTION_PLAN.md` + `HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md` | If Native owns the response stream, background should protect Native lifecycle rather than WebKit. WebKit true-background remains fallback research only if handoff is disproven. |
| Attachments | **High priority; iOS17 Web chooser limitation evidenced** | Future `DEV-attachments`; `ATTACHMENT_TRANSFER_PLAN.md` | b43 Web `+` latency ~100–200ms accepted, but photo chooser filtered videos. Public WebKit upload-panel override is iOS18.4+, so iOS17 native photo+video support still needs an evidenced upload/handoff path. |

## Current acceptance boundary

- Stable merged native baseline remains exact b38 for its recorded scope.
- b42 remains accepted security/transport-boundary evidence; legitimate Artifact `9709824510`.
- Accidental Artifact `9710515489` with stale b42 identity is permanently rejected.
- b43 visible-Web smoothness feasibility accepted for recorded scope; standalone Web-chat form rejected.
- b44 route/mapping/eventual-read observations accepted; integrated full-page hybrid UX rejected.
- **b45 exact source `accd7bdf...` / Artifact `9713774868`: Code/CI/Artifact/package identity passed; Native realtime handoff Runtime remains Unknown/Unverified.**
- API product architecture is not an active option unless the user explicitly reverses that decision.
- Fully hidden Web + Native DOM/button injection is not an accepted route.
- Background/UI product work is downstream of the realtime-handoff evidence gate.
- b39-b45 identities are permanently reserved.
- Still Unverified where applicable: lower iOS/iPad, non-personal workspace/account switch, supported Native attachment upload/handoff, Native same-response continuation, and long-background response preservation.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.
