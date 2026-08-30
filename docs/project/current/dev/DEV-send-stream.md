# DEV-send-stream

## Status

**Active — exact b65 passed focused iPhone/iOS17 probe Runtime. TD-029 is current production Send architecture. Future `DEV-composer-parity` owns the final Native Composer UI. Current `DEV-send-stream` owns reusable protected-Send/response/Stop lifecycle APIs, Repository response authority, minimal validation trigger, new-chat identity handoff, follow-tail/multi-conversation semantics, Web Rule Lab and final Send/Stream acceptance. Stable/Frozen Send remains No. PR #29 remains open / mergeable / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged
- Current formal branch head before this checkpoint update: `b54c307333282af8f24631b653ffbd254f2e1de4`
- Current actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- `main` advanced in docs/rules only for the newly inspected Composer/attachment planning; no current product-source overlap has been observed. Final Candidate/merge must still re-check target state.
- `DEV-composer-parity` is a future serialized Work, not a parallel Active checkpoint/branch/Candidate.
- Stable native predecessor: b38
- Latest Runtime-tested Candidate: `DEV-send-stream-0.1.0-b65`
- Exact b65 product/config source: `44138db766d00e62cfda7f20182f6d20f1ec3352`
- b65 Push Artifact: `9736876465`
- b65 IPA SHA: `e6a01b2eafd361b9df2567b002f9e8aa56b57dcee219c7999c65767b91138d16`
- b39-b65 emitted identities are permanently reserved.
- b66 is **not emitted yet**. Allocate only after one coherent TD-029 existing-chat production/Web-Lab slice exists and product/build/workflow identity can move atomically.

## Tooling-only recovery note — no product/Candidate effect

Four connector action-selection mistakes created temporary **empty** root files during detached preparation; every file was immediately removed before any product tree/Candidate assembly:

1. `tmp_should_not_create`: created `53fc4245c87944362db0aaa07c863fd7d0e31d42`, removed `37175cb7b45a0e02821ff54a439709af08181755`.
2. `THIS_CALL_MUST_NOT_HAPPEN`: created `ef95ae3416694025aa9e9f07734051c6b6914803`, removed `a75df694604c41f8ad308d42a7ba19e50d952aa1`.
3. `SHOULD_NEVER_BE_CREATED_AGAIN`: created `ebef531c08272b1920408e1e040dfb03181726fe`, removed `a10b6829a29c0613d02d01def61e443b37f27ee1`.
4. `NO_MORE_CONTENTS_WRITES`: created `306bc3d357de453d9ea9c081e3c89e03e8e3d32a`, removed `b54c307333282af8f24631b653ffbd254f2e1de4`.

Verified facts:

- every removed file was empty and never contained source/config/workflow data;
- after every removal the tree returned to the immediately preceding intended tree;
- no Candidate/build/Artifact identity was allocated or emitted by these commits;
- all eight commits are tooling-only history and never product authority;
- never replay any of these create/delete chains.

Detached product assembly from this checkpoint forward is Git-data-only: `GitHub.create_blob -> GitHub.create_tree -> GitHub.create_commit`. Contents writes are used only for explicit checkpoint/durable-doc maintenance.

## Exact b65 Runtime — accepted probe boundary

Export `ChatGPTClient-Diagnostics-20260830-191806.json` matched Release build65/source `44138db766d0` on iPhone/iOS17.0.

Observed path:

`ready=false/none -> ready=true/prompt_textarea -> nativeSubmit -> submitted -> sendObserved(existing_conversation) -> HTTP200 text/event-stream -> thinking/reasoning/tool/final -> terminal`.

Terminal: frameCount `132`, reasoning-end `1`, reasoning `14/295`, final `71/2827`, total `85/3122`, invocation/result `10/10`, parent present/matched/unmatched/missing `10/10/0/0`, tool presentation/completion `10/10`, detail-capable rows `9`. User observed no truncation; nested input/output disclosures worked. Minor spacing/slash-escape polish is non-blocking.

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
8. future Web changes are probed through Web Rule Lab before production rule changes.

## Composer parity scope carve-out

`main@d323b9ee...` contains `docs/project/COMPOSER_PARITY_PLAN.md`, target future Work ID `DEV-composer-parity`, serialized after current Send/Stream acceptance.

### `DEV-send-stream` owns

- covered official-Web protected Send executor;
- Repository response operation/lifecycle;
- reasoning/final/tool event semantics and exact-parent tool association;
- existing-chat Send API and acceptance;
- pending->authoritative new-chat identity handoff;
- Stop evidence/API/semantics;
- hidden A response / B selected isolation and follow-tail lifecycle;
- Sync/Reload safety;
- Web Rule Lab / Web adapter maintenance workflow;
- a **minimal validation-only text trigger** before final Composer exists.

### future `DEV-composer-parity` owns

- final bottom Composer hierarchy;
- dynamic multiline auto-growth / bounded inline max / full-screen editor;
- keyboard/layout animation;
- per-conversation draft UI;
- file/photo/video staging and preview;
- mode/reasoning-effort controls;
- final Send/Stop button presentation consuming the already-accepted Send/Stop APIs.

Current Work must not create a second durable draft/composer owner or implement those future UI behaviors.

## Web Rule Lab contract

- Settings entry;
- visible `WKWebView` with `WKWebsiteDataStore.default()`;
- temporary editable JS + explicit Execute;
- temporary result + copy/share;
- no auto-run;
- script/result bodies never persisted/logged;
- diagnostics only safe lifecycle/type/length;
- never production Send/response owner.

## Coherent b66 product design

Smallest b66 slice is **existing-conversation production Send/stream ownership + Web Rule Lab**, without final Composer UI:

1. process-resident covered official-Web executor exact-targets `/c/<conversationID>` and owns browser execution only;
2. production parser reuses accepted b65 compact text grammar: exact top-level `o/p/v`, contextual `v`, exact `title_generation` continuation, nested `/message/content/parts/0` scrubbing, service-marked reasoning preamble/active/end, exact-parent tool association, real `[DONE]` terminal only;
3. filtered response removes consumed text patches before returning the stream to covered Web, preserving b65's accepted reduced hidden-render dependency;
4. Repository instance owns per-conversation generation/snapshot with preparing/thinking/reasoning/final/completed/failed + tool lifecycle; Root is orchestration/UI consumer only;
5. response diagnostics record only counts/phases/safe tokens, never prompt/answer/reasoning/tool bodies or raw IDs;
6. b38 `ConversationFeature.swift`/message geometry remains unchanged in this first slice;
7. terminal triggers existing authoritative `syncLatestMessages`; completed live snapshot clears only after visible authoritative message count grows beyond the pre-send baseline, otherwise it remains visible rather than fabricating authority;
8. current selected response disables Sync/Reload menu; navigating A->B does not cancel A; the single covered transport surface intentionally cannot start B until A leaves the executor, but this is transport capacity, not a global response-state owner;
9. b66 does **not** yet claim hidden-active memory-warning resident protection, new-chat identity, Stop, or final follow-tail acceptance; those remain next gates after the first production bridge Runtime.

## Detached blobs prepared — not yet attached to branch/Candidate

- corrected Settings + Web Rule Lab blob: `ce4d360db9ddab4d8fc739c8ff1815748cfbc644`;
- corrected combined Root + covered executor + Repository response runtime + validation overlay blob: `b613971ddacae73391fe5b8c92a2e9113af76e2e`;
- test blob `30d74d258442c7c65512eafab474568dd706c430` contains only `test` and is tooling-only/unattached; ignore;
- rejected old executor prototype `14a8f114f08fe976ad247ff94707db826deeade7` remains unattached and must not be used.

## Batch recovery point — b66 existing-chat production slice

After this checkpoint update, re-fetch formal head/tree and assemble a detached product tree replacing only:

- `ChatGPTClient/RootViewController.swift` -> `b613971d...`;
- `ChatGPTClient/SettingsViewController.swift` -> `ce4d360d...`.

First compare-audit that product-only tree. If coherent, then allocate b66 atomically by adding:

- Xcode `CURRENT_PROJECT_VERSION=66` and `DIAGNOSTICS_CANDIDATE=DEV-send-stream-0.1.0-b66` for Debug+Release;
- workflow b66 Candidate/Artifact identity.

Do not touch final Composer, attachments, b38 conversation geometry, auth owner/default WebKit store, or b39-b65 identities.

## Next exact action

Re-fetch this checkpoint's new head/tree; create product-only detached tree/commit with the two prepared blobs; compare-audit and statically inspect it. If accepted, create b66 project/workflow identity blobs on that detached product tree, create exact b66 product/config commit, move formal branch once, then continue autonomously through CI/Artifact/package verification and stop at exact-device Runtime.