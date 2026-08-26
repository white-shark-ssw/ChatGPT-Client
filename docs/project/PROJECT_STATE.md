# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone / iOS 17.0 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + one-detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`, version `0.1.0 (9)`: **merged Stable production native-read baseline for tested scope**. Product source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7`; run `32978476582`; artifact `9610449216`; IPA SHA-256 `16168a9db6f03e4ab00ddae4149451563a31fe2862cfb7ab18320329d186b99e`; PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`. Runtime acceptance covers native shell, production list, two distinct details, current-branch extraction and visible user/assistant rendering on iPhone / iOS 17.0. Stable is scoped, not Frozen.

b8 remains historical partial/failing evidence only; b9's two successful detail reads supersede any inference that the earlier one-off HTTP 500 represented a systematic current read failure.

## Current active candidate

`DEV-conversation-recovery-0.1.0-b10`, version `0.1.0 (10)`, is the active manual recovery candidate on `dev/conversation-recovery-20260826` / PR #10.

- Product/config source: `89129913cb29a35db9dec7a6d5670d1b3b76bc23`.
- Validation: **Code written + CI passed + Artifact produced**.
- CI run: `32982836557`.
- Artifact ID: `9612167843`.
- IPA: `ChatGPTClient-0.1.0-b10-dev-conversation-recovery.ipa`.
- IPA SHA-256: `6e600f829fa24cdeb705e9ab104ebb780a8c70dd06871285d06fa30521aecb7e`.
- GitHub ZIP digest: `sha256:5a4818f2ea10569092e4144630372d2fecc62a2fcc87d03010ad2116947d224c`.
- Package inspection: version `0.1.0`, build `10`, candidate `DEV-conversation-recovery-0.1.0-b10`, source `89129913cb29`, minimum OS `14.0`, arm64.
- Runtime/manual/real-device recovery behavior: **Unverified**. b9 remains the accepted production baseline until b10 is tested and accepted.

b10 keeps b9 auth/session/header/endpoint behavior unchanged. `ConversationRepository` remains the sole selected/detail/current-branch authority. It now owns explicit `同步最新消息` and `重载当前会话` operations. Sync preserves the previously loaded detail on failure and replaces it with fresh server-backed detail on success. Full reload clears the authoritative selected detail before a fresh request and rebuild. The conversation overflow exposes both actions; terminal `重新加载` uses the full-reload path. No automatic retry, watchdog, timer, resend or fallback path was added.

## Delivery direction

- **V0.1 read-use**: native shell + list/detail/message rendering + manual latest-message sync/current-conversation reload. b10 is the first Code+CI+Artifact candidate for the complete loop; real-device acceptance is pending.
- **V0.2 chat-use**: V0.1 + send/new conversation + streaming + stop + visible reasoning interaction + reasoning-to-final haptics + recovery integration.
- **V0.3 daily-use refinement**: Markdown export, long-conversation tuning, attachments and other daily-use features.

Small low-risk UX enhancements may be inserted between core phases only when dependencies are merged and conflict scanning is clean. `DEV-conversation-round-count` is planned after recovery and before send/stream.

## UI / interaction direction

`docs/project/UI_INTERACTION_BASELINE.md` remains authoritative.

- b9 accepted the first production sidebar/detail read shell on iPhone / iOS 17.0.
- b10 adds loaded-state overflow entries for `同步最新消息` and `重载当前会话`; terminal `重新加载` is the full-reload action. These are not runtime-accepted yet.
- Recovery remains explicit user action only; no automatic watchdog/retry/resend chain.
- Planned round-count UI uses `聊天 · N轮` / `工作 · N轮` when enabled, derived from current active-branch user turns without a second mutable counter or new request.
- Markdown export remains a project enhancement. Reasoning UI/haptics remain future send/stream work.

## Authentication evidence

Embedded Google login and default persistent `WKWebsiteDataStore` remain the accepted architecture. `AuthSessionStore` remains the in-memory account-context owner; copied WebKit cookies/session bearer are transient. b9 again required explicit login verification before production reads succeeded, so install/update persistence of usable authentication remains Unknown / Unverified. b10 does not change auth behavior.

## Conversation-read / recovery evidence

### Accepted b9 runtime

- After explicit login verification, production list returned HTTP 200, 28 items / total 29.
- Position 1 / hash `sha256:e95144bf259d`: 1,529,866 bytes, mapping 337, visible 154, 5,668.41 ms.
- Position 13 / hash `sha256:084c1f4870f3`: 7,503,328 bytes, mapping 2023, visible 843, 20,742.89 ms.
- Both were confirmed fully readable on device.

### b10 implementation/artifact evidence

- `同步最新消息` reuses current selected identity and the existing detail endpoint through `ConversationRepository`.
- `重载当前会话` clears selected authoritative detail first, then uses the same established detail/current-branch parse path to rebuild.
- Recovery spans record previous/current visible counts, added/removed/changed counts and local-state transitions while omitting raw conversation IDs and message bodies.
- CI run `32982836557` passed and artifact `9612167843` was produced; downloaded IPA SHA matched its generated sidecar.
- These facts prove Code/CI/Artifact only, not device behavior.

## Conversation round-count planned semantics

- Work ID: `DEV-conversation-round-count` / **会话轮数显示**.
- Display: `聊天 · N轮` / `工作 · N轮`; `显示会话轮数` defaults On and hides only the count when Off.
- One user message on the **current active branch** equals one round. Assistant/tool/system/reasoning nodes do not add rounds; Regenerate alone does not increment; branch changes recalculate from the selected branch.
- Count is derived from `ConversationRepository`/current active branch, not a separately persisted mutable counter.
- Schedule: after `DEV-conversation-recovery`, before `DEV-send-stream`, unless future conflict scanning proves another order safer.

## Current architecture

- `AppDelegate`: lifecycle/root setup.
- `RootViewController`: production split shell.
- `ConversationRepository`: conversation summaries, selected identity, loaded detail, current visible branch, latest-message sync and full selected-conversation reload semantics.
- `ConversationSidebarViewController`: list presentation plus settings/login/list reload entry points.
- `ConversationDetailViewController`: detail/message presentation and manual recovery UI; consumer of repository state.
- `AuthWebViewController`: login UI/navigation.
- Default `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: account context and short-lived authorized native transport.
- `ProtocolReadProbe`: diagnostic-only.

## Durable development plan

1. `DEV-app-foundation` — Completed / merged / Stable.
2. `DEV-auth-bootstrap` — Completed / merged / Stable.
3. `DEV-protocol-read` — Completed / merged / Stable for tested diagnostic read scope.
4. `DEV-native-read-path` — Completed / merged / Stable for tested b9 scope.
5. `DEV-conversation-recovery` — **Active b10 candidate; Code + CI + Artifact; runtime pending**.
6. `DEV-conversation-round-count` — planned serial UI/data-derived task after recovery.
7. `DEV-send-stream`.
8. `DEV-markdown-export`.
9. `DEV-long-conversation`.
10. `DEV-attachments`.
11. Daily-use conversation features.
12. Advanced capabilities.

Core state-owner work remains serialized; parallel edges require normal conflict scanning.

## Known issues / constraints

- No unit/UI test target; automated validation is Release compile, IPA packaging/inspection and artifact upload.
- Install/update auth persistence remains Unverified.
- b10 recovery interactions are not yet real-device tested.
- b9's large tested conversation took 20.74 s end-to-end; performance decomposition remains Unverified.
- Send, streaming, attachments, non-personal workspace behavior, lower iOS runtime and iPad runtime remain Unknown / Unverified.

## Evidence rule

Always distinguish Code written, checks/CI passed, Artifact produced, Runtime/manual/real-device tested, and Stable/Frozen acceptance. Current real-device evidence outranks historical assumptions.
