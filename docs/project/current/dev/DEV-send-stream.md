# DEV-send-stream

## Status

**Active — b67 protected-Send transport remains Runtime accepted. Build71 remains a valid/reserved package but the user's exact iPhone/iOS17 comparison rejected its reasoning/tool interaction hierarchy and exposed cross-conversation global Send serialization. Build72 is now the exact current Runtime Candidate: product/config source, scope, Simulator compile, Push CI, PR CI, Artifact and package identity are verified. Runtime/manual/real-device remains pending. Stable/Frozen Send remains No; PR #29 stays open/unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Recovery/docs head immediately before b72 product: `2aaee7f6fa143c1c3426ca89d2d52b42949daf86`
- Exact b72 code commit: `451fa0cb58bbbc681a97d3156bada50357a6067e` (direct parent `2aaee7f6fa143c1c3426ca89d2d52b42949daf86`)
- Exact b72 product/config source: `d20536db37a028556c8032e7c74912805ade785c`
- Candidate: `DEV-send-stream-0.1.0-b72`
- Version / Build: `0.1.0 (72)`
- b72 Push CI: `33403473989 / 99525205970` — success
- b72 PR CI: `33403478927 / 99525223287` — success
- b72 Artifact: `9762189417`
- Artifact ZIP digest: `sha256:5107cedc43b3e5a096da60db9acc2f0705c30bb81be8134f1373dba6f929c1b9`
- IPA: `ChatGPTClient-0.1.0-b72-dev-send-stream.ipa`
- IPA SHA: `ff9d37022a310cab3eea0bb3c298e3d3ec8b0d3057f7256da4f0543dab18b53c`
- Independently unpacked built identity: Release `0.1.0`, Build `72`, Candidate b72, source marker `d20536db37a0`, minimum iOS14.0, bundle `com.whitesharkssw.chatgptclient`, Mach-O arm64
- b39-b72 permanently reserved; never rewrite/reuse b72 after Artifact emission
- Stable/Frozen Send: No

## Latest explicit product requirements carried into b72

### 1. Main-conversation reasoning disclosure

- `思考了 <duration>` / `思考过程` is the first-level expand/collapse control for the **entire visible reasoning/tool timeline of that assistant turn**.
- Expanded content stays inline and preserves real chronology: `reasoning -> tool -> reasoning -> tool -> ...`.
- Collapsing hides both visible reasoning prose and tool rows for that turn.
- Tapping the thinking disclosure itself does not open the secondary sheet.
- `assistant:thoughts` / `inline_cot_expandable_content` remain strictly non-presentational.

### 1.1 Official reasoning-duration format

Use only the exact service-backed `finished_duration_sec` / `reasoningEnded(durationSec)` value. Do not infer wall-clock duration.

- `<60s`: seconds only, e.g. `7s`, `59s`.
- `>=60s`: accumulated minutes + remainder, e.g. `1m`, `1m 5s`, `25m 32s`.
- omit trailing `0s` for exact minutes.
- largest display unit remains minutes; never switch to hours, e.g. `3632s -> 60m 32s`.
- use one shared formatter everywhere this duration is presented.

### 2. Tool row -> secondary sheet

- Tapping any concrete tool row opens the current assistant turn's **ordered tool-call list**.
- Sheet begins at its natural top; no invented auto-scroll-to-clicked behavior.
- Sheet title/presentation follows the supplied official reference (`正在思考`, rounded/dimmed sheet semantics).
- Sheet contains tool operations only; no reasoning prose.
- Each eligible tool item shows icon + title, then authorized tool input directly.
- No `工具输入` heading/disclosure.
- Tool output is hidden completely in this product presentation.
- One outer sheet scroll surface owns overflow.

### 3. Tool icons / disclosure parity

- Unknown tool identity must never masquerade as GitHub.
- Use bounded local icon identity from current evidenced recipient/resource metadata only; do not pair by title guessing.
- User-supplied decrypted official assets are visual evidence only; asset existence alone is not event->icon authority.
- No remote icon loader, persistent icon cache or second state owner.

### 4. Cross-conversation simultaneous generation

- A may keep generating while B independently sends/generates.
- B's Send availability is governed by B's own active-response state, not a global active response in A.
- Initial invariant remains at most one active response per conversation.
- No retry, queue timer, polling, fallback or duplicate Send.

## b72 implementation actually written

Exact detached compare `2aaee7f6...d20536db` changed only four authorized files:

- `.github/workflows/ios-foundation.yml`
- `ChatGPTClient.xcodeproj/project.pbxproj`
- `ChatGPTClient/Conversation/ConversationFeature.swift`
- `ChatGPTClient/RootViewController.swift`

No tooling/assembly files are in the product/config range.

Evidence-backed implementation:

1. `ConversationDetailViewController` now owns first-level reasoning expansion state as presentation state; main assistant cells pass actual `reasoningExpanded` instead of hard-coded false.
2. The main `思考了 <duration>` control expands/collapses the inline response timeline; tool rows remain chronological with reasoning segments.
3. Tapping a concrete tool row opens the ordered tool-list sheet; the sheet excludes reasoning prose and hides tool output, while authorized tool input is shown directly.
4. `ConversationReasoningPresentation.durationText(seconds:)` centralizes the service-backed duration display (`Ns`, `Nm`, `Nm Ns`; minutes remain maximum unit) and is used by summary/sheet status presentation.
5. Unknown/generic tool identity stays bounded; GitHub presentation is not reused for every tool.
6. Root now owns `sendExecutors: [String: CoveredWebSendExecutor]` keyed per conversation rather than one process-global executor gate, while Repository live-response ownership remains per conversation and the accepted per-executor b67 one-Send invariant remains intact.
7. Account-scope reset drains/resets the existing per-conversation executors and Repository live-response state; no second conversation/response/auth authority is introduced.
8. Protected route/composer selector/challenge/SSE grammar was guarded against change during assembly; b72 does not intentionally alter the accepted b67 Web Send transport contract.

## b72 assembly / validation evidence

Isolated tooling ref: `assembly/dev-send-stream-b72-20260831`.

- Assembly run `33401346952 / 99518126633` failed **tooling-only** before compile because macOS Bash 3.2 lacks `mapfile`; patch application and `git diff --check` had already completed. No product branch/Artifact was emitted.
- Assembly run `33401495902 / 99518627226` passed exact four-file scope audit and Xcode 16.4 iOS Simulator build. Final emit failed **tooling-only** because GitHub Actions token could not push a workflow-file change. No canonical Candidate/Artifact was emitted from that failed push.
- Recovery run `33401711501 / 99519351462` repeated scope + Simulator compile and emitted the clean three-file code/project commit; workflow identity was then added through GitHub contents API on the clean product branch.
- Clean code commit `451fa0cb58bbbc681a97d3156bada50357a6067e` has direct parent `2aaee7f6fa143c1c3426ca89d2d52b42949daf86`.
- Exact product/config source after workflow identity: `d20536db37a028556c8032e7c74912805ade785c`.
- Detached compare confirms exactly the four authorized files above.
- Formal branch was non-force fast-forwarded from `2aaee7f6...` to exact source `d20536db...` after repeated branch/PR/main/current-dev guard.
- Push CI `33403473989 / 99525205970`: success.
- PR CI `33403478927 / 99525223287`: success.
- Canonical Push Artifact `9762189417`: `ChatGPTClient-DEV-send-stream-0.1.0-b72`.
- GitHub Artifact digest and independently downloaded ZIP SHA agree: `5107cedc43b3e5a096da60db9acc2f0705c30bb81be8134f1373dba6f929c1b9`.
- ZIP contains the expected IPA + `.sha256` only.
- IPA sidecar and independent SHA agree: `ff9d37022a310cab3eea0bb3c298e3d3ec8b0d3057f7256da4f0543dab18b53c`.
- Independent package inspection confirms arm64, Release, `0.1.0 (72)`, Candidate b72, source marker `d20536db37a0`, minimum iOS14.0.

## Retained accepted boundaries

- b67: one local Send -> one protected official-page Send -> HTTP200 same-response SSE -> Repository updates -> terminal/reconcile is Runtime accepted.
- `ConversationRepository` remains sole conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` remains sole account authority; default `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Covered official Web remains browser challenge/protected-Send executor only; full Web conversation rendering stays rejected.
- b69 chronological response timeline + exact-parent result association remain retained.
- b38 deterministic long-message geometry/quick navigation remains accepted and must not regress.
- No retry/polling/timer/watchdog/fallback/compatibility shim/second message or response store.

## Evidence ladder

- b67 protected-Send transport: **Runtime accepted**.
- b69 ordered timeline direction: retained.
- b70: package valid/reserved; later presentation direction superseded.
- b71: Code/scope/Simulator/Push+PR CI/Artifact/package verified; exact user Runtime comparison rejected interaction hierarchy + global cross-conversation serialization.
- b72: **Code written / exact scope audited / Simulator compile passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Runtime pending / Stable-Frozen No.**

## Documentation / PR recovery point after Artifact

Confirmed complete:

1. exact b72 product/config source `d20536db...` exists and formal branch has been advanced to it non-force;
2. Push + PR CI passed on that exact source;
3. canonical Build72 Artifact/package identity is verified;
4. this checkpoint records the exact evidence.

Still pending in this documentation batch:

1. refresh `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `TECHNICAL_DECISIONS.md`, and `BUILD_TEST_INDEX.md` with b72 evidence/status where applicable;
2. synchronize PR #29 title/body to b72 while keeping it open/unmerged;
3. do not alter exact b72 product/config source identity when later docs-only commits advance the formal branch.

## Exact next action / human Runtime gate

After durable docs/PR synchronization, hand exact Build72 IPA to the user. On primary iPhone/iOS17:

1. verify Build72 / Candidate/source marker `d20536db37a0`, then clear diagnostics;
2. run a reasoning/tool response and verify the main `思考了 <duration>` control expands/collapses the entire chronological reasoning+tool timeline inline;
3. verify duration formatting around minute boundaries when naturally available (`<60s`, `>=60s`, accumulated minutes only; no hours);
4. tap concrete tool rows and verify the secondary sheet is an ordered tools-only list with direct authorized input, no reasoning prose and no tool-output section;
5. verify unknown/non-GitHub tool rows do not masquerade as GitHub;
6. start generation in A, switch to B, send in B while A remains active, and verify both responses remain independently owned/presented without duplicate Send;
7. verify hidden A navigation preservation, terminal reconciliation, hidden-thought exclusion, b38 geometry and b67 one-Send transport do not regress;
8. export diagnostics after terminal(s).

Do not allocate b73 unless exact b72 Runtime produces a concrete defect/evidence need.