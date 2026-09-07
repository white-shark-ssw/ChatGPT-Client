# DEV-send-stream — Prior Full-Web DOM-Pruning Product Evidence

_Date recorded: 2026-08-29_

## Evidence source and classification

This record captures the user's explicit prior real-device/product experience from an earlier project. It is **not** a Runtime result for current Candidate b47 and does not prove the current ChatGPT Web implementation has the same internal bottleneck.

It is nevertheless valid product evidence for rejecting one concrete mitigation strategy that the user has already implemented and abandoned.

## Prior experiment

The earlier project wrapped ChatGPT Web into an IPA and injected a userscript similar in role to a Tampermonkey script.

The script attempted to reduce long-conversation slowdown by keeping only roughly the latest two conversation rounds visible and making older conversation content invisible.

Observed user result:

- long-conversation presentation was reduced visually;
- opening/using the `+` attachment entry still had noticeable lag;
- the overall interaction remained poor enough that the approach was abandoned.

## Evidence boundary

This result does **not** establish whether the remaining cost came from DOM layout, React/application state, retained message objects, event listeners, attachment UI, WebKit process behavior, memory/GC, networking, or another owner.

It also does not prove that every current ChatGPT Web build will reproduce the same timings.

## Accepted architecture implication

Do not treat any of the following as a production solution for TD-028's full-Web Send-surface problem:

- loading the full existing conversation and merely hiding old turns with CSS or userscript logic;
- keeping the full page/application state alive while reducing only visible DOM content;
- progressively making more of the same full conversation invisible and assuming that this creates a lightweight Send surface.

A future `lightweight visible send-only` direction is worth investigating only if it is **structurally lightweight before rendering the existing conversation** — for example, an official supported route/product surface that does not require loading the full conversation-history application state.

Current public research has not established such an official existing-conversation send-only surface. `chatgpt.com/?q=...`-style behavior is not a documented existing-thread continuation contract and must not be promoted into production without direct evidence.

## Product conclusion

This prior experiment strengthens TD-028: optimizing the full ChatGPT Web page after load is not an accepted route for the native client's daily-chat Send architecture. Visible full Web remains diagnostic/fallback unless a different evidence-backed Send boundary is selected.
