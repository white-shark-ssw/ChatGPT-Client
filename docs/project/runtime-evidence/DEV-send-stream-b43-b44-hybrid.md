# DEV-send-stream b43 / b44 Hybrid Evidence

_Date: 2026-08-29_

## b43 exact identity

- Candidate `DEV-send-stream-0.1.0-b43`, `0.1.0 (43)`.
- Exact source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`.
- Push Run / Job `33241032864` / `99070294478` — success.
- PR Run / Job `33241035013` / `99070299776` — success.
- Artifact `9711364573`.
- ZIP `sha256:1a9516221ec5ece59741f9f2af2483815f09fa47f051ff6a97a67a12d40d4c23`.
- IPA SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.

## b43 exact-device Runtime

User tested the requested b43 hybrid sequence on the primary iPhone/iOS17 device and reported **“基本上没什么问题”**.

Observed accepted-feasibility behavior:

- first visible Web entry and resident re-entry: no material issue reported;
- keyboard/typing, visible Web Send, streamed response scrolling and rapid scrolling: no material issue reported;
- native return/regression sequence: no material issue reported;
- Web `+` -> attachment selector latency approximately **100–200 ms**, not rejected as excessive.

Observed limitation:

- Web photo selection opened the system photo library but filtered video assets out.
- User explicitly wants future media selection to include videos rather than hiding them merely because the Web chooser chose an image-only input.

Evidence classification: b43 is accepted as a visible-Web smoothness/residency **feasibility baseline**, not final integrated Send UX. Stable/Frozen No.

## iOS17 picker boundary

Current public WebKit evidence shows `WKUIDelegate webView(_:runOpenPanelWith:initiatedByFrame:completionHandler:)` is iOS18.4+, not the primary iOS17 runtime. Therefore:

- b44 does not claim to override the Web upload chooser on iOS17;
- no private WebKit API, DOM/file-input injection or hidden automation is used;
- a real iOS17 video-capable picker/upload flow requires separately evidenced native attachment upload/handoff work;
- current official ChatGPT image-input documentation describes static image input and does not establish arbitrary video processing support.

## b44 exact identity

- Candidate `DEV-send-stream-0.1.0-b44`, `0.1.0 (44)`.
- Exact product/config source `f1503cf7121512a84e5c55a3642181c17324d791`.
- Product delta from pre-b44 head `53947595bf4fd271fc588a1db0796b1004ac26ea`: exactly five files — Root, AuthWeb, Settings, Xcode identity, workflow identity.
- `ConversationFeature.swift` unchanged.
- Push Run / Job `33245105815` / `99081114295` — success.
- PR Run `33245107290` — success.
- Artifact `9712583513`.
- ZIP `sha256:33ba4a99fe933241ce8023e811f15d55dfa0d95cac2693f039bb6138d813face`.
- IPA `ChatGPTClient-0.1.0-b44-dev-send-stream.ipa`.
- IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.
- Independent package inspection: `0.1.0 (44)`, Candidate b44, source `f1503cf71215`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, Mach-O arm64.

## b44 implementation scope

- Root-owned native bottom `发送消息…` entry on selected conversation detail.
- Shared visible `AuthWebViewController.hybridChat` is prepared for selected native conversation.
- Trial visible route `https://chatgpt.com/c/<conversation-id>`; only safe `targetMatch` / route-class / timing diagnostics are logged.
- Explicit `返回并同步` calls exactly one existing `ConversationRepository.syncLatestMessages(id:)`; ordinary Back does not auto-Sync.
- Standalone ordinary Settings hybrid-chat entry removed; diagnostic Send probe retained.
- No prompt injection, DOM mirroring/scraping, challenge harvesting or private attachment interception.

## b44 Runtime gate

Runtime is pending. Exact iPhone/iOS17 must prove:

1. native conversation -> `发送消息…` -> same Web conversation;
2. text Send/typing/stream scrolling remains smooth;
3. `返回并同步` performs one reconciliation and native detail receives current server state;
4. ordinary Back performs no Sync;
5. A/B native selection maps to correct A/B Web target;
6. same-target resident re-entry avoids unnecessary reload;
7. Web `+` responsiveness remains acceptable; video filtering remains a known, explicitly non-fixed iOS17 limitation;
8. no b38 native long-conversation/round-navigation regression.

Do not treat CI/Artifact as Runtime acceptance. Any corrected product code after emitted b44 must use b45+.