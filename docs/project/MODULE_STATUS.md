# Module Status

| Module | Status | Owner / baseline | Current evidence / boundary |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/START_HERE.md` | Checkpoint/evidence/conflict rules active; final target sync required before merge. |
| Native application shell | **Stable b38 baseline** | `AppDelegate.swift`, `RootViewController.swift` | Phase 9 diagnostics do not redefine ordinary native read/navigation ownership. Frozen No. |
| Build/runtime metadata | **b63 exact diagnostic identity; Runtime pending** | Xcode settings / built `Info.plist` | `0.1.0 (63)`, Candidate b63, exact source `0c2e2b870e51...`, Artifact `9735145598`; b39-b63 permanently reserved. |
| Diagnostics / logging | **b63 artifact verified; focused detail-schema Runtime pending** | `DiagnosticsLogger` + `NativeWebSendEngineProbe` | Adds bounded connector-payload JSON top-level fingerprint + aggregate expandable source-reference match counts only. Raw IDs/values/bodies/auth/proof remain prohibited. |
| IPA build / CI packaging | **Stable capability; b63 exact Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33321982009/99285436158`, PR `33321983658/99285440962`, Artifact `9735145598`, ZIP `645cba67...ec7da`, IPA `b347d1e4...ff36`; Release / iOS14 / `[1,2]` / arm64. |
| Embedded Web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. |
| Protocol-read transport | Stable diagnostic scope | transient auth + probes | Completion-handler native read transport is not incremental response owner. |
| Official same-response resume | **Runtime Confirmed b45/b47** | official Web `/backend-api/f/conversation/resume` | HTTP200 SSE no-resend continuation; exact offset semantics still Unverified. |
| Native resume parity | **Rejected for tested duplicated path** | `NativeResumeParityProbeViewController` | b46/b47 Cookie+Bearer-only duplicate returned HTTP404 JSON; first/exclusive Native resume Unknown. |
| User-visible official-Web protected Send | **Security-permitted, daily full-Web product blocked** | TD-023/024/025/028 | b47 long-answer composer freeze blocks full conversation Web as production dependency. b48-b63 remain diagnostic exceptions only. |
| Native Web Send-engine diagnostic | **b62 focused Runtime pass; b63 structure diagnostic Artifact ready** | `NativeWebSendEngineProbeViewController` | b62 cold-launch verified-composer path passed. b63 preserves it and adds only safe expandable-detail structure evidence; b63 Runtime pending. |
| Native conversation read/recovery | **Stable merged baseline** | `ConversationRepository` | Sole native production conversation/list/read/recovery/future accepted response authority. b48-b63 do not mutate it. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Accepted b23 contracts retained. |
| Native message geometry / round navigation | **Stable merged b38** | presentation projection + message cell | Deterministic bounded geometry and accepted continuous quick-navigation retained. |
| Conversation message rich rendering | Planned | future `DEV-message-rendering` | General Markdown/code/table/link/citation rendering remains separate; response lifecycle/tool-card semantics stay in `DEV-send-stream`. |
| Streaming / Send | **Active diagnostic architecture experiment; b62 tested gate passed, b63 Runtime pending** | `DEV-send-stream`; PR #29 | b62 verifies explicit composer identity normal path and real protected Send; accepted production response ownership remains pending. |
| User-visible reasoning | **b62 tested presentation passed; b63 behavior unchanged** | `DEV-send-stream` | Event-driven `正在思考`, 497-char reasoning, segment breaks, exact `reasoning_ended` and complete-looking final answer retained; raw `assistant:thoughts` body remains prohibited. |
| Tool activity presentation | **b62 tested lifecycle passed; b63 behavior unchanged** | `DEV-send-stream` | 20 results, parent match `20/20`, 0 unmatched/missing, Native presentations/completion updates `20/20`; rows visibly completed. Expandable raw detail still unauthorized. |
| Expandable tool detail | **Active focused evidence gate; b63 Artifact ready** | `DEV-send-stream` | b63 records safe `connectorToolPayloadJSONShape` and aggregate `inline_cot_expandable_content.source_message_ids` matches only. Exact official user-visible field mapping remains Unknown / Unverified until same-run Runtime + Web screenshot evidence. |
| Background completion | **Hard requirement; production owner pending** | `BACKGROUND_EXECUTION_PLAN.md` | b45/b49 positive short-background evidence only; 5/15-minute and termination gates remain. |
| Attachments | **High priority; Send-boundary dependent** | future `DEV-attachments` | iOS17 native photo+video path still needs evidenced handoff; no private WebKit/DOM file injection. |

## Current acceptance boundary

- Stable merged native baseline remains exact b38 for recorded scope.
- b42 protected-Send security boundary and b45 official resume evidence remain accepted.
- Full mobile-Web existing-conversation Send remains blocked as daily production dependency.
- b51 title continuation, b55/b56 reasoning-end, b57 phase split, b59 exact preamble inclusion and b60 thinking/segmentation/parent association remain accepted diagnostic evidence.
- **Exact b61 Runtime:** successful tool-active turn passed thinking/reasoning/final and parent-paired row lifecycle (`14/14` matched and `14` completion updates); separate first run captured false-ready generic textarea with submitted but no protected Send. Overall Runtime Partial.
- **Exact b62 Runtime:** one focused cold-launch tool-active run passed the verified-composer gate: `ready=false/none -> ready=true/prompt_textarea -> submitted -> sendObserved -> HTTP200 SSE -> terminal`; reasoning/final appeared complete and exact-parent tool completion passed `20/20`.
- **Exact b63 pre-Runtime:** code diff audited; Push + PR CI passed; Artifact/package identity independently verified. b63 changes diagnostics only and does not yet establish any expandable-detail presentation semantics.
- TD-024/TD-025/TD-028 unchanged; b48-b63 remain isolated diagnostic exceptions.
- b39-b63 emitted identities are permanently reserved. Phase 9 Stable/Frozen: No.

## Auto-refresh rule

Update this matrix whenever ownership, Candidate identity, CI/Artifact evidence, accepted Runtime behavior or stability changes.
