# Module Status

| Module | Status | Owner / baseline | Current evidence / boundary |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/START_HERE.md` | Checkpoint/evidence/conflict rules active; final target sync required before merge. |
| Native application shell | **Stable b38 baseline; Phase 9 integrated validation surface** | `AppDelegate.swift`, `RootViewController.swift` | Native shell/read/navigation remains product UI. Current branch adds TD-029 covered-Send orchestration + validation-only trigger without changing b38 message geometry. Final Composer remains future `DEV-composer-parity`. |
| Build/runtime metadata | **b67 exact identity; Runtime pending** | Xcode settings / built `Info.plist` | `0.1.0 (67)`, source `52ab38f16fe9...`, Push Artifact `9739891865`; b39-b67 permanently reserved. |
| Diagnostics / logging | **Stable privacy contract** | `DiagnosticsLogger` | Prompt/answer/reasoning/tool bodies/raw IDs/auth/challenge values remain excluded. b66 Runtime evidence used only bounded lifecycle/count/state facts. |
| IPA build / CI packaging | **Stable capability; b67 exact Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33338865423/99330666394`, PR `33338868896/99330678769`, Artifact `9739891865`, ZIP `7e41508c...d78c2`, IPA `3712dec9...95497`; Release / iOS14 / `[1,2]` / arm64. |
| Embedded Web login / persistent browser state | Stable authority | `AuthWebViewController.swift` + `WKWebsiteDataStore.default()` | Default persistent WebKit store remains sole persistent auth-secret authority. TD-029 covered executor and Web Rule Lab reuse it; no second store. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. |
| Protocol-read transport | Stable read scope | transient auth + probes | Native read transport is not protected-Send executor and not incremental-response owner. |
| Official same-response resume | **Runtime Confirmed b45/b47** | official Web `/backend-api/f/conversation/resume` | HTTP200 SSE no-resend continuation; Native first/exclusive parity remains Unverified. |
| Native resume parity | **Rejected for tested duplicated path** | `NativeResumeParityProbeViewController` | b46/b47 Cookie+Bearer-only duplicate returned HTTP404 JSON; first/exclusive Native resume Unknown. |
| Covered official-Web protected Send executor | **Production implementation present; b67 Runtime pending** | `CoveredWebSendExecutor` + TD-029 + `WEB_SEND_ADAPTER.md` | b65 probe transport passed. b66 first production bridge reached the service but duplicate Swift->JS submit orchestration caused `send_transport_error` before HTTP Response. b67 changes only operation gating to issue one JS submit. |
| Full official-Web conversation UI | **Rejected as daily-chat product dependency** | TD-025/TD-028 | b44 full-page hybrid UX rejected; b47 long-conversation Web composer failure retained. TD-029 does not restore full-Web rendering. |
| Web Rule Lab | **Implemented / Runtime page-load observed b66** | Settings + visible `WKWebView` using `.default()` store | b66 diagnostics recorded Lab open/page loaded. Explicit execute only; temporary script/result; copy/share; no persisted body/log body; not a production owner. |
| Native Web Send-engine diagnostic | **b65 focused Runtime passed** | `NativeWebSendEngineProbeViewController` | Verified composer/protected Send/reasoning/final/tool-detail probe baseline remains accepted; diagnostic only. |
| Native conversation read/recovery | **Stable merged baseline + production response owner implementation present** | `ConversationRepository` | Sole production conversation/list/detail/recovery/response lifecycle authority. b66/b67 add Repository-owned live response snapshot/generation; exact successful Runtime pending. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Accepted b23 contracts retained. |
| Native message geometry / round navigation | **Stable merged b38** | presentation projection + message cell | Deterministic bounded geometry and continuous quick-navigation unchanged by b66/b67. |
| Conversation message rich rendering | Planned | future `DEV-message-rendering` | General Markdown/code/table/link/citation remains separate; response lifecycle/tool-card semantics stay `DEV-send-stream`. |
| Streaming / Send | **Active production integration — b67 Runtime gate** | `DEV-send-stream`; PR #29; TD-029 | b66 proved protected Send can reach service from production bridge but exposed duplicate-submit race. b67 exact `+2/-1` Root correction is Code/CI/Artifact/package verified; Runtime pending. |
| User-visible reasoning | **Probe Runtime accepted; production Runtime pending** | `ConversationRepository` live response + `DEV-send-stream` | Exact thinking preamble and `reasoning_ended` rules unchanged; `assistant:thoughts` prohibited. b66 failed before response HTTP acceptance, so production reasoning stream is not yet Runtime accepted. |
| Tool activity presentation | **Probe Runtime accepted; production Runtime pending** | `DEV-send-stream` | Exact parent association only; b67 does not change parser/tool semantics. |
| Expandable GitHub tool detail | **Focused b65 Runtime passed** | `DEV-send-stream` | Nested input/output disclosures + decoded hierarchy accepted for evidenced GitHub exact-parent shape; no cross-connector generalization. |
| Background completion | **Hard requirement; follows accepted production response owner** | `BACKGROUND_EXECUTION_PLAN.md` | b45 positive short-background evidence retained. b66 memory warning occurred after failure and protected resident was not evicted; full 5/15-minute/WebContent gates remain later. |
| Attachments | **High priority; Send-boundary dependent** | future `DEV-attachments` | iOS17 native photo+video handoff still needs evidence; no unsupported WebKit/DOM file injection. |

## Current acceptance boundary

- Stable merged native baseline remains exact b38 for its recorded scope.
- Exact b65 focused Runtime is the accepted diagnostic protected-Send/reasoning/final/tool-detail predecessor.
- Exact b66 first production existing-conversation bridge is **Runtime failed**: service accepted/completed the Send, while Native saw duplicate ready/submitted callbacks and `send_transport_error` before `sendResponse`.
- Exact b67 is the current production correction Candidate: source `52ab38f16fe914ef8316bb1dc712b77c2c87a271`, Artifact `9739891865`, Runtime pending.
- TD-029 remains authorized; `ConversationRepository` remains sole production response authority; full Web rendering remains rejected.
- `WEB_SEND_ADAPTER.md` remains unchanged because b66 failure was local orchestration, not a Web-rule regression.
- b39-b67 emitted identities are permanently reserved. Phase 9 Stable/Frozen: No.

## Auto-refresh rule

Update this matrix whenever ownership, Candidate identity, CI/Artifact evidence, Runtime behavior, Web-adapter rule or stability changes.