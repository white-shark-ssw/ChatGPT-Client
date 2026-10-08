# DEV-authenticated-protocol-capture

## Status

**Active / stacked dependency on DEV-send-stream / implementation preflight**

- **Work ID**: `DEV-authenticated-protocol-capture`
- **Routing aliases / keywords**: `Authenticated Protocol Capture / 协议采集 / sanitized fixture / Simulator replay / 真机协议抓取`
- **Task**: Establish a reusable user-controlled authenticated protocol capture pipeline: real-device authenticated capture -> local sensitive diagnostic export -> deterministic sanitization/fixture generation -> PR #37 Simulator replay, without persisting reusable auth secrets or creating a second production authority.
- **User acceptance intent**: on a logged-in iPhone, normal workflow is `开发者诊断 -> 开始采集 -> 正常操作目标功能 -> 停止采集 -> 导出诊断包`; JavaScript instrumentation, when required, is injected/managed automatically by the diagnostic tool rather than manually pasted. Development consumes only sanitized fixtures for repeated macOS Simulator replay.
- **Parent dependency**: explicitly stacked on `DEV-send-stream` / PR #29 because it reuses the currently integrated PR #37 Simulator fixture seam and current protocol/WebKit diagnostics. Parent exact tree baseline is current `dev/send-stream-20260829@79107c64347e05e0dfd4f679a3c970dfa09a18b0`; this commit is tree-equivalent to prior `1a478af5e98f799d8bc06547c45ffef1f5340e32` after an accidental temporary cross-task checkpoint file was immediately deleted. Parent product remains exact Build115 / `DEV-send-stream-0.1.0-b115`; no b116 is allocated by creating this Work.
- **Branch / PR**: branch `dev/authenticated-protocol-capture-20261009`; PR will target `dev/send-stream-20260829` after first coherent implementation/CI state. Formal IPA Candidate: **not allocated yet**. Simulator/test identity to be allocated separately from product Candidate.
- **Current evidence reused**: `ProtocolReadProbe.swift` already contains auto-injected `WKUserScript` structural request/response/SSE observation for the visible official Web Send probe; `DiagnosticsLogger` already provides local redaction + export-time identifier hashing; Web Rule Lab uses the same default `WKWebsiteDataStore`; `AuthSessionStore` is auth/account authority and transient native auth consumer; integrated `SimulatorFixtureTransport` is Debug-only input seam with production `ConversationRepository`/`AuthSessionStore` ownership preserved.
- **Why separate Work**: requested scope crosses shared Protocol/Diagnostics/Settings/Authentication/Testing infrastructure and should not enlarge Send/Stream response implementation or overwrite b115 Runtime evidence. The new Work is a stacked infrastructure dependency whose first real scenario is the still-open DEV-send-stream post-Stop authoritative Detail semantic capture.
- **Security boundary**: raw authenticated capture stays local/user-controlled by default and is never auto-committed/uploaded. Repository/CI fixtures must be sanitized and contain no password, Cookie, Authorization, access/session token, reusable auth header or other credential. Conversation/message/account identifiers may only survive as capture-local stable irreversible pseudonyms when protocol correlation requires it.
- **State ownership boundary**: diagnostic capture observes existing official Web/native transport paths only. It must not become conversation/auth/response authority and must not add production retry/fallback/timer/watchdog/polling or duplicate state.
- **Initial implementation direction**: extract/reuse the existing protocol structural instrumentation into a dedicated diagnostic capture controller/store; use default WebKit store solely on user device; export a sensitive raw capture package locally; add an explicit sanitizer/fixture compiler that rejects secrets and produces deterministic sanitized fixture JSON; extend the integrated Debug `SimulatorFixtureTransport`/XCTest path to replay those fixtures without any real account/network.
- **Candidate rule**: do not allocate b116 merely because this infrastructure task exists. First run Simulator/static/CI on source changes. If and only if a real-device package is later required to exercise the new capture mode, allocate a unique Candidate under this Work after rechecking `BUILD_TEST_INDEX` and parent/parallel heads.

## New-task preflight

- `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Parent PR #29 remains open/mergeable; parent product is Build115 / Candidate b115.
- PR #37 is merged into parent at `657f70703d0076bd50ebda761f8dde8ba732e972`; integration-current Simulator evidence is green and available for reuse.
- Parallel PR #35 is research-only and declares no `ChatGPTClient/**` or product-Xcode changes; no direct product path overlap with this new task at preflight.
- Existing active `DEV-message-rendering` checkpoint is stale relative to its already-completed parent integration but its product scope is `ConversationFeature.swift` + Xcode identity; this task will not touch `ConversationFeature.swift` during capture infrastructure implementation.
- Existing `DEV-simulator-test-baseline` checkpoint remains its task owner's lifecycle; this task consumes its already-integrated seams but does not modify that checkpoint.
- Build/Test index shows b115 as latest formal Candidate and no allocated b116 entry. No candidate is reserved by this preflight.

## Batch recovery point — initial infrastructure implementation

- **Exact baseline**: branch created from parent `79107c64347e05e0dfd4f679a3c970dfa09a18b0`, Build115 / Candidate b115 unchanged.
- **Batch A — completed**: isolated branch created + this task checkpoint created. No product code/Candidate change.
- **Batch B — pending**: inspect exact code seams and add capture/sanitizer/fixture infrastructure with the smallest shared-owner changes; expected scope includes Protocol/Diagnostics/Settings/Testing/tests/Xcode only if proven necessary. No `ConversationFeature.swift`, Send/SSE owner, Stop product implementation, retry/fallback/timer/watchdog or b116 allocation.
- **Batch C — pending**: run `git diff --check` + integrated Simulator Preflight, fix only deterministic source/test issues, then open stacked PR to `dev/send-stream-20260829` once exact source scope is stable.
- **Batch D — conditional/pending**: only after Simulator/CI is green, decide whether a real-device capture IPA is required. If yes, re-run candidate conflict guard and allocate a unique task-owned Candidate before packaging. If no, leave product Candidate unchanged.
- **Recovery rule**: never write this checkpoint to the parent branch; never modify/delete `DEV-send-stream`, `DEV-simulator-test-baseline`, or `DEV-message-rendering` checkpoints from this task. Re-read actual branch/PR/head before replaying any pending batch.

**Next exact action:** implement Batch B. The first fixture scenario should encode the already-proven Stop request/ack contract and capture the official page's own post-Stop authoritative Detail response automatically, eliminating manual JS injection for that gate.