# Module Status

| Module | Status | Owner / baseline | Current evidence / boundary |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/START_HERE.md` | Checkpoint/evidence/conflict rules active; final target sync required before merge. |
| Native application shell | **Stable b38 baseline; Phase 9 integrated validation surface** | `AppDelegate.swift`, `RootViewController.swift` | Native shell/read/navigation remains product UI. Current branch adds TD-029 covered-Send orchestration + validation-only trigger without changing b38 message geometry. Final Composer remains future `DEV-composer-parity`. |
| Build/runtime metadata | **b69 exact identity; Runtime pending** | Xcode settings / built `Info.plist` | `0.1.0 (69)`, source `5e9c21834830...`, Artifact `9748400171`; b39-b69 reserved. |
| Diagnostics / logging | **Stable privacy contract** | `DiagnosticsLogger` | Prompt/answer/reasoning/tool bodies/raw IDs/auth/challenge values remain excluded. b66 Runtime evidence used only bounded lifecycle/count/state facts. |
| IPA build / CI packaging | **Stable capability; b69 Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33366226539/99407331552`, PR `33366229125/99407340011`, Artifact `9748400171`, IPA `0c06256d...3b0aa`; package b69/source `5e9c21834830`/iOS14/arm64. |
| Embedded Web login / persistent browser state | Stable authority | `AuthWebViewController.swift` + `WKWebsiteDataStore.default()` | Default persistent WebKit store remains sole persistent auth-secret authority. TD-029 covered executor and Web Rule Lab reuse it; no second store. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. |
| Protocol-read transport | Stable read scope | transient auth + probes | Native read transport is not protected-Send executor and not incremental-response owner. |
| Official same-response resume | **Runtime Confirmed b45/b47** | official Web `/backend-api/f/conversation/resume` | HTTP200 SSE no-resend continuation; Native first/exclusive parity remains Unverified. |
| Native resume parity | **Rejected for tested duplicated path** | `NativeResumeParityProbeViewController` | b46/b47 Cookie+Bearer-only duplicate returned HTTP404 JSON; first/exclusive Native resume Unknown. |
| Covered official-Web protected Send executor | **Production transport Runtime accepted b67; unchanged by b69** | `CoveredWebSendExecutor` + TD-029 + `WEB_SEND_ADAPTER.md` | b67 passed one protected Send -> HTTP200 SSE -> terminal/reconcile. b69 changes ordered Repository presentation only. |
| Full official-Web conversation UI | **Rejected as daily-chat product dependency** | TD-025/TD-028 | b44 full-page hybrid UX rejected; b47 long-conversation Web composer failure retained. TD-029 does not restore full-Web rendering. |
| Web Rule Lab | **Implemented / Runtime page-load observed b66** | Settings + visible `WKWebView` using `.default()` store | b66 diagnostics recorded Lab open/page loaded. Explicit execute only; temporary script/result; copy/share; no persisted body/log body; not a production owner. |
| Native Web Send-engine diagnostic | **b65 focused Runtime passed** | `NativeWebSendEngineProbeViewController` | Verified composer/protected Send/reasoning/final/tool-detail probe baseline remains accepted; diagnostic only. |
| Native conversation read/recovery | **Stable merged baseline + production response owner implementation present** | `ConversationRepository` | Sole production conversation/list/detail/recovery/response lifecycle authority. b66/b67 add Repository-owned live response snapshot/generation; exact successful Runtime pending. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Accepted b23 contracts retained. |
| Native message geometry / round navigation | **Stable merged b38** | presentation projection + message cell | Deterministic bounded geometry and continuous quick-navigation unchanged by b66/b67. |
| Conversation message rich rendering | Planned | future `DEV-message-rendering` | General Markdown/code/table/link/citation remains separate; response lifecycle/tool-card semantics stay `DEV-send-stream`. |
| Streaming / Send | **Active — b67 transport accepted; b69 ordered presentation Runtime gate** | `DEV-send-stream`; PR #29; TD-029 | b69 is Code/CI/Artifact/package verified for chronological reasoning/tool interleaving; Runtime pending. |
| User-visible reasoning | **Production stream passed b67; ordered b69 presentation Runtime pending** | `ConversationRepository` + `DEV-send-stream` | Ordered reasoning segments interleave with tools; exact `reasoning_ended` remains final authority; hidden thoughts prohibited. |
| Tool activity presentation | **b69 Code/CI/Artifact verified; Runtime pending** | `DEV-send-stream` | Tool appends at event position, completion updates in place by slot, later reasoning forms a segment below it. |
| Expandable GitHub tool detail | **Focused b65 Runtime passed** | `DEV-send-stream` | Nested input/output disclosures + decoded hierarchy accepted for evidenced GitHub exact-parent shape; no cross-connector generalization. |
| Background completion | **Hard requirement; follows accepted production response owner** | `BACKGROUND_EXECUTION_PLAN.md` | b45 positive short-background evidence retained. b66 memory warning occurred after failure and protected resident was not evicted; full 5/15-minute/WebContent gates remain later. |
| Attachments | **High priority; Send-boundary dependent** | future `DEV-attachments` | iOS17 native photo+video handoff still needs evidence; no unsupported WebKit/DOM file injection. |

## Current acceptance boundary

- Stable merged native baseline remains b38.
- b67 production existing-conversation transport Runtime is accepted.
- b68 is a valid reserved Artifact but its flattened reasoning/tool presentation was superseded before Runtime.
- b69 source `5e9c2183483094304f7eaeecf4ffc7ad8e65b902`, Artifact `9748400171`, IPA `0c06256d...3b0aa` is the current ordered-timeline Runtime candidate.
- `ConversationRepository` remains sole response authority; `WEB_SEND_ADAPTER.md` is unchanged because b69 consumes already-emitted event order.
- b39-b69 are reserved. Phase 9 Stable/Frozen: No.

## Auto-refresh rule

Update this matrix whenever ownership, Candidate identity, CI/Artifact evidence, Runtime behavior, Web-adapter rule or stability changes.