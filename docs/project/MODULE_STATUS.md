# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | latest `main@1ac202c...` root `AGENTS.md` + `docs/project/START_HERE.md` | Current rules include autonomous continuation, rolling checkpoints, non-atomic batch recovery, same-session identity reuse and Full/Light Resume Guards. Feature branch still needs final rules synchronization before merge. |
| Native application shell | **Stable b38 baseline; b44 full-page trial rejected** | `AppDelegate.swift`, `RootViewController.swift`; Stable b38 behavior retained | Phase 9 diagnostics do not redefine ordinary native read/navigation ownership. Frozen No. |
| Build/runtime metadata | **b53 exact diagnostic identity; Runtime pending** | Xcode settings / `Info.plist` | Exact b53: `0.1.0 (53)`, Candidate `DEV-send-stream-0.1.0-b53`, product source `3204b183...`, Artifact `9726996570`. b39-b53 emitted identities are permanently reserved. |
| Diagnostics / logging | **b52 reasoning-gap Runtime classified; b53 adds bounded reasoning/tool structure signatures** | `DiagnosticsLogger` + `NativeWebSendEngineProbe` | b52 final answer was complete while visible reasoning beginning was slightly truncated; no inactive value-only/root-nonexact frame occurred. b53 logs only bounded safe event/path/content-type structure; no text/raw IDs. |
| IPA build / CI packaging | **Capability Stable; exact b53 CI/Artifact valid** | `scripts/build_ipa.sh`, workflow | b53 Push `33294541342` / Job `99211838094`, PR `33294542985` / Job `99211842336`, Artifact `9726996570`, IPA SHA `d5eee722...25dc`. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| User-visible official-Web protected Send | **Security-permitted; full-conversation production use blocked by long-chat Web performance** | TD-023/024/025/028 | Full mobile-Web conversation remains unacceptable as a daily-chat surface after exact-device long-conversation composer failure. b48-b53 instead test a diagnostic Native surface over a Web Send engine; this does not change the durable production boundary. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. Phase 9 diagnostic Web uses the existing default persistent WebKit store. |
| Protocol-read diagnostic transport | Stable accepted diagnostic scope | `AuthTransientSession` + probes | Completion-handler transport buffers full response and is not an incremental stream owner. |
| Official same-response resume transport | **Runtime Confirmed on b45/b47** | official Web `/backend-api/f/conversation/resume` evidence | `POST` body `{conversation_id, offset}`; successful response HTTP200 SSE; repeated no-resend recovery can continue the same response. Exact offset semantics still Unverified. |
| Native resume parity diagnostic | **b46 + b47 duplicated parity Runtime rejected with HTTP404 JSON** | `NativeResumeParityProbeViewController` | Native first/exclusive resume and required browser context remain Unknown / Unverified. Resume work is not the active parser path in b48-b53. |
| Native Web Send-engine diagnostic | **b52 partial Runtime pass; b53 Runtime pending** | `NativeWebSendEngineProbeViewController` | b51 fixed fresh-new-chat missing-middle. b52 exact Runtime refined the remaining issue to visible reasoning beginning only; final answer was complete. b53 preserves b52 output and only identifies reasoning/tool structural grammar. Diagnostic exception only; no production repository mutation. |
| Native conversation read/recovery | **Stable merged baseline** | `ConversationRepository` | Sole native production conversation authority. b48-b53 do not mutate it. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Existing cache contracts retained. |
| Native message presentation geometry | **Stable merged b38 performance baseline** | `ConversationMessagePresentationProjection` + `ConversationMessageCell` | Bounded chunks/deterministic geometry/manual layout retained; this native path is not implicated in the mobile-Web composer freeze. |
| Conversation metadata / Preferences / round navigation | Stable merged b38 | `AppPreferences` + detail presentation | Existing preference/round-navigation semantics retained. |
| Conversation message rich rendering | Planned | Future `DEV-message-rendering` | Current production native body remains plain string. |
| Streaming / Send | **Active diagnostic architecture experiment; human Runtime gate on b53** | `DEV-send-stream`; PR #29 | Final-answer text capture materially passes the b52 tool-style reproduction; visible reasoning remains incomplete. b53 must identify explicit reasoning/tool SSE structure before collapse/expand, tool-call sheet or reasoning lifecycle implementation. TD-024/TD-025 remain unchanged; PR remains evidence-only. |
| User-visible reasoning / tool presentation | **In-scope / evidence-gated** | `DEV-send-stream`; `SEND_STREAM_PREFLIGHT.md` | Planned UX includes reasoning collapse/expand and tap-driven tool-call detail sheet/popover, but only explicitly user-visible service reasoning/tool data may be shown. Hidden chain-of-thought/internal tool nodes are prohibited. b53 Runtime is the current grammar gate. |
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
- b53 is Code/CI/Artifact/package verified and behavior-neutral; it only adds bounded unique reasoning/tool structural signatures. Runtime pending.
- Reasoning collapse/expand and tool-call detail sheet remain in current Work, but implementation waits for b53 grammar evidence.
- TD-024/TD-025 hidden/shadow-Web production restriction is unchanged; b48-b53 remain isolated diagnostic exceptions requested by the user.
- b39-b53 emitted identities are permanently reserved. Identity-invalid b46-transition Artifacts `9715858402`, `9715857814`, `9715907420`, `9715902353` and stale-b42 Artifact `9710515489` remain permanently rejected.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.