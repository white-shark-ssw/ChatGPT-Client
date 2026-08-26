# DEV-conversation-recovery

## Status

**Active — b13 real-device gate**

- **Work ID**: `DEV-conversation-recovery`
- **Routing aliases / keywords**: `会话同步与重载 / 同步最新消息 / 重载当前会话 / 冷启动登录恢复 / conversation recovery`
- **Task**: Finish explicit manual conversation recovery UX and cold-start usable native-list startup through the accepted WebKit/auth + production conversation owners.
- **Accepted baseline**: `DEV-native-read-path-0.1.0-b9` remains the merged Stable production native-read baseline until this Work is finalized and merged.
- **Working branch / PR**: `dev/conversation-recovery-20260826`; PR #10 open/unmerged.
- **Current base**: main `3a138ab6378fb72b9b36dedd3df55dc29e2ba814`; product/config pre-CI compare was `behind_by=0`.
- **Ownership correction**: cold-start login-state recovery belongs to this Work. Do **not** create a separate `DEV-auth-resume` task.

## Accepted / rejected runtime history

### b10 core recovery accepted

- `DEV-conversation-recovery-0.1.0-b10` / source `89129913cb29a35db9dec7a6d5670d1b3b76bc23`.
- CI `32982836557`; artifact `9612167843`; IPA SHA `6e600f829fa24cdeb705e9ab104ebb780a8c70dd06871285d06fa30521aecb7e`.
- iPhone/iOS17 accepted loaded-state latest-sync and full reload; no resend/duplicate.

### b11 presentation rejected

- CI `32988700796`; artifact `9613806931`; IPA SHA `6c99a2b34ac5312b82930d1eeaeefb2a373e351325c92b7df7ad37a068316b33`.
- Request paths worked on device, but user saw no `navigationItem.prompt`; this feedback surface is rejected.

### b12 partial runtime acceptance

Identity: `DEV-conversation-recovery-0.1.0-b12`, `0.1.0 (12)`, source `4a7380b913ff`, iPhone/iOS17.

The user-provided exact export shows:

- true cold start `webDataWarmup.before = 0/0` cookies;
- after public `WKWebsiteDataStore.default()` initialization: `41/22`, 7 website-data records;
- warm-up `status=ok`, `194.97 ms`;
- later normal account probe used the warmed state and succeeded without opening Login: session HTTP 200, Plus/personal verified in `4701.90 ms`;
- list HTTP 200, 28/29, 23635 bytes; list load `9230.67 ms`.

**Accepted conclusion**: for this tested cold start, the b12 public WebKit warm-up successfully hydrates usable persisted auth state. No hidden WebView or copied persistent secret store is needed for this run.

**Remaining b12 startup defect**: `nativeConversationShell.loaded` occurred at `17:43:21Z`, but `listLoad.start` did not occur until `17:45:10Z`. Source ties first list load to `ConversationSidebarViewController.viewDidLoad`, and compact iPhone lazily loads the primary/sidebar controller. The user's recording matches this: initial `新对话` detail surface has unavailable/ineffective sidebar navigation; only later can the user enter the sidebar, after which list loading begins.

**Sync feedback accepted**: user confirms centered b12 toast is correct. Diagnostics exercised both unchanged (257 -> 257, zero diff) and changed (562 -> 563, +1 visible message) sync results.

Therefore b12 is **Code + CI + Artifact + Runtime/manual tested, partial acceptance**: auth warm-up + centered sync feedback accepted; initial list/sidebar sequencing rejected.

## New explicit requirement from b12 test

During an ordinary initial conversation detail load, overflow `同步最新消息` and `重载当前会话` must remain enabled. A stuck normal request is itself a recovery use case, so the user must be able to start one explicit manual recovery without waiting for terminal failure.

This remains user-triggered recovery, not automatic retry machinery.

## b13 identity / implementation

Candidate reserved and built:

- **`DEV-conversation-recovery-0.1.0-b13`**
- version/build **`0.1.0 (13)`**
- IPA `ChatGPTClient-0.1.0-b13-dev-conversation-recovery.ipa`
- product/config branch head **`fcc74ac4015449dba6c77f3136eede82cec3ec54`**

### Startup/list responsiveness

- Keep the b12 public WebKit warm-up unchanged.
- After warm-up and shell installation, `RootViewController` calls `sidebarViewController.loadViewIfNeeded()` so the sidebar's existing `viewDidLoad -> loadConversations()` starts immediately; first list loading is no longer gated on user revealing the primary column.
- Replace the delayed/system-managed detail `displayModeButtonItem` dependency with an explicit native top-left sidebar button. It logs `sidebar.open.requested` and calls `show(.primary)`.
- No timer/watchdog/retry was introduced.

### Manual recovery during an in-flight ordinary detail load

- Overflow sync/reload availability now depends on selected conversation identity and whether a **manual** recovery action is already active, not on ordinary `loadingConversationID` or whether detail is already loaded.
- One user-triggered sync/reload can therefore start while `正在读取会话…` is still shown.
- Duplicate manual recovery taps are disabled until that manual action completes.
- `ConversationRepository` owns `selectedDetailOperationGeneration`. Every selected detail operation gets one generation; when a newer manual recovery starts, any older ordinary detail completion is discarded with `reason=operation_superseded` and cannot overwrite/surface stale error over the newer result.
- Selection change remains a separate discard reason.
- This generation is a minimum current single-selected-conversation freshness guard, not a second conversation-state authority. Future `DEV-multi-conversation-state` may generalize it into account-scoped per-conversation freshness.

## b13 source/static review

From the b13 runtime checkpoint `fa2b7ef0ed50d0e37574c56067d1280e7a6094e2` to product/config head `fcc74ac4015449dba6c77f3136eede82cec3ec54`, only five files changed:

- `ConversationFeature.swift`: recovery-during-load + selected-detail generation guard.
- `RootViewController.swift`: immediate sidebar view/list initialization + explicit sidebar action.
- `project.pbxproj`: build 13 / candidate b13.
- `scripts/build_ipa.sh`: b13 default candidate.
- `.github/workflows/ios-foundation.yml`: b13 artifact identity.

No auth endpoint/parser/header change and no unrelated product refactor.

## b13 CI / Artifact evidence

- CI run **`32997544435`** completed success; build, artifact inspection and upload all passed.
- PR product/config head: `fcc74ac4015449dba6c77f3136eede82cec3ec54`.
- GitHub synthetic merge: `57187c0d0fd3116f964248a87f1a766268637788`.
- Branch head and tested merge share exact tree **`2068ab4dc8f4bd9f94f1cb89e21b8dab29436ebf`**.
- Artifact **`9617184873`**, name `ChatGPTClient-DEV-conversation-recovery-0.1.0-b13`.
- ZIP digest `sha256:7d7d1faa4e69f8892df2d2c2b944f7ada36cb252c50dd0ddd238ecc05c7baf27`.
- IPA SHA-256 **`2af6334278bcb88683cc123d47617e6956c0efb83aceb9b294961827f3e80040`**; sidecar matches independently calculated SHA.
- Embedded identity verified: `0.1.0 (13)`, candidate b13, source `57187c0d0fd3`, minimum iOS 14.0, device families `[1,2]`, Mach-O arm64.

## State owner / invariants

- `ConversationRepository` remains sole production conversation read/recovery owner.
- `AuthSessionStore` remains the account/native-auth bridge; default `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- UI recovery busy flag is presentation/action state only.
- No resend/regenerate, automatic retry/watchdog/timer, fallback endpoint/header set, hidden WebView, or second persistent state store.

## Validation state

- b10: Code + CI + Artifact + Runtime accepted for core recovery.
- b11: Code + CI + Artifact + Runtime; feedback presentation rejected.
- b12: **Code + CI + Artifact + Runtime/manual tested, partial accepted** — warm-up and centered toast accepted, startup/list sequencing rejected.
- b13: **Code written + static/source review + CI passed + Artifact produced; Runtime/manual pending**.
- Stable / merged: **no**.

## Next exact action

Install exact b13 on iPhone/iOS17 and test:

1. Force-quit -> launch; do **not** tap Login. The list request should start automatically after warm-up even if the sidebar has not been opened yet.
2. The top-left sidebar action should be present/usable immediately; opening it may show a still-loading list, but opening it must not be what starts the request.
3. Select a conversation and while `正在读取会话…` is still visible, open `...`; both `同步最新消息` and `重载当前会话` must be enabled.
4. Invoke one manual recovery before the ordinary load returns. The manual result must win; if the older load later finishes, diagnostics should show `detail.discarded reason=operation_superseded` rather than UI overwrite.
5. Confirm centered sync toast remains correct and full reload still clears/rebuilds.
6. If accepted, record Runtime evidence, perform final main/PR/conflict check, merge PR #10 and complete this Work; then start `DEV-multi-conversation-state`.

## Rejected / do-not-repeat

- No separate `DEV-auth-resume` Work.
- No hidden/shadow WebView.
- No persisted copied auth secrets.
- No automatic retry/watchdog/timer/resend/regenerate/fallback chain.
- Do not use `navigationItem.prompt` for required sync feedback.
- Do not gate initial list loading on primary/sidebar view becoming visible.
- Do not let an older ordinary detail operation overwrite a newer manual recovery result.