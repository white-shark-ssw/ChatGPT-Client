from pathlib import Path

index = Path('docs/project/BUILD_TEST_INDEX.md')
lines = index.read_text().splitlines()
b85_prefix = '| `DEV-send-stream-0.1.0-b85` |'
b86_prefix = '| `DEV-send-stream-0.1.0-b86` |'
b85_row = '| `DEV-send-stream-0.1.0-b85` | `DEV-send-stream` | `0.1.0 (85)` | exact product/config source `ec64dd170a6386612af8cb68b394045ce3c85313`; clean Push CI/package head `6be1e8a8bafa80ef09c6fcebff014006de264e0f`; PR #29 | Push `33564141168/100043319389`; PR `33564179303/100043444613`; canonical Artifact `9822441595`; ZIP `sha256:0e32a52f91cb8580b91451d97d37696073fb4ee57c5df3918897aab69700ba48`; IPA `sha256:f03f5d657cbf71772d197fcea969cafb73d249c2dcc3dd2feb72e139d6e9cf61`; package Release/source `6be1e8a8bafa`/iOS14/arm64 | Runtime Partial Positive / MVP continuation Rejected: explicit Sync projected authoritative timeline `1 -> 5 -> 7` on one external response generation and final authoritative materialization reconciled correctly; no page-owned streaming/snapshot/resume event occurred between Sync actions, so every newer block required another explicit Sync | **Manual block Runtime Positive / automatic continuation rejected for reliability; permanently reserved** |'
b86_row = '| `DEV-send-stream-0.1.0-b86` | `DEV-send-stream` | `0.1.0 (86)` | exact diagnostics product source `dc77a94be5b2f7eecd822480f759358ad6a0ad25`; clean Push CI/package head `f90caca0419f13254567485171fac7d970aa8c95`; PR #29 | Push `33566939415/100052171917`; PR `33566968066/100052259409`; canonical Artifact `9823485856`; ZIP `sha256:cdccdcd034964b99e98e62c2e79a9bece96c190138c774e6f1590896d54fbacb`; IPA `sha256:25d483ac31473b124e6ad555b79c488e78da91ec1761ee8a40076b6e978bee6f`; package Release/source `f90caca0419f`/iOS14/arm64 | Runtime Pending: diagnostics-only candidate logs matching page-owned `stream_status` request/response state and matching resume offset structure without adding any request or behavior change | **Code/guarded staging/Push+PR CI/Artifact/package verified; Runtime Pending; permanently reserved** |'
b85_indexes = [i for i, line in enumerate(lines) if line.startswith(b85_prefix)]
if len(b85_indexes) != 1:
    raise SystemExit(f'b85 row count {len(b85_indexes)}')
i = b85_indexes[0]
lines[i] = b85_row
b86_indexes = [j for j, line in enumerate(lines) if line.startswith(b86_prefix)]
if len(b86_indexes) > 1:
    raise SystemExit(f'b86 row count {len(b86_indexes)}')
if not b86_indexes:
    lines.insert(i, b86_row)
else:
    lines[b86_indexes[0]] = b86_row
index.write_text('\n'.join(lines) + '\n')

module = Path('docs/project/MODULE_STATUS.md')
text = module.read_text()
start = '## DEV-send-stream b85 candidate override — 2026-09-02\n'
end = '## DEV-send-stream b82 Runtime override — 2026-09-02\n'
if start not in text or end not in text:
    raise SystemExit('MODULE_STATUS b85/b82 override markers missing')
pre, rest = text.split(start, 1)
_, post = rest.split(end, 1)
replacement = '''## DEV-send-stream b86 diagnostics / b85 Runtime override — 2026-09-02

- b85 identity: exact product source `ec64dd170a6386612af8cb68b394045ce3c85313`; Push/PR CI passed; Artifact `9822441595`; IPA `sha256:f03f5d657cbf71772d197fcea969cafb73d249c2dcc3dd2feb72e139d6e9cf61`.
- b85 real-device Runtime: explicit Sync reliably projected active authoritative Detail reasoning/tool timeline `1 -> 5 -> 7` on the same external response generation and final authoritative assistant materialization reconciled/cleared it. Manual block acquisition is Runtime Positive.
- b85 automatic continuation: Rejected for reliability. Covered page re-armed/loaded after Sync but no external streaming/snapshot/resume event appeared; each newer block required another explicit Sync.
- b86 identity: exact diagnostics product source `dc77a94be5b2f7eecd822480f759358ad6a0ad25`; Push `33566939415/100052171917` and PR `33566968066/100052259409` passed; canonical Artifact `9823485856`; IPA `sha256:25d483ac31473b124e6ad555b79c488e78da91ec1761ee8a40076b6e978bee6f`.
- b86 is diagnostics-only: matching page-owned `stream_status` request/HTTP/state and matching resume offset structure are logged without issuing any new request or changing acquisition behavior. Runtime pending.
- Client-owned Send remains true SSE; no Native guessed resume/offset, polling, timer, retry/watchdog, duplicate Send or hidden-thought presentation. Stable/Frozen Send remains No; b39-b86 reserved.

'''
module.write_text(pre + replacement + end + post)

decisions = Path('docs/project/TECHNICAL_DECISIONS.md')
text = decisions.read_text()
heading = '# Technical Decisions\n\n'
section_title = '## b85 Runtime / b86 continuation diagnostics qualification — 2026-09-02\n'
section = '''## b85 Runtime / b86 continuation diagnostics qualification — 2026-09-02

- **Authoritative block path:** b85 real-device Runtime confirms explicit `同步最新消息` may project the already-approved active Detail trailing reasoning/tool timeline through the existing per-conversation Repository response owner. Repeated Sync updated one response generation (`1 -> 5 -> 7` timeline items) and final authoritative materialization reconciled it correctly.
- **Continuation qualification:** this does not establish one-Sync automatic continuation. In the supplied b85 run the covered page re-armed and loaded, but no page-owned streaming/snapshot/resume event appeared; each newer block required another explicit Sync. The remaining problem is page-owned continuation activation, not Native response ownership.
- **Diagnostic decision:** b86 may log only matching page-owned `stream_status` request/HTTP/status token and matching resume offset structure/response. It must not issue new requests, construct Native resume/offset, poll, retry, resend or create another state owner.
- **SSE research boundary:** historical exact Runtime already proves official Web can perform cross-device `/resume {conversation_id, offset}` -> HTTP200 `text/event-stream`; b86 exists only to determine whether/when the current covered page enters that official path after the new authoritative active-Detail anchor is known.

'''
if section_title not in text:
    if heading not in text:
        raise SystemExit('TECHNICAL_DECISIONS heading missing')
    text = text.replace(heading, heading + section, 1)
decisions.write_text(text)
