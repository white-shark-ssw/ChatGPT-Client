# Hybrid Web Background Resilience Plan

_Last updated: 2026-08-29._

## Purpose

This document owns the **existing-ChatGPT-account / user-visible official-Web Send background-resilience gate** for `DEV-send-stream` after exact b44 Runtime rejected the full-page Native -> Web -> Native product interaction.

It supplements `BACKGROUND_EXECUTION_PLAN.md`. The older plan primarily assumes a native-owned response stream. This file covers the narrower current question: whether a **visible official ChatGPT Web composer/live-response surface** can survive or automatically recover from iOS background/lock in the TrollStore deployment without hidden DOM automation, challenge harvesting or manual user refresh.

## Product decision

The user explicitly rejects the separately billed/supported API product route for this client.

Therefore the only active Send direction worth further evaluation is existing ChatGPT-account continuity through an explicitly visible official-Web surface. That direction is **not accepted** until this background gate passes.

Hard user requirement:

- during long reasoning / streamed reasoning-output / final-answer generation, backgrounding or locking the client for a while must not routinely leave the conversation timed out/disconnected and require manual refresh on return.

This is a product architecture requirement, not later polish.

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

## TrollStore-specific feasibility question

The repository already records source-level evidence that TrollStore-only long-running/non-freezable process techniques exist. That does **not** prove they preserve this app's official-Web ChatGPT stream.

The critical current question is:

> If the main TrollStore client is kept runnable/non-freezable while a visible ChatGPT Web Send surface is active, do the relevant WebKit WebContent/Network processes and the official Web response stream also remain alive across background/lock?

Until exact-device evidence exists, all of the following remain **Unknown / Unverified**:

- WebContent process survival;
- WebKit network-process survival;
- official ChatGPT stream continuity;
- reasoning/stream DOM state continuity without reload;
- background lock behavior;
- Wi-Fi/cellular transition behavior;
- battery/thermal cost;
- whether a Web process termination can be transparently recovered without user refresh.

Do not treat `main app process still alive` as proof of any item above.

## Security / authority boundary

This experiment must preserve TD-023/TD-024/TD-025:

- official Web Send surface remains visible and directly user-operated;
- no Native composer injection into hidden Web DOM/contenteditable;
- no synthetic hidden Send clicks;
- no DOM answer/reasoning scraping to create Native response authority;
- no Sentinel/Turnstile/PoW extraction, replay or solver;
- no second persistent credential store;
- `ConversationRepository` remains sole native read/recovery authority;
- default persistent `WKWebsiteDataStore` remains persistent browser-auth authority.

The experiment is about **process/background survival**, not Send-protocol bypass.

## Activation model for the first experiment

Native does not currently possess an authoritative Web response terminal signal without prohibited DOM/stream observation.

Therefore the first background experiment should be deliberately conservative:

1. User is on the explicitly visible Web Send/live-response surface.
2. App enters background/lock.
3. Start/retain the accepted background-preservation mechanism for the entire background interval while that visible Send surface was the active interaction surface at background entry.
4. Release preservation when the app returns to foreground, the user explicitly leaves the Send surface before backgrounding, or the preservation mechanism itself expires/fails.

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

A silently stalled Web response with no supported/native-observable failure signal remains Unverified and must be exercised in Runtime testing; do not invent DOM scraping to detect it.

## Public baseline experiment

Before any privileged TrollStore claim, instrument the existing visible-Web path with:

- app foreground/background transitions;
- `beginBackgroundTask` begin/end/expiration;
- `UIApplication.backgroundTimeRemaining` sampled only at meaningful lifecycle points, not heartbeat polling;
- Web navigation start/finish/failure class;
- `webViewWebContentProcessDidTerminate`;
- current safe route class/target match;
- foreground-return outcome: resumed / known-interruption recovery / user-visible failure.

Never log prompt, response text, reasoning text, raw conversation ID, auth values or challenge material.

Public baseline is expected to be finite-time only. A short success does not prove long background support.

## TrollStore true-background experiment

If the user explicitly authorizes the existing-account background feasibility experiment, create a separate isolated/stacked development Work per repository governance, based on the current unmerged Send branch only when conflict/ownership is documented.

Preferred order remains evidence-minimal:

1. attempt the smallest process-preservation mechanism that affects only this client;
2. keep ChatGPT cookies/tokens/message bodies out of any privileged helper;
3. if a helper is required, IPC is lifecycle/process-control only;
4. do not grant broad private entitlements to the main app without necessity evidence;
5. do not move authenticated ChatGPT traffic into a privileged helper merely for convenience.

The central Runtime question is WebKit continuity, not merely whether a helper can keep a PID alive.

## Go / no-go matrix

Primary authority: exact iPhone 15 Pro Max / iOS17.0 / TrollStore candidate.

Minimum sequence:

1. Start a long official-Web reasoning/stream response; background briefly; return.
2. Repeat with device lock.
3. Repeat around 5 minutes.
4. Repeat around 15 minutes when workload permits.
5. Extend to 30/60-minute observations only if a controlled response/workload can meaningfully remain active; do not fabricate fixed-duration support.
6. Record whether the same visible page/stream resumes without manual refresh.
7. Exercise public background-task expiration and verify no resend.
8. Exercise an observed WebContent/process failure and verify one-shot foreground recovery.
9. Verify no duplicate user message/assistant response caused by recovery.
10. Verify stable Wi-Fi baseline before testing Wi-Fi/cellular transition.
11. Observe battery/thermal impact enough to reject clearly harmful always-on behavior.
12. Recheck WebKit login/session handling after background intervals.

### Go

The existing-account hybrid direction may proceed only if one of these is true on the recorded primary device:

- the visible official-Web reasoning/stream reliably survives the user's normal background/lock habit; or
- a known lifecycle interruption is recovered automatically on foreground with no prompt resend and no routine manual refresh.

### No-go

Reject the embedded-Web product direction if:

- ordinary background use repeatedly leaves Web generation disconnected/stalled and the user must manually refresh;
- process preservation cannot reliably keep the required WebKit execution alive;
- recovery requires DOM/hidden-Web automation prohibited by project security boundaries;
- battery/thermal impact is unacceptable;
- the implementation requires permanently keeping the app alive while idle.

Because the API product route is explicitly rejected, a No-go result means **defer ChatGPT-account Send** rather than hiding a fragile Web transport behind Native UI.

## Relationship to UI work

Do not allocate a polished embedded-Web composer b45 merely to test layout before this gate is resolved.

Recommended sequencing:

1. background-survivability feasibility candidate;
2. exact-device Go/No-go evidence;
3. only after Go, design the embedded visible composer/live-response UI Candidate;
4. attachments remain a later independent transfer/handoff gate, including the iOS17 video-picker limitation.

## Evidence ladder

Keep these separate:

- Code written;
- CI passed;
- Artifact produced;
- main app process remained alive;
- WebKit page remained alive;
- response stream remained alive;
- foreground recovery worked;
- exact-device background matrix accepted;
- product architecture accepted;
- Stable/Frozen.

Never collapse these into one claim.
