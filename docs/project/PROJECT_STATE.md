# Project State

_Last updated: 2026-08-29 through exact b44 integrated-hybrid Runtime rejection and reopened Send architecture gate._

## Current accepted merged baseline

- Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21 and list-cache b23 remain accepted merged baselines for their recorded scopes.
- **Phase 8 b38** remains the current Stable merged native reading/metadata/round-navigation baseline; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Exact b38 tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Stable does not mean Frozen; current native conversation modules remain Frozen No.

## Current Phase 9 — DEV-send-stream

### Security boundary retained from b42

Exact b42 (`e8946e48a0b5ad86b402faf5eabba627e3393adf`, legitimate Artifact `9709824510`) proved successful tested ChatGPT-account Send requires browser anti-abuse challenge output: PoW, Turnstile and `so` required; non-empty PoW + Turnstile were finalized before Send.

Therefore pure-native/transient-auth ChatGPT-account Send remains blocked. Prohibited routes remain solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoint, hidden/shadow challenge WebView, challenge harvesting and DOM/message scraping that creates a second native response authority.

### b43 — visible-Web feasibility baseline

Exact b43 source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`, Artifact `9711364573`, IPA SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.

Primary-device Runtime:

- first/re-entry, keyboard/typing, visible Web Send, stream scrolling, rapid scrolling and native return had no material reported problem;
- Web `+` -> picker latency was roughly **100–200 ms**, not rejected as excessive;
- Web photo selection filtered video assets.

The standalone Settings Web-chat UX was not accepted as the final product interaction.

Verified iOS17 boundary: the public `WKUIDelegate.runOpenPanelWith...` replacement hook is iOS18.4+, so the iOS17 target cannot publicly swap the page's upload chooser for a custom PHPicker through that delegate. Do not fake the video fix with private WebKit or DOM/file-input injection. Proper iOS17 photo+video attachment support still requires separately evidenced native attachment upload/handoff.

### b44 — integrated full-page hybrid trial

Exact identity:

- Candidate `DEV-send-stream-0.1.0-b44`, `0.1.0 (44)`;
- product/config source `f1503cf7121512a84e5c55a3642181c17324d791`;
- Push Run / Job `33245105815` / `99081114295` — success;
- PR Run `33245107290` — success;
- Artifact `9712583513`;
- ZIP `sha256:33ba4a99fe933241ce8023e811f15d55dfa0d95cac2693f039bb6138d813face`;
- IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`;
- package identity verified as `0.1.0 (44)`, Candidate b44, source `f1503cf71215`, Release, iOS14 minimum, `[1,2]`, arm64.

b44 product shape:

`native detail -> 发送消息… -> visible Web /c/<conversation-id> -> Send -> 返回并同步 -> native detail`

`ConversationRepository` remained sole native conversation/read/recovery authority; ordinary Back did not auto-Sync; `返回并同步` issued exactly one existing Repository Sync request. `ConversationFeature.swift` and Stable b38 deterministic long-message geometry were unchanged.

### Exact b44 Runtime result — full-page product UX rejected

Primary iPhone/iOS17 observations:

1. Web Send worked.
2. Immediate `返回并同步` surfaced the newly sent **user message** in Native but not the assistant answer.
3. Re-entering Web already showed substantial assistant answer output.
4. Re-entering Web and using `返回并同步` again still did not immediately make that assistant answer readable in Native.
5. Immediate Native `同步最新消息` also did not expose it.
6. After waiting and syncing later, the assistant answer became visible.
7. Native A -> B -> `发送消息…` caused resident Web to navigate/reload from A to B and then show B history correctly.

Evidence conclusions:

- tested native ID -> Web `/c/<id>` mapping worked for A/B;
- the Native Detail read path is **eventually consistent relative to the Web generation surface** in this post-Send sequence;
- one immediate reconciliation request is not an immediate Web-response handoff;
- no stable readiness signal/delay was evidenced, so do not add timer/poll/retry loops to guess when assistant content becomes readable;
- the same conversation is effectively loaded once by Native Detail and again by Web when entering Send, and A/B switches repeat Web-side loading;
- the user explicitly rejected this browser-like flow because actual interaction remains Web-driven and the native client loses its purpose.

**b44 Runtime classification: route/mapping/reconciliation evidence accepted; integrated full-page hybrid product UX rejected / superseded. Stable/Frozen No.**

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b44-runtime.md`.

## Architecture gate reopened

The user's proposed `Native UI covers Web + Native composer forwards text to Web` would require programmatic DOM/JS/input automation of a covered/hidden official Web composer under current evidence. That turns Web into a hidden/shadow protected Send transport and conflicts with TD-023/TD-024. It is not an accepted product route.

Current choices:

### A — account-compatible compromise

Native list/history/read/navigation remain primary; embed an **explicitly visible official-Web composer/live-response panel** in the native detail rather than pushing a separate full-page Web chat. User directly operates the real Web composer. This preserves existing ChatGPT account/session/history semantics as far as current evidence allows, but Send/stream cannot honestly be described as fully Native.

### B — truly Native supported API product

Use an officially supported API with separate API authentication/billing and implement Native composer/stream/attachments. Current OpenAI documentation states API billing is separate from ChatGPT subscription billing. Do not claim API conversations are the same ChatGPT-account history/session without explicit supported evidence.

### C — defer ChatGPT-account Send

Keep the Stable native read client and wait for a supported ChatGPT-account transport that does not require browser-owned challenge output.

**No b45 is allocated. Product code is blocked until the architecture gate is explicitly resolved.**

## Candidate identity incident retained

Artifact `9710515489` was accidentally emitted with newer hybrid code under stale b42 identity. It is permanently rejected and must never be installed/promoted. Legitimate b42 remains Artifact `9709824510`.

## Authority / evidence rule

- `ConversationRepository` remains sole native conversation/list/read/recovery authority.
- `AuthSessionStore` remains native auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- UI text/title is never identity authority.
- Native Sync/Reload never resend/regenerate.
- CI/Artifact success is not Runtime proof.
- b39-b44 identities are permanently reserved; any later product candidate is b45+ only after architecture selection.
- iOS17 evidence does not prove lower iOS/iPad; non-personal workspace/account switch and native attachment handoff remain Unknown/Unverified where not explicitly tested.
