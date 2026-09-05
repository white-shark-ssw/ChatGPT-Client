# DEV-send-stream — Official iOS Probe v0.5 Runtime / v0.6 callback-surface gate — 2026-09-04

## Input identity

- User-exported JSONL: `ChatGPTRealtimeProbe(4).jsonl`
- SHA-256: `26e8646945831764bf6317c99213ff8a9621d09942e642a19b4f15aa24c892ba`
- Size: 47,648 bytes
- Parsed events: 146
- Parse errors: 0
- Probe version: all `0.5`

## Runtime result

Probe v0.5 is clean and does not reproduce the v0.2 receive-error logging storm. Task-level observation is Runtime Positive. The target conversation hash `0df178903e95` issued authoritative `__NSCFLocalDataTask` GET Detail requests at `20:57:28.958`, `20:57:56.962`, `20:58:07.117`, `20:58:16.235`, `20:58:25.668`, `20:58:35.051`, `20:58:44.323`, and `20:58:53.546Z`. Excluding the first 28.004s reacquisition gap, intervals are `10.155 / 9.118 / 9.433 / 9.383 / 9.272 / 9.223s`, median approximately `9.328s`.

This independently reconfirms the v0.4 finding: the official iOS app performs Native authoritative Conversation Detail polling for the cross-platform target.

There are zero `http.conversation_detail.async_status` events. Because the same target Detail tasks are visible at `NSURLSessionTask.resume`, this absence is classified as an instrumentation-coverage failure of the v0.5 public `URLSession:dataTask:didReceiveData:` observer for the Swift-async Detail response path. It is **not** a protocol negative and does not prove `conversation_async_status` is absent.

## v0.6 research gate

Probe v0.6 changes research instrumentation only. On the first target Conversation Detail task, it records one bounded `probe.detail_task_callback_surface` event containing only callback-relevant Objective-C class/selector names, method argument counts/type encodings, and callback/session/delegate-related ivar names/type encodings from the task class hierarchy. It does not read ivar values, hook guessed private callbacks, issue requests, poll, retry, or capture response/auth/content.

The next decision must come from the actual Runtime selector surface. Only after one exact response-delivery callback is evidenced may a later research revision attach the existing exact `conversation_async_status` scanner to that callback.

## Product boundary

ChatGPTClient product remains exact b95. b96 is unallocated. `ConversationRepository` remains sole Native response/content authority. Do not implement Native polling cadence, `/resume`, retry/watchdog/timers, duplicate Send, WebSocket-body authority, or a second store from this observer miss.

## v0.6 build/package identity

- Research source: `18cfc102dce68438e4ab185160e3be795261e1c0`
- Build trigger/head: `5587b8fa34900e73fe2d6a0d43b411a025b6346c`
- Dedicated research CI: `33807128921 / 100820168958` — success
- Canonical Artifact: `9913354388`
- Artifact digest / ZIP SHA-256: `1e99499aec8d7b59489c0534c962772293259ef2e29037d314d09d9cd23b4887`
- Probe dylib SHA-256: `6c834d02d2e3a271be5b070a4e4d0027f8246237bc487cd2b24984f960a170cc` — matches sidecar; Mach-O arm64
- Official source ZIP SHA-256: `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`
- Repacked IPA SHA-256: `d09160f1dce44ad7c1b8d9e4037ad4eaf2e29b68e73424eb2a81a78921a83681`
- Outer download ZIP SHA-256: `d63385fefd79c3d0c18c003a56025ce0dec517e81601ee1320675b433e2a945a`
- Official identity preserved: `com.openai.chat` / `1.2026.202` / `30140022279`
- Exact diff vs pristine official source: three intended files only (Probe substitution, original enhancer backup, research marker)

Human Runtime v0.6 remains pending. Product b95 is unchanged and b96 remains unallocated.
