from pathlib import Path

CHECKPOINT = Path('docs/project/current/dev/DEV-send-stream.md')
STATE = Path('docs/project/PROJECT_STATE.md')
WORKFLOW = Path('.github/workflows/research-official-ios-realtime-probe.yml')


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected exactly 1 match, got {count}')
    return text.replace(old, new, 1)

c = CHECKPOINT.read_text()
old = '''Evidence ladder after this source commit: **v0.5 research code written; dedicated research CI/Artifact/package pending; Human Runtime pending; product b95 unchanged; b96 unallocated; Stable/Frozen Send No.**\n\n**Next exact action:** run the existing dedicated research Probe CI for exact v0.5 source, package the verified dylib into the exact official source ZIP, independently verify IPA identity/diff/hash, then Human Runtime one long cross-platform response after `清空`. The decisive log is target-correlated `http.conversation_detail.async_status` transitioning from `is_streaming` to `complete` (or another explicitly observed safe enum). Do not allocate b96 before that result.\n'''
new = '''Exact v0.5 research identity: source `b5b48ac67c09f39b0a40666ad9574cfa389b900b`; build trigger/head `689230554240407cab878e5ffa70c5a4dad1b865`; dedicated research CI `33803516248 / 100808374551` passed build, Mach-O/codesign inspection and Artifact upload; canonical Artifact `9911983067`; Artifact digest `sha256:97d7b854ceda48afaff8efaac387e72af56812a256d5e96477cbfc9b6dd413ce`; independently verified Probe dylib `sha256:731ebdf5716cb321fa0f0047fadbc6ccc1a628e4fb4b17d162613e156e75b92e` matching its sidecar. Against exact official source ZIP `sha256:bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`, repacked `ChatGPT-Official-RealtimeProbe-v05-TrollStore-20260904.ipa` is `sha256:f53dfc8532738dbccfe80e24dc62fe1728abe0dcd57ce6a3cd015655378da86d`, preserves `com.openai.chat` / `1.2026.202` / `30140022279`, passes ZIP integrity, and differs from pristine official source in exactly three intended files: original enhancer backup, Probe dylib substitution, and research marker.\n\nEvidence ladder: **v0.5 research code written / guarded research-only scope passed / dedicated research CI passed / Artifact produced / dylib and research IPA independently verified / Human Runtime pending; product b95 unchanged; b96 unallocated; Stable/Frozen Send No.**\n\n**Next exact action:** Human Runtime exact v0.5. Fully relaunch the official research app, press `清空` immediately before one deliberately long cross-platform project response, let official iOS visibly show batched progression through terminal if possible, then export JSONL. The decisive evidence is same-target `http.conversation_detail.async_status` showing the authoritative active-to-terminal contract (`is_streaming` -> `complete`, or another explicitly observed safe enum). Do not allocate b96 before that result.\n'''
c = replace_once(c, old, new, 'checkpoint package block')
CHECKPOINT.write_text(c)

s = STATE.read_text()
block = '''## 2026-09-04 — Probe v0.5 packaged / Detail async-status Human Runtime gate\n\n- Cross-platform late-join remains primary. v0.4 Runtime observed same-target authoritative Conversation Detail GETs at ~9.7s median and user separately recalls official iOS updates arriving in blocks rather than SSE-like token flow.\n- Probe v0.5 is research-only: it retains task-resume observation and adds privacy-safe observation of only the exact `conversation_async_status` enum from Conversation Detail response chunks via `URLSession:dataTask:didReceiveData:`. It logs no content/auth and initiates no network request.\n- Exact source `b5b48ac67c09f39b0a40666ad9574cfa389b900b`; research CI `33803516248 / 100808374551` success; Artifact `9911983067`; digest `sha256:97d7b854ceda48afaff8efaac387e72af56812a256d5e96477cbfc9b6dd413ce`; dylib SHA `731ebdf5716cb321fa0f0047fadbc6ccc1a628e4fb4b17d162613e156e75b92e`; research IPA SHA `f53dfc8532738dbccfe80e24dc62fe1728abe0dcd57ce6a3cd015655378da86d`; official identity unchanged and exact diff vs pristine source is three intended files.\n- Human Runtime must now prove Detail active/terminal state on the same target. Product remains exact b95; b96 remains unallocated; Stable/Frozen Send No.\n\n'''
if block.splitlines()[0] in s:
    raise SystemExit('project state block already exists')
if not s.startswith('# Project State\n\n'):
    raise SystemExit('project state header mismatch')
s = s.replace('# Project State\n\n', '# Project State\n\n' + block, 1)
STATE.write_text(s)
