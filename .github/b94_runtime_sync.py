from pathlib import Path

checkpoint = Path('docs/project/current/dev/DEV-send-stream.md')
index = Path('docs/project/BUILD_TEST_INDEX.md')
adapter = Path('docs/project/WEB_SEND_ADAPTER.md')
state = Path('docs/project/PROJECT_STATE.md')

old_status = '**Active — exact b92 single-executor Runtime proves background lifecycle can stop the official page-owned continuation loop, and exact b93 proves selection focus reacquisition succeeds but is not sufficient to restart a stopped loop. b93 focus-sufficient is Rejected. Exact b94 foreground official-page rebootstrap is Code/guarded scope+Simulator/Push+PR CI/Artifact/package verified; Human Runtime pending. Stable/Frozen Send remains No.**'
new_status = '**Active — exact b94 proves foreground official-page rebootstrap can restart the page-owned continuation loop after background, but the same long-running project-conversation run later terminated the WKWebView WebContent process. Rebootstrap mechanism Runtime Positive; repeated/heavy covered-Web reliability Runtime Negative / not production-stable; OOM cause Unverified; external terminal/final still not achieved. Stable/Frozen Send remains No.**'

runtime_block = '''## b94 Human Runtime result — 2026-09-03\n\nExact b94 diagnostics match Candidate `DEV-send-stream-0.1.0-b94`, Build 94, source `59894bd9ca7c`, iPhone / iOS 17.0. Full evidence is recorded in `docs/project/runtime-evidence/DEV-send-stream-b94-foreground-rebootstrap-web-process-terminated-20260903.md`.\n\nThe foreground-rebootstrap mechanism itself is Runtime Positive. After background at `14:25:44-14:25:46Z`, foreground at `14:25:52Z` emitted the b94 rebootstrap diagnostics, reloaded the same official conversation page, and page-owned HTTP200 `IS_STREAMING` plus external snapshots resumed without another Sync. The live projection advanced through `11/4`, `13/4`, `15/5` service/tool counts. A later foreground rebootstrap at `14:27:25Z` again restored the loop and snapshots advanced through `34/12`, `36/13`, `37/14`, `39/14`. Therefore full official-page rebootstrap is sufficient to restart at least these interrupted page-owned continuation loops; b93 focus-only recovery remains rejected as sufficient.\n\nThe same exact run also exposes a new reliability failure. After several foreground/background transitions and repeated full conversation-page rebootstrap actions, foreground at `14:35:12Z` loaded the page, then at `14:35:17Z emitted `coveredExecutor.webProcess state=terminated` followed by `coveredExecutor.failed reason=web_process_terminated`; external generation 1 failed and the executor was released. This is direct Runtime evidence of WKWebView WebContent-process termination. The cause is Unverified: current diagnostics do not capture WebContent memory or jetsam reason, so do not call this proven OOM.\n\nThe conversation is now very large. Late authoritative Detail is `5,491,909` bytes, mapping `1535`, recipient-message count `397`, visible-message count `28`; the successful late Syncs take about `4.77s` and `5.44s`. This makes the earlier Web Rule Lab timeout/resource concern a material hypothesis, not a proven root cause.\n\nBoth late user Sync actions succeeded at the authoritative transport layer. At `14:36:15Z` and again `14:38:19Z`, HTTP200 Detail still contained trailing reasoning/timeline/tool counts `3 / 33 / 30` and no new visible final assistant. Repository therefore correctly rebuilt external generation 2, after which official `stream_status` continued returning `IS_STREAMING` and snapshots stayed around `service=109 / tools=30 / finalCharacters=0` through export. The final Sync did not fail; authoritative server state itself remained unfinished/stuck at export.\n\nCurrent UI intentionally disables `重载当前会话` whenever the selected live snapshot phase is active. Therefore after the authoritative Sync rebuilt an active external live response, Reload being grey is expected current policy, not an in-flight-operation leak. In combination with an indefinitely active external response, this creates a real user recovery dead-end.\n\nClassification: **foreground page rebootstrap mechanism Runtime Positive; repeated/heavy full-page covered-Web reliability Runtime Negative / not production-stable in this run; WebContent termination root cause Unverified; manual late Sync transport Runtime Positive; external terminal/final convergence Unverified/not achieved; manual Reload recovery blocked by current active-live UI policy; Stable/Frozen No.**\n\nDo not allocate a new candidate merely to add polling/retry/timers. Next work must first isolate a minimum event-driven response to the now-proven WebContent termination / repeated heavy reload problem and a deliberate user recovery path, while preserving official-page transport ownership and Repository content ownership.\n\n'''

text = checkpoint.read_text()
if old_status in text:
    text = text.replace(old_status, new_status, 1)
elif new_status not in text:
    raise SystemExit('checkpoint status marker not found')
if '## b94 Human Runtime result — 2026-09-03' not in text:
    marker = '\n## Validation / identity state\n'
    if marker not in text:
        marker = '\n## Batch recovery state\n'
    if marker not in text:
        raise SystemExit('checkpoint insertion marker not found')
    text = text.replace(marker, '\n' + runtime_block + marker.lstrip('\n'), 1)
checkpoint.write_text(text)

lines = index.read_text().splitlines()
new_row = '| `DEV-send-stream-0.1.0-b94` | `DEV-send-stream` | `0.1.0 (94)` | foreground official-page rebootstrap product `95f0f99921ad9f41a40b7919162498b00138d5a4`; exact package source `59894bd9ca7c293211cd856ecf33579f19ce4d84`; PR #29 | staging `33761087305/100667284502` exact two-file scope+Simulator passed; Push `33761341528/100668157341` passed; PR `33761346240/100668174308` passed; canonical Artifact `9895660898`; Artifact `sha256:65d29b08d10ef3c626f64a9fa16e574a53ab33aa0d7041fa53f9c094915b9b60`; IPA `sha256:a0d3de344f18f75e0286f26c27b9ea0c89548bed6a75bff4bb3369ee7bcfaffb`; package `0.1.0 (94)` / Candidate b94 / source `59894bd9ca7c` / iOS14 / `[1,2]` / arm64 | **Runtime Partial:** foreground page rebootstrap twice restarted official page-owned `IS_STREAMING` + snapshots after lifecycle interruption, but later the covered WKWebView WebContent process terminated. Late authoritative Sync remained HTTP200 with trailing `3/33/30`, and the page continued reporting `IS_STREAMING` with no final assistant before export. OOM cause Unverified | **Rebootstrap mechanism Runtime Positive; repeated/heavy covered-Web reliability Runtime Negative / not production-stable; terminal/final Unverified; Stable-Frozen No; permanently reserved** |'
replaced = False
for i, line in enumerate(lines):
    if line.startswith('| `DEV-send-stream-0.1.0-b94` |'):
        lines[i] = new_row
        replaced = True
        break
if not replaced:
    raise SystemExit('b94 index row not found')
index.write_text('\n'.join(lines) + '\n')

adapter_note = '''\n## b94 Runtime reliability finding — 2026-09-03\n\nExact b94 proves foreground reload of the same official conversation page can restart page-owned continuation after lifecycle interruption. It also proves this cannot yet be treated as production-stable: after repeated foreground/background transitions and repeated full-page rebootstrap of a very large project conversation, `webViewWebContentProcessDidTerminate` fired and the executor failed. The cause is Unverified; do not label it OOM without WebContent/OS evidence.\n\nLate authoritative Detail had grown to about 5.49 MB / mapping 1535. Two late manual Syncs still returned HTTP200, but authoritative trailing response remained active (`reasoning/timeline/tools = 3/33/30`) and official `stream_status` remained `IS_STREAMING` with no final assistant before export. Current Reload UI is intentionally disabled while any live response phase is active, creating a manual recovery dead-end if the external response stays active indefinitely.\n\nDo not answer this with Native `stream_status`, Native `/resume`, guessed offsets, cadence polling, retry/watchdog timers, WebSocket-body authority, duplicate Send, or a second response store. Any next candidate must isolate an event-driven WebContent/rebootstrap reliability change or explicit user recovery path.\n'''
atext = adapter.read_text()
if '## b94 Runtime reliability finding — 2026-09-03' not in atext:
    adapter.write_text(atext.rstrip() + '\n' + adapter_note)

state_note = '''\n## 2026-09-03 b94 Runtime update\n\n`DEV-send-stream` remains Active / Stable-Frozen No. Exact b94 foreground official-page rebootstrap is Runtime Positive as a restart mechanism, but the same long-running project-conversation run later recorded covered WKWebView WebContent-process termination. The termination cause is Unverified. Late authoritative Sync remained HTTP200 yet server-owned trailing response and `IS_STREAMING` persisted without a final assistant. Next work is evidence-driven WebContent/rebootstrap reliability and user recovery design; no speculative polling/retry/timer workaround is approved.\n'''
s = state.read_text()
if '## 2026-09-03 b94 Runtime update' not in s:
    state.write_text(s.rstrip() + '\n' + state_note)
