# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | latest `main@1ac202c...` root `AGENTS.md` + `docs/project/START_HERE.md` | Autonomous continuation, rolling checkpoints, non-atomic batch recovery and Full/Light Resume Guards remain active. Feature branch still needs final rules synchronization before any merge. |
| Native application shell | **Stable b38 baseline; b44 full-page trial rejected** | `AppDelegate.swift`, `RootViewController.swift`; Stable b38 behavior retained | Phase 9 diagnostics do not redefine ordinary native read/navigation ownership. Frozen No. |
| Build/runtime metadata | **b57 exact diagnostic identity; Runtime pending** | Xcode settings / `Info.plist` | Exact b57: `0.1.0 (57)`, Candidate `DEV-send-stream-0.1.0-b57`, exact source `7074b1f85a0f...`, Artifact `9729360247`. b39-b57 emitted identities are permanently reserved. |
| Diagnostics / logging | **b56 Runtime corrected recap semantics; b57 adds phase-text shape evidence** | `DiagnosticsLogger` + `NativeWebSendEngineProbe` | b56 proved recap UI works but exact recap was only 7 chars/status while real visible reasoning stayed in ordinary text. b57 adds bounded ordinary `assistant:text` content-shape evidence and before/after-reasoning-end counts without persisting text. |
| IPA build / CI packaging | **Capability Stable; exact b57 CI/Artifact valid** | `scripts/build_ipa.sh`, workflow | b57 Push `33302357908` / Job `99232731468`, PR `33302359351` / Job `99232735067`, Artifact `9729360247`, ZIP `sha256:ae5a5532...d275`, IPA SHA `c8662a06...0a06`; package `0.1.0 (57)` / source `7074b1f85a0f` / Release / iOS14 / `[1,2]` / arm64. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| User-visible official-Web protected Send | **Security-permitted; full-conversation production use blocked by long-chat Web performance** | TD-023/024/025/028 | Full mobile-Web conversation remains unacceptable as a daily-chat surface after exact-device long-conversation composer failure. b48-b57 are diagnostic Native-over-Web-Send exceptions only; durable production boundary unchanged. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. Phase 9 diagnostic Web uses the existing default persistent WebKit store. |
| Protocol-read diagnostic transport | Stable accepted diagnostic scope | `AuthTransientSession` + probes | Completion-handler transport buffers full response and is not an incremental stream owner. |
| Official same-response resume transport | **Runtime Confirmed on b45/b47** | official Web `/backend-api/f/conversation/resume` evidence | `POST` body `{conversation_id, offset}`; successful response HTTP200 SSE; repeated no-resend recovery can continue the same response. Exact offset semantics still Unverified. |
| Native resume parity diagnostic | **b46 + b47 duplicated parity Runtime rejected with HTTP404 JSON** | `NativeResumeParityProbeViewController` | Native first/exclusive resume and required browser context remain Unknown / Unverified. Resume work is not the active parser path in b48-b57. |
| Native Web Send-engine diagnostic | **b56 Runtime partial pass; b57 Runtime pending** | `NativeWebSendEngineProbeViewController` | b56 confirmed exact recap detection/collapse UI but falsified recap text as the real reasoning body. b57 uses exact `reasoning_ended` only as a phase marker, separates already-accepted pre/post-marker text into Native reasoning/final regions, and adds text-free ordinary assistant-text shape diagnostics for the remaining leading truncation. Diagnostic exception only. |
| Native conversation read/recovery | **Stable merged baseline** | `ConversationRepository` | Sole native production conversation authority. b48-b57 do not mutate it. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Existing cache contracts retained. |
| Native message presentation geometry | **Stable merged b38 performance baseline** | `ConversationMessagePresentationProjection` + `ConversationMessageCell` | Bounded chunks/deterministic geometry/manual layout retained; this native path is not implicated in the mobile-Web composer freeze. |
| Conversation metadata / Preferences / round navigation | Stable merged b38 | `AppPreferences` + detail presentation | Existing preference/round-navigation semantics retained. |
| Conversation message rich rendering | Planned | Future `DEV-message-rendering` | Current production native body remains plain string. |
| Streaming / Send | **Active diagnostic architecture experiment; human Runtime gate on b57** | `DEV-send-stream`; PR #29 | b56 showed real visible reasoning and final answer were still mixed. b57 is the first narrow evidence-backed phase split based on exact service `reasoning_ended`, while the leading reasoning prefix remains diagnostic-gated. TD-024/TD-025 unchanged; PR remains evidence-only. |
| User-visible reasoning / tool presentation | **Reasoning-end phase marker evidence-backed; leading prefix and tool UI still gated** | `DEV-send-stream`; `SEND_STREAM_PREFLIGHT.md` | Exact b55/b56 authorize `reasoning_ended` as a phase marker, not recap text as the reasoning body. Raw `assistant:thoughts` remains prohibited. b54/b55 prove tool pairing structure but not exact user-visible tool-node boundaries, so no raw tool UI yet. |
| Background execution / completion | **Positive short-background signals; final owner dependent** | `BACKGROUND_EXECUTION_PLAN.md` | b45 original-Web stream survived/buffered short background/lock; b49 also showed a long diagnostic response reaching terminal across background intervals. Production background ownership remains unaccepted. |
| Attachments | **High priority; iOS17 Web chooser limitation evidenced** | Future `DEV-attachments` | Web `+` ~100–200ms accepted in b43, Web Photos filtered video; iOS17 native photo+video path still needs separate evidence. |

## Current acceptance boundary

- Stable merged native baseline remains exact b38 for its recorded scope.
- b42 remains accepted protected-Send security evidence; pure-native/transient-auth protected Send remains blocked.
- b45 official no-resend `/backend-api/f/conversation/resume` is Runtime Confirmed.
- b46/b47 Native duplicated Cookie+Bearer-only resume are Runtime rejected with HTTP404 JSON; first/exclusive Native resume remains Unknown.
- Full mobile-Web existing-conversation Send remains blocked as a daily production dependency by the exact-device long-conversation composer freeze.
- b48-b50 established Native composer→official protected Send and incremental compact response delivery; b51 fixed fresh-new-chat title-generation continuation.
- b52 kept final answer complete while visible reasoning beginning remained slightly truncated.
- b53 identified explicit reasoning/tool message classes; b54 identified tool pairing but hit generic observer saturation; b55 special observation passed and proved exact recap/end structure.
- **b56 Runtime partial pass:** exact recap detection and expand/collapse worked, but recap was only a 7-char status/description in the tested turn, real visible reasoning/final remained mixed, and visible reasoning beginning remained truncated.
- **b57 Code/CI/Artifact/package verified; Runtime pending.** It separates already-accepted visible text by the exact `reasoning_ended` marker and adds bounded ordinary assistant-text start-shape diagnostics; it does not guess the missing initial field.
- Raw `assistant:thoughts`, raw tool args/results/connector payloads and hidden/internal reasoning remain excluded.
- TD-024/TD-025 hidden/shadow-Web production restriction is unchanged; b48-b57 remain isolated diagnostic exceptions.
- b39-b57 emitted identities are permanently reserved. Identity-invalid b46-transition Artifacts `9715858402`, `9715857814`, `9715907420`, `9715902353` and stale-b42 Artifact `9710515489` remain permanently rejected.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.
