# Project State

_Last updated: 2026-08-31 through accepted b67 production transport Runtime, exact b71 Runtime rejection evidence, and exact b72 Code/scope/Simulator/Push+PR CI/Artifact/package verification. Phase 9 `DEV-send-stream` remains Active at the b72 human Runtime gate. Stable/Frozen Send remains No._

## Current accepted merged baseline

Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21, list-cache b23 and **Phase 8 b38** remain accepted merged baselines for their recorded scopes. Exact b38 tested source is `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`. Stable does not mean Frozen.

## Current Work / source identity

`DEV-send-stream` is Active on `dev/send-stream-20260829`; PR #29 remains open / mergeable / unmerged and evidence-only. Current actual `main` last verified this cycle is `d323b9eed2dda75b9986fc06e14014d3e9b365fb`; final target-main synchronization is still required before merge.

Latest exact product Candidate is **`DEV-send-stream-0.1.0-b72` / `0.1.0 (72)`**:

- exact product/config source `d20536db37a028556c8032e7c74912805ade785c`; code commit `451fa0cb58bbbc681a97d3156bada50357a6067e` with direct parent `2aaee7f6fa143c1c3426ca89d2d52b42949daf86`;
- isolated assembly exact four-file scope audit, `git diff --check` and Xcode 16.4 iOS Simulator compile passed;
- Push `33403473989 / 99525205970` and PR `33403478927 / 99525223287` — success;
- Artifact `9762189417`; ZIP `sha256:5107cedc43b3e5a096da60db9acc2f0705c30bb81be8134f1373dba6f929c1b9`;
- IPA `sha256:ff9d37022a310cab3eea0bb3c298e3d3ec8b0d3057f7256da4f0543dab18b53c`;
- independently unpacked package `0.1.0 (72)` / Candidate b72 / source `d20536db37a0` / minimum iOS14 / arm64.

b72 retains b67 protected-Send/SSE ownership and b69 ordered response chronology, while implementing the latest explicit b71 Runtime corrections: first-level inline whole-timeline reasoning disclosure, tools-only/input-only secondary tool list, centralized service-backed minute-level reasoning duration formatting, bounded tool identity presentation, and per-conversation covered executor ownership so unrelated conversations are not globally serialized. No retry/replay/poll/timer/watchdog/fallback or second state owner was added. Evidence ladder: **Code / exact scope / Simulator compile / Push+PR CI / Artifact / package verified / Runtime pending / Stable-Frozen No.** b39-b72 are permanently reserved.

## b65 accepted probe predecessor

Exact b65 focused iPhone/iOS17 Runtime passed the verified-composer protected-Send / reasoning-final / exact-parent GitHub tool-detail scope: real Send -> HTTP200 SSE -> terminal, reasoning `14/295`, final `71/2827`, exact-parent matches `10/10`, tool presentation/completion `10/10`, and readable nested `工具输入` / `工具输出`. Remaining spacing/slash escaping was non-blocking.

## Exact b66 production Runtime — failed bridge, Send reached service

b66 was the first TD-029 production existing-conversation slice. Exact identity:

- Candidate `DEV-send-stream-0.1.0-b66`, source `9ce228ad880eaf81fc23ba26fe14f4d2bf524acb`, tree `31ef29457273a44dd202a63a96560563154e8823`;
- Push `33337771534 / 99327694040`, PR `33337774136 / 99327701256` — both success;
- Push Artifact `9739572172`;
- ZIP `sha256:6c6d8e165ed070e88a27abafc57973dc847937826e40c552bf9f0d29bb91bb45`;
- IPA `sha256:7f62e875bbd75d54e2d7bf76340f277d02f03e695d464d818fa5cab664c630e9`.

Exact iPhone/iOS17 export `ChatGPTClient-Diagnostics-20260830-220515.json` matched build66/source. Two generations reproduced:

`composer_ready x2 -> submit_result=submitted x2 -> one send_observed -> send_transport_error`

No `coveredExecutor.sendResponse` occurred and Native response characters stayed zero. The user independently verified that the official ChatGPT app already contained the assistant reply, so the protected Send reached the service; Native lost the same-response transport before receiving the HTTP Response object. This is **not** an SSE parser/Web-rule failure.

Source correlation isolated a production Swift->JS duplicate-submit race: b66 kept `pendingSend` until later `send_observed`, while multiple ready callbacks could schedule asynchronous `evaluateJavaScript(submit(...))` calls before page-local `activeSend` became true. Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b66-runtime.md`.

## b67 minimal correction

b67 changes only the executor operation gate:

1. `CoveredWebSendExecutor.isBusy` is owned by existing `activeEvents != nil`, spanning request through terminal/failure.
2. `pendingSend` is consumed immediately before issuing the one JS `submit(...)` evaluation.
3. Later duplicate composer-ready callbacks cannot schedule the same pending operation again.
4. Clearing `pendingSend` does not open a second Send window because `activeEvents` remains active.

Exact Root delta is only `+2/-1`; Xcode/workflow changes only allocate b67 identity. No selector, Web rule, protected route, SSE grammar, Repository ownership, Web Rule Lab, retry, resend, polling, timer, watchdog, fallback or compatibility shim changed.

## Durable Phase 9 architecture/security boundary

- Exact b42 proves successful ChatGPT-account protected Send requires browser anti-abuse challenge output. Pure-native/transient-auth account Send remains blocked.
- Separately billed API-product route remains rejected; primary-account Sub2API/Codex-subscription route remains blocked by account-safety policy.
- **TD-029 remains the production Send decision.** Native history/composer/reasoning/tool/final UI is the product surface; one process-resident covered official Web surface may perform browser challenge + exactly one page-owned protected Send.
- Covered Web is transport/challenge execution only, never conversation/message/response/list/draft authority.
- `ConversationRepository` remains sole native conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` remains sole auth/account authority; `WKWebsiteDataStore.default()` remains sole persistent auth-secret authority. b70 treats exact probe HTTP403 as temporary failure that preserves the last verified identity, while list/detail 401/403 discards stale copied transient transport and never auto-replays the failed operation.
- Full existing-conversation mobile-Web rendering remains rejected by TD-025/TD-028.
- No challenge solving/replay, no second credential store, no duplicate Send to obtain a stream, no automatic Sync/poll loop.
- Sync/Reload never resend/regenerate.

## Web Send maintenance capability

`docs/project/WEB_SEND_ADAPTER.md` remains the durable authority for current evidenced official composer/protected-Send/SSE/reasoning/tool rules and the Web Rule Lab maintenance loop. b66 evidence does **not** change that adapter contract: the failure was local production orchestration, not an official Web rule change.

The in-app Web Rule Lab is now implemented in the current production branch: visible `WKWebView`, `.default()` store, explicit user execution, temporary script/result only, copy/share allowed, no persisted body/log body, never production response owner.

## Current implementation boundary / shortest remaining Phase 9 sequence

Current source contains the Repository-owned existing-conversation production bridge and Web Rule Lab. b67 transport Runtime is accepted; exact b72 reasoning/tool hierarchy + simultaneous-generation Runtime is the immediate gate.

After that gate, the shortest remaining sequence is:

1. accept/fix existing-conversation production Send/stream;
2. new-chat first Send and pending->authoritative handoff only if actual timing requires it;
3. exact server Stop evidence and one response-scoped Stop implementation;
4. A/B hidden-response ownership + follow-tail/history intent;
5. Sync/Reload active-response safety + b38 geometry/round/time/Copy regression;
6. final daily-chat Runtime matrix, target-main synchronization and Stable/merge decision.

Final Composer hierarchy/dynamic input/attachment staging belongs future serialized `DEV-composer-parity`; current Work keeps only the validation trigger. Background completion and attachments remain subsequent Works after accepted text Send/Stream ownership.

## Current exact Runtime gate

Install exact b72 Artifact `9762189417` / IPA SHA `ff9d3702...8b53c` on the primary iPhone/iOS17 device. Verify Candidate/source marker `d20536db37a0`, clear diagnostics, then confirm: the main `思考了 <duration>` control expands/collapses the entire chronological reasoning+tool timeline inline; duration stays seconds below 60 and accumulated minutes thereafter without hours; tapping concrete tool rows opens one ordered tools-only sheet with direct authorized input and no reasoning/output section; unknown/non-GitHub tools do not masquerade as GitHub; A can continue generating while B independently sends/generates with one active response per conversation; hidden A survives navigation; b67 one-Send transport, hidden-thought exclusion and b38 geometry do not regress. Export diagnostics after terminal(s).

## Remaining Unknown / Unverified

Exact b70 daily-chat parity/auth-lifecycle Runtime, new-chat authoritative identity timing, exact server Stop mechanism, cross-conversation simultaneous server generation, connector-detail schemas beyond the evidenced GitHub mapping, Native first/exclusive resume, 5/15-minute background behavior, WebContent termination recovery, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.