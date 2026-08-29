# Project State

_Last updated: 2026-08-29 through b44 Runtime rejection plus explicit API-product rejection and hybrid-Web background-resilience gate._

## Current accepted merged baseline

- Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21 and list-cache b23 remain accepted merged baselines for their recorded scopes.
- **Phase 8 b38** remains the current Stable merged native reading/metadata/round-navigation baseline; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Exact b38 tested source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Stable does not mean Frozen; current native conversation modules remain Frozen No.

## Current Phase 9 — DEV-send-stream

### Security boundary retained

Exact b42 (`e8946e48a0b5ad86b402faf5eabba627e3393adf`, legitimate Artifact `9709824510`) proved successful tested ChatGPT-account Send requires browser anti-abuse challenge output: PoW, Turnstile and `so` required; non-empty PoW + Turnstile were finalized before Send.

Therefore pure-native/transient-auth ChatGPT-account Send remains blocked. Prohibited routes remain solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoint, hidden/shadow challenge WebView, challenge harvesting, DOM/message scraping that creates a second native response authority, covered-Web Native composer injection and synthetic hidden Send clicks.

### b43 visible-Web feasibility baseline

Exact b43 source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`, Artifact `9711364573`, IPA SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.

Primary-device Runtime:

- first/re-entry, keyboard/typing, visible Web Send, stream scrolling, rapid scrolling and native return had no material reported problem;
- Web `+` -> picker latency was roughly **100–200 ms**, not rejected as excessive;
- Web photo selection filtered video assets;
- standalone Settings Web-chat UX was not accepted as the final product interaction.

Verified iOS17 boundary: the public `WKUIDelegate.runOpenPanelWith...` replacement hook is iOS18.4+, so the iOS17 target cannot publicly swap the page's upload chooser for a custom PHPicker through that delegate. Proper iOS17 photo+video attachment support still requires separately evidenced native attachment upload/handoff.

### b44 integrated full-page hybrid trial

Exact identity:

- Candidate `DEV-send-stream-0.1.0-b44`, `0.1.0 (44)`;
- product/config source `f1503cf7121512a84e5c55a3642181c17324d791`;
- Push Run / Job `33245105815` / `99081114295` — success;
- PR Run `33245107290` — success;
- Artifact `9712583513`;
- ZIP `sha256:33ba4a99fe933241ce8023e811f15d55dfa0d95cac2693f039bb6138d813face`;
- IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.

Exact-device Runtime established:

1. Web Send worked.
2. Immediate `返回并同步` could surface the just-sent user message while assistant output already visible in Web was still absent from Native.
3. Repeated immediate Native Sync still could miss that assistant output.
4. A later Sync after waiting could expose it.
5. Tested Native A/B IDs mapped to the corresponding Web `/c/<id>` conversations.
6. A/B switching caused Web to load/render the selected conversation again.

Conclusion: Native Detail is eventually consistent relative to Web generation in this tested sequence; no stable readiness delay/signal was established. Do not add timer/poll/retry/repeated automatic Sync. The full-page Native -> Web -> Native product form is rejected / superseded.

## Latest product decision — API route rejected

The user explicitly stated that the separately authenticated/billed officially supported API product architecture will **not** be accepted for this client.

Do not keep the API product as an active Phase-9 alternative unless the user explicitly reverses that decision.

The active product question is now only:

1. prove an existing-ChatGPT-account visible-Web-assisted architecture can meet the required interaction/background behavior; or
2. defer ChatGPT-account Send.

## New hard gate — background reasoning/stream resilience

The user reports a high-frequency failure mode that is unacceptable: while reasoning/streaming, putting the client in background for a while can lead to timeout/disconnect and force manual refresh on return.

For any existing-account Web-assisted architecture, **background/lock survival or transparent foreground recovery is now a hard architecture gate before UI polish**.

Public iOS baseline:

- Apple documents that ordinary apps are suspended shortly after backgrounding unless granted additional finite execution time;
- `beginBackgroundTask` is finite and may expire/terminate early;
- therefore it may be used as a short-duration baseline but cannot be presented as a long-thinking guarantee.

TrollStore feasibility question:

- the repository already has a true-background experiment plan;
- however keeping the main app process alive does **not** yet prove WebKit WebContent/network processes or the official ChatGPT stream remain alive;
- exact-device Runtime must prove this on the primary iPhone 15 Pro Max / iOS17.0 TrollStore environment.

New durable owner: `HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md`.

Required outcome:

- preferred: same visible official-Web response remains alive across the user's normal background/lock habit and resumes without reload;
- acceptable recovery: when a **known** background/WebKit lifecycle interruption occurs, foreground return performs one deterministic same-conversation recovery without resending the prompt and without requiring manual refresh;
- rejected: routine manual refresh, timer/poll/retry loops, fake keepalive timers, hidden DOM recovery or permanent idle process immortality.

A silently stalled Web response with no native-observable failure signal remains Unknown/Unverified and must be exercised in Runtime testing.

## Current architecture gate

### Active direction — existing ChatGPT account/history continuity, conditional

Native list/history/read/navigation + an **explicitly visible official-Web composer/live-response surface** remains the only non-deferred Send direction.

It is **not accepted** until the background-resilience gate passes. Do not allocate a polished embedded-Web b45 merely to test layout first.

### Deferred direction

If the background-resilience experiment is No-go — Web generation routinely disconnects/stalls after normal background/lock and cannot transparently recover without violating security/authority rules — defer ChatGPT-account Send rather than hiding a fragile Web transport behind Native UI.

## Candidate / PR state

- b39-b44 identities are permanently reserved.
- No b45 is allocated.
- PR #29 remains open/mergeable as an evidence branch and must not be merged as accepted production Send UX.
- Exact b44 product source remains `f1503cf7121512a84e5c55a3642181c17324d791`; subsequent requirement/docs commits do not redefine that product Candidate.

## Authority / evidence rule

- `ConversationRepository` remains sole native conversation/list/read/recovery authority.
- `AuthSessionStore` remains native auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- UI text/title is never identity authority.
- Native Sync/Reload never resend/regenerate.
- CI/Artifact success is not Runtime proof.
- main-app process survival is not WebKit-stream survival proof.
- iOS17 evidence does not prove lower iOS/iPad; non-personal workspace/account switch and native attachment handoff remain Unknown/Unverified where not explicitly tested.
