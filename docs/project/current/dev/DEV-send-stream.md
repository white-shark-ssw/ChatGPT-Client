# DEV-send-stream

## Status

**Blocked — API product explicitly rejected; existing-account hybrid path must prove background resilience before b45**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail / 官方 Web / hybrid / 后台 / 真后台`
- **Branch / PR**: `dev/send-stream-20260829`; PR #29 open/mergeable; do not merge as accepted Send UX.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; Stable native predecessor b38 remains merged.
- **Current branch head before this docs batch**: `10843c106659186e84d08a181c1e0901f2a54857`.
- **Exact b44 product/config source**: `f1503cf7121512a84e5c55a3642181c17324d791`.
- **Exact b44 Artifact**: `9712583513`; IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.
- **Parallel guard**: current `docs/project/current/dev/` contains only this Active development checkpoint; no peer Active dev conflict found.
- **Candidate rule**: b39-b44 are permanently reserved. **No b45 is allocated.**

## Security / transport boundary retained

Exact b42 proved the tested successful ChatGPT-account Send requires browser anti-abuse challenge output (`proofOfWorkRequired=true`, `turnstileRequired=true`, `soRequired=true`, non-empty PoW + Turnstile finalize input). Pure-native/transient-auth ChatGPT-account Send remains blocked.

Never implement PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoints, hidden challenge-harvesting WebViews, DOM message/reasoning scraping, covered-Web Native composer injection, synthetic hidden Send clicks or browser challenge extraction/replay.

TD-024 permits only an **explicit user-visible** official ChatGPT Web Send surface. TD-025 records that b44's full-page Native -> Web -> Native form is not acceptable product UX.

## b43 / b44 accepted evidence retained

### b43 visible-Web feasibility

Exact b43 `DEV-send-stream-0.1.0-b43`, source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`, Artifact `9711364573`, IPA SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.

Primary-device Runtime:

- first/re-entry, keyboard/typing, visible Web Send, stream scrolling and rapid scrolling had no material problem reported;
- Web `+` -> attachment selection roughly **100–200 ms**, not rejected;
- Web Photos selection filtered video assets;
- standalone Settings Web-chat interaction was not accepted as final product UX.

Public `WKUIDelegate` file-open-panel replacement is iOS18.4+, not primary iOS17. Do not use private WebKit or DOM/file-input injection to fake an iOS17 photo+video picker fix.

### b44 integrated full-page trial

Exact b44 Candidate `DEV-send-stream-0.1.0-b44`, source `f1503cf7121512a84e5c55a3642181c17324d791`, Push Run/Job `33245105815` / `99081114295` success, PR Run `33245107290` success, Artifact `9712583513`, IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.

Runtime established:

1. Web Send worked.
2. Immediate `返回并同步` could expose the new user message but not assistant output already visible in Web.
3. Repeated immediate Native Sync still could miss that assistant output.
4. A later Sync after waiting could expose it.
5. Tested Native A/B IDs mapped to corresponding Web `/c/<id>` conversations.
6. A/B switching caused Web to load/render the selected conversation again.

Conclusion: Native Detail is eventually consistent relative to Web generation in the tested sequence; no stable readiness delay/signal was established. Do not add timer/poll/retry/repeated automatic Sync. The full-page Native -> Web -> Native product form is rejected / superseded.

## Latest explicit product decision — 2026-08-29

The user explicitly stated that the **separately billed/supported API product path will not be accepted**. Treat former TD-025 option B as rejected for this product unless the user later reverses that decision.

The user also raised a hard usability requirement for any existing-account Web-assisted architecture:

> During long reasoning / streamed reasoning-output / final-answer generation, putting the client into the background or leaving it there for a while must not routinely cause timeout/disconnect that forces the user to manually refresh on return.

This is now a **hard architecture acceptance gate**, not later polish.

## Background-resilience evidence boundary

Apple public iOS behavior is not sufficient as a long-duration guarantee:

- `beginBackgroundTask` grants only finite extra runtime;
- the system may expire the task, suspend the app, or terminate it;
- therefore ordinary UIKit background time may be a short-duration baseline but cannot honestly guarantee a long reasoning/stream session.

The repository already has `BACKGROUND_EXECUTION_PLAN.md`, including a TrollStore-only true-background experiment. However that plan assumed a native-owned response stream. TD-024 currently uses a visible official Web Send surface, so a new question must be proven:

**Can the primary iPhone 15 Pro Max / iOS17.0 TrollStore environment preserve the visible Web Send surface's actual WebKit/WebContent/network execution across background/lock for meaningful reasoning durations?**

Unknown / Unverified until exact-device testing:

- keeping the main app process runnable/non-freezable also keeps the relevant WebKit WebContent/Network processes alive;
- an official Web reasoning/stream connection survives background/lock without page reload;
- Wi-Fi/cellular transition survives while backgrounded;
- WebKit process termination can be recovered without user manual refresh;
- battery/thermal cost is acceptable.

Do not claim success merely because the main app process remains alive.

## Proposed account-compatible architecture, now conditional

The only active non-API direction remains:

**Native list/history/read/navigation + explicitly visible official-Web composer/live-response surface**.

But do **not** spend b45 on visual embedding first. Before accepting this architecture, prove background behavior.

Required behavior if this direction proceeds:

1. Web composer/live response remains genuinely visible/directly operated while Send is active; no hidden DOM automation.
2. If the app backgrounds during possible reasoning/streaming, use ordinary `beginBackgroundTask` only as the public short-duration baseline.
3. Because distribution is TrollStore, evaluate the existing true-background plan as an architecture feasibility experiment for the visible Web surface.
4. Preservation must be active only when needed; do not immortalize the app at idle.
5. Since exact Web response terminal state is not available to Native without prohibited DOM/stream scraping, an initial experiment may conservatively preserve the process for the whole background interval when the visible Send surface was active at background entry, then release on foreground return.
6. If preservation is known to have expired/lost or `WKWebView` content-process termination is observed, foreground recovery may perform **one lifecycle-triggered same-conversation Web recovery/reload**, not a timer/poll/retry loop. This is recovery from a known lifecycle interruption, not an automatic response polling mechanism.
7. If preservation succeeds, foreground return should resume the same live page/answer state without forced reload.
8. Manual user refresh must not be the normal recovery path.
9. Native Detail reconciliation remains eventual and must not be used as a fake real-time stream owner.

## Go / no-go Runtime matrix before UI b45

Any background feasibility Candidate must test on the exact primary iPhone/iOS17 TrollStore device:

- start a long visible Web reasoning/stream response, background for a short interval, return;
- repeat with device lock;
- repeat around 5 minutes, 15 minutes, then longer controlled intervals if the response/workload permits;
- verify whether the same live Web response continues without manual refresh;
- record whether app process, WebContent/process lifecycle and Web page survive;
- exercise the public background-task expiration path;
- exercise a known process/page interruption and verify one-shot foreground recovery does not resend the prompt;
- verify no duplicate message/send and no challenge/token capture;
- test Wi-Fi stable first, then network transition only after baseline works;
- observe battery/thermal impact sufficiently to reject an obviously harmful always-on design.

**Go**: Web reasoning/stream survives reliably enough for the user's background habit, or known interruption recovers automatically on foreground without manual refresh/resend.

**No-go**: long/ordinary background use repeatedly leaves the official Web stream disconnected and requires manual refresh, or keeping the WebKit execution alive is not reliable/acceptable. If no-go, do not proceed with a polished embedded-Web chat architecture; with API rejected, the remaining product-safe route is to defer ChatGPT-account Send.

## Batch recovery point — background requirement docs

Known baseline:

- branch head `10843c106659186e84d08a181c1e0901f2a54857` before this write chain;
- PR #29 open/mergeable;
- `main@34811877896ca88c6656be6676f5466a19931ce6` unchanged;
- no peer Active dev checkpoint;
- exact b44 product source remains `f1503cf7121512a84e5c55a3642181c17324d791`;
- no b45 allocated.

Completed:

- user rejected API product route;
- user promoted background reasoning/stream survival + no-manual-refresh recovery to a hard requirement;
- checkpoint updated with background architecture gate.

Pending docs-only batch:

- add a focused hybrid Web background-resilience plan under `docs/project/`;
- update `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_SPECIFIC_RULES.md`, `DEVELOPMENT_PLAN.md`, and PR #29 to reflect API rejection + background go/no-go gate;
- no Swift/Xcode/workflow/product mutation;
- no b45 allocation.

## Next exact action

Finish this docs-only requirement batch. Then stop at the remaining human architecture gate:

- if the user explicitly chooses to **run the existing-account background feasibility experiment**, create the appropriately isolated/stacked background experiment work according to `BACKGROUND_EXECUTION_PLAN.md`, re-run conflict/candidate preflight, and only then allocate a new Candidate;
- if the user chooses to defer account Send, leave `DEV-send-stream` blocked;
- do not reactivate the API route unless the user explicitly reverses the rejection.
