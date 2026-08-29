# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | latest `main@1ac202c...` root `AGENTS.md` + `docs/project/START_HERE.md` | Current rules include autonomous continuation, rolling checkpoints, non-atomic batch recovery, same-session identity reuse and Full/Light Resume Guards. Feature branch still needs final rules synchronization before merge. |
| Native application shell | **Stable b38 baseline; b44 full-page trial rejected** | `AppDelegate.swift`, `RootViewController.swift`; Stable b38 behavior retained | Phase 9 diagnostics do not redefine ordinary native read/navigation ownership. Frozen No. |
| Build/runtime metadata | **b52 exact diagnostic identity; Runtime pending** | Xcode settings / `Info.plist` | Exact b52: `0.1.0 (52)`, Candidate `DEV-send-stream-0.1.0-b52`, product source `5c0690c...`, Artifact `9721532867`. b39-b52 emitted identities are permanently reserved. |
| Diagnostics / logging | **b51 title-generation fix Runtime confirmed; b52 adds structural gap classifier** | `DiagnosticsLogger` + `NativeWebSendEngineProbe` | b51 first fresh long answer exercised title-generation count 1 and was visually complete. b52 only classifies exact/non-exact/nested text patches, inactive value-only frames and resets; no parser broadening. Diagnostics remain structural/aggregate only. |
| IPA build / CI packaging | **Capability Stable; exact b52 CI/Artifact valid** | `scripts/build_ipa.sh`, workflow | b52 Push `33276080936` / Job `99162937523`, PR `33276082767` / Job `99162942750`, Artifact `9721532867`, IPA SHA `a3de5c6e...46b23`. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| User-visible official-Web protected Send | **Security-permitted; full-conversation production use blocked by long-chat Web performance** | TD-023/024/025/028 | Full mobile-Web conversation remains unacceptable as a daily-chat surface after exact-device long-conversation composer failure. b48-b52 instead test a diagnostic Native surface over a Web Send engine; this does not change the durable production boundary. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. Phase 9 diagnostic Web uses the existing default persistent WebKit store. |
| Protocol-read diagnostic transport | Stable accepted diagnostic scope | `AuthTransientSession` + probes | Completion-handler transport buffers full response and is not an incremental stream owner. |
| Official same-response resume transport | **Runtime Confirmed on b45/b47** | official Web `/backend-api/f/conversation/resume` evidence | `POST` body `{conversation_id, offset}`; successful response HTTP200 SSE; repeated no-resend recovery can continue the same response. Exact offset semantics still Unverified. |
| Native resume parity diagnostic | **b46 + b47 duplicated parity Runtime rejected with HTTP404 JSON** | `NativeResumeParityProbeViewController` | Native first/exclusive resume and required browser context remain Unknown / Unverified. Resume work is not the active parser path in b48-b52. |
| Native Web Send-engine diagnostic | **b51 partial Runtime pass; b52 Runtime pending** | `NativeWebSendEngineProbeViewController` | b51 fixed the fresh-new-chat missing-middle path: first long reply 11,618 Native chars / 284 deltas / title-generation count 1 and visually complete. A separate GitHub/tool-style turn had a small leading gap. b52 preserves b51 output semantics and only measures the structural gap class. Diagnostic exception only; no production repository mutation. |
| Native conversation read/recovery | **Stable merged baseline** | `ConversationRepository` | Sole native production conversation authority. b48-b52 do not mutate it. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Existing cache contracts retained. |
| Native message presentation geometry | **Stable merged b38 performance baseline** | `ConversationMessagePresentationProjection` + `ConversationMessageCell` | Bounded chunks/deterministic geometry/manual layout retained; this native path is not implicated in the mobile-Web composer freeze. |
| Conversation metadata / Preferences / round navigation | Stable merged b38 | `AppPreferences` + detail presentation | Existing preference/round-navigation semantics retained. |
| Conversation message rich rendering | Planned | Future `DEV-message-rendering` | Current production native body remains plain string. |
| Streaming / Send | **Active diagnostic architecture experiment; human Runtime gate on b52** | `DEV-send-stream`; PR #29 | b51 Runtime confirmed title-generation preservation fixes the fresh-new-chat missing middle. b52 now targets only the distinct GitHub/tool-style leading truncation with behavior-neutral structural counters. TD-024/TD-025 remain unchanged; PR remains evidence-only. |
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
- **b51 Runtime confirms the narrow `title_generation` continuation-preserve correction fixes that fresh-new-chat missing-middle failure on the exact test.** A separate third GitHub/tool-style turn still showed a small leading truncation and title-generation count 0, so parser coverage is not complete.
- b52 is Code/CI/Artifact/package verified and behavior-neutral: it only adds aggregate classification needed to identify the leading-gap frame class. Runtime pending.
- TD-024/TD-025 hidden/shadow-Web production restriction is unchanged; b48-b52 remain isolated diagnostic exceptions requested by the user.
- b39-b52 emitted identities are permanently reserved. Identity-invalid b46-transition Artifacts `9715858402`, `9715857814`, `9715907420`, `9715902353` and stale-b42 Artifact `9710515489` remain permanently rejected.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.