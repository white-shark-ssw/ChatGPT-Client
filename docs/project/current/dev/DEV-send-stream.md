# DEV-send-stream

## Status

**Active — fresh-root visible-Web `/c/{project-conversation}` control is Runtime Positive: with transient activation false, official Web canonicalized to exact `/g/{scope}/c/{conversation}` and started page-owned continuation. Scoped-route identity alone no longer explains b88. The follow-up Web Rule Lab `navigator.userActivation` read is not causal evidence because executing the probe itself can create/retain user activation and the page had already timed out. b89 is now Code written + guarded Static/Simulator passed for the remaining covered-WKWebView interactivity differential; formal workflow identity / Push+PR CI / Artifact remain pending. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Verified pre-b89 product head: `39d90dc7ae8a6bc10f15f665ef2c3f438643ab9b`
- Original b89 recovery-point commit: `a1c4b579e3042c61fcfe21a332bdf90456c44541`
- Current verified b89 product head: `f39bc9387575028d431b85409780a2f3670b3259`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)` permanently reserved
- b89 Candidate / Build allocated: `DEV-send-stream-0.1.0-b89` / `0.1.0 (89)`
- b89 Artifact: **not emitted yet**
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

## b89 Code / staging evidence

Current verified branch head `f39bc9387575028d431b85409780a2f3670b3259` is commit `b89: test covered Web interactivity`.

Verified commit scope:

- `ChatGPTClient/RootViewController.swift`: exactly `isUserInteractionEnabled=false -> true` plus automatic page-activation `navigator.userActivation` booleans;
- `ChatGPTClient.xcodeproj/project.pbxproj`: Build `88 -> 89`, Candidate `b88 -> b89` in both target configurations;
- temporary `.github/workflows/b89-apply.yml` removed in the same commit;
- no route/status/resume/snapshot/Send/Repository behavior changed.

Guarded staging facts:

- run `33722176080`: exact product diff + Simulator build succeeded; bookkeeping failed before commit because the staged workflow deletion was checked with an unstaged-only file list;
- run `33722473430`: exact product diff + Simulator build succeeded; bookkeeping failed before commit because the already-removed workflow path was passed explicitly to `git add`;
- final corrected guarded run from staging commit `55648f61d97b1997c2f0058b10f9d274c1078106` used `git add -A` and produced current product head `f39bc9387575028d431b85409780a2f3670b3259`;
- prior failed runs did not commit/push partial product files;
- Xcode 16.4 Simulator gate emitted `** BUILD SUCCEEDED **` before the successful product commit.

Evidence level: **Code written + guarded static/Simulator passed. Formal Push/PR CI, Artifact, package identity, Runtime remain pending.**

## Next exact action

The temporary guarded workflow is gone, but the permanent `.github/workflows/ios-foundation.yml` still carries b88 header/name/upload-Artifact identity. This is the only deterministic missing write from the recorded b89 batch and no b89 Artifact has been emitted yet.

1. update only `.github/workflows/ios-foundation.yml` from b88 identity to b89 identity, with product-source comment bound to current verified product head `f39bc9387575028d431b85409780a2f3670b3259`;
2. verify actual feature head/diff and that Build89/Candidate b89 + workflow b89 identity agree;
3. let normal Push and PR CI run on the resulting exact product/config source;
4. select one canonical **feature-head / Push** b89 Artifact, independently verify ZIP/IPA checksum and built `Info.plist` version/build/Candidate/source marker, MinimumOSVersion and arm64;
5. update BUILD_TEST_INDEX / MODULE_STATUS / TECHNICAL_DECISIONS / WEB_SEND_ADAPTER / checkpoint and PR metadata with exact Code/CI/Artifact evidence;
6. hand exact b89 IPA to the user for the real-device interactivity A/B.

No route/gizmo fix, Native `stream_status`/`resume`, guessed offset, polling, timer/retry/watchdog, WebSocket-body authority, duplicate Send or second response store.

## Batch recovery state

**Recovery point active for b89.**

Current verified baseline:

- branch `dev/send-stream-20260829`;
- PR #29 open / mergeable / unmerged;
- actual main `94f0c5777dad262cd1fb22be49082dbd92c962f2`;
- current product head `f39bc9387575028d431b85409780a2f3670b3259`;
- b88 identities untouched and permanently reserved;
- b89 allocated as `0.1.0 (89)` / `DEV-send-stream-0.1.0-b89`;
- b89 Artifact not emitted.

Confirmed complete:

1. temporary guarded patch transport created and corrected deterministically after two post-build bookkeeping failures;
2. exact b89 product/version patch passed `git diff --check` + Xcode 16.4 Simulator build;
3. temporary patch workflow deleted itself in final real product commit;
4. actual product commit `f39bc9387575028d431b85409780a2f3670b3259` verified.

Pending coherent batches:

1. permanent `ios-foundation.yml` b89 identity update only;
2. exact head/diff/identity verification;
3. normal Push/PR CI;
4. canonical Push Artifact/package verification;
5. durable docs + PR metadata sync.

Next exact action: update only `.github/workflows/ios-foundation.yml`; do not replay product patch or temporary workflow. Do not touch b88 product/Artifact/IPA identities, unrelated modules or another work checkpoint.

## Preserved boundaries

Official page owns continuation; `ConversationRepository` owns Native response/content. No Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or second response store.

## Session round counter

This user turn is **round 55**.
