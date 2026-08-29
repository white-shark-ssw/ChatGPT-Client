# DEV-send-stream

## Status

**Blocked — b44 integrated full-page hybrid Runtime rejected; architecture decision reopened**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail / 官方 Web / hybrid`
- **Branch / PR**: `dev/send-stream-20260829`; PR #29 open; do not merge as accepted Send UX.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; Stable native predecessor b38 remains merged.
- **Exact b44 product/config source**: `f1503cf7121512a84e5c55a3642181c17324d791`.
- **Exact b44 Artifact**: `9712583513`; IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.
- **Resume guard**: branch head before this Runtime docs batch was `fbac2ffb44ef5acd5023d81286ebcdb890a07329`; PR #29 open/mergeable; `main` remained `34811877896ca88c6656be6676f5466a19931ce6`; current `docs/project/current/dev/` contains no peer Active development checkpoint.

## Security / transport boundary retained

Exact b42 proved the tested successful ChatGPT-account Send requires browser anti-abuse challenge output (`proofOfWorkRequired=true`, `turnstileRequired=true`, `soRequired=true`, non-empty PoW + Turnstile finalize input). Pure-native/transient-auth ChatGPT-account Send remains blocked.

Never implement PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoints, hidden challenge-harvesting WebViews, DOM message scraping or hidden native challenge harvesting.

TD-024 allowed **user-visible** official ChatGPT Web Send while native read/navigation remained authoritative. b44 Runtime now proves that one specific full-page integrated form of TD-024 is not an acceptable product interaction.

## b43 Runtime retained

Exact b43 `DEV-send-stream-0.1.0-b43` established that one process-resident visible official Web surface is technically smooth enough on the primary iPhone/iOS17 device for the tested sequence:

- first/re-entry, keyboard/typing, visible Web Send, stream scrolling and rapid scrolling had no material problem reported;
- Web `+` -> attachment selection was roughly 100–200 ms and not rejected;
- Web Photos selection filtered video assets.

The Settings-only standalone Web chat was rejected as final UX even though the Web feasibility/smoothness baseline was useful.

## Verified iOS17 attachment boundary retained

Public `WKUIDelegate` file-open-panel replacement is available on iOS 18.4+, not the primary iOS17 target. Therefore iOS17 cannot publicly replace the webpage's image-filtered picker with our own PHPicker through that delegate. Do not use private WebKit APIs or DOM/file-input injection to fake a fix. Proper photo+video selection on iOS17 requires a separately evidenced native attachment upload/handoff path.

## Exact b44 Code / CI / Artifact evidence

- Candidate `DEV-send-stream-0.1.0-b44`, `0.1.0 (44)`.
- Exact source `f1503cf7121512a84e5c55a3642181c17324d791`.
- Push Run / Job `33245105815` / `99081114295` — success.
- PR Run `33245107290` — success.
- Artifact `9712583513`; ZIP `sha256:33ba4a99fe933241ce8023e811f15d55dfa0d95cac2693f039bb6138d813face`.
- IPA `ChatGPTClient-0.1.0-b44-dev-send-stream.ipa`; SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.
- Independent package inspection: `0.1.0 (44)`, Candidate b44, source `f1503cf71215`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, arm64.

## b44 exact-device Runtime result — 2026-08-29

The user tested the integrated native-conversation -> visible Web -> native reconciliation flow on the primary iPhone/iOS17 device.

Observed behavior:

1. Sending in Web worked.
2. Tapping `返回并同步` immediately after Send caused the newly sent **user message** to appear in Native, but the assistant answer was not yet visible there.
3. Re-entering Web showed that the assistant had already produced substantial answer content.
4. Returning to Native with ordinary Back did not auto-Sync by design, so the assistant answer remained absent.
5. Re-entering Web and using `返回并同步` again still did not immediately surface the assistant answer.
6. Using Native `同步最新消息` immediately also did not surface the assistant answer.
7. After waiting and then syncing again, the assistant answer finally became visible in Native.
8. Switching Native to conversation B and tapping Send caused the resident Web surface to immediately navigate/reload from its old page to B and then show B history correctly.

Evidence conclusion:

- `/c/<conversation-id>` mapping worked for the tested A/B selection path.
- Native read visibility is **eventually consistent relative to the Web generation surface** for the tested post-Send sequence. One immediate reconciliation request is not sufficient evidence that a completed/ongoing Web assistant response is readable through the native Detail path.
- Do **not** patch this with speculative timer/poll/retry loops. The current Runtime establishes a product/authority mismatch, not merely a missing delay constant.
- The b44 full-page flow causes duplicate conversation work: Native Detail is already loaded, then Web loads the same conversation again to become the Send surface.
- The user explicitly rejected the interaction because the product still feels fundamentally Web-driven and makes the native experience lose its purpose.

**b44 Runtime status: functional route evidence accepted; integrated full-page hybrid product UX rejected / superseded. Stable/Frozen No.**

## Architecture consequence

The user's proposed idea is visually attractive: keep Native UI over a Web surface, provide a Native composer, and forward Native text into Web for Send. However, under the current transport evidence, forwarding a Native composer into a covered/hidden Web composer requires programmatic DOM/JS/input automation and turns the Web page into a hidden/shadow protected Send transport. That conflicts with TD-023/TD-024 security boundaries and is not an accepted implementation route.

Do not implement:

- fully covered/hidden WebView used only to execute the browser challenge + Send flow;
- Native composer text injection into a hidden Web DOM/contenteditable;
- synthetic hidden clicks on Web Send;
- Web DOM/stream scraping to manufacture immediate Native assistant state.

## Current architecture choices

### A — recommended if existing ChatGPT account/history must remain the product

**Native history/read surface + explicitly visible official-Web composer/live-response panel embedded into the Native detail flow.**

- Native list/history/long-conversation navigation remain visible and authoritative.
- The actual official Web composer remains visibly exposed and directly user-operated; do not replace it with a Native text field that secretly drives hidden Web DOM.
- Avoid the b44 full-screen push/pop interaction; use an embedded/expandable visible Send panel so switching into Send does not feel like entering another browser page.
- While the Web response is active, do not promise immediate Native mirroring. The Web live-response surface remains the truthful immediate response owner until later Native reconciliation is actually readable.
- One explicit reconciliation when leaving/collapsing the live Web surface may remain; do not auto-poll until a real completion/read-availability signal is evidenced.
- iOS17 Web attachment-video filtering remains a known boundary until native upload/handoff is separately evidenced.

This keeps the ChatGPT account/session/history route but cannot make Send/stream fully Native under current evidence.

### B — truly Native composer/stream via an officially supported API product

- Native composer, native incremental response ownership and native attachment UX become architecturally clean.
- OpenAI API billing is separate from ChatGPT subscription billing; current official documentation says API usage requires separate API billing/pay-as-you-go and is not moved from a ChatGPT subscription.
- API conversations are a separate product path; do not claim they are the same ChatGPT-account conversation/history semantics without explicit supported evidence.

### C — defer Send

Keep the Stable native read client and wait for a supported ChatGPT-account transport that does not require the current browser challenge ownership.

## Candidate rule

b39-b44 are permanently reserved. **Do not allocate b45 and do not modify product code until the architecture gate below is explicitly resolved.**

## Batch recovery point — Runtime/docs batch

Known baseline:

- exact b44 product/config source `f1503cf7121512a84e5c55a3642181c17324d791`;
- branch docs head before batch `fbac2ffb44ef5acd5023d81286ebcdb890a07329`;
- PR #29 open/mergeable;
- main unchanged at `34811877896ca88c6656be6676f5466a19931ce6`;
- no peer Active development checkpoint.

Completed before this checkpoint write:

- user supplied exact b44 Runtime behavior and rejected the full-page hybrid interaction;
- architecture analysis determined that immediate repeated Sync is not a justified fix;
- hidden/covered Web + Native DOM-injected composer remains outside the accepted security boundary.

Pending docs batch:

- add exact b44 Runtime evidence file;
- update `PROJECT_STATE.md`, `MODULE_STATUS.md`, `TECHNICAL_DECISIONS.md`, `BUILD_TEST_INDEX.md` and PR #29 to record b44 rejection + reopened architecture gate;
- no product/config/workflow mutation in this batch.

## Next exact action

Finish the docs-only b44 Runtime batch, then stop at the human architecture gate. If the user explicitly chooses A, re-run branch/PR/base/conflict guard and design the smallest **visible embedded Web composer/live-response** experiment as b45. If the user chooses B, verify current official API auth/billing/product semantics before implementation and create a separate supported-API architecture plan. If C, leave `DEV-send-stream` blocked. Do not infer the user's proposed hidden-Web/native-composer idea as permission to cross the current hidden-transport boundary.