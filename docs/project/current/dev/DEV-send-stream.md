# DEV-send-stream

## Status

**Active — exact b62 now has a focused iPhone/iOS17 Runtime pass for the verified-composer Send-entry gate. The tested cold-launch path remained `ready=false / strategy=none` until the official `prompt_textarea` appeared, then Native submit immediately produced a real `sendObserved`, HTTP200 SSE, event-driven thinking/reasoning, exact reasoning end, 20/20 parent-paired tool-result completions and a complete-looking final answer. This accepts the narrow b62 correction for the tested scope; it does not claim the intermittent b61 page race is impossible under every future official-Web state. TD-024/TD-025/TD-028 and production `ConversationRepository` ownership remain unchanged; PR #29 stays evidence-only / unmerged. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged; evidence-only
- Other Active development checkpoints: none at last verified guard
- Stable native predecessor: b38
- Current exact diagnostic Candidate: `DEV-send-stream-0.1.0-b62`
- Exact product/config source: `e1b44f7ab6c47bd41de3ed9460ec0b77b7cc9f3f`
- Artifact: `9733577825`
- IPA SHA: `ac9f031fb43b91ac12f486b1f743f741b404faf133725bdc8abec059b68b87d8`
- b39-b62 emitted identities: permanently reserved

## Exact b61 Runtime conclusion

b61 remains **Runtime Partial**.

- Failed cold/new-page run: generic `textarea` was treated as ready, Native reported submit, but no `sendObserved`, no response and no thinking/SSE followed. This was a false-ready / false-submitted Send-entry defect before protected Send.
- Successful relaunch run: HTTP200 SSE / terminal; reasoning `10/251`, final `68/2363`; exact result-parent association `14/14`; Native tool presentations/completion updates `14/14`; user observed complete reasoning opening and `调用中 -> 已完成`.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b61-runtime.md`.

## Exact b62 identity / pre-Runtime validation

- Candidate: `DEV-send-stream-0.1.0-b62`
- Version/build: `0.1.0 (62)`
- Exact product/config source: `e1b44f7ab6c47bd41de3ed9460ec0b77b7cc9f3f`
- Product tree: `d3432dfe2e32cddcfac7a5a56d7880772dc6989d`
- Push Run / Job: `33316398081 / 99270535435` — success
- PR Run / Job: `33316399402 / 99270539763` — success
- Artifact: `9733577825`
- ZIP: `sha256:d53ddb88c5d2092294592416e10e5a0a752cb7afb0bbe0a39c2c137d021082d0`
- IPA SHA: `ac9f031fb43b91ac12f486b1f743f741b404faf133725bdc8abec059b68b87d8`
- Package: Release / `0.1.0 (62)` / Candidate b62 / source marker `e1b44f7ab6c4` / minimum iOS14 / UIDeviceFamily `[1,2]` / arm64

b62 changes only the evidenced Send-entry boundary: generic `textarea:not([disabled])` is no longer composer authority; current accepted diagnostic identities are `#prompt-textarea` or explicit `[contenteditable="true"][role="textbox"]`. No retry, wait timer, polling, watchdog or speculative fallback was added. b61 text/reasoning/tool behavior is otherwise unchanged.

## Exact b62 Runtime — focused pass

User export: `ChatGPTClient-Diagnostics-20260830-151146.json`.

Package identity matched exact b62: Release / build62 / Candidate b62 / source `e1b44f7ab6c4` / iPhone / iOS17.0.

### Composer / protected-Send gate

Observed startup sequence:

1. composer `ready=false`, strategy `none`;
2. page loaded `new_or_other`;
3. composer remained `ready=false`, strategy `none`;
4. only later composer became `ready=true`, strategy `prompt_textarea`;
5. submit-time composer remained `prompt_textarea`;
6. `submitResult=submitted` was immediately followed by real `sendObserved`;
7. response was HTTP200 `text/event-stream` and entered `lifecycle_send_accepted` thinking state.

This passes the exact b62 primary gate for the tested cold-launch path. It directly differs from the rejected b61 generic-textarea run. One positive run does not prove the official page can never present another future race.

### Reasoning / final presentation

Terminal metrics:

- `frameCount=196`
- `terminal=true`
- Native reasoning `34 deltas / 497 chars`
- Native reasoning segment breaks `2`
- thinking preambles `3 / 20 chars`
- reasoning-active signals `3`
- Native thinking presentations `4`
- exact reasoning-end markers `1`
- fallback promoted `false`
- final answer `93 deltas / 2878 chars`
- Native total `127 deltas / 3375 chars`
- inactive value strings `0`
- root-nonexact text patches `0`

User directly reported the one tested round looked normal; screenshot showed populated reasoning, completed tool rows and complete-looking final text with no obvious truncation.

### Tool lifecycle

- tool invocations presented: `20`
- invocation identities observed: `21`
- results: `20`
- result parent present/matched/unmatched/missing: `20/20/0/0`
- paired Native result presentations: `20`
- Native tool presentations/completion updates: `20/20`

The extra observed invocation identity is **not** force-paired by count/order. Every completed result in the tested set had an exact parent match and corresponding Native completion update.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b62-runtime.md`.

Classification: **b62 focused Runtime pass for verified-composer Send entry + preserved tested reasoning/final + exact-parent tool lifecycle. Stable/Frozen No.**

## Current unresolved presentation boundary

Expandable tool details remain within `DEV-send-stream`. b62 safe shape diagnostics observed candidates including:

- `connector_tool_payload` as string-shaped metadata in several assistant code messages;
- `reasoning_titles` and `tool_icons` as bounded arrays;
- `invoked_resource` as object-shaped tool metadata;
- `inline_cot_expandable_content` on an `assistant:thoughts` structure.

These observations are **shape-only**. They do not authorize exposing raw connector/tool request or result bodies, service IDs, arbitrary `invoked_resource` values, or `assistant:thoughts`. Exact official user-visible expandable-detail schema remains Unknown / Unverified.

## Recovery point

Completed this cycle:

1. exact b62 package identity reverified from the user Runtime export;
2. b62 focused cold-launch Runtime classified as pass for the tested gate;
3. real protected Send grounded by `sendObserved` + HTTP200 SSE, not `submitted` alone;
4. reasoning/final presentation preserved through terminal;
5. tool result parent matches and Native completion updates passed `20/20`;
6. `docs/project/runtime-evidence/DEV-send-stream-b62-runtime.md` created;
7. durable project docs are being synchronized to this Runtime classification;
8. exact b62 product/config source remains `e1b44f7a...`; subsequent documentation commits do not redefine it;
9. PR #29 remains evidence-only and must not be merged yet.

## Next exact action

**Do not allocate b63 by guess.** First use existing b62 safe shape evidence together with the previously captured official-Web expanded-tool screenshots to identify whether any narrowly bounded service field can be proven to correspond to user-visible expandable tool detail. If current evidence cannot prove that mapping, the next Candidate may be a bounded diagnostic-only b63 designed around one exact unresolved field; it must not expose/log raw tool request/result bodies, connector payload values or `assistant:thoughts`. Keep PR #29 open/unmerged and retain exact b62 as the current tested product source until a concrete next change is justified.
