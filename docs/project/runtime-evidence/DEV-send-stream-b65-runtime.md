# DEV-send-stream b65 Runtime Evidence

Date: 2026-08-31

Candidate: `DEV-send-stream-0.1.0-b65`

Exact product/config source: `44138db766d00e62cfda7f20182f6d20f1ec3352`

Runtime export: `ChatGPTClient-Diagnostics-20260830-191806.json`

## Package identity

Export metadata matched the exact delivered package:

- app version `0.1.0`
- build `65`
- Candidate `DEV-send-stream-0.1.0-b65`
- source marker `44138db766d0`
- Release
- iPhone
- iOS `17.0`
- deployment target `14.0`

## Protected Send / response lifecycle

Observed one complete tested turn:

`ready=false/none -> ready=true/prompt_textarea -> nativeSubmit -> submitted -> sendObserved(existing_conversation) -> HTTP200 text/event-stream -> thinking active -> reasoning/final/tool lifecycle -> terminal`

Terminal stream metrics:

- frameCount `132`
- terminal `true`
- exact top-level text patches `10`
- nested text patches `9`
- inactive value strings `0`
- title-generation continuation `1`
- exact reasoning-end markers `1`
- reasoning fallback promoted `false`
- Native reasoning `14 deltas / 295 chars`
- Native final answer `71 deltas / 2827 chars`
- Native total `85 deltas / 3122 chars`
- thinking preambles `2 / 13 chars`
- reasoning-active signals `2`
- service/native reasoning segment breaks `1/1`

User directly reported no apparent reasoning/final truncation in the tested turn.

## Tool lifecycle / exact association

Terminal metrics:

- tool invocation identities `10`
- completed invocation presentations `9`
- results `10`
- result parent present/matched/unmatched/missing `10/10/0/0`
- paired Native result presentations `10`
- Native tool presentations/completion updates `10/10`
- Native detail-capable rows `9`

This preserves the accepted exact `parent_id` rule. No unmatched/missing result was present in this run.

## b65 structured detail presentation

The user directly verified:

- completed tool rows expand/collapse;
- opening a tool row exposes independent second-level `工具输入` and `工具输出` disclosures;
- the two child sections expand independently;
- tool output is no longer the b64 second-layer JSON escape wall and is shown as readable hierarchical content/text;
- no apparent answer/reasoning truncation occurred.

Exported presentation events independently show tool-row and child-section interaction, including one observed row with `inputCharacters=151`, `outputCharacters=15024`, and another with `inputCharacters=78`, `outputCharacters=15568`. Raw values are not present in diagnostics.

The user noted two visual polish issues only:

1. spacing between `工具输入` and `工具输出` is looser than desired;
2. pretty JSON input may still display legal escaped slash notation such as `\/`.

These are readability/polish observations. No Runtime evidence indicates data loss, incorrect parent association, Send failure or parser failure, so they do not justify another diagnostic Candidate by themselves.

## Classification

**Runtime pass for the exact b65 focused structured GitHub tool-detail gate.**

Accepted from this run:

- verified-composer protected Send path remained functional;
- HTTP200 SSE reached terminal;
- tested reasoning/final presentation remained complete-looking;
- exact-parent tool lifecycle remained correct;
- nested `工具输入` / `工具输出` disclosures work;
- b64 escaped/dense detail-rendering defect is closed for the tested GitHub shapes.

Not implied by this pass:

- production `ConversationRepository` response ownership;
- production approval of the diagnostic hidden/covered Web Send engine;
- Stop semantics;
- new-chat pending -> authoritative identity handoff;
- follow-tail / hidden-response production behavior;
- non-GitHub connector detail schema;
- Stable/Frozen Phase 9 acceptance.

No b66 is justified solely for the remaining spacing / escaped-slash polish.
