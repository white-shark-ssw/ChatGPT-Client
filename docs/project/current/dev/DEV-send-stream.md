# DEV-send-stream

## Status

**Active — b67 protected-Send transport remains Runtime accepted. Exact Build72 is a valid/reserved package. Exact iPhone/iOS17 b72 Runtime now positively supports the tested cross-conversation simultaneous-generation path, but rejects the current reasoning/tool presentation density and default live-disclosure behavior. Build73 is allocated for a presentation-only correction. Stable/Frozen Send remains No; PR #29 stays open/unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Formal head before this checkpoint update: `636701968c59124842da01b8d8b6585f8055d5e5`
- Exact b72 product/config source: `d20536db37a028556c8032e7c74912805ade785c`
- b72 Candidate: `DEV-send-stream-0.1.0-b72`
- b72 Version / Build: `0.1.0 (72)`
- b72 Push CI: `33403473989 / 99525205970` — success
- b72 PR CI: `33403478927 / 99525223287` — success
- b72 Artifact: `9762189417`
- b72 Artifact ZIP digest: `sha256:5107cedc43b3e5a096da60db9acc2f0705c30bb81be8134f1373dba6f929c1b9`
- b72 IPA: `ChatGPTClient-0.1.0-b72-dev-send-stream.ipa`
- b72 IPA SHA: `ff9d37022a310cab3eea0bb3c298e3d3ec8b0d3057f7256da4f0543dab18b53c`
- b39-b72 permanently reserved; never rewrite/reuse b72 after Artifact emission.
- Next unique Candidate allocated by the b72 Runtime defects below: `DEV-send-stream-0.1.0-b73` / Build `73`.
- Stable/Frozen Send: No.

## Retained accepted boundaries

- b67: one local Send -> one protected official-page Send -> HTTP200 same-response SSE -> Repository updates -> terminal/reconcile is Runtime accepted.
- `ConversationRepository` remains sole conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` remains sole account authority; default `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Covered official Web remains browser challenge/protected-Send executor only; full Web conversation rendering stays rejected.
- b69 chronological response timeline + exact-parent result association remain retained.
- b38 deterministic long-message geometry/quick navigation remains accepted and must not regress.
- No retry/polling/timer/watchdog/fallback/compatibility shim/second message or response store.

## Exact b72 package evidence

Exact detached product/config source is `d20536db37a028556c8032e7c74912805ade785c`; assembly/Simulator compile, Push CI, PR CI, Artifact and independently unpacked package identity all passed. Built package is Release `0.1.0 (72)`, Candidate b72, source marker `d20536db37a0`, minimum iOS14.0, arm64.

Evidence ladder before Runtime: **Code written / exact scope audited / Simulator compile passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified.**

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
6. New explicit requirement: **while a live response is in thinking/reasoning/tool activity, its first-level reasoning disclosure defaults expanded; on the exact `reasoning_ended` transition it automatically collapses once.** After that automatic collapse, later manual user expand/collapse remains user-owned and must not be repeatedly overridden by subsequent redraws/final deltas.
7. Historical completed responses continue to default collapsed unless the user explicitly expands them.

## b73 authorized product scope

Build73 is a presentation-only correction. It must not modify accepted transport/concurrency/auth ownership.

Authorized source/config files:

- `ChatGPTClient/Conversation/ConversationFeature.swift`
- `ChatGPTClient.xcodeproj/project.pbxproj`
- `.github/workflows/ios-foundation.yml`

`ChatGPTClient/RootViewController.swift` is **not authorized** for b73 unless new evidence proves the display-only correction cannot be implemented from the existing Repository snapshot fields. Current source already exposes `snapshot.reasoningEnded`, phase and ordered timeline to the Detail presentation layer, so no Root change is presently justified.

### b73 exact presentation behavior

1. Split tool selection for the two UI levels:
   - secondary tool-list sheet keeps the current ordered eligible tool operations, including generic entries needed to inspect the actual call list;
   - main inline reasoning timeline shows only tool rows with a meaningful service-authored title; fallback title `工具调用` is omitted from the main timeline even when authorized detail exists.
2. Do **not** merge, synthesize or rewrite tool titles by guessing. The concise main row must come from the current service-backed title already carried by the timeline (currently `metadata.reasoning_title` when present). Generic low-level calls remain accessible in the tool-list sheet.
3. Main reasoning prose uses body-sized primary-label typography and more official-like line spacing; tool rows remain secondary but receive larger minimum line height / paragraph spacing.
4. `思考了 <duration>` summary remains secondary and continues using the b72 minutes-only duration formatter (`Ns`, `Nm`, `Nm Ns`, never hours).
5. Live auto-disclosure is presentation state only:
   - on the first visible reasoning/tool timeline content of one live generation, auto-expand once;
   - if the user manually collapses while still thinking, later deltas must not auto-open it again;
   - on first observation of `snapshot.reasoningEnded == true`, auto-collapse once;
   - after that one collapse, later final deltas/rebuilds do not override manual user state.
6. Historical reasoning remains user-controlled and default collapsed.
7. Tool-list sheet behavior from b72 remains: clicking any visible concrete tool row opens the current assistant turn's ordered tools-only list; no reasoning prose; direct authorized input; no output UI.
8. No changes to b72 per-conversation executor dictionary, b67 protected route/selectors/SSE grammar, Repository response ownership, auth lifecycle, quick navigation or follow-tail semantics.

## b73 identity / batch recovery point

Candidate allocation is now reserved:

- Candidate: `DEV-send-stream-0.1.0-b73`
- Version / Build: `0.1.0 (73)`
- b73 Artifact identity does not exist yet.

Non-atomic write chain:

1. **Confirmed complete:** b72 package exists and is permanently reserved; user Runtime evidence is classified above; b73 Candidate is unique by repository search before allocation.
2. **Current write:** this checkpoint records the b72 Runtime and exact b73 authorized behavior before product writes.
3. **Pending batch A:** create a tooling-only assembly branch from the resulting checkpoint head; apply exact-anchor changes only to `ConversationFeature.swift` plus b73 project/workflow identity; audit changed-file scope and protected-Send invariants; run Xcode 16.4 iOS Simulator compile.
4. **Pending batch B:** produce a clean b73 product/config source with the checkpoint head as ancestor and no tooling files; detached compare must contain exactly the three authorized files.
5. **Pending batch C:** repeat branch/PR/main/current-dev/candidate conflict Guard, then non-force fast-forward formal Work branch to exact b73 product/config source.
6. **Pending batch D:** obtain exact-head Push CI + PR CI, canonical Push Artifact, IPA SHA and built Info.plist identity.
7. **Pending batch E:** synchronize this checkpoint plus `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `TECHNICAL_DECISIONS.md`, `BUILD_TEST_INDEX.md` and PR #29 as docs-only evidence. Do not redefine the exact product source with later docs commits.

Recovery must never touch/rewrite b72 Artifact `9762189417`, b72 source `d20536db...`, b67 transport rules, or the accepted b72 per-conversation executor implementation.

## Evidence ladder

- b67 protected-Send transport: **Runtime accepted**.
- b72 cross-conversation simultaneous generation: **Runtime positive for the supplied exact-device A/B test**.
- b72 main reasoning/tool presentation: **Runtime rejected for official parity/density/default-live-disclosure behavior**.
- b73: **Candidate allocated / code not yet written / CI not yet run / Artifact not yet produced / Runtime pending / Stable-Frozen No.**

## Exact next action

Resume from the resulting checkpoint head. Verify the branch update landed, then create the isolated b73 assembly branch and implement only the authorized presentation correction. Do not ask for another requirement decision unless source evidence contradicts the above interaction contract. Continue autonomously through compile/CI/Artifact if normal tooling remains available.
