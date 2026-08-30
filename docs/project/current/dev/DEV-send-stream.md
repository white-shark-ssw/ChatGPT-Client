# DEV-send-stream

## Status

**Active — exact b65 passed the focused iPhone/iOS17 Send/reasoning/final/exact-parent GitHub tool-detail Runtime gate. User explicitly selected production architecture Option B. TD-029 now authorizes the b48-b65 proven Native-composer -> covered official-Web page-owned protected-Send executor for production, while `ConversationRepository` remains the sole production conversation/response authority. Core Web adapter documentation and Web Rule Lab maintenance contract are established. Product batch B is now the next exact action. Stable/Frozen Send remains No. PR #29 remains open / mergeable / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged
- Other Active development checkpoints: none at latest guard
- Current actual `main`: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`
- Formal branch head after docs authority batch A: `74ecf41944294e6871827c548a487f159e00f4d3`
- Formal branch tree after docs authority batch A: `e1673e3fb4f988d1ee55749e2c8dc631523f9040`
- Stable native predecessor: b38
- Exact latest Runtime-tested Candidate: `DEV-send-stream-0.1.0-b65`
- Exact b65 product/config source: `44138db766d00e62cfda7f20182f6d20f1ec3352`
- b65 Push Run / Job: `33328232044 / 99302071335` — success
- b65 PR Run / Job: `33328233842 / 99302076369` — success
- b65 Push Artifact: `9736876465`
- b65 IPA SHA-256: `e6a01b2eafd361b9df2567b002f9e8aa56b57dcee219c7999c65767b91138d16`
- b39-b65 emitted identities: permanently reserved
- b66: **not emitted yet; reserved only when the detached first coherent TD-029 production/Web-Lab slice is complete and product+build+workflow identity can move together**

## Exact b65 Runtime — focused pass

User export `ChatGPTClient-Diagnostics-20260830-191806.json` matched exact Release b65 / build65 / source `44138db766d0` on iPhone/iOS17.0.

Observed path:

`ready=false/none -> ready=true/prompt_textarea -> nativeSubmit -> submitted -> sendObserved(existing_conversation) -> HTTP200 text/event-stream -> thinking/reasoning/tool/final -> terminal`.

Terminal metrics included frameCount `132`, exact reasoning-end `1`, reasoning `14/295`, final `71/2827`, total `85/3122`, thinking preambles `2/13`, invocation/result `10/10`, parent present/matched/unmatched/missing `10/10/0/0`, tool presentations/completions `10/10`, detail-capable rows `9`.

User directly reported no apparent reasoning/final truncation. Completed tool rows expanded/collapsed; `工具输入` and `工具输出` were independent second-level disclosures; decoded output no longer showed b64's second-layer escape wall. Remaining child spacing and legal slash escaping are non-blocking polish and do not justify another diagnostic Candidate.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b65-runtime.md`.

Classification: **b65 focused Runtime pass. Probe-level transport/parser/reasoning/tool lifecycle evidence accepted for the tested scope. Stable/Frozen No.**

## Production architecture — TD-029 current authority

The production bridge is now:

`Native composer -> Repository response operation -> covered official Web verified composer/page-owned protected Send -> same-response SSE -> ConversationRepository incremental response state -> Native presentation`.

Rules:

1. Native composer/history/reasoning/tool/final UI is the user-facing product surface.
2. One process-resident official Web execution surface may be covered/not user-visible and uses `WKWebsiteDataStore.default()`.
3. Official page owns Sentinel/PoW/Turnstile/conduit/challenge execution and the one protected browser Send.
4. Native code never solves/replays/persists challenge material.
5. Covered Web owns no conversation/message/response state; `ConversationRepository` is the sole production response owner.
6. One user Send -> exactly one protected Send; no second Send for stream/recovery.
7. Full Web conversation UI and b44 return+Sync product flow remain rejected.
8. Sync/Reload never resend/regenerate.
9. Web-specific current selectors/event rules live in `WEB_SEND_ADAPTER.md`.

## Web Rule Lab maintenance contract

A development Web Rule Lab is part of the current Work:

- Settings entry;
- visible `WKWebView` using the same default persistent data store;
- temporary editable JS area + explicit `执行`;
- temporary result display + copy/share;
- no auto-run;
- no persisted script/result bodies in diagnostics, defaults, files or database;
- diagnostics only safe execution lifecycle/type/length;
- never a production Send/response owner.

Future service changes use:

`reproduce -> AI supplies one small JS probe -> user runs it in Web Rule Lab -> structural evidence -> update WEB_SEND_ADAPTER -> one minimal production patch -> one coherent Candidate/Artifact -> exact Runtime`.

## Docs authority batch A — complete

Confirmed durable writes on the formal branch:

- `docs/project/WEB_SEND_ADAPTER.md` created;
- `docs/project/START_HERE.md` routes Send maintenance through both preflight + adapter playbook;
- `docs/project/SEND_STREAM_PREFLIGHT.md` rewritten for TD-029 Repository response ownership;
- `docs/project/TECHNICAL_DECISIONS.md` now contains TD-029 and explicit supersession boundaries;
- `docs/project/PROJECT_STATE.md` updated through b65 Runtime + TD-029;
- `docs/project/MODULE_STATUS.md` updated through b65 Runtime + production integration status;
- `docs/project/PROJECT_SPECIFIC_RULES.md` consolidated so stale “b48-b65 diagnostic only” language is no longer authoritative.

The formal branch head is exact `74ecf41944294e6871827c548a487f159e00f4d3`. These changes are docs-only; b65 product/config authority remains exact `44138db766d00e62cfda7f20182f6d20f1ec3352`.

## Current source implementation gap

- `RootViewController` still uses transitional `发送消息… -> AuthWebViewController.hybridChat -> return + explicit Sync`.
- `ConversationRepository` has per-conversation resident/detail ownership but no production response operation/lifecycle yet.
- `ConversationDetailViewController` has stable b38 table/geometry/navigation but no production composer/live response presentation.
- `NativeWebSendEngineProbe.swift` already contains the b65 Runtime-proven covered-Web composer/Send/interceptor/parser path and should be reused/extracted, not reinvented.
- `SettingsViewController` is the natural Web Rule Lab entry and already links diagnostics/probes.

## First production slice design boundary

The smallest safe b66 target is **existing conversation only** plus Web Rule Lab:

1. add one process-resident `CoveredWebSendExecutor` reusing the b65 exact verified composer/submit/fetch/SSE script;
2. executor requires exact `/c/<conversationID>` target match before Native Send and emits typed native events only;
3. add Repository-owned per-conversation live response state/generation with preparing/thinking/reasoning/final/completed/failed phases and response-local tool presentations;
4. active response keys protect resident state from memory-warning eviction;
5. add Native composer + live response panel to `ConversationDetailViewController` without replacing b38 historical table/geometry;
6. Root orchestrates composer -> Repository begin -> executor one Send; executor events -> Repository mutation; Root/VC never become response authority;
7. navigating A -> B does not cancel A; selected/hidden presentation consumes Repository state;
8. first slice does not invent new-chat identity or Stop before their own evidence gates;
9. add Settings Web Rule Lab in the same Candidate so future Web updates do not require repeated speculative IPA builds.

## Batch recovery point — product batch B / candidate batch C

Baseline:

- formal branch head `74ecf41944294e6871827c548a487f159e00f4d3`;
- base tree `e1673e3fb4f988d1ee55749e2c8dc631523f9040`;
- b65 product authority `44138db766d00e62cfda7f20182f6d20f1ec3352`;
- PR #29 open/mergeable/unmerged;
- main `1ac202c972f2dee6945fe8d0688df8e10f5d462c`.

Product files expected for detached batch B:

- `ChatGPTClient/Protocol/NativeWebSendEngineProbe.swift` — add reusable covered-Web executor around the same proven script; Probe remains diagnostic consumer;
- `ChatGPTClient/Conversation/ConversationFeature.swift` — Repository live response owner + existing-chat Native composer/live response presentation integration;
- `ChatGPTClient/RootViewController.swift` — own/attach executor and bridge Repository/Detail orchestration; stop using full-page hybrid as normal Send path;
- `ChatGPTClient/SettingsViewController.swift` — Web Rule Lab entry + implementation, preferably in-file to avoid unnecessary project-file source-list churn.

Candidate batch C, only after these files form one coherent slice:

- allocate b66;
- align Xcode CURRENT_PROJECT_VERSION/DiagnosticsCandidate and workflow Artifact identity in the same detached tree;
- compare audit against this docs head;
- formal branch fast-forward once only after exact diff approval.

Do not touch/reuse:

- b39-b65 Candidate identities;
- b38 geometry/round-navigation contracts beyond integration callbacks/layout insets required for composer/live response UI;
- auth/account/persistent WebKit ownership;
- full-Web conversation product UI.

## Next exact action

Build detached product batch B from `74ecf419...`, starting with the reusable covered-Web executor + Web Rule Lab, then Repository-owned existing-chat response state/UI/orchestration. Once coherent, atomically add b66 identity, compare-audit, move formal branch once, continue through CI/Artifact/package verification, and stop only at the real-device Runtime gate.