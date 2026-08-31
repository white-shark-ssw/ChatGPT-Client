from pathlib import Path
import re

# BUILD_TEST_INDEX
path = Path('docs/project/BUILD_TEST_INDEX.md')
text = path.read_text()
assert 'DEV-send-stream-0.1.0-b75' not in text
lines = text.splitlines()
idx = next(i for i, line in enumerate(lines) if line.startswith('| `DEV-send-stream-0.1.0-b74` |'))
b75 = '| `DEV-send-stream-0.1.0-b75` | `DEV-send-stream` | `0.1.0 (75)` | exact source `b77303b8870dc25851dbffbf38ffc153a47bbcb2`; PR #29 open | Assembly `33429163152`; Push `33429597213/99611443839`; PR `33429599704/99611451360`; Artifact `9772079468`; ZIP `sha256:6c4c4ec9de54264846376bdf7df4679daaaf33168481831698c884093b6209ad`; IPA `sha256:a912547a1845cae182d83d551eb51955b5060062f66ec3fbdf14be45954dab9d`; package source `b77303b8870d`/Release/iOS14/arm64 independently verified | Exact iPhone/iOS17 Runtime partial/rejected: pre-accept 404 no longer creates false Native failure, but three page-owned matching resume observations returned HTTP404 JSON while external response was still active, so Native never created live reasoning/tool/final rows; 26/18.2/18.2 typography visually rejected as too tight. Cooperative geometry path executed; worst-case Back gate not closed by this export. | **Runtime partial/rejected; permanently reserved** |'
lines.insert(idx + 1, b75)
path.write_text('\n'.join(lines) + '\n')

# PROJECT_STATE
path = Path('docs/project/PROJECT_STATE.md')
text = path.read_text()
heading = '## DEV-send-stream b75 Runtime override — 2026-09-01'
assert heading not in text
marker = '# Project State\n\n'
assert text.startswith(marker)
section = '''## DEV-send-stream b75 Runtime override — 2026-09-01

Exact b75 `DEV-send-stream-0.1.0-b75`, source `b77303b8870dc25851dbffbf38ffc153a47bbcb2`, Artifact `9772079468`, IPA SHA `a912547a1845cae182d83d551eb51955b5060062f66ec3fbdf14be45954dab9d` is package-verified and permanently reserved. iPhone/iOS17 Runtime is **partial/rejected**, not pending.

- Positive: b75 no longer promotes a page-owned matching resume request into a Native live response before HTTP200 SSE validation; repeated HTTP404 JSON resume responses therefore no longer flash the prior false `回答失败`.
- Rejected: while another platform's response was still active, the covered production page repeatedly issued matching `/backend-api/f/conversation/resume` but every observed response was HTTP404 JSON. Native correctly created no live response, so no `正在思考` / reasoning / tools / incremental final appeared. Successful Detail Sync/Reload only exposed server-backed visible messages later.
- Typography: exact 26 tool / 18.2 reasoning / 18.2 final values are implemented but the user's latest screenshot rejects the visual result as too tight/low. These numbers are not an accepted UI baseline.
- Geometry: supplied diagnostics prove `cooperative_main_queue` cache-miss scheduling and `resident_cache` reuse are executing. This export does not reproduce the former ~10s worst case, so the interactive-Back acceptance gate remains open.
- Next gate: use the existing Web Rule Lab on the same `.default()` WebKit session to determine current page-owned `stream_status -> resume` ordering/status and whether another page-owned transport follows the first resume 404. Do not guess Native resume/offset/polling or WebSocket body authority. b76 is not allocated yet.

'''
path.write_text(marker + section + text[len(marker):])

# MODULE_STATUS
path = Path('docs/project/MODULE_STATUS.md')
text = path.read_text()
heading = '## DEV-send-stream b75 Runtime override — 2026-09-01'
assert heading not in text
marker = '# Module Status\n\n'
assert text.startswith(marker)
section = '''## DEV-send-stream b75 Runtime override — 2026-09-01

- Build/runtime metadata: exact b75 package verified; Runtime partial/rejected; b39-b75 reserved; Stable/Frozen Send No.
- Covered external continuation: b75 pre-accept validation works, but covered production page-owned matching `/resume` returned HTTP404 JSON in three observed active-response attempts. HTTP200 SSE adoption is therefore not a current production-proven path; Web Rule Lab re-probe is required before product changes.
- User-visible reasoning/tool/final: no external live rows were created in the supplied b75 run. Local b67 transport and b72 tested simultaneous A/B ownership remain accepted predecessors.
- Typography: b75 26/18.2/18.2 is visually rejected as too tight; next correction must increase visible vertical rhythm rather than merely assert those numeric values.
- Geometry: cooperative cache-miss path and resident reuse observed; worst-case Back responsiveness remains Runtime-unverified in this export.

'''
path.write_text(marker + section + text[len(marker):])

# WEB_SEND_ADAPTER
path = Path('docs/project/WEB_SEND_ADAPTER.md')
text = path.read_text()
qual_heading = '### b75 covered-production qualification — 2026-09-01'
assert qual_heading not in text
needle = '**Current production rule:** external active-response adoption may observe and parse the official page\'s own `/backend-api/f/conversation/resume` SSE for the currently targeted conversation. Native code must not construct the resume request, choose/synthesize `offset`, replay browser/session headers, or poll `stream_status`. The page remains transport authority; `ConversationRepository` becomes/retains the sole Native response lifecycle owner once that page-owned resume is observed. Only a resume whose request `conversation_id` matches the executor\'s authoritative target may be adopted. The user-level WebSocket remains structural evidence only and is not authorized as a Native response-body source from this capture.\n'
assert needle in text
replacement = needle + '''\n### b75 covered-production qualification — 2026-09-01

The visible Web Rule Lab HTTP200-SSE capture above remains historical evidence for that exact visible-Web run, but exact Build75 production Runtime rejects treating it as proof that the covered executor will currently receive the same stream. In three separate covered-production attempts while the external response was still active, the page itself issued a matching `/backend-api/f/conversation/resume`, but the response was HTTP404 `application/json`; Native therefore had no validated SSE to adopt and correctly created no external live-response generation.

Current rule until re-probed: keep the b75 validation gate (request observation alone is never response authority), but **do not claim covered-production external adoption is working** and do not add Native-constructed resume/offset, polling, retry, delayed resend, WebSocket-body parsing or guessed alternate routes. Use Web Rule Lab to capture current page-owned `stream_status` status/order, all matching resume attempts/statuses, and whether a later page-owned HTTP/SSE transport follows an initial 404. Only that fresh evidence may define the next production continuation rule.
'''
text = text.replace(needle, replacement, 1)
path.write_text(text)
