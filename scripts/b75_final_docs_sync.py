from pathlib import Path

# PROJECT_PROFILE: add current override and replace stale current-candidate boundary.
path = Path('docs/project/PROJECT_PROFILE.md')
text = path.read_text()
heading = '## DEV-send-stream b75 current Runtime override — 2026-09-01'
assert heading not in text
marker = '# Project Profile\n\n'
assert text.startswith(marker)
section = '''## DEV-send-stream b75 current Runtime override — 2026-09-01

- Exact current package remains `DEV-send-stream-0.1.0-b75` / `0.1.0 (75)`, product/config source `b77303b8870dc25851dbffbf38ffc153a47bbcb2`, Artifact `9772079468`, IPA SHA `a912547a1845cae182d83d551eb51955b5060062f66ec3fbdf14be45954dab9d`.
- Exact iPhone/iOS17 Runtime is **partial/rejected**: pre-accept resume validation fixed the false Native failure, but three matching page-owned `/backend-api/f/conversation/resume` attempts returned HTTP404 JSON while the external response was still active, so no Native live reasoning/tool/final stream was adopted.
- b75 cooperative history geometry scheduling is executing; worst-case Back responsiveness remains unclosed by the supplied run.
- b75 tool/reasoning/final line-height values `26 / 18.2 / 18.2` are implemented but visually rejected as too tight by the latest Runtime screenshot.
- b39-b75 are permanently reserved. b76 is permitted by concrete b75 defects but **not allocated** before the current Web Rule Lab continuation re-probe resolves the transport rule.

'''
text = marker + section + text[len(marker):]
old = '''## Current next Candidate boundary

Build74 is the current exact real-device Runtime candidate. b39-b74 are permanently reserved. Do not allocate b75 unless exact b74 Runtime supplies a concrete defect or new evidence-backed requirement. The Runtime gate must verify long resident re-entry performance, larger tool-row rhythm, external active-response adoption through page-owned matching `/resume`, local protected-Send regression, b72 simultaneous-generation ownership, hidden-thought exclusion and b38 quick-navigation/geometry semantics.
'''
new = '''## Current next Candidate boundary

Build75 is the latest exact real-device Runtime package and is partial/rejected for the evidence above. b39-b75 are permanently reserved. The current human-only gate is a Web Rule Lab structural re-probe of page-owned `stream_status` / matching `/resume` ordering and statuses while another platform owns an active response. Do not allocate b76 until that transport evidence is captured and the larger reasoning/tool/final vertical-rhythm correction is one coherent scope.
'''
assert old in text
text = text.replace(old, new, 1)
path.write_text(text)

# TECHNICAL_DECISIONS: add explicit current qualification without rewriting historical decisions.
path = Path('docs/project/TECHNICAL_DECISIONS.md')
text = path.read_text()
heading = '## b75 Runtime qualification — 2026-09-01'
assert heading not in text
marker = '# Technical Decisions\n\n'
assert text.startswith(marker)
section = '''## b75 Runtime qualification — 2026-09-01

- **TD-014 presentation qualification:** Build75 proves the numeric `26 / 18.2 / 18.2` tool/reasoning/final line-height implementation is not the accepted visual target; the latest exact screenshot rejects it as too tight. Future correction must increase the visible vertical rhythm while keeping reasoning/final measurement and rendering consistent and preserving chronological reasoning/tool semantics.
- **TD-029 external-continuation qualification:** request observation alone remains non-authoritative. Exact b75 covered-production Runtime saw three matching official-page-owned `/backend-api/f/conversation/resume` responses return HTTP404 JSON while the external response was still active. Therefore covered-production external adoption is not Runtime accepted. Do not add Native resume/offset construction, polling, retry, guessed alternate routes or WebSocket body authority. Re-probe current official page behavior in Web Rule Lab first.
- b67 local protected-Send transport and b72 exact tested cross-conversation simultaneous ownership remain accepted predecessors; b75 does not revoke them.

'''
path.write_text(marker + section + text[len(marker):])

# PROJECT_SPECIFIC_RULES: current package/resume rules.
path = Path('docs/project/PROJECT_SPECIFIC_RULES.md')
text = path.read_text()
heading = '## b75 current Runtime override — 2026-09-01'
assert heading not in text
marker = '# Project-Specific Rules\n\n'
assert text.startswith(marker)
section = '''## b75 current Runtime override — 2026-09-01

- Exact b75 package is permanently reserved: source `b77303b8870dc25851dbffbf38ffc153a47bbcb2`, Artifact `9772079468`, IPA SHA `a912547a1845cae182d83d551eb51955b5060062f66ec3fbdf14be45954dab9d`.
- A page-owned matching `/resume` request is structural observation only. Exact b75 covered-production Runtime returned HTTP404 JSON for all three observed matching resume attempts while the external response was active; current external stream adoption is therefore **not Runtime accepted**.
- Do not bypass this with Native resume/offset construction, `stream_status` polling, retry/timer/watchdog, guessed route fallback, duplicate Send or WebSocket body parsing. Use Web Rule Lab to establish the current page-owned transport first.
- b75 `26 / 18.2 / 18.2` tool/reasoning/final line-height output is visually rejected as too tight. Those numbers are not an accepted presentation baseline.
- b76 may be allocated only after the continuation probe defines a minimal current transport correction and the larger visual-spacing correction is coherent; until then b76 remains unallocated.

'''
text = marker + section + text[len(marker):]
text = text.replace('b24-b74 emitted identities are permanently reserved;', 'b24-b75 emitted identities are permanently reserved;', 1)
old = '- b74 is the first packaged production candidate for this boundary; Runtime remains pending.'
new = '- b74 was the first packaged candidate for this boundary; exact b75 Runtime now rejects the covered-production adoption path because matching page-owned resume responses were HTTP404 JSON. Re-probe before another product implementation.'
assert old in text
text = text.replace(old, new, 1)
old = '- exact b74 package authority is `0.1.0 (74)`, source `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`, Artifact `9768668727`, ZIP `6ac4cc97954a0a26ed258a9775921cc4d12b17a1ff29c5e8d65cddf3c5595cb3`, IPA `07c999fd0e9aaa5685725e6a97f066221f1f986cc3e23a99693a91accda285da`; Code/CI/Artifact/package verified, Runtime pending;\n- do not allocate b75 unless exact b74 Runtime supplies a concrete defect or new evidence-backed requirement.'
new = '- exact b74 package authority is `0.1.0 (74)`, source `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`, Artifact `9768668727`, ZIP `6ac4cc97954a0a26ed258a9775921cc4d12b17a1ff29c5e8d65cddf3c5595cb3`, IPA `07c999fd0e9aaa5685725e6a97f066221f1f986cc3e23a99693a91accda285da`; permanently reserved;\n- exact b75 package authority is `0.1.0 (75)`, source `b77303b8870dc25851dbffbf38ffc153a47bbcb2`, Artifact `9772079468`, ZIP `6c4c4ec9de54264846376bdf7df4679daaaf33168481831698c884093b6209ad`, IPA `a912547a1845cae182d83d551eb51955b5060062f66ec3fbdf14be45954dab9d`; Runtime partial/rejected and permanently reserved;\n- do not allocate b76 before the current Web Rule Lab continuation re-probe resolves the covered-production 404 behavior.'
assert old in text
text = text.replace(old, new, 1)
path.write_text(text)

# Finalize checkpoint after durable docs + PR metadata are known complete.
path = Path('docs/project/current/dev/DEV-send-stream.md')
text = path.read_text()
old_start = '## Batch recovery point — b75 Runtime classification\n\n'
old_end = '\n## Exact next action\n\n'
start = text.index(old_start)
end = text.index(old_end, start)
replacement = '''## Completed documentation batch — b75 Runtime classification

- Exact b75 product source remains `b77303b8870dc25851dbffbf38ffc153a47bbcb2`; all later commits in this batch are docs-only and do not redefine the package.
- Checkpoint Runtime classification commit: `d07cde81277d5bbb1e57d2c3f85c8772a64745c7`.
- Durable b75 Runtime docs commit: `238b9e93b4e5f780aaf525106ec672de8ed8225b`, audited as exactly `BUILD_TEST_INDEX.md`, `MODULE_STATUS.md`, `PROJECT_STATE.md`, and `WEB_SEND_ADAPTER.md`.
- PR #29 metadata is synchronized to title `DEV-send-stream: b75 Runtime rejection -> Web continuation re-probe gate`; it remains open / mergeable / unmerged.
- This final docs-only batch synchronizes `PROJECT_PROFILE.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_SPECIFIC_RULES.md`, and this checkpoint.
- Actual `main` remains `d323b9eed2dda75b9986fc06e14014d3e9b365fb` at the last guard. Stable/Frozen Send remains No.
- b76 remains unallocated.
'''
text = text[:start] + replacement + text[end:]
old = '''## Exact next action

Complete the pending docs/PR metadata batch above, then hand the user the smallest Web Rule Lab probe needed to distinguish `stream_status -> first resume 404 -> later page-owned transport` behavior. Product code stops at that human evidence gate. After the Lab result arrives, rerun Resume Guard, finalize the larger visual-spacing correction together with the evidenced continuation rule, allocate b76 once, then compile/CI/package one coherent Runtime candidate.
'''
new = '''## Exact next action

Human-only Web Rule Lab gate: while another platform owns a still-active response, instrument only page-owned fetch structure before entering that target conversation, then report `stream_status` / matching `/resume` ordering, response status/content-type, request JSON key names, and whether another page-owned HTTP/SSE transport follows an initial 404. Do not send from the Lab and do not capture secrets or message bodies. After that evidence arrives, rerun Resume Guard, define the current continuation rule, combine it with the clearly required larger reasoning/tool/final vertical rhythm, allocate b76 once, then compile/CI/package one coherent Runtime candidate.
'''
assert old in text
text = text.replace(old, new, 1)
path.write_text(text)
