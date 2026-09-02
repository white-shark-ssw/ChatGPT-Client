from pathlib import Path


def replace_prefix(lines, prefix, replacement):
    matches = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    assert len(matches) == 1, (prefix, matches)
    i = matches[0]
    lines[i:i + 1] = replacement.splitlines()


index_path = Path('docs/project/BUILD_TEST_INDEX.md')
index = index_path.read_text()
assert 'DEV-send-stream-0.1.0-b87' not in index
marker = '| `DEV-send-stream-0.1.0-b86` |'
pos = index.find(marker)
assert pos >= 0
row = '| `DEV-send-stream-0.1.0-b87` | `DEV-send-stream` | `0.1.0 (87)` | exact diagnostics product source `6f98816f37c749c8d4cb8dfef4c4645df2c0f27a`; clean feature/package head `49cf74f5f97e5afd3ad78aa59d3b9ad19673d488`; PR #29 | clean-head PR CI `33607517120/100174803981` passed; exact feature-head package `33607783508/100175624048` passed; canonical Artifact `9837745187`; ZIP `sha256:5cf72023fdd7b309213da8d31e28e59907fae6e46b3c816230d93386b003dc3b`; IPA `sha256:02598b5325c65f2ae3402e97812eca5676debc56a475963c0e8e7a9127a2b1ba`; package `0.1.0 (87)` / Candidate b87 / source `49cf74f5f97e` / iOS14 / arm64. PR-triggered Artifact whose built source was synthetic merge `93f1a827f938` is non-canonical and must not be used for Runtime | Runtime pending: activation-only diagnostics compare covered-page JS visibility/focus/readiness and Native WKWebView attachment/occlusion structure against presence/absence of official `stream_status` continuation activation | **Code/PR CI/Artifact/package verified; Runtime Pending; permanently reserved** |\n'
index = index[:pos] + row + index[pos:]
index_path.write_text(index)

cp_path = Path('docs/project/current/dev/DEV-send-stream.md')
lines = cp_path.read_text().splitlines()
replace_prefix(lines, '**Active — exact b86 Runtime', '**Active — b87 diagnostics-only package is now Code/PR-CI/Artifact verified and ready for real-device Runtime. b86 remains the decisive Runtime baseline: covered-page continuation activation was absent despite authoritative active reasoning. b87 changes diagnostics only; no continuation behavior fix is claimed. Stable/Frozen Send remains No.**')
replace_prefix(lines, '- Verified branch/PR head before b87 allocation:', '- b87 exact diagnostics product source: `6f98816f37c749c8d4cb8dfef4c4645df2c0f27a`\n- b87 clean feature/package head and PR #29 head before docs-only evidence sync: `49cf74f5f97e5afd3ad78aa59d3b9ad19673d488`')
replace_prefix(lines, '- b87 Candidate / Build:', '- b87 Candidate / Build: `DEV-send-stream-0.1.0-b87` / `0.1.0 (87)`\n- b87 clean-head PR CI: `33607517120 / 100174803981` — passed\n- b87 exact feature-head packaging: `33607783508 / 100175624048` — passed\n- b87 canonical Artifact: `9837745187`\n- b87 ZIP: `sha256:5cf72023fdd7b309213da8d31e28e59907fae6e46b3c816230d93386b003dc3b`\n- b87 IPA: `sha256:02598b5325c65f2ae3402e97812eca5676debc56a475963c0e8e7a9127a2b1ba`\n- b87 built metadata: `0.1.0 (87)` / Candidate `DEV-send-stream-0.1.0-b87` / `DiagnosticsSourceCommit=49cf74f5f97e` / minimum iOS14 / arm64\n- b87 PR-triggered Artifact built from synthetic merge `93f1a827f938` is **non-canonical** and must not be used for Runtime evidence')
replace_prefix(lines, '- b39-b87 permanently reserved once b87 product identity is emitted;', '- b39-b87 permanently reserved')

start = lines.index('## Batch recovery point — b87 activation diagnostics')
end = lines.index('## Recorded later requirement')
package_section = '''## b87 canonical package evidence

The b87 product/config change is diagnostics-only. Exact product commit `6f98816f37c749c8d4cb8dfef4c4645df2c0f27a` added page/WebView activation structure probes and build 87 identity. A later workflow-comment-only commit produced clean feature/package head `49cf74f5f97e5afd3ad78aa59d3b9ad19673d488`.

Normal PR CI for that clean head passed, but GitHub's `pull_request` checkout built synthetic merge source `93f1a827f938`; that Artifact is intentionally non-canonical for device evidence.

Canonical b87 was therefore packaged in isolated run `33607783508 / 100175624048` after an explicit exact-source assertion and checkout of `49cf74f5f97e5afd3ad78aa59d3b9ad19673d488`. The resulting Artifact `9837745187` has ZIP digest `sha256:5cf72023fdd7b309213da8d31e28e59907fae6e46b3c816230d93386b003dc3b`. Extracted IPA SHA is `02598b5325c65f2ae3402e97812eca5676debc56a475963c0e8e7a9127a2b1ba`; its built Info.plist reports `0.1.0 (87)`, Candidate `DEV-send-stream-0.1.0-b87`, `DiagnosticsSourceCommit=49cf74f5f97e`, minimum iOS14.

Evidence classification: Code written / exact staging guard passed / PR CI passed / Artifact produced and identity verified. **Runtime/manual/real-device remains Pending.**

## Next exact action

Install the canonical b87 IPA on the primary iPhone/iOS17 device. Start a sufficiently long response from another official client while the same conversation is selected in ChatGPTClient. During active generation press `同步最新消息` exactly once, then keep ChatGPTClient foregrounded without a second Sync. Export diagnostics after additional reasoning/tool progress or completion.

Compare, in timestamp order:

- `coveredExecutor.pageActivation`: `visibilityState`, `hidden`, `hasFocus`, `readyState`, `route`, `reason`;
- `coveredExecutor.webViewActivation`: `windowAttached`, `windowIsKey`, `hidden`, `alphaZero`, `boundsEmpty`, `intersectsWindow`, `subviewIndex`, `siblingCount`, `visibleSiblingCountAbove`, `userInteractionEnabled`;
- whether `externalStreamStatusRequest/Response`, `externalResumeRequest`, `resumeResponse`, `externalStreamingObserved`, external snapshots or DOM structure begin afterward.

Do not allocate b88 or change continuation behavior until this b87 Runtime distinguishes page visibility/focus/attachment from router/navigation activation.

'''.splitlines()
lines[start:end] = package_section
replace_prefix(lines, '- b87 Code/CI/Artifact/Runtime:', '- b87 Code/PR CI/Artifact/package: **Verified**\n- b87 Runtime/manual/real-device: **Pending**')
replace_prefix(lines, 'This user turn is **round 20**.', 'This user turn is **round 21**.')
cp_path.write_text('\n'.join(lines) + '\n')
