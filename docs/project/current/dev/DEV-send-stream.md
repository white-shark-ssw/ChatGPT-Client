# DEV-send-stream

## Status

**Active — exact b63 has now passed the focused iPhone/iOS17 Runtime gate for verified composer / protected Send / complete-looking reasoning-final / exact-parent visible tool lifecycle, and the same-run official Web screenshots establish a concrete GitHub expandable-detail mapping. b64 is now the next unique Candidate and may implement only that evidenced mapping. Stable/Frozen Send remains No. PR #29 remains evidence-only / open / mergeable / unmerged. TD-024/TD-025/TD-028 and production `ConversationRepository` ownership remain unchanged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged; evidence-only
- Other Active development checkpoints: none at latest guard
- Current actual `main`: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`
- Stable native predecessor: b38
- Accepted Runtime Candidate: `DEV-send-stream-0.1.0-b63`
- Exact b63 product/config source: `0c2e2b870e51c363c7734182d49618c438839cc2`
- b63 Push Run / Job: `33321982009 / 99285436158` — success
- b63 PR Run / Job: `33321983658 / 99285440962` — success
- b63 Artifact: `9735145598`
- b63 ZIP SHA-256: `645cba67a91387f79d386931b5d0f4ead2502408b15c7f339013505e3f0ec7da`
- b63 IPA SHA-256: `b347d1e41ca5a4e1355a9cc713574ea96247e11918ccfb1f5ff621a0f9f6ff36`
- b63 package: Release / `0.1.0 (63)` / source marker `0c2e2b870e51` / iOS14 / `[1,2]` / arm64
- b39-b63 emitted identities: permanently reserved
- Next unique Candidate: `DEV-send-stream-0.1.0-b64` / `0.1.0 (64)`; repository search found no existing b64 identity before allocation

## Exact b63 Runtime — passed tested gate

User export `ChatGPTClient-Diagnostics-20260830-170359.json` matched exact Release b63 / iPhone / iOS17.0 / source `0c2e2b870e51`.

Observed Send-entry sequence remained the accepted verified-composer path:

`ready=false / none -> page loaded -> ready=false / none -> ready=true / prompt_textarea -> nativeSubmit -> submitted -> sendObserved -> HTTP200 text/event-stream -> terminal`.

Terminal response evidence:

- frameCount `308`, terminal `true`;
- exact reasoning-end `1`, fallback false;
- Native reasoning `23 deltas / 328 chars`;
- Native final answer `200 deltas / 6345 chars`;
- Native total `223 deltas / 6673 chars`;
- thinking preambles `2 / 7 chars`;
- reasoning-active signals `5`;
- Native thinking presentations `4`;
- service/native reasoning segment breaks `1/1`;
- title-generation while continuation active `1`.

The user directly reported no apparent truncation. Screenshot evidence showed populated reasoning, completed tool rows and a long final answer with no obvious prefix/middle loss.

Tool lifecycle metrics:

- invocation identities `24`;
- results `25`;
- parent present `25`;
- exact parent matches `24`;
- unmatched `1`;
- missing `0`;
- Native presentations/completion updates `24/24`;
- paired presentations `24`.

The unmatched result was not force-paired, confirming exact `parent_id` remains the only accepted row association rule; count/order/adjacency remain rejected.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b63-runtime.md`.

## Same-run official Web expandable-detail mapping

The user's official Web screenshots from the same b63 response establish that GitHub connector tool rows are individually expandable and that a representative expanded `fetch` row exposes:

- `工具描述`;
- `工具输入`, visibly showing the request argument object, including the `url` field/value;
- `工具输出`, visibly showing returned structured content including `content_type: "multimodal_text"` and `parts: Array(3)` plus returned part text when further expanded.

This lines up with b63 SSE evidence:

- completed assistant `code` invocations to `api_tool.call_tool` carry JSON-string `metadata.connector_tool_payload`; b63 observed direct shapes such as `json_object:url:string...`, `query + repository_name + topn`, and `owner + repo_name + query + page_size`;
- exact parent-paired tool results carry `message.content` shapes including `multimodal_text`, `code`, and `text`;
- the official Web `工具输入` matches the invocation payload, and `工具输出` matches the paired tool-result `message.content` shape.

`inline_cot_expandable_content.source_message_ids` evidence is supportive but not row authority: expandable messages/source refs were `3/3`, all three matched invocation identities, only two matched the tool-activity set, unmatched `0`; this is far fewer than the 24 visible Native rows.

## Accepted b64 implementation boundary

b64 may make the existing Native GitHub tool rows expandable with only the same-run evidenced content:

1. preserve current response-local invocation identity and exact result `parent_id` pairing;
2. retain a paired GitHub invocation's `metadata.connector_tool_payload` only in response-local transient presentation state and display its parsed JSON as `工具输入`;
3. when the exact paired result arrives, retain that result's `message.content` only in the same transient presentation state and display it as `工具输出`;
4. do not use or display `assistant:thoughts` body;
5. do not log/export raw tool input/output values or service IDs;
6. do not invent `工具描述` because its exact service source remains Unknown / Unverified;
7. do not broaden this mapping to unrelated connector/tool families without evidence;
8. preserve b63 composer / protected Send / SSE text / reasoning-final / reasoning-end / tool-row lifecycle behavior exactly;
9. add no retry, polling, timer, watchdog, fallback, compatibility shim, second state owner or production repository mutation.

## Recovery point before b64 product assembly

Completed:

1. exact b63 Runtime identity verified;
2. b63 Runtime classified as pass for the tested text/tool lifecycle gate;
3. same-run official Web screenshots correlated with b63 structural diagnostics;
4. accepted GitHub expandable input/output mapping persisted in `DEV-send-stream-b63-runtime.md`;
5. `main` rechecked at `1ac202c972f2dee6945fe8d0688df8e10f5d462c`;
6. PR #29 rechecked open / mergeable / unmerged with head on this feature branch;
7. repository search found no existing `DEV-send-stream-0.1.0-b64` identity.

Next non-atomic product assembly must use this checkpoint as the recovery point. Assemble complete b64 product/config identity off-ref first, audit the diff, then move the formal feature branch exactly once. Do not allow new b64 code to build under b63 package identity.

## Next exact action

Fetch the current b63 Swift/Xcode/workflow sources from this checkpoint head, implement only the accepted GitHub expandable input/output UI in `NativeWebSendEngineProbe.swift`, update build/Candidate/workflow identity to b64 in the same detached tree, audit parent→b64 diff for only intended files, then fast-forward `dev/send-stream-20260829` once. Run Push + PR CI, verify Artifact/package identity independently, update durable docs/PR, and hand exact b64 IPA to the user for Runtime. Any correction after a valid b64 Artifact must use b65+.