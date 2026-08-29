# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | latest `main@1ac202c...` root `AGENTS.md` + `docs/project/START_HERE.md` | Current rules include autonomous continuation, rolling checkpoints, non-atomic batch recovery, same-session identity reuse and Full/Light Resume Guards. Feature branch still needs final rules synchronization before merge. |
| Native application shell | **Stable b38 baseline; b44 full-page trial rejected** | `AppDelegate.swift`, `RootViewController.swift`; Stable b38 behavior retained | Phase 9 diagnostics do not redefine ordinary native read/navigation ownership. Frozen No. |
| Build/runtime metadata | **b51 exact diagnostic identity; Runtime pending** | Xcode settings / `Info.plist` | Exact b51: `0.1.0 (51)`, Candidate `DEV-send-stream-0.1.0-b51`, source `bd8f056...`, Artifact `9720327648`. b48-b51 are permanently reserved diagnostic identities. |
| Diagnostics / logging | **b50 Runtime-valid structural stream metrics; b51 adds title-generation continuation metric** | `DiagnosticsLogger` + `NativeWebSendEngineProbe` | b50 proves contextual compact `v:string` frames carry most Native assistant text on successful turns. Diagnostics remain structural/aggregate only and do not export prompt/answer/reasoning text. |
| IPA build / CI packaging | **Capability Stable; exact b51 CI/Artifact valid** | `scripts/build_ipa.sh`, workflow | b51 Push `33271794573` / Job `99151433241`, PR `33271796259` / Job `99151437702`, Artifact `9720327648`, IPA SHA `0aaa6317...45e51`. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| User-visible official-Web protected Send | **Security-permitted; full-conversation production use blocked by long-chat Web performance** | TD-023/024/025/028 | Full mobile-Web conversation remains unacceptable as a daily-chat surface after exact-device long-conversation composer failure. b48-b51 instead test a diagnostic Native surface over a Web Send engine; this does not change the durable production boundary. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. Phase 9 diagnostic Web uses the existing default persistent WebKit store. |
| Protocol-read diagnostic transport | Stable accepted diagnostic scope | `AuthTransientSession` + probes | Completion-handler transport buffers full response and is not an incremental stream owner. |
| Official same-response resume transport | **Runtime Confirmed on b45/b47** | official Web `/backend-api/f/conversation/resume` evidence | `POST` body `{conversation_id, offset}`; successful response HTTP200 SSE; repeated no-resend recovery can continue the same response. Exact offset semantics still Unverified. |
| Native resume parity diagnostic | **b46 + b47 duplicated parity Runtime rejected with HTTP404 JSON** | `NativeResumeParityProbeViewController` | Native first/exclusive resume and required browser context remain Unknown / Unverified. Resume work is not the active parser path in b48-b51. |
| Native Web Send-engine diagnostic | **b50 partial Runtime pass; b51 Runtime pending** | `NativeWebSendEngineProbeViewController` | b50: three sequential Native submissions all reached official protected Send and terminal; turns 2/3 were complete incremental Native replies while Web assistant DOM stayed small. New-chat first turn truncated. b51 preserves assistant-text continuation only across exact `title_generation` to test the evidenced first-turn difference. Diagnostic exception only; no production repository mutation. |
| Native conversation read/recovery | **Stable merged baseline** | `ConversationRepository` | Sole native production conversation authority. b48-b51 do not mutate it. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Existing cache contracts retained. |
| Native message presentation geometry | **Stable merged b38 performance baseline** | `ConversationMessagePresentationProjection` + `ConversationMessageCell` | Bounded chunks/deterministic geometry/manual layout retained; this native path is not implicated in the mobile-Web composer freeze. |
| Conversation metadata / Preferences / round navigation | Stable merged b38 | `AppPreferences` + detail presentation | Existing preference/round-navigation semantics retained. |
| Conversation message rich rendering | Planned | Future `DEV-message-rendering` | Current production native body remains plain string. |
| Streaming / Send | **Active diagnostic architecture experiment; human Runtime gate on b51** | `DEV-send-stream`; PR #29 | b50 materially confirms Native composer -> official Web protected Send -> intercepted SSE -> Native incremental output for established turns. b51 tests the remaining fresh-new-chat first-turn truncation. TD-024/TD-025 remain unchanged; PR remains evidence-only. |
| Background execution / completion | **Positive short-background signals; final owner dependent** | `BACKGROUND_EXECUTION_PLAN.md` | b45 original-Web stream survived/buffered short background/lock; b49 also showed a long diagnostic response reaching terminal across background intervals. Production background ownership remains unaccepted. |
| Attachments | **High priority; iOS17 Web chooser limitation evidenced** | Future `DEV-attachments` | Web `+` ~100–200ms accepted in b43, Web Photos filtered video; iOS17 native photo+video path still needs separate evidence. |

## Current acceptance boundary

- Stable merged native baseline remains exact b38 for its recorded scope.
- b42 remains accepted protected-Send security evidence; pure-native/transient-auth protected Send remains blocked.
- b45 official no-resend `/backend-api/f/conversation/resume` is Runtime Confirmed.
- b46/b47 Native duplicated Cookie+Bearer-only resume are Runtime rejected with HTTP404 JSON; first/exclusive Native resume remains Unknown.
- Exact-device full mobile-Web long-conversation composer usability failed before Send; root cause Unknown, product impact P0.
- b48 Runtime confirmed Native composer can drive official protected Send for two sequential turns, but its parser matched no compact text patches because it used wrong long-form field names.
- b49 Runtime confirmed real incremental Native delivery but captured only short explicit `o/p/v` fragments; complete-response interception rejected.
- b50 Runtime materially passed the diagnostic core on turns 2/3: contextual value-only continuations produced complete, visibly incremental Native replies while Web assistant text stayed small. Fresh new-chat turn 1 remained incomplete.
- b51 is exact Code/CI/Artifact/package verified and tests only whether evidenced new-chat `title_generation` should preserve the active assistant-text continuation context.
- TD-024/TD-025 hidden/shadow-Web production restriction is unchanged; b48-b51 remain isolated diagnostic exceptions requested by the user.
- b39-b51 emitted identities are permanently reserved. Identity-invalid b46-transition Artifacts `9715858402`, `9715857814`, `9715907420`, `9715902353` and stale-b42 Artifact `9710515489` remain permanently rejected.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.