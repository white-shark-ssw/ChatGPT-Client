# DEV-send-stream

## Status

**Active — b69 exact iPhone/iOS17 Runtime is Partial/Rejected for daily-chat parity. b67 remains the accepted existing-conversation protected-Send transport predecessor. b69 proves the ordered response timeline direction but exposes concrete b70 defects in keyboard focus, immediate user-message presentation, reasoning/tool detail+spacing+separator+icons, and Native read credential lifecycle. Stable/Frozen Send remains No; PR #29 stays open/unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29
- Formal branch head before b70 product assembly: `55f4f44c244fe2b188632e5a45192f729582c560` after the b69 Runtime checkpoint update
- Exact b69 product/config source: `5e9c2183483094304f7eaeecf4ffc7ad8e65b902`
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- b69 Artifact `9748400171`; IPA SHA `0c06256dc90aed86c706f8c72950528f61afa7f7fcdb504b2604d40befe3b0aa`
- b39-b69 permanently reserved
- Repository search found no existing `DEV-send-stream-0.1.0-b70`; b70 is now justified by concrete Runtime defects.

## Exact b69 Runtime evidence — 2026-08-31

User evidence:

- `RPReplay_Final1788160522.mp4` — simple Send/answer recording;
- `RPReplay_Final1788160538.mp4` — reasoning disclosure recording;
- supplied screenshot — official ChatGPT tool-row/icon reference;
- `ChatGPTClient-Diagnostics-20260831-072737.json` — exact b69 export.

Accepted from b69/b67:

- multiple real Sends still reach one `sendObserved` -> HTTP200 `text/event-stream` -> terminal/reconcile;
- Repository-owned ordered timeline remains the correct state direction;
- hidden `assistant:thoughts` / `inline_cot_expandable_content` remain excluded.

Rejected/current defects:

1. covered Web programmatic composer injection can raise the iOS keyboard after the Native validation alert dismisses;
2. the user's prompt is absent from live Native rows and only appears after terminal authoritative Sync;
3. expanded `思考过程` spacing is unlike official UI; no reasoning/final divider;
4. production b69 dropped b65 Runtime-accepted GitHub nested `工具输入` / `工具输出` disclosures;
5. tool rows lack corresponding leading icons;
6. Native read auth can become sticky/blank: verified session/accounts may be followed by list/detail 403; Web login can be visibly authenticated while Native account probe is temporarily 403; later the same account succeeds again.

## Source-backed b70 roots and minimum corrections

### Covered Web keyboard

`CoveredWebSendExecutor.bridgeScript.setComposerText` unconditionally calls `element.focus()`. Keep the already-verified input/submit mechanism but suppress the covered Web virtual keyboard during the temporary programmatic focus and blur immediately after injection. Do not replace the verified composer selector/route/send grammar.

### Immediate user row

Current `beginLiveResponse` receives only `promptCharacterCount`; the Repository snapshot has assistant state only. b70 passes the actual trimmed prompt into the existing response operation and stores it only inside that response snapshot. Native derives one optimistic user row immediately before the live assistant row; terminal authoritative Detail replaces both by clearing the live snapshot after successful reconcile. This remains one Repository owner, not a second persistent message store.

### Tool detail/icon/separator presentation

Reuse b65's already Runtime-accepted exact GitHub detail authorization:

- invocation `metadata.connector_tool_payload` is held transiently;
- only an exact-parent completed result with `recipient == api_tool.call_tool` and `metadata.invoked_resource.app_name == GitHub` authorizes presentation of that input plus result `message.content`;
- input/output are independent nested disclosures and collapsed by default;
- output uses the accepted hierarchical nested-JSON decoder;
- no raw tool body enters diagnostics.

Extend the ordered timeline item only with response-local input/output strings plus a bounded local icon kind. Derive icon kind from current service metadata/known GitHub result classification and render a small leading symbol; do not persist arbitrary remote icon payloads. Replace blank-line tool spacing with controlled paragraph spacing and add a deterministic separator between expanded reasoning/tool content and an actual final answer.

### Native read/auth owner correction

Exact source inspection confirms two separate b69 issues:

1. `ConversationRepository` caches one copied `AuthTransientSession` indefinitely for an unchanged account scope, and list/detail HTTP401/403 does not invalidate it.
2. `AuthSessionStore.probeAccountContext` currently maps HTTP403 at session/accounts stages to `.notAvailable`, and `setAccountState(.failed/.notAvailable)` clears the last verified account context. The supplied export proves HTTP403 can be temporary for the same browser-authenticated account and later return 200; therefore a 403 must not by itself be treated as persistent logout/account replacement.

b70 auth correction is intentionally non-retrying:

- add `ChatGPTClient/Authentication/AuthSessionStore.swift` to this Work's authorized scope;
- classify exact HTTP403 from session/accounts probes as temporary probe failure, not account absence; preserve the last verified identity across `.failed` while still returning no fresh transport from that failed probe;
- exact 401 remains unavailable/not-authenticated behavior;
- on Native list/detail 401/403 from the current copied transient transport, invalidate/discard that transient transport once; the current operation still fails visibly;
- the next explicit/normal read uses the existing account-context probe to materialize current WebKit cookies/token; no automatic replay/retry/poll/timer/watchdog;
- returning from the user-opened login screen may trigger one explicit list refresh so a successful re-auth is reflected without requiring force-quit; this is a new user/navigation operation, not hidden retry;
- `AuthSessionStore` remains sole account authority and `WKWebsiteDataStore.default()` remains sole persistent auth-secret authority.

## Authorized b70 files

Product/config changes may touch only:

- `ChatGPTClient/RootViewController.swift`;
- `ChatGPTClient/Conversation/ConversationFeature.swift`;
- `ChatGPTClient/Authentication/AuthSessionStore.swift`;
- `ChatGPTClient.xcodeproj/project.pbxproj` for Build70 identity;
- `.github/workflows/ios-foundation.yml` for b70 candidate/artifact identity.

Do not modify b38 quick-navigation algorithm, accepted b67 protected-Send route/challenge/SSE grammar beyond the narrow keyboard/detail metadata payload, persistent auth-secret storage, unrelated diagnostics, final Composer/attachments, or other Works.

## Batch recovery point — b70

Baseline/guards already verified before this checkpoint:

- formal branch/PR head lineage is b69 plus docs only; PR #29 open/mergeable/unmerged;
- actual `main` unchanged at `d323b9ee...`;
- only Active development checkpoint is this Work;
- b70 identity unused;
- b69 remains valid/reserved.

Completed write batches:

1. b69 Runtime/initial b70 checkpoint at `55f4f44...`;
2. this source-inspection qualification checkpoint.

Remaining deterministic batches:

1. create a tooling-only b70 assembly ref from the new formal checkpoint head;
2. apply exact-anchor patches only to the five authorized files above;
3. static assertions + `git diff --check`; emit one clean detached b70 product/config commit;
4. audit checkpoint->candidate changed files and semantic boundaries;
5. re-check formal branch/PR/main/Active checkpoint and fast-forward only if unchanged except this checkpoint;
6. wait for actual Push + PR Xcode CI; then independently verify Artifact ZIP/IPA/Info.plist/source marker;
7. update checkpoint + BUILD_TEST_INDEX / PROJECT_STATE / MODULE_STATUS / PROJECT_PROFILE / TECHNICAL_DECISIONS and PR #29 with actual evidence;
8. stop at the exact b70 real-device gate.

Recovery must not blindly replay prior writes and must not rewrite b69 identity/artifact.

## Evidence ladder

- b67: production existing-conversation transport Runtime passed.
- b68: valid reserved Artifact; flattened UI superseded.
- b69: Code/diff/Push+PR CI/Artifact/package passed; Runtime Partial/Rejected for current daily-chat parity and auth stability; transport success retained.
- b70: justified; no product source/Artifact yet.
- Stable/Frozen Send: No.

## Next exact action

Assemble and audit the smallest b70 candidate on the five authorized files. The human Runtime gate must verify: no covered-Web keyboard pop, immediate single optimistic user row, chronological reasoning/tools with restored GitHub nested details + leading icons + compact spacing/divider, preserved active response across navigation, and recovery from transient Native 403 via stale-session invalidation/current Web credentials without automatic retry.
