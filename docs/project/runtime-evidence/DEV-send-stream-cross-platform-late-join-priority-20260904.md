# DEV-send-stream — cross-platform late-join realtime priority — 2026-09-04

## Priority override

Latest explicit user direction: prioritize solving cross-platform automatic continuation interruption before the client-owned Web->Native handoff path. The client-owned handoff hypothesis remains recorded but is not the immediate product/research gate.

Latest user Runtime statement is treated as highest-priority evidence: official ChatGPT iOS is able to join/continue a response initiated on another platform. Therefore the service/official client stack has some late-join continuation capability; the unresolved question is the exact server-issued registration/topic/update mechanism exposed to a late-joining official iOS client.

This supersedes any earlier plan that put client-owned `stream_handoff` research first. It does not erase the older 2026-09-02 passive-visible-iOS UI negative sample; that older sample proved only that one visible UI state did not auto-refresh, not that the official native realtime subsystem lacks late-join capability.

## Existing evidence reused

Static inspection of the supplied official iOS package already proves native realtime types/services including `WebSocketConversationEventsService`, `WebSocketConversationObserver`, `WebSocketRegisterResponse.websocketURL`, `WebSocketTopic(topicId, offset)`, `SubscribePayload(topicId,lastOffset,recovered,catchups)`, connect/subscribe/presence commands, and conversation update types including `addMessages`, async status/update and stop.

A privacy-safe official-app research observer already exists under `scripts/research/official_ios_realtime_probe/`. Its decisive test is exactly a cross-platform long turn while official iOS observes without manual refresh. The observer records registration method/path/status/key shape, WebSocket host/path shape, subscribe/topic/offset structure, inbound update/event types and a privacy-safe conversation hash; it does not export auth/query values or prompt/answer/reasoning/tool text.

## Re-materialized official research package

The existing chained research probe Artifact was re-used without modifying its dylib:

- probe source head: `5d2fd88a4a7916827811387b571091f4a894c64f`
- probe Artifact ID: `9818748583`
- probe Artifact ZIP digest: `sha256:b0e3f36eec3d9b51befac98e43b54370d754125c4a7f19fcde7f66596dea2a52`
- probe dylib SHA-256: `0d20cf4761a982612fab995ed8766a887064005a561726c603edceea6072285e`
- user-supplied official source ZIP SHA-256: `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`
- source official bundle: `com.openai.chat`, version/build `1.2026.202 / 30140022279`, MinimumOSVersion 17.0
- original enhancer SHA-256: `aae66c63a7122d301be5025305b92ec63b8da020fdceef22df9bec7cc1acc7b3`
- re-materialized research IPA: `ChatGPT-Official-RealtimeProbe-TrollStore-20260904.ipa`
- research IPA SHA-256: `dd40dd092853f1e4dd4e52c560df0f1b24df18ebd47ca44015065442864ba555`
- ZIP integrity: passed
- extracted content diff versus the supplied official source package: exactly three intentional path changes: replace loaded enhancer entry with the chained Probe, preserve original enhancer at `.original.dylib`, add `ChatGPTRealtimeProbe-Research.txt`.

This package is research tooling only, not a ChatGPTClient Candidate and does not allocate b96.

## Decisive Human Runtime gate

1. Install the research official IPA through TrollStore as the official-app research replacement/update.
2. Fully terminate and relaunch official ChatGPT.
3. Confirm the small `Probe` export control is visible; if not, stop and report launch/UI failure.
4. Keep/open target project conversation A in official iOS.
5. From another platform, start one deliberately long response in A.
6. Do not manually refresh/navigate A during generation unless needed to reproduce the exact known official late-join behavior.
7. After enough live progression/completion, export `ChatGPTRealtimeProbe.jsonl` using the Probe control.
8. Determine the first target-matching late-join mechanism: registration, base conversation subscribe, per-turn subscribe/topic, `conversation-update`, `add-messages`, async status/update, catchup/live transition, offset/cursor semantics and timing relative to remote generation.

A positive target-matching event before terminal authorizes only the minimal evidenced Native late-join acquisition/continuation design. Do not promote WebSocket bodies to Native content authority until completeness/identity/lifecycle are separately proven. `ConversationRepository` remains the sole Native content owner.

## Preserved prohibitions

Do not add guessed topic/offset/resume, hidden fixed polling, retry/watchdog/timer, duplicate Send, WebSocket-body authority, official-framework linking/redistribution, or a second response store.

**Next exact action:** Human Runtime on the re-materialized official iOS realtime Probe package. Analyze its JSONL before allocating b96 or modifying ChatGPTClient product code.
