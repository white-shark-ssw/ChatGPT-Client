from pathlib import Path

CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
MARKER = "## Official iOS Probe v0.8 Stop evidence preflight"

section = r'''## Official iOS Probe v0.8 Stop evidence preflight — 2026-09-07

Purpose: close the remaining Phase 9 server-Stop evidence gate without changing ChatGPTClient product bits or allocating a product Candidate.

Exact recovery baseline:

- Owning Work: `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 remains open against unchanged `main@94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Exact preflight product remains canonical b115: product `2346c2d4ab26d40ef720b7850ae34316acb3cc62`, package `2dc0a4155f3549f32b1b08a9e4d8e6fb87495692`, Artifact `9992196070`. No b116 is allocated.
- Branch baseline before this research chain was `a6efef0c4974868822fa11cf95e6c6e9cb9939f5`; later preflight workflow/script commits are research/tooling only.
- Parallel PR #35 explicitly does not touch `scripts/research/official_ios_realtime_probe/**`; source-scope conflict is absent. Its research IPA shares the official bundle identity and must not be installed concurrently on the same device during this Stop capture.

Evidence already available:

- Static decrypted-official-app evidence identifies `StopConversationRequest`, `/stop_conversation`, `stopConversation(id:requestTrackingData:)` and `clearAsyncStatus(for:)`, but static strings do not prove request method/body/target/ack/terminal semantics.
- Current Probe v0.7 already observes privacy-safe HTTP method/path/status/JSON key structure, hooks `NSURLSessionTask.resume` for Swift-async-created tasks, and has a Runtime-evidenced `_task_onqueue_didReceiveDispatchData:completionHandler:` response-byte observer. No new guessed transport hook is required.
- Current v0.7 path classification does not distinguish exact `/stop_conversation` from generic Conversation Detail, and its dispatch-data observer only extracts `conversation_async_status`. One exact Stop-only structural extension is justified.

Research v0.8 authorized scope:

- Change only `scripts/research/official_ios_realtime_probe/ChatGPTRealtimeProbe.m`, its README, and the dedicated research workflow only if a build marker/validation update is required.
- Classify exact `/backend-api/conversation/<opaque>/stop_conversation` separately as `conversation_stop`.
- On the existing task-resume request observation, emit a Stop-only structural event containing safe path shape, method, top-level request JSON keys, each key's value class, and irreversible short hashes only for opaque string identifiers where needed. Never emit raw IDs, prompt/answer/reasoning/tool text, Cookie/Authorization or arbitrary request body bytes.
- On the already-evidenced dispatch-data callback and ordinary response/completion surfaces, emit Stop-only response status/MIME/body-byte count and JSON top-level key/value-class structure. Do not persist raw response content.
- The observer must not initiate Stop, Detail, polling, retry, resume, timer/watchdog, or any network request. It observes only traffic the official app itself creates.

Batch plan:

- **R0 (this preflight)**: durably record the recovery baseline and authorized v0.8 scope before source modification.
- **R1**: apply exact research-only v0.8 source/README delta and run dedicated macOS research CI; record exact source/run/job/Artifact/dylib SHA.
- **R2 Human Runtime**: install only the exact v0.8 official research package, clear its log, start one deliberately long response in the official app, invoke the official Stop control exactly once while active, wait for UI settlement, export JSONL. Required evidence is exact method/path/request key/value structure plus response status/structure and the official app's existing post-Stop Detail/async-status/terminal behavior.
- **R3 product**: only if R2 supplies sufficient Stop semantics may a new unique product Candidate be allocated. That later Candidate may also include the already-deferred stable-menu-host correction; the menu issue alone remains insufficient to allocate a build.

Do not replay completed b115 batches, modify PR #35, modify `ChatGPTClient/**`, Xcode build identity, `ios-foundation.yml`, protected Send/SSE/recovery ownership, or synthesize any server Stop before R2 evidence.

**Next exact action:** complete R1 research-only v0.8 source + dedicated CI. Product remains b115 / Human Runtime Partial / Stable-Frozen No.
'''

text = CHECKPOINT.read_text()
if MARKER not in text:
    CHECKPOINT.write_text(section + "\n" + text)
