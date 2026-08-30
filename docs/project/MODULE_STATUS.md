# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | latest `main@1ac202c...` root `AGENTS.md` + `docs/project/START_HERE.md` | Current rules include autonomous continuation, rolling checkpoints, non-atomic batch recovery, same-session identity reuse and Full/Light Resume Guards. Feature branch still needs final rules synchronization before merge. |
| Native application shell | **Stable b38 baseline; b44 full-page trial rejected** | `AppDelegate.swift`, `RootViewController.swift`; Stable b38 behavior retained | Phase 9 diagnostics do not redefine ordinary native read/navigation ownership. Frozen No. |
| Build/runtime metadata | **b54 exact diagnostic identity; Runtime pending** | Xcode settings / `Info.plist` | Exact b54: `0.1.0 (54)`, Candidate `DEV-send-stream-0.1.0-b54`, product source `6a6903c7...`, Artifact `9727636043`. b39-b54 emitted identities are permanently reserved. |
| Diagnostics / logging | **b53 reasoning/tool grammar Runtime identified; b54 refines content/visibility shape** | `DiagnosticsLogger` + `NativeWebSendEngineProbe` | b53 directly evidenced `assistant:reasoning_recap`, separate `assistant:thoughts`, `assistant:code` and `tool:*`. b54 adds only text-free content-container/metadata shape for those classes; no prompt/answer/reasoning/tool-output values. |
| IPA build / CI packaging | **Capability Stable; exact b54 CI/Artifact valid** | `scripts/build_ipa.sh`, workflow | b54 Push `33296672444` / Job `99217423647`, PR `33296674388` / Job `99217428590`, Artifact `9727636043`, ZIP `sha256:28d07c99...7065c`, IPA SHA `d4b85cff...153b`. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| User-visible official-Web protected Send | **Security-permitted; full-conversation production use blocked by long-chat Web performance** | TD-023/024/025/028 | Full mobile-Web conversation remains unacceptable as a daily-chat surface after exact-device long-conversation composer failure. b48-b54 instead test a diagnostic Native surface over a Web Send engine; this does not change the durable production boundary. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. Phase 9 diagnostic Web uses the existing default persistent WebKit store. |
| Protocol-read diagnostic transport | Stable accepted diagnostic scope | `AuthTransientSession` + probes | Completion-handler transport buffers full response and is not an incremental stream owner. |
| Official same-response resume transport | **Runtime Confirmed on b45/b47** | official Web `/backend-api/f/conversation/resume` evidence | `POST` body `{conversation_id, offset}`; successful response HTTP200 SSE; repeated no-resend recovery can continue the same response. Exact offset semantics still Unverified. |
| Native resume parity diagnostic | **b46 + b47 duplicated parity Runtime rejected with HTTP404 JSON** | `NativeResumeParityProbeViewController` | Native first/exclusive resume and required browser context remain Unknown / Unverified. Resume work is not the active parser path in b48-b54. |
| Native Web Send-engine diagnostic | **b53 Runtime structurally advances reasoning/tool boundary; b54 Runtime pending** | `NativeWebSendEngineProbeViewController` | b53 final answer complete, visible reasoning beginning still truncated, no Native tool UI. Service stream nevertheless contained `reasoning_recap`, `thoughts`, code and tool messages. b54 preserves output behavior and refines only safe structure. Diagnostic exception only. |
| Native conversation read/recovery | **Stable merged baseline** | `ConversationRepository` | Sole native production conversation authority. b48-b54 do not mutate it. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Existing cache contracts retained. |
| Native message presentation geometry | **Stable merged b38 performance baseline** | `ConversationMessagePresentationProjection` + `ConversationMessageCell` | Bounded chunks/deterministic geometry/manual layout retained; this native path is not implicated in the mobile-Web composer freeze. |
| Conversation metadata / Preferences / round navigation | Stable merged b38 | `AppPreferences` + detail presentation | Existing preference/round-navigation semantics retained. |
| Conversation message rich rendering | Planned | Future `DEV-message-rendering` | Current production native body remains plain string. |
| Streaming / Send | **Active diagnostic architecture experiment; human Runtime gate on b54** | `DEV-send-stream`; PR #29 | Final-answer capture passes the exact b53 reproduction. b54 must identify the concrete `reasoning_recap` container and visibility/presentation markers before reasoning/tool presentation implementation. TD-024/TD-025 unchanged; PR evidence-only. |
| User-visible reasoning / tool presentation | **In-scope / evidence-gated** | `DEV-send-stream`; `SEND_STREAM_PREFLIGHT.md` | `reasoning_recap` is now a direct service-side candidate for explicit user-visible reasoning. `thoughts` remains prohibited from presentation. Tool execution is structurally real, but visibility boundary is not yet proven. Planned UX remains collapse/expand + tap-driven tool detail sheet after b54 evidence. |
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
- b50 Runtime materially passed the diagnostic core on established turns but fresh new-chat turn 1 remained incomplete.
- **b51 Runtime confirms the narrow `title_generation` continuation-preserve correction fixes the fresh-new-chat missing-middle failure.**
- **b52 Runtime confirms the final answer is complete on the tested GitHub/tool-style turn while the beginning of visible reasoning is still slightly truncated.** `rootNonExactTextPatchCount=0` and `inactiveValueStringCount=0`; the prior root-nonexact/inactive-value hypothesis is rejected for this reproduction.
- **b53 Runtime confirms service-side tool activity existed even though Native showed no tool UI, and directly identifies `assistant:reasoning_recap`, separate `assistant:thoughts`, `assistant:code`, and multiple `tool` content types.** `thoughts` remains non-presentational.
- b54 is Code/CI/Artifact/package verified and behavior-neutral; it adds bounded text-free content/metadata structure only for reasoning/code/tool message classes. Runtime pending.
- Reasoning collapse/expand and tool-call detail sheet remain in current Work, but implementation waits for b54 visibility/content-shape evidence.
- TD-024/TD-025 hidden/shadow-Web production restriction is unchanged; b48-b54 remain isolated diagnostic exceptions requested by the user.
- b39-b54 emitted identities are permanently reserved. Identity-invalid b46-transition Artifacts `9715858402`, `9715857814`, `9715907420`, `9715902353` and stale-b42 Artifact `9710515489` remain permanently rejected.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.