# DEV-conversation-recovery

## Status

**Active — b12 real-device gate**

- **Work ID**: `DEV-conversation-recovery`
- **Routing aliases / keywords**: `会话同步与重载 / 同步最新消息 / 重载当前会话 / 冷启动登录恢复 / conversation recovery`
- **Task**: Finish explicit manual conversation recovery UX and the now-owned cold-start background login-state recovery through the accepted WebKit/auth owner.
- **Accepted baseline**: `DEV-native-read-path-0.1.0-b9` remains the merged Stable production native-read baseline until this Work is finalized and merged.
- **Working branch / PR**: `dev/conversation-recovery-20260826`; PR #10 open/unmerged.
- **Base sync**: main `3a138ab6378fb72b9b36dedd3df55dc29e2ba814` contained planning/governance changes only. Branch synchronized them via merge `465de1b20d52044f20b045ccb4b7c41f5639eea7`; latest compare before b12 docs updates was `behind_by=0`.
- **Ownership correction**: current main explicitly assigns cold-start login-state recovery to this Work. Do **not** create a separate `DEV-auth-resume` task.

## Accepted b10 core recovery runtime

- Candidate `DEV-conversation-recovery-0.1.0-b10` / `0.1.0 (10)` / source `89129913cb29a35db9dec7a6d5670d1b3b76bc23`.
- CI `32982836557` passed; artifact `9612167843`; IPA SHA-256 `6e600f829fa24cdeb705e9ab104ebb780a8c70dd06871285d06fa30521aecb7e`.
- iPhone / iOS 17.0 accepted loaded-state latest-sync and full reload core behavior. Full reload visibly cleared/rebuilt; two syncs and two reloads ended `status=ok`; no resend/duplicate observed.

## b11 runtime result — request path works, feedback presentation rejected

- Candidate `DEV-conversation-recovery-0.1.0-b11` / `0.1.0 (11)`; CI `32988700796` success; artifact `9613806931`; IPA SHA-256 `6c99a2b34ac5312b82930d1eeaeefb2a373e351325c92b7df7ad37a068316b33`.
- Exact export: Release, iPhone/iOS 17.0, candidate b11, source `7fe8ca7693e9`.
- User saw **no visible sync prompt**. `navigationItem.prompt` is therefore rejected for required feedback UX.
- Four syncs all ended `status=ok` with 275 visible messages and zero added/removed/changed messages: 2896.33 ms, 2991.85 ms, 3923.34 ms, 3327.18 ms. One full reload also ended `status=ok` in 2856.27 ms.
- b11 remains valid Code+CI+Artifact+Runtime evidence for the request path, but is **not accepted/Stable** for final feedback presentation.

## Cold-start evidence owned by this Work

- User confirms b11 cold launch still requires tapping `登录 / 账户验证`; b11 did not change auth.
- Prior evidence showed a true cold launch can expose default `WKHTTPCookieStore` as 0/0 and unusable `/api/auth/session` fields until real WebKit activity hydrates the default store.
- New b11 export starts when login is opened. After visible WebKit navigation, cookies are 47/28 then 49/30; three immediate probes fail at session transport with `NSURLErrorDomain -1005`; a later normal list-triggered probe succeeds with 48/29 cookies, session HTTP 200, Plus/personal account context and list HTTP 200 28/29.
- `-1005` is **not** evidence for an automatic retry loop. b12 tests background default-data-store initialization before the normal probe instead.

## b12 identity / implementation

- Conflict scan: PR #10 is the only open PR; no competing Active checkpoint on main; no prior b12 branch/commit reservation.
- Candidate: **`DEV-conversation-recovery-0.1.0-b12` / `0.1.0 (12)` / `ChatGPTClient-0.1.0-b12-dev-conversation-recovery.ipa`**.
- Exact product/config branch head for CI: `fd9fb3ac7a09eafa8dfd33918d114c7d3fee474f`.
- Exact tree: `81c801284b1e83f68043c30b9c75f47e76640128`.

### Centered sync feedback

- `ConversationDetailViewController` replaces the rejected navigation prompt with a centered native toast.
- Sync start shows `正在同步最新消息…` for the duration of the one request.
- Success shows `已是最新` when unchanged or `已同步最新消息` when changed, centered for **2.0 seconds**.
- Failure hides the toast and keeps the existing explicit failure alert.
- The 2-second delayed hide is presentation-only; it does not drive network/recovery correctness.

### Cold-start background WebKit warm-up

- `AuthSessionStore.warmDefaultWebDataStore` uses only public WebKit APIs on `WKWebsiteDataStore.default()`:
  - safe cookie counts before;
  - `fetchDataRecords(ofTypes: WKWebsiteDataStore.allWebsiteDataTypes())`;
  - safe cookie counts after;
  - record count and duration diagnostics.
- `RootViewController` now completes that warm-up **before installing the sidebar/detail shell**. The sidebar's existing initial `loadConversations()` then performs the **single existing account-context probe**.
- Existing `/api/auth/session`, accounts parser, transient native session semantics, endpoints and headers are unchanged.
- Default `WKWebsiteDataStore` remains the sole persistent auth-secret authority.
- No hidden/shadow `WKWebView`, copied-token/cookie persistence, new auth store, retry/watchdog loop or automatic visible login navigation.
- If warm-up + the one existing probe fails, the existing explicit error UI with `登录 / 账户验证` remains the foreground fallback.
- This is still an **experiment** until true cold-start device evidence proves whether public data-store warm-up is sufficient.

## b12 source/static review

From pre-b12 checkpoint `b97cb3a346cb1d02509229136b5020869612c5f2` to product/config head `fd9fb3ac7a09eafa8dfd33918d114c7d3fee474f`, only six files changed:

- `AuthSessionStore.swift`: warm-up helper only.
- `RootViewController.swift`: sequence shell installation after warm-up.
- `ConversationFeature.swift`: centered toast replacing navigation prompt.
- `project.pbxproj`: build 12 / b12 candidate.
- `scripts/build_ipa.sh`: b12 default candidate.
- `.github/workflows/ios-foundation.yml`: b12 candidate/artifact identity.

No unrelated product refactor was introduced.

## b12 CI / Artifact evidence

- CI run: **`32993589071`**, completed success; all build/inspect/upload steps passed.
- PR head: `fd9fb3ac7a09eafa8dfd33918d114c7d3fee474f`.
- GitHub synthetic merge used by build: `4a7380b913ff5bd847c676fceab31adafdeecb3f`.
- Branch head and tested merge both point to exact tree **`81c801284b1e83f68043c30b9c75f47e76640128`**; tested content is exact for current b12 product/config source.
- Artifact ID: **`9615588166`**; artifact name `ChatGPTClient-DEV-conversation-recovery-0.1.0-b12`.
- ZIP digest: `sha256:867c256314f7581f5550717287a604f22c6f55ba60ce659638406e5d34082aac`.
- IPA: `ChatGPTClient-0.1.0-b12-dev-conversation-recovery.ipa`.
- IPA SHA-256: **`2bd24e1dff89d2c04c82e838b44bf9e584d1587534ab6338b33b23bde0861aab`**; generated sidecar matches independently calculated SHA.
- Embedded identity independently verified: version `0.1.0`, build `12`, candidate `DEV-conversation-recovery-0.1.0-b12`, source `4a7380b913ff`, minimum OS `14.0`, device families `[1,2]`; executable Mach-O arm64.

## State owner / invariants

- `ConversationRepository` remains sole production conversation read/recovery owner.
- `AuthSessionStore` remains the accepted account-context/native-auth bridge; default `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- No resend/regenerate, automatic retry/watchdog, fallback endpoint/header set, hidden WebView, or second persistent state store.

## Validation state

- b10 core recovery: **Code + CI + Artifact + Runtime/manual/real-device tested**.
- b11: **Code + static review + CI + Artifact + Runtime tested; feedback presentation rejected**.
- b12: **Code written + static/source review + CI passed + Artifact produced; Runtime/manual/real-device pending**.
- Stable / merged: **no**.

## Next exact action

Install exact b12 and test on iPhone / iOS 17.0:

1. **True cold start without tapping Login first**: force-quit App, launch, wait for initial native list. Expected path is `webDataWarmup` -> shell install -> one normal account probe -> list load. Do not enter the visible login page before judging this test.
2. If the native list still reaches the login/error state, export diagnostics **before tapping Login** so the b12 warm-up before/after counts and single probe result are preserved.
3. Open a loaded conversation and tap `同步最新消息`: centered `正在同步最新消息…` must be visible while loading; then centered `已是最新` or `已同步最新消息` must remain visible for about 2 seconds.
4. Confirm `重载当前会话` still clears/rebuilds normally.
5. If both cold start and feedback are accepted, update Runtime evidence, final conflict/PR check, merge #10 and complete/archive this Work. If cold-start warm-up fails, preserve b12 as partial/failing Runtime evidence and diagnose from the exported facts without adding retries by guess.

## Rejected / do-not-repeat

- No separate `DEV-auth-resume` Work.
- No hidden/shadow WebView.
- No persisted copied auth secrets.
- No automatic retry/watchdog/resend/regenerate/fallback chain.
- Do not use `navigationItem.prompt` again for required sync feedback.
- Do not treat `NSURLErrorDomain -1005` as proof that retrying is the correct recovery mechanism.
