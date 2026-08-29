# DEV-send-stream

## Status

**Active — b43 hybrid smoothness Runtime largely accepted; b44 integrated native-conversation Send candidate being prepared**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail / 官方 Web / hybrid`
- **Branch / PR**: `dev/send-stream-20260829`; PR #29 open + mergeable.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; Stable native predecessor remains b38.
- **Current real branch head before this docs-only Runtime write**: `fc12cee1f2ce6162dcaf3076534ea3159db7a089`.
- **Parallel guard**: current `docs/project/current/dev/` contains only this Active development checkpoint; no peer Active development task conflict found.

## Security / architecture boundary

Exact b42 `DEV-send-stream-0.1.0-b42`, product source `e8946e48a0b5ad86b402faf5eabba627e3393adf`, legitimate Artifact `9709824510`, proved the tested successful ChatGPT-account Send requires browser anti-abuse challenge output (`proofOfWorkRequired=true`, `turnstileRequired=true`, `soRequired=true`, non-empty PoW + Turnstile finalize input).

Therefore pure-native/transient-auth ChatGPT-account Send remains blocked. Never implement PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoints or hidden challenge-harvesting WebViews.

The user explicitly selected TD-024 / Option 2: **native shell/read/navigation + a user-visible official ChatGPT Web Send surface**.

## Exact b43 identity

- Candidate `DEV-send-stream-0.1.0-b43`, `0.1.0 (43)`.
- Exact product/config source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`.
- Push Run / Job `33241032864` / `99070294478` — success.
- PR Run / Job `33241035013` / `99070299776` — success.
- Artifact `9711364573`; ZIP `sha256:1a9516221ec5ece59741f9f2af2483815f09fa47f051ff6a97a67a12d40d4c23`.
- IPA `ChatGPTClient-0.1.0-b43-dev-send-stream.ipa`; SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.
- Package identity independently verified: `0.1.0 (43)`, Candidate b43, source `f602d68ae95d`, Release, iOS14 minimum, `[1,2]`, arm64.
- Accidental Artifact `9710515489` carrying newer code under stale b42 identity remains permanently rejected and must never be installed/promoted.

## b43 exact-device Runtime result — 2026-08-29

User tested the requested b43 sequence on the primary device and reported **“基本上没什么问题”**.

Accepted / positive observations:

- first visible official-Web hybrid entry: no material problem reported;
- resident return/re-entry: no material problem reported;
- keyboard/typing/ordinary visible Web Send/stream scrolling/rapid scrolling: no material problem reported in the requested sequence;
- native return/regression path: no material problem reported;
- tapping Web `+` to attachment selection showed roughly **100–200 ms** latency, which the user did not reject as excessive.

Runtime defect / new requirement:

- after Web `+` -> photo selection, the system photo library opened but **videos were filtered out**;
- user explicitly requires the media selector not to filter video assets merely because the webpage chose an image-only photo input;
- selection UI capability and service acceptance are separate: current official ChatGPT image-input documentation says image inputs process static images, while generic file docs list documents/spreadsheets/presentations/text and do not establish video processing. A future picker may expose videos, but successful ChatGPT handling of a video remains **Runtime/Service Unverified** until tested.

Evidence classification for b43:

- Code / CI / Artifact / package identity: passed.
- Runtime smoothness / resident visible-Web feasibility: **largely accepted for the tested sequence**.
- Attachment video selection: **rejected limitation / requires follow-up**.
- Final integrated product flow: not accepted; b43 remains a feasibility baseline, not final Send UX.
- Stable/Frozen: No.

## Product direction correction after b43

The user confirmed that a Settings-only standalone Web chat feels like a separate browser feature. That is **not the intended final interaction**.

Target interaction now:

`native conversation list -> native conversation detail -> native send affordance -> visible official-Web layer scoped to the selected conversation -> user sends through official Web -> explicit return/sync to native detail`

Rules:

1. Native conversation/list/detail remains the primary product surface.
2. The standalone Settings hybrid entry is removed from ordinary product UX; protocol diagnostics remain in Settings.
3. Root remains the native navigation owner.
4. The Web surface remains user-visible and uses default persistent `WKWebsiteDataStore`.
5. No DOM message mirroring/scraping, hidden Web transport or challenge harvesting.
6. Native Repository remains sole native conversation/read/recovery authority.
7. Native current conversation may be opened in visible Web using the current public ChatGPT `/c/<conversation-id>` route only as a **b44 Runtime trial**; external 2026 evidence supports that route shape, but exact native-ID -> Web-page alignment must be validated on-device before becoming a durable accepted contract.
8. Do not pass prompt text through guessed URL/query parameters or DOM automation in b44.
9. After Web interaction, reconciliation back to native must remain explicit until there is evidence for a safe send-completion signal; do not silently Sync on every Back navigation.

## b44 planned minimal product scope

Candidate identity to allocate atomically with product code: `DEV-send-stream-0.1.0-b44`, version/build `0.1.0 (44)`.

Planned files only:

- `RootViewController.swift`
  - keep Root as navigation owner;
  - add a native bottom send affordance on the detail navigation controller;
  - from the selected native conversation, push the shared visible Web Send controller for that exact conversation;
  - provide an explicit `返回并同步` action that invokes exactly one existing Repository `syncLatestMessages(id:)` and then re-renders the selected native detail;
  - ordinary Back remains plain navigation and does not auto-Sync.
- `AuthWebViewController.swift`
  - preserve one resident shared WKWebView;
  - accept a selected conversation target and, when needed, visibly navigate to `https://chatgpt.com/c/<conversation-id>` as a Runtime trial;
  - log only safe `targetMatch` / route-class / timing metadata, never raw conversation ID;
  - customize WebKit file-upload open panels with public `WKUIDelegate` APIs and native Photos/Files UI;
  - Photos path must allow **images + videos** so the picker itself does not filter videos;
  - file bytes/names are not logged; video upload/service success remains Unverified.
- `SettingsViewController.swift`
  - remove the ordinary standalone `混合发送` section/button; keep diagnostic Send probe controls.
- `ChatGPTClient.xcodeproj/project.pbxproj` + `.github/workflows/ios-foundation.yml`
  - atomically move identity to b44 with the product changes before any product-path push.

No `ConversationFeature.swift` or Stable b38 geometry change is planned for b44.

## b44 exact-device Runtime gate

1. Open a native conversation and tap the new native send affordance; visible Web opens directly in the selected-conversation flow rather than via Settings.
2. Verify the Web page corresponds to the same selected conversation; diagnostics should record target match without raw IDs.
3. Type/send normally; keyboard and streaming scroll remain at least as smooth as b43.
4. Tap `+` and choose the media path; native picker should show both photos and videos and should present promptly.
5. Select one ordinary photo and verify ordinary upload/send still works.
6. Select one video only to establish actual service behavior; if ChatGPT rejects it, record that as a service capability boundary rather than hiding videos in the picker.
7. Use explicit `返回并同步`; exactly one native reconciliation request occurs and the native detail reflects current server state without duplicate message authority.
8. Ordinary Back without `返回并同步` must not trigger an automatic Sync.
9. Stable native list/detail/long-conversation/round-navigation behavior must remain intact.

## Candidate / write-chain rule

- b39-b43 are permanently reserved.
- Do not modify product paths while workflow/Xcode still carry b43.
- Prepare Root/AuthWeb/Settings + Xcode build44 + workflow b44 as one Git-data tree/commit, then non-force fast-forward branch once.
- If that atomic b44 Artifact emits, any corrected product code after emission must use b45 or later.

## Next exact action

Inspect current Root/AuthWeb/Settings definitions, construct the minimal b44 changes above, combine them atomically with b44 Xcode/workflow identity, fast-forward the real branch without force, then verify CI/Artifact/package identity and hand exact b44 to the user for the integrated native-conversation + media-picker Runtime matrix.