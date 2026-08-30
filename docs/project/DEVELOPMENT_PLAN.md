# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-30 through exact b56 Runtime and exact b57 Code/CI/Artifact/package verification._

## Purpose

Durable implementation sequence for the native iOS ChatGPT client. Current real source, exact CI/Artifact evidence, real-device evidence and the latest explicit requirements outrank stale plan wording.

Core constraints: UIKit native shell/read client, TrollStore IPA, primary tested runtime iPhone 15 Pro Max / iOS17.0, deployment target iOS14, and private/internal ChatGPT behavior must be evidenced rather than guessed.

## Delivery principles

1. Reach a genuinely usable client early; do not wait for roadmap breadth.
2. Keep one authoritative owner per identity/state domain.
3. Prefer official ChatGPT iOS interaction patterns where architecture permits.
4. Do not add speculative retry/fallback/timer/watchdog/duplicate-state machinery.
5. Distinguish Code / Static / CI / Artifact / Runtime / Stable evidence.
6. High-frequency daily-use interactions such as Copy, attachments and reliable background reasoning/stream continuation outrank low-value polish once dependencies exist.
7. Optimize only evidenced bottlenecks, especially for long conversations.
8. Durable production policy still requires protected browser Send to remain explicitly user-visible; b48-b57 are isolated diagnostic exceptions and do not silently change that policy.
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

- b40-b41 established official-Web protected-Send SSE structure.
- Exact b42 proved PoW, Turnstile and `so` are required before successful ChatGPT-account protected Send. Pure-native/transient-auth account Send remains blocked.
- The separately authenticated/billed API-product architecture remains rejected. Primary-account Sub2API/Codex-subscription Runtime remains blocked by the account-safety gate.
- Hidden/shadow Web Send, challenge replay/bypass and Native DOM/input automation remain rejected as **production** architecture under current TD-024/TD-025.
- b48-b57 are explicit diagnostic exceptions only and do not themselves change those production decisions.

### Full-Web product ceiling

- b43 showed a visible official-Web surface could be sufficiently smooth for a shorter tested sequence; Web `+` ~100–200ms; Web Photos filtered videos.
- b44 proved tested `/c/<id>` mapping but the full-page Native→Web→Native form was rejected and immediate Native reconciliation could lag Web-visible output.
- b47 exact-device evidence showed a few long-answer rounds could make the mobile-Web composer unusable before Send.
- Earlier wrapped-Web/userscript evidence also showed that display-layer hiding did not make full-Web conversation state acceptable.

Therefore full existing-conversation Web rendering before every protected Send remains rejected as the production daily-chat dependency.

### Official no-resend continuation / Native parity

- b45 Runtime Confirmed official `POST /backend-api/f/conversation/resume` with `{conversation_id: string, offset: number}`, HTTP200 SSE continuation and no second Send; short background/original-stream survival evidence is positive.
- b46/b47 Native duplicated-after-official-success Cookie+Bearer-only resume returned HTTP404 JSON while later official resume remained healthy.
- Native first/exclusive resume and required additional browser context remain Unknown / Unverified.

### b48-b57 Native composer / Web Send-engine diagnostic exception

Target diagnostic dataflow remains:

`Native composer -> page-owned official protected Send -> intercept Send SSE before Web React -> Native diagnostic incremental memory/UI -> return lifecycle/identity frames to Web`

The official page owns login, browser challenges and Send construction. Diagnostic code does not copy/replay challenge values and does not mutate production `ConversationRepository`.

#### b48-b52 — incremental response grammar

- b48 proved sequential Native submissions can drive official protected Send; parser initially used wrong long-form fields.
- b49 proved real compact `o/p/v` incremental delivery.
- b50 added contextual `{v:string}` continuation but fresh new-chat turn 1 remained incomplete.
- b51 preserving active continuation across exact top-level `title_generation` fixed the fresh-new-chat missing-middle defect; first long answer delivered 11,618 Native chars / 284 deltas and was visually complete.
- b52 kept final answer complete while visible reasoning beginning remained slightly truncated; root-nonexact/inactive-value theory was rejected.

#### b53-b55 — reasoning/tool structure evidence

- b53 identified `assistant:reasoning_recap`, separate `assistant:thoughts`, `assistant:code`, and tool text/code/multimodal classes. Raw `thoughts` is non-presentational.
- b54 materially identified assistant invocation→tool-result grammar, but generic observation saturated at 32/overflow13.
- b55 introduced an independent bounded special-structure channel; exact Runtime passed the intended saturation gate (generic 32/overflow14, special 7/overflow0) and captured completed `assistant:reasoning_recap / recipient=all` with `reasoning_status=reasoning_ended` and `reasoning_recap_type=collapse`. Separate `assistant:thoughts` remained non-presentational.

#### b56 — recap UI works; recap-body assumption rejected

Exact b56 identity: Candidate `DEV-send-stream-0.1.0-b56`, source `cec921030fd1af9f3853f35af52b661586b3a8ab`, Artifact `9728937100`, IPA SHA `da62776200ce94fef95326abaea3b980f65a5698df5dfe481bd34046e0f8dbe6`.

Exact b56 Runtime on iPhone/iOS17:

- HTTP200 SSE / terminal true;
- `frameCount=75`, Native 26 deltas / 504 chars;
- exact-root 4, nested 8, contextual value strings 14 / 299 chars, inactive strings 0;
- generic structures 32 / overflow16, special structures 8 / overflow0;
- exact recap chars 7.

User-visible result:

- recap control appeared and expand/collapse worked;
- recap was only `思考了 40s` in the tested turn, not the real visible reasoning body;
- real visible reasoning remained concatenated with final answer;
- reasoning beginning remained truncated.

Accepted correction:

- `reasoning_recap.content` is not established as the reasoning body;
- the exact completed recap event remains a trustworthy explicit `reasoning_ended` phase marker;
- raw `assistant:thoughts` remains prohibited;
- event ordering showed ordinary `assistant:text:in_progress` before the first accepted `/message/content/parts/0` append, giving a concrete missing-prefix hypothesis, but the ordinary message's actual content field shape was not captured. Do not guess it.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b56-runtime.md`.

#### b57 — current Runtime Candidate; phase split + missing-prefix evidence

Exact identity:

- Candidate `DEV-send-stream-0.1.0-b57`, version/build `0.1.0 (57)`.
- Exact product/config source `7074b1f85a0f239a5fd615f52196e1e28145523c`.
- Product tree `c402ce522e244cf63aa44b80a6d165b84342104c`.
- Push Run / Job `33302357908 / 99232731468` — success.
- PR Run / Job `33302359351 / 99232735067` — success.
- Artifact `9729360247`; ZIP `sha256:ae5a5532e2c30624907e9a2d61966090df4b8cc9ffa57f1b5725db8b61a8d275`.
- IPA SHA `c8662a065f0dc1ec627f7eba86387d190e80e593a6972cc13934f80c4efe0a06`.
- Package: Release / `0.1.0 (57)` / Candidate b57 / source `7074b1f85a0f` / iOS14 / `[1,2]` / arm64.

b57 makes only the smallest changes supported by b56:

1. Preserve every previously accepted protected-Send, `/message/content/parts/0`, contextual value and nested text acceptance rule.
2. Treat the exact completed recap only as the `reasoning_ended` marker; do not display recap text as the reasoning body.
3. Route accepted text before the marker to a distinct Native `思考过程` region.
4. Route accepted text after the marker to the ordinary final-answer region.
5. Show/expand `思考过程` while it streams; collapse it on exact reasoning end and allow explicit expand/collapse afterwards.
6. If terminal arrives without any reasoning-end marker, promote the provisional pre-marker text into the ordinary answer so non-reasoning turns are not permanently misclassified.
7. Record only phase aggregate counts plus a separate bounded 12-entry structure channel for ordinary `assistant:text` messages: direct content/message/metadata field names, string lengths, array shapes/string-char counts, safe booleans/enums, and before/after-marker phase.
8. Do not extract an unproven initial text field yet.
9. Do not expose raw `assistant:thoughts`, raw tool args/results, connector payloads, hidden/internal reasoning/system data or auth/proof/header values.

b57 Code/CI/Artifact/package is Passed; Runtime pending. b57 is permanently reserved.

### Reasoning / tool presentation plan

This remains part of `DEV-send-stream`, not a separate Work.

- User-visible reasoning and final answer are distinct presentation phases when explicit protocol/state evidence supports the boundary.
- Exact b55/b56 supports `reasoning_ended` as the current phase boundary; recap text itself is not the reasoning body.
- Raw `assistant:thoughts`, hidden chain-of-thought/internal reasoning, internal system/tool nodes, raw tool arguments/results remain prohibited.
- Tool invocation/result pairing is structurally real, but exact user-visible tool-node rules still need evidence before any tool card/sheet is built.
- Reasoning→final transition must belong to one authoritative response lifecycle and occur exactly once from protocol/state evidence, not elapsed time, DOM text, cell redraw or UI title.

### Current b57 human Runtime gate

One focused reproduction is sufficient:

1. install exact b57 and clear diagnostics;
2. open `Native 输入 / Web Send（b57诊断）`;
3. send one request that naturally produces visible reasoning plus tool activity;
4. verify the previously mixed visible reasoning now streams only inside `思考过程` and final answer begins only after the reasoning section collapses;
5. report whether the **beginning of `思考过程` is still truncated**;
6. expand/collapse the completed reasoning region once;
7. confirm no raw `assistant:thoughts` or raw tool payload appears;
8. wait for terminal and export diagnostics.

Primary remaining-prefix evidence:

- `assistantTextMessageCount`, before/after-reasoning-end counts;
- `phaseTextStructureSignatureCount` / overflow;
- the first `streamStructure` row with `messageRole=assistant`, `messageContentType=text`, `textPhase=before_reasoning_end`;
- especially its `contentKeys`, `contentStringFields`, `contentArrayFields`.

Do not allocate b58 or guess the initial text container until exact b57 Runtime supplies that structure evidence.

### Background ordering

Background resilience remains P0, but production implementation follows eventual response ownership.

- b45 proves positive short-background/original-stream survival and official recovery after forced interruption.
- b49 also showed a long diagnostic response reaching terminal across multiple background intervals.
- b48-b57 remain Web-owned diagnostic transport rather than accepted production response ownership.
- 5/15-minute, WebContent/process termination, network transitions and battery/thermal remain separate Runtime gates.

### Candidate sequencing

- b39-b57 identities are permanently reserved once emitted.
- Exact b57 product/config source `7074b1f85a0f239a5fd615f52196e1e28145523c` is immutable after Artifact emission.
- Any product-code correction requires b58+ and must be justified by exact b57 Runtime; do not pre-allocate b58.

Detailed Runtime records include `DEV-send-stream-b45-runtime.md`, b46, b47, b49, b50, b51, b52, b53, b54, b55 and b56 under `docs/project/runtime-evidence/`.

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

**Human Runtime Gate on exact b57.** Validate one reasoning/tool-active turn, the reasoning/final phase split, the remaining leading-prefix behavior and the text-free first `assistant:text` structure evidence. Do not merge PR #29, promote the diagnostic Web Send-engine architecture to production, add tool UI, guess the missing initial-text field, or allocate b58 before exact b57 Runtime is classified.
