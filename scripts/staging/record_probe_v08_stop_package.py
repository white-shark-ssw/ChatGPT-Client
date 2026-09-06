from pathlib import Path

FILES = {
    "checkpoint": Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md"),
    "state": Path("docs/project/PROJECT_STATE.md"),
    "module": Path("docs/project/MODULE_STATUS.md"),
    "profile": Path("docs/project/PROJECT_PROFILE.md"),
    "decisions": Path("docs/project/TECHNICAL_DECISIONS.md"),
    "preflight": Path("docs/project/SEND_STREAM_PREFLIGHT.md"),
}


def prepend_once(path: Path, marker: str, section: str) -> None:
    text = path.read_text()
    if marker not in text:
        path.write_text(section.rstrip() + "\n\n" + text)

checkpoint = '''## Official iOS Probe v0.8 Stop structural observer — package ready 2026-09-07

R1 research-only evidence is complete; ChatGPTClient product remains exact b115 and **b116 remains unallocated**.

Canonical v0.8 research identity:

- Recovery/preflight recorded before research source modification; v0.8 changes only `scripts/research/official_ios_realtime_probe/ChatGPTRealtimeProbe.m` + its README. No `ChatGPTClient/**`, product Xcode identity, `ios-foundation.yml`, Send/SSE/recovery or PR #35 file is changed by the v0.8 source delta.
- Exact v0.8 source commit `644a31c012f4d832ab581aa7766c3ec365ce155b` (`research: observe official stop structure`).
- macOS staging/build `34052999350 / 101539827776` passed b115/no-b116 guards, exact research scope, `git diff --check`, privacy markers, iPhoneOS arm64 dylib compile, Mach-O/otool/codesign validation, exact research source commit/push and Artifact upload.
- Canonical research Artifact `9995116883`, name `ChatGPTRealtimeProbe-v08-644a31c012f4d832ab581aa7766c3ec365ce155b`; GitHub digest and independently recomputed Artifact ZIP SHA-256 both `04e3b4b84e48bf709f66ae046125082df71a26b185bd290ec086d3a8a3d397cc`.
- `ChatGPTRealtimeProbe.dylib` SHA-256 `51eb111a1ff8bfcc674eb5946f141918d74f7b4eb661b49c7892e8d5b2e221c1`, matching the Artifact sidecar; Mach-O arm64 dynamic library.
- Exact user-supplied decrypted official package baseline remains SHA-256 `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`.
- Repacked TrollStore research IPA `ChatGPT-Official-RealtimeProbe-v08-TrollStore-20260907.ipa` SHA-256 `0d4da358c7b14eff52374627b9bb5ee3313cbb4e0fca48e8039a6493ced8d9f5`; ZIP integrity passes; bundle identity remains `com.openai.chat / 1.2026.202 / 30140022279`, MinimumOSVersion 17.0.
- Package diff against the exact baseline is exactly: **two added paths** (`ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.original.dylib` and `ChatGPTRealtimeProbe-v08.json`), **zero removed paths**, **one modified path** (`ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib`, replaced by exact Probe dylib). Both enhancer dylib entries are mode 0755. Original enhancer backup SHA-256 `aae66c63a7122d301be5025305b92ec63b8da020fdceef22df9bec7cc1acc7b3`.

Exact v0.8 observation behavior:

- Separately classifies `/backend-api/conversation/<opaque>/stop_conversation` as `conversation_stop` rather than generic Detail.
- Existing Runtime-evidenced `NSURLSessionTask.resume` observation emits Stop-only request structure: method/path shape, request JSON keys, top-level value classes and irreversible 12-hex SHA-256 prefixes only for identifier-like top-level string fields. It never logs raw identifiers or body bytes as content.
- Existing Runtime-evidenced dispatch-data callback plus ordinary response/completion surfaces emit Stop-only status/MIME/body-byte count and top-level response JSON key/value-class structure when available. Raw response content is never persisted.
- v0.8 initiates no request, Stop, Detail, polling, timer, retry, resume or watchdog. It only observes traffic produced by the official iOS app.

R2 Human Runtime gate:

1. Install only the exact v0.8 official research IPA. Do not install/use PR #35's official Sync/Reload inspector at the same time because both preserve the same official bundle ID.
2. Fully terminate/relaunch official ChatGPT, press Probe `清空`, open one ordinary existing conversation, and start one deliberately long response from official iOS.
3. While visibly generating/reasoning, invoke the official **Stop** control exactly once. Do not manually refresh, issue another Stop, or trigger unrelated navigation until the UI settles.
4. Wait briefly for the official app's own post-Stop Detail/async-status/terminal traffic, then export only `ChatGPTRealtimeProbe.jsonl`.
5. Required acceptance evidence before product Stop implementation: exact Stop method/path/request key+value structure and target identity relationship; server HTTP acknowledgement/response structure; post-Stop authoritative Detail/async-status/terminal behavior; whether partial response remains authoritative. No product Stop is authorized from static strings alone.

Deferred b115 menu persistence issue remains bundled for the next independently justified product Candidate. If R2 provides sufficient Stop semantics, that later Stop Candidate may include the stable-menu-host correction in the same exact product scope.

**Evidence ladder:** v0.8 research Code written / exact research scope + dedicated macOS build passed / Artifact produced / dylib + official research IPA independently verified / Stop Human Runtime pending; ChatGPTClient remains b115 Human Runtime Partial / b116 unallocated / Stable-Frozen No.

**Next exact action:** Human Runtime exact v0.8 official Stop once, export JSONL. Do not allocate product b116 until the Stop protocol evidence is sufficient.
'''
prepend_once(FILES["checkpoint"], "## Official iOS Probe v0.8 Stop structural observer — package ready", checkpoint)

state = '''## DEV-send-stream Stop evidence gate — Probe v0.8 package ready 2026-09-07

- Phase 9 remaining true product gap is response-scoped server Stop; conditional b107 clean-EOF / b101 -1005 / b98 WebContent-death events remain evidence debts and are not manufactured as closeout blockers.
- Research-only Probe v0.8 exact source `644a31c012f4d832ab581aa7766c3ec365ce155b`, CI `34052999350/101539827776`, Artifact `9995116883`, dylib SHA `51eb111a1ff8bfcc674eb5946f141918d74f7b4eb661b49c7892e8d5b2e221c1` is package-qualified for exact official `/stop_conversation` structural observation.
- Official research IPA SHA `0d4da358c7b14eff52374627b9bb5ee3313cbb4e0fca48e8039a6493ced8d9f5` preserves official identity and differs from the supplied baseline only by Probe substitution, original-enhancer backup and marker.
- Product remains canonical b115; no b116 allocation. Deferred top-right menu persistence defect remains queued to bundle with the next independently justified product Candidate, preferably Stop if Runtime evidence authorizes it.
'''
prepend_once(FILES["state"], "## DEV-send-stream Stop evidence gate — Probe v0.8 package ready", state)

module = '''## Send / Stream — Probe v0.8 Stop evidence gate 2026-09-07

- Production response ownership remains b115. Server Stop is not implemented yet because exact method/body/target/ack/partial-content semantics were previously unproven.
- Probe v0.8 now provides a research-only, privacy-safe observer for exact official `/stop_conversation` request/response structure without initiating any traffic. Source `644a31c012f4...`, research Artifact `9995116883`, dylib SHA `51eb111a...`, official research IPA SHA `0d4da358...`.
- Next gate is one official-iOS real Stop Runtime capture. Do not synthesize Stop or allocate a product build before that result.
'''
prepend_once(FILES["module"], "## Send / Stream — Probe v0.8 Stop evidence gate", module)

profile = '''## Current DEV-send-stream Stop research identity — 2026-09-07

- Product remains `DEV-send-stream-0.1.0-b115` / Build115; b116 is unallocated.
- Current research-only official probe is v0.8 source `644a31c012f4d832ab581aa7766c3ec365ce155b`, Artifact `9995116883`, dylib SHA `51eb111a1ff8bfcc674eb5946f141918d74f7b4eb661b49c7892e8d5b2e221c1`, TrollStore research IPA SHA `0d4da358c7b14eff52374627b9bb5ee3313cbb4e0fca48e8039a6493ced8d9f5`.
- Purpose is exact official server-Stop protocol observation only; Human Runtime pending. Stable/Frozen No.
'''
prepend_once(FILES["profile"], "## Current DEV-send-stream Stop research identity", profile)

decision = '''## 2026-09-07 — Server Stop must be Runtime-evidenced; Probe v0.8 is observer-only

Decision: keep ChatGPTClient product at b115 while a research-only official-iOS Probe observes the exact `/stop_conversation` request/response structure. Static symbols (`StopConversationRequest`, `/stop_conversation`, `stopConversation(id:requestTrackingData:)`) authorize observation but not a guessed product implementation. Probe v0.8 may record only method/path shape, JSON key/value classes, hashed identifier relationships, status/MIME and response key/value structure. It may not initiate Stop or any request. Product Stop can be implemented only after one exact official Stop Runtime captures enough target/ack/terminal semantics. The deferred b115 menu-host persistence fix may be bundled with that future justified product Candidate; it does not independently justify a build.
'''
prepend_once(FILES["decisions"], "## 2026-09-07 — Server Stop must be Runtime-evidenced; Probe v0.8 is observer-only", decision)

preflight = '''## Current Stop evidence gate — Probe v0.8 package ready 2026-09-07

- Static official-app symbols prove only existence of `StopConversationRequest`, `/stop_conversation`, `stopConversation(id:requestTrackingData:)`; they do not prove the production contract.
- Exact research-only Probe v0.8 source `644a31c012f4d832ab581aa7766c3ec365ce155b` / CI `34052999350/101539827776` / Artifact `9995116883` is now package-qualified to observe exact official Stop structure without initiating traffic.
- Human Runtime must capture one official Stop while a response is active and provide: request method/path, request key/value structure and hashed target relationship; HTTP acknowledgement/response structure; official post-Stop authoritative Detail/async-status/terminal behavior and partial-content authority.
- Until that evidence exists, server Stop remains unimplemented. Product stays b115 and b116 remains unallocated.
'''
prepend_once(FILES["preflight"], "## Current Stop evidence gate — Probe v0.8 package ready", preflight)
