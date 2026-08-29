# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-29 through exact b47 Runtime and the long-conversation full-Web composer architecture gate._

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
8. ChatGPT-account browser Send, when used, must remain explicitly user-visible; never convert Web into hidden protected transport controlled by Native DOM automation.
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

## Phase 9 — `DEV-send-stream` — Active Human Architecture Gate

### Accepted protected-Send boundary

- b40-b41 established the current official-Web Send SSE shape and server Stop structure.
- Exact b42 proved PoW, Turnstile and `so` are required before successful ChatGPT-account protected Send. Pure-native/transient-auth account Send remains blocked.
- The user explicitly rejects the separately authenticated/billed API-product architecture.
- Hidden/shadow Web Send, challenge replay/bypass and Native DOM/input automation remain rejected.

### Visible-Web product evidence progression

- b43 proved a resident visible official-Web surface could be sufficiently smooth for a **shorter tested sequence** on iPhone/iOS17; Web `+` ~100–200ms; Web Photos filtered videos.
- b44 proved tested `/c/<id>` mapping but exposed a full-page Native -> Web -> Native architecture ceiling: immediate Native reconciliation can lag Web output, and the user rejected duplicated full-page Web interaction.
- b47 exact-device preparation exposed a stronger pre-Send ceiling: an older conversation with only about three rounds but long answers repeatedly froze when trying to bring up/use the mobile-Web composer, making that conversation unusable for testing. The user switched to a new conversation.
- The b47 export covers the replacement new-conversation run, so the internal freeze owner remains Unknown / Unverified. The product consequence is still direct: **full Web conversation rendering before every protected Send is no longer accepted as a production dependency.**

### Official no-resend continuation evidence

Exact b45:

- Candidate `DEV-send-stream-0.1.0-b45`, source `accd7bdf29e4d9bcbaad9c51ee18000bc89fe072`, Artifact `9713774868`.
- Forced network interruption proved official `POST /backend-api/f/conversation/resume` with JSON body `{conversation_id: string, offset: number}`.
- Successful official resume returns HTTP200 `text/event-stream` and can continue the already-started response to terminal without another Send.
- b45 also provides positive ordinary short-background/original-stream survival evidence including ~126s continuous background/lock.

### Native parity evidence

Exact b46:

- source `4ab9be3ef2809204e88fcb0d44884e35b43726b1`, Artifact `9715903443`.
- official offset 18 resume HTTP200 SSE;
- Native same-body Cookie+Bearer-only duplicated attempt HTTP404 JSON;
- later official offset 54 resume HTTP200 SSE.

Exact b47:

- Candidate `DEV-send-stream-0.1.0-b47`, source `21028bbff7982abeb42f130c56fcb21e6ef44d7a`.
- Push Run / Job `33259640112` / `99119258573`, PR Run / Job `33259642459` / `99119264902`, success.
- Artifact `9716878034`; ZIP `sha256:a6915d0a2c48877e8d4d5b7eea966118ad84b321bc1462dafe55c593796e10fc`; IPA SHA `49d1bd4886310f7761883784f73fc5532fe1a9532773619f0796cd7aab816909`.
- official offset 23 resume HTTP200 SSE after a transport-error retry;
- Native same-body duplicated request again HTTP404 `application/json`, ~707ms, 116 bytes, 0 SSE frames;
- rejection JSON shape `{"detail":{"code":"string","message":"string"}}`;
- later official offset 74 resume HTTP200 SSE.

Successful official request header names:

`accept, authorization, content-type, oai-client-build-number, oai-client-version, oai-device-id, oai-echo-logs, oai-language, oai-session-id, x-conduit-token, x-oai-is-client-observation, x-oai-is-pending-updates, x-oai-turn-trace-id, x-openai-target-path, x-openai-target-route`

Native explicitly sets only `accept, content-type`, plus the existing transient bearer injection and WebKit-derived ephemeral cookies. This structural difference does not authorize copying browser values.

b47's intended safe code/type/status export was lost because the field key `safeErrorTokens` matched the generic diagnostics `token` redaction rule. Correcting that diagnostic field would require b48+.

### Current architecture decision point

The prior target:

`Native history/presentation -> user-visible official full Web conversation performs protected Send -> Native attaches/resumes to the same already-started response -> Native owns realtime response/background lifecycle`

is **paused as a production direction** after exact b47 long-conversation composer viability failure.

Do not allocate b48 merely to:

- rename the diagnostic field;
- copy browser header values;
- chase `/resume` headers;
- test first/exclusive resume;
- add production Native stream ownership;

until the production Send boundary is deliberately selected.

### Evidence-backed next architecture questions

Only these classes of direction are currently justified for investigation:

1. **Official lightweight visible send-only surface** — determine whether a supported official Web surface can perform protected Send without rendering the full conversation history.
2. **Another legitimate account-compatible protected-Send boundary** — only if evidenced and without hidden Web/DOM automation, proof replay or challenge bypass.
3. **Visible Web becomes diagnostic/fallback only** — if no acceptable production Send boundary avoids the long-conversation Web performance owner.

This is a real Human Architecture Gate because choosing a production route changes product behavior/security assumptions. Do not guess or silently continue the previous route.

### Background ordering

Background resilience remains P0, but no production background implementation should be built around a Send surface that can fail before Send.

- if a later accepted Native response owner exists, background work protects that Native lifecycle;
- if visible Web remains only fallback/diagnostic, WebKit background work is not the main production path;
- 5/15-minute, WebContent/process termination, network transitions and battery/thermal remain separate Runtime gates.

### Candidate sequencing

- b39-b47 identities are permanently reserved.
- Exact b47 product source is immutable after Artifact emission.
- **No b48 is allocated.** A later b48+ requires the normal guard/preflight after the architecture gate is resolved.

Detailed Runtime records:

- `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`
- `docs/project/runtime-evidence/DEV-send-stream-b46-runtime.md`
- `docs/project/runtime-evidence/DEV-send-stream-b47-runtime.md`

## Phase 10 — `DEV-attachments` — high priority but Send-boundary dependent

Attachment daily-use priority remains high. Known boundaries:

- Web `+` ~100–200 ms was acceptable in b43's tested scope;
- iOS17 Web Photos chooser filtered videos;
- public `WKUIDelegate` upload-panel replacement is iOS18.4+, not iOS17;
- do not use private WebKit or DOM/file-input injection;
- native iOS17 photo+video support requires an evidenced upload/handoff path;
- assistant file tap-download-share remains a core target before a full download manager.

Do not build native attachment upload against a Send architecture that is still under the Phase 9 Human Architecture Gate.

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

**Human Architecture Gate on `DEV-send-stream`:** decide whether to investigate an official lightweight visible send-only surface / another legitimate account-compatible protected-Send boundary, or demote visible Web to diagnostic/fallback only. Until this gate is resolved, do not allocate b48 and do not continue the previous full-Web-conversation production integration.
