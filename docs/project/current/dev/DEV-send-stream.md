# DEV-send-stream

## Status

**Active — `DEV-send-stream-0.1.0-b80` / `0.1.0 (80)` is now a formally built and independently verified Runtime candidate. Exact product source, Push CI, PR CI, canonical IPA and package identity are all verified. Runtime/manual/real-device remains Pending. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / unmerged
- Current `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Exact b80 product/config source: `b0f51041c2d7b645f152752ea6196526b2e4e0f6`
- Candidate / Version-Build: `DEV-send-stream-0.1.0-b80` / `0.1.0 (80)`
- Canonical Push Artifact: `9801761448`
- IPA: `ChatGPTClient-0.1.0-b80-dev-send-stream.ipa`
- IPA SHA-256: `87c360175a4adc4fa476383b395cffe74c57c5e75db252dd49acdf42be39ce1f`
- b39-b80 permanently reserved
- b80 Runtime/manual/real-device: **Pending**
- Stable/Frozen Send: **No**

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b79-device-runtime-20260901.md`
- `docs/project/runtime-evidence/DEV-send-stream-account-wide-web-notification-20260901.md`
- `docs/project/runtime-evidence/DEV-send-stream-b80-build-artifact-20260901.md`

Do not allocate b81 until b80 Runtime is classified.

## Resume / identity / conflict guard

The post-interruption full resume guard was completed before b80 formalization:

- feature branch / PR identity matched the selected Work;
- `docs/project/current/dev/` contained no second Active Work owner;
- b80 remained uniquely allocated;
- `main` had advanced to `94f0c5777dad262cd1fb22be49082dbd92c962f2`, but compare from the previously recorded main showed only `docs/project/COMPOSER_PARITY_PLAN.md` as a net changed file;
- no b80 product/config path or Send state owner overlapped, so the main drift did not invalidate the validated b80 patch.

## b80 formalization recovery chain — completed through Artifact

The non-atomic recovery chain recorded before formalization has now completed through the Artifact/package-verification milestone.

Completed deterministic batches:

1. recovery checkpoint established at `81e322c7e626a63048a1b303891a0c3efd87e83b`;
2. one exact four-file product/config tree was created and formalized as `b0f51041c2d7b645f152752ea6196526b2e4e0f6`;
3. branch fast-forwarded without force;
4. exact formal commit verified to change only:
   - `.github/workflows/ios-foundation.yml`
   - `ChatGPTClient.xcodeproj/project.pbxproj`
   - `ChatGPTClient/Conversation/ConversationFeature.swift`
   - `ChatGPTClient/RootViewController.swift`
5. Push CI passed;
6. PR CI passed;
7. canonical Push Artifact downloaded and independently verified;
8. durable b80 build/artifact evidence written.

No product retry/fallback/timer/watchdog or unrelated refactor was introduced.

## Exact b80 product scope

The formal source implements only the evidence-backed scope:

1. **Final timeline/tool -> reasoning-divider spacing** — the terminal expanded-timeline boundary now uses the same neutral separator representation instead of a separate pre-divider spacing owner; the 36-point tool line height was not increased.
2. **Normal external COMPLETE materialization gate** — when page-owned `complete=true` arrives while `reasoningEnded == true` and `finalText` is still empty, Native keeps the same covered observation alive instead of terminalizing/releasing immediately.
3. **Bridge ownership correction** — page-owned external observation state is no longer cleared merely because the first COMPLETE-associated plural snapshot was posted; Native release remains the terminal owner.
4. **Identity-only b80 changes** — Xcode Build/Candidate and workflow artifact identity moved from b79 to b80.

Explicitly excluded and still excluded:

- account-wide haptic / automatic Sync implementation;
- timer/poll/retry/watchdog;
- duplicate Sync/Send;
- fake progressive final/typewriter;
- DOM-body or WebSocket-body authority;
- Native resume/offset synthesis;
- second response owner;
- Composer work or unrelated refactor.

## Validation / Artifact evidence

Guarded assembly run `33506668882`:

- exact patch application: **Passed**
- exact-scope / prohibited-pattern / static guard: **Passed**
- Xcode 16.4 Simulator build: **Passed**

Formal exact source `b0f51041c2d7b645f152752ea6196526b2e4e0f6`:

- Push run `33511327452`: **success**
- PR run `33511332786`: **success**
- canonical Push Artifact `9801761448`
- Artifact ZIP SHA-256: `0d6a5ddfa3c05d956708e43fb91acd6bb19988198a5a3cf34e6b72e289091db9`
- IPA SHA-256: `87c360175a4adc4fa476383b395cffe74c57c5e75db252dd49acdf42be39ce1f`

Independent built-package inspection:

- Release: `0.1.0`
- Build: `80`
- Candidate: `DEV-send-stream-0.1.0-b80`
- Source marker: `b0f51041c2d7`
- Build configuration: `Release`
- Deployment target / Minimum OS: `14.0`
- Executable: Mach-O 64-bit `arm64`

Evidence classification:

- Code written: **Yes**
- Static/local/Simulator checks: **Passed**
- Push CI: **Passed**
- PR CI: **Passed**
- Artifact produced: **Yes**
- Package identity verified: **Yes**
- Runtime/manual/real-device: **Pending**
- Stable/Frozen: **No**

CI and Artifact success are not Runtime proof.

## Retained b79 Runtime findings to verify against b80

- Tool presentation was partial-positive / rejected because final timeline/tool -> divider spacing remained asymmetric.
- Manual-Sync external re-arm was Runtime positive and must remain positive.
- External stopped-thinking semantics were Runtime positive and must remain positive.
- External reasoning/tools remain page-snapshot granular, not token/SSE-delta granular.
- Progressive external final token streaming remains unavailable from the currently authorized source.
- b79 had a proven COMPLETE/final-materialization race: page COMPLETE could arrive while reasoning ended but final text was still empty, causing early terminal/release and a missed later final until another manual Sync.

## Account-wide official completion/new-answer signal boundary

User Runtime evidence supports an account-wide official new-answer/completion signal: official iOS can haptically signal another conversation and official PC Web can remain on A while never-opened B completes and still show an upper-right new-answer notification.

Exact transport/mechanism/schema/conversation identity/covered-WKWebView/background semantics remain **Unknown / Unverified**. This was deliberately excluded from b80. Do not infer WebSocket/APNs/service-worker semantics or imitate it with polling/timers.

## Next exact action — Human Runtime Gate

Install and test the exact b80 IPA. Verify:

1. **Spacing:** final tool/timeline -> reasoning-divider spacing is now visually symmetric/acceptable.
2. **Normal remote completion:** start a sufficiently long response from another platform; when the page reaches COMPLETE before final materialization, the client must keep observing and the eventual final answer must appear without requiring another manual Sync.
3. **Stopped-thinking regression:** external stopped-thinking still preserves reasoning/tools instead of promoting reasoning into normal final body text.
4. **Manual-Sync re-arm regression:** when a changed latest user turn is discovered by explicit Sync, the same covered page can still re-arm/reload once and adopt page-owned reasoning/tool snapshots.

Progressive final token streaming remains an open protocol gap and is **not** claimed fixed by b80.

After the exact b80 Runtime result is supplied, classify b80 first. Only then decide whether b81 is necessary. Separately, the account-wide Web signal probe remains future evidence work after b80 classification.
