# DEV-send-stream

## Status

**Active — b67 protected-Send transport remains Runtime accepted. Exact Build72 is a valid/reserved package and exact iPhone/iOS17 b72 Runtime positively supports the tested cross-conversation simultaneous-generation path, but rejects the prior reasoning/tool presentation density/default-live-disclosure behavior. Build73 is now Code/scope/Simulator/Push+PR CI/Artifact/package verified and is the current presentation Runtime candidate. Stable/Frozen Send remains No; PR #29 stays open/unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Exact b72 product/config source: `d20536db37a028556c8032e7c74912805ade785c`
- b72 Artifact: `9762189417`
- b72 IPA SHA: `ff9d37022a310cab3eea0bb3c298e3d3ec8b0d3057f7256da4f0543dab18b53c`
- Exact b73 product/config source: `4edda892a04a1a07f4a07e74b135b969ea82193e`
- b73 product code commit: `0e3eb6cad4cc56e8c2bcb946724d7cf1d4d55701`
- b73 Candidate: `DEV-send-stream-0.1.0-b73`
- b73 Version / Build: `0.1.0 (73)`
- b73 assembly: `33408291419` — success after the earlier tooling-only assertion failure `33408115270`; Xcode Simulator compile passed.
- b73 Push CI: `33408695143 / 99542593642` — success
- b73 PR CI: `33408698697 / 99542605699` — success
- b73 Artifact: `9764247402`
- b73 Artifact ZIP digest: `sha256:718c2f4fd0fe3521f7469f5996f6944960ffdaa3b2829c0c17e340ebd41dd206`
- b73 IPA: `ChatGPTClient-0.1.0-b73-dev-send-stream.ipa`
- b73 IPA SHA: `8285ba9d5f63207feb2eaf722ec722a886f3ee88956236a89a716ad58b884113`
- Independently unpacked b73 package identity: Release `0.1.0 (73)`, Candidate b73, source marker `4edda892a04a`, minimum iOS14.0, arm64, iPhone/iPad family.
- b39-b73 permanently reserved; never rewrite/reuse any emitted identity.
- Stable/Frozen Send: No.

## Retained accepted boundaries

- b67: one local Send -> one protected official-page Send -> HTTP200 same-response SSE -> Repository updates -> terminal/reconcile is Runtime accepted.
- `ConversationRepository` remains sole conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` remains sole account authority; default `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Covered official Web remains browser challenge/protected-Send executor only; full Web conversation rendering stays rejected.
- b69 chronological response timeline + exact-parent result association remain retained.
- b38 deterministic long-message geometry/quick navigation remains accepted and must not regress.
- No retry/polling/timer/watchdog/fallback/compatibility shim/second message or response store.

## Exact b72 iPhone/iOS17 Runtime — partial acceptance / presentation reject

User supplied direct screenshots comparing the same response in this client vs the official ChatGPT app plus `ChatGPTClient-Diagnostics-20260831-150238.json`.

### Accepted in the tested scope

1. Cross-conversation simultaneous generation no longer shows the former global `其他会话回答中` gate.
2. Diagnostics show A already active and continuing while B begins a second response operation; `coveredExecutor.created` reaches `activeExecutorCount=2` and the two conversations retain separate Repository live-response identities.
3. User reports a simple A/B simultaneous-generation test found no additional problem.
4. Therefore the tested existing-conversation A-generating + B-send/generate path is **Runtime positive for this exact b72 test**, without claiming broader service concurrency, background or memory-pressure completeness.
5. The b72 incremental reasoning-disclosure geometry correction is also positive: live toggles in the supplied export are single-digit milliseconds in the observed sequence rather than the former ~1.4s full-table rebuild path.

### Rejected presentation behavior

1. Main inline reasoning/tool block remains much denser than the official app. One historical turn can expose dozens of low-level tool rows; the supplied diagnostics include a `toolList.presented` case with `toolCount=49`.
2. Official main conversation presentation is semantic and concise: service-authored purpose/action text is shown, while low-value generic implementation calls are not sprayed line-by-line into the main chat surface.
3. Current main inline rendering can still show repeated fallback `工具调用` rows, especially when a GitHub exact-parent detail exists but the invocation had no meaningful `metadata.reasoning_title`.
4. Tool-row vertical rhythm is too tight; official tool rows have visibly larger row height/spacing.
5. Current visible reasoning prose uses secondary/subheadline styling and appears too gray/small compared with the official reference; official visible reasoning prose reads closer to ordinary body text while tool rows and the summary remain secondary.
6. Explicit requirement: **while a live response is in thinking/reasoning/tool activity, its first-level reasoning disclosure defaults expanded; on the exact `reasoning_ended` transition it automatically collapses once.** After that automatic collapse, later manual user expand/collapse remains user-owned and must not be repeatedly overridden by subsequent redraws/final deltas.
7. Historical completed responses continue to default collapsed unless the user explicitly expands them.

## Exact b73 implementation / evidence

Build73 is a presentation-only correction. Detached compare from the b73 checkpoint to exact source `4edda892...` contains exactly:

- `ChatGPTClient/Conversation/ConversationFeature.swift`
- `ChatGPTClient.xcodeproj/project.pbxproj`
- `.github/workflows/ios-foundation.yml`

`ChatGPTClient/RootViewController.swift` did not change, preserving the b72 per-conversation executor implementation and b67 transport path.

Implemented behavior:

1. Secondary tool-list sheet keeps the current ordered eligible tool operations, including generic entries needed to inspect the actual call list.
2. Main inline reasoning timeline shows only tool rows with a meaningful service-authored title; fallback title `工具调用` is omitted from the main timeline. No title merging/synthesis/guessing was added.
3. Main reasoning prose uses body-sized primary-label typography and looser line spacing; tool rows remain secondary with larger minimum line height/paragraph spacing.
4. `思考了 <duration>` keeps the minutes-only formatter (`Ns`, `Nm`, `Nm Ns`, never hours).
5. Live disclosure auto-opens once when first visible reasoning/tool content arrives; a user manual collapse during reasoning is not reopened by later deltas.
6. First observation of exact `snapshot.reasoningEnded == true` auto-collapses once; later final deltas/rebuilds do not reassert the auto state over manual user choice.
7. Historical completed reasoning remains default-collapsed/user-controlled.
8. Tool-list sheet semantics from b72 remain tools-only/input-only; no reasoning prose and no tool-output UI.
9. No changes to protected route/selectors/SSE grammar, Repository response owner, auth lifecycle, per-conversation executor dictionary, b38 quick navigation, retry/poll/timer/watchdog/fallback machinery.

Validation:

- first assembly run `33408115270 / 99540666049` failed tooling-only before compile because an exact assertion missed one remaining selector call; no product branch/Artifact was emitted.
- corrected assembly run `33408291419` succeeded, including scope audit, `git diff --check`, protected baseline checks and Xcode 16.4 iOS Simulator compile.
- Push CI `33408695143 / 99542593642` succeeded on exact source `4edda892...` using Xcode 16.4 / iPhoneOS18.5 / Release arm64 iOS14 target.
- PR CI `33408698697 / 99542605699` succeeded on the same exact source.
- canonical Push Artifact `9764247402` has GitHub digest `sha256:718c2f4fd0fe3521f7469f5996f6944960ffdaa3b2829c0c17e340ebd41dd206`.
- downloaded Artifact ZIP independently hashes to the same digest.
- independently unpacked IPA SHA is `8285ba9d5f63207feb2eaf722ec722a886f3ee88956236a89a716ad58b884113`; sidecar matches.
- built `Info.plist`: `0.1.0 (73)`, Candidate `DEV-send-stream-0.1.0-b73`, source `4edda892a04a`, Release, minimum iOS14.0; executable is Mach-O arm64.

Evidence ladder: **Code written / exact scope audited / Simulator compile passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Runtime pending / Stable-Frozen No.**

## b73 exact Runtime gate

On the primary iPhone/iOS17 device, install exact Build73 and focus on presentation only:

1. start one response that visibly reasons/tools; confirm first visible reasoning/tool content auto-expands the first-level reasoning block while generation is active;
2. while still reasoning, manually collapse once and confirm later reasoning/tool deltas do not force it open again;
3. on a normal run left expanded, confirm exact reasoning end auto-collapses once as final answer becomes the visual focus;
4. after that automatic collapse, manually expand/collapse and confirm later final deltas/redraws do not override the user choice;
5. compare main inline density against official: fallback generic `工具调用` rows should not spray through the main chat; meaningful service-authored purpose rows remain chronological with visibly looser row height/spacing;
6. reasoning prose should read at ordinary body scale/primary contrast; summary/tool rows remain secondary;
7. click a concrete tool row and confirm the ordered tools-only/input-only sheet still exposes the actual tool-call list, including generic operations omitted from the main timeline;
8. confirm b72 cross-conversation A-generating + B-send behavior does not regress; this is regression-only because Root did not change;
9. confirm hidden thoughts remain absent and b38 long-message/quick-navigation behavior does not regress.

Runtime/manual/real-device for b73 is **pending**. Do not describe the presentation defect as solved until this exact package passes.

## b73 evidence synchronization — complete

- Exact b73 product/config source remains `4edda892a04a1a07f4a07e74b135b969ea82193e`; later docs-only commits do not redefine product identity.
- Checkpoint package-evidence commit: `8a2437194f837e7002460829c15e4d2428832902`.
- Durable docs-only commit: `3da5f09adf8d860b531428275e3c1e3ba97e8dad`; detached audit from `8a243719...` changed only six `docs/project/**` files.
- `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `TECHNICAL_DECISIONS.md`, `BUILD_TEST_INDEX.md` and directly conflicting `PROJECT_SPECIFIC_RULES.md` wording are synchronized to b72/b73 evidence.
- PR #29 title/body is synchronized to b73 and remains open / mergeable / unmerged.
- `main` remains `d323b9eed2dda75b9986fc06e14014d3e9b365fb` at this gate.
- b73 Artifact/package identity is permanently reserved; recovery must not rewrite product/config source or allocate b74 without concrete b73 Runtime evidence.

## Exact next action

Human-only gate: install exact Build73 IPA on the primary iPhone/iOS17 device and run the b73 Runtime matrix above. Return screenshots/recording and diagnostics if a defect remains. If b73 passes, record the exact Runtime result and continue to the next Phase 9 evidence gate; if it exposes a concrete defect, allocate the earliest unique b74 only after re-running the Resume Guard.
