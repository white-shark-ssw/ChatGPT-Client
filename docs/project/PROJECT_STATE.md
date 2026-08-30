# Project State

_Last updated: 2026-08-30 through exact b62 focused iPhone/iOS17 Runtime classification. Phase 9 `DEV-send-stream` remains Active. b62 passed the tested verified-composer Send-entry / reasoning-final / exact-parent tool lifecycle gate; Stable/Frozen Send remains No._

## Current accepted merged baseline

Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21, list-cache b23 and **Phase 8 b38** remain accepted merged baselines for their recorded scopes. Exact b38 tested source is `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`. Stable does not mean Frozen.

## Current Work / target

`DEV-send-stream` is Active on `dev/send-stream-20260829`; PR #29 remains open / mergeable / unmerged and evidence-only. Final target-main synchronization remains required before any future merge.

Current exact tested diagnostic Candidate is **`DEV-send-stream-0.1.0-b62` / `0.1.0 (62)`**, exact product/config source `e1b44f7ab6c47bd41de3ed9460ec0b77b7cc9f3f`, Artifact `9733577825`, IPA SHA `ac9f031fb43b91ac12f486b1f743f741b404faf133725bdc8abec059b68b87d8`.

Evidence ladder: **Code written / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / focused Runtime passed; Stable/Frozen No.**

## Durable Phase 9 architecture/security boundary

- Exact b42 proves successful ChatGPT-account protected Send requires browser anti-abuse challenge output. Pure-native/transient-auth account Send remains blocked.
- The separately billed API-product route remains rejected; primary-account Sub2API/Codex-subscription Runtime remains blocked by the account-safety gate.
- TD-024/TD-025/TD-028 remain unchanged. Full existing-conversation mobile-Web rendering is not an accepted daily-chat dependency after the b47 long-answer composer failure.
- b48-b62 are **diagnostic exceptions only**. Their success does not approve hidden/shadow Web as production architecture and does not transfer production response ownership away from `ConversationRepository`.
- `ConversationRepository` remains sole native production conversation/list/detail/recovery/future accepted response authority; `AuthSessionStore` remains auth/account authority; default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Sync/Reload never resend/regenerate; no second Send may be created merely to obtain a stream.

## Current Send/stream evidence progression

- b45 Runtime Confirmed official no-resend `POST /backend-api/f/conversation/resume` with `{conversation_id, offset}` -> HTTP200 SSE; b46/b47 duplicated Native Cookie+Bearer-only resume returned HTTP404 JSON. Native first/exclusive resume remains Unknown / Unverified.
- b48-b51 established Native composer -> official protected Send and compact incremental text grammar, including fresh-new-chat continuation across `title_generation`.
- b52-b56 isolated reasoning/tool grammar and exact `reasoning_ended`, while keeping `assistant:thoughts` non-presentational.
- b57-b59 established Native reasoning/final split and exact service-marked thinking-preamble inclusion without the earlier leading gap.
- b60 preserved later reasoning paragraph boundaries, presented event-driven `正在思考`, and proved exact invocation→result parent association for tested traffic.
- b61 successful Runtime passed parent-paired tool-row lifecycle but a separate cold/new-page run exposed generic-`textarea` false readiness: `submitted` occurred with no actual protected Send observation.
- b62 removed only that exact generic-textarea authority, retaining only verified composer identities and adding no retry/timer/watchdog/fallback.

## Exact b62 focused Runtime

User export `ChatGPTClient-Diagnostics-20260830-151146.json` exactly matched Release / build62 / Candidate b62 / source `e1b44f7ab6c4` / iPhone / iOS17.0.

### Composer / Send entry

Observed cold-launch path:

- composer `ready=false / strategy=none`;
- page loaded `new_or_other`;
- composer remained `ready=false / strategy=none`;
- only later became `ready=true / strategy=prompt_textarea`;
- submit-time strategy remained `prompt_textarea`;
- `submitResult=submitted` was followed by real `sendObserved` in the same second;
- response HTTP200 `text/event-stream`;
- thinking presentation entered from accepted response lifecycle.

Classification: **focused Runtime pass for the exact b62 verified-composer Send-entry gate.** This is scoped to the observed cold-launch path and does not claim the intermittent b61 page race is impossible forever.

### Reasoning / final / tool lifecycle

Terminal metrics:

- frameCount `196`, terminal `true`;
- Native reasoning `34 deltas / 497 chars`;
- preambles `3 / 20 chars`;
- reasoning segment breaks `2`, reasoning-active signals `3`, Native thinking presentations `4`;
- exact reasoning-end `1`, fallback false;
- final answer `93 deltas / 2878 chars`;
- Native total `127 deltas / 3375 chars`;
- results `20`, parent present/matched/unmatched/missing `20/20/0/0`;
- paired Native result presentations `20`;
- Native tool presentations/completion updates `20/20`.

User directly reported the single tested round looked normal; screenshot showed visible reasoning, completed tool rows and complete-looking final text with no obvious truncation.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b62-runtime.md`.

## Current unresolved evidence boundary

Expandable tool details remain part of `DEV-send-stream`, but exact user-visible schema is still **Unknown / Unverified**. b62 safe structural observations include string-shaped `connector_tool_payload`, bounded `reasoning_titles` / `tool_icons`, object-shaped `invoked_resource`, and `inline_cot_expandable_content` on an `assistant:thoughts` structure. These shapes do **not** authorize raw values/bodies or `assistant:thoughts` presentation.

Do not allocate b63 from field-name guesses. A future candidate requires one concrete evidence need and a fresh uniqueness/conflict guard.

## Remaining Unknown / Unverified

Accepted production incremental-response ownership, exact cross-tool user-visible expandable-detail schema, Native first/exclusive resume, existing-conversation pre-React history virtualization, full 5/15-minute background behavior, WebContent termination, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified where not explicitly tested. CI/Artifact success is never Runtime proof.
