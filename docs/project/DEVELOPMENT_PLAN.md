# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-30 through exact b54 Runtime and exact b55 Code/CI/Artifact/package verification._

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
8. Durable production policy still requires protected browser Send to remain explicitly user-visible; b48-b55 are isolated diagnostic exceptions and do not silently change that policy.
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
- b48-b55 are explicit diagnostic exceptions only and do not themselves change those production decisions.

### Full-Web product ceiling

- b43 showed a visible official-Web surface could be sufficiently smooth for a shorter tested sequence; Web `+` ~100–200ms; Web Photos filtered videos.
- b44 proved tested `/c/<id>` mapping but the full-page Native→Web→Native form was rejected and immediate Native reconciliation could lag Web-visible output.
- b47 exact-device preparation exposed a stronger pre-Send ceiling: a conversation with only a few rounds but long answers could repeatedly freeze when trying to use the mobile-Web composer.
- Earlier wrapped-Web/userscript evidence likewise showed hiding most visible rounds did not make the full-Web conversation surface acceptable.

Therefore full existing-conversation Web rendering before every protected Send remains rejected as the production daily-chat dependency.

### Official no-resend continuation / Native parity

- b45 Runtime Confirmed official `POST /backend-api/f/conversation/resume` with body `{conversation_id: string, offset: number}`, HTTP200 SSE continuation and no second Send. b45 also provides positive short-background/original-stream survival evidence.
- b46/b47 Native duplicated-after-official-success Cookie+Bearer-only resume returned HTTP404 JSON while later official resume remained healthy.
- Native first/exclusive resume and required additional browser context remain Unknown / Unverified.

### b48-b55 Native composer / Web Send-engine diagnostic exception

Target diagnostic dataflow remains:

`Native composer -> page-owned official protected Send -> intercept Send SSE before Web React -> Native diagnostic incremental memory/UI -> return lifecycle/identity frames to Web`

The official page owns login, browser challenges and Send construction. Diagnostic code does not copy/replay challenge values and does not mutate production `ConversationRepository`.

#### b48-b50 — transport / incremental compact grammar

- b48 proved two sequential Native submissions could drive official protected Send; parser used wrong long-form patch fields.
- b49 proved real incremental Native delivery from compact explicit `o/p/v` patches but captured only short fragments.
- b50 added contextual value-only `{v:string}` continuation and materially passed established turns; fresh new-chat turn 1 still lost a middle section.

#### b51 — fresh-new-chat missing-middle corrected

b51 preserves active assistant-text continuation across exact top-level `title_generation` with no `o`/`p`.

Exact first long answer: 11,618 Native chars / 284 deltas / `titleGenerationWhileContinuationCount=1`, terminal true and visually complete. Accepted: the b50 fresh-first-turn missing-middle defect is Runtime corrected.

#### b52 — final-answer pass; reasoning gap isolated

Exact b52 Runtime: HTTP200 SSE / terminal true; user reported **visible reasoning/thinking beginning slightly truncated, final answer complete**. `rootNonExactTextPatchCount=0`, `inactiveValueStringCount=0`; do not broaden final-answer parser grammar from the rejected root-nonexact hypothesis.

#### b53 — explicit reasoning/tool message classes identified

Exact b53 Runtime:

- visible reasoning beginning still truncated;
- final answer complete;
- Native showed no tool-call presentation;
- service stream explicitly exposed `assistant:reasoning_recap`, separate `assistant:thoughts`, `assistant:code`, and `tool:text` / `tool:code` / `tool:multimodal_text` classes.

Accepted:

- tool execution is structurally real;
- `reasoning_recap` is the direct candidate for explicitly user-visible reasoning;
- raw `thoughts` is non-presentational and must not be exposed;
- role/content type alone is insufficient for safe tool presentation.

#### b54 — tool call/result shape identified; recap evidence blocked by observer saturation

Exact b54:

- Candidate `DEV-send-stream-0.1.0-b54`, source `6a6903c7ad56e534303bfca6a486b83b2d6fe35f`.
- Push `33296672444 / 99217423647`; PR `33296674388 / 99217428590` — success.
- Artifact `9727636043`; IPA SHA `d4b85cffe4db499252d0bc9a2c7c8ea582acf2b88f3d28eeb60e366ee471153b`.

Exact Runtime matched b54 / Release / iPhone iOS17.0, HTTP200 SSE, terminal true. Generic structure signatures reached **32 with overflow 13**.

Material evidence:

- assistant `code` invocation recipients include `api_tool.list_resources` / `api_tool.call_tool`;
- completed assistant code includes `is_complete:true`, `connector_tool_payload`, `tool_icons` structural metadata;
- tool results expose `api_tool` / `api_tool.call_tool` author names, `recipient=all`, text/code/multimodal result containers, and `invoked_plugin` / `invoked_resource` where present;
- `assistant:thoughts` contains a `thoughts` object with `chunks,content,finished,summary`, plus `can_save:false`, `reasoning_status:is_reasoning`, `tool_summary_type:github`, `inline_cot_expandable_content` and `tool_icons` structure.

Accepted: assistant invocation→tool-result pairing is structurally evidenced. Raw tool arguments/results and raw thoughts remain non-presentational. Because the generic observer saturated, absent b54 `reasoning_recap` cannot be treated as protocol absence. b54 is a partial Runtime pass.

#### b55 — current Runtime Candidate; special-structure capacity only

Exact b55 identity:

- Candidate `DEV-send-stream-0.1.0-b55`, version/build `0.1.0 (55)`.
- Exact product/config source `aae856069b461e12dc11ee7d2d450a40ca621d21`.
- Push Run / Job `33299965737 / 99226125826` — success.
- PR Run / Job `33299967033 / 99226129092` — success.
- Artifact `9728606514`.
- ZIP `sha256:fda8dfb16e3d734b9e0f0d55c4e49c0f6cd656e4ec228b13dab3cae108c0a7e3`.
- IPA SHA `f5106949814b44c6c97e2f519ff181498f6a75ff7b9bf9edf0dc0bb0bd299ad1`.
- Package independently verified: `0.1.0 (55)` / Candidate b55 / source `aae856069b46` / Release / iOS14 / `[1,2]` / arm64.

b55 changes **diagnostic capacity only**:

- all b54 protected-Send, SSE filtering, text extraction and Native output behavior remains unchanged;
- generic unique-structure set remains capped at 32;
- `assistant:reasoning_recap`, `assistant:thoughts`, `assistant:code`, and `tool:*` additionally use a separate 24-entry special set;
- special structures can be emitted even after generic saturation;
- terminal metrics add special count/overflow;
- no new raw prompt, answer, reasoning, tool result/payload, ID, auth/proof/header data is logged.

b55 Code/CI/Artifact/package is passed; Runtime pending. b55 is permanently reserved.

### Reasoning / tool presentation plan

This remains part of `DEV-send-stream`, not a separate Work.

After explicit display-boundary evidence:

- explicitly user-visible reasoning summary becomes a distinct Native response phase/presentation from final answer;
- reasoning summary is collapsible/expandable;
- service-visible tool activity may be shown with a compact status/card and tap-driven native sheet/popover for approved user-facing details;
- reasoning→final transition belongs to one authoritative response lifecycle and occurs exactly once;
- raw `assistant:thoughts`, hidden chain-of-thought, internal tool/system nodes, raw tool arguments and raw tool results are never exposed merely because diagnostic structures exist.

### Current b55 human Runtime gate

One focused reproduction is sufficient:

1. install exact b55 and clear diagnostics;
2. open `Native 输入 / Web Send（b55诊断）`;
3. send one request that naturally produces visible reasoning plus tool activity;
4. wait for terminal;
5. export diagnostics.

Visual behavior is intentionally expected to remain similar to b54 because b55 is evidence-only.

Decision signals:

- `specialStructureSignatureCount` / overflow must prove the special channel itself did not saturate;
- if `assistant:reasoning_recap` is emitted, its text-free content-container and presentation metadata become the evidence for the explicitly user-visible reasoning surface;
- assistant-code/tool-result special structures must remain available even after generic count reaches 32.

Do not implement reasoning/tool UI or allocate b56 until exact b55 Runtime supports a concrete smallest next change.

### Background ordering

Background resilience remains P0, but production implementation follows eventual response ownership.

- b45 proves positive short-background/original-stream survival and official recovery after forced interruption.
- b49 also showed a long diagnostic response reaching terminal across multiple background intervals.
- b48-b55 remain Web-owned diagnostic transport rather than accepted production response ownership.
- 5/15-minute, WebContent/process termination, network transitions and battery/thermal remain separate Runtime gates.

### Candidate sequencing

- b39-b55 identities are permanently reserved once emitted.
- Exact b55 product/config source is immutable after Artifact emission.
- Any product-code correction requires b56+ and must be justified by exact b55 Runtime; do not pre-allocate b56.

Detailed current Runtime records include:

- `docs/project/runtime-evidence/DEV-send-stream-b45-runtime.md`
- `DEV-send-stream-b46-runtime.md`
- `DEV-send-stream-b47-runtime.md`
- `DEV-send-stream-b49-runtime.md`
- `DEV-send-stream-b50-runtime.md`
- `DEV-send-stream-b51-runtime.md`
- `DEV-send-stream-b52-runtime.md`
- `DEV-send-stream-b53-runtime.md`
- `DEV-send-stream-b54-runtime.md`

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

**Human Runtime Gate on exact b55.** Run one reasoning/tool-active turn and export diagnostics. Do not merge PR #29, promote the diagnostic Web Send-engine architecture to production, implement reasoning/tool presentation, or allocate b56 before the exact b55 special-structure evidence is classified.
