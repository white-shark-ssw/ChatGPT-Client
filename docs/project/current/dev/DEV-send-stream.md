# DEV-send-stream

## Status

**Active — exact b65 passed focused iPhone/iOS17 probe Runtime. TD-029 is current production Send architecture. The later rules-session plan `DEV-composer-parity` explicitly owns the final Native Composer UI (auto-growth/full-screen editor/draft/attachment staging/mode-effort controls). Current `DEV-send-stream` owns the reusable protected-Send/response/Stop lifecycle APIs, Repository response authority, minimal validation trigger, new-chat identity handoff, follow-tail/multi-conversation semantics, Web Rule Lab and final Send/Stream acceptance. Stable/Frozen Send remains No. PR #29 remains open / mergeable / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged
- Current formal branch head before this checkpoint update: `37175cb7b45a0e02821ff54a439709af08181755`
- Current formal branch tree before this checkpoint update: `40ab7c52d35634b7896f2676cee84e5d9bbee6e2`
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

## Tooling-only recovery note — no product/Candidate effect

During detached product preparation an empty root file `tmp_should_not_create` was accidentally created by a connector call at commit `53fc4245c87944362db0aaa07c863fd7d0e31d42`, then immediately deleted at `37175cb7b45a0e02821ff54a439709af08181755`.

Verified recovery facts:

- recovered tree is exact `40ab7c52d35634b7896f2676cee84e5d9bbee6e2`, identical to the pre-accident product/docs tree;
- no product source/config/workflow file changed in the recovered tree;
- no Candidate/build/Artifact identity was allocated or emitted;
- both commits are tooling-only history and must never be treated as product authority.

Recovery continues from the current checkpoint commit after this file update; never replay the accidental create/delete chain.

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

## Composer parity scope carve-out — current main authority

`main@d323b9ee...` contains `docs/project/COMPOSER_PARITY_PLAN.md`, target future Work ID `DEV-composer-parity`.

It explicitly serializes:

`DEV-send-stream -> DEV-composer-parity -> DEV-attachments -> ...`

Ownership split frozen for current development:

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

Current Work adds a development-only Lab:

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

1. add one process-resident covered official-Web executor using only b65-evidenced composer/protected-Send/SSE rules;
2. executor exact-targets `/c/<conversationID>` before Send and emits typed events only; it owns no response state;
3. add Repository-owned per-conversation response operation/state: preparing/thinking/reasoning/final/completed/failed plus response-local tool presentation bookkeeping;
4. detail/native validation UI consumes Repository live response state but preserves b38 history geometry; no final Composer implementation;
5. replace old full-page hybrid Send toolbar with a clearly temporary **validation trigger** (simple prompt/alert) that invokes Repository/executor APIs; it is deleted/replaced by future `DEV-composer-parity` and must not become a durable draft owner;
6. navigating A->B must not cancel A's covered-Web stream; b66 does not yet claim hidden-active memory-warning resident protection until the owner-internal resident-key patch is separately completed and validated;
7. unsafe Sync/Reload for the currently active response is disabled in validation presentation rather than guessed;
8. add Web Rule Lab in the same Candidate;
9. first slice does not guess new-chat or Stop behavior beyond already evidenced rules.

## Detached product preparation already completed

The following Git blobs were created but **have never been attached to the formal branch or any Candidate**:

- old prototype executor `14a8f114f08fe976ad247ff94707db826deeade7` — rejected before assembly because it observed the original SSE without reusing b65's filtered-response text-patch removal; do not use it;
- Web Rule Lab prototype `167fe806988a499ac8cdae6f57656085b40be0a3` — usable content, intended to be folded into an already-targeted source file to avoid unnecessary Xcode source-list churn;
- Repository response runtime prototype `414979dc527a0a4223bf79df84cf7b51b205e2a7` — usable design, intended to be folded into existing target source;
- live-response overlay prototype `de70050d2240e530e2076723f43c80f38f2cbf57` — validation-only presentation;
- Settings-with-Lab-entry prototype `931b5d4c945f2ae0a958b8db1cde3ac3881d31b4`.

Current assembly strategy is smaller: fold executor/runtime/overlay into existing `RootViewController.swift` and Lab into existing `SettingsViewController.swift`, avoiding new target source entries. The production executor must reuse the exact accepted b65 compact text grammar: exact `o/p/v`, contextual `v`, exact `title_generation` continuation, nested `/message/content/parts/0` scrubbing, reasoning preamble/active/end semantics and exact-parent tool association.

## Batch recovery point — b66 existing-chat production slice

Current baseline after the checkpoint update must be re-fetched before tree assembly.

Expected product/config files for the coherent detached tree:

- `ChatGPTClient/RootViewController.swift` — covered executor + Repository response runtime extension + validation overlay/orchestration; remove full-page Web as normal Send path;
- `ChatGPTClient/SettingsViewController.swift` — Web Rule Lab implementation + entry;
- Xcode project build/Candidate identity only after the product slice is coherent;
- workflow Artifact identity only when b66 is actually allocated.

Do not touch/reimplement:

- final Composer UI owned by future `DEV-composer-parity`;
- attachment staging/upload;
- b38 message geometry/round-navigation semantics;
- auth owner/default WebKit persistent-store contract;
- b39-b65 identities.

## Next exact action

Re-fetch this checkpoint's new head/tree. Create corrected combined Root/Settings detached blobs, statically audit against b65 grammar and state-owner invariants, then assemble a coherent detached product tree. Only then allocate b66 atomically with project/workflow identity, compare-audit, move formal branch once, continue through CI/Artifact/package verification, and stop at exact-device Runtime.