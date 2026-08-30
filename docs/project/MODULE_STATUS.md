# Module Status

| Module | Status | Owner / baseline | Current evidence / boundary |
|---|---|---|---|
| Repository AI governance | Active | `main@1ac202c...` `AGENTS.md` + `docs/project/START_HERE.md` | Autonomous continuation, checkpoint, evidence ladder and conflict rules active; final target sync required before merge. |
| Native application shell | **Stable b38 baseline** | `AppDelegate.swift`, `RootViewController.swift` | Phase 9 diagnostics do not redefine ordinary native read/navigation ownership. Frozen No. |
| Build/runtime metadata | **b59 exact diagnostic identity; Runtime tested** | Xcode settings / built `Info.plist` | `0.1.0 (59)`, Candidate b59, exact source `138c09a5d111...`, Artifact `9730376958`; b39-b59 permanently reserved. |
| Diagnostics / logging | **b59 Runtime evidence active** | `DiagnosticsLogger` + `NativeWebSendEngineProbe` | b59 adds preamble counts only; current next evidence may add reasoning-active and privacy-safe tool-association counts, never raw IDs/bodies/auth/proof values. |
| IPA build / CI packaging | **Stable capability; b59 exact Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33305680998/99241706079`, PR `33305683021/99241711695`, Artifact `9730376958`, ZIP `sha256:4c13fc59...763ef`, IPA `5758cf40...49252`; Release / iOS14 / `[1,2]` / arm64. |
| Embedded Web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. |
| Protocol-read transport | Stable diagnostic scope | transient auth + probes | Completion-handler native read transport is not incremental response owner. |
| Official same-response resume | **Runtime Confirmed b45/b47** | official Web `/backend-api/f/conversation/resume` | HTTP200 SSE no-resend continuation; exact offset semantics still Unverified. |
| Native resume parity | **Rejected for tested duplicated path** | `NativeResumeParityProbeViewController` | b46/b47 Cookie+Bearer-only duplicate returned HTTP404 JSON; first/exclusive Native resume Unknown. |
| User-visible official-Web protected Send | **Security-permitted, daily full-Web product blocked** | TD-023/024/025/028 | b47 long-answer composer freeze blocks full conversation Web as production dependency. b48-b59 remain diagnostic exceptions only. |
| Native Web Send-engine diagnostic | **b59 Runtime text-completeness pass; presentation partial** | `NativeWebSendEngineProbeViewController` | Two service-marked thinking preambles were captured; reasoning/final complete. Remaining defects: reasoning segment breaks, explicit thinking-state UX, exact tool-detail semantics/pairing. |
| Native conversation read/recovery | **Stable merged baseline** | `ConversationRepository` | Sole native production conversation/list/read/recovery/future accepted response authority. b48-b59 do not mutate it. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Accepted b23 contracts retained. |
| Native message geometry / round navigation | **Stable merged b38** | presentation projection + message cell | Deterministic bounded geometry and accepted continuous quick-navigation retained. |
| Conversation message rich rendering | Planned | future `DEV-message-rendering` | General Markdown/code/table/link/citation rendering remains separate; response lifecycle/tool-card semantics stay in `DEV-send-stream`. |
| Streaming / Send | **Active diagnostic architecture experiment** | `DEV-send-stream`; PR #29 | b59 reasoning/preamble/final completeness passed. Official-like ordered response presentation and accepted production response ownership remain pending. |
| User-visible reasoning | **b59 Runtime complete for tested text; presentation refinement active** | `DEV-send-stream` | Exact `reasoning_ended` remains phase marker; two thinking preambles in one phase confirmed; `reasoning_status=is_reasoning` safely signals return-to-reasoning after tools. `assistant:thoughts` body remains prohibited. |
| Tool activity presentation | **b59 compact activity Runtime passed; detail semantics pending** | `DEV-send-stream` | 12 invocations produced 12 compact Native entries; 13 results prove adjacency pairing unsafe. Expandable request/result detail remains current Work but must wait for exact association/user-visible-field evidence. |
| Background completion | **Hard requirement; production owner pending** | `BACKGROUND_EXECUTION_PLAN.md` | b45/b49 positive short-background evidence only; 5/15-minute and termination gates remain. |
| Attachments | **High priority; Send-boundary dependent** | future `DEV-attachments` | iOS17 native photo+video path still needs evidenced handoff; no private WebKit/DOM file injection. |

## Current acceptance boundary

- Stable merged native baseline remains exact b38 for recorded scope.
- b42 protected-Send security boundary and b45 official resume evidence remain accepted.
- Full mobile-Web existing-conversation Send remains blocked as daily production dependency.
- b51 title continuation fix, b55/b56 reasoning-end marker, b57 phase split and b58 bounded tool activity remain accepted diagnostic evidence.
- **b59 Runtime passed the tested missing-preamble/text completeness correction:** two exact service-marked preambles (`2 / 13 chars`), Native reasoning `12 / 207`, final `18 / 357`, terminal true.
- **Remaining current Work:** preserve reasoning segment boundaries, expose protocol/lifecycle-backed `正在思考`, establish exact invocation→result/user-visible-detail semantics, then build the official-like ordered response timeline without exposing internal thoughts/raw connector payloads.
- TD-024/TD-025/TD-028 unchanged; b48-b59 remain isolated diagnostic exceptions.
- b39-b59 emitted identities are permanently reserved. Phase 9 Stable/Frozen: No.

## Auto-refresh rule

Update this matrix whenever ownership, Candidate identity, CI/Artifact evidence, accepted Runtime behavior or stability changes.
