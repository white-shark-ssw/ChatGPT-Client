# DEV-send-stream b76 device Runtime — 2026-08-31

## Candidate identity

- Work: `DEV-send-stream`
- Candidate: `DEV-send-stream-0.1.0-b76`
- Version / Build: `0.1.0 (76)`
- Exact product/config source: `0da5a7577f2cf3b2a6882d8a0ec920b5c8f37c71`
- User-supplied diagnostics: `ChatGPTClient-Diagnostics-20260831-213927.json`
- User-supplied screenshot: b76 conversation presentation showing GitHub tool rows plus reasoning/final text.

## Runtime classification

b76 is **partial positive / partial rejected**. It is not Stable/Frozen.

### Cross-platform active-response adoption — partial positive

User confirms the externally-started response is now adopted and visible in Native through thinking/reasoning/tool progression.

Diagnostics corroborate the page-owned read path:

- `21:23:58` external Repository live response starts (`source=external_page_owned`).
- matching page-owned `/resume` is observed and returns HTTP404 JSON; b76 correctly stays on the page-owned read path instead of failing the response.
- external snapshots then carry live reasoning/tool state:
  - `21:24:00`: `phase=reasoning`, `reasoningCharacters=82`, `toolCount=2`, `serviceMessageCount=6`.
  - `21:24:06`: `phase=reasoning`, `reasoningCharacters=82`, `toolCount=3`, `serviceMessageCount=8`.
  - `21:24:24`: `phase=reasoning`, `reasoningCharacters=182`, `toolCount=7`, `serviceMessageCount=18`.
  - `21:24:31`: `phase=final`, `toolCount=8`, `serviceMessageCount=23`.

### Cross-platform final answer body — rejected / not progressive

The user's observation is confirmed by diagnostics: the current evidenced plural response path does **not** expose incremental final body text before completion.

- `21:24:31`: `phase=final`, `finalCharacters=0`, `serviceMessageCount=23`.
- `21:24:42`: still `phase=final`, `finalCharacters=0`, `serviceMessageCount=23`.
- `21:24:48`: still `phase=final`, `finalCharacters=0`, `serviceMessageCount=23`.
- `21:25:00`: `finalCharacters` jumps directly to `6718`, then terminal fires in the same second; the following plural snapshot is `complete=true`.

Therefore b76 solves live reasoning/tool adoption but not true progressive final-answer body delivery. Increasing plural observation frequency would not create missing body bytes and must not be implemented. Do not fake streaming with a typewriter, timer, watchdog, retry loop, or synthetic chunking.

The next true-stream implementation requires exact evidence for an official page-owned body-bearing transport/presentation source during the final phase. WebSocket body authority remains unproven; current rules still prohibit parsing it as response authority without evidence.

### Refresh / login complaint — transport failure, not proven auth loss

The user's reported refresh failure is real, but the evidence does **not** show the login session disappearing.

Before the failure window, account probes succeed with HTTP200 session/account responses. During the later failure window:

- repeated manual list requests fail at the network stage with `NSURLErrorDomain/-1200` beginning `21:38:12`.
- a detail sync also fails with `NSURLErrorDomain/-1200` at `21:38:22`.
- after relaunch, WebKit persistent data is still present (`itemCount=45`, `matchedItemCount=26`).
- account-context probing then fails while requesting `/api/auth/session` with the same `NSURLErrorDomain/-1200`; there is no observed 401, 403, `notAuthenticated`, or cookie disappearance in this evidence.
- automatic list load preserves cached content and records `auth=temporarily_unavailable`; manual refresh surfaces failure.

`NSURLErrorDomain/-1200` is a secure-connection/TLS transport failure. Classify this Runtime event as **native secure-transport unavailable**, not as authenticated-session loss. Product changes may improve state/UX classification and preserve verified identity semantics, but must not add speculative retries/fallback timers.

### Typography — rejected

The screenshot rejects b76's current `toolLineHeight=30` and shared reasoning/final fixed line height `21`.

User requirement for the next candidate:

- tool-operation vertical rhythm must have matching top/bottom spacing around the tool row; current visible lower side is too tight.
- increase the current tool-line metric by 20% (`30 -> 36`) and keep the upper/lower tool-row vertical treatment symmetric.
- increase current reasoning/final line height by 20% (`21 -> 25.2`).
- do not change font size unless separately evidenced; this request is line-height/vertical-rhythm only.

## Next exact action

AI-owned continuation is allowed for one minimal b77 scope after identity/candidate guard:

1. apply the explicit typography correction above;
2. correct native auth/network state handling so transport/TLS failure is not represented as login loss, without retry/timer/watchdog/fallback machinery;
3. add only privacy-safe evidence needed to determine whether the official covered page exposes progressive final body text before `COMPLETE`; do not adopt a guessed WebSocket/DOM body source yet;
4. build/static/CI/Artifact/package-identity checks;
5. return to Human real-device Runtime.

b77 must not be described as allocated until the product/config candidate identity is actually committed.