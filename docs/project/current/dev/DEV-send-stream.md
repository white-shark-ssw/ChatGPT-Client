# DEV-send-stream

## Status

**Active — b48 diagnostic experiment allocated. Long-term TD-024/TD-025 hidden/shadow-Web boundary is intentionally NOT changed yet. The user's latest explicit requirement authorizes one isolated Runtime experiment to determine whether a Native composer can drive the official Web Send machinery while assistant SSE text is intercepted before Web React/DOM rendering.**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / reasoning / follow-tail / 官方 Web / hybrid / realtime handoff / resume / stream / Native composer / Web Send engine`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; evidence branch only.
- **Current target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`.
- **Head before this checkpoint batch**: `ae39bbf6fc0aac893eb0427c7846f7f94991c8b2`.
- **Stable native predecessor**: b38.
- **Exact b47 product/config source**: `21028bbff7982abeb42f130c56fcb21e6ef44d7a`.
- **b47 Runtime Artifact**: `9716878034`; b47 remains immutable/reserved.
- **Allocated diagnostic Candidate**: `DEV-send-stream-0.1.0-b48`, version/build `0.1.0 (48)`.
- **Stable/Frozen Send**: No.

## Resume guard / conflict state

Current-session Light Resume Guard revalidated before b48 allocation:

- latest repository `AGENTS.md` and `docs/project/START_HERE.md` reread;
- selected task uniquely remains `DEV-send-stream`;
- branch exists and was at `ae39bbf6fc0aac893eb0427c7846f7f94991c8b2`;
- PR #29 is open / mergeable / not merged and points to this branch;
- `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c`;
- `docs/project/current/dev/` contains no other Active development checkpoint;
- repository search found no existing `DEV-send-stream-0.1.0-b48` / `b48` allocation;
- b47 exact product source has not been redefined by later docs-only work.

## Accepted prior evidence that constrains b48

1. Exact b42 proved ordinary ChatGPT consumer protected Send through `/backend-api/f/conversation` requires browser-owned anti-abuse challenge output on the tested account/device path. b48 does **not** solve/replay/harvest Sentinel, Turnstile, PoW or Conduit values.
2. Exact b40 established ordinary Send as HTTP200 SSE and text patch structure including append `/message/content/parts/0`, plus status/end-turn/metadata lifecycle patches.
3. Exact b45 established official no-resend `POST /backend-api/f/conversation/resume` with `{conversation_id, offset}` and HTTP200 SSE.
4. b46/b47 Native duplicated Cookie+Bearer-only resume returned HTTP404 after official Web had already resumed. Native first/exclusive resume remains Unknown.
5. Exact-device long-answer Web composer use failed badly enough before b47 testing that the user switched to a new conversation.
6. The user's earlier wrapped-Web/userscript experiment already showed that loading the full conversation then merely hiding all but about two visible rounds did not make the Web `+`/overall interaction acceptable.
7. Sub2API/Codex OAuth remains static research only; primary-account Runtime is blocked by the user's account-safety concern.

## Long-term boundary vs this diagnostic exception

The durable production rule still rejects hidden/shadow protected Web Send, Native DOM composer injection and synthetic hidden clicks. **Do not edit TD-024/TD-025/PROJECT_SPECIFIC_RULES merely because this experiment exists.**

The user's latest explicit decision is narrower: try one isolated version first, measure real-device behavior, and only reconsider the durable boundary if the result is good. Therefore b48 is evidence acquisition, not production acceptance.

b48 must not:

- copy/replay challenge/proof/Conduit/OAI header values;
- construct a Native `/f/conversation` protected Send;
- integrate streamed text into `ConversationRepository`;
- persist prompt/answer/reasoning text in diagnostics;
- add retry/timer/watchdog/fallback machinery;
- implement attachments;
- claim existing long-conversation performance is solved;
- change the durable hidden/shadow-Web decision before Runtime.

## b48 exact diagnostic scope

Build a separate diagnostic controller, initially **new-chat focused**, with:

- a full-size official `WKWebView` using the existing default persistent `WKWebsiteDataStore`, kept behind an opaque Native surface so Web layout still has normal iPhone dimensions;
- a Native text composer and Native Send button as the only normal user input surface;
- one document-start script that finds the official Web composer at runtime, transfers the current Native text into its real editable state and invokes the page's own submit path;
- the official page remains responsible for its own protected Send/challenge flow;
- a `window.fetch` wrapper on `/backend-api/f/conversation` that consumes the returned SSE before React, forwards raw assistant text deltas to Native **in memory only**, and removes evidenced append `/message/content/parts/0` text patch operations from the stream returned to Web while preserving the remaining structural lifecycle events and `[DONE]`;
- no `response.clone()` for the production-like interception path; use one stream transform/reader path so a non-consuming clone cannot accumulate long-answer buffers;
- privacy-safe structural diagnostics only: Send observed/accepted, frame counts, removed text-patch counts/character counts, terminal state, Web element/message-node counts and Native presentation counts; never log the text itself;
- no production state mutation.

The first Candidate does **not** yet virtualize an existing conversation-detail response before React. That is a later experiment only if b48 proves the Native composer + filtered-SSE state machine can survive at least two sequential turns.

## b48 Runtime questions

On the exact iPhone/iOS17 device, determine:

1. Can the user send from the Native composer without touching the Web composer?
2. Does official protected Send still succeed using the Web page's own machinery?
3. Does Native receive incremental assistant text while the corresponding assistant text patch is withheld from Web React?
4. Does the hidden Web message/element footprint stay small enough that a long answer does not create the previous assistant DOM growth?
5. After the first filtered response reaches terminal `[DONE]`, can a second Native-composer Send in the same Web session succeed without branch/parent/state failure?
6. Does ordinary typing/Send feel Native-smooth on the target device?

Passing b48 does **not** prove existing long-chat viability. It only unlocks a later existing-conversation data-virtualization experiment.

## Non-atomic GitHub write-chain recovery point

### Batch A — checkpoint / allocation

- allocate b48 identity and record diagnostic exception;
- completed by this checkpoint write.

### Batch B — non-CI assembly branch

Create a temporary assembly branch from the post-checkpoint head so intermediate product/config files cannot trigger the real `dev/send-stream-20260829` workflow. Assemble only the expected b48 files:

- `ChatGPTClient/Protocol/NativeWebSendEngineProbe.swift` — new diagnostic controller/script;
- `ChatGPTClient/SettingsViewController.swift` — point diagnostic entry to b48;
- `ChatGPTClient.xcodeproj/project.pbxproj` — add source + Build 48 / Candidate b48;
- `.github/workflows/ios-foundation.yml` — b48 Candidate/workflow/artifact identity.

No `ConversationFeature.swift`, `AuthSessionStore.swift`, `RootViewController.swift`, build scripts or stable b38 presentation code are expected to change.

### Batch C — assembly audit / publish

- compare assembly against the real development head;
- require exactly the expected files above;
- Light Guard real branch head immediately before publish;
- non-force fast-forward the complete assembly commit chain to `dev/send-stream-20260829` in one ref move.

### Batch D — CI / Artifact

- accept only CI whose head is the exact complete b48 product/config source;
- require both push/PR CI success where emitted;
- inspect the Push Artifact package identity independently;
- reserve/reject any identity-invalid intermediate Artifact if one somehow appears;
- hand exact IPA to user for Runtime.

### Batch E — docs after evidence milestone

Update Build/Test Index and PR/checkpoint with exact b48 CI/Artifact identity. Do **not** modify the durable production hidden-Web boundary until Runtime result justifies a separate architecture decision.

## Next exact action

Create the non-CI b48 assembly branch from the post-checkpoint head, implement only the four expected b48 product/config files, audit the assembly diff, fast-forward the real development branch, then autonomously continue through CI/package identity verification to the exact-device Runtime gate. Do not wait for an extra `继续` reply at ordinary milestones.