# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | latest `main@1ac202c...` root `AGENTS.md` + `docs/project/START_HERE.md` | Autonomous continuation, rolling checkpoints, non-atomic batch recovery and Full/Light Resume Guards remain active. Feature branch still needs final rules synchronization before any merge. |
| Native application shell | **Stable b38 baseline; b44 full-page trial rejected** | `AppDelegate.swift`, `RootViewController.swift`; Stable b38 behavior retained | Phase 9 diagnostics do not redefine ordinary native read/navigation ownership. Frozen No. |
| Build/runtime metadata | **b55 exact diagnostic identity; Runtime pending** | Xcode settings / `Info.plist` | Exact b55: `0.1.0 (55)`, Candidate `DEV-send-stream-0.1.0-b55`, exact source `aae856069b46...`, Artifact `9728606514`. b39-b55 emitted identities are permanently reserved. |
| Diagnostics / logging | **b54 Runtime identified tool call/result shape; b55 fixes only diagnostic capacity** | `DiagnosticsLogger` + `NativeWebSendEngineProbe` | b54 captured assistant-code invocation recipients, tool result author/recipient/content containers, and `assistant:thoughts` summary-related structure. Generic structure set hit 32/overflow13 before deterministic recap coverage. b55 adds a separate bounded special-message dedupe channel; no response text/UI behavior changed. |
| IPA build / CI packaging | **Capability Stable; exact b55 CI/Artifact valid** | `scripts/build_ipa.sh`, workflow | b55 Push `33299965737` / Job `99226125826`, PR `33299967033` / Job `99226129092`, Artifact `9728606514`, ZIP `sha256:fda8dfb1...a7e3`, IPA SHA `f5106949...99ad1`; package `0.1.0 (55)` / source `aae856069b46` / Release / iOS14 / `[1,2]` / arm64. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| User-visible official-Web protected Send | **Security-permitted; full-conversation production use blocked by long-chat Web performance** | TD-023/024/025/028 | Full mobile-Web conversation remains unacceptable as a daily-chat surface after exact-device long-conversation composer failure. b48-b55 are diagnostic Native-over-Web-Send exceptions only; durable production boundary unchanged. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. Phase 9 diagnostic Web uses the existing default persistent WebKit store. |
| Protocol-read diagnostic transport | Stable accepted diagnostic scope | `AuthTransientSession` + probes | Completion-handler transport buffers full response and is not an incremental stream owner. |
| Official same-response resume transport | **Runtime Confirmed on b45/b47** | official Web `/backend-api/f/conversation/resume` evidence | `POST` body `{conversation_id, offset}`; successful response HTTP200 SSE; repeated no-resend recovery can continue the same response. Exact offset semantics still Unverified. |
| Native resume parity diagnostic | **b46 + b47 duplicated parity Runtime rejected with HTTP404 JSON** | `NativeResumeParityProbeViewController` | Native first/exclusive resume and required browser context remain Unknown / Unverified. Resume work is not the active parser path in b48-b55. |
| Native Web Send-engine diagnostic | **b54 Runtime partial pass; b55 Runtime pending** | `NativeWebSendEngineProbeViewController` | b53 final answer complete while visible reasoning beginning remained truncated and Native showed no tool UI. b54 proves real assistant-code→tool-result structure and captures `thoughts` summary/status metadata, but recap display-container evidence was blocked by observer saturation. b55 isolates special structure capacity only. Diagnostic exception. |
| Native conversation read/recovery | **Stable merged baseline** | `ConversationRepository` | Sole native production conversation authority. b48-b55 do not mutate it. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Existing cache contracts retained. |
| Native message presentation geometry | **Stable merged b38 performance baseline** | `ConversationMessagePresentationProjection` + `ConversationMessageCell` | Bounded chunks/deterministic geometry/manual layout retained; this native path is not implicated in the mobile-Web composer freeze. |
| Conversation metadata / Preferences / round navigation | Stable merged b38 | `AppPreferences` + detail presentation | Existing preference/round-navigation semantics retained. |
| Conversation message rich rendering | Planned | Future `DEV-message-rendering` | Current production native body remains plain string. |
| Streaming / Send | **Active diagnostic architecture experiment; human Runtime gate on b55** | `DEV-send-stream`; PR #29 | Final-answer capture passes prior exact reproductions. b55 must deterministically capture late reasoning/tool special structures after generic observer saturation. TD-024/TD-025 unchanged; PR remains evidence-only. |
| User-visible reasoning / tool presentation | **In-scope / evidence-gated** | `DEV-send-stream`; `SEND_STREAM_PREFLIGHT.md` | `reasoning_recap` is the direct service-side candidate for visible reasoning from b53. Raw `thoughts` remains prohibited. b54 materially identifies tool invocation/result pairing, but no raw tool payload/result exposure is authorized. Planned collapse/expand and tool detail UI wait for b55 display-boundary evidence. |
| Background execution / completion | **Positive short-background signals; final owner dependent** | `BACKGROUND_EXECUTION_PLAN.md` | b45 original-Web stream survived/buffered short background/lock; b49 also showed a long diagnostic response reaching terminal across background intervals. Production background ownership remains unaccepted. |
| Attachments | **High priority; iOS17 Web chooser limitation evidenced** | Future `DEV-attachments` | Web `+` ~100–200ms accepted in b43, Web Photos filtered video; iOS17 native photo+video path still needs separate evidence. |

## Current acceptance boundary

- Stable merged native baseline remains exact b38 for its recorded scope.
- b42 remains accepted protected-Send security evidence; pure-native/transient-auth protected Send remains blocked.
- b45 official no-resend `/backend-api/f/conversation/resume` is Runtime Confirmed.
- b46/b47 Native duplicated Cookie+Bearer-only resume are Runtime rejected with HTTP404 JSON; first/exclusive Native resume remains Unknown.
- Full mobile-Web existing-conversation Send remains blocked as a daily production dependency by the exact-device long-conversation composer freeze.
- b48-b50 established Native composer→official protected Send and incremental compact response delivery; b50 still failed fresh turn 1.
- **b51 Runtime confirms the narrow `title_generation` continuation-preserve correction fixes the fresh-new-chat missing-middle failure.**
- **b52 Runtime confirms final answer completeness on the tested tool-style turn while the visible reasoning beginning remains slightly truncated.**
- **b53 Runtime confirms service-side tool activity and directly identifies `assistant:reasoning_recap`, separate `assistant:thoughts`, `assistant:code`, and multiple `tool` content types.** Raw `thoughts` is non-presentational.
- **b54 Runtime is a partial pass:** HTTP200 SSE/terminal true; tool invocation/result grammar materially identified; `assistant:thoughts` structure includes `summary`/reasoning/tool-summary metadata; generic structure set saturated at 32 with overflow13, so missing `reasoning_recap` cannot be interpreted as protocol absence.
- **b55 Code/CI/Artifact/package is verified. Runtime pending.** It preserves b54 response behavior and only adds an independent 24-entry special-structure channel plus count/overflow metrics.
- Reasoning collapse/expand and tool-call presentation remain in current Work but are not implemented until explicit user-visible display boundaries are proven.
- TD-024/TD-025 hidden/shadow-Web production restriction is unchanged; b48-b55 remain isolated diagnostic exceptions.
- b39-b55 emitted identities are permanently reserved. Identity-invalid b46-transition Artifacts `9715858402`, `9715857814`, `9715907420`, `9715902353` and stale-b42 Artifact `9710515489` remain permanently rejected.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.
