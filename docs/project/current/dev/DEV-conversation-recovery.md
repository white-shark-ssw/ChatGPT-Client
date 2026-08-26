# DEV-conversation-recovery

## Status

**Active — b14 compact startup/navigation accepted; selected-detail replacement correction pending**

- **Work ID**: `DEV-conversation-recovery`
- **Routing aliases / keywords**: `会话同步与重载 / 同步最新消息 / 重载当前会话 / 冷启动登录恢复 / conversation recovery`
- **Task**: Finish explicit manual conversation recovery UX and cold-start usable native-list startup through the accepted WebKit/auth + production conversation owners.
- **Accepted baseline**: `DEV-native-read-path-0.1.0-b9` remains the merged Stable production native-read baseline until this Work is finalized and merged.
- **Working branch / PR**: `dev/conversation-recovery-20260826`; PR #10 open/unmerged.
- **Current base**: main `3a138ab6378fb72b9b36dedd3df55dc29e2ba814`; current compare `behind_by=0`.
- **Only Active development checkpoint**: yes at latest scan; no competing branch/candidate owner found when b14 was allocated.
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

Exact user recording + diagnostics proved:

- Cold launch warm-up 0/0 -> 39/20 cookies in `177.47 ms`.
- `listLoad.start` occurred immediately after warm-up, so the previous lazy list-start defect was fixed.
- Account context took `17089.96 ms`; complete list load took `22005.52 ms`; list returned HTTP200 28/29.
- User still spent close to a minute trying to enter the list because compact startup/navigation was wrong: initial surface was `新对话 / 从侧边栏选择一个会话`, duplicate sidebar icons appeared, and repeated custom sidebar taps often did not reveal primary.
- Recovery actions were available during ordinary detail loading as required.
- Freshness generation worked: an older successful detail completion was discarded as `operation_superseded`.
- Separate defect exposed: while ordinary detail generation 1 remained in flight, manual reload generations 2/3 returned HTTP429 in about 1.1 s. Current generation protection prevents stale mutation but does not cancel the replaced network task.

### b14 identity / implementation

- Candidate **`DEV-conversation-recovery-0.1.0-b14`** / **`0.1.0 (14)`**.
- Product/config head **`82d96bf085dbee3877bcb16e27bbf69f4dc0990f`**; exact tree **`4d0ddb24ba6e261cdb7a4057ce47e73f199ad481`**.
- CI run **`33000566633`** success; synthetic merge **`5b2f60dc8b30ae15d56cbe2d49bbe6b61aff0ad6`** shares the exact tree.
- Artifact **`9618410313`**; IPA `ChatGPTClient-0.1.0-b14-dev-conversation-recovery.ipa`; IPA SHA **`b9100deb1d59b8ce22e15e72f766f0313be2903ec96ed2cda3d397986ba89182`**; ZIP digest `sha256:d8c489159d0c68f315d5c9f9c7920cf6349ab76214c740e07cc30d99fbbbeccf`.
- Embedded identity: version `0.1.0`, build `14`, candidate b14, source `5b2f60dc8b30`, minimum iOS14.0, device families `[1,2]`, Mach-O arm64.
- Product changes were intentionally limited to compact shell/navigation: accepted WebKit warm-up runs before product-root installation; split columns are constructed synchronously; no selected conversation starts compact on `.primary`; b13 custom `sidebar.left`/custom `show(.primary)` ownership was removed.
- Auth endpoint/parser/header behavior, list/detail routes, centered sync toast and selected-detail generation logic were unchanged from b13.

### b14 real-device result — accepted for compact startup/navigation scope

User tested the exact b14 candidate on the target iPhone/iOS17 and reported **“这次没问题了”** against the stated b14 gate. Treat the following b14 scope as Runtime/manual accepted:

- cold start now lands on the useful conversation-list root rather than the blank `新对话` secondary placeholder;
- duplicate top-left sidebar icons are no longer present;
- native compact list/detail navigation is usable, including returning from detail to the list;
- no new b14 regression was reported in the unchanged centered sync/full-reload behavior.

This acceptance does **not** cover the b13 HTTP429 selected-detail overlap defect because b14 intentionally did not change that request lifecycle.

## Remaining defect inside this Work

The b13 HTTP429 overlap remains the last known recovery defect in this Work: when explicit manual sync/reload replaces an ordinary selected-detail request that is still in flight, the old network task is currently left active while the replacement request starts.

The minimum next correction should make `ConversationRepository` own the current selected-detail task lifecycle so a newer explicit manual recovery **cancels/replaces the older selected-detail request before starting the replacement request**, while retaining the existing operation-generation guard for late callbacks.

This remains **inside `DEV-conversation-recovery`**, not a new Work ID: it is the same manual-recovery state owner, same source area, same PR dependency, and directly closes a defect exposed while exercising this Work's recovery-during-load contract. A new candidate identity is still required because b14 is already a tested artifact. Do not assume the next build number until a fresh build-index/Active-task conflict check is performed.

## State owner / invariants

- `ConversationRepository` remains sole production conversation read/recovery owner.
- `AuthSessionStore` and default `WKWebsiteDataStore` contracts are unchanged.
- UISplitViewController/native navigation is the sole compact list/detail navigation owner after b14.
- A selected-detail task handle, if added, is request-lifecycle ownership only and must not become a second conversation-data authority.
- No retry, timer, watchdog, fallback endpoint/header set, hidden WebView, resend/regenerate or second persistent state store.

## Validation state

- b10: Code + CI + Artifact + Runtime accepted for core recovery.
- b11: Code + CI + Artifact + Runtime; feedback presentation rejected.
- b12: Code + CI + Artifact + Runtime partial accepted — warm-up + centered toast accepted, startup sequencing rejected.
- b13: **Code + CI + Artifact + Runtime/manual tested, partial/failing** — immediate list initiation/freshness guard worked; compact startup/navigation failed; overlapping replacement requests produced HTTP429.
- b14: **Code + static/source review + CI + Artifact + Runtime/manual accepted for compact startup/navigation**.
- Entire `DEV-conversation-recovery`: **not Stable / not merged** because the selected-detail overlap correction remains pending.

## Next exact action

When the user asks to continue this feature:

1. Re-run the resume identity/conflict guard against current main, PR #10, all Active checkpoints and `BUILD_TEST_INDEX.md`.
2. Keep the same Work ID / branch / PR unless repository truth has changed.
3. Allocate a fresh unique candidate/build identity; do not reuse b14.
4. Implement the minimum selected-detail task cancellation/replacement lifecycle in `ConversationRepository`, retaining generation-based stale-result rejection.
5. Validate that starting one manual recovery during an ordinary detail load cancels/replaces the older selected-detail request rather than intentionally leaving both active; verify centered sync/full reload still behave correctly.
6. Only after real-device acceptance perform final main/PR/conflict check, merge PR #10, update durable status and complete this checkpoint.

## Rejected / do-not-repeat

- No separate `DEV-auth-resume` Work.
- No hidden/shadow WebView or persisted copied auth secrets.
- No automatic retry/watchdog/timer/resend/regenerate/fallback chain.
- No `navigationItem.prompt` for required feedback.
- Do not gate list start on sidebar reveal.
- Do not add a second custom compact sidebar button on top of UISplitViewController/native navigation.
- Do not claim the b13 HTTP429 overlap defect is fixed by b14.
