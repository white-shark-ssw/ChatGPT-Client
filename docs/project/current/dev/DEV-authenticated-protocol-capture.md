# DEV-authenticated-protocol-capture

## Status

**Active / stacked dependency on DEV-send-stream / cleaned branch Simulator CI green / durable-doc sync + stacked PR pending**

- **Work ID**: `DEV-authenticated-protocol-capture`
- **Routing aliases / keywords**: `Authenticated Protocol Capture / 协议采集 / sanitized fixture / Simulator replay / 真机协议抓取`
- **Task**: Establish a reusable user-controlled authenticated protocol capture pipeline: real-device authenticated capture -> local sensitive diagnostic export -> deterministic sanitization/fixture generation -> Simulator replay, without persisting reusable auth secrets or creating a second production authority.
- **User acceptance intent**: on a logged-in iPhone, normal workflow is `开发者诊断 -> 开始采集 -> 正常操作目标功能 -> 停止采集 -> 导出诊断包`; JavaScript instrumentation, when required, is injected/managed automatically rather than manually pasted. Development consumes only sanitized fixtures for repeated macOS Simulator replay.
- **Parent dependency**: explicitly stacked on `DEV-send-stream` / PR #29. Parent was re-verified open + mergeable at `dev/send-stream-20260829@79107c64347e05e0dfd4f679a3c970dfa09a18b0`; base `main@94f0c5777dad262cd1fb22be49082dbd92c962f2`. Parent product remains Build115 / `DEV-send-stream-0.1.0-b115`.
- **Branch / PR**: `dev/authenticated-protocol-capture-20261009`; cleaned branch head `3abb06889902cd96b8fca45d7d50fec6bdcf237d`. Stacked PR not opened yet; intended base is `dev/send-stream-20260829` only. Formal IPA Candidate: **not allocated**.
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
- Privacy-source final run `37977354593 / 113978874101` on `832ba7e7b7bb8875c5e63fde82ec7fef24e702ce` passed sanitizer + full XCTest/XCUITest and produced Artifact `11640295007`, digest `sha256:f3bc55f7c179c2a781af29bd7fedb4d5387291a04cf6d1bcd215f2975b439a0c`.
- PR-prep cleanup then removed exactly the two temporary one-off staging artifacts: `.github/workflows/stage-authenticated-protocol-capture.yml` at commit `294a7fe3273b19f986ed2b2f67ac42848621fc92`, and `scripts/staging/apply_authenticated_protocol_capture.py` at commit `3abb06889902cd96b8fca45d7d50fec6bdcf237d`.
- **Cleaned-branch final Push Simulator gate**: run `37978621723`, job `113983154439`, exact head `3abb06889902cd96b8fca45d7d50fec6bdcf237d`, completed success. Checkout/toolchain/Simulator boot, protocol sanitizer validation, full XCTest+XCUITest step, evidence capture and upload all passed. Artifact `11639784911`, name `SimulatorPreflight-37978621723-1`, size `2668006`, digest `sha256:0b2833a65a3da54189107468c81b18df13737bd1bbebc10a3577abe0ae02b2c0`. This is Simulator/CI evidence only.
- Parent `dev/send-stream-20260829` and PR #29 were re-verified unchanged after this clean run, so the tested child is still based on the current intended parent.
- Product Xcode identity, `ConversationFeature.swift`, `RootViewController.swift`, production Send/SSE ownership and Authentication ownership were not changed by this Work.

## Current implementation surface

Long-lived PR scope after cleanup is limited to:

- `.github/workflows/ios-simulator-preflight.yml`
- `ChatGPTClient/Protocol/ProtocolReadProbe.swift`
- `ChatGPTClient/SettingsViewController.swift`
- `ChatGPTClient/Testing/SimulatorFixtureTransport.swift`
- `ChatGPTClientTests/ConversationRepositorySimulatorTests.swift`
- `fixtures/protocol/stop-request-ack-v1.json`
- `scripts/protocol_capture/README.md`
- `scripts/protocol_capture/sanitize_capture.py`
- this selected checkpoint and durable project documentation updates.

The seed Stop fixture contains only the already Runtime-proven official Web contract: `POST /backend-api/stop_conversation`, capture-local conversation alias, empty `exclude_async_types`, HTTP200 JSON `status=ok`, `last_message_id=null`. It intentionally invents no post-Stop Detail semantics.

## Batch recovery point — durable docs + stacked PR

- **Known branch head before batch**: `3abb06889902cd96b8fca45d7d50fec6bdcf237d`; cleaned Push Simulator CI green at `37978621723 / 113983154439` with Artifact `11639784911`.
- **Known parent/base**: `dev/send-stream-20260829@79107c64347e05e0dfd4f679a3c970dfa09a18b0`, PR #29 open/mergeable; no parent advancement observed.
- **Batch E1 — current write completed**: checkpoint now records cleanup + current-head CI and authorizes only documentation synchronization next.
- **Batch E2 — pending**: prepend durable authenticated-capture evidence/contract sections to `PROJECT_STATE.md`, `MODULE_STATUS.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_SPECIFIC_RULES.md`, and `BUILD_TEST_INDEX.md`. Do not change product/source code or any other task checkpoint.
- **Batch E3 — pending**: verify branch/parent again, then open one stacked PR from `dev/authenticated-protocol-capture-20261009` to `dev/send-stream-20260829`; run/inspect PR Simulator CI on the merge ref.
- **Batch D real-device package — conditional only**: after PR CI, decide whether a task-owned physical-device IPA is required to validate Start -> capture -> Stop -> Export on logged-in iPhone. If required, perform fresh candidate-conflict guard before allocating any build. Otherwise keep inherited Build115/b115 untouched.
- **Recovery rule**: never modify/delete `DEV-send-stream`, `DEV-send-stream-round7-runtime-addendum`, `DEV-simulator-test-baseline` or `DEV-message-rendering` checkpoints from this task. If interrupted, compare branch head and the five durable docs before replaying only missing E2/E3 writes.

## Evidence ladder

**Code written / static sanitizer + exact-scope checks passed / strict replay correction passed / privacy path hardening passed / cleaned current-head Simulator CI passed / Simulator evidence Artifact produced / stacked PR pending / formal IPA none / real-device authenticated capture not tested / sanitized real post-Stop Detail fixture not yet produced / Stable-Frozen No.**

## Next exact action

Synchronize the five durable project docs from the cleaned current-head evidence, then open the stacked PR to `dev/send-stream-20260829` and classify its merge-ref Simulator CI. Do not allocate b116.