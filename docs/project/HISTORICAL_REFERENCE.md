# Historical Reference — Previous iOS ChatGPT Client Experience

_Last summarized: 2026-08-26._

## Source package

- User-supplied archive: `ChatGPT_iOS_Native_Client_History_Pack_2026-08-25.zip`
- SHA-256: `571c6d100091792a85917c6451fb1b6d7d430b3eeaf798b8724a9bd7b90c3b98`
- Archive contents inspected: 22 files.
- High-value sources included: `00_START_HERE_FOR_NEW_PROJECT.md`, `01_EXECUTIVE_HANDOFF.md`, `04_LONG_CONVERSATION_PERFORMANCE.md`, `06_AUTH_NETWORK_AND_CONVERSATION_DATA.md`, `07_UPLOAD_DOWNLOAD_AND_ATTACHMENTS.md`, `10_NATIVE_CLIENT_ARCHITECTURE_HANDOFF.md`, `11_DO_NOT_REPEAT.md`, `12_MVP_ACCEPTANCE_CHECKLIST.md`, and `references/EVIDENCE_LEVELS.md`.

This archive came from a previous project. It is **reference-only**. It is not current source code, current ChatGPT protocol documentation, or proof that a historical design is correct for the new client.

## Additional user-confirmed historical result

On 2026-08-26 the user clarified that the previous Web-based IPA had already completed a working web-login flow for ChatGPT, and that the user's account signs in through **Google**. This is stronger evidence than a historical architecture suggestion: it confirms that this path worked in the previous app/runtime at that time.

It still does **not** prove that current Google/OpenAI authentication will accept the same embedded WebView flow today. Current Google OAuth guidance warns that authorization in embedded user-agents such as `WKWebView` can be rejected with `disallowed_useragent`. The new client must therefore reproduce the current login flow on-device and treat present runtime behavior as authoritative.

## Evidence boundary

Use the historical material in this order:

1. Old user runtime feedback is useful for identifying real failure classes and UX pain.
2. Old user-confirmed successful flows (including the previous Web IPA Google-based login) prove that the old implementation/runtime path worked at that time only.
3. Old repository/source evidence can prove that an implementation existed at that time only.
4. Old CI/artifact results prove build/package success only, not runtime correctness.
5. Historical diagnoses and architecture suggestions are hypotheses/experience until revalidated.
6. Historical private ChatGPT endpoint names, headers, request bodies, response shapes, streaming events, auth context, and conversation semantics are **not current contracts**.

Current user requirements, current repository source, current network/protocol evidence, current CI/artifacts, and current runtime testing always outrank this document.

## Distilled experience worth carrying forward

### 1. Do not use the old WebView project as the new source baseline

The previous project evolved from `ChatGPT Web + WKWebView + native enhancements`. It gained broad feature coverage quickly, but long-conversation performance, WebContent lifecycle, React/WebKit state, native overlays, recovery logic, and multiple state owners became increasingly expensive.

For the new project, the useful inheritance is the **problem model**, not the old chat-WebView implementation.

### 2. Long conversations need a data model separate from visible views

Historical work showed that hiding/detaching DOM does not remove React's full conversation state cost. Native development should preserve the principle that data may remain complete while UI only creates/reconfigures visible items.

Important historical lessons:

- Conversation history is a tree, not necessarily a flat array.
- `current_node -> parent -> ... -> root` was historically important for reconstructing the active branch.
- Internal reasoning/tool nodes, visible messages, and user/assistant turns are not the same concept.
- Edit/Regenerate can create branches.
- Streaming should update only the item/state that changed rather than causing broad re-layout.
- Upward history loading should preserve scroll anchor.

These are architectural clues; current ChatGPT data shapes must still be verified.

### 3. Conversation identity needs one authority

The old project repeatedly hit A/B conversation mix-ups when active conversation identity lagged behind UI navigation.

For the future native implementation, treat this as a strong design warning: conversation ID/navigation state should have one explicit owner. Header text, sidebar selection, URLs, visible text, and export UI should consume that state rather than becoming competing identity sources.

### 4. Current ChatGPT protocol research is a first-class task

Historical experience shows that knowing an endpoint name is insufficient. A working capability may depend on:

- Cookie/session state
- Authorization/access context
- account/workspace/project context
- required headers
- request body
- model/feature flags
- stream protocol
- pagination/cursor semantics
- status/error behavior

Before implementing list/detail/send/stream/upload/edit/regenerate or related functionality, capture current evidence from the official current environment. Old paths such as historical `/backend-api/...` names are search clues only.

### 5. Authentication should be separated from chat UI architecture

The previous Web IPA successfully used web login for the user's Google-based ChatGPT account. That result makes web-based bootstrap a high-value route to test first, but not an automatically accepted current implementation.

The durable lesson is to decouple:

- how session/auth context is established,
- from how conversation/navigation/message UI is rendered.

For the new client:

- reproduce the current Google-based login on-device first;
- if embedded Google authorization is rejected, capture the exact current evidence before selecting a supported system-browser/auth handoff;
- do not assume browser/WebKit/native-network session state can be copied or shared without current evidence;
- never log authentication secrets.

### 6. Attachments should be native-first and diagnosable

Historical user needs included selecting files, photos, videos, and iOS screen recordings that the official picker/UI did not always expose cleanly.

Useful experience:

- Avoid arbitrary client-side extension whitelists unless the backend contract requires them.
- Allow photo and video selection where product requirements call for both.
- Large files/videos should not be loaded into memory as one giant blob unnecessarily.
- Upload progress and HTTP/business failures should be diagnosable.
- Attachment upload identity/metadata should remain separate from message-send state.
- Temporary files need explicit cleanup ownership.

Backend acceptance rules still require current protocol evidence.

### 7. Export should read conversation data, not rendered UI

The previous project learned that export should not depend on which messages happen to be mounted/visible. Historical branch reconstruction also mattered for Edit/Regenerate conversations.

Future native export should therefore operate from the authoritative conversation model/store once that model is implemented and verified.

### 8. Avoid recovery logic that becomes a second failure source

Historical WebView development accumulated timers, watchdogs, DOM observers, reload/rebase logic, and fallback chains. Some of those mechanisms became performance and correctness risks themselves.

Carry forward the governance rule: do not add retry/fallback/watchdog/recovery mechanisms without a concrete current failure mode, a known state owner, a clear termination condition, and evidence that the normal path is insufficient.

### 9. Performance and diagnostics must be validated on real devices

Historical CI/artifact success did not answer the important runtime questions. The new project explicitly requires structured logging/diagnostics from the first executable build so future real-device failures can be reconstructed instead of inferred.

For future native-client work, distinguish at least:

- source written
- local/static checks
- CI passed
- artifact produced
- runtime/manual/real-device tested
- stable/frozen acceptance

Useful old measurement ideas for long conversations included response size, parse time, model/store construction time, first visible content, scroll hitches, input latency, stream update frequency, memory pressure, and background/foreground behavior.

## Historical MVP suggestion — not current scope commitment

The previous-project handoff suggested proving a narrow vertical loop first:

`login -> conversation list -> open conversation -> native long-conversation rendering -> send text -> streaming reply -> attachment upload`

The current durable roadmap refines that into:

`app/diagnostics foundation -> auth bootstrap -> protocol read -> native read -> send/stream -> long conversation -> attachments`

See `docs/project/DEVELOPMENT_PLAN.md`. This remains a dependency plan; each implementation phase still requires its own Development/Feature Work ID/checkpoint.

## Do-not-repeat reminders

Do not automatically recreate historical routes such as:

- chat UI running primarily in `WKWebView`
- broad DOM virtualization/MutationObserver systems
- scroll-pin watchdog loops
- Shadow WebView rebase/swap
- UI-text-based conversation identity
- multi-endpoint fallback chains used to mask an unknown protocol
- automatic reload/recreate based only on short transient latency
- exporting by scraping rendered UI

If a future current task has concrete evidence that one of these techniques is appropriate, it may be reconsidered explicitly; history alone is not a permanent ban.

## How future sessions should use this file

Consult this file when work touches authentication, protocol research, conversation state, long-conversation performance, streaming, attachments, export, recovery, diagnostics, or WebView/native boundaries.

Then verify the current source/protocol/runtime evidence before making implementation decisions. Do not ask the user to reconstruct these old lessons from chat history unless a specific missing detail is not represented here.
