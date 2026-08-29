# DEV-send-stream

## Status

**Active — b45 native realtime handoff evidence probe authorized; Web should carry Send only if Native can own live response**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / reasoning / follow-tail / 官方 Web / hybrid / realtime handoff / resume / stream`
- **Branch / PR**: `dev/send-stream-20260829`; PR #29 open/mergeable; do not merge as accepted Send UX.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; Stable native predecessor remains b38.
- **Resume guard 2026-08-29**: branch `d2a8fb7aa07fcac1ca57b1ebde54dc34f2aac51d`; PR #29 open/mergeable; main unchanged; only this Active dev checkpoint; no peer conflict.
- **Exact b44 product source**: `f1503cf7121512a84e5c55a3642181c17324d791`; Artifact `9712583513`; IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.
- **Candidate rule**: b39-b44 permanently reserved. `DEV-send-stream-0.1.0-b45` / build 45 is now allocated for the realtime-handoff diagnostic probe. No b45 Artifact exists yet.

## Security / transport boundary retained

Exact b42 proved successful tested ChatGPT-account Send requires browser anti-abuse challenge output (`proofOfWorkRequired=true`, `turnstileRequired=true`, `soRequired=true`, non-empty PoW + Turnstile finalize input). Pure-native account Send remains blocked.

Never implement PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay, captured challenge/proof replay, guessed alternate Send endpoints, hidden challenge-harvesting WebViews, DOM answer/reasoning scraping, Native composer injection into a covered/hidden Web composer, synthetic hidden Send clicks, or private file-input injection.

The user's latest visual suggestion — hook the Web send button and hide Web completely — remains rejected for implementation because it would turn the protected browser Send flow into hidden/shadow transport. The useful goal instead is to minimize Web responsibility to the smallest **user-visible legal Send initiation** and move response ownership to Native if protocol evidence supports it.

## Accepted b40-b44 evidence retained

- b40: existing/new official Web Send uses `POST /backend-api/f/conversation`, HTTP200 SSE; normal `v1` + structural patch events + `[DONE]`; early `resume_conversation_token` observed; new-chat authoritative identity appears early.
- b41: server Stop `POST /backend-api/stop_conversation`; prepare/Sentinel precursor structure evidenced.
- b42: browser-owned PoW/Turnstile/`so` challenge output required before successful Send.
- b43: visible Web feasibility/smoothness largely accepted; Web `+` ~100–200ms; Web Photos filtered videos on iOS17.
- b44: `/c/<id>` A/B mapping worked, but immediate Native reconciliation could lag Web assistant output; full-page Native->Web->Native UX rejected.

## Latest product architecture decision

The user explicitly rejects the separate API product route and now accepts this as the desired architecture only if evidence supports it:

`Native composer/history/presentation -> user-visible official Web performs legal Send -> Native attaches/resumes/subscribes to the same in-progress response without resending prompt -> Native owns reasoning/final streaming presentation and later background lifecycle.`

This architecture is **not yet proven**. Web must not remain the realtime-response authority merely because it can Send.

## b45 evidence question

Before any new hybrid UI or TrollStore background work, determine whether official ChatGPT Web exposes a same-response continuation mechanism that Native could legitimately consume **without a second Send**.

The existing probe currently observes only selected fetch/XHR routes and the original `/f/conversation` SSE. It does not yet provide enough evidence for Native handoff.

b45 must observe, structurally only:

1. when `resume_conversation_token` / response / turn / handoff identity first appears in the original Send SSE;
2. whether the official page subsequently opens any additional same-origin fetch/XHR/EventSource/WebSocket connection associated with the active response;
3. route/path class, method, transport, content-type/framing, header **names only**, JSON key/type structure, and safe identity-presence/shape only;
4. whether any `stream_handoff`, turn-stream, resume, subscribe, stream-status or equivalent official-page behavior occurs naturally;
5. whether a later connection appears to receive continuation events without issuing another Send.

Do **not** log prompt/answer/reasoning text, raw conversation/message/response/resume IDs, Cookie/Authorization values, Sentinel/Turnstile/PoW/conduit values, or raw payloads.

b45 is observation-only: do not replay a resume token or guess a continuation endpoint yet. If the official page itself demonstrates a continuation request, a later Candidate may test Native parity against that exact observed route/structure.

## Background ordering changed

TD-026 background resilience remains a hard product requirement, but implementation is now **deferred behind realtime-handoff feasibility**. If Native can own/resume the response stream, background work should protect the Native response lifecycle rather than WebKit. Only if Native handoff is disproven would WebKit true-background remain relevant to the fallback visible-Web architecture.

## b45 Runtime target

On the exact primary iPhone/iOS17 device:

1. Settings -> Send protocol probe.
2. Use default ChatGPT / primary assistant, preferably a response long enough to expose reasoning/stream behavior.
3. Send one new-chat prompt and one existing-chat prompt if practical.
4. Let each response progress normally; do not manually refresh during the capture.
5. Export diagnostics JSON.

Acceptance of the probe means only that the needed structural evidence was captured. It does **not** mean Native handoff exists until the evidence shows a real continuation mechanism.

## Batch recovery point — b45 assembly

Known baseline before allocation: `dev/send-stream-20260829@d2a8fb7aa07fcac1ca57b1ebde54dc34f2aac51d`; PR #29 open/mergeable; `main@34811877896ca88c6656be6676f5466a19931ce6`; no peer Active dev Work; b45 previously absent from Build Index.

Planned coherent product batch:

- `ChatGPTClient/Protocol/ProtocolReadProbe.swift` — extend structural observation to handoff/resume-related SSE semantics and additional browser transports/routes, without raw protected values.
- `ChatGPTClient.xcodeproj/project.pbxproj` — build 45 / Candidate b45.
- `.github/workflows/ios-foundation.yml` — b45 workflow/artifact identity.

Because product-file pushes on the real dev branch trigger CI, assemble these three changes first on a non-triggering tooling branch, verify its exact diff, then non-force fast-forward the real dev branch once to the complete b45 commit chain. Never publish product code under stale b44 metadata.

## Next exact action

Create the non-CI assembly branch from this checkpoint commit, implement the smallest observation-only probe, change build/workflow identity to b45, audit the three-file product/config diff, then fast-forward the real branch and continue through CI/Artifact/package verification. Do not stop for approval before the Runtime handoff gate unless a real blocker appears.
