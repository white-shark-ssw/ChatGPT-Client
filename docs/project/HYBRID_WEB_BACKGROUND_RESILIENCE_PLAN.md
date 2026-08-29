# Hybrid Web Background Resilience Plan

_Last updated: 2026-08-29 through exact b45 repeated active-response background/lock Runtime._

## Purpose

This document owns the **existing-ChatGPT-account / user-visible official-Web Send background-resilience gate** for `DEV-send-stream` after exact b44 Runtime rejected the full-page Native -> Web -> Native product interaction.

It supplements `BACKGROUND_EXECUTION_PLAN.md`. The older plan primarily assumes a native-owned response stream. This file covers the narrower current question: whether a **visible official ChatGPT Web composer/live-response surface** can survive or automatically recover from iOS background/lock in the TrollStore deployment without hidden DOM automation, challenge harvesting or manual user refresh.

## Product decision

The user explicitly rejects the separately billed/supported API product route for this client.

Therefore the only active Send direction worth further evaluation is existing ChatGPT-account continuity through an explicitly visible official-Web surface. That direction is **not accepted** until the remaining response-ownership/background gates pass.

Hard user requirement:

- during long reasoning / streamed reasoning-output / final-answer generation, backgrounding or locking the client for a while must not routinely leave the conversation timed out/disconnected and require manual refresh on return.

This is a product architecture requirement, not later polish.

## Exact b45 short-background Runtime evidence

Candidate / device:

- `DEV-send-stream-0.1.0-b45`, exact source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`;
- Artifact `9713774868`, IPA SHA `9fc53543d652cc42c824feea8e8cc77cb5341c577a44d499e7ed2a3c8b1ec136`;
- iPhone / iOS17.0 / Release.

The clean default-primary new-chat capture used `POST /backend-api/f/conversation` -> HTTP200 `text/event-stream` and then remained on that original `fetch` stream while the app was repeatedly backgrounded/locked.

Active-response background intervals:

1. approximately **35 seconds**;
2. approximately **34 seconds**;
3. approximately **126 seconds**.

Total active-response background time: approximately **195 seconds / 3m15s**.

Total Send-to-terminal elapsed time: approximately **227 seconds / 3m47s**.

At the end of the final ~126-second interval, foreground return and the original-stream terminal sequence occurred in the same second: `server_ste_metadata -> message_stream_complete -> conversation_detail_metadata -> [DONE]`.

No second Send, no new SSE response, no resume/handoff/turn-stream/subscription/EventSource/WebSocket connection, and no manual refresh/resend were observed.

### Accepted conclusion from this exact scope

On the primary device, the tested official-Web/WebKit response path can **survive or buffer across repeated ordinary background/lock intervals**, including one ~126-second continuous interval, and still complete normally.

### Important non-conclusions

This does **not** prove:

- continuous per-event delivery while suspended rather than buffering until foreground;
- 5-minute or 15-minute background survival;
- WebContent process survival after actual process termination;
- network-loss recovery;
- battery/thermal acceptability;
- Native same-response continuation.

Because the original stream survived, this capture also did not force official Web to expose any reconnect mechanism.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`.

## Public iOS baseline

Apple documents that ordinary apps are placed into the suspended state shortly after entering background and that `beginBackgroundTask(withName:expirationHandler:)` grants only finite additional execution time. The system can expire that task or terminate the app earlier according to conditions.

Therefore:

- `beginBackgroundTask` is a valid short-duration baseline;
- it is **not** a long-reasoning guarantee;
- do not advertise or encode fixed promises such as 5/15/30/60 minutes from public UIKit background time;
- do not add timer keepalives or unrelated audio/location background-mode abuse.

Reference:

- Apple: `Extending your app's background execution time`
- Apple: `Choosing Background Strategies for Your App`

## Remaining TrollStore-specific feasibility question

The repository already records source-level evidence that TrollStore-only long-running/non-freezable process techniques exist. Exact b45 now provides a positive ordinary short-background signal even without a privileged preservation implementation, but it does **not** close the longer-duration/process-failure gate.

Remaining questions:

- 5-minute / 15-minute WebKit response survival;
- actual WebContent / network-process termination behavior;
- official recovery after real connectivity loss;
- reasoning/stream state continuity after a genuine transport/process break;
- Wi-Fi/cellular transition behavior;
- battery/thermal cost;
- whether a Web process termination can be transparently recovered without user refresh.

Do not treat `main app process still alive` as proof of any remaining item above.

## Security / authority boundary

This experiment must preserve TD-023/TD-024/TD-025/TD-027:

- official Web Send surface remains visible and directly user-operated;
- no Native composer injection into hidden Web DOM/contenteditable;
- no synthetic hidden Send clicks;
- no DOM answer/reasoning scraping to create Native response authority;
- no Sentinel/Turnstile/PoW extraction, replay or solver;
- no second persistent credential store;
- `ConversationRepository` remains sole native read/recovery authority;
- default persistent `WKWebsiteDataStore` remains persistent browser-auth authority.

The experiment is about **response/background/recovery behavior**, not Send-protocol bypass.

## Immediate next experiment — force the original transport to fail

Repeated ordinary short background is no longer the best way to discover official reconnect behavior because exact b45 showed the original fetch can remain viable across those intervals.

Before allocating a Native continuation implementation, reuse exact b45 and force one controlled connectivity interruption:

1. Use default ChatGPT / primary assistant in an **existing long conversation**.
2. Start a response expected to remain active long enough to observe recovery.
3. While visibly streaming, remove connectivity for about **10–15 seconds** and then restore it.
4. Preferred deterministic variant: Airplane Mode / both Wi-Fi and cellular unavailable, then restore. A Wi-Fi -> cellular transition is also useful after a stable Wi-Fi baseline.
5. Do not refresh, resend, Stop, switch GPT or navigate away.
6. Let official Web recover or fail naturally.
7. Export b45 diagnostics.

Evidence question:

> After a genuine transport break, does official Web open a status/resume/handoff/turn-stream/subscription connection that continues the same already-started response without a second Send?

If yes, only that exact observed route/transport/identity structure may justify a later b46 Native no-resend parity experiment.

If no, record the negative evidence; do not guess from the existence/name of `resume_conversation_token`.

## Activation model for any future background-preservation implementation

Native does not currently possess an authoritative Web response terminal signal without prohibited DOM/stream observation.

Therefore any future preservation experiment should remain deliberately conservative:

1. User is on the explicitly visible Web Send/live-response surface.
2. App enters background/lock.
3. Retain the accepted preservation mechanism for the entire background interval while that visible Send surface was active at background entry.
4. Release preservation on foreground return, explicit departure from that Send surface before backgrounding, or preservation failure/expiration.

Do **not** invent a fake `isWebStreaming` Boolean derived from UI text, timers or DOM scraping.

A later narrower activation policy requires real evidence for a supported response lifecycle signal.

## Foreground recovery contract

Normal success case:

- background preservation remains valid;
- WebKit page/stream survives;
- foreground return resumes the same official Web live-response page without forced reload.

Known-interruption case:

- public background assertion expired;
- privileged preservation reports loss/failure;
- `webViewWebContentProcessDidTerminate` is observed;
- navigation/process failure is otherwise explicitly known.

For a **known interruption**, foreground recovery may perform exactly one lifecycle-triggered recovery of the same visible official-Web conversation page.

Rules:

- no prompt resend/regenerate;
- no timer/poll/retry loop;
- no repeated automatic Native Sync waiting for assistant visibility;
- no hidden page recreation solely to harvest challenge output;
- recovery remains visible or is completed immediately as the user returns to the visible Send surface;
- one recovery attempt must be logged with privacy-safe reason/timing only.

A silently stalled Web response with no supported/native-observable failure signal remains Unverified; do not invent DOM scraping to detect it.

## Public baseline instrumentation for a future dedicated background candidate

Before any privileged TrollStore claim, instrument the visible-Web path with:

- app foreground/background transitions;
- `beginBackgroundTask` begin/end/expiration;
- `UIApplication.backgroundTimeRemaining` sampled only at meaningful lifecycle points, not heartbeat polling;
- Web navigation start/finish/failure class;
- `webViewWebContentProcessDidTerminate`;
- current safe route class/target match;
- foreground-return outcome: resumed / known-interruption recovery / user-visible failure.

Never log prompt, response text, reasoning text, raw conversation ID, auth values or challenge material.

Exact b45's current lifecycle logging is sufficient for its protocol/background observation purpose; it is not yet the full dedicated background instrumentation above.

## TrollStore true-background experiment

If later evidence still requires privileged preservation, create a separate isolated/stacked development Work per repository governance, based on the current unmerged Send branch only when conflict/ownership is documented.

Preferred order remains evidence-minimal:

1. attempt the smallest process-preservation mechanism that affects only this client;
2. keep ChatGPT cookies/tokens/message bodies out of any privileged helper;
3. if a helper is required, IPC is lifecycle/process-control only;
4. do not grant broad private entitlements to the main app without necessity evidence;
5. do not move authenticated ChatGPT traffic into a privileged helper merely for convenience.

The central Runtime question is WebKit continuity, not merely whether a helper can keep a PID alive.

## Go / no-go matrix

Primary authority: exact iPhone 15 Pro Max / iOS17.0 / TrollStore candidate.

Progress:

- brief/repeated ordinary background + lock: **positive exact-b45 signal up to ~126s continuous / ~195s cumulative active-response background**;
- no manual refresh/resend in that exact capture;
- 5-minute and 15-minute intervals: Pending;
- genuine network-loss recovery: Pending;
- observed WebContent/process failure + one-shot recovery: Pending;
- battery/thermal: Pending.

Remaining minimum sequence:

1. Force one real connectivity interruption while an existing long response is active; observe official recovery without resend.
2. Repeat background around 5 minutes when workload permits.
3. Repeat around 15 minutes when workload permits.
4. Extend to 30/60-minute observations only if a controlled response/workload can meaningfully remain active; do not fabricate fixed-duration support.
5. Exercise public background-task expiration in a dedicated background candidate if that path is implemented; verify no resend.
6. Exercise an observed WebContent/process failure and verify one-shot foreground recovery.
7. Verify no duplicate user message/assistant response caused by recovery.
8. Verify stable Wi-Fi baseline before Wi-Fi/cellular transition testing.
9. Observe battery/thermal impact enough to reject clearly harmful always-on behavior.
10. Recheck WebKit login/session handling after longer background intervals.

### Go

The existing-account hybrid direction may proceed only if one of these is true on the recorded primary device:

- the visible official-Web reasoning/stream reliably survives the user's normal background/lock habit; or
- a known lifecycle interruption is recovered automatically on foreground with no prompt resend and no routine manual refresh.

Exact b45 is encouraging for ordinary short background, but it does not yet satisfy the full Go matrix.

### No-go

Reject the embedded-Web product direction if:

- ordinary background use repeatedly leaves Web generation disconnected/stalled and the user must manually refresh;
- process preservation cannot reliably keep the required WebKit execution alive where needed;
- recovery requires DOM/hidden-Web automation prohibited by project security boundaries;
- battery/thermal impact is unacceptable;
- the implementation requires permanently keeping the app alive while idle.

Because the API product route is explicitly rejected, a No-go result means **defer ChatGPT-account Send** rather than hiding a fragile Web transport behind Native UI.

## Relationship to response-ownership / UI work

Current sequencing:

1. exact b45 forced-transport-interruption evidence;
2. if official reconnect traffic is observed, smallest b46 Native no-resend parity experiment;
3. only after response ownership is proven, decide the correct background implementation owner;
4. polished integrated UI follows the response-owner decision;
5. attachments remain a later independent transfer/handoff gate, including the iOS17 video-picker limitation.

Do not spend a new Candidate merely to repeat an observation exact b45 can already make.

## Evidence ladder

Keep these separate:

- Code written;
- CI passed;
- Artifact produced;
- ordinary background/lock survival observed;
- WebKit page remained alive;
- response stream remained viable/buffered through foreground return;
- genuine transport-failure recovery worked;
- 5/15-minute matrix accepted;
- exact-device background matrix accepted;
- Native response ownership accepted;
- product architecture accepted;
- Stable/Frozen.

Never collapse these into one claim.