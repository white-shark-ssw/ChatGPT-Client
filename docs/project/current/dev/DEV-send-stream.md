# DEV-send-stream

## Status

**Active — b71 presentation/performance Candidate is now Code/scope/Simulator/Push+PR CI/Artifact/package verified and awaits exact iPhone/iOS17 Runtime. b67 transport remains accepted; b70 presentation Runtime remains rejected/reserved; Stable/Frozen Send remains No; PR #29 stays open/unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Formal branch head before this b70 Runtime checkpoint: `b936c8c328e58a5da6befebf6aec930e17effe06`
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Exact b70 product/config source: `fb83be9163838f78abfa47903e67f27b6f66ec52`
- Candidate: `DEV-send-stream-0.1.0-b70`
- Version / Build: `0.1.0 (70)`
- b70 Artifact: `9752289536`; IPA SHA `8084e2ace5926b7ee6a790f3eeb2445a2c4ce1fee67d8953300aca93a446a44a`
- b39-b70 permanently reserved; never reuse b70
- Repository/code search found no existing `DEV-send-stream-0.1.0-b71`; b71 is justified by the exact Runtime evidence below
- Stable/Frozen Send: No

## b71 formal source / CI / Artifact milestone — 2026-08-31

- Exact product/config source: `af8d4a4b291c05fb63a50cee0261c06d7ce474d3`; clean product commit `38a12f52f1a5034c43a446f737b0da210a5a1a4f`; direct clean checkpoint parent `5e9c0a8cfa00118a4facca640e8ee739ce480c1a`.
- Candidate: `DEV-send-stream-0.1.0-b71`; Version / Build: `0.1.0 (71)`.
- Tooling assembly compile evidence: Run `33386550230`, Job `99470358015`; four-file scope audit passed and Xcode 16.4 iOS Simulator ended `BUILD SUCCEEDED`. The run itself later failed only when its GitHub Actions token was denied permission to push a workflow file; this is tooling-output failure, not product compile failure.
- Clean product extraction: Run `33388165867`, Job `99475407591` — success; exact compiled patch reapplied and three product files emitted from the clean checkpoint; connector then changed only the formal workflow Candidate/Artifact identity.
- Detached checkpoint -> candidate audit: exactly four authorized files; `.github/workflows/ios-foundation.yml` `+2/-2`, Xcode project `+4/-4`, `ConversationFeature.swift` `+425/-171`, `RootViewController.swift` `+9/-5`.
- Push CI: `33388396118 / 99476130099` — success.
- PR CI: `33388399484 / 99476140778` — success.
- Push Artifact: `9756491305`, name `ChatGPTClient-DEV-send-stream-0.1.0-b71`, ZIP `sha256:74b554c98333e365b03073a39b0286f966b98c94ec2a695d62b81cb4f8f7bda0`.
- IPA: `ChatGPTClient-0.1.0-b71-dev-send-stream.ipa`, `sha256:a9322dba9351842ac2d2374a1f8792129fe64750a1c79da514e2444bb785fd65`; sidecar agrees.
- Independently unpacked package identity: Release `0.1.0`, Build `71`, Candidate `DEV-send-stream-0.1.0-b71`, source marker `af8d4a4b291c`, minimum iOS `14.0`, device families `[1,2]`, Mach-O arm64.
- Evidence ladder: **Code written / exact scope audited / Simulator compile passed / Push CI passed / PR CI passed / Artifact produced / package identity verified / Runtime pending / Stable-Frozen No.**
- b71 is now permanently reserved. Later docs-only commits do not redefine exact product source `af8d4a4b291c05fb63a50cee0261c06d7ce474d3`.

## Exact b70 Runtime evidence — 2026-08-31

User-supplied evidence:

- exact diagnostics `ChatGPTClient-Diagnostics-20260831-094954.json`;
- two current-client screenshots showing the b70 inline reasoning/tool presentation;
- two official ChatGPT iOS screenshots showing the compact conversation summary and official reasoning bottom sheet;
- latest explicit requirement: official interaction/presentation is the target, with pixel-level parity for spacing, row heights, icon size and thinking-time placement; lower-complexity/high-impact corrections should be done first.

The diagnostics identify the tested binary exactly as Release `0.1.0 (70)`, Candidate `DEV-send-stream-0.1.0-b70`, source marker `fb83be916383`, iPhone/iOS17.0.

### Retained b70/b67 behavior

The supplied run still contains one local Send -> one submitted -> one real `sendObserved` -> HTTP200 `text/event-stream` -> Repository response events -> terminal -> authoritative reconcile. Navigation away while generation remained active did not create another response owner. The user explicitly reported only the presentation/performance defects below. This keeps b67 transport ownership accepted; it does **not** prove every unexercised b70 auth/403 gate.

### Rejected b70 presentation/runtime behavior

1. Tool rows still do not match official icon/presentation. GitHub is rendered as literal `GH`; the client also shows a generic `</> 工具调用 · 已完成` row that the supplied official example does not show. The resulting timeline appears noisy and unstructured.
2. Expand/collapse is observably slow. Exact b70 diagnostics show `reasoningSummary.toggled` around 1.38–1.73s and `toolDetail.toggled` around 1.39–1.45s in the supplied long conversation.
3. Source correlation identifies the root: each historical reasoning/tool toggle calls `rebuildPresentationGeometry(...)`, which clears and recomputes metrics/offsets for every presentation row before `reloadData`. The same diagnostics show the post-rebuild table layout itself is only a few to tens of milliseconds. Therefore the interaction hitch is the full deterministic-geometry rebuild, not the final table layout.
4. b70 caps expanded reasoning/tool detail to `toolDetailMaximumBodyHeight = 260` and enables inner `UITextView` scrolling. The official reference instead grows the expanded detail and pushes later content down; scrolling belongs to the outer reasoning surface.
5. The current assistant clear bubble still applies 12pt inner horizontal padding on top of the 16pt table margin, so assistant text/reasoning begins around 28pt while the supplied official reference begins around 16–18pt.
6. Current main-conversation interaction uses inline `思考过程` expansion. The supplied official ChatGPT iOS reference instead shows a compact `思考了 7s` summary + chevron and compact tool row in the conversation, while tapping it presents a rounded bottom sheet titled `正在思考` with tool detail, vertical progress line, completion marker, `思考了 7s`, then `完成`.
7. The official GitHub mark in the supplied 3x screenshot is approximately 16pt square. b70’s literal `GH` text is not acceptable parity.

b70 is therefore **Runtime Partial/Rejected for daily-chat presentation parity**. Its package identity remains valid/reserved.

## Source-backed b71 direction

b71 is intentionally presentation/performance-only. Do not modify accepted protected-Send route/selectors/challenge handling/SSE grammar, Repository response authority, AuthSessionStore lifecycle, b38 quick-navigation algorithm, Stop/new-chat/background/attachments, or unrelated modules.

### Main conversation — official compact summary

- Keep the final answer in the existing deterministic b38 message projection.
- A response timeline produces a compact summary above the final answer rather than inline expanded reasoning.
- Summary title is service-backed `思考了 Ns` when exact duration is known; otherwise use `思考过程` rather than fabricate a duration.
- Use the supplied official spacing hierarchy: assistant content begins at the existing ~16pt outer margin without the additional 12pt clear-bubble inset.
- Show compact meaningful tool rows under the thinking summary with a real bounded local icon and title.
- Hide only the exact generic placeholder row whose normalized title is `工具调用` and which has no authorized visible detail; do not hide real titled tools.
- Completed compact rows do not append the noisy `· 已完成`; active rows may retain an explicit active state until separate Runtime evidence refines it.
- Keep a thin deterministic divider before a real final answer.

### Thinking duration

The already-observed reasoning recap metadata contains exact `finished_duration_sec` together with `reasoning_status=reasoning_ended` / `reasoning_recap_type=collapse`. b71 may carry that bounded duration into the Repository-owned response presentation and historical message projection. Do not infer duration from arbitrary wall-clock gaps when the service field is absent.

### Official-like reasoning detail sheet

Tapping the compact thinking summary presents a presentation-only bottom sheet; it never becomes a response/message authority.

Primary iPhone/iOS17 target follows the supplied official screenshot:

- dimmed background, rounded page sheet, visible grabber;
- title `正在思考`;
- compact tool title row with the same local icon used in the conversation;
- expanded input/output rendered at intrinsic height; no 260pt nested-scrolling cap;
- one outer sheet scroll view owns overflow so long detail pushes later content down;
- vertical progress line / completion marker, `思考了 Ns` when exact duration is available, then `完成`;
- tool input/output disclosure state is local to this presented sheet only. It is not Repository state and does not force conversation-table geometry rebuilds.

### Performance invariant

Historical `思考过程` or tool-detail interaction must not call the full conversation `rebuildPresentationGeometry(...)` path. Opening/closing the reasoning sheet and changing disclosure inside the sheet must be isolated from the b38 table geometry. b38 deterministic final-message geometry/quick-navigation remains untouched.

## Authorized b71 product/config files

The initial b71 candidate may touch only:

- `ChatGPTClient/Conversation/ConversationFeature.swift` — compact summary geometry, official-like sheet, local icon rendering, historical duration projection, removal of inline detail expansion from the main table;
- `ChatGPTClient/RootViewController.swift` — only the exact `reasoning_ended` duration field carried through the existing Repository-owned response event/snapshot; no Send transport semantic change;
- `ChatGPTClient.xcodeproj/project.pbxproj` — Build71/Candidate identity only;
- `.github/workflows/ios-foundation.yml` — b71 candidate/artifact identity only.

Do not touch `AuthSessionStore.swift` in b71 unless new Runtime evidence independently requires it. No new dependency or remote icon loader is authorized. The GitHub mark must be a bounded process-local visual asset/value; it is not remote state.

## b71 batch recovery point

Known pre-write facts:

- formal Work branch was `b936c8c328e58a5da6befebf6aec930e17effe06` before this checkpoint write;
- exact b70 product source remains `fb83be9163838f78abfa47903e67f27b6f66ec52` and must never be rewritten;
- PR #29 remains open/mergeable/unmerged;
- actual `main` remains `d323b9eed2dda75b9986fc06e14014d3e9b365fb`;
- this is the only Active dev checkpoint on the Work branch;
- b71 repository identity search is empty before allocation;
- b70 Runtime evidence now authorizes b71; b70 remains reserved.

Planned non-atomic batches:

1. persist this exact b70 Runtime rejection + b71 scope/recovery checkpoint;
2. re-read the resulting formal head and repeat PR/main/Active/candidate Guard;
3. create a tooling-only b71 assembly ref from that clean checkpoint head;
4. patch only the four authorized product/config files above using exact anchors; run `git diff --check`, scope assertions and Xcode iOS Simulator compile;
5. emit one clean product/config commit whose direct parent is the clean b71 checkpoint and which contains no tooling workflow/script;
6. audit checkpoint->candidate changed files and semantic boundaries;
7. repeat formal branch/PR/main/Active Guard and non-force fast-forward only if unchanged except this Work checkpoint;
8. wait for actual Push + PR CI; verify exact Artifact ZIP/IPA/Info.plist/source marker independently;
9. update checkpoint + BUILD_TEST_INDEX / PROJECT_STATE / MODULE_STATUS / PROJECT_PROFILE / TECHNICAL_DECISIONS and PR #29 from actual evidence;
10. stop only at the exact b71 iPhone/iOS17 Runtime gate.

Recovery must never replay tooling-only commits onto the formal branch and must never redefine b70 identity.

## Evidence ladder

- b67 protected-Send transport: Runtime accepted.
- b69 ordered timeline direction: retained.
- b70: Code/scope/static+sim compile/Push+PR CI/Artifact/package passed; exact iPhone/iOS17 presentation Runtime **Partial/Rejected** by the user-supplied screenshots + diagnostics; auth 403 recovery remains unverified in this supplied run.
- b71: exact source/scope/Simulator compile/Push+PR CI/Artifact/package identity verified; exact iPhone/iOS17 Runtime pending.
- Stable/Frozen Send: No.

## Next exact action

Install exact b71 Artifact `9756491305` / IPA SHA `a9322dba9351842ac2d2374a1f8792129fe64750a1c79da514e2444bb785fd65` on the primary iPhone/iOS17 device and compare directly with the supplied official screenshots. Verify Build71/Candidate/source marker, clear diagnostics, then confirm: compact `思考了 Ns`/`思考过程` summary and meaningful tool rows are aligned near the ~16pt assistant margin; GitHub icon is bounded and no generic empty `工具调用 · 已完成` row appears; tapping thinking opens the rounded `正在思考` sheet immediately without a full-table ~1.4s geometry rebuild; sheet disclosures grow intrinsically under one outer scroll view; duration/completion ordering is correct; final answer divider/spacing is compact; b67 one-Send transport, hidden-thought exclusion, b38 geometry/quick navigation and active-response navigation do not regress. Export diagnostics after terminal. Runtime/manual remains the only next acceptance gate.
