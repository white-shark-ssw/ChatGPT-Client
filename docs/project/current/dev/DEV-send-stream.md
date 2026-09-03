# DEV-send-stream

## Status

**Active — fresh-root visible-Web `/c/{project-conversation}` control is Runtime Positive: with transient activation false, official Web canonicalized to exact `/g/{scope}/c/{conversation}` and started page-owned continuation. Scoped-route identity alone no longer explains b88. The follow-up Web Rule Lab `navigator.userActivation` read is not causal evidence because executing the probe itself can create/retain user activation and the page had already timed out. Next candidate is a diagnostics-focused b89 single-variable A/B on the remaining covered-WKWebView interactivity differential. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Verified pre-b89 product head: `39d90dc7ae8a6bc10f15f665ef2c3f438643ab9b`
- Recovery-point commit: `a1c4b579e3042c61fcfe21a332bdf90456c44541`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)` permanently reserved
- b89 Candidate / Build allocated: `DEV-send-stream-0.1.0-b89` / `0.1.0 (89)`
- Stable/Frozen Send: No

## Latest Runtime result

The fresh-root visible-Web control remains decisive:

- `phase=unscoped_full_navigation_started`;
- `activationAtNavigation=false`;
- final route exact `/g/{scope}/c/{conversation}`;
- page visible, focused, complete;
- Resource Timing not saturated;
- page-owned `stream_status=1`, `plural_snapshot=1`, `resume=0`;
- canonicalization and continuation both observed.

Therefore Native does not need a guessed project scope merely to make the tested official page continue.

The later manual Web Rule Lab read returned `isActive=true`, `hasBeenActive=true`, but this is **measurement-contaminated / non-decisive** because Web Rule Lab requires a user-triggered Execute action and sticky activation cannot be cleared afterward; page timeout additionally prevents treating that late read as the state when continuation began. Do not repeat the same probe.

## b89 exact A/B intent

Keep b88 behavior unchanged except for one native behavior variable:

- change covered `WKWebView.isUserInteractionEnabled` from `false` to `true`;
- keep the covered WebView behind Native siblings, no full-Web daily-chat UI;
- retain b88 one-shot focus activation after manual Sync rearm;
- add privacy-safe automatic page-activation diagnostics for `navigator.userActivation.isActive` / `hasBeenActive` only, so no Web Rule Lab Execute action is needed to measure covered state;
- do not change route construction, continuation protocol, Send behavior, polling/cadence, response ownership or Repository state.

Acceptance gate: on a deliberately long remote response, one explicit Sync/rearm must establish the external generation; after covered load/focus, observe whether official page-owned `stream_status` / `/resume` / snapshot continuation begins while the remote generation remains active. Artifact/CI success is not Runtime proof.

## Next exact action

Use one temporary guarded GitHub Actions patch workflow because the available repository write API can only replace the very large `RootViewController.swift` as a whole. The temporary workflow must apply only exact-count string replacements, run `git diff --check` plus the existing Xcode Simulator compile gate, delete itself before committing, and push the resulting product/version/workflow commit to this same feature branch. Then verify the actual commit diff before any CI/package claim.

After the guarded product commit is verified, run normal Push/PR CI, obtain one canonical b89 Artifact/IPA, independently verify package version/build/candidate/source identity, then hand b89 to the user for the real-device A/B. No route/gizmo fix, Native `stream_status`/`resume`, guessed offset, polling, timer/retry/watchdog, WebSocket-body authority, duplicate Send or second response store.

## Batch recovery state

**Recovery point active for b89.**

Baseline before product writes:

- branch `dev/send-stream-20260829`;
- PR #29 open / mergeable / unmerged;
- actual main `94f0c5777dad262cd1fb22be49082dbd92c962f2`;
- product head before recovery docs `39d90dc7ae8a6bc10f15f665ef2c3f438643ab9b`;
- recovery-point commit `a1c4b579e3042c61fcfe21a332bdf90456c44541`;
- b88 identities untouched and permanently reserved;
- b89 allocated as `0.1.0 (89)` / `DEV-send-stream-0.1.0-b89`.

Planned coherent batches:

1. create temporary `.github/workflows/b89-apply.yml` only as a deterministic repository-edit transport;
2. that workflow must assert and apply exactly: covered interactivity `false -> true`; automatic page user-activation diagnostic fields; project Build `88 -> 89` and Candidate `b88 -> b89`; normal `ios-foundation.yml` candidate/name/artifact identity `b88 -> b89`; then `git diff --check` + Simulator compile; finally remove itself and commit/push the real b89 changes;
3. verify actual branch head/diff and confirm the temporary workflow is absent before depending on the product commit;
4. verify normal Push/PR CI and produce/inspect one canonical b89 Artifact;
5. update BUILD_TEST_INDEX / MODULE_STATUS / WEB_SEND_ADAPTER / checkpoint and PR metadata with exact Code/CI/Artifact evidence.

Confirmed complete: recovery point and edit-transport plan.
Pending: temporary guarded patch workflow, real product/version/workflow commit, verification, CI, Artifact, durable doc sync.
Do not touch b88 product/Artifact/IPA identities, unrelated modules or another work checkpoint.

## Preserved boundaries

Official page owns continuation; `ConversationRepository` owns Native response/content. No Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or second response store.

## Session round counter

This user turn is **round 54**.
