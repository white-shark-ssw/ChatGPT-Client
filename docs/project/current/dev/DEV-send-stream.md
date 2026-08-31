# DEV-send-stream

## Status

**Active — exact b69 ordered reasoning/tool timeline Candidate is Code/CI/Artifact/package verified and is now at the human iPhone/iOS17 Runtime gate. b67 remains the accepted production existing-conversation transport Runtime predecessor. b68 is a valid reserved Artifact whose flattened presentation was superseded before Runtime by the user-supplied official-app recording. b69 preserves one assistant-turn chronology `思考 -> 工具 -> 再思考 -> 再工具 ... -> final` in one Repository-owned ordered timeline while keeping covered-Web transport/SSE/auth boundaries unchanged. Stable/Frozen Send remains No. PR #29 stays open / mergeable / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — keep open / evidence-only / unmerged
- Exact b69 product/config source: `5e9c2183483094304f7eaeecf4ffc7ad8e65b902`
- Current actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Stable merged predecessor: b38
- Latest accepted production Runtime pass: b67
- Latest emitted Candidate: b69 — CI/Artifact/package verified; Runtime pending
- b39-b69 identities are permanently reserved.

## Exact b67 accepted production transport identity

- Candidate: `DEV-send-stream-0.1.0-b67`
- Version / Build: `0.1.0 (67)`
- Exact product/config source: `52ab38f16fe914ef8316bb1dc712b77c2c87a271`
- Product tree: `dcd492d142bf0035208b8466ff02b6ae7209193c`
- Push Run / Job: `33338865423 / 99330666394` — success
- PR Run / Job: `33338868896 / 99330678769` — success
- Push Artifact: `9739891865`
- IPA SHA: `3712dec92cddfe64e84fc797e1506d83231cd878633b932b9acf0e7381795497`
- Runtime export: `ChatGPTClient-Diagnostics-20260831-052810.json`
- Device: iPhone / iOS17.0

Accepted b67 Runtime proved one local Send -> one submitted event -> one real protected Send -> HTTP200 SSE -> Repository-owned reasoning/tool/final updates -> terminal -> one authoritative reconciliation. No transport/SSE correction is justified by the current presentation request.

## Exact b68 identity — valid package, presentation superseded before Runtime

- Candidate: `DEV-send-stream-0.1.0-b68`
- Version / Build: `0.1.0 (68)`
- Exact product/config source: `269d9530223f2ed59dbd06c5b14dc87fce7a742f`
- Product assembly parent: `745de68faf15b330c9afec0d84da855e036df91a`
- Product-only assembly commit: `a510b31e185659b93477b2e9695fec4233176135`
- Push Run / Job: `33364874077 / 99403338734` — success
- PR Run / Job: `33364879111 / 99403353153` — success
- Push Artifact: `9747954069`
- Artifact ZIP digest: `sha256:dfe3282aee3f36aa6acbc835c7e8f1230a46a8b746f40d04edce875579e3a43f`
- IPA: `ChatGPTClient-0.1.0-b68-dev-send-stream.ipa`
- IPA SHA: `d6f81953a07f29c43e755547b344276b1e503864664325d96d16e07dd9ebcf73`
- Build log source marker: `269d9530223f`
- Runtime: not accepted / not needed as the next gate because a concrete presentation mismatch was established from the user’s official-app recording before Runtime handoff.

b68 is permanently reserved. Never rebuild corrected code as b68.

Audited b68 product range changed only the authorized presentation/config surfaces and did not intentionally modify accepted b67 covered-Web route, composer selectors, browser challenge, protected Send, response SSE grammar, auth ownership, or response lifecycle authority.

## User recording — current official interaction requirement

The user supplied `RPReplay_Final1788158459.mp4` and explicitly requires the Native conversation to match the official response sequence within one assistant turn:

`思考段 -> 工具段 -> 新思考段 -> 新工具段 -> ... -> final`

The recording is treated as current user/runtime UI evidence. The important invariant is chronological interleaving, not merely styling. A tool invocation separates reasoning phases; later reasoning must render after that tool rather than being concatenated before every tool.

### Confirmed b68 mismatch

Current exact b68 source stores live response presentation as:

- one cumulative `reasoningText: String`;
- one separate `tools: [ConversationLiveTool]` sorted by slot;
- one `finalText`.

`ConversationDetailViewController.rebuildLiveResponsePresentation` then creates one `reasoningSummary` by appending all `reasoningText` first and all tool rows second. Therefore a real event sequence `reasoning A -> tool 1 -> reasoning B -> tool 2` is rendered as `reasoning A+B -> tool 1 -> tool 2`, which contradicts the supplied official recording.

The existing covered-Web bridge already emits sufficient ordered signals: `reasoningPreamble(segmentStart:)`, `reasoningDelta`, `toolActivity(slot:title:completed:)`, `reasoningEnded`, and final deltas are delivered in event order. No selector/SSE/Web-rule change is needed.

## b69 evidence-backed design boundary

### Single response owner / ordered timeline

`ConversationRepository` remains the sole response owner. Replace the flattened live `reasoningText + tools[]` representation with one response-local ordered timeline value inside the existing Repository snapshot; do not add a second response store.

Each timeline item is presentation/state data of one of these evidenced kinds:

- visible reasoning text segment;
- tool activity segment with existing local slot/title/completed fields.

Mutation rules:

1. `reasoningPreamble`: append to the current last reasoning item unless `segmentStart` or the previous timeline item is a tool; then create a new reasoning item.
2. `reasoningDelta`: append to the last item only when that item is reasoning; if the previous item is a tool, create a new reasoning item. This preserves `tool -> reasoning` even when no new preamble precedes the delta.
3. first `toolActivity` for a slot appends a tool item at the current event position; completion updates that same existing item in place by slot and never reorders the timeline.
4. `reasoningEnded` remains the only exact reasoning->final phase authority.
5. final text remains separate authoritative visible final text and keeps existing incremental chunk presentation.
6. terminal non-reasoning promotion remains deterministic classification only; it must not duplicate reasoning text around tool segments.
7. diagnostics derive only counts/character lengths from the ordered timeline; never export reasoning/tool bodies.

### Native conversation presentation

Keep the existing outer `思考过程` disclosure semantics, but when expanded its body must render timeline items in chronological order, visually distinguishing tool rows from reasoning text. Do not introduce self-sizing giant cells or a second UIKit message hierarchy; preserve b38 deterministic/manual geometry by deriving measurement and layout from the same ordered presentation content.

Expected visible behavior for the user’s example:

`思考 A`  
`工具 1 · 调用中/已完成`  
`思考 B`  
`工具 2 · 调用中/已完成`  
`...`  
then final answer.

While reasoning is active, the disclosure may remain expanded as b68 intended; after exact `reasoningEnded`, it collapses unless explicitly expanded by the user.

### Historical authoritative Detail

After terminal reconciliation/reload, do not lose the interleaving merely because live snapshot disappears. Extend the existing branch projection only with evidenced shapes:

- service-marked visible thinking preambles become reasoning timeline items;
- completed assistant tool invocations already evidenced by the current parser/tool rules become tool timeline items in branch order;
- exact-parent tool results may mark that existing tool item completed in place;
- completed `reasoning_recap` remains a safe reasoning fallback when no already-collected visible reasoning segment exists;
- attach the pending ordered timeline to the next eligible visible assistant final in the same user turn;
- crossing a user message clears pending timeline/transient parent mapping;
- `assistant:thoughts` and `inline_cot_expandable_content` stay strictly non-presentational;
- raw service IDs used transiently for exact-parent association are not persisted/exported.

Do not generalize raw connector input/output disclosure beyond already-evidenced GitHub detail rules.

## TD-029 production authority retained

`Native send action -> ConversationRepository response operation -> covered official Web verified composer/page-owned protected Send -> same-response SSE -> Repository ordered response state -> Native conversation presentation`.

- official page owns browser challenge + protected request execution;
- `ConversationRepository` is sole production conversation/response owner;
- `AuthSessionStore` remains auth/account owner;
- `WKWebsiteDataStore.default()` remains sole persistent auth-secret authority;
- full Web conversation rendering remains rejected;
- Sync/Reload never resend;
- `WEB_SEND_ADAPTER.md` remains Web-rule authority;
- no timer/debounce/polling/retry/watchdog/fallback/compatibility shim;
- `assistant:thoughts` remains non-presentational.

## Batch recovery point — b69 ordered timeline

Verified baseline before product assembly:

- formal branch head: `b47242cc7d856eefda9a6fdfaf1584efca380fb5` before this checkpoint commit;
- exact product predecessor: b68 source `269d9530223f2ed59dbd06c5b14dc87fce7a742f`;
- b68 Artifact `9747954069` and IPA SHA `d6f81953...ebcf73` are valid and permanently reserved;
- actual main: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`;
- PR #29 open / mergeable / unmerged;
- only Active development checkpoint is this Work;
- repository search found no existing `DEV-send-stream-0.1.0-b69` identity.

Intended coherent write batches:

1. create a tooling-only b69 assembly ref from the new formal checkpoint head;
2. modify only `ChatGPTClient/RootViewController.swift`, `ChatGPTClient/Conversation/ConversationFeature.swift`, and Xcode b69 identity as required for the ordered Repository timeline; do not modify the covered-Web bridge parser/selector/SSE rule body;
3. update `.github/workflows/ios-foundation.yml` to b69 identity on the assembly ref;
4. audit exact detached diff against the checkpoint head and verify no transport/auth/b38 quick-navigation scope drift;
5. re-check branch/PR/main/other Active tasks, then fast-forward the formal Work branch once to the coherent b69 source;
6. continue through Push + PR CI, unique Artifact/package identity verification;
7. update checkpoint + BUILD_TEST_INDEX / PROJECT_STATE / MODULE_STATUS / PROJECT_PROFILE / technical/product rules and PR with actual evidence;
8. stop only at the exact b69 iPhone/iOS17 Runtime gate requiring a response that naturally executes at least `reasoning -> tool -> reasoning -> tool -> final`.

Recovery must not touch or rewrite b68 source/artifact identity, accepted b67 transport logic, final Composer/attachments, auth/default WebKit ownership, b38 quick-navigation algorithm, or Web selector/challenge/SSE grammar.

## Exact b69 identity — ordered reasoning/tool timeline Runtime candidate

- Candidate: `DEV-send-stream-0.1.0-b69`; Version / Build: `0.1.0 (69)`.
- Exact product/config source: `5e9c2183483094304f7eaeecf4ffc7ad8e65b902`; product commit `905ac2633a408cf571d25ccfe427bdd1a9a27f34`; checkpoint base `33022dc8c9fdcb17f5b462a2766ac86238417c58`.
- Push Run / Job: `33366226539 / 99407331552` — success; PR Run / Job: `33366229125 / 99407340011` — success.
- Push Artifact: `9748400171`; ZIP `sha256:b1d91179c47822a7a42bf5405ef4bbd7240b97ddff58743a8a12e5f16fb232f1`.
- IPA: `ChatGPTClient-0.1.0-b69-dev-send-stream.ipa`; IPA SHA `0c06256dc90aed86c706f8c72950528f61afa7f7fcdb504b2604d40befe3b0aa`.
- Independently inspected built `Info.plist`: Release `0.1.0`, Build `69`, Candidate b69, `DiagnosticsSourceCommit=5e9c21834830`, minimum iOS14.
- Compile note: one non-blocking unused local `index` warning; valid Artifact exists, so b69 is permanently reserved and is not rewritten merely for that warning.
- Runtime: pending on primary iPhone/iOS17 device.

b69 keeps one Repository-owned ordered response timeline. First tool activity appends at its event position; completion updates that item in place by slot; reasoning after a tool creates a new reasoning segment; exact `reasoning_ended` still owns reasoning->final; final text stays separate/incremental. Authoritative Detail reconstructs supported visible thinking/tool order while `assistant:thoughts` / `inline_cot_expandable_content` remain hidden. Covered-Web route/selectors/challenge/protected-Send/SSE grammar were not intentionally modified.

### Exact b69 Runtime gate

Install exact b69 and run one real request that naturally yields at least `reasoning A -> tool 1 -> reasoning B -> tool 2 -> final`. Accept only if live ordering is chronological, tool completion updates in place, later reasoning stays below the preceding tool, reasoning-end collapses into incremental final, authoritative reconciliation preserves the supported historical order, hidden thoughts stay absent, and the old floating overlay does not return. Export diagnostics after terminal.

## Evidence ladder now

- b67: production existing-conversation Send/stream/terminal/reconcile Runtime passed.
- b68: Code/diff/Push+PR CI/Artifact/package verified; Runtime not accepted; flattened presentation superseded by explicit official-flow evidence.
- b69: Code written / detached diff audited / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Runtime pending.
- Stable/Frozen Send: No.

## Next exact action

Human-only Runtime gate: install exact `DEV-send-stream-0.1.0-b69` / Build69 / source marker `5e9c21834830` on the primary iPhone/iOS17 device, clear diagnostics, execute one real request that naturally yields at least `reasoning -> tool -> reasoning -> tool -> final`, verify chronological interleaving plus in-place tool completion and post-terminal historical preservation, then export diagnostics. Do not allocate b70 unless that exact Runtime produces a concrete defect/evidence need.
