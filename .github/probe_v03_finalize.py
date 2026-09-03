from pathlib import Path


def insert_after_title(path: str, marker: str, block: str) -> None:
    p = Path(path)
    text = p.read_text()
    if marker in text:
        return
    lines = text.splitlines(keepends=True)
    if not lines or not lines[0].startswith('# '):
        raise SystemExit(f'unexpected heading: {path}')
    p.write_text(lines[0] + '\n' + block.rstrip() + '\n\n' + ''.join(lines[1:]).lstrip('\n'))


def append_once(path: str, marker: str, block: str) -> None:
    p = Path(path)
    text = p.read_text()
    if marker not in text:
        p.write_text(text.rstrip() + '\n\n' + block.rstrip() + '\n')


checkpoint_block = '''## Official iOS Probe v0.3 package-ready research override — 2026-09-04

Probe v0.2 Human Runtime remains **Inconclusive for cross-platform late-join**: its clean-log/privacy changes worked, but one failed official user WebSocket produced 195,999 repeated `NSPOSIXErrorDomain/53` receive errors and a 76 MB JSONL, materially perturbing observation. No target conversation HTTP/SSE or conversation/per-turn WebSocket event was observed, so that absence is not promoted to a protocol rejection.

Probe v0.3 changes research instrumentation only. Exact research source commit `91abb9ca95d80ea4ab646fc33effd55083e0d3ee` removes `ws.receive.arm`, records only the first repeated receive error on the same failed socket until a real message arrives, and adds privacy-safe `dataTaskWithURL:` / `dataTaskWithURL:completionHandler:` observation. No `ChatGPTClient/**`, Xcode project or product CI source changed; b95 remains the product Candidate and b96 remains unallocated.

Dedicated research CI `33793891708 / 100776808437` passed build, validation, codesign inspection and Artifact upload on trigger/source head `a80a9c287873bca8049c8b79a63c1005ca603369`. Canonical research Artifact `9908389485`, ZIP digest `sha256:d649ff697023121fad2e8d6a59f1de53f7174a2ee6f1c1bce264c9fccb081e2d`; independently verified Probe dylib `sha256:cd4294d523054109886a5026bc0c3dabcc6309d8dbcfafe3d27e2c3adec14f85`.

The exact official source ZIP remains `sha256:bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`. Repackaged TrollStore research IPA `ChatGPT-Official-RealtimeProbe-v03-TrollStore-20260904.ipa` independently verifies `sha256:3ec2645c338f25d99c9ccf94c38190994cccd8153a0846a5d76a5ca755288d61`, unchanged official identity `com.openai.chat` / `1.2026.202` / `30140022279`, valid ZIP, and exactly three expected file differences versus pristine official source: original enhancer backup added, Probe dylib substituted at the existing enhancer path, and a research marker added.

Evidence ladder for Probe v0.3: **research code written / exact research scope guard passed / dedicated research CI passed / Artifact produced / dylib and research IPA independently verified / v0.3 real-device Runtime pending.** Product evidence ladder is unchanged; Stable/Frozen Send remains No.

**Next exact action:** install exact v0.3 research IPA, fully relaunch official ChatGPT, press `清空` immediately before one deliberately long cross-platform project response, reproduce the normal official-iOS late-join behavior without extra refreshes, then export JSONL after visible join/continuation or terminal. Record separately whether the official iOS UI visibly joined the remote response. If a visually confirmed join still produces no target-correlated HTTP/SSE/WS event, only then consider the next isolated broader task-level observer; do not change product or copy official polling cadence yet.'''

state_block = '''## 2026-09-04 — official iOS Probe v0.3 research package ready

Cross-platform late-join remains the primary Send/Stream research gate. Probe v0.2 Runtime is Inconclusive because an official user-WebSocket error produced a very large repeated-receive log storm; the absence of target events in that polluted sample is not a protocol rejection. Probe v0.3 is research-only and package-verified: source `91abb9ca95d80ea4ab646fc33effd55083e0d3ee`, research CI `33793891708 / 100776808437` success, Artifact `9908389485`, dylib SHA `cd4294d523054109886a5026bc0c3dabcc6309d8dbcfafe3d27e2c3adec14f85`, research IPA SHA `3ec2645c338f25d99c9ccf94c38190994cccd8153a0846a5d76a5ca755288d61`. It deduplicates failed-socket receive logging and adds URL-form URLSession observation only. Human Runtime v0.3 is pending. b95 remains the product Candidate; b96 is unallocated; Stable/Frozen Send No.'''

tech_block = '''## DEV-send-stream Probe v0.3 observation decision — 2026-09-04

- Treat the v0.2 76 MB / 195,999-error sample as **observationally perturbed and overall Inconclusive**, not as evidence that official iOS late-join has no conversation transport.
- The next research delta is deliberately narrow: remove per-receive-arm logging, deduplicate repeated receive errors on one failed WebSocket task, and add the two URL-form `NSURLSession` data-task constructors that the exact official binary exposes but Probe v0.2 did not hook.
- Do **not** add a global task-resume hook yet. Escalate to that broader observer only if exact v0.3 visually confirms official iOS late-join while still recording no target-correlated HTTP/SSE/WebSocket acquisition event.
- Static official-iOS strings for `stream_handoff`, `resume_conversation_token`, `turn_exchange_id`, `topic`, `resume_sse_endpoint`, `ConversationResumeFetchRecovery`, and inline stream-status/fetch recovery prove native continuation/recovery machinery exists, but do not prove the active late-join branch and do not authorize product polling/cadence reproduction.
- This is research tooling only. Product ownership and b95 identity remain unchanged; b96 remains unallocated.'''

identity_block = '''## Probe v0.3 build/package identity

- Exact research source commit: `91abb9ca95d80ea4ab646fc33effd55083e0d3ee`.
- Research build trigger/source head: `a80a9c287873bca8049c8b79a63c1005ca603369`.
- Dedicated research CI: run/job `33793891708 / 100776808437` — success.
- Canonical research Artifact: `9908389485`.
- Artifact/ZIP SHA-256: `d649ff697023121fad2e8d6a59f1de53f7174a2ee6f1c1bce264c9fccb081e2d`.
- Probe dylib SHA-256: `cd4294d523054109886a5026bc0c3dabcc6309d8dbcfafe3d27e2c3adec14f85`, matching sidecar; Mach-O arm64.
- Official source ZIP SHA-256: `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`.
- Research IPA: `ChatGPT-Official-RealtimeProbe-v03-TrollStore-20260904.ipa`, SHA-256 `3ec2645c338f25d99c9ccf94c38190994cccd8153a0846a5d76a5ca755288d61`.
- Official app identity remains `com.openai.chat`, version `1.2026.202`, build `30140022279`.
- Independent pristine-package comparison: exactly three intended differences — research marker added, original enhancer backed up unchanged, and v0.3 Probe dylib placed at the enhancer injection path; no removals.
- Classification: research code/CI/Artifact/package verification Positive; v0.3 Human Runtime Pending; ChatGPTClient product unchanged; b96 unallocated.'''

insert_after_title('docs/project/current/dev/DEV-send-stream.md', 'Official iOS Probe v0.3 package-ready research override', checkpoint_block)
insert_after_title('docs/project/PROJECT_STATE.md', 'official iOS Probe v0.3 research package ready', state_block)
insert_after_title('docs/project/TECHNICAL_DECISIONS.md', 'DEV-send-stream Probe v0.3 observation decision', tech_block)
append_once('docs/project/runtime-evidence/DEV-send-stream-official-ios-probe-v02-runtime-storm-v03-plan-20260904.md', '## Probe v0.3 build/package identity', identity_block)

workflow = Path('.github/workflows/research-official-ios-realtime-probe.yml')
text = workflow.read_text()
text = text.replace('\n# Probe v0.3 source anchor: 91abb9ca95d80ea4ab646fc33effd55083e0d3ee\n', '\n')
workflow.write_text(text)

temporary = [
    '.github/official-ios-probe-v02-docs.patch',
    '.github/official-ios-probe-v02-fixup.patch',
    '.github/official-ios-probe-v02.patch',
    '.github/probe_v02_apply.py',
    '.github/probe_v03_apply.py',
    '.github/probe_v03_finalize.py',
    '.github/workflows/official-ios-probe-v02-apply.yml',
    '.github/workflows/official-ios-probe-v02-finalize.yml',
    '.github/workflows/official-ios-probe-v03-checkpoint.yml',
    '.github/workflows/official-ios-probe-v03-apply.yml',
    '.github/workflows/official-ios-probe-v03-finalize.yml',
]
for item in temporary:
    p = Path(item)
    if p.exists():
        p.unlink()
