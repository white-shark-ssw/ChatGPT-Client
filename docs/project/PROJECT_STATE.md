# Project State

_Last updated: 2026-08-30 through exact b61 Runtime classification and exact b62 Code / CI / Artifact / package verification. Phase 9 remains Active; b62 Runtime/manual is pending._

## Current accepted merged baseline

Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21, list-cache b23 and **Phase 8 b38** remain accepted merged baselines for their recorded scopes. Exact b38 tested source is `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`. Stable does not mean Frozen.

## Current Work / target

`DEV-send-stream` is Active on `dev/send-stream-20260829`; PR #29 remains evidence-only / unmerged. Final target-main synchronization is still required before any future merge.

Current exact test Candidate is **`DEV-send-stream-0.1.0-b62` / `0.1.0 (62)`**, exact product/config source `e1b44f7ab6c47bd41de3ed9460ec0b77b7cc9f3f`, Artifact `9733577825`, IPA SHA `ac9f031fb43b91ac12f486b1f743f741b404faf133725bdc8abec059b68b87d8`. Code / Push CI / PR CI / Artifact / package identity passed; Runtime/manual pending.

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
- b61 Runtime passed the tested parent-paired tool-row lifecycle but exposed an independent Send-entry race: generic `textarea` could be reported ready/submitted without an official protected Send.
- b62 removes only that exact false-ready generic-textarea authority and otherwise preserves b61 behavior.

## Exact b61 Runtime — Partial

Exact b61 identity: Candidate `DEV-send-stream-0.1.0-b61`, source `2386872af03e0684eee8deca87f636dc265114ec`, Artifact `9732514781`, IPA SHA `6fff9fa7178d0915f74a08eadeeb8ad9cb7927416ca1c09c979b69df67a18e21`.

Two user-provided runs were intentionally classified separately:

- First run (`ChatGPTClient-Diagnostics-20260830-134827.json`): `new_or_other`, composer strategy `textarea`, `nativeSubmit`, `submitResult=submitted`, then no `sendObserved`, no `sendResponse`, no thinking and no stream metrics. User observed no response activity. **Runtime defect: false-ready / false-submitted Send entry.**
- Second run (`ChatGPTClient-Diagnostics-20260830-135112.json`) after force-quit/relaunch: HTTP200 SSE / terminal; reasoning `10/251`, final `68/2363`, preambles `2/11`, segment breaks `1/1`, reasoning-end 1, fallback false; invocation identities/results `14/14`; parent present/matched/unmatched/missing `14/14/0/0`; paired presentations and Native tool presentations/completion updates `14/14/14`. User observed complete reasoning opening and `调用中 -> 已完成` tool lifecycle. **Runtime pass for tested tool lifecycle/response presentation.**

Overall classification: **b61 Runtime Partial**. Detailed record: `docs/project/runtime-evidence/DEV-send-stream-b61-runtime.md`.

## Exact b62 Candidate / validation

- Candidate `DEV-send-stream-0.1.0-b62`, `0.1.0 (62)`.
- Exact product/config source `e1b44f7ab6c47bd41de3ed9460ec0b77b7cc9f3f`; tree `d3432dfe2e32cddcfac7a5a56d7880772dc6989d`.
- Push Run / Job `33316398081 / 99270535435` — success.
- PR Run / Job `33316399402 / 99270539763` — success.
- Artifact `9733577825`; ZIP `sha256:d53ddb88c5d2092294592416e10e5a0a752cb7afb0bbe0a39c2c137d021082d0`.
- IPA SHA `ac9f031fb43b91ac12f486b1f743f741b404faf133725bdc8abec059b68b87d8`.
- Package: Release / `0.1.0 (62)` / Candidate b62 / source `e1b44f7ab6c4` / iOS14 / `[1,2]` / arm64.
- b62 is permanently reserved after Artifact emission.

b62 behavior change is intentionally narrow: `findComposer()` no longer treats an arbitrary enabled textarea as the official composer. Only `#prompt-textarea` or explicit contenteditable role=textbox remains authoritative. No retry/timer/watchdog/polling/fallback was added. b61 parsing, thinking/reasoning/final presentation, parent pairing and bounded detail-shape diagnostics are unchanged.

Evidence ladder: **Code written / Push CI passed / PR CI passed / Artifact produced / package identity independently verified; Runtime/manual pending; Stable/Frozen No.**

## Next evidence gate

Run exact b62 on the primary iPhone/iOS17 target after a force-quit/cold launch. It is **not required** to reproduce b61's intermittent false-ready race. The required gate is:

- before an evidenced official composer exists, Send must remain unavailable/not-ready rather than accepting generic `textarea`;
- once Send is enabled and pressed, a successful normal turn must produce a real `sendObserved` protected-Send lifecycle and HTTP200 SSE when the service succeeds;
- thinking/reasoning/tool/final behavior must retain b61's accepted successful-path behavior, including tool rows advancing `调用中 -> 已完成` and no obvious text truncation;
- if any run again reports submitted with no `sendObserved`, export immediately: that would reject the current narrow fix even if another run passes.

One focused cold-launch tool-active run is sufficient for the primary gate; one additional cold launch is useful but optional. Do not demand indefinite attempts to reproduce a rare race.

## Remaining Unknown / Unverified

Accepted production incremental-response ownership, exact cross-tool user-visible detail schema, Native first/exclusive resume, existing-conversation pre-React history virtualization, full 5/15-minute background behavior, WebContent termination, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified where not explicitly tested. CI/Artifact success is never Runtime proof.
