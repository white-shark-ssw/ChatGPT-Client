# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | latest `main@1ac202c...` root `AGENTS.md` + `docs/project/START_HERE.md` | Current rules include autonomous continuation, rolling checkpoints, non-atomic batch recovery, same-session identity reuse and Full/Light Resume Guards. Feature branch still needs final rules synchronization before merge. |
| Native application shell | **Stable b38 baseline; b44 full-page trial rejected** | `AppDelegate.swift`, `RootViewController.swift`; Stable b38 behavior retained | Phase 9 diagnostics do not redefine ordinary native read/navigation ownership. Frozen No. |
| Build/runtime metadata | **b47 Runtime-tested diagnostic identity** | Xcode settings / `Info.plist` | Exact legitimate b47: `0.1.0 (47)`, Candidate `DEV-send-stream-0.1.0-b47`, source `21028bb...`, Artifact `9716878034`. Any changed product code requires b48+. |
| Diagnostics / logging | **b47 Runtime-valid with one known field-name defect** | `DiagnosticsLogger` | b47 captured privacy-safe header names + rejection JSON shape. `safeErrorTokens` was redacted because sanitizer redacts keys containing `token`; correcting it requires b48+ if still useful. |
| IPA build / CI packaging | **Capability Stable; exact b47 CI/Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33259640112` / Job `99119258573`, PR `33259642459` / Job `99119264902`, Artifact `9716878034`, IPA SHA `49d1bd48...6909`. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| User-visible official-Web protected Send | **Security-permitted but production viability blocked by long-conversation composer failure** | TD-023/024/025 + exact b47 user Runtime | Visible official Web may legally perform protected Send, but an exact target-device long conversation (~3 long-answer rounds) repeatedly froze when trying to use the mobile-Web composer. Root cause Unverified; production dependency on full Web conversation is now a P0 architecture gate. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. b47 transient cookie+bearer re-verification succeeded during parity attempt. |
| Protocol-read diagnostic transport | Stable accepted diagnostic scope | `AuthTransientSession` + probes | Completion-handler transport buffers full response and is not an incremental stream owner. |
| Official same-response resume transport | **Runtime Confirmed on b45/b47** | official Web `/backend-api/f/conversation/resume` evidence | `POST` body `{conversation_id, offset}`; successful response HTTP200 SSE; repeated no-resend recovery can continue the same response. Exact offset semantics still Unverified. |
| Native resume parity diagnostic | **b46 + b47 duplicated parity Runtime rejected with HTTP404 JSON** | `NativeResumeParityProbeViewController` | b47 official offset 23 returned 200 SSE, Native same-body Cookie+Bearer-only duplicate returned 404 JSON, later official offset 74 returned 200 SSE. Header-name difference is large but required context vs second-consumer/cursor ownership remains unresolved. |
| Native conversation read/recovery | **Stable merged baseline** | `ConversationRepository` | Sole native conversation authority. Phase 9 diagnostics must not mutate it until Native continuation is accepted. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Existing cache contracts retained. |
| Native message presentation geometry | **Stable merged b38 performance baseline** | `ConversationMessagePresentationProjection` + `ConversationMessageCell` | Bounded chunks/deterministic geometry/manual layout retained; this native path is not implicated in the reported mobile-Web composer freeze. |
| Conversation metadata / Preferences / round navigation | Stable merged b38 | `AppPreferences` + detail presentation | Existing preference/round-navigation semantics retained. |
| Conversation message rich rendering | Planned | Future `DEV-message-rendering` | Current native body remains plain string. |
| Streaming / Send | **Active Human Architecture Gate** | `DEV-send-stream`; PR #29 | Protected Send remains browser-owned under current evidence. Official resume exists, but Native duplicated parity still 404 and the full-Web composer now has a demonstrated long-conversation pre-Send failure. Do not allocate b48 merely to chase headers until product Send boundary is selected. |
| Background execution / completion | **Positive short-background signal; response-owner dependent** | `BACKGROUND_EXECUTION_PLAN.md` | b45 short background/lock survived/buffered. Native response ownership is still unaccepted; current full-Web Send viability is also blocked. |
| Attachments | **High priority; iOS17 Web chooser limitation evidenced** | Future `DEV-attachments` | Web `+` ~100–200ms accepted in b43, Web Photos filtered video; iOS17 native photo+video path still needs separate evidence. |

## Current acceptance boundary

- Stable merged native baseline remains exact b38 for its recorded scope.
- b42 remains accepted protected-Send security evidence; pure-native/transient-auth protected Send remains blocked.
- b43 visible-Web smoothness is accepted only for its tested shorter-sequence scope and is **not** proof of long-conversation daily-use viability.
- b44 mapping/eventual-read observations accepted; full-page hybrid UX rejected.
- b45 official no-resend `/backend-api/f/conversation/resume` is **Runtime Confirmed**.
- Exact b46 source `4ab9be3...` / Artifact `9715903443`: Native Cookie+Bearer-only duplicated resume returned HTTP404 JSON while official Web resume remained healthy.
- Exact b47 source `21028bb...` / Artifact `9716878034`: same Native duplicated parity class again returned HTTP404 JSON; official request header-name set is much richer than Native but no required header subset was established.
- b47 rejection shape: `{"detail":{"code":"string","message":"string"}}`; safe code token export was accidentally redacted by the generic sanitizer because the field key contained `token`.
- Exact-device long-conversation Web composer usability failed before Send; root cause Unknown, product impact P0.
- Fully hidden Web + Native DOM/button injection remains prohibited.
- b39-b47 identities are permanently reserved once emitted.
- Identity-invalid intermediate b46-transition Artifacts `9715858402`, `9715857814`, `9715907420`, `9715902353` remain permanently rejected.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.