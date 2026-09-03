from pathlib import Path

CHECKPOINT = Path('docs/project/current/dev/DEV-send-stream.md')
PROJECT_STATE = Path('docs/project/PROJECT_STATE.md')
EVIDENCE = Path('docs/project/runtime-evidence/DEV-send-stream-official-ios-probe-v05-runtime-v06-callback-surface-20260904.md')


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected exactly 1 match, got {count}')
    return text.replace(old, new, 1)

identity = '''Exact v0.6 research identity: source `18cfc102dce68438e4ab185160e3be795261e1c0`; build trigger/head `5587b8fa34900e73fe2d6a0d43b411a025b6346c`; dedicated research CI `33807128921 / 100820168958` passed; canonical Artifact `9913354388`; Artifact digest / independently recomputed ZIP SHA `sha256:1e99499aec8d7b59489c0534c962772293259ef2e29037d314d09d9cd23b4887`; Probe dylib `sha256:6c834d02d2e3a271be5b070a4e4d0027f8246237bc487cd2b24984f960a170cc` matching sidecar. Against official source ZIP `sha256:bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`, repacked `ChatGPT-Official-RealtimeProbe-v06-TrollStore-20260904.ipa` is `sha256:d09160f1dce44ad7c1b8d9e4037ad4eaf2e29b68e73424eb2a81a78921a83681`; outer download ZIP is `sha256:d63385fefd79c3d0c18c003a56025ce0dec517e81601ee1320675b433e2a945a`. Package preserves `com.openai.chat` / `1.2026.202` / `30140022279`, passes ZIP integrity, and differs from pristine source in exactly three intended files.\n\n'''

c = CHECKPOINT.read_text()
old = 'Evidence ladder: **Probe v0.5 package verified / Native Detail polling Runtime Positive again / v0.5 async-status callback coverage Runtime Negative / async-status semantics Unverified / v0.6 research source next / product remains b95 / b96 unallocated / Stable-Frozen Send No.**\n\n**Next exact action:** build/package exact Probe v0.6 and run one clean long cross-platform response after `清空`. Decisive v0.6 evidence is `probe.detail_task_callback_surface`; use only an evidenced callback signature from that output for any later response-state observer. Do not allocate b96 yet, and do not add Native polling/resume/timer/retry/watchdog/duplicate Send or a second response store from the callback-coverage miss.\n'
new = identity + 'Evidence ladder: **Probe v0.5 Runtime analyzed / Native Detail polling Runtime Positive again / v0.5 async-status callback coverage Runtime Negative / Probe v0.6 code + dedicated CI + Artifact + package verified / v0.6 Human Runtime pending / product remains b95 / b96 unallocated / Stable-Frozen Send No.**\n\n**Next exact action:** Human Runtime exact Probe v0.6. Fully relaunch the official research app, press `清空`, run one deliberately long cross-platform response, and export JSONL after the first target Detail task appears. Decisive evidence is the single `probe.detail_task_callback_surface` event; use only an evidenced callback signature from that output for any later response-state observer. Do not allocate b96 yet.\n'
c = replace_once(c, old, new, 'checkpoint package state')
CHECKPOINT.write_text(c)

p = PROJECT_STATE.read_text()
old_state = '- Probe v0.6 is research-only and records one bounded callback-surface snapshot from the first target Detail task (relevant selector/ivar names and type signatures only). It installs no guessed private callback hook and reads no content/auth. Product remains b95; b96 remains unallocated.\n'
new_state = '- Probe v0.6 is research-only and records one bounded callback-surface snapshot from the first target Detail task (relevant selector/ivar names and type signatures only). It installs no guessed private callback hook and reads no content/auth. Dedicated research CI `33807128921 / 100820168958` passed; Artifact `9913354388`; dylib SHA `6c834d02d2e3a271be5b070a4e4d0027f8246237bc487cd2b24984f960a170cc`; repacked IPA SHA `d09160f1dce44ad7c1b8d9e4037ad4eaf2e29b68e73424eb2a81a78921a83681`; outer ZIP SHA `d63385fefd79c3d0c18c003a56025ce0dec517e81601ee1320675b433e2a945a`. Human Runtime pending. Product remains b95; b96 remains unallocated.\n'
p = replace_once(p, old_state, new_state, 'project state package identity')
PROJECT_STATE.write_text(p)

e = EVIDENCE.read_text()
append = '''\n## v0.6 build/package identity\n\n- Research source: `18cfc102dce68438e4ab185160e3be795261e1c0`\n- Build trigger/head: `5587b8fa34900e73fe2d6a0d43b411a025b6346c`\n- Dedicated research CI: `33807128921 / 100820168958` — success\n- Canonical Artifact: `9913354388`\n- Artifact digest / ZIP SHA-256: `1e99499aec8d7b59489c0534c962772293259ef2e29037d314d09d9cd23b4887`\n- Probe dylib SHA-256: `6c834d02d2e3a271be5b070a4e4d0027f8246237bc487cd2b24984f960a170cc` — matches sidecar; Mach-O arm64\n- Official source ZIP SHA-256: `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`\n- Repacked IPA SHA-256: `d09160f1dce44ad7c1b8d9e4037ad4eaf2e29b68e73424eb2a81a78921a83681`\n- Outer download ZIP SHA-256: `d63385fefd79c3d0c18c003a56025ce0dec517e81601ee1320675b433e2a945a`\n- Official identity preserved: `com.openai.chat` / `1.2026.202` / `30140022279`\n- Exact diff vs pristine official source: three intended files only (Probe substitution, original enhancer backup, research marker)\n\nHuman Runtime v0.6 remains pending. Product b95 is unchanged and b96 remains unallocated.\n'''
if '## v0.6 build/package identity' in e:
    raise SystemExit('evidence package section already exists')
EVIDENCE.write_text(e + append)
