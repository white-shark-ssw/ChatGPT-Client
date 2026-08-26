# DEV-conversation-recovery

## Status

**Active — b14 real-device gate**

- **Work ID**: `DEV-conversation-recovery`
- **Routing aliases / keywords**: `会话同步与重载 / 同步最新消息 / 重载当前会话 / 冷启动登录恢复 / conversation recovery`
- **Task**: Finish explicit manual conversation recovery UX and cold-start usable native-list startup through the accepted WebKit/auth + production conversation owners.
- **Accepted baseline**: `DEV-native-read-path-0.1.0-b9` remains the merged Stable production native-read baseline until this Work is finalized and merged.
- **Working branch / PR**: `dev/conversation-recovery-20260826`; PR #10 open/unmerged.
- **Current base**: main `3a138ab6378fb72b9b36dedd3df55dc29e2ba814`; pre-b14 compare was `behind_by=0`.
- **Only Active development checkpoint**: yes; no competing branch/candidate owner found when b14 was allocated.
- **Ownership correction**: cold-start login-state recovery belongs to this Work. Do **not** create a separate `DEV-auth-resume` task.

## Runtime history

### b10 core recovery accepted

- `DEV-conversation-recovery-0.1.0-b10`; CI `32982836557`; artifact `9612167843`; IPA SHA `6e600f829fa24cdeb705e9ab104ebb780a8c70dd06871285d06fa30521aecb7e`.
- iPhone/iOS17 accepted loaded-state latest-sync and full reload; no resend/duplicate.

### b11 presentation rejected

- Request paths worked on device, but `navigationItem.prompt` was not visible. This feedback surface is rejected.

### b12 partial acceptance

- Public `WKWebsiteDataStore.default()` warm-up accepted for the tested persisted cold start: 0/0 -> 41/22 cookies in 194.97 ms; unchanged account/list path later succeeded without opening Login.
- Centered sync toast accepted.
- Initial list request was still gated by lazy compact-iPhone sidebar loading, so startup sequencing was rejected.

### b13 real-device result — partial/failing

Identity: `DEV-conversation-recovery-0.1.0-b13`, `0.1.0 (13)`; tested product/config head `fcc74ac4015449dba6c77f3136eede82cec3ec54`; CI `32997544435`; artifact `9617184873`; IPA SHA `2af6334278bcb88683cc123d47617e6956c0efb83aceb9b294961827f3e80040`.

Exact user recording + diagnostics prove:

- Cold launch `18:18:50Z`; warm-up 0/0 -> 39/20 cookies in `177.47 ms`.
- `listLoad.start` occurred at `18:18:51Z`, so b13 **did fix the previous lazy list-start defect**.
- Account context took `17089.96 ms`; complete list load took `22005.52 ms`; list returned HTTP200 28/29 at `18:19:13Z`.
- Despite data finishing around 22 seconds after list-load start, the user still spent close to a minute trying to **enter** the list. Recording + repeated `sidebar.open.requested` logs prove the remaining problem is compact shell/navigation presentation, not delayed list initiation.
- Initial compact surface was the secondary placeholder `新对话 / 从侧边栏选择一个会话`, which is not the useful startup root for the current read-only client.
- Recording visibly showed **two identical top-left sidebar icons**. Current b13 source combined UISplitViewController system compact navigation with a custom `sidebar.left` item, creating duplicate ownership.
- Recovery actions were available during ordinary detail loading as required.
- Ordinary detail generation 1 eventually returned HTTP200 in `9733.60 ms`; manual reload generations 2 and 3 started concurrently and each returned HTTP429 in about 1.1 s. Generation 1 was correctly discarded as `operation_superseded`, proving the freshness guard works but also exposing a separate overlap/rate-limit issue.

## b14 identity / implementation

Candidate:

- **`DEV-conversation-recovery-0.1.0-b14`**
- **`0.1.0 (14)`**
- product/config head **`82d96bf085dbee3877bcb16e27bbf69f4dc0990f`**
- exact head tree **`4d0ddb24ba6e261cdb7a4057ce47e73f199ad481`**

b14 intentionally fixes only the newly evidenced compact startup/navigation defect so this candidate has one clear runtime question:

1. `AppDelegate` performs the already accepted public WebKit warm-up before installing `RootViewController` as the window root.
2. `RootViewController` constructs both split columns synchronously in `init`, before its first compact presentation.
3. As there is no selected conversation at cold start, the split delegate chooses `.primary` as the compact top column. The first real screen should therefore be the conversation list, not the blank secondary `新对话` placeholder.
4. The b13 custom `sidebar.left` button and `show(.primary)` action were removed. UISplitViewController/native compact navigation is the single navigation owner; no duplicate sidebar icon should remain.
5. The sidebar's existing `viewDidLoad -> loadConversations()` still starts the initial list request, but because the whole root shell is only installed after warm-up and primary is the initial compact top column, the request remains sequenced after warm-up and no longer requires a custom sidebar reveal action.
6. Auth endpoint/parser/header behavior, conversation protocol, sync toast and selected-detail generation logic are unchanged from b13.

### b14 CI / Artifact evidence

- CI run **`33000566633`** completed success; build, inspect and upload all passed.
- Synthetic merge **`5b2f60dc8b30ae15d56cbe2d49bbe6b61aff0ad6`**.
- Branch head and synthetic merge share exact tree **`4d0ddb24ba6e261cdb7a4057ce47e73f199ad481`**.
- Artifact **`9618410313`**, name `ChatGPTClient-DEV-conversation-recovery-0.1.0-b14`.
- ZIP digest `sha256:d8c489159d0c68f315d5c9f9c7920cf6349ab76214c740e07cc30d99fbbbeccf`.
- IPA `ChatGPTClient-0.1.0-b14-dev-conversation-recovery.ipa`.
- IPA SHA-256 **`b9100deb1d59b8ce22e15e72f766f0313be2903ec96ed2cda3d397986ba89182`**; generated sidecar matches independently calculated SHA.
- Embedded identity: version `0.1.0`, build `14`, candidate b14, source `5b2f60dc8b30`, minimum iOS14.0, device families `[1,2]`, Mach-O arm64.

## Known defect intentionally not changed in b14

b13 runtime also exposed the HTTP429 overlap when manual recovery starts while the old selected-detail network task is still active. That issue is **not fixed by b14**. The generation guard prevents stale mutation but does not cancel the older request.

Because b14 is already a uniquely built/tested candidate, any product change to cancel/replace an in-flight selected-detail task requires a **new candidate identity after a fresh conflict/build-number check**. Do not reuse b14 and do not describe HTTP429 overlap as solved.

## State owner / invariants

- `ConversationRepository` remains sole production conversation read/recovery owner.
- `AuthSessionStore` and default `WKWebsiteDataStore` contracts are unchanged.
- UISplitViewController/native navigation is the sole compact list/detail navigation owner in b14.
- No retry, timer, watchdog, fallback endpoint/header set, hidden WebView, resend/regenerate or second persistent state store.

## Validation state

- b10: Code + CI + Artifact + Runtime accepted for core recovery.
- b11: Code + CI + Artifact + Runtime; feedback presentation rejected.
- b12: Code + CI + Artifact + Runtime partial accepted — warm-up + centered toast accepted, startup sequencing rejected.
- b13: **Code + CI + Artifact + Runtime/manual tested, partial/failing** — immediate list initiation/freshness guard worked; compact startup/navigation failed; overlapping replacement requests produced HTTP429.
- b14: **Code written + static/source review + CI passed + Artifact produced; Runtime/manual pending**.
- Stable / merged: **no**.

## Next exact action

Install exact b14 on iPhone/iOS17 and test:

1. Force-quit -> launch. After the very short WebKit warm-up, the first product screen should be the **conversation list** immediately, even if rows are still loading; it must not start on `新对话 / 从侧边栏选择一个会话`.
2. Confirm there is **no duplicated pair of sidebar icons**.
3. List loading should begin automatically after warm-up; no sidebar tap should be required to start it.
4. Select a conversation -> detail; native Back/system split navigation should reliably return to the list.
5. Confirm centered sync feedback and ordinary full reload still behave as before.
6. Do not use b14 as proof that the b13 concurrent-manual-recovery HTTP429 issue is fixed; that remains a separate pending correction inside this Work.

If b14 compact startup/navigation is accepted, record Runtime evidence, then allocate a fresh candidate for the minimum selected-detail cancellation/replacement correction unless the user explicitly scopes that defect out.

## Rejected / do-not-repeat

- No separate `DEV-auth-resume` Work.
- No hidden/shadow WebView or persisted copied auth secrets.
- No automatic retry/watchdog/timer/resend/regenerate/fallback chain.
- No `navigationItem.prompt` for required feedback.
- Do not gate list start on sidebar reveal.
- Do not add a second custom compact sidebar button on top of UISplitViewController/native navigation.
- Do not claim the b13 HTTP429 overlap defect is fixed in b14.