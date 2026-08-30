# Project State

_Last updated: 2026-08-30 through exact b63 Code/CI/Artifact/package verification. Phase 9 `DEV-send-stream` remains Active. b62 retains its focused iPhone/iOS17 Runtime pass; b63 is diagnostic-only and Runtime Pending. Stable/Frozen Send remains No._

## Current accepted merged baseline

Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21, list-cache b23 and **Phase 8 b38** remain accepted merged baselines for their recorded scopes. Exact b38 tested source is `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`. Stable does not mean Frozen.

## Current Work / target

`DEV-send-stream` is Active on `dev/send-stream-20260829`; PR #29 remains open / mergeable / unmerged and evidence-only. Final target-main synchronization remains required before any future merge.

Current exact diagnostic Candidate is **`DEV-send-stream-0.1.0-b63` / `0.1.0 (63)`**:

- exact product/config source `0c2e2b870e51c363c7734182d49618c438839cc2`;
- product tree `cae7f27e2800fe48f8d492bfd364c91755935c67`;
- Push `33321982009 / 99285436158` — success;
- PR `33321983658 / 99285440962` — success;
- Artifact `9735145598`;
- ZIP `sha256:645cba67a91387f79d386931b5d0f4ead2502408b15c7f339013505e3f0ec7da`;
- IPA `sha256:b347d1e41ca5a4e1355a9cc713574ea96247e11918ccfb1f5ff621a0f9f6ff36`;
- package Release / source marker `0c2e2b870e51` / minimum iOS14 / UIDeviceFamily `[1,2]` / arm64.

Evidence ladder: **Code written / diff audited / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Runtime pending; Stable/Frozen No.**

## Durable Phase 9 architecture/security boundary

- Exact b42 proves successful ChatGPT-account protected Send requires browser anti-abuse challenge output. Pure-native/transient-auth account Send remains blocked.
- The separately billed API-product route remains rejected; primary-account Sub2API/Codex-subscription Runtime remains blocked by the account-safety gate.
- TD-024/TD-025/TD-028 remain unchanged. Full existing-conversation mobile-Web rendering is not an accepted daily-chat dependency after the b47 long-answer composer failure.
- b48-b63 are **diagnostic exceptions only**. Their success does not approve hidden/shadow Web as production architecture and does not transfer production response ownership away from `ConversationRepository`.
- `ConversationRepository` remains sole native production conversation/list/detail/recovery/future accepted response authority; `AuthSessionStore` remains auth/account authority; default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Sync/Reload never resend/regenerate; no second Send may be created merely to obtain a stream.

## Current Send/stream evidence progression

- b45 Runtime Confirmed official no-resend `POST /backend-api/f/conversation/resume` with `{conversation_id, offset}` -> HTTP200 SSE; b46/b47 duplicated Native Cookie+Bearer-only resume returned HTTP404 JSON. Native first/exclusive resume remains Unknown / Unverified.
- b48-b51 established Native composer -> official protected Send and compact incremental text grammar, including fresh-new-chat continuation across `title_generation`.
- b52-b56 isolated reasoning/tool grammar and exact `reasoning_ended`, while keeping raw `assistant:thoughts` non-presentational.
- b57-b59 established Native reasoning/final split and exact service-marked thinking-preamble inclusion without the earlier leading gap.
- b60 preserved later reasoning paragraph boundaries, presented event-driven `正在思考`, and proved exact invocation→result parent association for tested traffic.
- b61 successful Runtime passed parent-paired tool-row lifecycle but a separate cold/new-page run exposed generic-`textarea` false readiness.
- b62 removed only that exact generic-textarea authority and passed the focused verified-composer Runtime gate while retaining reasoning/final and exact-parent tool lifecycle.
- b63 does **not** alter b62 response behavior. It adds only bounded expandable-detail structure diagnostics needed to determine whether any service field can safely back a future user-visible Native tool-detail expansion.

## Exact b62 focused Runtime retained

User export `ChatGPTClient-Diagnostics-20260830-151146.json` exactly matched Release / build62 / Candidate b62 / source `e1b44f7ab6c4` / iPhone / iOS17.0.

Observed Send path reached real `sendObserved` and HTTP200 `text/event-stream` only after `prompt_textarea` became the verified composer. Terminal metrics included Native reasoning `34/497`, final answer `93/2878`, exact reasoning-end `1`, tool result parent matches `20/20`, and Native tool presentations/completion updates `20/20`. User reported the tested round looked normal with complete-looking reasoning/final output.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b62-runtime.md`.

## Exact b63 diagnostic boundary

b63 is justified by current b62 structures, not field-name guesswork:

- `metadata.connector_tool_payload` repeatedly appears as a string on finished assistant tool-invocation messages;
- `metadata.inline_cot_expandable_content` appears as an object on finished assistant `thoughts` structures and can contain `source_message_ids`;
- exact result-parent association already uses one response-local transient invocation-ID Map.

b63 records only:

- `connectorToolPayloadJSONShape`: JSON parse class plus sanitized top-level key/type/direct string-or-array length fingerprint, capped to 180 characters;
- aggregate inline-expandable message/reference counts and source-reference matches against existing response-local invocation/tool-activity identities.

It does **not** export connector payload values, nested request/result bodies, raw IDs or `assistant:thoughts`, and it does not present expandable Native bodies. Composer detection, protected Send, SSE text grammar, reasoning/final split, exact reasoning end and tool-row lifecycle remain b62 behavior.

The focused b63 Runtime gate is one exact iPhone/iOS17 tool-active response plus same-response official-Web expanded-detail screenshot if the official UI exposes it, followed by diagnostics export. Only same-run evidence may authorize a later detail mapping.

## Remaining Unknown / Unverified

Accepted production incremental-response ownership, exact cross-tool user-visible expandable-detail schema, Native first/exclusive resume, existing-conversation pre-React history virtualization, full 5/15-minute background behavior, WebContent termination, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified where not explicitly tested. CI/Artifact success is never Runtime proof.
