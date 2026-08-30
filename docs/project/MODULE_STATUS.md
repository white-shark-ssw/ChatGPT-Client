# Module Status

| Module | Status | Owner / baseline | Current evidence / boundary |
|---|---|---|---|
| Repository AI governance | Active | `main@1ac202c...` `AGENTS.md` + `docs/project/START_HERE.md` | Autonomous continuation, checkpoint, evidence ladder and conflict rules active; final target sync required before merge. |
| Native application shell | **Stable b38 baseline** | `AppDelegate.swift`, `RootViewController.swift` | Phase 9 diagnostics do not redefine ordinary native read/navigation ownership. Frozen No. |
| Build/runtime metadata | **b58 exact diagnostic identity; Runtime pending** | Xcode settings / built `Info.plist` | `0.1.0 (58)`, Candidate b58, exact source `d9dbf208625e...`, Artifact `9729864129`; b39-b58 permanently reserved. |
| Diagnostics / logging | **b57 Runtime passed phase split; b58 adds tool aggregates** | `DiagnosticsLogger` + `NativeWebSendEngineProbe` | b58 logs invocation/result counts and title character counts only; never tool title text, raw args/results, IDs, auth/proof values. |
| IPA build / CI packaging | **Stable capability; b58 exact Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33303998650/99237187408`, PR `33304001877/99237195550`, Artifact `9729864129`, ZIP `sha256:3a907e6b...60ac`, IPA `0d5988ca...b8875`; Release / iOS14 / `[1,2]` / arm64. |
| Embedded Web login | Stable explicit fallback | `AuthWebViewController.swift` | Default persistent WebKit store remains persistent auth-secret authority. |
| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. |
| Protocol-read transport | Stable diagnostic scope | transient auth + probes | Completion-handler native read transport is not incremental response owner. |
| Official same-response resume | **Runtime Confirmed b45/b47** | official Web `/backend-api/f/conversation/resume` | HTTP200 SSE no-resend continuation; exact offset semantics still Unverified. |
| Native resume parity | **Rejected for tested duplicated path** | `NativeResumeParityProbeViewController` | b46/b47 Cookie+Bearer-only duplicate returned HTTP404 JSON; first/exclusive Native resume Unknown. |
| User-visible official-Web protected Send | **Security-permitted, daily full-Web product blocked** | TD-023/024/025/028 | b47 long-answer composer freeze blocks full conversation Web as production dependency. b48-b58 remain diagnostic exceptions only. |
| Native Web Send-engine diagnostic | **b57 Runtime phase split passed; b58 Runtime pending** | `NativeWebSendEngineProbeViewController` | b57 separated reasoning/final and no prefix truncation reproduced. b58 adds bounded Native tool-activity presentation while preserving b57 text behavior. |
| Native conversation read/recovery | **Stable merged baseline** | `ConversationRepository` | Sole native production conversation/list/read/recovery/future accepted response authority. b48-b58 do not mutate it. |
| Conversation-list cache | Stable merged | `ConversationRepository` + `ConversationListCacheStore` | Accepted b23 contracts retained. |
| Native message geometry / round navigation | **Stable merged b38** | presentation projection + message cell | Deterministic bounded geometry and accepted continuous quick-navigation retained. |
| Conversation message rich rendering | Planned | future `DEV-message-rendering` | Production native body still plain text; only authoritative user-visible content may enter future rich rendering. |
| Streaming / Send | **Active diagnostic architecture experiment** | `DEV-send-stream`; PR #29 | b57 reasoning/final gate passed. b58 tests bounded tool activity. TD-024/025/028 unchanged; PR evidence-only/unmerged. |
| User-visible reasoning | **b57 exact Runtime pass** | `DEV-send-stream` | `reasoning_ended` is accepted phase marker; recap text is not reasoning body. Raw `assistant:thoughts` remains prohibited. |
| Tool activity presentation | **b58 Code/CI/Artifact passed; Runtime pending** | `DEV-send-stream` | Only exact completed assistant-code invocation produces compact activity line; service `reasoning_title` transiently if present, generic fallback otherwise. Result body is never shown. |
| Background completion | **Hard requirement; production owner pending** | `BACKGROUND_EXECUTION_PLAN.md` | b45/b49 positive short-background evidence only; 5/15-minute and termination gates remain. |
| Attachments | **High priority; Send-boundary dependent** | future `DEV-attachments` | iOS17 native photo+video path still needs evidenced handoff; no private WebKit/DOM file injection. |

## Current acceptance boundary

- Stable merged native baseline remains exact b38 for recorded scope.
- b42 protected-Send security boundary and b45 official resume evidence remain accepted.
- Full mobile-Web existing-conversation Send remains blocked as daily production dependency.
- b51 fixed fresh-new-chat continuation; b52 isolated remaining reasoning gap; b53-b55 identified reasoning/tool grammar; b56 corrected recap-body assumption.
- **b57 Runtime passed:** reasoning streamed only in `思考过程`, final answer stayed separate, prior leading truncation did not reproduce; tool activity remained absent.
- **b58 Code/CI/Artifact/package passed; Runtime pending:** compact tool-activity region only, no raw tool payloads.
- TD-024/TD-025/TD-028 unchanged; b48-b58 remain isolated diagnostic exceptions.
- b39-b58 emitted identities are permanently reserved. Phase 9 Stable/Frozen: No.

## Auto-refresh rule

Update this matrix whenever ownership, Candidate identity, CI/Artifact evidence, accepted Runtime behavior or stability changes.
