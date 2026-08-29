# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-30 through exact b51 Runtime and exact b52 Code/CI/Artifact/package verification._

## Purpose

Durable implementation sequence for the native iOS ChatGPT client. Current real source, exact CI/Artifact evidence, real-device evidence and the user's latest explicit requirements outrank stale plan wording.

Core constraints: UIKit native shell/read client, TrollStore IPA, primary tested runtime iPhone 15 Pro Max / iOS17.0, deployment target iOS14, and private/internal ChatGPT behavior must be evidenced rather than guessed.

## Delivery principles

1. Reach a genuinely usable client early; do not wait for roadmap breadth.
2. Keep one authoritative owner per identity/state domain.
3. Prefer official ChatGPT iOS interaction patterns where architecture permits.
4. Do not add speculative retry/fallback/timer/watchdog/duplicate-state machinery.
5. Distinguish Code / Static / CI / Artifact / Runtime / Stable evidence.
6. High-frequency daily-use interactions such as Copy, attachments and reliable background reasoning/stream continuation outrank low-value polish once dependencies exist.
7. Optimize only evidenced bottlenecks, especially for long conversations.
8. Durable production policy still requires protected browser Send to remain explicitly user-visible; b48-b52 are isolated diagnostic exceptions requested by the user and do not silently change that policy.
9. A token/event/header name is not an implementation contract by itself.
10. A protocol path that works but depends on an unusable product surface is not an accepted production architecture.

## Accepted merged foundation

- Phase 1 `DEV-app-foundation`: merged Stable.
- Phase 2 `DEV-auth-bootstrap`: merged Stable for recorded scope.
- Phase 3 `DEV-protocol-read`: merged accepted diagnostic read evidence.
- Phase 4 `DEV-native-read-path`: merged Stable b9; `ConversationRepository` is native conversation authority.
- Phase 5 `DEV-conversation-recovery`: merged Stable b15.
- Phase 6 `DEV-multi-conversation-state`: merged Stable b21 for recorded read-state scope; Frozen No.
- Phase 7 `DEV-conversation-list-cache-core`: merged Stable b23; Frozen No.
- **Phase 8 `DEV-conversation-round-count`: merged Stable b38; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`; Frozen No.**

## Stable Phase 8 native baseline

Exact b38: Candidate `DEV-conversation-round-count-0.1.0-b38`, source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`, Runtime Artifact `9708425762`, IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.

Retain native list/detail/recovery ownership, per-conversation resident state, Copy/timestamps/preferences/round count, bounded long-message chunks, deterministic row geometry/manual cell layout, and continuous O(1)-target round navigation. Do not replace this baseline merely to accommodate Web Send.

## Phase 9 — `DEV-send-stream` — Active diagnostic architecture experiment

### Accepted protected-Send boundary

- b40-b41 established the current official-Web Send SSE shape and server Stop structure.
- Exact b42 proved PoW, Turnstile and `so` are required before successful ChatGPT-account protected Send. Pure-native/transient-auth account Send remains blocked.
- The user rejects the separately authenticated/billed API-product architecture and has blocked primary-account Sub2API/Codex-subscription Runtime because of account-safety concern.
- Hidden/shadow Web Send, challenge replay/bypass and Native DOM/input automation remain rejected as **production** architecture under current TD-024/TD-025.

### Full-Web product ceiling

- b43 proved a resident visible official-Web surface could be sufficiently smooth for a shorter tested sequence on iPhone/iOS17; Web `+` ~100–200ms; Web Photos filtered videos.
- b44 proved tested `/c/<id>` mapping but exposed a full-page Native -> Web -> Native architecture ceiling: immediate Native reconciliation can lag Web output, and the user rejected duplicated full-page Web interaction.
- b47 exact-device preparation exposed a stronger pre-Send ceiling: an older conversation with only about three rounds but long answers repeatedly froze when trying to bring up/use the mobile-Web composer.
- The user's earlier wrapped-Web/userscript experiment independently showed that loading the full conversation and hiding all but roughly two visible rounds still left `+`/overall interaction too slow.
- Therefore full existing-conversation Web rendering before every protected Send remains rejected as the production daily-chat dependency.

### Official no-resend continuation evidence

Exact b45:

- Candidate `DEV-send-stream-0.1.0-b45`, source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`, Artifact `9713774868`.
- Forced network interruption proved official `POST /backend-api/f/conversation/resume` with JSON body `{conversation_id: string, offset: number}`.
- Successful official resume returns HTTP200 `text/event-stream` and can continue the already-started response to terminal without another Send.
- b45 also provides positive ordinary short-background/original-stream survival evidence including ~126s continuous background/lock.

### Native duplicated resume evidence

- b46 exact source `4ab9be3ef2809204e88fcb0d44884e35b43726b1`, Artifact `9715903443`: official offset 18 resume HTTP200 SSE; Native same-body Cookie+Bearer-only duplicate HTTP404 JSON; later official offset 54 HTTP200 SSE.
- b47 exact source `21028bbff7982abeb42f130c56fcb21e6ef44d7a`, Artifact `9716878034`: official offset 23 HTTP200 SSE; one Native duplicate HTTP404 JSON / ~707ms / 116 bytes / 0 SSE; later official offset 74 HTTP200 SSE.
- Native first/exclusive resume and required browser context remain Unknown / Unverified. Resume parity is not the active b48-b52 diagnostic path.

### b48-b52 Native-composer / Web-Send-engine diagnostic exception

The user explicitly asked to try a Native UI over a minimal Web protected-Send engine **without changing TD-024/TD-025 first**. This is a diagnostic architecture experiment only.

Target diagnostic dataflow:

`Native composer -> page-owned official protected Send -> intercept Send SSE before Web React -> Native incremental answer memory/UI -> return lifecycle/identity frames to Web`

The official page remains responsible for login, browser challenges and Send construction. Diagnostic code does not copy/replay challenge values and does not mutate production `ConversationRepository`.

#### b48

- exact source `6ccba03cefaa32a1186f1f468c3e696ed9457699`, Artifact `9718885751`.
- Runtime: two sequential Native submissions successfully drove official protected Send and preserved enough Web conversation state for a second turn.
- Assistant text interception failed because parser used long-form `op/path/value` instead of compact `o/p/v`; Web received the answer. Superseded.

#### b49

- exact source `20fb8f3f400200965acb868aeb8a7504b9bfb91f`, Artifact `9719418761`.
- Runtime: real incremental Native delivery confirmed for explicit compact `o/p/v` text patches, but only short fragments were captured.
- Historical b40 evidence identified contextual value-only `{v:string}` continuation as the missing middle. Superseded.

#### b50

- exact source `837d5feeff05d198785f884ccf9cc4c1f71412ec`, Artifact `9719942650`.
- Runtime: three sequential Native-composer turns all reached official protected Send and terminal.
- Fresh first turn remained incomplete: 35 Native characters across 3 deltas; user reported a long answer with a missing middle.
- Turn 2: 191 Native characters / 10 deltas / 8 contextual value-only frames; user reported complete visible incremental output.
- Turn 3: 671 Native characters / 31 deltas / 29 contextual value-only frames; user reported complete incremental/effectively character-by-character output.
- Web assistant terminal text remained 45 characters on successful turns, materially smaller than Native output.
- Accepted: contextual value-only continuation is real; Native incremental streaming is Runtime Confirmed for this diagnostic path on established turns; sequential official protected Send is viable in the fresh session. b50 is a partial Runtime pass because new-chat turn 1 truncated.

#### b51 — fresh-new-chat title-generation correction Runtime confirmed

Historical b40/b41 evidence established that fresh new-chat first Send emits `title_generation`. b51 changed only one rule: if assistant-text continuation is already active and a top-level event has `type == "title_generation"` with no `o`/`p`, forward that frame unchanged without clearing continuation and increment `titleGenerationWhileContinuationCount`.

Exact b51:

- Candidate `DEV-send-stream-0.1.0-b51`, version/build `0.1.0 (51)`.
- exact product/config source `bd8f056cc4d13ea2f1ab178353d926d8e4d21992`.
- Push Run / Job `33271794573` / `99151433241`; PR Run / Job `33271796259` / `99151437702` — success.
- Artifact `9720327648`; IPA SHA `0aaa6317918314cc4cd89961dca534e932cc4c42de8bd1648279056818c45e51`.

Exact Runtime:

- fresh first long answer: `nativeCharacters=11618`, `nativeDeltaCount=284`, `contextualValueStringCount=282`, `titleGenerationWhileContinuationCount=1`, terminal true, Web assistant text 0; user visually judged it complete;
- second long answer: terminal true and visually complete;
- third GitHub/project-progress answer: terminal true, but user observed a small **leading truncation**; title-generation count 0.

Accepted: b51 fixes the b50 fresh-new-chat missing-middle failure. Complete parser coverage remains unaccepted because the third turn is a distinct leading-gap class.

#### b52 — current Runtime Candidate, diagnostics only

Exact b52:

- Candidate `DEV-send-stream-0.1.0-b52`, version/build `0.1.0 (52)`.
- exact product/config source `5c0690ce062e0fa3ff9bd253953842b99ecd2e0f`.
- Push Run / Job `33276080936` / `99162937523` — success.
- PR Run / Job `33276082767` / `99162942750` — success.
- Artifact `9721532867`; ZIP `sha256:2ffd7e46e80019d3c4e8d6cbfa5c91dffa2a5f88222a30d5c4d5fb1e4fd752fc`.
- IPA SHA `a3de5c6eb4f7b790764fcd0adc4c98108fb550e7cedb3d6b02b931d266946b23`.
- package identity `0.1.0 (52)` / Candidate b52 / source `5c0690ce062e` / Release / iOS14 / `[1,2]` / arm64.

Source evidence shows b51 activates contextual value-only continuation only after an exact top-level assistant append whose key set is exactly `o/p/v`. Other assistant text patches may be recursively scrubbed and delivered to Native without activating continuation. Existing b51 metrics cannot prove whether that explains the third-turn leading gap.

b52 therefore makes **no output/filtering correction**. It only adds structural aggregate counts for exact top-level patches, root non-exact patches, nested patches, inactive value-only strings, resets while active, and a bounded first inactive-gap context. It does not send inactive value-only strings to Native, preserve new frame classes, or alter the b51 title-generation rule.

### Current b52 human Runtime gate

One focused reproduction is sufficient:

1. install exact b52 and clear diagnostics;
2. open `Native 输入 / Web Send（b52诊断）`;
3. send a GitHub/tool-style request similar to the b51 third turn that showed a missing prefix;
4. observe whether the Native answer again starts truncated;
5. after terminal, export diagnostics.

The decision signal is the relationship between any reproduced leading gap and `exactTopLevelTextPatchCount`, `rootNonExactTextPatchCount`, `nestedTextPatchCount`, `inactiveValueStringCount`, `continuationResetWhileActiveCount`, and `firstInactiveValueContext`.

Do not broaden parser grammar until this evidence identifies the actual gap class.

### Background ordering

Background resilience remains P0, but production implementation follows eventual response ownership.

- b45 proves positive short-background/original-stream survival and official recovery after forced interruption.
- b49 also showed a long diagnostic response reaching terminal across multiple background intervals.
- b48-b52 remain Web-owned diagnostic transport rather than accepted production response ownership.
- 5/15-minute, WebContent/process termination, network transitions and battery/thermal remain separate Runtime gates.

### Candidate sequencing

- b39-b52 identities are permanently reserved once emitted.
- Exact b52 product/config source is immutable after Artifact emission.
- Any product-code correction requires b53+ and must be justified by exact b52 Runtime; do not pre-allocate b53.

Detailed current Runtime records include:

- `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`
- `docs/project/runtime-evidence/DEV-send-stream-b46-runtime.md`
- `docs/project/runtime-evidence/DEV-send-stream-b47-runtime.md`
- `docs/project/runtime-evidence/DEV-send-stream-b49-runtime.md`
- `docs/project/runtime-evidence/DEV-send-stream-b50-runtime.md`
- `docs/project/runtime-evidence/DEV-send-stream-b51-runtime.md`

## Phase 10 — `DEV-attachments` — high priority but Send-boundary dependent

Attachment daily-use priority remains high. Known boundaries:

- Web `+` ~100–200 ms was acceptable in b43's tested scope;
- iOS17 Web Photos chooser filtered videos;
- public `WKUIDelegate` upload-panel replacement is iOS18.4+, not iOS17;
- do not use private WebKit or DOM/file-input injection for production attachment selection;
- native iOS17 photo+video support requires an evidenced upload/handoff path;
- assistant file tap-download-share remains a core target before a full download manager.

Do not build native attachment upload until the accepted Send architecture defines attachment ownership.

## Phase 11 — `DEV-message-rendering`

Implement native Markdown/code/table/link/citation presentation only from authoritative user-visible content. Never expose hidden reasoning/tool/system content.

## Phase 12 — `DEV-conversation-list-preview`

Reuse the accepted list-cache owner/store. Do not issue one Detail per row merely to manufacture previews.

## Phase 13 — `DEV-markdown-export`

Export the authoritative current native user-visible branch; never scrape hybrid Web DOM.

## Phase 14 — `DEV-long-conversation`

Measure network / parse-model / first-visible-render / rich-layout timing and optimize only evidenced bottlenecks. Preserve Stable b38 deterministic native geometry unless new exact Runtime evidence justifies change.

The b47 long-conversation mobile-Web composer failure is a separate Phase 9 architecture issue; it does not reopen the accepted native b38 geometry baseline.

## Phase 15 — remaining daily-use features

Isolated Work IDs for download manager, pagination, background completion/notification, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat and settings/diagnostics refinement.

## Phase 16 — advanced capabilities

Projects, web search, image/multimodal generation, Voice, Memory, Deep Research, GPTs and other capabilities only with current protocol/UI evidence.

## Current next action

**Human Runtime Gate on exact b52.** Reproduce one GitHub/tool-style response that previously showed a leading gap and export diagnostics. b52 is deliberately behavior-neutral. Do not merge PR #29, promote the diagnostic Web Send-engine architecture to production, or allocate b53 until exact b52 Runtime identifies the actual structural gap class.