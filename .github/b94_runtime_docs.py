from pathlib import Path
import re

CHECKPOINT = Path('docs/project/current/dev/DEV-send-stream.md')
INDEX = Path('docs/project/BUILD_TEST_INDEX.md')
STATE = Path('docs/project/PROJECT_STATE.md')
MODULE = Path('docs/project/MODULE_STATUS.md')
DECISIONS = Path('docs/project/TECHNICAL_DECISIONS.md')
ADAPTER = Path('docs/project/WEB_SEND_ADAPTER.md')
PLAN = Path('docs/project/DEVELOPMENT_PLAN.md')


def replace_once(text, old, new, label):
    if old not in text:
        raise SystemExit(f'missing expected text: {label}')
    return text.replace(old, new, 1)


def append_once(path, marker, block):
    text = path.read_text()
    if marker not in text:
        if not text.endswith('\n'):
            text += '\n'
        text += '\n' + block.strip() + '\n'
        path.write_text(text)

cp = CHECKPOINT.read_text()
cp = replace_once(
    cp,
    '**Active — exact b92 proves covered single-conversation external continuation and client-owned Send/SSE terminal reconciliation, but overlap/reselection recovery is Runtime Negative. Exact b93 is Code/guarded two-file scope+Simulator/Push+PR CI/Artifact/package verified and tests only selection-time focus reacquisition for an already-active external executor. Human Runtime pending. Stable/Frozen Send remains No.**',
    '**Active — new exact b92 single-executor Runtime proves background lifecycle can stop the official page-owned continuation loop, and exact b93 proves selection focus reacquisition succeeds but is not sufficient to restart a stopped loop. b93 focus-sufficient is Rejected. The next isolated evidence target is official-page rebootstrap on foreground for one active external response; b94 is not yet allocated. Stable/Frozen Send remains No.**',
    'checkpoint status')

b93_marker = '## b93 Human Runtime result — 2026-09-03'
if b93_marker not in cp:
    insert = '''## b93 Human Runtime result — 2026-09-03\n\nThe user supplied exact b92 and b93 logs that materially revise the earlier focus hypothesis. Full evidence is in `docs/project/runtime-evidence/DEV-send-stream-b92-b93-page-loop-interruption-20260903.md`.\n\nExact b92 (`54b5803a74a1`) reproduces the terminal freeze with a single external conversation and a single executor. Page-owned status/snapshot progression reached `service 88 / tools 33`; the last `stream_status` request/HTTP200 `IS_STREAMING` and last snapshot coincide with entry to background at `12:13:30-12:13:31Z`. After later foreground returns the page becomes visible and the user WebSocket can reconnect, but no further page-owned `stream_status` or external snapshot is emitted. Explicit Sync at `12:19:46Z` then materializes the completed assistant and clears the stale live response. Therefore a second executor is not necessary for the failure.\n\nExact b93 (`2d2cde58a7fb`) proves the added focus mechanism itself: reselection repeatedly obtains `nativeFirstResponder=true` and `documentHasFocus=true`. At `13:07:31Z` that rearm is followed by another page-owned HTTP200 `IS_STREAMING` and snapshot `80 / 19`. After switching away at `13:07:38Z` and returning at `13:07:42Z`, focus rearm again succeeds (and repeats at `13:07:47Z`) but page-owned status requests never restart. Explicit Sync at `13:10:24Z` later adds the completed assistant (`visible 26 -> 27`) and performs `liveResponse.externalDetailReconciled`.\n\nClassification: **b93 focus reacquisition mechanism Runtime Positive; focus reacquisition as a sufficient restart condition Rejected.** The common failure is now the lifetime of the official page-owned continuation acquisition loop itself.\n\n## b94 exact minimum A/B — not yet allocated\n\nThe next candidate, if allocated, must test the clean single-executor lifecycle case first. Keep b93 transport/ownership/route behavior, but when ChatGPTClient becomes active again and the selected Repository snapshot is still an active external response (`promptText` empty), rebootstrap that same existing official conversation page without a Native Detail Sync. Add a distinct foreground-rebootstrap diagnostic stage.\n\nThis is an official-page lifecycle A/B only. Do not add Native `stream_status`, `/resume`, guessed offset, polling/cadence reproduction, retry/watchdog/timer, duplicate Send, WebSocket-body authority, or a second response store.\n\nRuntime gate: one external conversation/executor, one initial Sync to acquire continuation, background while the remote answer remains active, return foreground without Sync, then require page-owned status/snapshots to resume and the final assistant to reconcile naturally. Selection-triggered page rebootstrap remains a separate later A/B.\n\n'''
    cp = cp.replace('## Validation / identity state\n', insert + '## Validation / identity state\n', 1)

cp = replace_once(
    cp,
    '**Closed for b93 product/package/docs preparation. Next exact action:** install exact canonical b93 and execute the overlap/reselection Human Runtime gate. No product/config change is permitted before that Runtime evidence.',
    '**Closed for b93 Runtime classification. Next exact action:** perform a fresh resume/conflict guard, then allocate b94 only for foreground official-page rebootstrap of one already-active external response. Do not combine selection rebootstrap into b94 and do not modify continuation protocol.',
    'next exact action')
CHECKPOINT.write_text(cp)

idx = INDEX.read_text()
pattern = re.compile(r'^\| `DEV-send-stream-0\.1\.0-b93` .*$', re.M)
m = pattern.search(idx)
if not m:
    raise SystemExit('missing b93 index row')
old = m.group(0)
new = old
new = re.sub(r'\| Human Runtime pending:.*? \| \*\*Code/guarded scope\+Simulator/Push\+PR CI/Artifact/package verified; Runtime Unverified; Stable-Frozen No; permanently reserved\*\* \|$',
             '| **Runtime Partial / sufficient-condition Rejected:** selection focus rearm repeatedly achieved `nativeFirstResponder=true` / `documentHasFocus=true`; one rearm still continued, but a later rearm after switching away/back remained focused while page-owned `stream_status` and snapshots never restarted; explicit Sync later materialized the completed assistant. Separate exact b92 single-executor evidence also proves background lifecycle can stop the same page-owned loop | **Focus mechanism Runtime Positive; focus as sufficient continuation-restart condition Rejected; page-loop lifecycle rebootstrap next; Stable-Frozen No; permanently reserved** |', new)
if new == old:
    raise SystemExit('b93 index replacement did not apply')
INDEX.write_text(idx[:m.start()] + new + idx[m.end():])

block = '''## 2026-09-03 — b92/b93 page-owned continuation loop interruption\n\nExact b92 single-executor Runtime proves that a background lifecycle transition can stop the official page-owned `stream_status`/snapshot loop even without another executor. Exact b93 proves successful first-responder/document-focus reacquisition does not necessarily restart a stopped loop. The next isolated candidate is foreground official-page rebootstrap without Native Detail Sync; selection rebootstrap remains separate. Stable/Frozen Send remains No.'''
for path in (STATE, MODULE, DECISIONS, ADAPTER, PLAN):
    append_once(path, 'b92/b93 page-owned continuation loop interruption', block)
