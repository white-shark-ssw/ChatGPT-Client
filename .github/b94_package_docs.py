from pathlib import Path

CP=Path('docs/project/current/dev/DEV-send-stream.md')
IDX=Path('docs/project/BUILD_TEST_INDEX.md')
for p in [CP,IDX]:
    assert p.exists()
cp=CP.read_text()
old='- b94 Candidate / Build: `DEV-send-stream-0.1.0-b94` / `0.1.0 (94)` permanently reserved; product/package pending at allocation checkpoint\n- Stable/Frozen Send: No'
new='''- b94 Candidate / Build: `DEV-send-stream-0.1.0-b94` / `0.1.0 (94)` permanently reserved
- b94 allocation checkpoint: `d957e29595e13fcb46da133d98eebaa716f93d25`
- Exact b94 product commit: `95f0f99921ad9f41a40b7919162498b00138d5a4`
- Exact b94 product/config package source: `59894bd9ca7c293211cd856ecf33579f19ce4d84`
- b94 staging: `33761087305 / 100667284502` — success
- b94 Push CI: `33761341528 / 100668157341` — success
- b94 PR CI: `33761346240 / 100668174308` — success
- b94 canonical Push Artifact: `9895660898`
- b94 Artifact digest: `sha256:65d29b08d10ef3c626f64a9fa16e574a53ab33aa0d7041fa53f9c094915b9b60`
- b94 IPA SHA-256: `a0d3de344f18f75e0286f26c27b9ea0c89548bed6a75bff4bb3369ee7bcfaffb`
- Stable/Frozen Send: No'''
assert old in cp
cp=cp.replace(old,new,1)
marker='## Validation / identity state\n'
block='''## b94 package / validation state\n\nb94 changes only foreground lifecycle recovery for the selected already-active external response. On `UIApplication.willEnterForegroundNotification`, if the selected Repository live snapshot is active/external (`promptText` empty), the existing covered executor reloads the same official conversation page and logs `foreground_external_page_rebootstrap` / `coveredExecutor.foregroundPageRebootstrap`. It does not perform Native Detail Sync and does not synthesize `stream_status` or `/resume`.\n\nAllocation checkpoint `d957e29595e13fcb46da133d98eebaa716f93d25`; product `95f0f99921ad9f41a40b7919162498b00138d5a4`; exact product/config package source `59894bd9ca7c293211cd856ecf33579f19ce4d84`. Staging `33761087305 / 100667284502` passed exact two-file scope and Simulator compile. Push CI `33761341528 / 100668157341` and PR CI `33761346240 / 100668174308` passed. Canonical Push Artifact `9895660898` has digest `sha256:65d29b08d10ef3c626f64a9fa16e574a53ab33aa0d7041fa53f9c094915b9b60`. Independent unpacking verified IPA SHA `a0d3de344f18f75e0286f26c27b9ea0c89548bed6a75bff4bb3369ee7bcfaffb` matching sidecar, `0.1.0 (94)`, Candidate b94, source `59894bd9ca7c`, MinimumOS 14.0, device family `[1,2]`, `iphoneos`, arm64.\n\nEvidence ladder: **Code written / guarded exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**\n\n## b94 Human Runtime gate\n\nUse one project conversation/executor only. Start a deliberately long remote response, press `同步最新消息` once to establish advancing page-owned external snapshots, keep that same conversation selected, background ChatGPTClient while the remote response is still active, then return foreground **without pressing Sync**. Require `foregroundExternalRebootstrap.requested`, activation stage `foreground_external_page_rebootstrap`, `coveredExecutor.foregroundPageRebootstrap`, a completed official page load, then renewed matching `externalStreamStatusRequest/Response` and external snapshots. Let the remote response finish naturally and require final materialization/reconcile without Sync.\n\nIf the remote answer is already terminal before foreground rebootstrap, classify the sample Inconclusive and reuse exact b94; do not allocate a new candidate. Selection-triggered page rebootstrap remains outside b94.\n\n'''
assert marker in cp
cp=cp.replace(marker,block+marker,1)
cp=cp.replace('**Open for b94 foreground page-rebootstrap A/B. Next exact action:** apply only foreground rebootstrap of the selected already-active external executor, validate exact two-product-file scope + Simulator, package exact b94, then stop at Human Runtime. Selection-triggered page rebootstrap remains separate.','**Closed at exact b94 Human Runtime gate. Next exact action:** install exact canonical b94 and run the single-executor foreground lifecycle test above. Do not modify product/config or allocate another candidate before Runtime evidence. Selection-triggered page rebootstrap remains separate.',1)
CP.write_text(cp)
idx=IDX.read_text()
anchor='| `DEV-send-stream-0.1.0-b93` |'
assert anchor in idx
row='| `DEV-send-stream-0.1.0-b94` | `DEV-send-stream` | `0.1.0 (94)` | foreground official-page rebootstrap product `95f0f99921ad9f41a40b7919162498b00138d5a4`; exact package source `59894bd9ca7c293211cd856ecf33579f19ce4d84`; PR #29 | staging `33761087305/100667284502` exact two-file scope+Simulator passed; Push `33761341528/100668157341` passed; PR `33761346240/100668174308` passed; canonical Artifact `9895660898`; Artifact `sha256:65d29b08d10ef3c626f64a9fa16e574a53ab33aa0d7041fa53f9c094915b9b60`; IPA `sha256:a0d3de344f18f75e0286f26c27b9ea0c89548bed6a75bff4bb3369ee7bcfaffb`; package `0.1.0 (94)` / Candidate b94 / source `59894bd9ca7c` / iOS14 / `[1,2]` / arm64 | Human Runtime pending: single-executor foreground official-page rebootstrap after background while remote generation remains active | **Code/guarded scope+Simulator/Push+PR CI/Artifact/package verified; Runtime Unverified; Stable-Frozen No; permanently reserved** |\n'
idx=idx.replace(anchor,row+anchor,1)
IDX.write_text(idx)
