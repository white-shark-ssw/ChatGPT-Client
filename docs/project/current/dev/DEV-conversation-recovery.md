# DEV-conversation-recovery

## Status

**Active — b15 selected-detail cancellation/replacement candidate**

- **Work ID**: `DEV-conversation-recovery`
- **Routing aliases / keywords**: `会话同步与重载 / 同步最新消息 / 重载当前会话 / 冷启动登录恢复 / conversation recovery`
- **Task**: Finish explicit manual conversation recovery UX and cold-start usable native-list startup through the accepted WebKit/auth + production conversation owners.
- **Accepted baseline**: `DEV-native-read-path-0.1.0-b9` remains the merged Stable production native-read baseline until this Work is finalized and merged.
- **Working branch / PR**: `dev/conversation-recovery-20260826`; PR #10 open/unmerged.
- **Current base**: main `3a138ab6378fb72b9b36dedd3df55dc29e2ba814`; latest pre-b15 compare `behind_by=0`.
- **Active conflict scan**: only this development checkpoint exists on the working branch; no competing Active Work/candidate owner found. Existing development branches contain only earlier completed/merged work.

## Accepted runtime history

- **b10**: core `同步最新消息` / full `重载当前会话` accepted on iPhone/iOS17; no resend/duplicate.
- **b11**: request path worked but `navigationItem.prompt` feedback was invisible; presentation rejected.
- **b12**: centered sync toast accepted; public `WKWebsiteDataStore.default()` warm-up accepted for tested persisted cold start; lazy compact sidebar delayed initial list request.
- **b13**: immediate list start and operation-generation stale rejection worked; compact startup/navigation failed; while ordinary detail generation 1 remained active, manual replacement generations 2/3 returned HTTP429.
- **b14**: exact `DEV-conversation-recovery-0.1.0-b14` / `0.1.0 (14)` real-device accepted for compact startup/navigation. Cold start lands on conversation list, duplicate sidebar icons are gone, native compact list/detail navigation is usable. User explicitly reported b14 had no issues for the stated gate.

## b14 accepted identity

- Product/config head `82d96bf085dbee3877bcb16e27bbf69f4dc0990f`; tested merge `5b2f60dc8b30ae15d56cbe2d49bbe6b61aff0ad6`; exact tree `4d0ddb24ba6e261cdb7a4057ce47e73f199ad481`.
- CI `33000566633`; artifact `9618410313`.
- IPA `ChatGPTClient-0.1.0-b14-dev-conversation-recovery.ipa`.
- IPA SHA `b9100deb1d59b8ce22e15e72f766f0313be2903ec96ed2cda3d397986ba89182`.

## b15 identity

Fresh candidate allocated after checking `BUILD_TEST_INDEX.md`, the only Active checkpoint, real Xcode build source, PR #10 and current branch/base state:

- **Candidate**: `DEV-conversation-recovery-0.1.0-b15`
- **Version / Build**: `0.1.0 (15)`
- **Expected IPA**: `ChatGPTClient-0.1.0-b15-dev-conversation-recovery.ipa`
- **Current product/config head after implementation + identity files**: `159e8ea4f7baf6cd890d1f9bbebeac41feefbf52`
- **CI / Artifact / Runtime**: pending at this checkpoint update.

## b15 evidence-backed implementation

The remaining b13 HTTP429 overlap is the only target. No new Work ID was created because this is the same `ConversationRepository` manual-recovery owner and same PR dependency.

### `AuthTransientSession`

- Existing `dataTask(with:completion:)` now returns the same `URLSessionDataTask` it already creates and resumes.
- `@discardableResult` preserves all existing callers.
- Authorization header, ephemeral session, cookies, endpoint behavior and task-start behavior are unchanged.

### `ConversationRepository`

- Adds one selected-detail `URLSessionDataTask` handle plus its operation generation. This is request-lifecycle ownership only, not conversation state authority.
- Ordinary `loadConversation` behavior is unchanged by default.
- `同步最新消息` and `重载当前会话` call the same detail path with explicit replacement ownership.
- A new manual recovery increments/owns the new generation first, then cancels the older tracked selected-detail task before starting its replacement request.
- Intentional `NSURLErrorCancelled` is logged as `detail.cancelled` / span status `cancelled`, not as a network failure and not surfaced to the obsolete UI completion.
- Existing `operationGeneration` guard remains in place so any late non-cancelled callback from an obsolete operation is still rejected.
- No retry, timer, watchdog, delayed retry, fallback endpoint/header set, resend/regenerate, hidden WebView or second persistent state store was added.

## Static/source review

Diff from pre-b15 branch head `dbac22552b5c8f58fb4e51e4b6dead2c429a0005` before identity files:

- `AuthSessionStore.swift`: +5 / -2, only return of existing task handle.
- `ConversationFeature.swift`: +38 / -5, selected-detail task lifecycle + intentional-cancel diagnostics + manual replacement flag.
- No auth parser/endpoint/header, conversation endpoint/parser or UI presentation changes.

## State owner / invariants

- `ConversationRepository` remains sole production conversation read/recovery owner.
- Default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- `AuthSessionStore` auth/account semantics remain Stable; b15 only exposes an already-created transient `URLSessionDataTask` handle needed by the production owner.
- b14 native compact navigation contract is unchanged.

## Validation state

- b14: **Code + static/source review + CI + Artifact + Runtime/manual accepted for compact startup/navigation**.
- b15: **Code written + static/source review; CI pending; Artifact pending; Runtime pending**.
- Entire Work: **not Stable / not merged** until b15 real-device acceptance.

## b15 real-device gate

After exact b15 Artifact exists:

1. Enter a conversation and, while ordinary `正在读取会话…` is still active, trigger exactly one manual `重载当前会话` or `同步最新消息`.
2. Diagnostics should show `detail.cancel.requested` for the old generation, then `detail.cancelled` for that old task, followed by one replacement `detail.request` for the new generation.
3. There must not be an intentionally concurrent old + replacement selected-detail request left active by the client.
4. The replacement should complete normally without reproducing the b13 overlap-driven HTTP429 in the tested case.
5. Existing centered sync feedback, full reload behavior, b14 cold-start/list root and native Back navigation must remain intact.

## Next exact action

1. Accept only CI associated with final b15 product/config head or an exact-tree-equivalent PR synthetic merge.
2. Inspect/download Artifact and verify embedded version/build/candidate/source + SHA.
3. Deliver exact b15 IPA for the real-device gate above.
4. If accepted, record Runtime evidence, perform final main/PR/conflict scan, merge PR #10, update durable docs and complete this Work.
5. Only then start `DEV-multi-conversation-state`.

## Rejected / do-not-repeat

- Do not create a separate Work for this replacement fix.
- Do not reuse b14 or any prior candidate identity.
- No hidden/shadow WebView or copied persistent auth secrets.
- No automatic retry/watchdog/timer/resend/regenerate/fallback chain.
- Do not remove the generation guard merely because task cancellation now exists.
- Do not claim cancellation solves the HTTP429 runtime defect until exact b15 device evidence confirms it.
