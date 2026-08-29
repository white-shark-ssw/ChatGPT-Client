# DEV-send-stream

## Status

**Active — exact b44 integrated hybrid Artifact ready; waiting for real-device Runtime**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail / 官方 Web / hybrid`
- **Branch / PR**: `dev/send-stream-20260829`; PR #29 open; do not merge before b44 Runtime acceptance.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; Stable native predecessor b38 remains merged.
- **Exact b44 product/config source**: `f1503cf7121512a84e5c55a3642181c17324d791`.
- **Parallel guard**: no peer Active development checkpoint existed when b44 was assembled/published.

## Security / architecture boundary retained

Exact b42 proved the tested successful ChatGPT-account Send requires browser anti-abuse challenge output (`proofOfWorkRequired=true`, `turnstileRequired=true`, `soRequired=true`, non-empty PoW + Turnstile finalize input). Pure-native/transient-auth ChatGPT-account Send remains blocked.

Never implement PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoints, hidden challenge-harvesting WebViews, DOM message scraping or hidden native challenge harvesting.

The user selected TD-024: **native shell/read/navigation + a user-visible official ChatGPT Web Send surface**.

## b43 exact-device Runtime result — accepted feasibility baseline with one attachment limitation

Exact b43:

- Candidate `DEV-send-stream-0.1.0-b43`, `0.1.0 (43)`;
- source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`;
- Artifact `9711364573`;
- IPA SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.

User tested the requested sequence on the primary iPhone/iOS17 device and reported **“基本上没什么问题”**:

- first entry/re-entry: no material problem reported;
- keyboard/typing/visible Web Send/stream scrolling/rapid scrolling: no material problem reported;
- native return/regression sequence: no material problem reported;
- Web `+` -> attachment selection latency roughly **100–200 ms**, not rejected as excessive.

Observed limitation:

- Web photo selection filtered video assets out of the Photos picker.
- User explicitly wants video assets not hidden by the media picker.

### Verified iOS17 boundary

Before implementing a guessed fix, current public WebKit evidence was checked:

- `WKUIDelegate webView(_:runOpenPanelWith:initiatedByFrame:completionHandler:)` is public on **iOS 18.4+**, not iOS17;
- therefore the primary iOS17 target cannot publicly replace the Web page's upload chooser with a custom PHPicker through that delegate;
- no private WebKit API, DOM/file-input injection or hidden automation will be used to force this;
- current official ChatGPT image-input documentation describes static image input and does not establish video processing support.

Result: b44 **does not claim the video filter is fixed**. Proper iOS17 video-selection/upload support needs a separately evidenced native attachment upload/handoff path.

## Product direction after b43

The Settings-only standalone Web page was useful as a feasibility probe but is not the final interaction. The user asked to continue with native conversation as the primary surface.

Target flow:

`native list -> native detail -> native 发送消息… -> visible official-Web layer for the selected conversation -> Send -> explicit 返回并同步 -> native detail`

Rules:

1. Native list/detail stays primary.
2. Root remains native navigation owner.
3. `ConversationRepository` remains sole native conversation/read/recovery authority.
4. default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
5. Web Send remains visible.
6. No prompt injection, DOM mirroring/scraping or hidden Web transport.
7. Ordinary Back from Web does not automatically Sync.
8. `返回并同步` performs exactly one existing Repository Sync request.
9. `/c/<conversation-id>` is a **b44 Runtime trial**; public 2026 evidence supports that route shape, but exact native-ID -> same Web conversation mapping is not durable until exact-device validation.

## Exact b44 implementation

Candidate: `DEV-send-stream-0.1.0-b44`, `0.1.0 (44)`.

Product delta from pre-b44 head `53947595bf4fd271fc588a1db0796b1004ac26ea` to exact source `f1503cf7121512a84e5c55a3642181c17324d791` is exactly five files:

- `ChatGPTClient/RootViewController.swift`
  - retains Root as navigation owner;
  - retains one repository instance;
  - adds native bottom `发送消息…` affordance on selected native detail;
  - pushes the shared visible hybrid Web controller scoped to selected conversation;
  - explicit sync callback calls `repository.syncLatestMessages(id:)` once and re-renders the selected detail on success;
  - account reset hides the send toolbar.
- `ChatGPTClient/Authentication/AuthWebViewController.swift`
  - preserves one process-resident shared WKWebView on default persistent data store;
  - `prepareForConversation(id:onSyncRequested:)` binds only the current visible trial target;
  - visibly loads `https://chatgpt.com/c/<conversation-id>` only when current resident Web URL does not already match that target;
  - diagnostics expose only route class / `targetMatch` / timing; raw conversation ID is never logged;
  - adds explicit `返回并同步` + refresh;
  - no DOM/message-body observation.
- `ChatGPTClient/SettingsViewController.swift`
  - removes the ordinary standalone `混合发送` section/button;
  - retains Send protocol diagnostic controls.
- `ChatGPTClient.xcodeproj/project.pbxproj`
  - build 44 / Candidate b44 for Debug + Release.
- `.github/workflows/ios-foundation.yml`
  - workflow `iOS Integrated Hybrid Send` / Artifact b44.

`ConversationFeature.swift` and Stable b38 deterministic long-message geometry were not changed.

## Exact b44 Code / CI / Artifact evidence

- **Exact source**: `f1503cf7121512a84e5c55a3642181c17324d791`.
- **Push Run / Job**: `33245105815` / `99081114295` — success.
- **PR Run**: `33245107290` — success.
- **Artifact**: `9712583513`.
- **Artifact ZIP digest**: `sha256:33ba4a99fe933241ce8023e811f15d55dfa0d95cac2693f039bb6138d813face`.
- **IPA**: `ChatGPTClient-0.1.0-b44-dev-send-stream.ipa`.
- **IPA SHA-256**: `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.
- **Independent package inspection**: `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=44`, `DiagnosticsCandidate=DEV-send-stream-0.1.0-b44`, `DiagnosticsSourceCommit=f1503cf71215`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, Mach-O arm64.
- **Evidence classification**: Code written / Xcode CI passed / Artifact produced / package identity verified. **Runtime pending; Stable/Frozen No.**

## b44 exact-device Runtime gate

1. Open an existing conversation in the native detail and tap bottom `发送消息…`.
2. Confirm visible Web opens the **same selected conversation**, not root or another chat.
3. Send one ordinary text message; keyboard/typing/stream scrolling must remain at least as smooth as b43.
4. Tap `返回并同步`; exactly one native reconciliation should run and the native detail should show the just-sent turn after the server state is available.
5. Re-enter the same conversation's Send surface; resident reuse should avoid unnecessary reload.
6. Switch native A -> B and open Send for B; Web target must switch to B, not remain A.
7. Use ordinary Back once without `返回并同步`; it must not trigger automatic Sync.
8. Web `+` responsiveness should remain comparable to b43 (~100–200 ms observed). **Video filtering is a known iOS17/Web limitation and is not claimed fixed in b44.**
9. Recheck native long-conversation scrolling and round navigation for b38 regression.
10. If target mismatch or reconciliation is unclear, export diagnostics. Logs must contain no prompt/answer/raw ID/Cookie/Auth/challenge/proof/token values.

## Candidate identity rule

b39-b44 are permanently reserved once emitted. Any corrected product code after exact b44 Artifact `9712583513` must use **b45 or later**.

## Next exact action

User installs/tests exact `DEV-send-stream-0.1.0-b44` on the primary iPhone/iOS17 device using the matrix above. On any defect, re-run branch/PR/base/conflict guard, interpret exact b44 Runtime/diagnostics, and allocate b45+ for product correction. Do not merge PR #29 as accepted integrated Send before b44 Runtime acceptance.