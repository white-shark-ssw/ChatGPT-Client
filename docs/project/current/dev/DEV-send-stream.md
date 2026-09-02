# DEV-send-stream

## Status

**Active — fresh-root visible-Web `/c/{project-conversation}` control is Runtime Positive: with transient activation false, official Web canonicalized to exact `/g/{scope}/c/{conversation}` and started page-owned continuation. Scoped-route identity alone no longer explains b88. The follow-up Web Rule Lab `navigator.userActivation` read is not causal evidence because executing the probe itself can create/retain user activation and the page had already timed out. Next candidate is a diagnostics-focused b89 single-variable A/B on the remaining covered-WKWebView interactivity differential. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Verified pre-b89 PR head: `39d90dc7ae8a6bc10f15f665ef2c3f438643ab9b`
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

Complete b89 product + version changes, run exact source/static/CI validation, produce one canonical b89 IPA, then hand it to the user for the real-device A/B. No route/gizmo fix, Native `stream_status`/`resume`, guessed offset, polling, timer/retry/watchdog, WebSocket-body authority, duplicate Send or second response store.

## Batch recovery state

**Recovery point opened for b89.**

Baseline before writes:

- branch `dev/send-stream-20260829`;
- PR #29 open / mergeable / unmerged;
- head `39d90dc7ae8a6bc10f15f665ef2c3f438643ab9b`;
- b88 identities untouched and permanently reserved;
- b89 newly allocated as `0.1.0 (89)` / `DEV-send-stream-0.1.0-b89`.

Planned coherent batches:

1. product source: `ChatGPTClient/RootViewController.swift` — interactivity single-variable A/B + user-activation diagnostics;
2. version identity: `ChatGPTClient.xcodeproj/project.pbxproj` — build 89 / Candidate b89;
3. verify exact branch head/diff, then CI/package identity;
4. after Artifact identity is known, update BUILD_TEST_INDEX / MODULE_STATUS / WEB_SEND_ADAPTER / checkpoint and PR metadata.

Confirmed complete: recovery point only.
Pending: all product/version/CI/Artifact/doc-sync batches above.
Do not touch b88 product/Artifact/IPA identities, unrelated modules or other work checkpoints.

## Preserved boundaries

Official page owns continuation; `ConversationRepository` owns Native response/content. No Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or second response store.

## Session round counter

This user turn is **round 53**.
