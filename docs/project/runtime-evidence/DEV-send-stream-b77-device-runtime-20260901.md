# DEV-send-stream b77 device Runtime — 2026-09-01

## Candidate under test

- Work ID: `DEV-send-stream`
- Candidate: `DEV-send-stream-0.1.0-b77`
- Version / Build: `0.1.0 (77)`
- Exact product/config source: `c0266e83a5a27d2e39751ecb84a25e0072fb01f4`
- Canonical Artifact: `9777216066`
- Supplied diagnostics metadata independently reports Candidate b77, Build 77 and source marker `c0266e83a5a2`.

## User Runtime findings

### 1. Inline tool presentation remains rejected

The user-supplied iPhone screenshot shows inline GitHub/tool activity rows still have visually incorrect vertical rhythm and are not prominent enough as a special message type.

Source inspection explains why b77 did not fully normalize the spacing: reasoning paragraphs still use their own `paragraphSpacing`, while tool paragraphs use both `paragraphSpacingBefore` and `paragraphSpacing`. A transition into a tool row can therefore combine the previous paragraph's trailing spacing with the tool paragraph's leading spacing, while a transition out of a tool row follows a different total. Merely increasing `toolLineHeight` could not make the inter-item rhythm symmetric.

Runtime result: **Rejected.**

### 2. User-message presentation differs from official Web and visibly truncates

The user supplied side-by-side screenshots of the same round on official Web and Native. Official Web presents the full user message with inline-link rendering. Native presents raw markup and the bubble stops mid-sentence after `...证据边界和下`, despite `UILabel.numberOfLines = 0`.

Current Native source renders user messages as plain `UILabel.text`, while geometry is independently measured with `NSString.boundingRect`. The reported message begins with long link/markup text, which is exactly a class where rendering and independent measurement must not be allowed to diverge. b78 must use the same attributed representation for user rendering and measurement, with explicit wrapping, and preserve full message content.

Runtime result: **Rejected.**

### 3. Relaunch during externally active response can lose history and remain stuck on `正在读取会话…`

This defect is directly explained by diagnostics and current source.

At the 07:03:49Z relaunch:

1. Web data warmup completes with 44 website-data items / 26 auth-domain matches.
2. Account-context probe succeeds: `/api/auth/session` HTTP200, accounts HTTP200, account state becomes `verified`.
3. Native starts both conversation-list GET and selected-conversation Detail GET on the same transient session.
4. The list GET returns HTTP403.
5. `authTransport.invalidated` immediately retires the current transient session using `invalidateAndCancel()`.
6. The in-flight Detail is cancelled after only ~158ms.
7. The Detail cancellation path logs `detail.cancelled` and returns without finishing/removing the still-current Detail operation.
8. Later requests at 07:04:25Z and 07:04:59Z log `detail.coalesced` against operationGeneration 1 with completion counts 2 then 3; the operation never reaches a terminal result.
9. External page-owned streaming begins with `baselineVisibleMessageCount=0`, so only the live reasoning/tool/final overlay can render. The authoritative user/history rows remain absent and the UI keeps the pending-read state.
10. Only after external terminal causes a replacement Sync at 07:05:32Z does a new Detail operation succeed at HTTP200, returning 34 visible messages and restoring authoritative history.

This is **not** an authentication-loss finding. The same launch verified the account immediately before the route-specific list 403.

Runtime result: **Rejected; root cause identified.**

## Progressive final-body evidence from b77

b77's structure-only DOM probe did not reveal an earlier progressive final-body source:

- At external streaming start 07:04:06Z, the latest official-Web assistant DOM snapshot is still the previous assistant set: `assistantNodeCount=4`, `textCharacters=4867`.
- Native plural snapshots remain `finalCharacters=0` through 07:05:15Z.
- At 07:05:21Z the page-owned plural snapshot jumps directly to `finalCharacters=5475`.
- Only after that, at 07:05:22Z, DOM structure changes to `assistantNodeCount=5`, `textCharacters=4444`.

Therefore the tested covered DOM does **not** provide current-response final text earlier than the already-observed completed plural body. This evidence does not justify a DOM-body authority, fake typewriter stream, polling, timer, retry or WebSocket-body parser.

## b78 evidence-backed correction boundary

Allowed minimal product changes:

1. Make inline tool rows a clearly distinct presentation and remove compound/directional paragraph spacing so inter-item vertical spacing has one deterministic source.
2. Render and measure user-message text from the same attributed representation with explicit wrapping; use inline Markdown semantics where the OS supports it, with a plain exact-text fallback.
3. On route-level 401/403, retire the shared transient session for future requests without cancelling already-running requests.
4. If a Detail task is cancelled while its operation is still current, finish that operation instead of leaving a permanently coalescing load.
5. Keep b77's privacy-safe structural DOM evidence; do not promote DOM text to response authority.

No retry/timer/watchdog/polling/duplicate Send/second state owner is allowed.

## Evidence classification

- b77 Code/CI/Artifact/package: previously verified.
- b77 Runtime/manual/real-device: **Partial/rejected**.
- Cross-platform reasoning/tool adoption: remains positive.
- Inline tool presentation: **Rejected**.
- User-message parity/integrity: **Rejected**.
- Relaunch authoritative-history loading: **Rejected; root cause identified**.
- Progressive final-body source: **still unresolved; DOM structure probe negative for earlier body availability**.
- Stable/Frozen Send: **No**.
