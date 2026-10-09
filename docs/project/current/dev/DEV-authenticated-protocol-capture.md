# DEV-authenticated-protocol-capture

## Status

**Active / stacked dependency on DEV-send-stream / cleaned Push Simulator CI green / durable docs synced / PR #38 open + mergeable / PR Simulator CI pending**

- **Work ID**: `DEV-authenticated-protocol-capture`
- **Routing aliases / keywords**: `Authenticated Protocol Capture / 协议采集 / sanitized fixture / Simulator replay / 真机协议抓取`
- **Task**: Establish a reusable user-controlled authenticated protocol capture pipeline: real-device authenticated capture -> local sensitive diagnostic export -> deterministic sanitization/fixture generation -> Simulator replay, without persisting reusable auth secrets or creating a second production authority.
- **User acceptance intent**: on a logged-in iPhone, normal workflow is `开发者诊断 -> 开始采集 -> 正常操作目标功能 -> 停止采集 -> 导出诊断包`; JavaScript instrumentation, when required, is injected/managed automatically rather than manually pasted. Development consumes only sanitized fixtures for repeated macOS Simulator replay.
- **Parent dependency**: explicitly stacked on `DEV-send-stream` / PR #29. Parent re-verified open + mergeable at `dev/send-stream-20260829@79107c64347e05e0dfd4f679a3c970dfa09a18b0`; base `main@94f0c5777dad262cd1fb22be49082dbd92c962f2`. Parent product remains Build115 / `DEV-send-stream-0.1.0-b115`.
- **Branch / PR**: `dev/authenticated-protocol-capture-20261009`; source-clean Simulator-tested head `3abb06889902cd96b8fca45d7d50fec6bdcf237d`; current PR head before this checkpoint write was `f400173c03a5cb9240e21bfe5b04e2cfdb5ec344`. Stacked **PR #38** targets exactly `dev/send-stream-20260829`; re-query after creation reports open / mergeable / non-draft. Formal IPA Candidate: **not allocated**.
- **Simulator/test identity**: `SIM-DEV-authenticated-protocol-capture-v1`; distinct from inherited `SIM-DEV-simulator-test-baseline-v1`.
- **Candidate rule**: do not allocate b116 merely because this infrastructure exists. A task-owned formal Candidate is allowed only if physical-device packaging is genuinely required after stacked PR CI and after a fresh global candidate/conflict check.

## Ownership and security boundary

- Diagnostic capture observes existing official Web/native transport paths only. It is not conversation/auth/response authority and adds no production retry/fallback/timer/watchdog/polling or duplicate response state.
- `ConversationRepository` remains conversation/content/response authority; `AuthSessionStore` remains auth/account authority; Simulator fixture transport remains Debug-only input substitution.
- Raw authenticated capture exports stay local/user-controlled and are never automatic repository/CI input.
- Repository fixtures must contain no password, Cookie, Authorization, access/session token, reusable auth header or equivalent credential.
- Conversation/message/account identifiers may survive only as capture-local stable aliases when correlation requires them. Arbitrary user/assistant text is reduced to structural projections/lengths.
- Generic unclassified `/backend-api/` path segments preserve only structural alphabetic endpoint names plus `_`/`-`; digit-bearing/high-entropy/identifier-like segments become `{opaque}`. Explicit Conversation Detail identity remains capture-local alias data.

## Implementation and evidence history

- Branch baseline: parent `79107c64347e05e0dfd4f679a3c970dfa09a18b0`; inherited Build115 / Candidate b115 unchanged.
- Initial source commit `ac54c32c904c64926c62ab50d4f2fd00aabfe207` added Settings capture UI/store, document-start WK instrumentation, sanitizer/fixture compiler, sanitized Stop seed fixture, replay seam extension and one Stop replay XCTest. Static staging `37843282969 / 113537778690` passed scope, sanitizer self-test and `git diff --check`.
- Simulator workflow delta was integrated as `89ed8f76281a46afbfdf5526253c7b699f0022cd` after a GitHub-token workflow-write limitation prevented the bot from pushing that workflow directly. This was a tooling permission issue, not a product/test failure.
- First Simulator run `37843389537 / 113538957651` failed only `testSanitizedProtocolReplayFixtureReplaysStopRequestAndAckWithoutNetwork` with `protocol_replay_request_body_mismatch`; inherited 2 XCTest + 3 XCUITest stayed green. Failure Artifact `11578822569`, digest `sha256:fe4263ae8de40fc82416cc775c9d6b120612c6128eeac56eafe74b88510933c9`.
- Root cause was request-body representation at the custom URLProtocol seam, not fixture-value mismatch. Exact fixture/request JSON matched.
- Replay correction commit `ace92921b0195fbd60dd28a8e55c5c643fd1c6ca` reads the strict JSON body from either `URLRequest.httpBody` or Foundation's equivalent `httpBodyStream`; canonical JSON equality remains strict. No relaxed matcher or production fallback was added.
- Replay-correction push run `37976040038 / 113974470892` passed sanitizer + 3 XCTest + 3 inherited XCUITest and produced Simulator evidence Artifact `11638483189`, digest `sha256:45a4b0a9c9db1526d4429a796d7631ce1d0404bfee3352a7439ec5babb5036d1`.
- Privacy hardening staging run `37977287903 / 113978649674` passed exact one-file scope and source guards; commit `f13b663e4b32468ae3c4873a2b3d52f1249714bf` changed only diagnostic `safePathSegment`.
- Privacy-source run `37977354593 / 113978874101` on `832ba7e7b7bb8875c5e63fde82ec7fef24e702ce` passed sanitizer + full XCTest/XCUITest and produced Artifact `11640295007`, digest `sha256:f3bc55f7c179c2a781af29bd7fedb4d5387291a04cf6d1bcd215f2975b439a0c`.
- PR-prep cleanup removed exactly `.github/workflows/stage-authenticated-protocol-capture.yml` at `294a7fe3273b19f986ed2b2f67ac42848621fc92` and `scripts/staging/apply_authenticated_protocol_capture.py` at `3abb06889902cd96b8fca45d7d50fec6bdcf237d`.
- **Cleaned-branch final Push Simulator gate**: run `37978621723`, job `113983154439`, exact source-clean head `3abb06889902cd96b8fca45d7d50fec6bdcf237d`, completed success. Checkout/toolchain/Simulator boot, protocol sanitizer validation, full XCTest+XCUITest step, evidence capture and upload all passed. Artifact `11639784911`, name `SimulatorPreflight-37978621723-1`, size `2668006`, digest `sha256:0b2833a65a3da54189107468c81b18df13737bd1bbebc10a3577abe0ae02b2c0`. This is Simulator/CI evidence only.
- **Durable-doc sync completed**: guarded docs-only workflow run `37989864878 / 114020965448` passed parent/Candidate/cleanup/sanitizer guards, exact five-doc scope and `git diff --check`, producing docs commit `08af475e811efe38f9c9eeced569a3c74211924e`. Updated only `PROJECT_STATE.md`, `MODULE_STATUS.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_SPECIFIC_RULES.md`, and `BUILD_TEST_INDEX.md`.
- Temporary durable-doc sync workflow was removed at `f400173c03a5cb9240e21bfe5b04e2cfdb5ec344`; parent compare then contained exactly the intended 14 long-lived paths and no one-off staging/sync artifacts.
- **Stacked PR opened**: PR #38 `DEV-authenticated-protocol-capture: sanitized authenticated capture + Simulator replay`, head `f400173c03a5cb9240e21bfe5b04e2cfdb5ec344`, base `dev/send-stream-20260829@79107c64347e05e0dfd4f679a3c970dfa09a18b0`. Immediate second query reports `mergeable=true`. PR changed-filename list exactly matches the intended 14 long-lived paths.
- Product Xcode identity, `ConversationFeature.swift`, `RootViewController.swift`, production Send/SSE ownership and Authentication ownership were not changed by this Work.

## Current long-lived implementation surface

PR #38 currently contains exactly:

- `.github/workflows/ios-simulator-preflight.yml`
- `ChatGPTClient/Protocol/ProtocolReadProbe.swift`
- `ChatGPTClient/SettingsViewController.swift`
- `ChatGPTClient/Testing/SimulatorFixtureTransport.swift`
- `ChatGPTClientTests/ConversationRepositorySimulatorTests.swift`
- `docs/project/BUILD_TEST_INDEX.md`
- `docs/project/MODULE_STATUS.md`
- `docs/project/PROJECT_SPECIFIC_RULES.md`
- `docs/project/PROJECT_STATE.md`
- `docs/project/TECHNICAL_DECISIONS.md`
- `docs/project/current/dev/DEV-authenticated-protocol-capture.md`
- `fixtures/protocol/stop-request-ack-v1.json`
- `scripts/protocol_capture/README.md`
- `scripts/protocol_capture/sanitize_capture.py`

The seed Stop fixture contains only the already Runtime-proven official Web contract: `POST /backend-api/stop_conversation`, capture-local conversation alias, empty `exclude_async_types`, HTTP200 JSON `status=ok`, `last_message_id=null`. It intentionally invents no post-Stop Detail semantics.

## Batch recovery point — PR CI -> physical-device gate

- **Known source-clean tested head**: `3abb06889902cd96b8fca45d7d50fec6bdcf237d`; Push Simulator CI green at `37978621723 / 113983154439`, Artifact `11639784911`.
- **Known PR creation head**: `f400173c03a5cb9240e21bfe5b04e2cfdb5ec344`; PR #38 base `79107c64347e05e0dfd4f679a3c970dfa09a18b0`; mergeable true; 14-path diff exact.
- **Batch E1 — completed**: checkpoint recorded cleanup + source-clean CI.
- **Batch E2 — completed**: five durable docs synchronized by guarded run `37989864878 / 114020965448`; temporary sync workflow removed before PR.
- **Batch E3 — PR opened / CI pending**: PR #38 exists. Current checkpoint write moves head docs-only; PR CI must be classified against the current merge ref after GitHub updates it. Do not treat the prior Push run as PR merge-ref proof.
- **Batch D real-device package — conditional after PR CI**: if PR CI is green, decide whether a task-owned physical-device IPA is required to validate Start -> capture -> Stop -> Export on logged-in iPhone. If required, perform fresh candidate-conflict guard before allocating any build. Otherwise keep inherited Build115/b115 untouched.
- **Recovery rule**: never modify/delete `DEV-send-stream`, `DEV-send-stream-round7-runtime-addendum`, `DEV-simulator-test-baseline` or `DEV-message-rendering` checkpoints from this task. If interrupted, compare PR #38 head/base/mergeability, branch head, parent head and PR CI before taking the next action.

## Evidence ladder

**Code written / static sanitizer + exact-scope checks passed / strict replay correction passed / privacy path hardening passed / cleaned source-head Push Simulator CI passed / Simulator evidence Artifact produced / durable docs synced / stacked PR #38 open+mergeable / PR Simulator CI pending / formal IPA none / real-device authenticated capture not tested / sanitized real post-Stop Detail fixture not yet produced / Stable-Frozen No.**

## Next exact action

Classify PR #38 merge-ref `iOS Simulator Preflight` on the current head. If green, re-run global candidate/conflict guard and decide whether the new real-device capture UX justifies a task-owned IPA for Human Runtime; do not allocate b116 before that gate.