# Project-Specific Rules

This file contains durable repository/product rules backed by explicit requirements, current source, accepted tests or technical decisions. Detailed historical evidence belongs in the build/test index and runtime-evidence files; current rules below take precedence over stale historical wording.

## Product and architecture contracts

- Product goal remains a native iOS ChatGPT client shell/read experience distributed primarily as a TrollStore IPA.
- Stable merged native baselines remain b9 read, b15 recovery, b21 multi-conversation state, b23 list-cache core and b38 conversation metadata/settings/round navigation for their recorded scopes. Stable does not mean Frozen.
- Exact Stable Phase 8 tested source is `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Exact b42 Runtime proves successful ChatGPT-account protected Send depends on browser challenge output. Pure-native/transient-auth protected Send remains blocked.
- The separately billed API-product route remains rejected unless that explicit product decision changes. Primary-account Sub2API/Codex-subscription Runtime remains blocked by the account-safety gate.
- TD-024 permits only the recorded user-visible official-Web protected-Send surface; TD-025 rejects b44's full-page Native→Web→Native product form; TD-028 records that full existing-conversation Web rendering is not an accepted daily-chat dependency after the long-answer composer failure.
- b48-b65 are isolated diagnostic exceptions only. Their success does not approve the diagnostic Web Send-engine architecture as production architecture and does not transfer production response ownership.
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
- b59 Runtime authorizes consuming **only** that exact service-marked thinking-preamble shape into the same Native reasoning stream. The tested turn contained two such preambles before one reasoning-end marker and no leading truncation.
- b59 also proves a safe explicit `metadata.reasoning_status=is_reasoning` token can occur after tool activity before a later thinking preamble. This token may drive reasoning-active presentation; the associated `assistant:thoughts` body remains non-presentational.
- b60 Runtime confirms the bounded event-driven presentation and the exact tested tool association rule: when completed result metadata `parent_id` exactly equals an invocation service message ID observed in the same response stream, that invocation/result pair is associated. Raw IDs remain transient and unlogged.
- Adjacency, completed-count alignment, author/tool-name equality, recipient equality or presentation order are **not** accepted invocation→result pairing rules.
- b61 Runtime confirms the tested parent-paired Native tool lifecycle and separately captures generic-`textarea` false readiness / false-submitted behavior.
- Exact b62 removes generic `textarea:not([disabled])` from composer authority. The only currently accepted diagnostic composer identities are `#prompt-textarea` and explicit `[contenteditable="true"][role="textbox"]`.
- Do not add retry, timer, watchdog, polling, delayed auto-submit or alternative composer fallback merely to mask composer readiness. If the official composer is not evidenced yet, Native Send must remain not-ready.
- A successful submitted diagnostic turn must be grounded by the actual protected-Send lifecycle (`sendObserved` and observed response), not by `submitResult=submitted` alone.
- Exact b62 Runtime passes that focused verified-composer gate for the tested cold-launch path.
- Exact b63 preserves b62 response behavior and may inspect only bounded connector-payload JSON top-level structure plus aggregate `inline_cot_expandable_content.source_message_ids` associations for evidence. It does not expose values/body/IDs by diagnostics alone.
- Exact b63 same-run Runtime plus official-Web expanded-detail evidence establishes one narrow user-visible mapping for the GitHub connector family: the invocation's string-valued `metadata.connector_tool_payload` is the visible `工具输入`, and the exact parent-paired completed GitHub result's `message.content` is the visible `工具输出`.
- That b63 mapping is scoped to exact response-local `parent_id` association and result evidence that `invoked_resource.app_name == GitHub`; it does not authorize adjacency/count/name pairing, unmatched results, unrelated connector families, or `assistant:thoughts`.
- Exact b64 implements only that mapping. b64 Runtime confirms real protected Send, complete-looking reasoning/final, exact-parent row completion, 26 detail-capable rows and successful expand/collapse. Runtime rejects only detail formatting/density: outer `message.content` JSON pretty-print leaves nested strings escaped and opens both sections at once.
- Exact b65 is presentation-only: preserve the b64 transport/parser/reasoning/association/data-authorization behavior; after a tool row opens, present `工具输入` and `工具输出` as independent second-level disclosures, both collapsed by default. Input remains pretty JSON; output decodes the authorized outer result-content JSON into readable dictionaries/arrays and actual string text. A string containing one complete JSON object/array may be decoded one additional structural layer.
- b65 must not add arbitrary character truncation merely to reduce density. Collapse/hierarchy is the accepted density control. It must not silently omit authorized paired result content.
- If a turn reaches terminal with no exact reasoning-end marker, provisional pre-marker accepted text may be promoted into ordinary final-answer presentation so non-reasoning turns are not permanently misclassified. This is deterministic terminal classification, not retry/timer/watchdog behavior.
- Do not generalize arbitrary `v:string`, arbitrary initial assistant `parts` or arbitrary structural frames into assistant text. Parser changes require exact structural/runtime evidence.

## User-visible reasoning and tool contract

- User-visible reasoning, reasoning→final transition, thinking-state presentation, tool activity and verified tool-detail semantics remain part of `DEV-send-stream`; do not create a separate Work merely for these presentation details.
- Only service data explicitly intended for the user may enter Native presentation. Internal reasoning structures, system/internal nodes and unverified raw connector/tool payloads must not be exposed.
- `assistant:thoughts` remains explicitly non-presentational. A safe enum such as `reasoning_status=is_reasoning` may be consumed as state only when its meaning is evidenced; it does not authorize the thoughts body.
- Exact b55/b56 authorizes `reasoning_ended` as the current phase marker; it does **not** authorize recap text as the reasoning body.
- Exact b57-b60 authorize presenting accepted visible assistant text before that marker as `思考过程`, including exact service-marked thinking preambles; accepted text after it is final answer.
- A later exact service-marked thinking preamble starts a distinct visible reasoning segment. Native presentation may insert a local paragraph separator before such a later segment when prior reasoning text exists; that separator is not service text and must not alter source character metrics.
- `思考过程` may be visible/expanded while active and collapse on exact reasoning end; explicit user expand/collapse after completion is permitted.
- Reasoning→final transition must occur exactly once from protocol/state evidence, not elapsed time, DOM text, cell redraw or UI title.
- Initial `正在思考` may be shown as deterministic response-lifecycle state only after protected response acceptance/active state and before visible reasoning arrives. It must not be timer-based.
- An explicit service `reasoning_status=is_reasoning` may return presentation to `正在思考` after tool activity in the evidenced scope.
- Exact b60 authorizes transient result `parent_id` matching to update the corresponding invocation presentation, provided raw service IDs never cross into Native/logged state.
- Local tool slots are presentation bookkeeping only, not a second message/repository authority.
- An unmatched result must not be force-paired by count/order/adjacency/title/name. b64 Runtime observed 5 unmatched results while 30 exact matches updated their rows; this preserves the association rule.
- A matched result may refine a generic tool label only with the already-authorized bounded `reasoning_title`.
- GitHub expandable input/output is authorized only by the b63 same-run Runtime/Web mapping and exact b64 implementation scope. Do not generalize to other connectors/tool families until separately evidenced.
- b65 may organize that already-authorized GitHub detail into nested disclosures and readable hierarchy; it does not create a new content authority or broaden which service values are user-visible.
- `assistant:thoughts`, arbitrary unrelated tool bodies, unmatched result bodies and unverified invoked-resource values remain prohibited from Native presentation.
- The official-like target sequence is: `发送 -> 正在思考 -> 思考流式输出 -> 工具调用（可展开验证过的用户可见详情） -> 再次正在思考/思考流 -> ... -> reasoning_ended -> 自动折叠完整思考 -> 突出完整最终回答`.
- Matching evidenced interaction/state ordering is a product target. Exact pixel identity or support for every unverified tool-card subtype must not be claimed before Runtime evidence.

## Diagnostics contract

- Use existing `DiagnosticsLogger` authority.
- Exported diagnostics remain privacy-safe structural/aggregate evidence, not message-content archives.
- Do not persist prompt text, assistant answer text, reasoning text, tool title text, raw tool request/result/output, raw conversation/message identity, or browser challenge/auth values.
- Existing aggregate frame/patch/character/DOM counts remain permitted.
- b54+ may record bounded direct structural key names, safe recipient/author protocol tokens, content field names/counts/string lengths, direct metadata booleans and safe status/type-like enums where needed for exact evidence.
- Generic unique structure capacity remains 32; special reasoning/tool structure capacity remains 24 with independent count/overflow.
- b57+ ordinary assistant-text phase structure capacity remains separately bounded to 12 unique shapes with count/overflow and must not record text values or unbounded arrays.
- b58+ may record aggregate invocation/result/title/presentation counts; b59+ may record thinking-preamble count/characters.
- Exact b60+ may record aggregate reasoning-active signals, Native-only segment breaks and tool parent/reference match/missing counts after transient in-memory comparison; raw compared identities/bodies stay unexported.
- Exact b61-b65 may record bounded shape descriptors for detail metadata plus local non-secret presentation slot numbers and aggregate paired-completion/detail-presentation counts. b63 may additionally record its capped connector-payload top-level JSON fingerprint and aggregate inline-expandable source-reference matches.
- b64/b65 may retain authorized raw tool input/output only in response-local transient presentation state. Those values must never be copied into exported diagnostics; diagnostics may record only lengths, slots, disclosure state and aggregate counts.
- Composer diagnostics may record only the bounded strategy token and ready/submitted/send-observed lifecycle needed to distinguish false-ready Send from transport/stream failures; do not log DOM content.
- Background diagnostics may record lifecycle/public background-task/Web process/navigation failure classes without adding heartbeat timers merely to manufacture activity.
- Scroll/round diagnostics may record non-secret indices, offsets, geometry durations, travel distance and landing error, never message identity/body.

## Fast usable Candidate / identity contract

- Every testable Candidate has a unique build/Candidate/Artifact identity. Code / Static / CI / Artifact / Runtime / Stable are separate evidence levels.
- Once an Artifact identity is emitted, corrected product code must not reuse that identity.
- Actual built `Info.plist` version/build/Candidate/source marker plus IPA filename/SHA are package identity authority; workflow Artifact container naming alone is not proof.
- `scripts/build_ipa.sh` must fail on Candidate/version/build mismatch.
- Exact b24-b65 identities and emitted Artifacts are permanently reserved. Previously rejected identity-invalid transition/stale Artifacts remain rejected.
- Exact current Phase 9 diagnostic product/config authority is b65 source `44138db766d00e62cfda7f20182f6d20f1ec3352`; later docs-only commits do not redefine it.
- b65 package authority: Release `0.1.0 (65)`, Candidate `DEV-send-stream-0.1.0-b65`, Push Artifact `9736876465`, Push ZIP `sha256:d9a52ecb0cd7d5131e22fc399bc5db0d573a9de3e5d80838f3a8d2b3164ceb7a`, IPA SHA `e6a01b2eafd361b9df2567b002f9e8aa56b57dcee219c7999c65767b91138d16`, source marker `44138db766d0`, minimum iOS14, device family `[1,2]`, arm64. PR Artifact `9736874445` is a second successful exact-head package container.
- Exact b64 retains a Runtime partial-pass: verified composer / protected Send / reasoning-final / exact-parent GitHub detail lifecycle passed; escaped/dense detail presentation was the only accepted defect.
- Exact b65 has passed detached product diff audit, Push CI, PR CI, Artifact production and independent package identity verification; Runtime remains pending. CI/Artifact success does not prove the formatting defect is resolved on device.
- Build66 must not be allocated merely because b65 Artifact exists. Allocate b66 only after exact b65 Runtime yields a concrete product defect or next evidence need.

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
- Tooling-only assembly commits/refs are never Work/Candidate authority. Stable Phase 8 authority remains b38 source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; current Phase 9 diagnostic product/config authority is exact b65 source `44138db766d00e62cfda7f20182f6d20f1ec3352`.

## Critical invariants / prohibited routes

- Historical hidden WebView chat code is not the native product baseline.
- TD-024/TD-025/TD-028 remain in force while b48-b65 operate only as diagnostic exceptions.
- Full existing-conversation Web rendering is not a performance fix merely because it is hidden or display-trimmed.
- CI/Artifact success is never Runtime proof.
- Main-app background survival is never WebKit-stream survival proof.
- No speculative timers, watchdogs, retry loops, duplicate state owners, compatibility shims, alternate protocol endpoints or unrelated refactors without evidence.
- Stable does not mean Frozen; no Frozen business/architecture rules are currently recorded.

## Code style / naming constraints

Follow existing repository style and established APIs/names. Do not rename interfaces or variables without source-backed need. Keep concise statements on one line where natural.

## Rule maintenance

Only promote verified current facts or explicit requirements into durable rules. Temporary hypotheses belong to an Active checkpoint; completed Work keeps durable conclusions here and history in Git/index.
