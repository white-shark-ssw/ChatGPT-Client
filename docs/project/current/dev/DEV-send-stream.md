# DEV-send-stream

## Status

**Active — user explicitly selected production architecture Option B. Exact b65 passed the focused iPhone/iOS17 Send/reasoning/final/exact-parent GitHub tool-detail Runtime gate; the b64 detail-formatting defect is closed for the tested shapes. The covered official-Web Send engine proven by b48-b65 is now explicitly authorized as the production protected-Send transport/challenge executor, while `ConversationRepository` remains the sole native production conversation/response authority. A reusable Web Rule Lab is now part of this Work so future ChatGPT Web-rule changes can be probed from one installed IPA before product code is rebuilt. Stable/Frozen Send remains No. PR #29 remains open / mergeable / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged
- Other Active development checkpoints: none at latest guard
- Current actual `main`: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`
- Current branch head before this checkpoint update: `8e740f407350ee27f2094a8cbcd64e618d1e3ef1`
- Stable native predecessor: b38
- Exact latest Runtime-tested Candidate: `DEV-send-stream-0.1.0-b65`
- Exact b65 product/config source: `44138db766d00e62cfda7f20182f6d20f1ec3352`
- b65 Push Run / Job: `33328232044 / 99302071335` — success
- b65 PR Run / Job: `33328233842 / 99302076369` — success
- b65 Push Artifact: `9736876465`
- b65 IPA SHA-256: `e6a01b2eafd361b9df2567b002f9e8aa56b57dcee219c7999c65767b91138d16`
- b39-b65 emitted identities: permanently reserved
- b66: **not yet emitted; may be allocated only as the first coherent production/Web-Lab slice, with code+build+workflow identity aligned atomically before the formal branch moves**

## Exact b65 Runtime — focused pass

User export: `ChatGPTClient-Diagnostics-20260830-191806.json`.

Package identity matched exact b65: Release / build65 / Candidate b65 / source `44138db766d0` / iPhone / iOS17.0.

Observed path:

`ready=false/none -> ready=true/prompt_textarea -> nativeSubmit -> submitted -> sendObserved(existing_conversation) -> HTTP200 text/event-stream -> thinking/reasoning/tool/final -> terminal`.

Terminal metrics:

- frameCount `132`, terminal `true`;
- exact reasoning-end `1`, fallback false;
- Native reasoning `14 deltas / 295 chars`;
- Native final answer `71 deltas / 2827 chars`;
- Native total `85 deltas / 3122 chars`;
- thinking preambles `2 / 13 chars`;
- reasoning-active signals `2`;
- service/native reasoning segment breaks `1/1`;
- invocation identities `10`, results `10`;
- parent present/matched/unmatched/missing `10/10/0/0`;
- Native tool presentations/completion updates `10/10`;
- Native detail-available rows `9`.

User directly reported no apparent reasoning/final truncation. Completed tool rows expanded/collapsed; `工具输入` and `工具输出` appeared as independent second-level disclosures; decoded output no longer showed b64's second-layer JSON escape wall. Remaining child spacing and legal JSON slash escaping are non-blocking polish and do not justify another diagnostic Candidate.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b65-runtime.md`.

Classification: **b65 focused Runtime pass. Probe-level Send/reasoning/final/tool lifecycle evidence accepted for the tested primary account/device scope. Stable/Frozen No.**

## Production architecture decision — Option B accepted

The user explicitly selected Option B after reviewing the prior TD-024/TD-025 prohibition. The production contract is now:

1. Native composer and Native conversation UI are the user-facing product surface.
2. One process-resident official ChatGPT Web execution surface uses the existing default persistent `WKWebsiteDataStore` and is allowed to be covered/not user-visible while it performs the official browser challenge and protected Send flow.
3. Native code may drive only the already-evidenced official composer/Send path; it must not synthesize/replay Sentinel/PoW/Turnstile/challenge values.
4. The covered Web execution surface is a **transport/challenge executor only**. It is not a conversation/message/response repository and must not become a second production state owner.
5. `ConversationRepository` remains the sole production owner for authoritative conversation/resident/response lifecycle state.
6. SSE events consumed from the one protected Send are committed through the Repository-owned response lifecycle; no second Send may be created merely to obtain a stream.
7. Sync/Reload remain explicit reconciliation/recovery operations and never resend/regenerate.
8. Account/auth authority remains `AuthSessionStore`; persistent auth-secret authority remains the default persistent `WKWebsiteDataStore`.
9. When official Web rules change, update the adapter from fresh evidence rather than adding speculative fallback/retry/alternate selectors.

This decision supersedes only the prior production prohibition on a covered/hidden official-Web Send executor. It does **not** revive full-Web conversation rendering, b44 Native->full-Web->Native UX, challenge replay, or Web ownership of conversation state.

## Reusable Web Rule Lab — required maintenance capability

A development-only Web Rule Lab is now part of this Work and should live inside the normal app, reachable from Settings.

Requirements:

- use the same default persistent `WKWebsiteDataStore` as login/production Web execution;
- visibly present a normal `WKWebView` so the user can navigate/login/inspect the current ChatGPT page;
- provide a temporary editable JavaScript input area plus explicit `执行` action;
- execute only code the user deliberately pastes/runs in the Lab;
- show the returned value in a temporary result area and allow copying/sharing it;
- do not persist probe JS or result bodies in `DiagnosticsLogger`, `UserDefaults`, files or another database;
- diagnostics may log only safe lifecycle facts such as page-load category, script executed/succeeded/failed and result type/length;
- do not log Cookie/Authorization/challenge values, raw prompt/answer/tool bodies or raw service IDs;
- the Lab is not a production Send owner and does not auto-run scripts on launch;
- future AI-assisted rule updates may use a short one-off JS probe supplied in chat, run by the user in this Lab, then use the returned evidence to update the versioned production adapter.

Durable adapter rules and update procedure will be centralized in `docs/project/WEB_SEND_ADAPTER.md` and linked from `START_HERE.md`, `SEND_STREAM_PREFLIGHT.md`, `PROJECT_SPECIFIC_RULES.md` and technical decisions.

## Accepted Web/protocol evidence to preserve

The b42-b65 evidence establishes, for the tested primary account/iPhone/iOS17 scope:

- browser challenge output is required for successful ChatGPT-account protected Send; pure-native/transient-auth Send remains blocked;
- the official page can perform the protected `/backend-api/f/conversation` Send and expose HTTP200 SSE;
- accepted diagnostic composer authority is `#prompt-textarea` or explicit `[contenteditable="true"][role="textbox"]`; generic textarea is rejected;
- compact SSE assistant-text behavior includes exact top-level `o/p/v`, contextual value continuation and the b51 `title_generation` continuation rule;
- exact service-marked thinking preambles are user-visible reasoning; `assistant:thoughts` remains non-presentational;
- exact `reasoning_ended` is the accepted reasoning->final phase marker;
- event-driven `正在思考` / reasoning / final ordering is accepted;
- exact invocation->result association is response-local exact `parent_id` only; no count/order/adjacency pairing;
- GitHub connector visible input/output mapping is authorized only for the evidenced exact-parent GitHub shape;
- unknown/new structural events stay observable and never trigger guessed state transitions;
- no retry/timer/watchdog/polling/fallback was required for the accepted path.

## Shortest production completion order

1. **Core docs + Web Rule Lab foundation** — record the superseding architecture decision and add the reusable Lab without emitting an identity-invalid intermediate Artifact.
2. **Existing-conversation production Send/stream slice** — add Repository-owned response lifecycle and Native composer; covered official Web executes exactly one protected Send; Native detail receives incremental Repository-owned updates.
3. **New-chat first Send** — use pending->authoritative handoff only if current server identity timing requires it; never fabricate server IDs.
4. **Stop** — acquire/verify exact server Stop evidence, then implement one response-scoped Stop; local Web/URL task cancellation alone is not proof of server Stop.
5. **A/B active-response + follow-tail** — hidden A remains owned/active while B visible; deliberate upward reading exits follow-tail; hidden growth never mutates B viewport.
6. **Sync/Reload/b38 regression** — no resend/regenerate; round count/time/Copy/deterministic geometry/quick navigation remain intact.
7. **Final daily-chat Runtime matrix + target-main sync** — only then decide Stable/merge. Background notification/true-background remain subsequent Works.

## Batch recovery point — architecture/docs/Web-Lab -> first production Candidate

Baseline before this batch:

- formal branch head: docs-only b65 handoff/architecture-gate lineage ending at `8e740f407350ee27f2094a8cbcd64e618d1e3ef1` before this checkpoint write;
- exact product/config authority remains b65 source `44138db766d00e62cfda7f20182f6d20f1ec3352` until a new coherent Candidate is emitted;
- PR #29 remains open / mergeable / unmerged;
- `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c`.

Planned non-atomic batches:

A. **Docs authority batch** — create `WEB_SEND_ADAPTER.md`; update technical decisions / project-specific rules / preflight / START_HERE and current state docs to make Option B the current authority. Docs-only commits may move the formal branch safely.

B. **Detached product batch** — implement Web Rule Lab and the smallest existing-chat production Send/stream slice using Git blobs/tree/commit off the formal branch. Do not place new product behavior under b65 identity on the formal branch.

C. **Candidate identity batch** — when the product slice is coherent, allocate b66 (or the next still-free identity), align Swift/Xcode/workflow identity in the same detached tree, compare-audit the exact delta, then fast-forward the formal branch once.

D. **Validation batch** — Push/PR CI -> Artifact -> independent package identity -> Runtime handoff -> durable docs/PR synchronization.

Writes already confirmed complete:

- b65 Runtime evidence file exists;
- checkpoint now records Option B and this recovery plan.

Writes still pending:

- authoritative adapter/TD/preflight/startup docs;
- Web Rule Lab product code;
- production existing-chat response-owner slice;
- next Candidate identity/CI/Artifact.

Do not touch/reuse:

- b39-b65 emitted Candidate identities;
- b38 Stable message geometry/round navigation contracts except where explicitly integrated and regression-tested;
- `AuthSessionStore` or persistent auth storage ownership without new evidence;
- full-Web conversation rendering as daily-chat UI.

## Next exact action

Complete docs authority batch A, then inspect/reuse the current Web probe engine and production Repository/UI call sites to implement Web Rule Lab plus the smallest existing-chat production Send/stream slice in detached product state. Do not stop for routine intermediate milestones; stop only at a real Runtime/human gate or evidence/architecture conflict.