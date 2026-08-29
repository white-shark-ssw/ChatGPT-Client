# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | latest `main@1ac202c...` root `AGENTS.md` + `docs/project/START_HERE.md` | Current rules include autonomous continuation, rolling checkpoints, non-atomic batch recovery, same-session identity reuse and Full/Light Resume Guards. Feature branch still needs final rules synchronization before merge. |
| Native application shell | **Stable b38 baseline; b44 full-page trial rejected** | `AppDelegate.swift`, `RootViewController.swift`; Stable b38 behavior retained | Phase 9 diagnostics do not redefine ordinary native read/navigation ownership. Frozen No. |
| Build/runtime metadata | **b46 Runtime-tested diagnostic identity; b47 next** | Xcode settings / `Info.plist` | Exact legitimate b46: `0.1.0 (46)`, Candidate `DEV-send-stream-0.1.0-b46`, source `4ab9be3...`, Artifact `9715903443`. Any changed product code requires b47+. |
| Diagnostics / logging | **b46 Runtime-valid; b47 clarification authorized** | `DiagnosticsLogger` | Privacy-safe structural evidence only. b47 may add safe HTTP error structure + header-name comparison; never message/auth/challenge/header values. |
| IPA build / CI packaging | **Capability Stable; exact b46 CI/Artifact valid** | `scripts/build_ipa.sh`, workflow | b46 Push `33256273567` / Job `99110448112`, PR `33256275218` / Job `99110452786`, Artifact `9715903443`, IPA SHA `2c64a635...becec`. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| User-visible official-Web protected Send | **Legal Send feasibility accepted; full-page UX rejected** | TD-023/024/025 | Web may visibly perform protected Send. Hidden/shadow browser Send, DOM composer injection and synthetic hidden Send remain prohibited. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. b46 transient cookie+bearer re-verification succeeded during parity attempt. |
| Protocol-read diagnostic transport | Stable accepted diagnostic scope | `AuthTransientSession` + probes | Completion-handler transport buffers full response and is not an incremental stream owner. |
| Official same-response resume transport | **Runtime Confirmed on b45** | official Web `/backend-api/f/conversation/resume` evidence | `POST` body `{conversation_id, offset}`; successful response HTTP200 SSE; repeated no-resend recovery can reach `[DONE]`. Exact offset semantics still Unverified. |
| Native resume parity diagnostic | **b46 Runtime rejected for duplicated cookie+bearer-only attempt; b47 active clarification gate** | `NativeResumeParityProbeViewController` | Official offset 18 resume returned 200 SSE, then Native same-body cookie+bearer-only request returned 404 JSON; later official offset 54 resume again returned 200 SSE. Missing request-context vs second-consumer/cursor ownership remains unresolved. |
| Native conversation read/recovery | **Stable merged baseline** | `ConversationRepository` | Sole native conversation authority. Phase 9 diagnostics must not mutate it until Native continuation is accepted. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Existing cache contracts retained. |
| Native message presentation geometry | **Stable merged b38 performance baseline** | `ConversationMessagePresentationProjection` + `ConversationMessageCell` | Bounded chunks/deterministic geometry/manual layout retained. |
| Conversation metadata / Preferences / round navigation | Stable merged b38 | `AppPreferences` + detail presentation | Existing preference/round-navigation semantics retained. |
| Conversation message rich rendering | Planned | Future `DEV-message-rendering` | Current native body remains plain string. |
| Streaming / Send | **Active evidence gate — b47 diagnostic clarification next** | `DEV-send-stream`; PR #29 | Protected Send remains browser-owned. Official resume exists. Native duplicated parity failed 404; do not add browser header values or first-consumer takeover until b47 classifies rejection structure. |
| Background execution / completion | **Positive short-background signal; response-owner dependent** | `BACKGROUND_EXECUTION_PLAN.md` | b45 short background/lock survived/buffered; full 5/15-minute/process/network matrix still Unverified. If Native continuation succeeds later, background protects Native response lifecycle. |
| Attachments | **High priority; iOS17 Web chooser limitation evidenced** | Future `DEV-attachments` | Web `+` ~100–200ms accepted; Web Photos filtered video; iOS17 native photo+video path needs separate evidence. |

## Current acceptance boundary

- Stable merged native baseline remains exact b38 for its recorded scope.
- b42 remains accepted protected-Send security evidence; pure-native/transient-auth Send remains blocked.
- b43 visible-Web smoothness feasibility accepted; standalone Web-chat final form rejected.
- b44 mapping/eventual-read observations accepted; full-page hybrid UX rejected.
- b45 official no-resend `/backend-api/f/conversation/resume` is **Runtime Confirmed**.
- Exact b46 source `4ab9be3ef280...` / Artifact `9715903443`: Code/CI/Artifact/package identity passed; real-device Native cookie+bearer-only duplicated resume returned **HTTP404 JSON** while official Web resume remained healthy.
- b46 failure does not prove Native continuation impossible because request-context requirements and cursor/consumer ownership are still unresolved.
- b47 may only classify the rejection and compare header **names**, with one Native attempt and no copied browser header values.
- Fully hidden Web + Native DOM/button injection remains prohibited.
- b39-b46 identities are permanently reserved once emitted.
- Identity-invalid intermediate b46-transition Artifacts `9715858402`, `9715857814`, `9715907420`, `9715902353` remain permanently rejected.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.