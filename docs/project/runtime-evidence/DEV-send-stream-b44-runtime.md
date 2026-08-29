# DEV-send-stream b44 — integrated hybrid Runtime

_Date: 2026-08-29_

## Exact identity

- Candidate: `DEV-send-stream-0.1.0-b44`
- Version/build: `0.1.0 (44)`
- Exact product/config source: `f1503cf7121512a84e5c55a3642181c17324d791`
- Push Run / Job: `33245105815` / `99081114295` — success
- PR Run: `33245107290` — success
- Artifact: `9712583513`
- Artifact ZIP digest: `sha256:33ba4a99fe933241ce8023e811f15d55dfa0d95cac2693f039bb6138d813face`
- IPA: `ChatGPTClient-0.1.0-b44-dev-send-stream.ipa`
- IPA SHA-256: `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`
- Embedded package identity independently verified: `0.1.0 (44)`, Candidate b44, source marker `f1503cf71215`, Release, iOS14 minimum, `[1,2]`, arm64.

## Test environment

Primary project device/runtime: iPhone 15 Pro Max / iOS 17.0.

## Tested b44 flow

`native selected conversation -> 发送消息… -> visible Web /c/<conversation-id> -> Send -> 返回并同步 -> native detail`

b44 intentionally performed one explicit Repository `syncLatestMessages(id:)` on `返回并同步`; ordinary Back performed no automatic Sync.

## User-observed Runtime

1. Web Send worked.
2. Immediately tapping `返回并同步` caused the new **user message** to appear in Native.
3. The assistant answer was not visible in Native at that time.
4. Re-entering the same Web conversation showed the assistant had already produced substantial answer content.
5. Ordinary Back returned to Native without automatic Sync, as designed; Native still lacked the assistant answer.
6. Re-entering Web and tapping `返回并同步` again still did not immediately expose the assistant answer in Native.
7. Native `同步最新消息` immediately afterward also did not expose the assistant answer.
8. After waiting and then using Native Sync again, the assistant answer became visible.
9. Switching Native from conversation A to conversation B and tapping `发送消息…` caused the resident Web surface to immediately navigate/reload away from A and show B's history correctly.

## Evidence-backed conclusions

### Same-conversation mapping

The tested native conversation ID -> public Web `/c/<conversation-id>` mapping worked for the supplied A/B switching path. This is accepted only for the tested scope; it is not a public API contract.

### Post-Send native read visibility is eventually consistent relative to Web

The Web surface can already display assistant output while an immediate Native Detail reconciliation still lacks that assistant output. Repeating immediate explicit Sync did not close the gap; a later Sync did.

Therefore one immediate `返回并同步` request is not evidence of an immediate Web->Native completed-turn handoff.

Do **not** convert this observation into an arbitrary delay constant, timer, polling loop or speculative automatic retry chain. No exact stable readiness signal or delay duration has been evidenced.

### Duplicate conversation work

The Native Detail is already loaded before Send. Entering b44's Web Send surface then loads/renders the same conversation again in Web. Switching A -> B repeats that Web conversation load. The user explicitly identified this double-work/interaction shape as a major product defect.

### Product UX rejection

The user judged the full-page Native -> Web -> Native interaction as making the native client lose its purpose because actual conversation interaction still happens through Web after first entering the native detail.

b44 is therefore **not accepted as production Send UX**, even though the Web route and explicit Native reconciliation functioned.

## User proposal and security boundary

The user proposed covering a Web surface with Native UI and using a Native input field that forwards text into Web for Send.

Under current evidence, a fully covered/hidden Web surface driven by Native input requires programmatic DOM/JS/input automation or equivalent hidden browser interaction. That would make Web a hidden/shadow protected Send transport and conflicts with TD-023/TD-024's current boundary.

Rejected without a new supported transport:

- fully hidden/covered WebView used only to execute browser challenge + Send;
- Native composer text injection into hidden Web DOM/contenteditable;
- synthetic hidden Web Send clicks;
- DOM/stream scraping to create immediate Native assistant authority;
- extracting/replaying browser challenge output.

## Architecture gate reopened

### Choice A — account-compatible compromise

Native conversation history/read/navigation remain primary; embed an **explicitly visible** official-Web composer/live-response panel in the native detail instead of pushing a separate full-page Web chat.

The real official Web composer remains directly user-operated and visible. This can remove the b44 browser-like push/pop interaction, but it cannot honestly make Send/stream fully Native. While the browser response is active, immediate Native mirror remains unavailable under current evidence.

### Choice B — truly Native supported API product

Use an officially supported API with separate API authentication/billing, then implement Native composer, incremental stream ownership and attachments natively. This is a different product/billing path and must not be represented as the existing ChatGPT subscription/session/history without explicit support evidence.

### Choice C — defer ChatGPT-account Send

Retain the Stable native read client and wait for a supported ChatGPT-account transport that does not require browser-owned challenge output.

## Evidence classification

- Code written: passed.
- CI passed: passed.
- Artifact produced / identity verified: passed.
- Runtime route/mapping/reconciliation evidence: accepted for the observations above.
- Full-page integrated hybrid UX: **rejected**.
- Stable/Frozen: **No**.
- Next product Candidate: **not allocated**; b45+ only after an explicit architecture choice.