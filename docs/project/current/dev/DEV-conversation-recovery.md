# DEV-conversation-recovery

## Status

**Active — b11 real-device feedback check pending**

- **Work ID**: `DEV-conversation-recovery`
- **Routing aliases / keywords**: `会话同步与重载 / 同步最新消息 / 重载当前会话 / conversation recovery`
- **Task**: Implement explicit manual `同步最新消息` and complete `重载当前会话` through the authoritative production conversation owner, including the runtime-discovered sync-result feedback gap.
- **Accepted baseline**: `DEV-native-read-path-0.1.0-b9` remains the merged Stable production native-read baseline until recovery is finalized and merged.
- **Working branch / PR**: `dev/conversation-recovery-20260826`; PR #10 open/unmerged; base `main@a43762d255e699a753011103b7e1a6bb5416cb30`; latest branch compare before this docs-only update was `behind_by=0`.

## b10 accepted core runtime

- Candidate `DEV-conversation-recovery-0.1.0-b10` / `0.1.0 (10)` / product source `89129913cb29a35db9dec7a6d5670d1b3b76bc23`.
- CI run `32982836557` passed; artifact `9612167843`; IPA SHA-256 `6e600f829fa24cdeb705e9ab104ebb780a8c70dd06871285d06fa30521aecb7e`.
- User tested exact b10 on iPhone / iOS 17.0 and reported no functional problems. Full reload visibly cleared the current content, showed reload state, then rebuilt the same conversation.
- Diagnostics confirm two loaded-state latest-syncs and two full reloads ended `status=ok`; both tested syncs had zero visible diff, which exposed only the missing completion-feedback UX. No resend/duplicate observed.

## b11 implementation

- Candidate: **`DEV-conversation-recovery-0.1.0-b11` / `0.1.0 (11)` / `ChatGPTClient-0.1.0-b11-dev-conversation-recovery.ipa`**.
- Feedback product change is limited to `ConversationFeature.swift`, 21 additions / 0 deletions from the pre-b11 checkpoint.
- Manual latest sync now shows `正在同步最新消息…`, then `已是最新` when visible messages are unchanged or `已同步最新消息` when changed. Result prompt auto-clears after 1.5 s and is presentation-only.
- `ConversationRepository`, endpoints, headers, auth, recovery request semantics and authoritative state ownership are unchanged.

## b11 CI / artifact evidence

- Initial run `32987959118` is **not accepted b11 artifact evidence** even though it compiled successfully: it checked out intermediate commit `512a2c5280f0109cdd52fdf73fed5f8300ed6c23` before final build-number/workflow metadata. Its artifact was named `ChatGPTClient-DEV-conversation-recovery-0.1.0-b10`, embedded `CFBundleVersion=10` with candidate `DEV-conversation-recovery-0.1.0-b11`, and therefore had inconsistent identity. Do not distribute or reuse it.
- Final PR run **`32988700796`** completed **success** against current PR head `c3490eb67f8d8218281b30560a5c20b3d846c931` using GitHub synthetic merge commit `7fe8ca7693e9e8daa5fa80c9b8c600215e443cf3`.
- Synthetic merge commit tree SHA and branch-head tree SHA are identical: **`80cd8e60977bbcc8dc2dc83881a58afb29a51bde`**. Therefore the final CI tested the same source/config tree as the branch head.
- Artifact ID **`9613806931`**, artifact name `ChatGPTClient-DEV-conversation-recovery-0.1.0-b11`, ZIP digest `sha256:70bb214d01bcf7f2a57df25f10c2280f5dce5482d06b545a168b4963f3b2ee2f`.
- Downloaded IPA: `ChatGPTClient-0.1.0-b11-dev-conversation-recovery.ipa`; sidecar and independently calculated SHA-256 both equal **`6c99a2b34ac5312b82930d1eeaeefb2a373e351325c92b7df7ad37a068316b33`**.
- Embedded identity independently inspected: `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=11`, `DiagnosticsCandidate=DEV-conversation-recovery-0.1.0-b11`, `DiagnosticsSourceCommit=7fe8ca7693e9`, minimum OS `14.0`, device families `[1,2]`; executable is Mach-O arm64.

## Separate auth-resume evidence / direction

- Cold app launch repeatedly reports default WebKit cookie store `itemCount=0/matchedItemCount=0`; `/api/auth/session` returns HTTP 200 but lacks required session fields. After a real visible `WKWebView` navigation, the same default store hydrates to dozens of cookies and account verification succeeds.
- User wants normal cold-start verification fully background/invisible.
- After recovery completes, create a separate auth-resume Work. First experiment must test public `WKWebsiteDataStore.default()` background warm-up/data-record + cookie-store initialization, then perform one normal account probe. No hidden/shadow `WKWebView`, no persisted copied Cookie/token/session secrets, no retry/watchdog loop. Visible official verification is fallback only if background warm-up is proven insufficient.

## Validation state

- b10 recovery core: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**.
- b11 feedback: **Code written + static/source diff reviewed + CI passed + Artifact produced**.
- b11 Runtime/manual/real-device tested: **pending**.
- Stable / merged: **no** until b11 sync-feedback is confirmed on device and final merge-time checks pass.

## Next exact action

Install exact b11 IPA and test one loaded conversation:
1. Tap `同步最新消息` and confirm `正在同步最新消息…` is visible while the request is active.
2. When there is no server-visible change, confirm it becomes `已是最新` and clears automatically.
3. If a changed conversation is available naturally, confirm success feedback becomes `已同步最新消息`; do not manufacture/re-send a prompt only for this test.
4. Confirm existing `重载当前会话` behavior remains normal.

If accepted: record runtime evidence, run final base/PR/conflict check, merge PR #10, archive/complete this checkpoint, then start the separate auth-resume Work before or according to the latest serialized roadmap/conflict scan.

## Rejected / do-not-repeat

- No hidden/shadow WebView.
- No persisted copied auth secrets.
- No automatic retry/watchdog/resend/regenerate/fallback chain.
- Do not treat intermediate run `32987959118` as valid final b11 artifact evidence.
- Do not make the sync-feedback timer part of network/recovery correctness.
