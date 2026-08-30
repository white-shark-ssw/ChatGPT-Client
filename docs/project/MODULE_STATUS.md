# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | latest `main@1ac202c...` root `AGENTS.md` + `docs/project/START_HERE.md` | Autonomous continuation, rolling checkpoints, non-atomic batch recovery and Full/Light Resume Guards remain active. Feature branch still needs final rules synchronization before any merge. |
| Native application shell | **Stable b38 baseline; b44 full-page trial rejected** | `AppDelegate.swift`, `RootViewController.swift`; Stable b38 behavior retained | Phase 9 diagnostics do not redefine ordinary native read/navigation ownership. Frozen No. |
| Build/runtime metadata | **b56 exact diagnostic identity; Runtime pending** | Xcode settings / `Info.plist` | Exact b56: `0.1.0 (56)`, Candidate `DEV-send-stream-0.1.0-b56`, exact source `cec921030fd1...`, Artifact `9728937100`. b39-b56 emitted identities are permanently reserved. |
| Diagnostics / logging | **b55 special observer Runtime passed; b56 adds exact recap presentation counters only** | `DiagnosticsLogger` + `NativeWebSendEngineProbe` | b55 captured `assistant:reasoning_recap` after generic 32/overflow14 with special 7/overflow0 and proved `content.content`, `reasoning_ended`, `collapse`. b56 logs only recap character count and expand/collapse state; recap text itself is not persisted. |
| IPA build / CI packaging | **Capability Stable; exact b56 CI/Artifact valid** | `scripts/build_ipa.sh`, workflow | b56 Push `33301008807` / Job `99229039032`, PR `33301010617` / Job `99229043710`, Artifact `9728937100`, ZIP `sha256:2f4b5a21...d430`, IPA SHA `da627762...dbe6`; package `0.1.0 (56)` / source `cec921030fd1` / Release / iOS14 / `[1,2]` / arm64. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| User-visible official-Web protected Send | **Security-permitted; full-conversation production use blocked by long-chat Web performance** | TD-023/024/025/028 | Full mobile-Web conversation remains unacceptable as a daily-chat surface after exact-device long-conversation composer failure. b48-b56 are diagnostic Native-over-Web-Send exceptions only; durable production boundary unchanged. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. Phase 9 diagnostic Web uses the existing default persistent WebKit store. |
| Protocol-read diagnostic transport | Stable accepted diagnostic scope | `AuthTransientSession` + probes | Completion-handler transport buffers full response and is not an incremental stream owner. |
| Official same-response resume transport | **Runtime Confirmed on b45/b47** | official Web `/backend-api/f/conversation/resume` evidence | `POST` body `{conversation_id, offset}`; successful response HTTP200 SSE; repeated no-resend recovery can continue the same response. Exact offset semantics still Unverified. |
| Native resume parity diagnostic | **b46 + b47 duplicated parity Runtime rejected with HTTP404 JSON** | `NativeResumeParityProbeViewController` | Native first/exclusive resume and required browser context remain Unknown / Unverified. Resume work is not the active parser path in b48-b56. |
| Native Web Send-engine diagnostic | **b55 Runtime evidence gate passed; b56 Runtime pending** | `NativeWebSendEngineProbeViewController` | b55 proves the exact service recap container and collapsed/end semantics while keeping raw `thoughts` separate. b56 extracts only exact `assistant:reasoning_recap / finished_successfully / recipient=all / reasoning_ended / collapse` into a distinct default-collapsed Native region. Diagnostic exception only. |
| Native conversation read/recovery | **Stable merged baseline** | `ConversationRepository` | Sole native production conversation authority. b48-b56 do not mutate it. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Existing cache contracts retained. |
| Native message presentation geometry | **Stable merged b38 performance baseline** | `ConversationMessagePresentationProjection` + `ConversationMessageCell` | Bounded chunks/deterministic geometry/manual layout retained; this native path is not implicated in the mobile-Web composer freeze. |
| Conversation metadata / Preferences / round navigation | Stable merged b38 | `AppPreferences` + detail presentation | Existing preference/round-navigation semantics retained. |
| Conversation message rich rendering | Planned | Future `DEV-message-rendering` | Current production native body remains plain string. |
| Streaming / Send | **Active diagnostic architecture experiment; human Runtime gate on b56** | `DEV-send-stream`; PR #29 | b55 passes the recap display-boundary gate. b56 is the first narrow Native recap presentation Candidate; current b55 mixed/final text parser is intentionally unchanged. TD-024/TD-025 unchanged; PR remains evidence-only. |
| User-visible reasoning / tool presentation | **Recap presentation now evidence-backed; tool UI still gated** | `DEV-send-stream`; `SEND_STREAM_PREFLIGHT.md` | Exact b55 authorizes only `reasoning_recap` `content.content` with service `collapse`/`reasoning_ended` semantics. Raw `assistant:thoughts` remains prohibited. b54/b55 prove tool pairing structure but not exact user-visible tool-node boundaries, so no raw tool UI yet. |
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
- **b54 Runtime is a partial pass:** tool invocation/result grammar materially identified; generic structure set saturated at 32 with overflow13, so missing recap could not be interpreted as protocol absence.
- **b55 Runtime passes its intended evidence gate:** generic structures 32/overflow14 while special structures 7/overflow0; exact `assistant:reasoning_recap` exposed `content.content`, `reasoning_status=reasoning_ended`, `reasoning_recap_type=collapse`; raw `assistant:thoughts` remained separate and non-presentational.
- **b56 Code/CI/Artifact/package is verified; Runtime pending.** It only presents the exact evidence-backed recap in a default-collapsed Native region and keeps b55 response text interception unchanged.
- Tool-call presentation remains evidence-gated; raw tool args/results/connector payloads remain excluded.
- TD-024/TD-025 hidden/shadow-Web production restriction is unchanged; b48-b56 remain isolated diagnostic exceptions.
- b39-b56 emitted identities are permanently reserved. Identity-invalid b46-transition Artifacts `9715858402`, `9715857814`, `9715907420`, `9715902353` and stale-b42 Artifact `9710515489` remain permanently rejected.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.
