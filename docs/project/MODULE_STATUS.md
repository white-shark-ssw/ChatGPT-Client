# Module Status

## DEV-send-stream b75 Runtime override — 2026-09-01

- Build/runtime metadata: exact b75 package verified; Runtime partial/rejected; b39-b75 reserved; Stable/Frozen Send No.
- Covered external continuation: b75 pre-accept validation works, but covered production page-owned matching `/resume` returned HTTP404 JSON in three observed active-response attempts. HTTP200 SSE adoption is therefore not a current production-proven path; Web Rule Lab re-probe is required before product changes.
- User-visible reasoning/tool/final: no external live rows were created in the supplied b75 run. Local b67 transport and b72 tested simultaneous A/B ownership remain accepted predecessors.
- Typography: b75 26/18.2/18.2 is visually rejected as too tight; next correction must increase visible vertical rhythm rather than merely assert those numeric values.
- Geometry: cooperative cache-miss path and resident reuse observed; worst-case Back responsiveness remains Runtime-unverified in this export.

| Module | Status | Owner / baseline | Current evidence / boundary |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/START_HERE.md` | Checkpoint/evidence/conflict rules active; final target sync required before merge. |
| Native application shell | **Stable b38 baseline; Phase 9 integrated validation surface** | `AppDelegate.swift`, `RootViewController.swift` | Native shell/read/navigation remains product UI. Current branch adds TD-029 covered-Send orchestration + validation-only trigger without changing b38 message geometry. Final Composer remains future `DEV-composer-parity`. |
| Build/runtime metadata | **b74 exact identity; Runtime pending** | Xcode settings / built `Info.plist` | `0.1.0 (74)`, exact source `50dd61b8...`, Artifact `9768668727`; b39-b74 reserved. |
| Diagnostics / logging | **Stable privacy contract** | `DiagnosticsLogger` | Prompt/answer/reasoning/tool bodies/raw IDs/auth/challenge values remain excluded. b66 Runtime evidence used only bounded lifecycle/count/state facts. |
| IPA build / CI packaging | **Stable capability; b74 Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33420408779/99581104920`, PR `33420412792/99581117817`, Artifact `9768668727`, ZIP `6ac4cc97...95cb3`, IPA `07c999fd...285da`; package independently verified as b74/source `50dd61b8b31c`/Release/iOS14/arm64. |
| Embedded Web login / persistent browser state | Stable authority | `AuthWebViewController.swift` + `WKWebsiteDataStore.default()` | Default persistent WebKit store remains sole persistent auth-secret authority. TD-029 covered executor and Web Rule Lab reuse it; no second store. |
| Authentication/account context | **Stable owner; b70 transient-403 behavior Runtime pending** | `AuthSessionStore.swift` | Sole native auth/account owner. Exact probe 403 preserves last verified identity while returning no fresh transport; 401 remains unavailable semantics. |
| Protocol-read transport | Stable read scope | transient auth + probes | Native read transport is not protected-Send executor and not incremental-response owner. |
| Official same-response resume | **Runtime Confirmed official-page continuation; b74 external adoption candidate** | official Web `/backend-api/f/conversation/resume` | b45/b47 proved no-resend continuation; 2026-09-01 Web Rule Lab additionally proves page-owned matching `{conversation_id, offset}` -> HTTP200 SSE on cross-device active-conversation entry. Native construction remains Unverified/rejected for current product path. |
| Native resume parity | **Rejected for tested duplicated path** | `NativeResumeParityProbeViewController` | b46/b47 Cookie+Bearer-only duplicate returned HTTP404 JSON; first/exclusive Native resume Unknown. |
| Covered official-Web protected Send executor | **b67 local Send Runtime accepted; b74 page-owned resume observation packaged** | `CoveredWebSendExecutor` + TD-029 + `WEB_SEND_ADAPTER.md` | b67 passed protected Send -> HTTP200 SSE -> terminal/reconcile. b74 retains that path and adds observation of only the official page's matching `/resume` SSE for external active-response adoption; Runtime pending. |
| Full official-Web conversation UI | **Rejected as daily-chat product dependency** | TD-025/TD-028 | b44 full-page hybrid UX rejected; b47 long-conversation Web composer failure retained. TD-029 does not restore full-Web rendering. |
| Web Rule Lab | **Implemented / Runtime page-load observed b66** | Settings + visible `WKWebView` using `.default()` store | b66 diagnostics recorded Lab open/page loaded. Explicit execute only; temporary script/result; copy/share; no persisted body/log body; not a production owner. |
| Native Web Send-engine diagnostic | **b65 focused Runtime passed** | `NativeWebSendEngineProbeViewController` | Verified composer/protected Send/reasoning/final/tool-detail probe baseline remains accepted; diagnostic only. |
| Native conversation read/recovery | **Stable merged baseline + b74 response/adoption candidate** | `ConversationRepository` | Sole production conversation/list/detail/recovery/response lifecycle authority. b74 external continuation creates one response generation in the existing Repository runtime; no second response store. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Accepted b23 contracts retained. |
| Native message geometry / round navigation | **Stable merged b38 semantics; b74 reuse optimization Runtime pending** | presentation projection + message cell | b38 deterministic bounded geometry/quick navigation remain authoritative. b74 caches only derived presentation geometry for unchanged resident identity to avoid repeated full rebuild; no message-body cache. |
| Conversation message rich rendering | Planned | future `DEV-message-rendering` | General Markdown/code/table/link/citation remains separate; response lifecycle/tool-card semantics stay `DEV-send-stream`. |
| Streaming / Send | **Active — b67 transport accepted; b72 A/B positive; b74 exact Runtime candidate** | `DEV-send-stream`; PR #29; TD-029 | b74 exact source/Push+PR CI/Artifact/package verified; external page-owned resume adoption + geometry reuse/tool spacing Runtime pending. |
| User-visible reasoning | **Production local stream passed b67; b74 external-adoption Runtime pending** | `ConversationRepository` + `DEV-send-stream` | Ordered reasoning/tool segments retained; external matching resume feeds the same Repository timeline; hidden thoughts prohibited. |
| Tool activity presentation | **b74 Code/CI/Artifact/package verified; Runtime pending** | `DEV-send-stream` | b73 semantic filtering retained; b74 increases main meaningful tool-row vertical rhythm only. Ordered tools-only/input-only sheet remains. |
| Expandable GitHub tool detail | **b65 Runtime mapping accepted; b70 production restoration Runtime pending** | `DEV-send-stream` | b70 restores nested input/output disclosures + decoded hierarchy only for the evidenced exact-parent GitHub shape; no cross-connector generalization. |
| Background completion | **Hard requirement; follows accepted production response owner** | `BACKGROUND_EXECUTION_PLAN.md` | b45 positive short-background evidence retained. b66 memory warning occurred after failure and protected resident was not evicted; full 5/15-minute/WebContent gates remain later. |
| Attachments | **High priority; Send-boundary dependent** | future `DEV-attachments` | iOS17 native photo+video handoff still needs evidence; no unsupported WebKit/DOM file injection. |

## Current acceptance boundary

- Stable merged native baseline remains b38.
- b67 production existing-conversation transport Runtime is accepted.
- Exact b72 Runtime positively supports the tested A-generating + B-send/generate simultaneous-generation path.
- Exact b73 Runtime is the evidence predecessor that exposed long resident geometry rebuild cost, insufficient tool rhythm and the external-active-response lifecycle gap.
- Exact b74 source `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`, Push/PR CI, canonical Artifact `9768668727`, ZIP `6ac4cc97...95cb3` and IPA `07c999fd...285da` are verified; package identity independently unpacked.
- b74 observes only the official page-owned matching `/backend-api/f/conversation/resume` SSE for external adoption; it does not construct resume/offset/polling and does not change `ConversationRepository` authority.
- b39-b74 are reserved. Phase 9 Stable/Frozen: No. Runtime remains pending.

## Auto-refresh rule

Update this matrix whenever ownership, Candidate identity, CI/Artifact evidence, Runtime behavior, Web-adapter rule or stability changes.