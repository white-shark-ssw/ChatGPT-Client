# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-30 through exact b52 Runtime and exact b53 Code/CI/Artifact/package verification._

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
8. Durable production policy still requires protected browser Send to remain explicitly user-visible; b48-b53 are isolated diagnostic exceptions requested by the user and do not silently change that policy.
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
- Native first/exclusive resume and required browser context remain Unknown / Unverified. Resume parity is not the active b48-b53 diagnostic path.

### b48-b53 Native-composer / Web-Send-engine diagnostic exception

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
- Turns 2/3 were complete and visibly incremental/effectively character-by-character.
- Accepted: contextual value-only continuation is real; Native incremental streaming is Runtime Confirmed for this diagnostic path on established turns. b50 is a partial Runtime pass because new-chat turn 1 truncated.

#### b51 — fresh-new-chat title-generation correction Runtime confirmed

Historical b40/b41 evidence established that fresh new-chat first Send emits `title_generation`. b51 changed only one rule: if assistant-text continuation is already active and a top-level event has `type == "title_generation"` with no `o`/`p`, forward that frame unchanged without clearing continuation and increment `titleGenerationWhileContinuationCount`.

Exact b51:

- Candidate `DEV-send-stream-0.1.0-b51`, exact product/config source `bd8f056cc4d13ea2f1ab178353d926d8e4d21992`, Artifact `9720327648`.
- Fresh first long answer: `nativeCharacters=11618`, `nativeDeltaCount=284`, `titleGenerationWhileContinuationCount=1`, terminal true, Web assistant text 0; user visually judged it complete.
- Accepted: b51 fixes the b50 fresh-new-chat missing-middle failure.

#### b52 — final-answer pass; reasoning gap isolated

Exact b52:

- Candidate `DEV-send-stream-0.1.0-b52`, exact product/config source `5c0690ce062e0fa3ff9bd253953842b99ecd2e0f`.
- Push Run / Job `33276080936` / `99162937523`; PR Run / Job `33276082767` / `99162942750` — success.
- Artifact `9721532867`; IPA SHA `a3de5c6eb4f7b790764fcd0adc4c98108fb550e7cedb3d6b02b931d266946b23`.

Exact Runtime:

- HTTP200 SSE / terminal true;
- `frameCount=74`, `nativeCharacters=614`, `nativeDeltaCount=26`;
- `exactTopLevelTextPatchCount=5`, `rootNonExactTextPatchCount=0`, `nestedTextPatchCount=6`;
- `contextualValueStringCount=15`, `inactiveValueStringCount=0`;
- `continuationResetWhileActiveCount=5`, `firstInactiveValueContext=none`, title-generation count 0;
- user reported **visible reasoning/thinking beginning slightly truncated, but final answer complete**.

Accepted: the remaining b52 failure is reasoning-specific. The prior root-nonexact→inactive-value hypothesis is rejected for this reproduction. Do not broaden final-answer parser grammar.

#### b53 — current Runtime Candidate, reasoning/tool structure only

Exact b53:

- Candidate `DEV-send-stream-0.1.0-b53`, version/build `0.1.0 (53)`.
- exact product/config source `3204b183ca4fe6310b48f13c067fbf993ca8d0f8`.
- Push Run / Job `33294541342` / `99211838094` — success.
- PR Run / Job `33294542985` / `99211842336` — success.
- Artifact `9726996570`; ZIP `sha256:8831bbae1c5cad9c9cd7f0ad9fbcf4846d709b27ae950b0391d436e20749b38c`.
- IPA SHA `d5eee722ea01dc2c1b419a803574aec8ad2199299a3d0bbb51de4bae574f25dc`.
- package identity `0.1.0 (53)` / Candidate b53 / source `3204b183ca4f` / Release / iOS14 / `[1,2]` / arm64.

b53 makes **no parser-output/UI correction**. It records at most 32 unique privacy-safe structural signatures before existing b52 parsing: frame index, event type, operation/path, structurally discoverable message role/content type/status/end-turn, bounded key names and nested patch operation/path summaries. It never logs prompt, answer, reasoning text, raw payload, raw IDs, auth/proof/header values or DOM reasoning state.

### Reasoning / tool presentation plan

This is part of `DEV-send-stream`, not a separate Work.

Planned product presentation after protocol evidence:

- explicitly user-visible reasoning becomes a distinct response phase/presentation from final answer;
- reasoning is collapsible/expandable in the Native conversation UI;
- user-visible tool activity may be tapped to open a native sheet/popover that shows service-provided tool status/details appropriate for the user;
- reasoning→final transition belongs to one authoritative response lifecycle and is recorded exactly once;
- hidden chain-of-thought, internal tool/system nodes or inferred private reasoning are never shown.

Exact message/event/content types and transition grammar remain Unknown until b53 Runtime identifies them. Do not implement these UI components from guessed event names.

### Current b53 human Runtime gate

One focused reproduction is sufficient:

1. install exact b53 and clear diagnostics;
2. open `Native 输入 / Web Send（b53诊断）`;
3. send a request that naturally produces visible reasoning plus tool activity, preferably the same GitHub/project-progress style request used for b52;
4. observe whether reasoning begins complete or truncated, whether final answer is complete, and whether visible tool activity occurs;
5. after terminal, export diagnostics.

The decision signal is the emitted `streamStructure` signatures. Only after these identify explicit service-visible reasoning/tool grammar may the next Candidate implement the minimal reasoning state/parser/presentation.

### Background ordering

Background resilience remains P0, but production implementation follows eventual response ownership.

- b45 proves positive short-background/original-stream survival and official recovery after forced interruption.
- b49 also showed a long diagnostic response reaching terminal across multiple background intervals.
- b48-b53 remain Web-owned diagnostic transport rather than accepted production response ownership.
- 5/15-minute, WebContent/process termination, network transitions and battery/thermal remain separate Runtime gates.

### Candidate sequencing

- b39-b53 identities are permanently reserved once emitted.
- Exact b53 product/config source is immutable after Artifact emission.
- Any product-code correction requires b54+ and must be justified by exact b53 Runtime; do not pre-allocate b54.

Detailed current Runtime records include:

- `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`
- `docs/project/runtime-evidence/DEV-send-stream-b46-runtime.md`
- `docs/project/runtime-evidence/DEV-send-stream-b47-runtime.md`
- `docs/project/runtime-evidence/DEV-send-stream-b49-runtime.md`
- `docs/project/runtime-evidence/DEV-send-stream-b50-runtime.md`
- `docs/project/runtime-evidence/DEV-send-stream-b51-runtime.md`
- `docs/project/runtime-evidence/DEV-send-stream-b52-runtime.md`

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

**Human Runtime Gate on exact b53.** Reproduce one reasoning/tool-active turn and export diagnostics. b53 is deliberately behavior-neutral. Do not merge PR #29, promote the diagnostic Web Send-engine architecture to production, implement reasoning/tool presentation, or allocate b54 until exact b53 Runtime identifies the service-visible reasoning/tool grammar.