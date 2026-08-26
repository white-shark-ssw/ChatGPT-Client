# Background Execution / Completion Notification Plan

_Last updated: 2026-08-27._

## Purpose

Define how the TrollStore-installed native client should keep one or more in-progress ChatGPT responses alive after the user backgrounds/locks the device and notify the user locally when responses complete.

This plan intentionally separates the **ordinary iOS-safe baseline** from a **TrollStore-only true-background experiment**. The experimental path must not block the first daily-chat candidate.

See also `docs/project/CLIENT_ARCHITECTURE_GAP_REVIEW.md` and `docs/project/MULTI_CONVERSATION_STATE_PLAN.md`.

## Product goal

When one or more responses are actively reasoning/streaming and the user leaves the app:

1. keep the existing response lifecycle/network streams running for as long as the accepted runtime mechanism permits;
2. if a response completes while the app is backgrounded, commit its final state through that response's normal conversation/response owner and show a local notification such as `回答已完成`;
3. if background execution stops before a response completes, never resend the prompt automatically; when the user returns, use the existing `同步最新消息` recovery path for the affected conversation;
4. consume essentially no special background resources when no response is active.

There is **no product requirement for a fake 30-minute / 1-hour selector**. Public iOS APIs do not provide that guarantee. If a TrollStore true-background technique is accepted, the desired behavior is instead **active-response-set continuation**: enable only while at least one owned response requires background preservation, then release when the protected set becomes empty.

## Evidence classification

### `巨魔真后台`

Public distribution material currently identifies:

- name: `巨魔真后台`;
- developer: `bswbw`;
- current public version seen during research: 1.5;
- stated TrollStore support: iOS 14.0–16.6.1 / 17.0;
- stated behavior: enable/disable true background for running apps, with explicit battery-cost warning.

Public reference inspected: `https://trollstore.xin/180.html`.

**No public GitHub/source repository for this exact app was found during the 2026-08-26 search.** Therefore its internal implementation is Unknown / Unverified and must not be described as known.

### Open-source TrollStore reference chain

`Lessica/TrollSpeed` is a concrete open-source TrollStore reference at commit/tree `a609be260c8261ead36509c3bc4ded8479da9c40`.

Relevant evidence:

- README states the TrollStore build spawns a HUD process with root privilege and uses UIDaemon/AssistiveTouch-derived behavior to persist outside the normal foreground app lifecycle.
- `sources/HUDHelper.mm` uses root persona spawning (`posix_spawnattr_set_persona_np`, uid/gid 0) and can launch a detached process group without waiting for normal child completion.
- `supports/entitlements.plist` includes private capabilities such as `platform-application`, `com.apple.private.kernel.jetsam`, `com.apple.private.memorystatus`, `com.apple.private.security.no-sandbox`, and SpringBoard/background-related entitlements.
- `sources/JetsamHelper.h` sets a process to critical jetsam priority, removes high-water/task limits, marks it unmanaged/non-freezable, and disables dirty tracking.
- Open-source projects such as `inyourwalls/Blossom` explicitly credit TrollSpeed/UIDaemon AssistiveTouch logic for running a TrollStore process in the background indefinitely.

This is **reference evidence that TrollStore-only long-running processes are technically possible**, not proof that the same technique can safely preserve this client's existing authenticated streaming connections.

Apple XNU documentation also confirms that process freezability is a distinct memorystatus property and that system components can opt processes out of freezing. That fact alone does not guarantee foreground-equivalent execution, network continuity, or immunity from every kill reason.

## Architecture rule

The authoritative ChatGPT response/stream state remains in the normal production response/conversation owner established by `DEV-send-stream`.

Background support must **not** create a second stream, second conversation store, second message owner or server-side credential authority.

### Multiple active responses

Future multi-conversation streaming must be treated as a **set of independently owned responses**, not one global `isStreaming` flag.

When the app backgrounds:

- protect every response that is already legitimately active and eligible for background continuation;
- one app-level background assertion/elevated-preservation mechanism may cover the process, but its lifetime is derived from the protected response set;
- A completing must not release background preservation while B is still active;
- release the app-level preservation only when the last protected response reaches a terminal state or the user disables/stops background waiting;
- no duplicate request/stream may be created merely to represent the protected set.

Actual simultaneous A/B server-stream support remains Unknown / Unverified until `DEV-send-stream` proves it on-device.

If a privileged TrollStore helper is ultimately required:

- prefer a **small isolated helper** with only the private privileges proven necessary;
- keep ChatGPT authentication cookies/tokens/message bodies out of that helper;
- helper IPC should be limited to lifecycle/process-control facts such as the client process identity, enable/disable and status;
- helper must only control the intended ChatGPT client process/own accepted process identity, not become a generic arbitrary-PID privilege surface;
- do not grant the main ChatGPT client broad `no-sandbox` / platform entitlements merely because a reference project uses them;
- the main app should keep owning the actual authenticated network streams whenever feasible.

## Development ordering

Background continuation depends on a real production send/stream lifecycle, so it must not be implemented before `DEV-send-stream` establishes the real response owner and terminal states.

Recommended order:

1. `DEV-send-stream` — text send/new conversation + real streaming + stop + reasoning/final lifecycle.
2. `DEV-background-notify` — ordinary iOS background continuation + local completion notification + recovery integration over the active response set.
3. `DEV-trollstore-true-background` — isolated TrollStore-only experiment; promote only after real-device evidence.

The experimental task must not block a usable V0.2 daily-chat candidate.

## Work A — `DEV-background-notify`

### User-facing name

**后台等待与完成通知**

### Scope

- Request local-notification permission using normal `UNUserNotificationCenter` behavior.
- Add setting `后台等待回答完成` (planned default On).
- Add setting `回答完成时通知` (planned default On).
- When at least one owned response is active and the app enters background, use the normal iOS `beginBackgroundTask` continuation path.
- Continue the existing response lifecycles; do not create another request.
- Maintain the active protected-response set through real response terminal transitions.
- If one response finishes while other protected responses remain active:
  - commit that response through its normal owner;
  - optionally issue its deduplicated local completion notification;
  - keep the app-level background assertion alive for the remaining protected responses.
- When the last protected response reaches terminal state:
  - end the background task promptly.
- If the public background task expires first:
  - execute the required expiration cleanup once;
  - mark each still-active protected response as locally interrupted/needs explicit reconciliation according to the response owner;
  - do not resend/retry/regenerate;
  - on return, expose/use `同步最新消息` for the affected conversations.

### Notification ownership and deduplication

A completion notification belongs to one completed response lifecycle.

- emit at most one completion notification for the same response terminal transition;
- late duplicate callbacks, reloads, syncs or UI redraws must not emit the same notification again;
- if several background responses finish separately, each may produce one notification according to the user's notification preference;
- do not use notification count as response/conversation state authority.

### Notification privacy

Default notification should be concise (`回答已完成` plus an optional safe conversation title if accepted by the user). Do not put full prompts, answers, tokens or auth data into notification payload/content by default.

If notification-tap routing later opens the exact conversation, do not expose raw sensitive state in the visible notification content merely to route it. Exact private routing metadata/persistence should be designed with the normal app-private storage/privacy rules when implemented.

### Foreground hidden-conversation completion

If A completes while the app is foregrounded but the user is viewing B, system local-notification behavior is not the only UX mechanism.

Prefer the multi-conversation plan's derived sidebar completion/unseen state. Whether a hidden foreground response should also emit haptic feedback remains a UI/runtime tuning question; do not reuse the visible reasoning-to-final two-pulse haptic blindly without user acceptance.

### Diagnostics

Record safe events for:

- app foreground/background transition;
- active protected response count;
- ordinary background-task begin/end/expiration;
- response added/removed from the protected set;
- response terminal reason while backgrounded;
- local notification scheduled/display-requested and deduplication result;
- foreground resume and which conversation hashes require reconciliation.

Do not add heartbeat timers merely to manufacture activity.

## Work B — `DEV-trollstore-true-background`

### User-facing name

**TrollStore 真后台实验**

### Goal

Determine whether the current iOS 14–17 TrollStore environment can keep the **existing production response streams** running for long periods while the app is backgrounded/locked, with low idle overhead and without weakening the client's authentication/security model.

### Step 1 — source-level feasibility prototype

Use TrollSpeed/UIDaemon-derived source as reference, not as a drop-in patch.

Evaluate the smallest mechanism that can affect only this app/active-response lifecycle, in this preference order:

1. keep the main app process runnable/non-freezable using narrowly scoped entitlement/process controls;
2. if the main app cannot safely hold the needed privileges, use a minimal privileged helper that controls/asserts the main process but does **not** own ChatGPT credentials/network content;
3. only consider a detached long-running helper process if real evidence shows it is necessary.

Do not move the ChatGPT streams into a privileged helper merely for convenience.

### Step 2 — feature gating

Until real-device acceptance, expose any true-background mode only as an explicit experimental TrollStore-only setting, planned wording:

`TrollStore 真后台（实验）`

Default: **Off** until accepted.

If later proven stable and battery cost is acceptable, default behavior may be reconsidered from runtime evidence.

### Step 3 — active-response-set activation

Even if true background can run indefinitely, do not immortalize the app continuously.

Activate elevated/background-preservation state only when all are true:

- at least one real response is actively reasoning/streaming;
- the user has enabled background waiting / experimental mode as applicable;
- the app leaves the foreground.

Keep it active while the protected response set is non-empty.

Remove each response from the set when that response:

- commits its final answer;
- is stopped/cancelled by the user;
- terminates with an error;
- otherwise reaches an accepted terminal state.

Release elevated/background-preservation state when:

- the protected response set becomes empty;
- the user disables the mode;
- the app intentionally ends all owned streams.

An explicit user force-quit should be treated as a stop request rather than silently auto-relaunching/respawning the client, unless a later explicit requirement changes that behavior.

### Step 4 — real-device matrix

At minimum test on the accepted target iPhone / iOS 17.0 environment:

- one active response, screen on + app backgrounded;
- one active response, device locked;
- two simultaneous conversation responses if `DEV-send-stream` proves the server supports that concurrency;
- one of two responses completes while the other continues; background preservation must remain active;
- all protected responses complete; preservation releases promptly;
- Wi-Fi stable;
- Wi-Fi/cellular transition where the production stream semantics support it;
- multiple background durations including short and long runs (target observations around 5, 15, 30 and 60 minutes when a controlled test can keep work active);
- response completes while backgrounded -> local notification -> reopen -> exact final state;
- stop/cancel while foregrounded after a background interval;
- sync/reload recovery after an interrupted background stream;
- memory pressure / thermal / battery observations sufficient to reject obviously harmful behavior.

Do not claim `30分钟` or `1小时` support until the exact candidate survives those real-device tests.

### Step 5 — safety acceptance

Before promotion from Experimental, prove:

- no second authenticated stream/request is created;
- no copied auth secret is persisted or exposed to helper IPC;
- helper/process control cannot be trivially redirected to arbitrary unrelated processes;
- normal foreground/background transitions remain stable;
- true-background mode releases when the last protected response reaches terminal state;
- local notification fires at most once per completed response lifecycle;
- reopening/reloading a completed response does not replay completion notification/haptic;
- the feature does not materially break WebKit login/session handling;
- battery/thermal behavior is acceptable for the user's actual workload.

## Public iOS baseline remains mandatory

Even if TrollStore true background is later accepted, keep the ordinary `DEV-background-notify` path as a simpler baseline/diagnostic behavior. The true-background experiment must not hide or replace normal expiration evidence with silent retries.

## Non-goals / rejected shortcuts

- No fake configurable public-API guarantee such as `后台存活 30 分钟 / 1 小时`.
- No silent audio, fake location, or other unrelated background-mode abuse as the default solution.
- No automatic prompt resend or regenerate when background streaming breaks.
- No remote server that receives the user's ChatGPT cookies/tokens merely to provide completion notifications.
- No blanket copy of TrollSpeed's private entitlements into the main app without a dedicated proof of necessity.
- No claim that `巨魔真后台` uses TrollSpeed's mechanism until its own source is available and inspected.
- No global single-response background flag that can release preservation while another conversation is still actively generating.

## Handoff rule

When `DEV-send-stream` becomes Stable for an accepted streaming lifecycle, the next session may open `DEV-background-notify`. After that baseline is accepted, open `DEV-trollstore-true-background` as a separate isolated experiment/candidate. Each task must run the normal branch/checkpoint/candidate/conflict preflight before implementation.
