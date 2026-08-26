# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-27._

## Purpose

This is the durable implementation sequence for the iOS-native ChatGPT client. Current source, CI/artifact evidence, real-device evidence and specialized plans under `docs/project/` take priority over stale historical wording.

Current constraints: native UIKit iOS client; TrollStore IPA; intended primary runtime iPhone/iOS17; deployment target iOS14; current ChatGPT private/internal behavior must be evidenced rather than guessed.

## Delivery principles

1. Fast usable loop before breadth.
2. Diagnosability before complexity.
3. Authentication/session ownership before protocol assumptions.
4. One authoritative owner per identity/state domain.
5. Native model/state separate from mounted UI.
6. Official ChatGPT iOS interaction is the default visual/interaction baseline unless explicit requirements or runtime pain points justify deviation.
7. Core owner work is serial; edge work parallelizes only after conflict scanning.
8. Always distinguish Code, static checks, CI, Artifact, Runtime and Stable/Frozen evidence.
9. Do not add speculative retry, fallback, watchdog, duplicate state or compatibility machinery.

## Usability milestones

- **V0.1 read-use**: native shell + conversation list/detail/message rendering + manual sync/full reload + usable cold-start login-state recovery.
- **V0.2 chat-use**: V0.1 + stable multi-conversation state ownership + text send/new conversation + streaming + stop + user-visible reasoning interaction/haptics + recovery integration.
- **V0.3 daily-use refinement**: preferences/metadata, Markdown export, long-conversation tuning, attachments and remaining daily-use conversation features.

## Completed foundations

### Phase 1 — `DEV-app-foundation`
Completed / merged / Stable.

### Phase 2 — `DEV-auth-bootstrap`
Completed / merged / Stable for tested scope. Default persistent `WKWebsiteDataStore` is the sole persistent auth-secret authority; native auth consumption remains transient.

### Phase 3 — `DEV-protocol-read`
Completed / merged / Stable for accepted diagnostic read scope.

### Phase 4 — `DEV-native-read-path`
Completed / merged / Stable for tested b9 scope. `ConversationRepository` owns production conversation summaries/selected detail/current visible branch.

## Phase 5 — `DEV-conversation-recovery`

### Current status

**Active b15 test candidate. b14 compact startup/navigation is real-device accepted; b15 implements the remaining selected-detail replacement lifecycle correction and awaits Runtime validation.**

Runtime progression:

- b10: accepted core `同步最新消息` and full `重载当前会话`.
- b11: request paths worked, but navigation-bar prompt feedback was invisible and rejected.
- b12: centered sync feedback + public WebKit warm-up accepted; initial list still waited for lazy compact sidebar reveal.
- b13: immediate list initiation and stale-operation rejection accepted; compact startup/navigation failed; manual replacement requests overlapped an older selected-detail request and returned HTTP429.
- b14: `DEV-conversation-recovery-0.1.0-b14`, run `33000566633`, artifact `9618410313`, IPA SHA `b9100deb1d59b8ce22e15e72f766f0313be2903ec96ed2cda3d397986ba89182`. Exact b14 is real-device accepted: cold start reaches the conversation-list root, duplicate sidebar icons are gone, and native compact list/detail navigation works on iPhone/iOS17.
- b15: `DEV-conversation-recovery-0.1.0-b15`, `0.1.0 (15)`, product/config head `159e8ea4f7baf6cd890d1f9bbebeac41feefbf52`, run `33004536664` success, artifact `9619988065`, IPA SHA `b2b54905cff2b67604f95d44033efd6b4b98d319b311ac06204ddec359dd905e`. Code + static/source review + CI + Artifact complete; Runtime pending.

### Manual recovery contract

- `同步最新消息` uses authoritative selected conversation identity and existing detail path; never resend/regenerate.
- Success reconciles server-backed detail; failure preserves previously loaded detail when applicable.
- `重载当前会话` clears authoritative selected detail first, then performs one fresh server detail request.
- During an ordinary initial detail load, overflow sync/reload remains available for explicit recovery.
- Operation generation rejects older selected-detail completions once a newer operation owns the selected detail.
- Duplicate manual recovery taps are disabled only while the manual action itself is active.
- No automatic retry/watchdog/fallback/resend chain.

### b15 selected-detail replacement lifecycle

b13 supplied direct runtime evidence that freshness rejection alone was insufficient for the request lifecycle: an ordinary detail request stayed in flight while manual replacement requests started, and those replacements returned HTTP429 even though the later old result was safely discarded.

b15 makes the minimum owner-level correction:

1. `AuthTransientSession.dataTask(with:completion:)` returns the same already-created/resumed `URLSessionDataTask`; Authorization, cookies, endpoints and ephemeral transport semantics do not change.
2. `ConversationRepository` tracks the current selected-detail task plus the generation that owns it.
3. Ordinary detail loading behavior remains unchanged by default.
4. Explicit manual sync/reload increments the replacement generation first, cancels the older tracked selected-detail task, then starts one replacement detail request.
5. Intentional `NSURLErrorCancelled` is recorded as cancellation and is not surfaced to the obsolete UI operation.
6. Existing generation rejection remains as a second freshness safeguard for any late callback.
7. No retry, delay, timer, watchdog, fallback endpoint/header set, resend/regenerate or second state authority is added.

### b15 acceptance gate

Exact b15 on iPhone/iOS17 must prove:

- enter a conversation and, while ordinary `正在读取会话…` is still active, invoke exactly one manual sync or reload;
- diagnostics show `detail.cancel.requested` for the old generation and `detail.cancelled` for that obsolete task, followed by one replacement `detail.request`;
- the client does not intentionally leave the old and replacement selected-detail requests active concurrently;
- the replacement completes normally without reproducing the b13 overlap-driven HTTP429 in the tested case;
- centered sync feedback/full reload and the accepted b14 cold-start/list/detail navigation remain intact.

Only exact b15 real-device acceptance can close recovery. CI/Artifact alone are not Runtime proof.

### Accepted cold-start/navigation state

- Public default-WebKit warm-up is accepted for tested iPhone/iOS17 cold starts.
- Initial list loading begins after warm-up without requiring sidebar reveal.
- b14 starts compact on primary/list rather than blank detail.
- Native UISplitViewController/navigation is the sole compact list/detail navigation owner; no custom duplicate sidebar control.

## Phase 6 — `DEV-multi-conversation-state`

Starts **after recovery is accepted/merged**. Establish account-scoped per-conversation resident state/freshness before send/stream. See `docs/project/MULTI_CONVERSATION_STATE_PLAN.md`.

## Phase 7 — `DEV-conversation-round-count`

After multi-conversation state. Display `聊天 · N轮` / `工作 · N轮`; derive count from authoritative active-branch user messages; no second mutable counter or extra network request.

## Phase 8 — `DEV-send-stream`

After read/recovery/multi-conversation ownership is stable: evidence current text-send/new-conversation protocol, implement composer/stream/stop, bind response identity correctly under switching, and integrate manual recovery without automatic resend.

## Phase 9 — `DEV-markdown-export`

Export authoritative current user-visible branch to Markdown; never scrape mounted cells or expose hidden/internal reasoning/tool content.

## Phase 10 — `DEV-long-conversation`

Measure/improve parse/model/render timing, first-visible latency, mounted-view bounds, memory growth, scrolling/input latency and lifecycle behavior.

## Phase 11 — `DEV-attachments`

Add native photo/file/video attachment flows after text-chat ownership is stable; evidence current upload protocol before production implementation.

## Phase 12 — remaining daily-use features

Split into isolated Work IDs as dependencies stabilize: search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat, settings/diagnostics refinement and other evidenced daily-use capabilities.

## Phase 13 — advanced capabilities

Later candidates: Projects, web search, image/multimodal, Voice, Memory, Deep Research, GPTs and other current ChatGPT-specific capabilities.

## Current next action

Real-device test exact `DEV-conversation-recovery-0.1.0-b15` against the selected-detail cancellation/replacement gate. If accepted, record Runtime evidence, perform final main/PR/conflict checks, merge PR #10, complete recovery, then start `DEV-multi-conversation-state`.
