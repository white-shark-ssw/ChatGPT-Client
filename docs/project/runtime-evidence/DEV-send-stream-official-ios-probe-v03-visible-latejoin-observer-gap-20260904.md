# DEV-send-stream — official iOS Probe v0.3 visible late-join / observer gap — 2026-09-04

## Human Runtime input

- JSONL SHA-256: `a9965b3a7a693bd6d1f6d9a62d55249b97275db9fd49f581008feefb3bd24047`
- Size: 3,465 bytes
- Parsed events: 15
- Parse errors: 0
- Probe version: `0.3`
- First event: `probe.log_cleared`
- User explicitly confirms the official iPhone visibly joined and continued the cross-platform response.

## Observed timeline

After the clear marker, the existing official user WebSocket emitted background presence and received a reply. At `19:13:28.944Z` receive failed with `NSPOSIXErrorDomain / 53`; the corresponding WebSocket task completed with status 101/error 53. A foreground presence send immediately afterward also failed. At `19:16:02.044Z` the Probe loaded again, hooks reinstalled, and a new ordinary user WebSocket was created; it sent `connect` plus the same base subscriptions (`app_notifications`, `push_auth_challenge`, `calpico-chatgpt`) and received reply frames.

Across the full clean sample there are zero target conversation hashes, zero conversation/per-turn WebSocket subscribe/update frames, and zero conversation Detail/status/resume/SSE HTTP events. Yet the user visibly observed successful cross-platform continuation.

## Classification

- Official iOS cross-platform late-join capability: **Runtime Positive**.
- Direct ordinary user-WebSocket conversation subscription as observed by v0.3: **not supported by this sample**.
- v0.3 public URLSession constructor/delegate coverage as sufficient to reveal acquisition: **Rejected**.
- Exact acquisition transport/path: **Unverified / unseen**.

This combination proves an observation gap. It does not justify guessing a polling cadence or promoting any WebSocket body to product content authority.

## Next exact gate

Use exact Probe v0.4, which adds one privacy-safe `http.task.resume` record per relevant NSURLSessionTask, including tasks internally created by Swift async URLSession. Repeat one visually confirmed cross-platform long-response join from a cleared log and identify the earliest target-correlated task/path before terminal. No ChatGPTClient b96/product change until that path is observed.

Exact v0.4 research identity: source `db3f8a7d01f39f364f6166cf72245db426cadef1`; build head `ce43a7fc3fb4f581dd7614bac541c44dff8af512`; research CI `33795191324 / 100781074234` success; Artifact `9908872470`; Artifact digest `sha256:29675f185f8b0919821e6fdb44a3cc4ff3673187c346dd00e1f45fc3f47a8ccc`; dylib SHA `cc6a2b29b19441f56f214b199e5e7512c1739b3ae8563bc7968c0eb26779ecf9`; research IPA SHA `b4c0e53ea07bea92787ef7186b5ad79e1aa5f7bb52ebd2c2272e7060261d3d6e`.
