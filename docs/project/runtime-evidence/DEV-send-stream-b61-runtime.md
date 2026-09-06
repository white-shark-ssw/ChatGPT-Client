# DEV-send-stream b61 Runtime Evidence

Date: 2026-08-30

## Exact candidate

- Candidate: `DEV-send-stream-0.1.0-b61`
- Version/build: `0.1.0 (61)`
- Exact product/config source: `2386872af03e0684eee8deca87f636dc265114ec`
- Artifact: `9732514781`
- IPA SHA: `6fff9fa7178d0915f74a08eadeeb8ad9cb7927416ca1c09c979b69df67a18e21`
- Runtime target: iPhone / iOS 17.0
- User evidence: `ChatGPTClient-Diagnostics-20260830-134827.json` (first failed attempt), then after clearing diagnostics and force-quitting/relaunching, `ChatGPTClient-Diagnostics-20260830-135112.json` (successful tool-active attempt), plus direct screenshots/observation.

## Attempt 1 — false-ready / false-submitted Send-entry defect

Direct observation: the message appeared to be sent, but no `正在思考` state or answer activity appeared and the turn remained stuck.

Diagnostic sequence:

- page was `new_or_other`;
- composer reported `ready=true` with strategy `textarea`;
- Native recorded `nativeSubmit` attempt 1;
- submission re-probed the same generic `textarea` strategy;
- script reported `submitResult=submitted`;
- no official protected-Send observation followed: no `sendObserved`, no `sendResponse`, no thinking presentation, no stream metrics.

Source correlation: b61 `findComposer()` accepted an unqualified `textarea:not([disabled])` after the two explicit official-composer strategies. `submit()` could call `requestSubmit()` and report `submitted` even though that generic textarea/form did not produce the official `/backend-api/f/conversation` request.

Classification: **Runtime defect — false-ready composer / false-submitted Send entry.** This is earlier than model generation or SSE parsing and must not be misclassified as a response-stream stall.

## Attempt 2 — tool lifecycle and response presentation pass

After clearing diagnostics and force-quitting/relaunching, the official composer reached strategy `prompt_textarea`; the same class of GitHub/repository request then completed normally.

Terminal metrics:

- HTTP 200 SSE / terminal true;
- frameCount `135`;
- Native reasoning `10 deltas / 251 chars`;
- Native final answer `68 deltas / 2363 chars`;
- reasoning preambles `2 / 11 chars`;
- service / Native reasoning segment breaks `1 / 1`;
- reasoning-end marker `1`;
- fallback promotion `false`;
- Native thinking presentations `3`;
- tool invocation identities `14`;
- tool results `14`;
- result parent present/matched/unmatched/missing `14/14/0/0`;
- paired presentations `14`;
- Native tool presentations `14`;
- Native tool completion updates `14`.

Direct user observation: reasoning opening appeared complete; tool rows visibly showed both `调用中` and `已完成`; final answer looked complete.

Classification: **Runtime pass for the tested parent-paired tool lifecycle, thinking/reasoning/final presentation and text completeness scope.**

## Combined b61 conclusion

b61 is **Runtime Partial** overall:

1. The b61 parent-paired Native tool lifecycle is accepted for this tested tool-active turn: 14 invocation identities and 14 results were paired by exact result `parent_id`, with 14 visible completion updates and no unmatched/missing parent in the exported run.
2. The tested thinking/reasoning/final answer path remained complete and terminal.
3. A separate Send-entry reliability defect exists: an early generic textarea can be misclassified as the official composer, allowing `submitResult=submitted` without any protected Send request.
4. The defect is intermittent/page-state dependent; absence of reproduction in later runs does not invalidate the first exact evidence.
5. No raw tool request/result body, connector payload value, service ID or `assistant:thoughts` is authorized by this Runtime.

## Evidence-driven next change

Allocate b62 only for the concrete Send-entry defect. Remove generic `textarea:not([disabled])` from composer authority; retain only evidenced official composer identities (`#prompt-textarea` and explicit `[contenteditable="true"][role="textbox"]`). Do not add retry, timer, watchdog, polling or speculative fallback. Preserve b61 text/reasoning/tool parsing and bounded detail-shape diagnostics unchanged.
