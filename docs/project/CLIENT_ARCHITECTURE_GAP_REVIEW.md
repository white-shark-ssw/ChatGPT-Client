# Client Architecture Gap Review

_Last reviewed: 2026-08-27._

## Purpose

This is a focused pre-send/stream architecture review for the native TrollStore ChatGPT client. It records missing invariants discovered after the native-read, manual-recovery, multi-conversation and background-execution planning work.

The goal is **not** to add every future feature before the client becomes usable. The goal is to prevent a small number of structural mistakes that would otherwise force expensive rework once multiple conversations, streaming, background execution and long conversations are active at the same time.

## Current evidence baseline

Verified current facts relevant to this review:

- `DEV-native-read-path-0.1.0-b9` is the accepted production read baseline for the tested iPhone / iOS 17.0 scope.
- `ConversationRepository` is the production conversation owner.
- Current main source has one foreground `selectedConversationID` and one loaded `selectedConversation` slot.
- Current detail parsing walks `mapping` from `current_node`, derives visible user/assistant messages, then stores only the simplified `ConversationDetail`/message projection. `current_node` and graph relationships are not retained in the resident result.
- Current list request is `offset=0&limit=28&order=updated`; b7/b9 evidence already showed total count can exceed the returned 28.
- b9 repeatedly started with 0 total / 0 matched WebKit cookies until an explicit real WKWebView login/account-verification flow hydrated the default WebKit store.
- `SettingsViewController` currently has diagnostic/build controls but no accepted centralized preference/state owner for new feature toggles.
- There is currently no unit/UI test target.
- Active PR #10 owns manual recovery product changes and overlapping development/status/build documents; this review intentionally does not modify that work.

## Priority classification

### P0 — must be structurally resolved before production send/stream becomes authoritative

These items are small enough to address now and expensive/dangerous to retrofit later.

1. **Per-conversation resident state instead of one loaded slot.**
2. **Async operation freshness / stale-result protection.**
3. **Retain authoritative conversation/node identity needed by later send/branch operations.**
4. **Scope resident state to the verified account/workspace context and purge it on account/logout change.**
5. **Define new-conversation identity handoff before first production send.**
6. **Define per-conversation response ownership and multi-conversation concurrency before streaming.**
7. **Define sync/reload behavior when the target conversation has an active response.**
8. **Resolve cold-start authentication resume sufficiently for daily use without creating a second auth-secret owner.**

### P1 — should be delivered around the first daily-chat candidates

These materially improve daily use but should not block the first protocol/send proof.

1. **Basic Markdown/code-block message rendering path.**
2. **Conversation-list pagination / load-more beyond the current 28-item page.**
3. **Per-conversation draft and scroll-position restoration while the process remains alive.**
4. **Hidden-conversation generation/completion status in the sidebar.**
5. **One centralized app-settings preference owner for round-count/background/notification/experimental toggles.**
6. **Background completion with multiple active responses handled as an active set, not a single global boolean.**
7. **Phase timing for large conversation load: network / parse-model / first-visible-render.**

### P2 — useful after the daily-chat loop is stable

1. Optional persisted state across process death beyond normal WebKit auth persistence.
2. Persistent chat-body/disk caching, only if a later explicit privacy/storage requirement justifies it.
3. Advanced branch/edit/regenerate cache optimization.
4. Advanced unread/history synchronization with other clients.
5. Broad iPad/lower-iOS optimization after exact runtime testing.

## P0 findings and required invariants

### 1. Per-conversation resident state

Already planned in `MULTI_CONVERSATION_STATE_PLAN.md`.

Invariant:

> Foreground selection is presentation state. It must not destroy another conversation's loaded model or owned response.

Conceptually:

`account/workspace context + conversation ID -> resident conversation state`

Do not implement one authoritative repository per screen. Keep one production conversation authority with per-conversation entries.

### 2. Async freshness / stale-result protection

The multi-conversation change removes the current `selection_changed` discard, but that alone is insufficient.

Example race:

1. A is loaded and later starts streaming.
2. User invokes `同步最新消息` for A.
3. Stream advances locally.
4. An older detail/sync response returns afterward.
5. A blind replacement could regress A to an older server/local snapshot.

Similar races exist between:

- ordinary load vs explicit reload;
- old reload vs newer reload;
- list/detail request completion vs newer state;
- sync vs current streaming update;
- stop/cancel vs late stream callback;
- account change vs old request completion.

Required direction:

- each async operation is bound to its target account/context + conversation identity;
- per-conversation load/reload generations or another single-owner freshness mechanism prevents an older operation from blindly overwriting a newer authoritative state;
- selection change alone is not a discard reason;
- request generation/versioning is not a second state authority; it is only an ownership/freshness guard around the authoritative resident entry;
- duplicate requests for the same missing detail should be coalesced where the current owner can do so cleanly instead of issuing parallel equivalent loads.

Do not add arbitrary timers or generic retry loops to solve this.

### 3. Preserve node/current-branch identity

The current read model retains visible `message.id`, role, text and create time but does not retain the detail's authoritative `current_node` after parsing.

Before production send/stream, the resident conversation model must retain the **minimum current evidence-backed identity needed by the send protocol**, likely including current-node/parent/message identity once the send protocol probe proves the exact required fields.

Rules:

- do not re-fetch a conversation only because the model threw away an identity that the same accepted detail response already supplied;
- do not retain the raw multi-megabyte JSON payload merely for convenience;
- normalize only the node/branch metadata proven necessary;
- keep the user-visible message list a derived projection, not the only authoritative conversation representation.

This also avoids painting future Edit/Regenerate/branch work into a corner.

### 4. Account/workspace scoping and purge

Multi-conversation residency introduces an account-isolation requirement.

Resident conversation state, drafts, response owners and any future local status must never survive an explicit account identity change as though the same account still owned them.

Required behavior:

- bind the resident working set to the verified account/workspace context;
- explicit logout/account switch invalidates the transient native session and clears resident conversation/message/draft/response state belonging to the old context;
- late callbacks from the old context must be rejected even if a conversation ID string happens to match;
- never show old-account resident content under a newly verified account.

This is an in-memory safety boundary. It does not require persistent credential storage.

### 5. New-conversation identity handoff

The existing architecture only loads server-created conversation IDs. Send/new-chat will introduce a period where the UI has a composing/pending chat before the authoritative server conversation identity is known.

Before implementation, the send protocol probe must establish:

- whether a client-generated conversation ID is sent or a server ID is returned later;
- parent/current-node identity requirements;
- request/message IDs and their lifecycle;
- when the new conversation becomes safe to insert into the production list/resident map.

Implementation rule:

- a temporary local presentation identity, if required, must have one explicit handoff to the authoritative server conversation identity;
- do not let both temporary and server IDs remain independent state owners;
- rapid double-send must not accidentally create duplicate conversations/messages while the first identity handoff is unresolved.

### 6. Per-conversation response ownership and concurrency

The product requirement is stronger than fast navigation:

- A may be reasoning/streaming;
- user opens B;
- A keeps running;
- if current service/protocol evidence allows B to start its own response, A and B must have independent response owners.

Required design:

`conversation identity + response/message identity -> response lifecycle`

Do not use a global `isStreaming` or whichever conversation is visible as the response owner.

Initial concurrency policy:

- one active response per conversation is the safe product assumption unless current protocol/runtime evidence explicitly proves overlapping responses within the same conversation are valid;
- multiple conversations should be architecturally independent, but the actual number of simultaneous server streams is **Unknown / Unverified** until tested;
- do not hard-code an arbitrary global concurrency limit without evidence;
- Stop targets the exact owning response/conversation, never all conversations.

### 7. Sync/reload while a response is active

This needs explicit semantics because recovery is intended for stalled streams.

#### Sync latest

- targets one conversation;
- does not resend;
- may request server detail while a local response owner still exists;
- reconciliation must not regress newer local state;
- if server evidence proves the response is already complete, the local stale response lifecycle can transition to the server-backed terminal state and must ignore later obsolete callbacks;
- if server still shows an in-progress state, keep the owned response unless current protocol evidence gives a terminal reason.

#### Full reload

Reload is deliberately stronger.

- targets one conversation only;
- user explicitly asks to rebuild that conversation from server state;
- if an active local response exists, implementation must define one clear owner transition so the old stream cannot later resurrect/overwrite the reloaded state;
- no prompt resend/regenerate is implied;
- B/C resident conversations remain untouched.

Exact stream-cancel/detach behavior must follow the actual send/stream protocol evidence rather than being guessed now.

### 8. Cold-start auth resume

Current b9 evidence shows a daily-use problem: a fresh launch may observe an empty default WebKit cookie store until a real WKWebView is opened/hydrated.

Create a separate future Work:

`DEV-auth-resume` — **冷启动登录态恢复**

First experiment should follow the evidence already recorded by PR #10:

- test background/default `WKWebsiteDataStore.default()` warm-up/website-data access first;
- preserve WebKit as the sole persistent auth-secret authority;
- no hidden/shadow login WebView as a speculative permanent workaround;
- no copied-token persistence;
- if background warm-up is insufficient, capture exact evidence before choosing the smallest visible verification flow.

This Work is a good candidate to run in parallel with conversation-model work **only after a normal branch/file/state-owner conflict scan proves isolation**.

## P1 findings

### 9. Basic Markdown/code rendering is not a separate current roadmap Work

The UI baseline expects native Markdown, headings/lists/links, code blocks and tables, while the current production read model primarily renders visible text.

Do not block the first send protocol proof on a perfect renderer, but schedule a dedicated small Work around the first daily-chat candidate:

`DEV-message-rendering` — **Markdown 与代码块渲染**

First scope should prioritize development-chat usefulness:

- paragraphs/headings/lists;
- inline/fenced code;
- code-copy action;
- links;
- table handling when current content requires it;
- text selection/copy where UIKit implementation permits cleanly.

Streaming performance rule: do not broad-reload/reparse the whole long conversation for every token. Optimize only from measured behavior.

### 10. Conversation-list pagination

Current accepted list transport returns at most 28 items and has already reported a larger `total`.

Create a small Work once recovery/multi-conversation repository ownership is stable:

`DEV-conversation-pagination` — **会话列表加载更多**

Rules:

- preserve conversation identity while pages/reordering change;
- deduplicate by authoritative conversation ID;
- pagination/list refresh never clears resident detail merely because an item changes list position;
- exact cursor/offset behavior must use current protocol evidence;
- Search remains a separate later feature.

This should not block the first send/stream candidate if the user's currently needed conversations are reachable, but it should not be forgotten because multi-session development will quickly exceed one page.

### 11. Per-conversation draft and scroll state

Within the live process, A/B switching should also preserve lightweight presentation state:

- unsent composer draft;
- scroll anchor / last visible message identity;
- reasoning-detail expand/collapse state where useful.

Use a semantic message/anchor identity rather than only a raw pixel offset when long content can grow above/below it.

Do not persist chat drafts/bodies to disk merely because in-memory residency exists. Cross-process draft persistence requires its own explicit privacy/storage decision.

### 12. Hidden-conversation generation/completion status

Once multiple responses are possible, the sidebar should help the user understand what hidden conversations are doing.

Planned derived UI state, after send/stream exists:

- generating/thinking indicator for a hidden conversation with an active response;
- completed/unseen marker when a hidden response reaches final state;
- marker clears when that conversation is viewed according to the accepted UI behavior.

This is local presentation state, not a claim about an OpenAI server-side unread API.

Do not let sidebar status become a second response authority.

### 13. Central settings owner

Confirmed/planned settings now include at least:

- `显示会话轮数`;
- `后台等待回答完成`;
- `回答完成时通知`;
- future `TrollStore 真后台（实验）`;
- later appearance/diagnostic refinements.

Current `SettingsViewController` has no accepted preference-state owner.

When the first real toggle is implemented, establish one small app-settings owner around `UserDefaults`/system state instead of scattering independent keys and defaults through view controllers.

Rules:

- settings UI is a consumer;
- notification authorization remains owned by iOS/`UNUserNotificationCenter`, while the app setting expresses user preference;
- exact Swift type/key names are not frozen by this plan.

### 14. Multi-response background semantics

`BACKGROUND_EXECUTION_PLAN.md` originally describes a response-scoped path mostly in singular terms. With multi-conversation streaming, background protection must operate over an **active protected response set**.

Required semantics:

- if A and B are both active when the app backgrounds, background/true-background preservation stays enabled while at least one protected response remains active;
- A finishing must not release protection if B is still active;
- completion notification is deduplicated per response lifecycle;
- releasing the last protected response ends the background assertion/elevated preservation state;
- no response is duplicated just to maintain the background set.

### 15. Large-conversation phase timing

b9 measured 20.74 s end-to-end for a 7.50 MB / 2023-node conversation, but current evidence does not separate transfer, JSON parsing/model construction and first visible render.

Before major performance rewrites, add safe phase timing around:

- response bytes received;
- JSON parse / branch-model construction;
- first visible message presentation;
- later Markdown/layout time where relevant.

This is evidence collection, not a reason to prematurely add caching/retries/background parsing abstractions.

## Additional correctness gaps to keep visible

### Conversation freshness while resident

A resident conversation can become stale because another client/device changes it.

The existing list already provides `update_time`.

Potential future direction, only when implementation evidence supports it:

- if a refreshed list shows a newer server update time than the resident detail's known baseline, mark that entry as potentially stale;
- do not silently reload it merely because the list changed;
- `同步最新消息` remains the explicit reconciliation action unless a later product rule accepts automatic freshness behavior.

### `聊天` / `工作` type derivation

The user confirmed two visible official-App types/modes, but the current production read model does not yet have an accepted protocol contract for deriving a per-conversation `聊天` vs `工作` value.

Therefore:

- do not fabricate the type from title/UI text;
- if the current UI temporarily uses a known static type, record that implementation honestly;
- before authoritative dynamic type display, capture the actual current service field/context that differentiates the two.

### Process death / app relaunch

In-memory resident conversation state naturally disappears if iOS terminates the process or the user force-quits.

That is acceptable for the early client.

Do not introduce a persistent chat-body cache simply to make relaunch instant. If later requested, define:

- storage owner;
- encryption/file-protection expectation;
- eviction/size;
- logout/account-switch purge;
- schema/version migration;
- privacy/export behavior.

### Network transition / rate-limit behavior

Keep explicit failures observable.

- no speculative reachability-driven resend;
- no automatic duplicate stream after Wi-Fi/cellular transition;
- HTTP/auth/rate-limit errors should become clear terminal states according to actual protocol evidence;
- manual sync/reload remains the accepted recovery mechanism unless new evidence justifies more.

## Testing gap

There is no test target today. Once the conversation state/stream parser becomes more complex, pure deterministic logic should stop depending only on real-device manual tests.

Do not create a large testing framework project before it is useful. The first XCTest target should focus on logic that has real regression risk and no network dependency, such as:

- current-branch extraction / node identity normalization;
- round-count derivation;
- per-conversation resident lookup/eviction policy;
- stale async-operation generation guard;
- response lifecycle reducer/terminal transition once send/stream exists;
- stream parser once the actual event format is captured;
- Markdown export transformation later.

Real-device testing remains mandatory for WebKit auth, networking, haptics, background execution, TrollStore behavior and performance acceptance.

## Revised sequencing recommendation

The active recovery Work remains first and is not modified by this review.

After it merges, use this order unless a fresh conflict scan gives a better isolated parallel path:

1. `DEV-conversation-recovery` — finish current b11 validation/merge.
2. `DEV-multi-conversation-state` — include resident entries, async freshness, account scoping and retention of minimum authoritative node identity.
3. `DEV-auth-resume` — cold-start login-state recovery; may run in parallel with #2 only if branch/file/state-owner overlap is clean.
4. `DEV-conversation-round-count` — small derived UI setting; establish the first centralized settings owner if one still does not exist.
5. `DEV-send-stream` — establish actual send/new-conversation/response/stream protocol and per-conversation response lifecycle; test whether concurrent A/B streams are actually supported.
6. Issue the earliest practical chat-use Candidate immediately when send/stream works; do not wait for every P1 item.
7. `DEV-message-rendering` — basic Markdown/code usability.
8. `DEV-conversation-pagination` — load more than one conversation page.
9. `DEV-background-notify` — ordinary background continuation/local completion notification over the active response set.
10. `DEV-trollstore-true-background` — isolated true-background experiment.
11. `DEV-markdown-export`.
12. `DEV-long-conversation`.
13. `DEV-attachments` and later daily/advanced features.

The exact ordering of #7–#10 may be parallelized only after the send/stream owner is merged/stable and normal conflict scanning confirms they do not compete for the same core files/state owner.

## Acceptance mindset

The project should continue producing small TrollStore candidates. A planning item only blocks the next candidate when it protects a core invariant that would otherwise make that candidate unsafe or cause immediate rework.

Do not wait for this whole document to be implemented before using the app.
