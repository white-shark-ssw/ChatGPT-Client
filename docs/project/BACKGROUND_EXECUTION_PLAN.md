# Background Execution / Completion Notification Plan

_Last updated: 2026-08-26._

## Purpose

Define how the TrollStore-installed native client should keep an in-progress ChatGPT response alive after the user backgrounds/locks the device and notify the user locally when the response completes.

This plan intentionally separates the **ordinary iOS-safe baseline** from a **TrollStore-only true-background experiment**. The experimental path must not block the first daily-chat candidate.

## Product goal

When a response is actively reasoning/streaming and the user leaves the app:

1. keep the existing response lifecycle/network stream running for as long as the accepted runtime mechanism permits;
2. if the response completes while the app is backgrounded, commit the final state through the normal conversation/response owner and show a local notification such as `回答已完成`;
3. if background execution stops before completion, never resend the prompt automatically; when the user returns, use the existing `同步最新消息` recovery path to reconcile with server state;
4. consume essentially no special background resources when no response is active.

There is **no product requirement for a fake 30-minute / 1-hour selector**. Public iOS APIs do not provide that guarantee. If a TrollStore true-background technique is accepted, the desired behavior is instead **response-scoped continuation**: enable only while an owned response is active, then release immediately on final/cancel/error.

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

This is **reference evidence that TrollStore-only long-running processes are technically possible**, not proof that the same technique can safely preserve this client's existing authenticated streaming connection.

Apple XNU documentation also confirms that process freezability is a distinct memorystatus property and that system components can opt processes out of freezing. That fact alone does not guarantee foreground-equivalent execution, network continuity, or immunity from every kill reason.

## Architecture rule

The authoritative ChatGPT response/stream state remains in the normal production response/conversation owner established by `DEV-send-stream`.

Background support must **not** create a second stream, second conversation store, second message owner or server-side credential authority.

If a privileged TrollStore helper is ultimately required:

- prefer a **small isolated helper** with only the private privileges proven necessary;
- keep ChatGPT authentication cookies/tokens/message bodies out of that helper;
- helper IPC should be limited to lifecycle/process-control facts such as PID, enable/disable and status;
- do not grant the main ChatGPT client broad `no-sandbox` / platform entitlements merely because a reference project uses them;
- the main app should keep owning the actual authenticated network stream whenever feasible.

## Development ordering

Background continuation depends on a real production send/stream lifecycle, so it must not be implemented before `DEV-send-stream` establishes the real response owner and terminal states.

Recommended order:

1. `DEV-send-stream` — text send/new conversation + real streaming + stop + reasoning/final lifecycle.
2. `DEV-background-notify` — ordinary iOS background continuation + local completion notification + recovery integration.
3. `DEV-trollstore-true-background` — isolated TrollStore-only experiment; promote only after real-device evidence.

The experimental task must not block a usable V0.2 daily-chat candidate.

## Work A — `DEV-background-notify`

### User-facing name

**后台等待与完成通知**

### Scope

- Request local-notification permission using normal `UNUserNotificationCenter` behavior.
- Add setting `后台等待回答完成` (planned default On).
- Add setting `回答完成时通知` (planned default On).
- When an owned response is active and the app enters background, use the normal iOS `beginBackgroundTask` continuation path.
- Continue the existing response lifecycle; do not create another request.
- If final answer arrives while backgrounded:
  - commit through the normal response/conversation owner;
  - end the background task;
  - issue a local completion notification.
- If the public background task expires first:
  - execute the required expiration cleanup;
  - do not resend/retry/regenerate;
  - preserve enough local response identity/state for foreground recovery;
  - on return, expose/use `同步最新消息` as the explicit reconciliation path.

### Notification privacy

Default notification should be concise (`回答已完成` plus an optional safe conversation title if accepted by the user). Do not put full prompts, answers, tokens or auth data into notification payload/content by default.

### Diagnostics

Record safe events for:

- app foreground/background transition;
- active response present/absent;
- ordinary background-task begin/end/expiration;
- response terminal reason while backgrounded;
- local notification scheduled/display-requested;
- foreground resume and whether reconciliation was required.

Do not add heartbeat timers merely to manufacture activity.

## Work B — `DEV-trollstore-true-background`

### User-facing name

**TrollStore 真后台实验**

### Goal

Determine whether the current iOS 14–17 TrollStore environment can keep the **existing production response stream** running for long periods while the app is backgrounded/locked, with low idle overhead and without weakening the client's authentication/security model.

### Step 1 — source-level feasibility prototype

Use TrollSpeed/UIDaemon-derived source as reference, not as a drop-in patch.

Evaluate the smallest mechanism that can affect only this app/response lifecycle, in this preference order:

1. keep the main app process runnable/non-freezable using narrowly scoped entitlement/process controls;
2. if the main app cannot safely hold the needed privileges, use a minimal privileged helper that controls/asserts the main process but does **not** own ChatGPT credentials/network content;
3. only consider a detached long-running helper process if real evidence shows it is necessary.

Do not move the ChatGPT stream into a privileged helper merely for convenience.

### Step 2 — feature gating

Until real-device acceptance, expose any true-background mode only as an explicit experimental TrollStore-only setting, planned wording:

`TrollStore 真后台（实验）`

Default: **Off** until accepted.

If later proven stable and battery cost is acceptable, default behavior may be reconsidered from runtime evidence.

### Step 3 — response-scoped activation

Even if true background can run indefinitely, do not immortalize the app continuously.

Activate elevated/background-preservation state only when all are true:

- a real response is actively reasoning/streaming;
- the user has enabled background waiting / experimental mode as applicable;
- the app leaves the foreground.

Release immediately when:

- final answer is committed;
- user stops/cancels;
- response terminates with an error;
- user disables the mode;
- the app intentionally ends the owned stream.

An explicit user force-quit should be treated as a stop request rather than silently auto-relaunching/respawning the client, unless a later explicit requirement changes that behavior.

### Step 4 — real-device matrix

At minimum test on the accepted target iPhone / iOS 17.0 environment:

- screen on + app backgrounded;
- device locked;
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
- normal foreground/background transitions remain stable;
- true-background mode releases after response terminal state;
- local notification fires only once per completed response lifecycle;
- reopening/reloading a completed response does not replay completion notification/haptic;
- the feature does not materially break WebKit login/session handling;
- battery/thermal behavior is acceptable for the user's actual workload.

## Public iOS baseline remains mandatory

Even if TrollStore true background is later accepted, keep the ordinary `DEV-background-notify` path as a simpler fallback/diagnostic baseline. The true-background experiment must not hide or replace normal expiration evidence with silent retries.

## Non-goals / rejected shortcuts

- No fake configurable public-API guarantee such as `后台存活 30 分钟 / 1 小时`.
- No silent audio, fake location, or other unrelated background-mode abuse as the default solution.
- No automatic prompt resend or regenerate when background streaming breaks.
- No remote server that receives the user's ChatGPT cookies/tokens merely to provide completion notifications.
- No blanket copy of TrollSpeed's private entitlements into the main app without a dedicated proof of necessity.
- No claim that `巨魔真后台` uses TrollSpeed's mechanism until its own source is available and inspected.

## Handoff rule

When `DEV-send-stream` becomes Stable for an accepted streaming lifecycle, the next session may open `DEV-background-notify`. After that baseline is accepted, open `DEV-trollstore-true-background` as a separate isolated experiment/candidate. Each task must run the normal branch/checkpoint/candidate/conflict preflight before implementation.
