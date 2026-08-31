# DEV-send-stream

## Status

**Active — exact b67 production existing-conversation Send/stream Runtime passed on the primary iPhone/iOS17 device. Exact b68 inline-presentation source passed Push + PR CI and produced a valid reserved Artifact, but before its Runtime gate the user supplied a current official ChatGPT recording that establishes a more precise required interaction: one assistant turn must preserve the event timeline `思考 -> 工具 -> 再思考 -> 再工具 ... -> final`, not flatten all reasoning first and all tools afterward. Current b68 source demonstrably flattens `reasoningText + tools[]`, so b68 is superseded for presentation without invalidating its package identity. b69 is authorized for the smallest Repository-owned ordered response-timeline correction. Stable/Frozen Send remains No. PR #29 stays open / mergeable / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — keep open / evidence-only / unmerged
- Current formal branch head before this checkpoint write: `b47242cc7d856eefda9a6fdfaf1584efca380fb5`
- Current actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Stable merged predecessor: b38
- Latest probe Runtime pass: b65
- Latest production Runtime pass: b67
- Latest emitted Candidate: b68 — CI/Artifact valid, Runtime not accepted
- Next authorized Candidate: b69 — ordered reasoning/tool timeline
- b39-b68 identities are permanently reserved.
- Future serialized `DEV-composer-parity` still owns final Composer hierarchy/drafts/attachment staging; this Work retains only the validation send trigger while response/reasoning/tool semantics are accepted.

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

## Evidence ladder now

- b67: Runtime passed for existing-conversation production Send/stream/terminal/reconcile scope.
- b68: Code written / diff audited / Push CI passed / PR CI passed / Artifact produced / package identity verified / Runtime not accepted / presentation superseded by newer explicit official-flow requirement.
- b69: authorized, not yet written.
- Stable/Frozen Send: No.

## Next exact action

Create the b69 tooling assembly ref from this checkpoint head, implement one Repository-owned ordered reasoning/tool timeline using only already-emitted event ordering, preserve b38 deterministic geometry and hidden-thought prohibition, audit the detached diff, then proceed autonomously through b69 CI/Artifact/package verification before asking for the human real-device Runtime gate.