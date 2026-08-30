# DEV-send-stream

## Status

**Active — exact b65 passed focused iPhone/iOS17 probe Runtime. TD-029 is current production Send architecture. The later rules-session plan `DEV-composer-parity` now explicitly owns the final Native Composer UI (auto-growth/full-screen editor/draft/attachment staging/mode-effort controls). Current `DEV-send-stream` therefore owns only the reusable protected-Send/response/Stop lifecycle APIs, Repository response authority, minimal validation trigger, new-chat identity handoff, follow-tail/multi-conversation semantics, Web Rule Lab and final Send/Stream acceptance. Stable/Frozen Send remains No. PR #29 remains open / mergeable / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged
- Formal branch head before this checkpoint update: `4c94956b6be8eb87ad01563598ee3294eab74370`
- Current actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- `main` advanced materially in docs/rules since the old `1ac202c...` base. New product-source overlap has not been observed; final Candidate/merge must re-check/synchronize target state.
- Current `main` `docs/project/current/dev/` has no Active Composer checkpoint. `DEV-composer-parity` is a planned **future serialized Work**, not a parallel implementation branch/candidate.
- Stable native predecessor: b38
- Latest Runtime-tested Candidate: `DEV-send-stream-0.1.0-b65`
- Exact b65 product/config source: `44138db766d00e62cfda7f20182f6d20f1ec3352`
- b65 Push Artifact: `9736876465`
- b65 IPA SHA: `e6a01b2eafd361b9df2567b002f9e8aa56b57dcee219c7999c65767b91138d16`
- b39-b65 emitted identities are permanently reserved.
- b66 is **not emitted yet**. Allocate only after one coherent TD-029 existing-chat production/Web-Lab slice exists and product/build/workflow identity can move atomically.

## Exact b65 Runtime — accepted probe boundary

Export `ChatGPTClient-Diagnostics-20260830-191806.json` matched Release build65/source `44138db766d0` on iPhone/iOS17.0.

Observed path:

`ready=false/none -> ready=true/prompt_textarea -> nativeSubmit -> submitted -> sendObserved(existing_conversation) -> HTTP200 text/event-stream -> thinking/reasoning/tool/final -> terminal`.

Terminal: frameCount `132`, reasoning-end `1`, reasoning `14/295`, final `71/2827`, total `85/3122`, invocation/result `10/10`, parent present/matched/unmatched/missing `10/10/0/0`, tool presentation/completion `10/10`, detail-capable rows `9`. User observed no truncation; nested input/output disclosures worked. Minor spacing/slash-escape polish is non-blocking and belongs later presentation polish/Composer work rather than another probe Candidate.

## Current production authority — TD-029

Production conceptual path:

`Native send action -> ConversationRepository response operation -> covered official Web verified composer/page-owned protected Send -> same-response SSE -> Repository incremental response state -> Native consumers`.

Hard rules:

1. official page owns browser challenge + exactly one protected Send;
2. Native never solves/replays/persists challenge material;
3. covered Web owns no conversation/message/response/draft state;
4. `ConversationRepository` is sole production conversation/response owner;
5. one user Send -> exactly one protected Send; Sync/Reload never resend;
6. full Web conversation UI remains rejected;
7. current selectors/SSE semantics live in `WEB_SEND_ADAPTER.md`;
8. future Web changes are probed through the Web Rule Lab before changing production rules.

## Composer parity scope carve-out — new main authority

`main@d323b9ee...` contains `docs/project/COMPOSER_PARITY_PLAN.md`, target future Work ID `DEV-composer-parity`.

It explicitly serializes:

`DEV-send-stream -> DEV-composer-parity -> DEV-attachments -> ...`

Ownership split now frozen for current development:

### `DEV-send-stream` owns

- covered official-Web protected Send executor;
- Repository response operation/lifecycle;
- reasoning/final/tool event semantics;
- exact-parent tool association;
- existing-chat Send API and acceptance;
- pending->authoritative new-chat identity handoff;
- Stop protocol evidence + accepted Stop API/semantics;
- hidden A response / B selected isolation;
- follow-tail lifecycle contract and Sync/Reload safety;
- Web Rule Lab and Web adapter maintenance workflow;
- **minimal validation-only text trigger** needed to test these APIs before the final Composer exists.

### future `DEV-composer-parity` owns

- final bottom Composer hierarchy;
- dynamic multiline auto-growth;
- bounded inline max/full-screen editor;
- keyboard/layout animation;
- per-conversation draft UI;
- file/photo/video staging strip + previews;
- mode/reasoning-effort controls;
- final Send/Stop button presentation consuming the already-accepted Send/Stop APIs.

Current Work must not create a second durable draft/composer owner or implement those future UI behaviors.

## Web Rule Lab contract

Current Work still adds a development-only Lab:

- Settings entry;
- visible `WKWebView` using `WKWebsiteDataStore.default()`;
- temporary editable JS + explicit Execute;
- temporary result + copy/share;
- no auto-run;
- script/result bodies never persisted/logged;
- diagnostics only safe lifecycle/type/length;
- never production Send/response owner.

## Current source gap

- `RootViewController` still uses transitional `发送消息… -> AuthWebViewController.hybridChat -> return+Sync`.
- `ConversationRepository` has read/list/detail resident ownership but no response operation/lifecycle.
- `ConversationDetailViewController` is stable b38 history/geometry presentation and has no live response consumer.
- `NativeWebSendEngineProbe.swift` contains b65-proven Web rules but is diagnostic state owner only.
- `SettingsViewController` is the natural Lab entry.

## Product batch B — revised by Composer ownership

Smallest coherent b66 slice is **existing-conversation Send/stream production ownership + Lab**, without final Composer UI:

1. add `CoveredWebSendExecutor` (process-resident, default persistent WebKit store) using only b65-evidenced composer/protected-Send/SSE rules;
2. executor exact-targets `/c/<conversationID>` before Send and emits typed events only; it owns no response state;
3. add Repository-owned per-conversation response operation/state: preparing/thinking/reasoning/final/completed/failed plus response-local tool presentation bookkeeping;
4. active response protects that conversation resident from normal memory-warning eviction;
5. detail UI may consume/display Repository live response state but must preserve b38 history geometry; no final Composer implementation;
6. replace the old full-page hybrid Send toolbar with a clearly temporary **validation trigger** (e.g. simple prompt/alert) that invokes the Repository/executor API; this trigger is deleted/replaced by future `DEV-composer-parity` and must not become a durable draft owner;
7. navigating A->B does not cancel A;
8. unsafe Sync/Reload while a response is active may be explicitly disabled until semantics are accepted;
9. add Web Rule Lab in the same Candidate;
10. first slice does not guess new-chat or Stop behavior beyond already evidenced rules.

## Batch recovery point — b66 existing-chat production slice

Baseline for the next non-atomic product chain is this checkpoint commit after it lands.

Before product mutation, re-fetch the new branch head/tree. Expected product files may include:

- `ChatGPTClient/Protocol/CoveredWebSendExecutor.swift` — new reusable executor;
- `ChatGPTClient/Conversation/ConversationFeature.swift` — Repository response owner + live response consumer hooks;
- `ChatGPTClient/RootViewController.swift` — executor orchestration + validation trigger; remove full-page Web as normal Send path;
- `ChatGPTClient/SettingsViewController.swift` and/or `ChatGPTClient/Protocol/WebRuleLabViewController.swift` — Lab;
- Xcode project source list only if new Swift files are added;
- workflow/build identity only after the coherent slice is complete and b66 is actually allocated.

Do not touch/reimplement:

- final Composer UI owned by future `DEV-composer-parity`;
- attachment staging/upload;
- b38 message geometry/round-navigation semantics except minimal live-response integration;
- auth owner/default WebKit persistent-store contract;
- b39-b65 identities.

## Next exact action

Re-fetch this checkpoint's new commit/tree. Implement Web Rule Lab + reusable covered-Web executor + Repository-owned existing-chat Send/stream with a minimal validation trigger. Compare-audit product scope. Only when coherent, allocate b66 atomically with build/workflow identity, re-check `main@d323b9ee...` overlap before CI/Artifact, then continue autonomously through CI/package verification and stop at exact-device Runtime.