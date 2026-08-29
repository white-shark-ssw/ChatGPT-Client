# DEV-send-stream

## Status

**Active — b43 hybrid smoothness Runtime largely accepted; b44 integrated native-conversation Send candidate being prepared**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail / 官方 Web / hybrid`
- **Branch / PR**: `dev/send-stream-20260829`; PR #29 open + mergeable.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; Stable native predecessor remains b38.
- **Resume head before b43 Runtime docs**: `fc12cee1f2ce6162dcaf3076534ea3159db7a089`.
- **Parallel guard**: current `docs/project/current/dev/` contains only this Active development checkpoint; no peer Active dev conflict found.

## Security / architecture boundary

Exact b42 `DEV-send-stream-0.1.0-b42`, product source `e8946e48a0b5ad86b402faf5eabba627e3393adf`, legitimate Artifact `9709824510`, proved the tested successful ChatGPT-account Send requires browser anti-abuse challenge output (`proofOfWorkRequired=true`, `turnstileRequired=true`, `soRequired=true`, non-empty PoW + Turnstile finalize input).

Therefore pure-native/transient-auth ChatGPT-account Send remains blocked. Never implement PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoints or hidden challenge-harvesting WebViews.

The user explicitly selected TD-024 / Option 2: **native shell/read/navigation + a user-visible official ChatGPT Web Send surface**.

## Exact b43 identity / evidence

- Candidate `DEV-send-stream-0.1.0-b43`, `0.1.0 (43)`.
- Exact product/config source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`.
- Push Run / Job `33241032864` / `99070294478` — success.
- PR Run / Job `33241035013` / `99070299776` — success.
- Artifact `9711364573`; ZIP `sha256:1a9516221ec5ece59741f9f2af2483815f09fa47f051ff6a97a67a12d40d4c23`.
- IPA `ChatGPTClient-0.1.0-b43-dev-send-stream.ipa`; SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.
- Package identity independently verified: `0.1.0 (43)`, Candidate b43, source `f602d68ae95d`, Release, iOS14 minimum, `[1,2]`, arm64.
- Accidental Artifact `9710515489` carrying newer code under stale b42 identity remains permanently rejected.

## b43 exact-device Runtime result — 2026-08-29

User tested the requested b43 sequence on the primary iPhone/iOS17 device and reported **“基本上没什么问题”**.

Positive observations:

- first hybrid entry / resident re-entry: no material problem reported;
- keyboard, typing, visible Web Send, streamed-response scrolling and rapid scrolling: no material problem reported;
- native return/regression sequence: no material problem reported;
- Web `+` -> attachment selection latency was roughly **100–200 ms**, not rejected as excessive.

Observed limitation / explicit new requirement:

- Web `+` -> photo selection opened the photo library but filtered out videos;
- user wants media selection not to hide video assets merely because the current Web chooser is image-filtered.

Evidence classification:

- Code / CI / Artifact / package identity: passed.
- Visible-Web smoothness/residency feasibility: **largely accepted for the tested sequence**.
- Video selection: **current limitation remains**.
- Final integrated product flow: not accepted; b43 is a feasibility baseline, not the final Send UX.
- Stable/Frozen: No.

## Verified iOS17 attachment-picker boundary

A planned assumption was corrected before product code was changed:

- Apple/WebKit exposes `WKUIDelegate webView(_:runOpenPanelWith:initiatedByFrame:completionHandler:)` on **iOS 18.4+**, not iOS17;
- WebKit's own public header states `WK_API_AVAILABLE(... ios(18.4) ...)` and says older iOS WKWebView uses Safari-like upload behavior when the delegate method is unavailable;
- therefore the primary iOS17 target **cannot** use a public WKUIDelegate hook to replace the webpage's image-filtered upload panel with our own PHPicker;
- do not use private WebKit APIs, DOM/file-input injection or hidden automation to bypass that limitation;
- current official ChatGPT image-input documentation says image inputs process static images; generic file docs do not establish video processing. Exposing videos and successfully processing videos are separate product/service questions.

For iOS17, fixing the video filter properly requires a separately evidenced native attachment upload/handoff architecture, not a fake WebKit override. This remains a follow-up dependency and must not block the b44 text-Send integration trial.

## Product direction after b43

The user confirmed the Settings-only Web page feels like a separate browser feature. That is not the intended final interaction.

Target interaction:

`native conversation list -> native conversation detail -> native send affordance -> visible official-Web layer scoped to selected conversation -> user sends through official Web -> explicit return/sync -> native detail`

Rules:

1. Native list/detail remains the primary product surface.
2. Remove the standalone ordinary Settings hybrid entry; protocol diagnostic controls remain in Settings.
3. Root remains the native navigation owner.
4. Visible Web uses the existing default persistent `WKWebsiteDataStore` and remains process-resident where practical.
5. No DOM message mirroring/scraping, hidden Web transport, challenge harvesting or native prompt injection.
6. `ConversationRepository` remains sole native conversation/read/recovery authority.
7. Opening selected conversation at public ChatGPT `/c/<conversation-id>` is allowed only as a **b44 Runtime trial**. Current 2026 public evidence shows this route shape, but exact native-ID -> Web-page alignment must be validated on-device before it becomes a durable accepted contract.
8. Do not pass prompt text through guessed URL/query parameters or DOM automation.
9. Reconciliation back to native remains explicit until a safe send-completion signal is evidenced; ordinary Back must not automatically Sync.

## b44 planned minimal product scope

Candidate to allocate atomically with product code: `DEV-send-stream-0.1.0-b44`, version/build `0.1.0 (44)`.

Planned product files:

- `RootViewController.swift`
  - keep Root as navigation owner;
  - add a native bottom `发送消息…` affordance to the selected conversation detail navigation stack;
  - push the shared visible Web Send controller prepared for that selected conversation;
  - receive explicit `返回并同步` from the Web surface and invoke exactly one existing `ConversationRepository.syncLatestMessages(id:)`, then re-render the selected native detail;
  - ordinary Back performs no automatic Sync.
- `AuthWebViewController.swift`
  - preserve one resident shared WKWebView;
  - accept a selected conversation target and visibly navigate to `https://chatgpt.com/c/<conversation-id>` when the resident page is not already that target;
  - log only safe route class / `targetMatch` / timing metadata, never raw conversation IDs;
  - add explicit `返回并同步` action; do not observe DOM or message bodies.
- `SettingsViewController.swift`
  - remove the ordinary standalone `混合发送` section/button; keep diagnostic Send probe controls.
- Xcode/workflow identity files move atomically to b44 in the same product commit.

No `ConversationFeature.swift`, Stable b38 geometry or native message authority change is planned for b44.

## b44 exact-device Runtime gate

1. From a native conversation, tap `发送消息…`; visible Web should open as part of that conversation flow rather than via Settings.
2. Verify Web resolves to the same selected conversation; safe diagnostics should show target match without raw IDs.
3. Send one normal text message; keyboard/typing/stream scrolling must remain at least as smooth as b43.
4. Use explicit `返回并同步`; exactly one native reconciliation request should occur and native detail should reflect current server state without duplicate authority.
5. Ordinary Back without `返回并同步` must not trigger Sync.
6. Web `+` latency should remain around the accepted b43 range; the iOS17 video-filter limitation is recorded separately and is **not claimed fixed in b44**.
7. Stable native list/detail/long-conversation/round-navigation behavior must remain intact.

## Candidate / write-chain rule

- b39-b43 are permanently reserved.
- Do not push product-path changes while Xcode/workflow still carry b43.
- Prepare Root/AuthWeb/Settings + Xcode build44 + workflow b44 as one Git-data tree/commit, then non-force fast-forward once.
- If b44 Artifact emits, any corrected product code after emission must use b45 or later.

## Next exact action

Construct the minimal Root/AuthWeb/Settings b44 integration, combine it atomically with b44 Xcode/workflow identity, fast-forward the real branch without force, then verify CI/Artifact/package identity and hand exact b44 to the user for the integrated native-conversation Send Runtime matrix.