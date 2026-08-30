# Module Status

| Module | Status | Owner / baseline | Current evidence / boundary |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/START_HERE.md` | Checkpoint/evidence/conflict rules active; final target sync required before merge. |
| Native application shell | **Stable b38 baseline; Phase 9 integration pending** | `AppDelegate.swift`, `RootViewController.swift` | Native shell/read/navigation remains product UI; old full-page hybrid Send toolbar is transitional and must be replaced by TD-029 Native composer path. Frozen No. |
| Build/runtime metadata | **b65 exact identity; focused Runtime passed** | Xcode settings / built `Info.plist` | `0.1.0 (65)`, exact source `44138db766d0...`, Push Artifact `9736876465`; b39-b65 permanently reserved. Next identity not yet emitted. |
| Diagnostics / logging | **Stable privacy contract** | `DiagnosticsLogger` | Prompt/answer/reasoning/tool bodies/raw IDs/auth/challenge values remain excluded. Future Web Rule Lab must not persist script/result bodies. |
| IPA build / CI packaging | **Stable capability; b65 exact Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33328232044/99302071335`, PR `33328233842/99302076369`, Push Artifact `9736876465`, ZIP `d9a52ecb...ceb7a`, IPA `e6a01b2e...38d16`; Release / iOS14 / `[1,2]` / arm64. |
| Embedded Web login / persistent browser state | Stable authority | `AuthWebViewController.swift` + `WKWebsiteDataStore.default()` | Default persistent WebKit store remains sole persistent auth-secret authority. TD-029 reuses it for covered official-Web Send execution; no second store. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. |
| Protocol-read transport | Stable read scope | transient auth + probes | Completion-handler native read transport is not the protected-Send executor and not the incremental response owner. |
| Official same-response resume | **Runtime Confirmed b45/b47** | official Web `/backend-api/f/conversation/resume` | HTTP200 SSE no-resend continuation; exact Native first/exclusive parity remains Unverified. |
| Native resume parity | **Rejected for tested duplicated path** | `NativeResumeParityProbeViewController` | b46/b47 Cookie+Bearer-only duplicate returned HTTP404 JSON; first/exclusive Native resume Unknown. |
| Covered official-Web protected Send executor | **Production architecture authorized; implementation pending** | TD-029 + `WEB_SEND_ADAPTER.md` | b48-b65 prove verified-composer -> one real page-owned protected Send -> SSE on primary device. Covered Web is transport/challenge executor only; no conversation/response ownership. |
| Full official-Web conversation UI | **Rejected as daily-chat product dependency** | TD-025/TD-028 | b44 full-page Native->Web->Native UX rejected; b47 long-conversation mobile-Web composer failure retained. TD-029 does not restore full-Web rendering. |
| Web Rule Lab | **Planned in current Work / docs contract established** | Settings + visible `WKWebView` using `.default()` store | User-pasted temporary JS -> temporary result -> copy/share. No auto-run, no persisted scripts/results, no production state ownership. |
| Native Web Send-engine diagnostic | **b65 focused Runtime passed** | `NativeWebSendEngineProbeViewController` | Real protected Send/reasoning/final/tool lifecycle accepted for tested scope; remains evidence/probe UI, not production state owner. |
| Native conversation read/recovery | **Stable merged baseline / future response owner** | `ConversationRepository` | Sole native production conversation/list/detail/recovery authority and TD-029 future response owner. Production Send/response lifecycle not yet implemented. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Accepted b23 contracts retained. |
| Native message geometry / round navigation | **Stable merged b38** | presentation projection + message cell | Deterministic bounded geometry and accepted continuous quick-navigation retained; Phase 9 must integrate without replacing it. |
| Conversation message rich rendering | Planned | future `DEV-message-rendering` | General Markdown/code/table/link/citation rendering remains separate; response lifecycle/tool-card semantics stay in `DEV-send-stream`. |
| Streaming / Send | **Active production integration** | `DEV-send-stream`; PR #29; TD-029 | Transport/protocol evidence passed through b65. Current blocker is Repository-owned production integration, not Web protocol discovery. |
| User-visible reasoning | **Probe Runtime accepted; production owner integration pending** | `DEV-send-stream` | Exact thinking-preamble and `reasoning_ended` semantics accepted; `assistant:thoughts` prohibited. Must move into Repository-owned response state. |
| Tool activity presentation | **Probe Runtime accepted; production owner integration pending** | `DEV-send-stream` | Exact parent association only. Hidden/unmatched results never force-paired. |
| Expandable GitHub tool detail | **Focused b65 Runtime passed** | `DEV-send-stream` | Nested input/output disclosures + decoded hierarchy accepted for evidenced GitHub exact-parent shape; do not generalize connector families without evidence. |
| Background completion | **Hard requirement; follows Repository response owner** | `BACKGROUND_EXECUTION_PLAN.md` | b45 positive short-background evidence; 5/15-minute and WebContent termination gates remain later. |
| Attachments | **High priority; Send-boundary dependent** | future `DEV-attachments` | iOS17 native photo+video path still needs evidenced handoff; no unsupported WebKit/DOM file injection. |

## Current acceptance boundary

- Stable merged native baseline remains exact b38 for its recorded scope.
- Exact b65 focused Runtime passes the tested verified-composer protected-Send / reasoning-final / exact-parent tool lifecycle and structured GitHub detail presentation.
- **TD-029 now authorizes covered official-Web protected-Send execution for production**, superseding only the former visibility/hidden-executor prohibition in TD-024/025/028.
- Full official-Web conversation rendering remains rejected.
- `ConversationRepository` remains sole production response authority; production response lifecycle code is still pending.
- `WEB_SEND_ADAPTER.md` is the durable Web-rule maintenance source, including Web Rule Lab workflow.
- b39-b65 emitted identities are permanently reserved. Phase 9 Stable/Frozen: No.

## Auto-refresh rule

Update this matrix whenever ownership, Candidate identity, CI/Artifact evidence, accepted Runtime behavior, Web-adapter rule or stability changes.
