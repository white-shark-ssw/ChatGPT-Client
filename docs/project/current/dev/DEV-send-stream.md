# DEV-send-stream

## Status

**Active — b89 interactivity A/B is fully packaged and ready for Human Runtime. Fresh-root visible-Web `/c/{project-conversation}` control remains Runtime Positive, so scoped-route identity alone does not explain b88. b89 changes only covered `WKWebView` interactivity plus privacy-safe automatic user-activation diagnostics while retaining b88 focus/rearm behavior. Code, guarded Static/Simulator, Push CI, PR CI, canonical Push Artifact and package identity are verified; real-device continuation causality remains Pending. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged; title `DEV-send-stream: b89 interactivity A/B packaged — real-device gate`
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Verified pre-b89 product head: `39d90dc7ae8a6bc10f15f665ef2c3f438643ab9b`
- Original b89 recovery-point commit: `a1c4b579e3042c61fcfe21a332bdf90456c44541`
- Exact b89 product commit: `f39bc9387575028d431b85409780a2f3670b3259`
- Exact b89 product/config package source: `fe45aeadf7ae03bf09aff66a8a05aa2542959676`
- Durable b89 package-doc commit before checkpoint close: `94e5708f97d2fc22f9f1951abb5feae53c06fcd1`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)` permanently reserved
- b89 Candidate / Build: `DEV-send-stream-0.1.0-b89` / `0.1.0 (89)` permanently reserved
- Canonical b89 Artifact: `9881665748`
- Canonical Artifact ZIP digest: `sha256:2e383a6328f801dd754d6858c3b9a8b71be5d5765a9a612d497b18c91b73988f`
- Canonical IPA: `ChatGPTClient-0.1.0-b89-dev-send-stream.ipa`
- Canonical IPA SHA-256: `c8ad5dcebbfde2131d3fc73c0309a47745f71527ad38b44c5fe3c5fbffe21a55`
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

## b89 exact A/B implementation

Keep b88 behavior unchanged except for one native behavior variable:

- covered `WKWebView.isUserInteractionEnabled` is `true` instead of `false`;
- covered WebView remains behind Native siblings; no full-Web daily-chat UI;
- b88 one-shot first-responder focus activation after manual Sync rearm remains unchanged;
- existing page-activation diagnostics now automatically record privacy-safe `navigator.userActivation` availability / `isActive` / `hasBeenActive` booleans;
- route construction, continuation protocol, Send behavior, polling/cadence, response ownership and Repository state are unchanged.

Acceptance gate: on a deliberately long remote response, one explicit Sync/rearm must establish the external generation; after covered load/focus, observe whether official page-owned `stream_status` / `/resume` / snapshot continuation begins while the remote generation remains active. Artifact/CI success is not Runtime proof.

## b89 Code / staging evidence

Exact product commit `f39bc9387575028d431b85409780a2f3670b3259` is `b89: test covered Web interactivity`.

Verified commit scope:

- `ChatGPTClient/RootViewController.swift`: exactly covered interactivity `false -> true` plus automatic page user-activation booleans;
- `ChatGPTClient.xcodeproj/project.pbxproj`: Build `88 -> 89`, Candidate `b88 -> b89` in both target configurations;
- temporary `.github/workflows/b89-apply.yml` removed in the same commit;
- no route/status/resume/snapshot/Send/Repository behavior changed.

Guarded staging:

- run `33722176080`: exact product diff + Simulator build succeeded; bookkeeping failed before commit because staged deletion was checked with an unstaged-only file list;
- run `33722473430`: exact product diff + Simulator build succeeded; bookkeeping failed before commit because an already-removed workflow path was explicitly passed to `git add`;
- final run `33722656297 / 100544857329` from staging source `55648f61d97b1997c2f0058b10f9d274c1078106` succeeded through exact patch, `git diff --check`, Xcode 16.4 Simulator compile, temporary workflow self-deletion, commit and push;
- failed staging runs did not commit/push partial product files.

## b89 CI / Artifact / package evidence

Permanent workflow identity commit makes exact package source `fe45aeadf7ae03bf09aff66a8a05aa2542959676` with workflow `iOS Send Covered Interactivity A-B b89` and Artifact name `ChatGPTClient-DEV-send-stream-0.1.0-b89`.

Validation:

- Push CI: `33725042383 / 100552047445` — success on exact feature head `fe45aeadf7ae03bf09aff66a8a05aa2542959676`;
- PR CI: `33725044367 / 100552051932` — success against unchanged `main` `94f0c5777dad262cd1fb22be49082dbd92c962f2`;
- canonical Runtime Artifact is **Push** Artifact `9881665748`, not a PR synthetic-merge package;
- Artifact ZIP digest `sha256:2e383a6328f801dd754d6858c3b9a8b71be5d5765a9a612d497b18c91b73988f` independently matched the downloaded ZIP;
- contained IPA `ChatGPTClient-0.1.0-b89-dev-send-stream.ipa`;
- sidecar and independent recomputation both give IPA `sha256:c8ad5dcebbfde2131d3fc73c0309a47745f71527ad38b44c5fe3c5fbffe21a55`;
- unpacked `Info.plist`: `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=89`, `DiagnosticsCandidate=DEV-send-stream-0.1.0-b89`, `DiagnosticsSourceCommit=fe45aeadf7ae`, `MinimumOSVersion=14.0`, `UIDeviceFamily=[1,2]`, platform `iPhoneOS`;
- unpacked executable: Mach-O 64-bit arm64.

Evidence ladder: **Code written / guarded Static+Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Runtime pending / Stable-Frozen No.**

Any later docs-only commit may advance PR head; that does not change the canonical b89 Runtime package source above. Product/config changes after `fe45aead...` would require a new identity decision before claiming the same package covers them.

## Durable documentation / PR sync

- guarded docs-sync run `33725756198` succeeded;
- docs commit `94e5708f97d2fc22f9f1951abb5feae53c06fcd1` records b89 in `BUILD_TEST_INDEX.md`, `MODULE_STATUS.md`, `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, `PROJECT_SPECIFIC_RULES.md`, `TECHNICAL_DECISIONS.md` and `WEB_SEND_ADAPTER.md`;
- temporary `.github/workflows/b89-docsync.yml` self-deleted in that commit;
- PR #29 title/body now record exact b89 package identity, evidence ladder and Human Runtime gate;
- docs-only head advancement does not alter the canonical Runtime package source `fe45aead...`.

## Human Runtime gate — next exact action

Install exact b89 IPA and run one clean production A/B:

1. on another official client, start a deliberately long response with multiple reasoning/tool steps remaining;
2. in ChatGPTClient b89, enter/select the same target conversation while that remote generation is clearly still early/mid-flight;
3. press `同步最新消息` exactly once to establish/rearm the external generation;
4. keep ChatGPTClient foregrounded for at least 30–60 seconds without another Sync;
5. independently confirm the remote official client continues generating after b89 covered load/focus/interactivity activation;
6. export diagnostics **before** doing a second manual Sync if possible.

Decisive fields/events:

- `coveredExecutor.pageActivation` after rearm, especially `hasFocus`, `userActivationAvailable`, `userActivationIsActive`, `userActivationHasBeenActive`;
- `coveredExecutor.focusActivationResult`;
- any `coveredExecutor.externalStreamStatusRequest/Response`;
- any `coveredExecutor.externalResumeRequest/Response`;
- any `coveredExecutor.externalStreamingObserved` / page-owned snapshot;
- authoritative Detail/live-response progression and whether final materializes automatically.

Decision:

- interactivity + focus followed by genuine page-owned continuation while remote generation remains active -> b89 Runtime Positive; interactivity/user-activation differential is causal enough to retain and then test stability;
- interactivity enabled, covered state established, remote generation demonstrably remains active, but still zero page-owned continuation -> reject interactivity as sufficient; return to the remaining genuine official SPA/router conversation-entry differential;
- if the sample again reaches terminal before covered activation, classify Inconclusive and reuse exact b89; do not allocate b90 from an ambiguous run.

No route/gizmo fix, Native `stream_status`/`resume`, guessed offset, polling, timer/retry/watchdog, WebSocket-body authority, duplicate Send or second response store.

## Batch recovery state

**Closed for b89 product/package/docs preparation. The next gate is human-only real-device Runtime.**

Verified immutable Runtime package identity:

- product commit `f39bc9387575028d431b85409780a2f3670b3259`;
- product/config package source `fe45aeadf7ae03bf09aff66a8a05aa2542959676`;
- Push/PR CI both success;
- canonical Push Artifact `9881665748`;
- IPA SHA `c8ad5dcebbfde2131d3fc73c0309a47745f71527ad38b44c5fe3c5fbffe21a55`;
- b88 identity untouched; b89 identity emitted/reserved.

All repository-write batches for this candidate are complete: product patch, temporary workflow cleanup, permanent workflow identity, exact identity guard, Push/PR CI, canonical Artifact, independent package verification, durable docs and PR metadata. Do not modify product/config or allocate b90 before b89 Runtime evidence.

Next exact action: install exact b89, run the clean early/mid-generation A/B above, and return diagnostics. No repository write is required before that human gate.

## Preserved boundaries

Official page owns continuation; `ConversationRepository` owns Native response/content. No Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or second response store.

## Session round counter

This user turn is **round 55**.
