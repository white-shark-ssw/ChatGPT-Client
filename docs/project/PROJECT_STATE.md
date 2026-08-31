# Project State

_Last updated: 2026-08-31 through accepted b67 production transport Runtime, exact b70 presentation Runtime rejection, and exact b71 Code/scope/Simulator compile/Push+PR CI/Artifact/package verification. Phase 9 `DEV-send-stream` remains Active at the b71 human Runtime gate. Stable/Frozen Send remains No._

## Current accepted merged baseline

Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21, list-cache b23 and **Phase 8 b38** remain accepted merged baselines for their recorded scopes. Exact b38 tested source is `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`. Stable does not mean Frozen.

## Current Work / source identity

`DEV-send-stream` is Active on `dev/send-stream-20260829`; PR #29 remains open / mergeable / unmerged and evidence-only. Current actual `main` last verified this cycle is `d323b9eed2dda75b9986fc06e14014d3e9b365fb`; final target-main synchronization is still required before merge.

Latest exact product Candidate is **`DEV-send-stream-0.1.0-b71` / `0.1.0 (71)`**:

- exact product/config source `af8d4a4b291c05fb63a50cee0261c06d7ce474d3`; clean product commit `38a12f52f1a5034c43a446f737b0da210a5a1a4f`; direct clean checkpoint parent `5e9c0a8cfa00118a4facca640e8ee739ce480c1a`;
- Simulator compile `33386550230 / 99470358015` passed after exact four-file scope audit; the containing tooling run failed only at unauthorized workflow push;
- clean extract `33388165867 / 99475407591` success;
- Push `33388396118 / 99476130099` and PR `33388399484 / 99476140778` — success;
- Artifact `9756491305`; ZIP `sha256:74b554c98333e365b03073a39b0286f966b98c94ec2a695d62b81cb4f8f7bda0`;
- IPA `sha256:a9322dba9351842ac2d2374a1f8792129fe64750a1c79da514e2444bb785fd65`;
- independently unpacked package `0.1.0 (71)` / Candidate b71 / source `af8d4a4b291c` / minimum iOS14 / `[1,2]` / arm64.

b71 is presentation/performance-only: it preserves b67 protected-Send/SSE ownership and b69 ordered timeline, carries exact service `finished_duration_sec`, replaces b70 inline reasoning/tool disclosure with compact conversation summary + presentation-only reasoning sheet, removes historical disclosure-triggered full-table geometry rebuilds, uses one outer sheet scroller for intrinsic tool detail, and changes no protected route/selector/challenge/SSE ownership semantics. Exact b70 package remains valid/reserved but its supplied iPhone/iOS17 presentation Runtime is rejected. Evidence ladder: **Code / exact scope / Simulator compile / Push+PR CI / Artifact / package verified / Runtime pending / Stable-Frozen No.** b39-b71 are permanently reserved.

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

Current source contains the Repository-owned existing-conversation production bridge and Web Rule Lab. b67 transport Runtime is accepted; exact b70 daily-chat parity/auth-lifecycle Runtime is the immediate gate.

After that gate, the shortest remaining sequence is:

1. accept/fix existing-conversation production Send/stream;
2. new-chat first Send and pending->authoritative handoff only if actual timing requires it;
3. exact server Stop evidence and one response-scoped Stop implementation;
4. A/B hidden-response ownership + follow-tail/history intent;
5. Sync/Reload active-response safety + b38 geometry/round/time/Copy regression;
6. final daily-chat Runtime matrix, target-main synchronization and Stable/merge decision.

Final Composer hierarchy/dynamic input/attachment staging belongs future serialized `DEV-composer-parity`; current Work keeps only the validation trigger. Background completion and attachments remain subsequent Works after accepted text Send/Stream ownership.

## Current exact Runtime gate

Install exact b71 Artifact `9756491305` / IPA SHA `a9322dba9351842ac2d2374a1f8792129fe64750a1c79da514e2444bb785fd65` on the primary iPhone/iOS17 device. Verify Candidate/source marker, clear diagnostics, then compare the main conversation and `正在思考` sheet against the supplied official screenshots: compact service-duration summary or `思考过程`, bounded meaningful tool icons/rows, no empty generic completed placeholder, ~16pt assistant content alignment, compact divider/spacing, immediate sheet opening without full-table geometry rebuild, intrinsic input/output growth under one outer sheet scroller, correct duration/completion ordering, and no regressions to b67 one-Send transport, hidden-thought exclusion, active-response navigation or b38 deterministic geometry/quick navigation. Export diagnostics after terminal. b70 auth-403 recovery remains separately Unverified if this run does not exercise it.

## Remaining Unknown / Unverified

Exact b71 presentation/performance Runtime, b70 transient-auth recovery when not exercised, new-chat authoritative identity timing, exact server Stop mechanism, cross-conversation simultaneous server generation, connector-detail schemas beyond the evidenced GitHub mapping, Native first/exclusive resume, 5/15-minute background behavior, WebContent termination recovery, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.