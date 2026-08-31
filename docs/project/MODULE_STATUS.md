# Module Status

| Module | Status | Owner / baseline | Current evidence / boundary |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/START_HERE.md` | Checkpoint/evidence/conflict rules active; final target sync required before merge. |
| Native application shell | **Stable b38 baseline; Phase 9 integrated validation surface** | `AppDelegate.swift`, `RootViewController.swift` | Native shell/read/navigation remains product UI. Current branch adds TD-029 covered-Send orchestration + validation-only trigger without changing b38 message geometry. Final Composer remains future `DEV-composer-parity`. |
| Build/runtime metadata | **b73 exact identity; Runtime pending** | Xcode settings / built `Info.plist` | `0.1.0 (73)`, source `4edda892a04a...`, Artifact `9764247402`; b39-b73 reserved. |
| Diagnostics / logging | **Stable privacy contract** | `DiagnosticsLogger` | Prompt/answer/reasoning/tool bodies/raw IDs/auth/challenge values remain excluded. b66 Runtime evidence used only bounded lifecycle/count/state facts. |
| IPA build / CI packaging | **Stable capability; b73 Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33408695143/99542593642`, PR `33408698697/99542605699`, Artifact `9764247402`, IPA `8285ba9d...84113`; package b73/source `4edda892a04a`/Release/iOS14/arm64. |
| Embedded Web login / persistent browser state | Stable authority | `AuthWebViewController.swift` + `WKWebsiteDataStore.default()` | Default persistent WebKit store remains sole persistent auth-secret authority. TD-029 covered executor and Web Rule Lab reuse it; no second store. |
| Authentication/account context | **Stable owner; b70 transient-403 behavior Runtime pending** | `AuthSessionStore.swift` | Sole native auth/account owner. Exact probe 403 preserves last verified identity while returning no fresh transport; 401 remains unavailable semantics. |
| Protocol-read transport | Stable read scope | transient auth + probes | Native read transport is not protected-Send executor and not incremental-response owner. |
| Official same-response resume | **Runtime Confirmed b45/b47** | official Web `/backend-api/f/conversation/resume` | HTTP200 SSE no-resend continuation; Native first/exclusive parity remains Unverified. |
| Native resume parity | **Rejected for tested duplicated path** | `NativeResumeParityProbeViewController` | b46/b47 Cookie+Bearer-only duplicate returned HTTP404 JSON; first/exclusive Native resume Unknown. |
| Covered official-Web protected Send executor | **Production transport Runtime accepted b67; b70 keyboard-only correction Runtime pending** | `CoveredWebSendExecutor` + TD-029 + `WEB_SEND_ADAPTER.md` | b67 passed one protected Send -> HTTP200 SSE -> terminal/reconcile. b70 retains route/selectors/SSE grammar and only suppresses covered programmatic keyboard focus. |
| Full official-Web conversation UI | **Rejected as daily-chat product dependency** | TD-025/TD-028 | b44 full-page hybrid UX rejected; b47 long-conversation Web composer failure retained. TD-029 does not restore full-Web rendering. |
| Web Rule Lab | **Implemented / Runtime page-load observed b66** | Settings + visible `WKWebView` using `.default()` store | b66 diagnostics recorded Lab open/page loaded. Explicit execute only; temporary script/result; copy/share; no persisted body/log body; not a production owner. |
| Native Web Send-engine diagnostic | **b65 focused Runtime passed** | `NativeWebSendEngineProbeViewController` | Verified composer/protected Send/reasoning/final/tool-detail probe baseline remains accepted; diagnostic only. |
| Native conversation read/recovery | **Stable merged baseline + b70 response/read lifecycle candidate** | `ConversationRepository` | Sole production conversation/list/detail/recovery/response lifecycle authority. b70 invalidates stale copied transient transport on list/detail 401/403 without automatic replay; Runtime pending. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Accepted b23 contracts retained. |
| Native message geometry / round navigation | **Stable merged b38** | presentation projection + message cell | Deterministic bounded geometry and continuous quick-navigation unchanged by b66/b67. |
| Conversation message rich rendering | Planned | future `DEV-message-rendering` | General Markdown/code/table/link/citation remains separate; response lifecycle/tool-card semantics stay `DEV-send-stream`. |
| Streaming / Send | **Active — b67 transport accepted; b72 tested A/B simultaneous generation positive; b73 presentation Runtime gate** | `DEV-send-stream`; PR #29; TD-029 | b73 exact source/Push+PR CI/Artifact/package verified; transport/concurrency code unchanged from b72/b67; presentation Runtime pending. |
| User-visible reasoning | **Production stream passed b67; b73 official-like presentation Runtime pending** | `ConversationRepository` + `DEV-send-stream` | Ordered segments retained; b73 uses body-scale primary reasoning prose, live auto-open once and exact `reasoning_ended` auto-collapse once; later manual disclosure stays user-owned; hidden thoughts prohibited. |
| Tool activity presentation | **b73 Code/CI/Artifact/package verified; Runtime pending** | `DEV-send-stream` | Main timeline keeps meaningful service-authored tool actions with looser rhythm and omits generic fallback rows; ordered tools-only/input-only sheet retains actual eligible calls. No guessed title synthesis. |
| Expandable GitHub tool detail | **b65 Runtime mapping accepted; b70 production restoration Runtime pending** | `DEV-send-stream` | b70 restores nested input/output disclosures + decoded hierarchy only for the evidenced exact-parent GitHub shape; no cross-connector generalization. |
| Background completion | **Hard requirement; follows accepted production response owner** | `BACKGROUND_EXECUTION_PLAN.md` | b45 positive short-background evidence retained. b66 memory warning occurred after failure and protected resident was not evicted; full 5/15-minute/WebContent gates remain later. |
| Attachments | **High priority; Send-boundary dependent** | future `DEV-attachments` | iOS17 native photo+video handoff still needs evidence; no unsupported WebKit/DOM file injection. |

## Current acceptance boundary

- Stable merged native baseline remains b38.
- b67 production existing-conversation transport Runtime is accepted.
- Exact b72 Runtime positively supports the tested A-generating + B-send/generate simultaneous-generation path and the incremental disclosure-performance correction; b72 presentation density/default-live-disclosure behavior is rejected.
- b73 exact source `4edda892a04a1a07f4a07e74b135b969ea82193e`, Artifact `9764247402`, IPA `8285ba9d...84113` is the current presentation Runtime candidate; package identity independently verified.
- `ConversationRepository` remains sole response authority; `AuthSessionStore` remains sole account authority; `WEB_SEND_ADAPTER.md` route/SSE contract is unchanged by b73.
- b39-b73 are reserved. Phase 9 Stable/Frozen: No.

## Auto-refresh rule

Update this matrix whenever ownership, Candidate identity, CI/Artifact evidence, Runtime behavior, Web-adapter rule or stability changes.