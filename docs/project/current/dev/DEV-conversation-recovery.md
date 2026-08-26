# DEV-conversation-recovery

## Status

**Active — b12 implementation pending**

- **Work ID**: `DEV-conversation-recovery`
- **Routing aliases / keywords**: `会话同步与重载 / 同步最新消息 / 重载当前会话 / 冷启动登录恢复 / conversation recovery`
- **Task**: Finish explicit manual conversation recovery UX and the now-owned cold-start background login-state recovery through the accepted WebKit/auth owner.
- **Accepted baseline**: `DEV-native-read-path-0.1.0-b9` remains the merged Stable production native-read baseline until this Work is finalized and merged.
- **Working branch / PR**: `dev/conversation-recovery-20260826`; PR #10 open/unmerged.
- **Latest base sync**: main advanced to `3a138ab6378fb72b9b36dedd3df55dc29e2ba814` with four planning/governance commits only. They add/adjust `BACKGROUND_EXECUTION_PLAN.md`, `CLIENT_ARCHITECTURE_GAP_REVIEW.md`, `MULTI_CONVERSATION_STATE_PLAN.md`, `START_HERE.md`, `PROJECT_SPECIFIC_RULES.md`, and `TECHNICAL_DECISIONS.md`; no product/build source changed. Branch synchronized these updates through merge commit `465de1b20d52044f20b045ccb4b7c41f5639eea7`; compare after merge is `behind_by=0`.
- **Latest ownership correction**: main now explicitly says cold-start login-state recovery belongs to this active `DEV-conversation-recovery` Work. Do **not** create a separate `DEV-auth-resume` task. The older checkpoint/PR wording proposing a separate auth task is superseded.

## Accepted b10 core recovery runtime

- Candidate `DEV-conversation-recovery-0.1.0-b10` / `0.1.0 (10)` / product source `89129913cb29a35db9dec7a6d5670d1b3b76bc23`.
- CI run `32982836557` passed; artifact `9612167843`; IPA SHA-256 `6e600f829fa24cdeb705e9ab104ebb780a8c70dd06871285d06fa30521aecb7e`.
- Exact b10 on iPhone / iOS 17.0 accepted loaded-state latest-sync and full reload core behavior. Full reload visibly cleared/rebuilt the same conversation; diagnostics confirmed two syncs and two reloads `status=ok`; no resend/duplicate observed.

## b11 evidence and runtime rejection reason

- Candidate `DEV-conversation-recovery-0.1.0-b11` / `0.1.0 (11)` / final run `32988700796` success / artifact `9613806931` / IPA SHA-256 `6c99a2b34ac5312b82930d1eeaeefb2a373e351325c92b7df7ad37a068316b33`.
- Exact device export identity: Release, iPhone/iOS 17.0, candidate b11, source `7fe8ca7693e9`.
- User reports **no visible sync prompt**. The b11 navigation-bar `navigationItem.prompt` presentation therefore fails the required UX even though sync itself works.
- Device diagnostics confirm four latest-sync executions on one loaded conversation all completed `status=ok` with 275 visible messages and zero added/removed/changed messages. Durations: 2896.33 ms, 2991.85 ms, 3923.34 ms, 3327.18 ms. One full reload in the same export also completed `status=ok` in 2856.27 ms.
- Conclusion: b11 is valid Code+CI+Artifact and runtime evidence for the request path, but **not accepted for final sync-feedback UX**. Do not merge/mark Stable from b11.

## Cold-start evidence now owned by this Work

- User confirms b11 cold launch still requires tapping `登录 / 账户验证`; b11 intentionally did not change auth.
- Prior accepted diagnostics established the cold-start class: default `WKHTTPCookieStore` can initially report 0/0 and `/api/auth/session` can return unusable session fields until real WebKit activity hydrates the default store.
- New b11 export begins when the user opens login. After visible WebKit navigation, cookie counts are already 47/28 then 49/30. Three immediate account probes fail at session transport with `NSURLErrorDomain -1005`; a later list-triggered normal account probe succeeds with 48/29 cookies, `/api/auth/session` HTTP 200, Plus/personal account context, then list HTTP 200 28/29.
- Do not convert the `-1005` observations into an automatic retry loop. The next experiment is specifically **default WebKit data-store background warm-up followed by one normal account probe**.

## b12 candidate allocation

- Conflict/identity preflight: PR #10 is the only open PR; main `current/dev/` has no competing Active checkpoint; this branch has only this Active checkpoint; branch/commit search found no existing `b12` reservation.
- Reserve **`DEV-conversation-recovery-0.1.0-b12` / `0.1.0 (12)` / `ChatGPTClient-0.1.0-b12-dev-conversation-recovery.ipa`**. Do not reuse b11 for changed product code.

## b12 minimum implementation contract

### Sync feedback

- Replace navigation-bar prompt feedback with an unmistakable **screen-centered native toast** in the conversation detail view.
- On tap, show `正在同步最新消息…` centered and keep it visible while the one sync request is active.
- On success, replace it with `已是最新` when visible content is unchanged or `已同步最新消息` when changed.
- Success result remains centered for **2.0 seconds**, then disappears. The 2-second timer is presentation-only and does not drive network/recovery correctness.
- On failure, remove the progress toast and preserve the existing explicit failure alert.

### Cold-start background login-state recovery

- Keep default `WKWebsiteDataStore` as the **sole persistent auth-secret authority**.
- Add a bounded public-API warm-up owned by `AuthSessionStore`: initialize `WKWebsiteDataStore.default()`, fetch website-data records, then read its `httpCookieStore`; record safe record/cookie counts and duration only.
- `ConversationRepository` uses that warm-up **once before its normal account-context probe whenever it has no transient session**. No second probe, no retry loop, no hidden/shadow `WKWebView`, no copied-token/cookie persistence, no new auth store.
- If the warm-up + single normal probe still fails, preserve the existing explicit error state with `登录 / 账户验证` as the foreground fallback; do not silently navigate a web view.
- This b12 is an experiment until exact real-device cold-start evidence proves whether public data-store warm-up hydrates the usable WebKit state.

## State owner / invariants

- `ConversationRepository` remains the sole production conversation read/recovery owner.
- `AuthSessionStore` remains the accepted account-context/native-auth bridge; default `WKWebsiteDataStore` remains the only persistent auth-secret authority.
- No resend/regenerate, automatic retry/watchdog, fallback endpoint/header set, hidden WebView, or second persistent state store.

## Validation state

- b10 core recovery: **Code + CI + Artifact + Runtime/manual/real-device tested**.
- b11 feedback/request path: **Code + static review + CI + Artifact + Runtime tested, but feedback presentation rejected**.
- b12: **candidate reserved; code/CI/artifact/runtime pending**.
- Stable / merged: **no**.

## Next exact action

1. Implement only the centered 2-second sync toast and background default-data-store warm-up + single existing account probe.
2. Bump build/candidate/workflow/artifact identity to b12.
3. Review exact diff; run CI and inspect exact IPA identity.
4. Real-device test a true cold launch **without tapping login first** and one manual latest-sync.
5. If background warm-up does not recover auth, export diagnostics before changing strategy; do not add retries by guess.

## Rejected / do-not-repeat

- No separate `DEV-auth-resume` Work; latest main planning explicitly folded cold-start auth into this Work.
- No hidden/shadow WebView.
- No persisted copied auth secrets.
- No automatic retry/watchdog/resend/regenerate/fallback chain.
- Do not use navigation-bar `navigationItem.prompt` again for required sync feedback.
- Do not treat `NSURLErrorDomain -1005` as proof that retrying is the correct recovery mechanism.
