# DEV-send-stream

## Status

**Active — exact b67 production existing-conversation Send/stream Runtime passed on the primary iPhone/iOS17 device. b68 presentation-only source is now written and audited: the temporary floating live-response overlay is removed, Repository-owned response state is projected inline at the end of the Native conversation, and authoritative completed `reasoning_recap` data can be shown as a collapsible historical reasoning section without exposing hidden thoughts. Exact b68 product/config source `269d9530223f2ed59dbd06c5b14dc87fce7a742f` is in Push + PR CI. CI/Artifact/Runtime are not yet accepted. Stable/Frozen Send remains No. PR #29 remains open / mergeable / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — keep open / evidence-only / unmerged
- Current actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Formal branch product head before this checkpoint update: `269d9530223f2ed59dbd06c5b14dc87fce7a742f`
- Stable merged predecessor: b38
- Latest probe Runtime pass: b65
- Latest production Runtime pass: b67
- Current presentation candidate in CI: b68
- b39-b68 emitted identities are permanently reserved once a valid artifact exists; b39-b67 are already reserved.
- Future serialized `DEV-composer-parity` still owns final Composer hierarchy/drafts/attachment staging; this Work keeps only the validation send trigger while integrating response/reasoning presentation.

## Exact b67 identity

- Candidate: `DEV-send-stream-0.1.0-b67`
- Version / Build: `0.1.0 (67)`
- Exact product/config source: `52ab38f16fe914ef8316bb1dc712b77c2c87a271`
- Product tree: `dcd492d142bf0035208b8466ff02b6ae7209193c`
- Push Run / Job: `33338865423 / 99330666394` — success
- PR Run / Job: `33338868896 / 99330678769` — success
- Push Artifact: `9739891865`
- Artifact ZIP digest: `sha256:7e41508c76556466ab180009a30f36b5c12cbc731197d4213387698ed54d78c2`
- IPA SHA: `3712dec92cddfe64e84fc797e1506d83231cd878633b932b9acf0e7381795497`
- Runtime export: `ChatGPTClient-Diagnostics-20260831-052810.json`
- Device: iPhone / iOS17.0

b67 package identity is valid and permanently reserved.

## Exact b67 Runtime — accepted production existing-conversation transport gate

Generation 1:

`liveResponse.started -> composer_ready x2 -> submit_result=submitted x1 -> send_observed x1 -> HTTP200 text/event-stream -> accepted visible text -> terminal -> authoritative Sync 14→16 -> live snapshot cleared`

Generation 2, tool-active:

`liveResponse.started -> composer_ready x1 -> submit_result=submitted x1 -> send_observed x1 -> HTTP200 text/event-stream -> tool activity -> thinking_active -> exact reasoning_ended -> final deltas -> terminal -> authoritative Sync 16→18 -> live snapshot cleared`

Important evidence:

1. b66 duplicate-submit defect is closed for the tested production path: repeated ready callbacks did not create a second submitted event.
2. no `send_transport_error` occurred.
3. same-response SSE reached true terminal and the existing one-shot authoritative reconciliation succeeded.
4. generation 2 briefly crossed resign-active / become-active while still completing the same response. This is positive short-interval evidence only, not the later 5/15-minute background gate.
5. user visually confirmed Send, incremental response and final synchronization worked.

Classification: **Runtime passed for the current existing-conversation production Send/stream/terminal/reconcile gate; not Stable/Frozen and not yet a complete daily-chat UI.**

## User-confirmed presentation defect after b67

The temporary `ConversationLiveResponseOverlayView` visibly floats over the conversation. The user explicitly requires:

1. active assistant output must stream inline at the bottom of the current Native conversation, not in a floating popup/overlay;
2. historical assistant messages should expose a collapsible/expandable reasoning section where authoritative service data supports it.

This is within `DEV-send-stream` because it is response/reasoning lifecycle presentation, not final Composer work or general Markdown rendering.

## Exact b68 source — presentation-only integration

- Candidate: `DEV-send-stream-0.1.0-b68`
- Version / Build: `0.1.0 (68)`
- Exact product/config source: `269d9530223f2ed59dbd06c5b14dc87fce7a742f`
- Product assembly parent: `745de68faf15b330c9afec0d84da855e036df91a`
- Product-only assembly commit: `a510b31e185659b93477b2e9695fec4233176135`
- Identity/workflow commit: `269d9530223f2ed59dbd06c5b14dc87fce7a742f`
- Push Run / Job: `33364874077 / 99403338734` — in progress at checkpoint write
- PR Run / Job: `33364879111 / 99403353153` — in progress at checkpoint write
- Artifact: pending
- Runtime: pending

Audited detached range `745de68f...269d9530` changes exactly four authorized files:

1. `.github/workflows/ios-foundation.yml` — b68 candidate identity only;
2. `ChatGPTClient.xcodeproj/project.pbxproj` — Build 68 / b68 diagnostics candidate only;
3. `ChatGPTClient/Conversation/ConversationFeature.swift` — inline live-response projection, deterministic reasoning disclosure geometry, and narrow historical recap extraction;
4. `ChatGPTClient/RootViewController.swift` — remove floating response overlay and forward Repository live-response changes to Detail presentation.

No accepted b67 covered-Web route, selector, challenge, protected Send, response SSE grammar, auth ownership, or response lifecycle ownership was intentionally changed.

Evidence ladder at this checkpoint: **Code written / detached diff audited / formal source advanced / CI running / Artifact pending / Runtime pending / Stable-Frozen No.**

## b68 presentation behavior encoded

### Live response

- `ConversationRepository.liveResponse(for:)` remains the sole response state owner.
- `ConversationDetailViewController` derives presentation from that snapshot and does not own a second response lifecycle.
- the Root floating response overlay is removed.
- active assistant output is appended after authoritative history in the existing table and keeps the existing 1200-character presentation chunking.
- live reasoning text and tool status derive from the same Repository snapshot under one `思考过程` disclosure.
- reasoning is expanded while reasoning is active; after `reasoningEnded`, it is collapsed unless the user explicitly expands it.
- final text grows inline as SSE deltas update the Repository snapshot.
- automatic growth follows only when the table was already at the exact physical bottom (`maximumY - 0.5`); no new fuzzy threshold, timer, debounce, polling, retry, watchdog, fallback or compatibility shim was added.
- b38 historical message geometry remains separately cached; live deltas rebuild only the live presentation geometry.

### Historical reasoning

A separate `reasoningSummary` field is populated only from service-marked completed recap rows matching all of:

- assistant recipient `all`;
- message status `finished_successfully`;
- `content.content_type == reasoning_recap`;
- non-empty `content.content`;
- `metadata.reasoning_status == reasoning_ended`;
- `metadata.reasoning_recap_type == collapse`.

The recap is attached to the next eligible visible assistant response in the same turn and is cleared if a user message is crossed. Historical reasoning is collapsed by default. `assistant:thoughts` and `inline_cot_expandable_content` remain explicitly non-presentational.

## TD-029 production authority retained

`Native send action -> ConversationRepository response operation -> covered official Web verified composer/page-owned protected Send -> same-response SSE -> Repository incremental response state -> Native conversation presentation`.

- official page owns browser challenge + protected request execution;
- `ConversationRepository` is sole production conversation/response owner;
- `AuthSessionStore` remains auth/account owner;
- `WKWebsiteDataStore.default()` remains sole persistent auth-secret authority;
- full Web conversation rendering remains rejected;
- Sync/Reload never resend;
- `WEB_SEND_ADAPTER.md` remains the Web-rule maintenance authority;
- `assistant:thoughts` remains non-presentational.

## Assembly / recovery evidence — b68

- Resume Guard before assembly: formal branch / PR head `745de68faf15b330c9afec0d84da855e036df91a`, actual main `d323b9eed2dda75b9986fc06e14014d3e9b365fb`, PR #29 open/mergeable/unmerged, unique Active Work.
- tooling-only assembly attempts that failed before producing product source did not advance the formal branch.
- clean product ref `assembly/dev-send-stream-b68-product-20260831` was emitted from exact parent `745de68f...`.
- detached compare before formal advance proved exactly the four files listed above after candidate workflow identity was added.
- pre-advance Guard was repeated and passed; formal `dev/send-stream-20260829` was then fast-forwarded once to `269d9530...` without force.

Do not touch final Composer, attachments, auth ownership/default WebKit store, b38 quick-navigation algorithm, Web selector rules, challenge logic, or b39-b67 identities while resolving any b68 presentation CI/runtime issue.

## Next exact action

Read exact Push `33364874077 / 99403338734` and PR `33364879111 / 99403353153` results for source `269d9530223f2ed59dbd06c5b14dc87fce7a742f`. If either fails, fix only evidence-backed b68 presentation code. If both pass, verify the exact b68 Artifact/package identity, update project evidence/index/state/module/PR, then stop at the exact iPhone/iOS17 b68 Runtime/manual gate.