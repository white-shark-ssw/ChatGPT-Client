# DEV-conversation-recovery

## Status

**Active — b13 implementation after b12 runtime findings**

- **Work ID**: `DEV-conversation-recovery`
- **Routing aliases / keywords**: `会话同步与重载 / 同步最新消息 / 重载当前会话 / 冷启动登录恢复 / conversation recovery`
- **Task**: Finish explicit manual conversation recovery UX and cold-start usable native-list startup through the accepted WebKit/auth + production conversation owners.
- **Accepted baseline**: `DEV-native-read-path-0.1.0-b9` remains the merged Stable production native-read baseline until this Work is finalized and merged.
- **Working branch / PR**: `dev/conversation-recovery-20260826`; PR #10 open/unmerged.
- **Current branch head before b13 product edits**: `187ef5dbf0dfa44a9bfa064afc5842d571a2a60e`.
- **Current base**: main `3a138ab6378fb72b9b36dedd3df55dc29e2ba814`; compare is `behind_by=0`.
- **Ownership correction**: current main explicitly assigns cold-start login-state recovery to this Work. Do **not** create a separate `DEV-auth-resume` task.

## Accepted b10 core recovery runtime

- Candidate `DEV-conversation-recovery-0.1.0-b10` / `0.1.0 (10)` / source `89129913cb29a35db9dec7a6d5670d1b3b76bc23`.
- CI `32982836557` passed; artifact `9612167843`; IPA SHA-256 `6e600f829fa24cdeb705e9ab104ebb780a8c70dd06871285d06fa30521aecb7e`.
- iPhone / iOS 17.0 accepted loaded-state latest-sync and full reload core behavior. Full reload visibly cleared/rebuilt; two syncs and two reloads ended `status=ok`; no resend/duplicate observed.

## b11 runtime result — request path works, feedback presentation rejected

- Candidate `DEV-conversation-recovery-0.1.0-b11` / `0.1.0 (11)`; CI `32988700796` success; artifact `9613806931`; IPA SHA-256 `6c99a2b34ac5312b82930d1eeaeefb2a373e351325c92b7df7ad37a068316b33`.
- Four syncs all ended `status=ok`; one full reload also ended `status=ok`, but the user saw no `navigationItem.prompt` feedback.
- `navigationItem.prompt` is rejected for required recovery feedback UX.

## b12 identity / build evidence

- Candidate: `DEV-conversation-recovery-0.1.0-b12` / `0.1.0 (12)`.
- Product/config branch head: `fd9fb3ac7a09eafa8dfd33918d114c7d3fee474f`.
- CI run `32993589071` success; synthetic merge `4a7380b913ff5bd847c676fceab31adafdeecb3f`; exact tree `81c801284b1e83f68043c30b9c75f47e76640128`.
- Artifact `9615588166`; IPA `ChatGPTClient-0.1.0-b12-dev-conversation-recovery.ipa`; IPA SHA-256 `2bd24e1dff89d2c04c82e838b44bf9e584d1587534ab6338b33b23bde0861aab`.
- Embedded identity: `0.1.0 (12)`, candidate b12, source `4a7380b913ff`, iOS min 14.0, arm64.

## b12 real-device evidence — 2026-08-27

Exact user export matches b12 Release / iPhone / iOS 17.0 / source `4a7380b913ff`.

### Cold-start WebKit warm-up works for the tested auth state

On the true cold launch at `17:43:20Z`:

- `webDataWarmup.before`: total/matched cookies `0/0`.
- `webDataWarmup.after`: `41/22`, website-data records `7`.
- warm-up completed `status=ok` in `194.97 ms`.
- `nativeConversationShell.loaded` followed at `17:43:21Z`.

When the first native conversation-list request finally started later, it used the warmed `41/22` WebKit cookie state. The normal single account probe succeeded without opening Login first:

- `/api/auth/session` HTTP 200;
- Plus/personal account context verified in `4701.90 ms`;
- list HTTP 200, `28/29`, `23635` bytes;
- list load completed `status=ok` in `9230.67 ms`.

**Conclusion**: b12 proves the public default-WebKit-data-store warm-up can hydrate a usable auth state on this tested cold start. The remaining launch problem is not an auth failure in this export.

### Remaining startup bug: initial list load is lazy behind the hidden sidebar

The same cold launch loaded the native shell at `17:43:21Z`, but **no `listLoad.start` occurred until `17:45:10Z`**, when the user was finally able to enter the sidebar. Source currently starts `loadConversations()` only from `ConversationSidebarViewController.viewDidLoad`; on compact iPhone the primary/sidebar controller is lazily loaded while the secondary empty `新对话` screen is foreground.

The supplied recording matches this state: the app initially shows the empty detail surface, the top-left sidebar affordance is absent/non-responsive for an extended period, and only later does navigation become usable; after entering the sidebar the list then waits for its ~9 s network load.

This is direct evidence to make initial list loading independent of the user opening the primary column.

### b12 sync feedback accepted

The user confirms the centered sync feedback is visible and correct.

Diagnostics also prove both result classes:

- position 1: sync `status=ok`, 257 -> 257 visible messages, zero diff, `2887.02 ms`;
- position 3: sync `status=ok`, 562 -> 563 visible messages, `addedVisibleMessageCount=1`, `6705.75 ms`.

The centered 2-second toast contract is therefore accepted for the tested b12 scope.

## New explicit recovery requirement from b12 test

While a conversation is in its ordinary initial detail-loading state, the overflow actions **must remain available**:

- `同步最新消息`
- `重载当前会话`

Reason: the normal detail request itself can hang/fail; the user wants one explicit manual recovery attempt without waiting for a terminal error state.

This remains user-triggered recovery, not automatic retry machinery.

## b13 candidate allocation

Conflict/identity preflight:

- PR #10 is the only open PR.
- main `current/dev/` has no competing Active checkpoint.
- branch is `behind_by=0` against current main.
- repository search found no existing `DEV-conversation-recovery-0.1.0-b13` reservation.

Reserve **`DEV-conversation-recovery-0.1.0-b13` / `0.1.0 (13)` / `ChatGPTClient-0.1.0-b13-dev-conversation-recovery.ipa`**. Do not reuse b12 after product changes.

## b13 minimum implementation contract

### Startup/list responsiveness

1. After b12 WebKit warm-up completes, force the sidebar controller's initial view/load path to start immediately instead of waiting for the user to reveal the primary column.
2. Keep the background warm-up as accepted from b12; do not add another auth probe/retry loop.
3. Replace dependence on the delayed/system-managed `displayModeButtonItem` with an explicit native top-left sidebar button owned by `RootViewController`; tapping it calls the split controller's primary-column presentation directly.
4. No timer/watchdog is added. The list request simply begins as soon as the warmed shell is configured.

### Manual recovery during an in-flight ordinary load

1. The overflow menu stays enabled when a conversation identity exists even if the ordinary initial detail request is still in flight.
2. A user-triggered sync or reload during that load starts one new explicit recovery request and supersedes the older ordinary detail operation.
3. Add the minimum owner-level detail-operation generation/freshness guard in `ConversationRepository` so an older request completion cannot overwrite or surface an error over the newer manual recovery result.
4. Once a manual recovery action itself is active, disable duplicate manual recovery taps until that action completes. This is presentation/action state only, not a second conversation-data authority.
5. No automatic retry, timeout, watchdog, resend/regenerate, fallback endpoint/header set, or hidden WebView.

The future `DEV-multi-conversation-state` Work may evolve this single-selected-conversation freshness guard into the planned per-conversation/account-scoped mechanism, but b13 implements only the minimum needed for the current explicit retry-during-load requirement.

## State owner / invariants

- `ConversationRepository` remains sole production conversation read/recovery owner.
- `AuthSessionStore` remains the account/native-auth bridge; default `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- UI loading/recovery flags are presentation/action state only.
- No resend/regenerate, automatic retry/watchdog, fallback endpoint/header set, hidden WebView, or second persistent state store.

## Validation state

- b10 core recovery: **Code + CI + Artifact + Runtime/manual/real-device tested**.
- b11: **Code + CI + Artifact + Runtime; feedback presentation rejected**.
- b12: **Code + CI + Artifact + Runtime/manual/real-device tested, partial acceptance**:
  - centered sync toast accepted;
  - background WebKit warm-up successfully hydrates usable auth in tested cold start;
  - initial native list does not auto-start because sidebar view loading is lazy; startup/sidebar UX rejected.
- b13: **candidate reserved; code/CI/artifact/runtime pending**.
- Stable / merged: **no**.

## Next exact action

1. Implement only the b13 startup/list initiation, explicit sidebar button, recovery-during-load enablement, and minimum stale-detail-operation guard.
2. Bump build/candidate/workflow/artifact identity to b13.
3. Review exact diff; run CI; inspect exact IPA identity.
4. Real-device test:
   - force-quit -> launch -> do not tap Login; list request should start automatically and sidebar button should work immediately;
   - while opening a conversation and it still shows `正在读取会话…`, open overflow and invoke one sync or reload; action must run rather than appear gray;
   - verify older initial-load completion cannot overwrite the manual recovery result;
   - verify centered sync toast remains correct.
5. If accepted, update runtime evidence, run final conflict/PR check, merge #10 and complete this Work.

## Rejected / do-not-repeat

- No separate `DEV-auth-resume` Work.
- No hidden/shadow WebView.
- No persisted copied auth secrets.
- No automatic retry/watchdog/resend/regenerate/fallback chain.
- Do not use `navigationItem.prompt` again for required sync feedback.
- Do not gate initial list loading on the primary/sidebar view becoming user-visible.
- Do not allow an older ordinary detail request to overwrite a newer user-triggered recovery result.