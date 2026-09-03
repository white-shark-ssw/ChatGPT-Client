from pathlib import Path

block = '''## DEV-send-stream b92 covered-form package-ready override — 2026-09-03

- b91 project-scoped route identity and official page-owned live continuation are Runtime Positive; Native progressive projection works without a second Sync. Natural terminal/final remains Unverified because b91 was force-quit while still streaming.
- b92 is one isolated presentation cleanup only: it removes the b90 `bringSubviewToFront(webView)` z-order mutation and retains the b91 scoped-route parser, page-owned continuation observation, protected Send ownership, and `ConversationRepository` response authority. Manual Sync records `manual_sync_covered` but does not promote the WebView.
- Candidate / Build: `DEV-send-stream-0.1.0-b92` / `0.1.0 (92)`, permanently reserved. Allocation checkpoint `296de318c20ccc32bfea1cb93246bd9d824d3403`; exact product `96ea3e3d8c5cabf67ff33331d40c9dcc6c9f0850`; exact product/config package source `54b5803a74a123431f0a2a8e662a1a2fe874b3ca`.
- Two earlier staging runs `33749925741` and `33750233706` failed in guard-only tooling before checkpoint/product application. Successful guarded staging `33750363774 / 100632281401` passed exact b91-state guard, exact two-product-file scope audit and Xcode Simulator compile.
- Formal Push CI `33750585725 / 100632980237` and PR CI `33750591494 / 100632998279` both passed on the b92 package identity.
- Canonical Push Artifact `9891430379`; Artifact digest `sha256:f3cb6291fabcb2cf48729750d23a4403607e8ac81dc4354749974e287412e970`; IPA `ChatGPTClient-0.1.0-b92-dev-send-stream.ipa`, independently recomputed SHA-256 `82d96d359767b72c623f367bf3cd2c5f3ae9d1d7411ad547c1ba3634341c3514`, matching sidecar.
- Independent package inspection confirms Release `0.1.0 (92)`, Candidate b92, source `54b5803a74a1`, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, `iphoneos`, Mach-O 64-bit arm64.
- Evidence ladder: **Code written / guarded exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**
- Human Runtime must use a project conversation, one explicit Sync only, keep Native UI visible, prove covered `manual_sync_covered` + `route=conversation` + page-owned live continuation without a second Sync, then allow natural completion and verify terminal/final convergence before exporting diagnostics.

'''

docs = [
    'docs/project/PROJECT_STATE.md',
    'docs/project/MODULE_STATUS.md',
    'docs/project/DEVELOPMENT_PLAN.md',
    'docs/project/WEB_SEND_ADAPTER.md',
    'docs/project/TECHNICAL_DECISIONS.md',
]
for name in docs:
    p = Path(name)
    text = p.read_text()
    marker = block.splitlines()[0]
    if marker in text:
        continue
    pos = text.find('\n\n')
    if pos < 0:
        raise SystemExit(f'heading separator missing: {name}')
    p.write_text(text[:pos + 2] + block + text[pos + 2:])

idx = Path('docs/project/BUILD_TEST_INDEX.md')
text = idx.read_text()
row = '| `DEV-send-stream-0.1.0-b92` | `DEV-send-stream` | `0.1.0 (92)` | exact covered-form cleanup product `96ea3e3d8c5cabf67ff33331d40c9dcc6c9f0850`; exact product/config package source `54b5803a74a123431f0a2a8e662a1a2fe874b3ca`; PR #29 | staging `33750363774/100632281401` exact guard+two-file scope+Simulator passed; Push `33750585725/100632980237` passed; PR `33750591494/100632998279` passed; canonical Push Artifact `9891430379`; Artifact `sha256:f3cb6291fabcb2cf48729750d23a4403607e8ac81dc4354749974e287412e970`; IPA `sha256:82d96d359767b72c623f367bf3cd2c5f3ae9d1d7411ad547c1ba3634341c3514`; package `0.1.0 (92)` / Candidate b92 / source `54b5803a74a1` / iOS14 / `[1,2]` / arm64 | Runtime pending: project covered-form live continuation plus natural terminal/final completion after one Sync, no second Sync | **Code/guarded scope+Simulator/Push+PR CI/Artifact/package verified; Runtime Unverified; Stable-Frozen No; permanently reserved** |\n'
if row.strip() not in text:
    anchor = '| `DEV-send-stream-0.1.0-b91` |'
    pos = text.find(anchor)
    if pos < 0:
        raise SystemExit('b91 index anchor missing')
    idx.write_text(text[:pos] + row + text[pos:])

cp = Path('docs/project/current/dev/DEV-send-stream.md')
text = cp.read_text()
old_status = '**Active — exact b91 project route identity and official page-owned live continuation are Runtime Positive on iPhone/iOS17. Web -> bridge -> `ConversationRepository` progressive projection works without a second Sync. The remaining visible Web-page trap is the intentionally retained b90 `bringSubviewToFront` diagnostic, not a transport failure. Automatic terminal/final convergence remains Unverified because the app was force-quit while still streaming. Stable/Frozen Send remains No.**'
new_status = '**Active — exact b91 project route identity and page-owned live continuation are Runtime Positive. Exact b92 removes only the frontmost Web diagnostic and is Code/guarded scope+Simulator/Push+PR CI/Artifact/package verified. Human Runtime must now prove the same live path while covered and natural terminal/final convergence. Stable/Frozen Send remains No.**'
if text.count(old_status) != 1:
    raise SystemExit('checkpoint status marker mismatch')
text = text.replace(old_status, new_status, 1)
old_identity = '- b92 Candidate / Build: `DEV-send-stream-0.1.0-b92` / `0.1.0 (92)` permanently reserved; product/package not yet emitted at allocation checkpoint'
new_identity = '''- b92 Candidate / Build: `DEV-send-stream-0.1.0-b92` / `0.1.0 (92)` permanently reserved
- b92 allocation checkpoint: `296de318c20ccc32bfea1cb93246bd9d824d3403`
- Exact b92 product commit: `96ea3e3d8c5cabf67ff33331d40c9dcc6c9f0850`
- Exact b92 product/config package source: `54b5803a74a123431f0a2a8e662a1a2fe874b3ca`
- b92 Push CI: `33750585725 / 100632980237` — success
- b92 PR CI: `33750591494 / 100632998279` — success
- b92 canonical Push Artifact: `9891430379`
- b92 IPA SHA-256: `82d96d359767b72c623f367bf3cd2c5f3ae9d1d7411ad547c1ba3634341c3514`'''
if text.count(old_identity) != 1:
    raise SystemExit('checkpoint identity marker mismatch')
text = text.replace(old_identity, new_identity, 1)
package = '''## b92 covered-form package / validation state

b92 removes only the b90 frontmost z-order mutation. The executor remains inserted at index 0 and manual rearm now records `manual_sync_covered` without changing z-order; b91 scoped route identity and page-owned continuation logic are unchanged.

Two early staging attempts (`33749925741`, `33750233706`) failed in guard-only tooling before product application. Successful staging `33750363774 / 100632281401` passed exact b91-state guard, exact two-product-file scope audit, and Simulator compile, then emitted product `96ea3e3d8c5cabf67ff33331d40c9dcc6c9f0850`.

Exact product/config package source `54b5803a74a123431f0a2a8e662a1a2fe874b3ca` passed Push CI `33750585725 / 100632980237` and PR CI `33750591494 / 100632998279`. Canonical Push Artifact `9891430379` has digest `sha256:f3cb6291fabcb2cf48729750d23a4403607e8ac81dc4354749974e287412e970`. Independent unpacking verified IPA SHA `82d96d359767b72c623f367bf3cd2c5f3ae9d1d7411ad547c1ba3634341c3514` matching sidecar, Release `0.1.0 (92)`, Candidate b92, source `54b5803a74a1`, MinimumOS 14.0, device family `[1,2]`, iphoneos and Mach-O arm64.

Evidence ladder: **Code written / guarded exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**

## b92 Human Runtime gate

1. Install the exact canonical b92 IPA.
2. In another official client start a long response in a **project conversation**.
3. Open the same project conversation in b92 and press `同步最新消息` exactly once.
4. Native UI must remain visible/usable; official Web must not cover/trap the Native UI.
5. Diagnostics must show `coveredExecutor.webViewActivation` stage `manual_sync_covered`, with the executor still covered, and project page `route=conversation`.
6. While the remote response continues, matching page-owned `externalStreamStatusRequest/Response`, `IS_STREAMING`, `externalStreamingObserved` and/or `externalSnapshot` must advance the existing Native live response without a second Sync.
7. Do **not** force quit. Let the response finish naturally.
8. Verify final assistant content materializes and live response terminalizes/clears automatically without a second Sync, then export diagnostics after completion.

'''
anchor = '## Validation / identity state\n'
if package.splitlines()[0] not in text:
    pos = text.find(anchor)
    if pos < 0:
        raise SystemExit('checkpoint validation anchor missing')
    text = text[:pos] + package + text[pos:]
old_batch = '**Open for b92 covered-form cleanup. Next exact action:** remove only the b90 frontmost z-order mutation while retaining b91 scoped-route identity, page-owned continuation and Repository ownership; validate exact two-file scope + Simulator, then package b92 and stop at Human Runtime for covered live progression + natural terminal/final completion.'
new_batch = '**Closed for b92 product/package/docs preparation. Next exact action:** install exact canonical b92 and execute the b92 Human Runtime gate through covered live progression and natural terminal/final completion. No product/config change is permitted before that Runtime evidence.'
if text.count(old_batch) != 1:
    raise SystemExit('checkpoint batch marker mismatch')
cp.write_text(text.replace(old_batch, new_batch, 1))
