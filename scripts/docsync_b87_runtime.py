from pathlib import Path

path = Path('docs/project/BUILD_TEST_INDEX.md')
lines = path.read_text().splitlines()
prefix = '| `DEV-send-stream-0.1.0-b87` |'
matches = [i for i, line in enumerate(lines) if line.startswith(prefix)]
assert len(matches) == 1, matches
idx = matches[0]
old = lines[idx]
assert 'Runtime pending:' in old
assert '**Code/PR CI/Artifact/package verified; Runtime Pending; permanently reserved**' in old
lines[idx] = '| `DEV-send-stream-0.1.0-b87` | `DEV-send-stream` | `0.1.0 (87)` | exact diagnostics product source `6f98816f37c749c8d4cb8dfef4c4645df2c0f27a`; clean feature/package head `49cf74f5f97e5afd3ad78aa59d3b9ad19673d488`; PR #29 | clean-head PR CI `33607517120/100174803981` passed; exact feature-head package `33607783508/100175624048` passed; canonical Artifact `9837745187`; ZIP `sha256:5cf72023fdd7b309213da8d31e28e59907fae6e46b3c816230d93386b003dc3b`; IPA `sha256:02598b5325c65f2ae3402e97812eca5676debc56a475963c0e8e7a9127a2b1ba`; package `0.1.0 (87)` / Candidate b87 / source `49cf74f5f97e` / iOS14 / arm64. PR-triggered Artifact whose built source was synthetic merge `93f1a827f938` is non-canonical and must not be used for Runtime | Runtime Diagnostic Positive / continuation rejected: manual Sync projected active authoritative Detail while target page was `visibilityState=visible`, `hidden=false`, ready `complete`, route `conversation`, attached to key window with non-empty intersecting bounds; `document.hasFocus=false` throughout. After manual re-arm there was ~161s clean foreground with zero `stream_status`, `/resume`, page-owned snapshot or SSE. User-socket frames remained `targetMatch=false`; completed assistant materialized only after a later explicit Sync | **Diagnostic Runtime Positive; Page Visibility/off-window hypotheses rejected, focus-vs-router causality Unverified; automatic continuation + final convergence rejected in exact run; permanently reserved** |'
path.write_text('\n'.join(lines) + '\n')
