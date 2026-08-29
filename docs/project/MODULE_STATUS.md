# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap/routing/checkpoint rules remain authoritative. |
| Native application shell | **Stable b38 baseline; b44 full-page trial rejected** | `AppDelegate.swift`, `RootViewController.swift`; Stable b38 behavior retained | b45 does not change the ordinary native conversation shell. Frozen No. |
| Build/runtime metadata | **Stable b38 + exact b45 diagnostic Candidate** | Xcode settings / `Info.plist` | b45 `DEV-send-stream-0.1.0-b45`, `0.1.0 (45)`, exact source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072` is permanently reserved. Any corrected product code requires b46+. |
| Diagnostics / logging | **b45 structural probe Runtime-valid for recorded capture** | `DiagnosticsLogger` | Export matched exact b45 and safely captured route/transport/status/header-name/query-name/structural identity evidence without prompt/answer/reasoning/raw IDs/auth/challenge values. |
| IPA build / CI packaging | **Capability Stable; b45 CI/Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33248952646` / Job `99091176390`, PR `33248954018` / Job `99091179731`, Artifact `9713774868`, ZIP digest `17843765...7626d`, IPA SHA `9fc53543...ec136`. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| User-visible official-Web Send surface | **Legal Send feasibility accepted; realtime ownership still targeted for Native** | TD-024/TD-025 + b45 evidence | b43 proved visible Web smooth enough for official Send; b44 full-page interaction rejected. Hidden/shadow Web Send remains prohibited. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner; unchanged. |
| Protocol-read diagnostic transport | Stable accepted diagnostic scope | `AuthTransientSession` + `ProtocolReadProbe.swift` | Diagnostic-only native reads. Existing completion-handler transport is not an incremental stream owner. |
| Realtime handoff protocol probe | **b45 first Runtime captured; reconnect mechanism still Unverified** | `ProtocolHandoffProbeViewController` | Uninterrupted official Web retained original `/f/conversation` fetch SSE to DONE. Early `resume_conversation_token` is real. `/conversation/{id}/stream_status` was JSON `{status:string}` only. No secondary continuation stream observed. Next evidence requires mid-stream interruption while reusing exact b45. |
| Native conversation read/recovery | **Stable merged baseline; eventual post-Web-Send visibility observed** | `ConversationRepository` | Sole native conversation authority. b44 immediate Sync may lag Web assistant output; no polling/retry without a readiness signal. A future accepted Native stream must extend this authority rather than form a second store. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Existing cache contracts retained. |
| Native message presentation geometry | **Stable merged b38 performance baseline** | `ConversationMessagePresentationProjection` + `ConversationMessageCell` | b45 does not modify `ConversationFeature.swift`; bounded chunks/deterministic geometry/manual layout retained. |
| Conversation metadata / Preferences / round navigation | Stable merged b38 | `AppPreferences` + detail presentation | Existing preference/round-navigation semantics retained. |
| Conversation message rich rendering | Planned | Future `DEV-message-rendering` | Current native body remains plain string. |
| Streaming / Send | **Active evidence gate — Native same-response continuation still not proven** | `DEV-send-stream`; PR #29 | b42 blocks pure-native protected Send. API product rejected. b45 normal uninterrupted traffic did not expose a second stream; that is insufficient to prove absence of reconnect. Exact b45 must next capture a real active-stream interruption before any b46 Native parity implementation. |
| Background execution / completion | **Hard requirement; implementation deferred behind handoff feasibility** | `BACKGROUND_EXECUTION_PLAN.md` + `HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md` | Next b45 Runtime intentionally uses short active-stream background/lock only to expose official reconnect behavior. It is not yet the full long-background acceptance matrix. |
| Attachments | **High priority; iOS17 Web chooser limitation evidenced** | Future `DEV-attachments`; `ATTACHMENT_TRANSFER_PLAN.md` | b43 Web `+` latency ~100–200ms accepted, but photo chooser filtered videos. Public WebKit upload-panel override is iOS18.4+, so iOS17 native photo+video support still needs an evidenced upload/handoff path. |

## Current acceptance boundary

- Stable merged native baseline remains exact b38 for its recorded scope.
- b42 remains accepted security/transport-boundary evidence; legitimate Artifact `9709824510`.
- Accidental Artifact `9710515489` with stale b42 identity is permanently rejected.
- b43 visible-Web smoothness feasibility accepted for recorded scope; standalone Web-chat form rejected.
- b44 route/mapping/eventual-read observations accepted; integrated full-page hybrid UX rejected.
- **b45 exact source `accd7bdf...` / Artifact `9713774868`: Code/CI/Artifact/package identity passed; first exact-device structural Runtime captured.**
- b45 first Runtime proves early `resume_conversation_token`, original-Send-SSE ownership through DONE, and status-only `stream_status` shape for the captured normal path. It does **not** prove Native continuation or absence of an interruption-only reconnect route.
- The second b45 Send carried `gizmo_id`; default-primary new-chat evidence remains incomplete for this capture.
- Fully hidden Web + Native DOM/button injection is not an accepted route.
- b39-b45 identities are permanently reserved.
- Still Unverified where applicable: active-response reconnect path, Native same-response continuation, native reasoning/follow-tail/background ownership, lower iOS/iPad, non-personal workspace/account switch and supported Native attachment upload/handoff.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.
