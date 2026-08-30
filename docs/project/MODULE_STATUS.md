# Module Status

| Module | Status | Owner / baseline | Current evidence / boundary |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/START_HERE.md` | Checkpoint/evidence/conflict rules active; final target sync required before merge. |
| Native application shell | **Stable b38 baseline** | `AppDelegate.swift`, `RootViewController.swift` | Phase 9 diagnostics do not redefine ordinary native read/navigation ownership. Frozen No. |
| Build/runtime metadata | **b65 exact diagnostic identity; Runtime pending** | Xcode settings / built `Info.plist` | `0.1.0 (65)`, Candidate b65, exact source `44138db766d0...`, Push Artifact `9736876465`; b39-b65 permanently reserved. |
| Diagnostics / logging | **b65 behavior preserved; privacy contract unchanged** | `DiagnosticsLogger` + `NativeWebSendEngineProbe` | Raw prompt/answer/reasoning/tool bodies/IDs/auth/proof remain excluded from export; b65 logs only structural presentation state/counts. |
| IPA build / CI packaging | **Stable capability; b65 exact Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33328232044/99302071335`, PR `33328233842/99302076369`, Push Artifact `9736876465`, ZIP `d9a52ecb...ceb7a`, IPA `e6a01b2e...38d16`; Release / iOS14 / `[1,2]` / arm64. |
| Embedded Web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. |
| Protocol-read transport | Stable diagnostic scope | transient auth + probes | Completion-handler native read transport is not incremental response owner. |
| Official same-response resume | **Runtime Confirmed b45/b47** | official Web `/backend-api/f/conversation/resume` | HTTP200 SSE no-resend continuation; exact offset semantics still Unverified. |
| Native resume parity | **Rejected for tested duplicated path** | `NativeResumeParityProbeViewController` | b46/b47 Cookie+Bearer-only duplicate returned HTTP404 JSON; first/exclusive Native resume Unknown. |
| User-visible official-Web protected Send | **Security-permitted, daily full-Web product blocked** | TD-023/024/025/028 | b47 long-answer composer freeze blocks full conversation Web as production dependency. b48-b65 remain diagnostic exceptions only. |
| Native Web Send-engine diagnostic | **b64 Runtime partial-pass; b65 Artifact ready** | `NativeWebSendEngineProbeViewController` | b64 exact protected Send/reasoning/final/exact-parent detail lifecycle passed; only detail formatting/density rejected. b65 corrects presentation only; Runtime pending. |
| Native conversation read/recovery | **Stable merged baseline** | `ConversationRepository` | Sole native production conversation/list/read/recovery/future accepted response authority. b48-b65 do not mutate it. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Accepted b23 contracts retained. |
| Native message geometry / round navigation | **Stable merged b38** | presentation projection + message cell | Deterministic bounded geometry and accepted continuous quick-navigation retained. |
| Conversation message rich rendering | Planned | future `DEV-message-rendering` | General Markdown/code/table/link/citation rendering remains separate; response lifecycle/tool-card semantics stay in `DEV-send-stream`. |
| Streaming / Send | **Active diagnostic architecture experiment; b64 tested transport/lifecycle pass, b65 Runtime pending** | `DEV-send-stream`; PR #29 | Verified composer + real protected Send remains positive in b64; accepted production response ownership remains pending. |
| User-visible reasoning | **b64 tested presentation passed; b65 behavior unchanged** | `DEV-send-stream` | b64 reasoning `27/440`, exact `reasoning_ended=1`, final `215/6716`, no apparent truncation; raw `assistant:thoughts` remains prohibited. |
| Tool activity presentation | **b64 exact-parent lifecycle passed; b65 behavior unchanged** | `DEV-send-stream` | 30 Native presentations/completion updates; 30 exact parent matches, 5 unmatched not force-paired, 0 missing. |
| Expandable tool detail | **GitHub mapping Runtime-backed; b65 formatting gate pending** | `DEV-send-stream` | b63 same-run evidence authorized GitHub connector input + exact-parent result content; b64 proved 26 detail-capable rows and expansion works but formatting is poor; b65 adds nested input/output disclosures + decoded hierarchy only. |
| Background completion | **Hard requirement; production owner pending** | `BACKGROUND_EXECUTION_PLAN.md` | b45/b49 positive short-background evidence only; 5/15-minute and termination gates remain. |
| Attachments | **High priority; Send-boundary dependent** | future `DEV-attachments` | iOS17 native photo+video path still needs evidenced handoff; no private WebKit/DOM file injection. |

## Current acceptance boundary

- Stable merged native baseline remains exact b38 for recorded scope.
- b42 protected-Send security boundary and b45 official resume evidence remain accepted.
- Full mobile-Web existing-conversation Send remains blocked as daily production dependency.
- b51 title continuation, b55/b56 reasoning-end, b57 phase split, b59 exact preamble inclusion and b60 thinking/segmentation/parent association remain accepted diagnostic evidence.
- b62 retains the focused verified-composer Send-entry pass.
- b63 Runtime + same-response official-Web evidence authorized the minimal GitHub expandable-detail mapping only.
- **Exact b64 Runtime:** protected Send reached HTTP200 SSE/terminal; reasoning/final appeared complete; exact-parent rows completed `30/30`; detail expansion worked. Runtime rejected only escaped/dense detail rendering.
- **Exact b65 pre-Runtime:** product diff audited; Push + PR CI passed; Push Artifact/package identity independently verified. b65 changes Native detail presentation only.
- TD-024/TD-025/TD-028 unchanged; b48-b65 remain isolated diagnostic exceptions.
- b39-b65 emitted identities are permanently reserved. Phase 9 Stable/Frozen: No.

## Auto-refresh rule

Update this matrix whenever ownership, Candidate identity, CI/Artifact evidence, accepted Runtime behavior or stability changes.
