# DEV-send-stream

## Status

**Active — exact b69 Runtime is now Partial/Rejected for daily-chat parity. The accepted b67 protected-Send transport still works, and b69's ordered Repository timeline is directionally correct, but the user's two exact iPhone/iOS17 recordings + screenshot + `ChatGPTClient-Diagnostics-20260831-072737.json` establish concrete production defects requiring b70: covered-Web keyboard activation, delayed user-message presentation, reasoning/tool spacing/separator/detail/icon regressions, and unstable Native read auth caused by HTTP403 around copied transient credentials. Stable/Frozen Send remains No. PR #29 stays open / evidence-only / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29
- Current formal branch head before this checkpoint update: `b221d9bbad25007efb9d149568dc493ea3d3afa6`
- Exact b69 product/config source: `5e9c2183483094304f7eaeecf4ffc7ad8e65b902`
- Current actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Stable merged predecessor: b38
- Accepted production transport Runtime predecessor: b67
- Latest emitted Candidate: b69 — Artifact valid; Runtime Partial/Rejected for current product UX
- Next identity: b70 is now justified by concrete b69 Runtime evidence; repository search found no existing `DEV-send-stream-0.1.0-b70` identity.
- b39-b69 are permanently reserved.

## Exact b69 package identity

- Candidate: `DEV-send-stream-0.1.0-b69`, `0.1.0 (69)`
- Product/config source: `5e9c2183483094304f7eaeecf4ffc7ad8e65b902`
- Push `33366226539 / 99407331552` — success
- PR `33366229125 / 99407340011` — success
- Artifact `9748400171`
- ZIP `sha256:b1d91179c47822a7a42bf5405ef4bbd7240b97ddff58743a8a12e5f16fb232f1`
- IPA `sha256:0c06256dc90aed86c706f8c72950528f61afa7f7fcdb504b2604d40befe3b0aa`
- Package marker `5e9c21834830`, minimum iOS14

b69 remains permanently reserved. Product corrections use b70.

## Accepted predecessor retained

Exact b67 remains accepted for the tested existing-conversation transport path:

`one Native Send -> one page-owned protected Send -> HTTP200 text/event-stream -> Repository response events -> terminal -> one authoritative reconciliation`.

The b69 diagnostics again show real `sendObserved`, HTTP200 SSE and terminal on multiple turns. Therefore the current b70 work must not rewrite the covered route/challenge/SSE architecture merely because the UI/auth consumers are defective.

## Exact b69 Runtime evidence — 2026-08-31

User evidence:

- `RPReplay_Final1788160522.mp4` — simple Send/answer recording.
- `RPReplay_Final1788160538.mp4` — reasoning disclosure recording.
- screenshot supplied with the same report — official ChatGPT conversation/tool-row visual reference.
- `ChatGPTClient-Diagnostics-20260831-072737.json` — exact b69 diagnostics export.

### A. Send interaction defects

1. After the validation Send alert dismisses, the keyboard can rise again while the response is already active. Source correlation shows the covered official-Web bridge's `setComposerText` unconditionally calls `element.focus()` before programmatic text assignment. On iOS a covered/noninteractive Web composer focus is still capable of becoming the keyboard first responder. This is a product defect; the covered executor must not steal visible keyboard focus.
2. The user's submitted text does not appear in Native conversation immediately. Current `startValidationSend` gives `ConversationRepository.beginLiveResponse` only the prompt character count; the live response snapshot contains assistant state only. The user message arrives in Native only after terminal `syncLatestMessages` adds the authoritative user+assistant pair. This violates normal chat interaction. b70 must show one Repository-owned optimistic user presentation immediately and reconcile it away when the authoritative user message arrives; no second persistent message store.

### B. Reasoning/tool presentation defects

1. b69's chronology work is retained, but expanded `思考过程` spacing/density is visibly unlike the official app.
2. Production b69 tool timeline items contain only `slot/title/completed`; the b65 Runtime-accepted GitHub `工具输入` / `工具输出` nested disclosures were dropped during production timeline integration. This is a regression and must be restored from the already-authorized exact-parent GitHub mapping, not re-invented.
3. Expanded reasoning needs a visual separator between the reasoning/tool area and formal final answer, matching the user's official recording.
4. Official tool rows have leading tool-specific icons. Existing service/probe evidence already exposes safe tool classification/icon metadata such as `metadata.tool_summary_type` and `metadata.tool_icons` shape. b70 may carry a bounded presentation icon kind through the existing response timeline; it must not persist arbitrary remote icon payloads or create another state owner.
5. `assistant:thoughts` and `inline_cot_expandable_content` remain prohibited from presentation.

### C. Native read/auth stability defect

The diagnostics establish a credential-lifecycle problem, not simply “user was logged out”:

- `/api/auth/session` and accounts-check can return HTTP200 / verified, followed immediately by Native list/detail HTTP403.
- repeated list/detail requests can keep returning HTTP403.
- the Web login surface can finish on `chatgpt.com` and be marked authenticated while immediate Native account-context probes still transiently return HTTP403.
- later a newly materialized account context can succeed again and list/detail return HTTP200.
- later in the same export another account probe reaches HTTP403 at accounts stage.

Current source explains the sticky failure: `ConversationRepository` caches one copied `AuthTransientSession` (ephemeral cookies + copied access token) and reuses it indefinitely while account identity/scope stays equal. List/detail 401/403 does not invalidate that copied transport. A browser session/credential refresh for the same user/account identity therefore does not necessarily replace the stale native transient session.

b70 correction boundary:

- `AuthSessionStore` remains sole auth/account owner and default WebKit store remains sole persistent auth-secret authority.
- On a Native conversation list/detail HTTP401 or HTTP403 from the **current** transient transport, invalidate/discard that cached transient transport so the next explicit/normal read obtains fresh cookies/token through the existing account-context probe.
- Do not automatically repeat the failed request inside a retry loop; current operation fails observably. A subsequent user/normal load is a new operation and may materialize current Web credentials.
- Do not treat a transport 403 alone as proof that persistent Web login is gone.
- Preserve existing account-scope isolation and stale-callback rejection.

## b70 minimum product scope

Only evidence-backed changes are authorized:

1. `ChatGPTClient/RootViewController.swift`
   - stop covered Web programmatic text injection from taking visible keyboard focus while preserving the existing verified composer/one-Send path;
   - pass actual prompt text into the existing Repository response operation for immediate optimistic user presentation;
   - extend tool activity event data only with already-authorized GitHub detail and bounded icon classification needed by Native presentation.
2. `ChatGPTClient/Conversation/ConversationFeature.swift`
   - add Repository-owned optimistic user presentation to the existing live response snapshot, then remove it on authoritative terminal reconciliation;
   - restore b65-authorized GitHub input/output nested disclosure state inside the ordered tool timeline and carry bounded icon kind;
   - tighten reasoning/tool spacing and add the reasoning/final separator using the existing deterministic/manual b38 geometry path;
   - invalidate current cached transient Native read session on list/detail HTTP401/403, with no automatic retry.
3. Xcode/workflow identity files only for unique b70 Candidate.

Do not add a second message/response/auth store, retry/poll/timer/watchdog, speculative selector fallback, compatibility shim, Web DOM conversation mirroring, arbitrary connector raw detail, or unrelated refactor.

## Batch recovery point — b70

Verified baseline before the b70 non-atomic write chain:

- formal branch head entering this checkpoint write: `b221d9bbad25007efb9d149568dc493ea3d3afa6`;
- exact b69 product source: `5e9c2183483094304f7eaeecf4ffc7ad8e65b902`;
- b69 Artifact/IPA above are valid and permanently reserved;
- PR #29 open / mergeable / unmerged at `b221d9bb...`;
- actual `main` `d323b9eed2dda75b9986fc06e14014d3e9b365fb`;
- only Active development checkpoint is this Work;
- b70 identity is unused before assembly.

Intended batches:

1. finish exact source inspection of current live snapshot/cell layout, b65 GitHub detail decoder/disclosure, Auth Web return/list lifecycle, and b69 tool bridge metadata;
2. create tooling-only b70 assembly ref from the new checkpoint head;
3. patch only the authorized b70 source/config surfaces above with exact-anchor assertions;
4. run static source assertions + `git diff --check`, then emit one clean detached b70 product/config commit;
5. audit checkpoint->candidate changed files and semantic boundaries; re-check formal branch/PR/main/other Active checkpoints before fast-forward;
6. move formal Work branch only after that audit;
7. wait for real Push + PR Xcode CI; if successful, independently verify the unique IPA/Info.plist/source marker and hashes;
8. update this checkpoint plus BUILD_TEST_INDEX / PROJECT_STATE / MODULE_STATUS / PROJECT_PROFILE / TECHNICAL_DECISIONS / relevant project rules and PR #29 with actual evidence;
9. stop at the exact b70 iPhone/iOS17 Runtime gate.

Confirmed completed writes at this recovery point: this checkpoint update only. Remaining writes: all b70 product/config, CI/Artifact, durable-doc and PR updates.

Recovery must not rewrite b69 identity, b67 accepted transport semantics, b38 quick-navigation geometry, default WebKit persistent auth authority, or hidden-thought prohibition.

## Evidence ladder now

- b67: production existing-conversation transport Runtime passed.
- b68: valid reserved Artifact; flattened presentation superseded before Runtime.
- b69: Code/diff/Push+PR CI/Artifact/package passed; exact real-device Runtime is **Partial/Rejected for daily-chat parity** with concrete b70 defects above. Transport success remains accepted evidence; UI/auth stability does not.
- b70: identity justified but no product source/Artifact exists yet.
- Stable/Frozen Send: No.

## Next exact action

Resume from this checkpoint and inspect the exact b69 cell/live-response/auth/login-return source plus the already Runtime-accepted b65 GitHub detail implementation. Then assemble the smallest b70 correction covering keyboard focus, immediate optimistic user presentation, ordered tool detail/icon/separator spacing, and stale transient-read invalidation on 401/403. Audit before moving the formal branch; do not create an Artifact until the detached scope is clean.
