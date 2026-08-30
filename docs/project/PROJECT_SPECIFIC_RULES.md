# Project-Specific Rules

This file contains durable repository/product rules backed by explicit requirements, current source, accepted tests or technical decisions. Detailed historical evidence belongs in the build/test index and runtime-evidence files; current rules below take precedence over stale historical wording.

## Product and architecture contracts

- Product goal remains a native iOS ChatGPT client shell/read experience distributed primarily as a TrollStore IPA.
- Stable merged native baselines remain b9 read, b15 recovery, b21 multi-conversation state, b23 list-cache core and b38 conversation metadata/settings/round navigation for their recorded scopes. Stable does not mean Frozen.
- Exact Stable Phase 8 tested source is `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Exact b42 Runtime proves successful ChatGPT-account protected Send depends on browser challenge output. Pure-native/transient-auth protected Send remains blocked.
- The separately billed API-product route remains rejected unless that explicit product decision changes. Primary-account Sub2API/Codex-subscription Runtime remains blocked by the account-safety gate.
- TD-024 permits only the recorded user-visible official-Web protected-Send surface; TD-025 rejects b44's full-page Native→Web→Native product form; TD-028 records that full existing-conversation Web rendering is not an accepted daily-chat dependency after the long-answer composer failure.
- b48-b62 are isolated diagnostic exceptions only. Their success does not approve the diagnostic Web Send-engine architecture as production architecture and does not transfer production response ownership.
- `ConversationRepository` remains sole native production conversation/list/detail/recovery/future accepted response authority.
- `AuthSessionStore` remains native auth/account authority.
- Default persistent `WKWebsiteDataStore` remains the only persistent auth-secret authority. Diagnostic Web uses that same store and does not create another persistent credential/challenge store.

## Send / stream diagnostic contract

- The official page owns login, browser challenges and protected `/backend-api/f/conversation` request construction. Diagnostic code must not synthesize or replay browser challenge material.
- Diagnostic dataflow may remain `Native composer -> page-owned official protected Send -> pre-React SSE interception -> Native diagnostic memory/UI`, without mutating production `ConversationRepository`.
- Do not continuously mirror Web DOM prompt/answer/reasoning state. Current diagnostics are SSE-structure based.
- b45 proves official no-resend continuation through `POST /backend-api/f/conversation/resume` with `{conversation_id, offset}` and HTTP200 SSE after a real interruption.
- b46/b47 prove only that duplicated-after-official-success Native Cookie+Bearer-only resume attempts returned HTTP404 JSON. Native first/exclusive resume remains Unknown / Unverified.
- Do not guess resume/handoff/turn-stream endpoints or browser request context.
- b48-b50 establish Native composer→official protected Send and compact `o/p/v` plus contextual `{v:string}` incremental text behavior.
- b51 Runtime confirms preserving active text continuation across exact top-level `title_generation` fixes the fresh-new-chat missing-middle defect.
- b52 Runtime confirms the tested final answer remained complete while visible reasoning beginning was slightly truncated; the root-nonexact/inactive-value hypothesis is rejected for that reproduction.
- b53 identifies separate `assistant:reasoning_recap`, `assistant:thoughts`, assistant code and tool result classes. Internal `assistant:thoughts` is not presentation data.
- b54 materially identifies assistant invocation→tool-result structure; generic structure observation can saturate and missing late structures must not be treated as protocol absence.
- b55 captures completed `assistant:reasoning_recap` with `reasoning_status=reasoning_ended` and `reasoning_recap_type=collapse` while `assistant:thoughts` remains separate.
- b56 Runtime corrects the recap interpretation: recap text itself was only a short status/description in the tested turn and is **not established as the real visible reasoning body**. The exact completed recap event remains an accepted explicit reasoning-phase end marker.
- b57 Runtime confirms already-accepted assistant text can be split at exact `reasoning_ended`: before-marker text enters Native `思考过程`, after-marker text remains final answer.
- b58 Runtime supersedes the earlier b57 no-prefix concern: side-by-side Native/Web evidence proves the omitted Native opening length exactly matched one service-marked `assistant:text:in_progress` string part with `metadata.is_thinking_preamble_message=true`.
- b59 Runtime authorizes consuming **only** that exact service-marked thinking-preamble shape into the same Native reasoning stream. The tested turn contained two such preambles (`2 / 13 chars`) before one reasoning-end marker and no leading truncation.
- b59 also proves a safe explicit `metadata.reasoning_status=is_reasoning` token can occur after tool activity before a later thinking preamble. This token may drive reasoning-active presentation; the associated `assistant:thoughts` body remains non-presentational.
- b60 Runtime confirms the bounded event-driven presentation: initial accepted-response state may present `正在思考`; later exact `reasoning_status=is_reasoning` may re-enter that state; a later service-marked thinking preamble may start a Native-only paragraph break; both tested turns completed with exact `reasoning_ended`, no fallback and no obvious user-observed truncation.
- b60 Runtime also confirms the tested tool association rule: when a completed result metadata `parent_id` exactly equals an invocation service message ID observed in the same response stream, that invocation/result pair is associated. Across two turns the match was `15/15` and `5/5`, with zero unmatched/missing. Raw IDs remain transient and unlogged.
- Adjacency, completed-count alignment, author/tool-name equality, recipient equality or presentation order are **not** accepted invocation→result pairing rules. In b60, author-name==invocation-recipient was only 14/15 and 3/5.
- b61 Runtime confirms the tested parent-paired Native tool lifecycle: in the successful tool-active run, 14 invocation identities and 14 results produced parent matches `14/14`, zero unmatched/missing, 14 Native tool presentations and 14 completion updates; the user observed rows advance `调用中 -> 已完成` and the reasoning/final path appeared complete.
- b61 Runtime also captures a separate Send-entry defect: on a cold/new-page run, an unqualified generic `textarea` was reported `ready`, Native submitted through it, and the page script reported `submitted` without any subsequent `sendObserved`, `sendResponse`, thinking presentation or SSE metrics. This is a false-ready / false-submitted composer defect, not a model/SSE stall.
- Exact b62 therefore removes generic `textarea:not([disabled])` from composer authority. The only currently accepted diagnostic composer identities are `#prompt-textarea` and explicit `[contenteditable="true"][role="textbox"]`.
- Do not add retry, timer, watchdog, polling, delayed auto-submit or alternative composer fallback merely to mask composer readiness. If the official composer is not evidenced yet, Native Send must remain not-ready.
- A successful submitted diagnostic turn must be grounded by the actual protected-Send lifecycle (`sendObserved` and the observed response), not by `submitResult=submitted` alone.
- Exact b62 Runtime passes that focused gate for the tested cold-launch path: composer remained `ready=false / strategy=none` until `prompt_textarea` appeared, submit used `prompt_textarea`, `submitted` was followed immediately by real `sendObserved`, HTTP200 SSE and a terminal response. This positive run is scoped evidence and does not prove the intermittent official-page race is impossible under every future state.
- If a turn reaches terminal with no exact reasoning-end marker, provisional pre-marker accepted text may be promoted into ordinary final-answer presentation so non-reasoning turns are not permanently misclassified. This is deterministic terminal classification, not retry/timer/watchdog behavior.
- Do not generalize arbitrary `v:string`, arbitrary initial assistant `parts` or arbitrary structural frames into assistant text. Parser changes require exact structural/runtime evidence.

## User-visible reasoning and tool contract

- User-visible reasoning, reasoning→final transition, thinking-state presentation, tool activity and verified tool-detail semantics remain part of `DEV-send-stream`; do not create a separate Work merely for these presentation details.
- Only service data explicitly intended for the user may enter Native presentation. Internal reasoning structures, system/internal nodes and unverified raw connector/tool payloads must not be exposed.
- `assistant:thoughts` remains explicitly non-presentational. A safe enum such as `reasoning_status=is_reasoning` may be consumed as state only when its meaning is evidenced; it does not authorize the thoughts body.
- Exact b55/b56 authorizes `reasoning_ended` as the current phase marker; it does **not** authorize recap text as the reasoning body.
- Exact b57-b60 authorize presenting the accepted visible assistant text before that marker as `思考过程`, including exact service-marked thinking preambles; accepted text after it is final answer. No additional hidden content becomes authorized by this split.
- A later exact service-marked thinking preamble starts a distinct visible reasoning segment. Native presentation may insert a local paragraph separator before such a later segment when prior reasoning text exists; that UI separator is not service text and must not alter source character metrics. b60 Runtime passed this tested presentation.
- `思考过程` may be visible/expanded while active and collapse on exact reasoning end; explicit user expand/collapse after completion is permitted.
- Reasoning→final transition must occur exactly once from protocol/state evidence, not elapsed time, DOM text, cell redraw or UI title.
- Initial `正在思考` may be shown as a deterministic response-lifecycle state only after the protected response is accepted/active and before visible reasoning arrives. It must not be timer-based or misrepresented as a literal service reasoning-status event unless that exact initial event is later proved.
- An explicit service `reasoning_status=is_reasoning` may return presentation to `正在思考` after tool activity in the evidenced scope.
- Exact b60 authorizes using transient result `parent_id` matching to update the corresponding invocation presentation, provided raw service IDs never cross into Native/logged state.
- b61 may assign local transient presentation slots to invocation identities and use an exact matched result only to update the correct row from an invocation state to a completed state. The local slot is presentation bookkeeping, not a second message/repository authority.
- Exact b61 Runtime accepts that row lifecycle for the tested successful turn; it does not prove every tool subtype or every future service shape.
- Exact b62 Runtime preserves and extends that tested evidence: 20 completed results all had parent references, all `20/20` matched observed invocation identities, zero were unmatched/missing, and Native produced `20` tool presentations with `20` completion updates. An extra observed invocation identity is not force-paired by count/order.
- A matched result may refine a generic tool label only with the already-authorized bounded `reasoning_title`; b61/b62 do **not** authorize raw tool request/result bodies.
- Expandable tool request/result detail remains a current `DEV-send-stream` target, but implementation must wait for evidence that a bounded field is actually intended for user-visible presentation. Field names alone are not authorization.
- b62 safe shape evidence includes string-shaped `connector_tool_payload`, bounded `reasoning_titles` / `tool_icons`, object-shaped `invoked_resource`, and `inline_cot_expandable_content` on an `assistant:thoughts` structure. These shapes remain non-presentational until exact evidence maps a field to official user-visible detail.
- `assistant:thoughts`, arbitrary raw tool bodies, connector payload values and unverified invoked-resource values remain prohibited from Native presentation.
- The official-like target sequence is: `发送 -> 正在思考 -> 思考流式输出 -> 工具调用（可展开验证过的用户可见详情） -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考 -> 突出完整最终回答`.
- Matching the evidenced interaction/state ordering is a product target. Exact pixel identity or support for every unverified tool-card subtype must not be claimed before Runtime evidence.

## Diagnostics contract

- Use existing `DiagnosticsLogger` authority.
- Exported diagnostics remain privacy-safe structural/aggregate evidence, not message-content archives.
- Do not persist prompt text, assistant answer text, reasoning text, tool title text, raw tool request/result/output, raw conversation/message identity, or browser challenge/auth values.
- Existing aggregate frame/patch/character/DOM counts remain permitted.
- b54+ may record bounded direct structural key names, safe recipient/author protocol tokens, content field names/counts/string lengths, direct metadata booleans and safe status/type-like enums where needed for exact evidence.
- Generic unique structure capacity remains 32; special reasoning/tool structure capacity remains 24 with independent count/overflow.
- b57+ ordinary assistant-text phase structure capacity remains separately bounded to 12 unique shapes with count/overflow and must not record text values or unbounded arrays.
- b58+ may record aggregate invocation/result/title/presentation counts. b59 may additionally record thinking-preamble count/characters. It must not log service title text or message IDs.
- Exact b60 may record aggregate reasoning-active signal counts, Native-only segment-break counts and tool parent/reference match/missing counts after transient in-memory comparison. It must not export the compared raw identities or bodies.
- Exact b61/b62 may additionally record bounded shape descriptors for candidate detail metadata: primitive type, direct object key/type list, array count/item direct keys/types, or string length. They must never log/display candidate values, nested payload bodies or raw IDs.
- b61/b62 may log local non-secret tool presentation slot numbers and aggregate paired-completion counts; local slots are ephemeral and reset per response.
- Composer diagnostics may record only the bounded strategy token and ready/submitted/send-observed lifecycle needed to distinguish false-ready Send from transport/stream failures; do not log DOM content.
- Background diagnostics may record lifecycle/public background-task/Web process/navigation failure classes without adding heartbeat timers merely to manufacture activity.
- Scroll/round diagnostics may record non-secret indices, offsets, geometry durations, travel distance and landing error, never message identity/body.

## Fast usable Candidate / identity contract

- Every testable Candidate has a unique build/Candidate/Artifact identity. Code / Static / CI / Artifact / Runtime / Stable are separate evidence levels.
- Once an Artifact identity is emitted, corrected product code must not reuse that identity.
- Actual built `Info.plist` version/build/Candidate/source marker plus IPA filename/SHA are package identity authority; workflow Artifact container naming alone is not proof.
- `scripts/build_ipa.sh` must fail on Candidate/version/build mismatch.
- Exact b24-b62 identities and emitted Artifacts are permanently reserved. Previously rejected identity-invalid transition/stale Artifacts remain rejected.
- Exact current Phase 9 diagnostic product/config authority is b62 source `e1b44f7ab6c47bd41de3ed9460ec0b77b7cc9f3f`; later docs-only commits do not redefine it.
- b62 package authority: Release `0.1.0 (62)`, Candidate `DEV-send-stream-0.1.0-b62`, Artifact `9733577825`, ZIP `sha256:d53ddb88c5d2092294592416e10e5a0a752cb7afb0bbe0a39c2c137d021082d0`, IPA SHA `ac9f031fb43b91ac12f486b1f743f741b404faf133725bdc8abec059b68b87d8`, source marker `e1b44f7ab6c4`, minimum iOS14, device family `[1,2]`, arm64.
- Exact b62 now has a focused Runtime pass for the tested verified-composer Send-entry / reasoning-final / parent-paired tool lifecycle gate. This does not promote it to Stable/Frozen or production ownership.
- Build63 must not be allocated merely because b62 passed. Allocate b63 only for one concrete unresolved evidence or implementation need after a fresh uniqueness/conflict guard. Current expandable-tool-detail field mapping is still Unknown / Unverified, so field names alone are not sufficient allocation grounds.

## Native UI / conversation presentation contracts

- Official ChatGPT iOS interaction is the default baseline where acceptable; use native UIKit/system behavior rather than inventing a second UI language.
- UI text/title is a consumer, never identity authority.
- `UISplitViewController`/native navigation remains compact list/detail navigation owner.
- Right-top list refresh and pull-to-refresh remain separate presentation sources over one repository refresh path. Do not reintroduce `navigationItem.prompt`, attributed refresh text or old offset compensation rejected by b27-b29 evidence.
- Round count/navigation consumes one derived `ConversationRoundProjection`; do not maintain a second mutable semantic round index.
- Each visible authoritative user message starts a round. Hidden/internal messages do not create ordinary rounds.
- `AppPreferences` remains the single persisted native settings owner. Current defaults remain: round count On, message time On, quick round navigation On.
- Message timestamps use authoritative historical time when available; omit rather than fabricate.
- Copy reads only authoritative user-visible message text and does not mutate message state or issue network requests.

## Long-conversation geometry / navigation contract

- Stable b37/b38 uses bounded display chunks plus deterministic derived row geometry/manual cell layout. `ConversationMessagePresentationProjection` is ephemeral presentation state only, not a second persistent message store.
- Copy still uses the full authoritative message even when display chunks are bounded.
- Do not restore one unbounded giant self-sized message row without new exact Runtime evidence.
- Stable b38 round navigation resolves the semantic target from derived O(1) prefix geometry and uses one cancellable `UIViewPropertyAnimator(duration: 0.35, curve: .easeInOut)` for continuous motion.
- Do not perform pre-jump teleport steps or use `scrollToRow` merely to discover target geometry.
- Rapid retargeting stops the current animator at its visual position and immediately starts toward the new semantic target. Real finger drag cancels programmatic ownership immediately. No debounce/wait gate.
- Physical top/bottom boundaries outrank drag delta, including rubber-band overscroll.
- Per-conversation native scroll presentation belongs to detail presentation, not `ConversationRepository`; use semantic message/chunk anchors rather than a single global raw offset.
- First visible presentation with no valid saved reading anchor shows latest/bottom without visibly animating through history.
- Sync/Reload may preserve an established anchor only while the same authoritative message remains; otherwise discard it explicitly.

## Manual recovery contract

- `同步最新消息` and `重载当前会话` are explicit authoritative `ConversationRepository` recovery actions and never resend/regenerate existing prompts.
- Preserve an already loaded detail on sync failure where applicable.
- A newer explicit same-target Sync/Reload cancels/replaces older target network ownership; generation/freshness rejects late callbacks. This is not a second store or retry chain.
- No automatic retry/watchdog/timer/resend/regenerate/fallback chain.
- b44 remains an important boundary: immediate Native Sync after visible-Web Send may lag assistant output already visible in Web. Do not turn this into automatic polling without a real readiness signal.

## Cold-start auth / list-cache contracts

- Default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority; native copied session context is transient.
- Native `/auth/login` is not an account-context prerequisite. Accepted sequence remains WebKit context -> `/api/auth/session` -> transient auth context -> accounts-check.
- b12 accepted public WebKit data-store warm-up for the tested persisted cold-start path.
- `ConversationRepository` remains sole list/conversation authority; `ConversationListCacheStore` is storage only.
- Persist only a small versioned account-scoped list summary snapshot and privacy-safe bookkeeping, never Detail/full-body data or copied auth secrets.
- Provisional cached rows cannot authorize Detail until current account scope is verified.
- Temporary auth transport failure may retain valid provisional rows without converting it into logout or automatic retry.
- Exact b23 accepts the 60-second rapid-relaunch window; manual refresh bypasses suppression and issues exactly one user-requested list refresh.
- Page-1 absence is not deletion evidence; preserve the accepted authoritative-total bound established through b23/b26.
- Do not add timer/polling/watchdog/retry, alternate endpoints, per-row Detail prefetch or another list/account authority solely for cache behavior.

## Message rendering / attachment boundary

- Current native ordinary message body remains plain string content. Markdown/code/table/link/citation presentation belongs to future `DEV-message-rendering` and must consume authoritative user-visible content only.
- Tool-card/reasoning lifecycle semantics remain current `DEV-send-stream`; do not defer their ownership merely because eventual card bodies may need rich rendering.
- Do not strip/rewrite raw Markdown or citation-adjacent markers without authoritative rich-content/annotation evidence.
- Attachment support remains high priority but Send-boundary dependent.
- Exact b43 Web `+` latency ~100–200ms was acceptable for its tested scope, but the Web Photos chooser filtered videos.
- Public WebKit upload-panel replacement is iOS18.4+, not the primary iOS17 target. Do not use private WebKit or DOM/file-input injection as the production iOS17 video-picker solution.

## Background / compatibility

- Background continuation follows `BACKGROUND_EXECUTION_PLAN.md`: no automatic prompt resend and no second response store/stream.
- Public `beginBackgroundTask` is a finite short-duration baseline only and must not be described as a long-duration guarantee.
- Main-app process survival does not prove WebContent/network/stream survival.
- b45 provides positive short-background/original-stream and official-recovery evidence; b49 also observed a long diagnostic response reaching terminal across background intervals. Full background acceptance waits for an accepted production response owner and its own Runtime matrix.
- Native iOS / TrollStore IPA; intended primary runtime iOS17; current minimum iOS14. Do not raise the minimum without concrete need.

## Repository governance contract

- Repository AI Governance Rules are dynamic authority.
- Every work session reads root `AGENTS.md`, then `docs/project/START_HERE.md`.
- Material source/CI/Artifact/Runtime/architecture/status changes update the current checkpoint and corresponding durable docs in the same work cycle.
- Current main may advance independently; exact Candidate evidence remains tied to its tested product source. Final merge must reconcile target-branch state without overwriting parallel work.
- Non-atomic GitHub write chains use the selected checkpoint recovery point and never blindly replay already-confirmed Candidate writes.
- Tooling-only assembly commits are never Work/Candidate authority. Stable Phase 8 authority remains b38 source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; current Phase 9 diagnostic product/config authority is exact b62 source `e1b44f7ab6c47bd41de3ed9460ec0b77b7cc9f3f`.

## Critical invariants / prohibited routes

- Historical hidden WebView chat code is not the native product baseline.
- TD-024/TD-025/TD-028 remain in force while b48-b62 operate only as diagnostic exceptions.
- Full existing-conversation Web rendering is not a performance fix merely because it is hidden or display-trimmed.
- CI/Artifact success is never Runtime proof.
- Main-app background survival is never WebKit-stream survival proof.
- No speculative timers, watchdogs, retry loops, duplicate state owners, compatibility shims, alternate protocol endpoints or unrelated refactors without evidence.
- Stable does not mean Frozen; no Frozen business/architecture rules are currently recorded.

## Code style / naming constraints

Follow existing repository style and established APIs/names. Do not rename interfaces or variables without source-backed need. Keep concise statements on one line where natural.

## Rule maintenance

Only promote verified current facts or explicit requirements into durable rules. Temporary hypotheses belong to an Active checkpoint; completed Work keeps durable conclusions here and history in Git/index.