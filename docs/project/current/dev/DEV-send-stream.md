# DEV-send-stream

## Status

**Blocked — b44 integrated full-page hybrid Runtime rejected; explicit architecture decision required before b45**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail / 官方 Web / hybrid`
- **Branch / PR**: `dev/send-stream-20260829`; PR #29 open; do not merge as accepted Send UX.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; Stable native predecessor b38 remains merged.
- **Exact b44 product/config source**: `f1503cf7121512a84e5c55a3642181c17324d791`.
- **Exact b44 Artifact**: `9712583513`; IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.
- **Resume guard before b44 Runtime docs batch**: branch head `fbac2ffb44ef5acd5023d81286ebcdb890a07329`; PR #29 open/mergeable; main unchanged at `34811877896ca88c6656be6676f5466a19931ce6`; no peer Active development checkpoint.

## Security / transport boundary retained

Exact b42 proved tested successful ChatGPT-account Send requires browser anti-abuse challenge output (`proofOfWorkRequired=true`, `turnstileRequired=true`, `soRequired=true`, non-empty PoW + Turnstile finalize input). Pure-native/transient-auth ChatGPT-account Send remains blocked.

Never implement PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoints, hidden challenge-harvesting WebViews, DOM message/reasoning scraping or hidden native challenge harvesting.

TD-024 permits only an **explicit user-visible** official ChatGPT Web Send surface. TD-025 now records that b44's full-page integrated form is not acceptable product UX.

## b43 feasibility Runtime retained

Exact b43 `DEV-send-stream-0.1.0-b43`, source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`, Artifact `9711364573`, IPA SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.

Primary-device Runtime:

- first/re-entry, keyboard/typing, visible Web Send, stream scrolling and rapid scrolling had no material problem reported;
- Web `+` -> attachment selection roughly **100–200 ms**, not rejected;
- Web Photos selection filtered video assets;
- standalone Settings Web-chat interaction was not accepted as final product UX.

Public `WKUIDelegate` file-open-panel replacement is iOS18.4+, not primary iOS17. Do not use private WebKit or DOM/file-input injection to fake an iOS17 photo+video picker fix.

## Exact b44 identity / evidence

- Candidate `DEV-send-stream-0.1.0-b44`, `0.1.0 (44)`.
- Exact source `f1503cf7121512a84e5c55a3642181c17324d791`.
- Push Run / Job `33245105815` / `99081114295` — success.
- PR Run `33245107290` — success.
- Artifact `9712583513`; ZIP `sha256:33ba4a99fe933241ce8023e811f15d55dfa0d95cac2693f039bb6138d813face`.
- IPA `ChatGPTClient-0.1.0-b44-dev-send-stream.ipa`; SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.
- Package identity independently verified: `0.1.0 (44)`, Candidate b44, source `f1503cf71215`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, arm64.

## Exact b44 Runtime result — 2026-08-29

Tested flow:

`native detail -> 发送消息… -> visible Web /c/<conversation-id> -> Send -> 返回并同步 -> native detail`

User observations:

1. Web Send worked.
2. Immediate `返回并同步` surfaced the newly sent **user message** in Native but not the assistant answer.
3. Re-entering Web already showed substantial assistant answer content.
4. Repeating `返回并同步` still did not immediately expose the assistant answer in Native.
5. Immediate Native `同步最新消息` also did not expose it.
6. After waiting and syncing later, the assistant answer became visible.
7. Native A -> B -> `发送消息…` caused resident Web to navigate/reload from A to B and show B history correctly.

Accepted evidence conclusions:

- tested Native ID -> Web `/c/<id>` mapping worked for A/B;
- Native Detail visibility is **eventually consistent relative to the Web generation surface** in this tested post-Send sequence;
- one immediate reconciliation request is not an immediate Web-response handoff;
- no stable readiness signal or fixed delay was evidenced, so do not add timer/poll/retry/repeated automatic Sync;
- b44 duplicates conversation work because Native has already loaded Detail and Web then loads/renders the same conversation for Send;
- the user explicitly rejected this browser-like full-page interaction because it leaves actual conversation interaction fundamentally Web-driven.

**b44 classification: Code/CI/Artifact/package identity passed; route/mapping/reconciliation Runtime observations accepted; integrated full-page hybrid product UX rejected / superseded. Stable/Frozen No.**

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b44-runtime.md`.

## Native-over-hidden-Web proposal boundary

The user's proposed visual direction — Native interface over Web plus a Native input field forwarding text to Web — would be attractive only if the Web Send path could remain a supported transport. Under current evidence, a fully covered/hidden official Web composer would require DOM/JS/contenteditable automation and synthetic hidden Send interaction.

Do not implement:

- fully covered/hidden WebView used only for browser challenge + Send;
- Native composer text injection into hidden Web DOM/contenteditable;
- synthetic hidden Web Send clicks;
- DOM/stream scraping to create immediate Native assistant authority;
- browser challenge extraction/replay.

That would convert Web into hidden/shadow protected transport and violate TD-023/TD-024/TD-025.

## Current architecture gate — TD-025

### A — recommended if existing ChatGPT account/history continuity is required

**Native list/history/read/navigation + an explicitly visible embedded official-Web composer/live-response panel.**

- actual official Web composer/live-response area stays visibly exposed and directly user-operated;
- avoid b44's separate full-page Web push/pop interaction;
- Native history remains visible/primary where layout permits;
- while Web response is active, Web remains the truthful immediate response surface;
- Native reconciliation occurs only when native read availability actually supports it;
- no automatic polling without a real readiness signal;
- iOS17 video picker limitation remains until native attachment upload/handoff is evidenced.

This preserves current ChatGPT-account/session/history continuity as far as current evidence permits but does **not** make Send/stream fully Native.

### B — truly Native supported API product

Use an officially supported API with separate API authentication/billing, then implement Native composer, incremental stream ownership and attachments. Current official OpenAI documentation states ChatGPT subscription billing and API billing are separate. Do not claim API conversations are the same existing ChatGPT-account history/session without explicit supported evidence.

### C — defer ChatGPT-account Send

Keep the Stable native read client and wait for a supported account transport that does not require browser-owned challenge output.

## Candidate rule

b39-b44 are permanently reserved. **No b45 is allocated. Do not modify Send product code until the user explicitly chooses A, B or C.**

## Runtime/docs batch closure

Completed docs-only after exact b44 product source:

- created `runtime-evidence/DEV-send-stream-b44-runtime.md`;
- updated `PROJECT_STATE.md`;
- updated `MODULE_STATUS.md`;
- updated `TECHNICAL_DECISIONS.md` with TD-025;
- updated `BUILD_TEST_INDEX.md` with b43/b44 Runtime classification;
- updated `PROJECT_SPECIFIC_RULES.md` with hidden-Web/native-composer prohibition and architecture gate;
- refreshed `PROJECT_PROFILE.md`;
- refreshed `DEVELOPMENT_PLAN.md`;
- updated PR #29 title/body to b44 Runtime rejected / architecture gate reopened.

No Swift/Xcode/workflow/script/product mutation was intentionally made in this Runtime/docs batch.

## Next exact action

**Wait for explicit user architecture choice A, B or C.**

- If A: rerun branch/PR/base/conflict guard and design the smallest explicitly visible embedded Web composer/live-response experiment as b45.
- If B: first re-verify current official OpenAI API authentication/billing/models/stream/files semantics, then define a separate supported-API architecture before product code.
- If C: leave `DEV-send-stream` blocked and preserve Stable native read baseline.

Do not infer the user's Native-over-covered-Web idea as authorization to cross the hidden-transport boundary.