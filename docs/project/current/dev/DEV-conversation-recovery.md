# DEV-conversation-recovery

## Status

**Active — b14 implementation**

- **Work ID**: `DEV-conversation-recovery`
- **Routing aliases / keywords**: `会话同步与重载 / 同步最新消息 / 重载当前会话 / 冷启动登录恢复 / conversation recovery`
- **Task**: Finish explicit manual conversation recovery UX and cold-start usable native-list startup through the accepted WebKit/auth + production conversation owners.
- **Accepted baseline**: `DEV-native-read-path-0.1.0-b9` remains the merged Stable production native-read baseline until this Work is finalized and merged.
- **Working branch / PR**: `dev/conversation-recovery-20260826`; PR #10 open/unmerged.
- **Current base**: main `3a138ab6378fb72b9b36dedd3df55dc29e2ba814`; latest compare before b14 work is `behind_by=0`.
- **Only Active development checkpoint**: yes; no competing branch/candidate owner found.
- **Ownership correction**: cold-start login-state recovery belongs to this Work. Do **not** create a separate `DEV-auth-resume` task.

## Accepted / rejected runtime history

### b10 core recovery accepted

- Candidate `DEV-conversation-recovery-0.1.0-b10`; CI `32982836557`; artifact `9612167843`; IPA SHA `6e600f829fa24cdeb705e9ab104ebb780a8c70dd06871285d06fa30521aecb7e`.
- iPhone/iOS17 accepted loaded-state latest-sync and full reload; no resend/duplicate.

### b11 presentation rejected

- Request paths worked on device, but `navigationItem.prompt` was not visible. This feedback surface is rejected.

### b12 partial runtime acceptance

- Public `WKWebsiteDataStore.default()` warm-up is accepted for the tested persisted cold start: 0/0 -> 41/22 cookies in 194.97 ms; later unchanged account/list path succeeded without opening Login.
- Centered sync toast is accepted.
- Lazy compact-iPhone sidebar view loading delayed the first list request until the sidebar was eventually revealed, so b12 startup sequencing was rejected.

## b13 identity / CI / Artifact

- Candidate `DEV-conversation-recovery-0.1.0-b13` / `0.1.0 (13)`.
- Tested product/config head `fcc74ac4015449dba6c77f3136eede82cec3ec54`; synthetic merge `57187c0d0fd3116f964248a87f1a766268637788`; exact tree `2068ab4dc8f4bd9f94f1cb89e21b8dab29436ebf`.
- CI `32997544435` success; artifact `9617184873`; IPA SHA `2af6334278bcb88683cc123d47617e6956c0efb83aceb9b294961827f3e80040`.
- Later branch commits before this checkpoint were docs-only; b13 runtime package identity is exact.

## b13 real-device result — partial/failing

Exact user recording + diagnostics on iPhone/iOS17 prove:

### What b13 fixed

- Cold launch at `18:18:50Z`; public WebKit warm-up completed at `18:18:51Z`, 0/0 -> 39/20 cookies, `177.47 ms`.
- `listLoad.start` also occurred at `18:18:51Z`, so b13 **did fix the prior lazy-list-start defect**. The list request no longer waits for the user to reveal the sidebar.
- Normal detail operation generation/freshness logic is active. A later old generation-1 success was rejected as `detail.discarded reason=operation_superseded` after newer manual recovery generations existed.
- Recovery actions were available during the ordinary detail-loading state, matching the explicit requirement.

### Remaining startup/navigation defect

- The recording starts on the secondary placeholder `新对话 / 从侧边栏选择一个会话` rather than the useful conversation-list root for this current read-only startup state.
- The recording visibly shows **two identical sidebar icons** at top-left after compact navigation state changes. Current source has both UISplitViewController system compact navigation behavior and a b13 custom `sidebar.left` `leftBarButtonItem`; this is duplicate ownership of the same navigation affordance.
- `sidebar.open.requested` is logged repeatedly from `18:18:52Z` through `18:19:38Z`, including well after list response, while the recording shows taps often do not reveal the list. Therefore the custom `show(.primary)` button is not an acceptable compact-iPhone navigation contract.
- The second launch's list path itself completed at `18:19:13Z`: account context probe `17089.96 ms`, whole list load `22005.52 ms`, HTTP200 28/29. The user's near-minute wait to **enter** the list is therefore primarily a shell/navigation presentation defect, not delayed list initiation.

### Manual recovery overlap defect exposed by b13

- Conversation generation 1 ordinary load began `18:19:44Z` and eventually returned HTTP200 after `9733.60 ms` with 1017 visible messages.
- User-triggered reload generations 2 and 3, started while generation 1 remained in flight, each returned HTTP429 in about 1.1 s.
- Generation 1 was correctly prevented from overwriting newer manual recovery (`operation_superseded`), but the runtime proves that starting replacement detail requests while the prior selected-detail network task is still active can provoke rate-limit failure.
- Therefore manual recovery should **replace/cancel the prior selected-detail request before issuing the new one**, not run another selected-detail request concurrently. This is explicit user recovery ownership, not automatic retry machinery.

## b14 reserved identity / implementation direction

Candidate identity is reserved after checking the only Active checkpoint and build index:

- **`DEV-conversation-recovery-0.1.0-b14`**
- version/build **`0.1.0 (14)`**
- expected IPA `ChatGPTClient-0.1.0-b14-dev-conversation-recovery.ipa`

Minimum evidence-backed changes:

1. Configure the split shell synchronously before first compact presentation instead of installing its columns after the asynchronous warm-up callback.
2. On compact iPhone with no selected conversation, make **primary/sidebar** the initial top column; selecting a conversation shows secondary and normal native Back/system split navigation returns to the list.
3. Remove the b13 custom duplicate sidebar button. Do not own the same compact navigation affordance twice.
4. Keep accepted WebKit warm-up ordering for network work: sidebar `viewDidLoad` must no longer auto-start the list; `RootViewController` starts exactly one initial list load only after warm-up completes.
5. Track the current selected-detail network task in `ConversationRepository`. When explicit sync/reload replaces an in-flight selected-detail operation, cancel the older task before the new request starts; retain the generation guard so late callbacks cannot mutate newer state.
6. No retry, timer, watchdog, fallback endpoint/header set, hidden WebView, resend/regenerate, or second persistent state owner.

## State owner / invariants

- `ConversationRepository` remains sole production conversation read/recovery owner.
- `AuthSessionStore` and default `WKWebsiteDataStore` contracts remain unchanged in b14.
- UISplitViewController/native navigation owns compact sidebar/back presentation; no duplicate custom sidebar owner.
- A selected-detail task handle is request-lifecycle ownership only, not a second conversation data store.

## Validation state

- b10: Code + CI + Artifact + Runtime accepted for core recovery.
- b11: Code + CI + Artifact + Runtime; feedback presentation rejected.
- b12: Code + CI + Artifact + Runtime partial accepted — warm-up + centered toast accepted, startup sequencing rejected.
- b13: **Code + CI + Artifact + Runtime/manual tested, partial/failing** — immediate list initiation and freshness guard worked; compact startup/navigation failed; overlapping manual replacement requests produced HTTP429.
- b14: **identity reserved; implementation/CI/Artifact pending**.
- Stable / merged: **no**.

## Next exact action

Implement the b14 minimum patch above, run CI/package inspection, then real-device test:

1. Force-quit -> launch: initial compact page should be the conversation list immediately, not blank `新对话` detail.
2. No duplicate top-left sidebar icons.
3. List network still starts only after accepted WebKit warm-up, exactly once.
4. Select a conversation -> detail; native Back/system split navigation returns to list reliably.
5. While ordinary detail is loading, sync/reload remain available. Starting one manual recovery cancels/replaces the old selected-detail request; there must not be two selected-detail requests intentionally left active by the client.
6. Centered sync feedback and normal full reload behavior remain intact.

## Rejected / do-not-repeat

- No separate `DEV-auth-resume` Work.
- No hidden/shadow WebView or persisted copied auth secrets.
- No automatic retry/watchdog/timer/resend/regenerate/fallback chain.
- No `navigationItem.prompt` for required feedback.
- Do not gate list start on sidebar reveal.
- Do not add a second custom compact sidebar button on top of UISplitViewController/native navigation.
- Do not intentionally leave the older selected-detail task running when explicit manual recovery is replacing it.