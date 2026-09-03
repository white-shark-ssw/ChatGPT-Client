from pathlib import Path

PACKAGE_SOURCE = "2d2cde58a7fbc7e6bdc1cd32fd52e73fc6ed1fb0"
PRODUCT = "556bd8886061f4126d11e4ac44f4e24ed580500c"
ALLOCATION = "b86c1a3ca94b215204b0cfb135fa0cd8b3603619"
IPA_SHA = "379218aa869b566c26e582a220be34a025a11517c8ebee1f9ce631140ea32a2d"
ARTIFACT_DIGEST = "sha256:5a07512a1bf3becac3a8d2a7655c3d3f09caa150c1162b95327e40b3c8ed2ad5"


def prepend(path: str, heading: str, body: str) -> None:
    p = Path(path)
    s = p.read_text()
    marker = f"## {heading}"
    if marker in s:
        return
    lines = s.splitlines(True)
    assert lines and lines[0].startswith("# ")
    p.write_text(lines[0] + "\n" + marker + "\n\n" + body.rstrip() + "\n\n" + "".join(lines[1:]).lstrip("\n"))


checkpoint = Path("docs/project/current/dev/DEV-send-stream.md")
s = checkpoint.read_text()
assert "DEV-send-stream-0.1.0-b93" in s
assert "product/package pending at allocation checkpoint" in s
s = s.replace(
    "**Active — exact b92 proves the covered project page-owned continuation path and client-owned protected Send/SSE terminal path on iPhone/iOS17. A narrower overlap regression remains: after switching away from an externally streaming conversation and starting a client-owned Send in another executor, the first external page-owned loop stops advancing and does not reacquire automatically on reselection; final assistant materializes only after explicit Sync. Stable/Frozen Send remains No.**",
    "**Active — exact b92 proves covered single-conversation external continuation and client-owned Send/SSE terminal reconciliation, but overlap/reselection recovery is Runtime Negative. Exact b93 is Code/guarded two-file scope+Simulator/Push+PR CI/Artifact/package verified and tests only selection-time focus reacquisition for an already-active external executor. Human Runtime pending. Stable/Frozen Send remains No.**",
    1,
)
s = s.replace(
    "- b93 Candidate / Build: `DEV-send-stream-0.1.0-b93` / `0.1.0 (93)` permanently reserved; product/package pending at allocation checkpoint\n",
    f"- b93 Candidate / Build: `DEV-send-stream-0.1.0-b93` / `0.1.0 (93)` permanently reserved\n- b93 allocation checkpoint: `{ALLOCATION}`\n- Exact b93 product commit: `{PRODUCT}`\n- Exact b93 product/config package source: `{PACKAGE_SOURCE}`\n- b93 staging: `33754848709 / 100646690995` — success\n- b93 Push CI: `33755063112 / 100647405265` — success\n- b93 PR CI: `33755067202 / 100647418537` — success\n- b93 canonical Push Artifact: `9893141097`\n- b93 IPA SHA-256: `{IPA_SHA}`\n",
    1,
)
s = s.replace(
    "b91/b92 exact package identities remain permanently reserved. b93 is allocated only for selection-time external focus reacquisition; product/package is pending.",
    f"b91/b92 exact package identities remain permanently reserved. Exact b93 product `{PRODUCT}` and package source `{PACKAGE_SOURCE}` are fixed; later docs/tooling commits do not redefine that package identity.",
    1,
)
s = s.replace(
    "**Open for b93 selection-focus A/B. Next exact action:** apply only selection-time focus reacquisition to the existing external-live executor, validate exact two-file product scope + Simulator, then package b93 and stop at Human Runtime. Do not modify continuation protocol or add speculative recovery logic.",
    "**Closed for b93 product/package/docs preparation. Next exact action:** install exact canonical b93 and execute the overlap/reselection Human Runtime gate. No product/config change is permitted before that Runtime evidence.",
    1,
)
insert = f'''\n## b93 package / validation state\n\nb93 changes only reselection behavior for an already-active external live response. `reactivateExternalObservationFocus()` keeps the existing covered WebView and route, calls `becomeFirstResponder()`, samples `document.hasFocus()`, and logs `selection_external_focus_rearm` / `selectionFocusActivationAttempt` / `selectionFocusActivationResult`. No page reload, manual Sync, status/resume synthesis, timer, retry, polling, duplicate Send or response-store change was added.\n\nAllocation checkpoint `{ALLOCATION}` precedes product `{PRODUCT}`. Guarded staging `33754848709 / 100646690995` passed the exact b92 state guard, exact two-product-file audit and Simulator compile. Exact product/config package source `{PACKAGE_SOURCE}` passed Push CI `33755063112 / 100647405265` and PR CI `33755067202 / 100647418537`.\n\nCanonical Push Artifact `9893141097` has backend digest `{ARTIFACT_DIGEST}`. Independent unpacking verified `ChatGPTClient-0.1.0-b93-dev-send-stream.ipa`, SHA `{IPA_SHA}` matching sidecar, Release `0.1.0 (93)`, Candidate b93, source `2d2cde58a7fb`, MinimumOS 14.0, device family `[1,2]`, `iphoneos`, and Mach-O arm64.\n\nEvidence ladder: **Code written / guarded exact two-file scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**\n\n## b93 Human Runtime gate\n\n1. Start a long response in a project conversation on another official client.\n2. In b93 select the same conversation and press `同步最新消息` exactly once; confirm covered external snapshots begin.\n3. Switch to a second conversation and send one message from ChatGPTClient; allow its local SSE response to finish naturally.\n4. Return to the original external-live conversation **without pressing Sync**.\n5. Diagnostics must show `selection_external_focus_rearm`, `selectionFocusActivationAttempt`, and `selectionFocusActivationResult`; the decisive focus result is `documentHasFocus=true`.\n6. After reselection, page-owned `externalStreamStatusRequest/Response` and external snapshots must resume for the original response without reload/Sync.\n7. Let the remote response finish naturally and verify the final assistant materializes/reconciles automatically. Export diagnostics after completion.\n\nIf focus is reacquired and continuation resumes, selection-time focus reacquisition is Runtime Positive. If focus is reacquired but continuation remains frozen while the remote answer advances, reject focus reacquisition as sufficient and continue from that evidence without speculative protocol work.\n'''
anchor = "\n## Validation / identity state\n"
assert anchor in s and "## b93 package / validation state" not in s
s = s.replace(anchor, insert + anchor, 1)
checkpoint.write_text(s)

# BUILD_TEST_INDEX: add b93 and replace b92 Runtime pending wording.
p = Path("docs/project/BUILD_TEST_INDEX.md")
s = p.read_text()
b92 = "| `DEV-send-stream-0.1.0-b92` | `DEV-send-stream` | `0.1.0 (92)` |"
assert b92 in s
if "| `DEV-send-stream-0.1.0-b93` |" not in s:
    row = f"| `DEV-send-stream-0.1.0-b93` | `DEV-send-stream` | `0.1.0 (93)` | selection-focus A/B product `{PRODUCT}`; exact package source `{PACKAGE_SOURCE}`; PR #29 | staging `33754848709/100646690995` exact two-file scope+Simulator passed; Push `33755063112/100647405265` passed; PR `33755067202/100647418537` passed; canonical Artifact `9893141097`; Artifact `{ARTIFACT_DIGEST}`; IPA `sha256:{IPA_SHA}`; package b93/source `2d2cde58a7fb`/iOS14/`[1,2]`/arm64 | Human Runtime pending: overlap external stream -> local Send -> reselect external stream without Sync, focus rearm must restore page-owned continuation and natural final reconcile | **Code/guarded scope+Simulator/Push+PR CI/Artifact/package verified; Runtime Unverified; Stable-Frozen No; permanently reserved** |\n"
    s = s.replace(b92, row + b92, 1)
s = s.replace(
    "Runtime pending: project covered-form live continuation plus natural terminal/final completion after one Sync, no second Sync | **Code/guarded scope+Simulator/Push+PR CI/Artifact/package verified; Runtime Unverified; Stable-Frozen No; permanently reserved**",
    "**Runtime Partial:** covered project continuation advances automatically while selected; client-owned Send/SSE reaches terminal and authoritative reconcile automatically; overlap/reselection is Runtime Negative because external live froze after focus/context handoff and final required explicit Sync | **Covered continuation + local terminal Runtime Positive; overlap/reselection recovery Runtime Negative; Stable-Frozen No; permanently reserved**",
    1,
)
p.write_text(s)

common = f'''- Exact b92 Runtime is Partial: covered external continuation works and client-owned protected Send/SSE natural terminal reconciliation works, but when an external live executor overlaps a second client-owned Send, the first stream can stop advancing and does not recover merely by reselection; explicit Sync later materialized the already-completed assistant.\n- Exact b93 tests one evidence-backed variable only: when reselecting an already-active external response, reuse the existing covered executor and restore WKWebView first-responder/document focus without reload or Sync.\n- b93 identity: allocation `{ALLOCATION}`, product `{PRODUCT}`, package source `{PACKAGE_SOURCE}`, Push `33755063112/100647405265`, PR `33755067202/100647418537`, Artifact `9893141097`, IPA SHA `{IPA_SHA}`.\n- b93 package inspection: `0.1.0 (93)`, Candidate `DEV-send-stream-0.1.0-b93`, source `2d2cde58a7fb`, iOS14+, `[1,2]`, iphoneos, arm64. Human Runtime pending; Stable/Frozen Send No.\n- Preserved boundary: official page owns continuation transport, Repository owns Native content. No polling/retry/watchdog/timer, Native status/resume synthesis, guessed offset, duplicate Send, WebSocket-body authority, or second response store.\n'''
prepend("docs/project/PROJECT_STATE.md", "DEV-send-stream b93 selection-focus package-ready override — 2026-09-03", common)
prepend("docs/project/MODULE_STATUS.md", "DEV-send-stream b93 selection-focus package-ready override — 2026-09-03", common)
prepend("docs/project/DEVELOPMENT_PLAN.md", "DEV-send-stream b93 selection-focus Runtime gate — 2026-09-03", common + "- Next exact action: install exact b93; reproduce external A -> local B Send -> reselect A without Sync; require selection focus rearm and resumed page-owned continuation through natural final.\n")
prepend("docs/project/TECHNICAL_DECISIONS.md", "DEV-send-stream b93 selection-focus A/B decision — 2026-09-03", common + "- This is an A/B, not a declared root-cause fix: b92 blur events lacked executor identity, so focus handoff remains the strongest evidenced differential, not proven causality.\n")
prepend("docs/project/WEB_SEND_ADAPTER.md", "DEV-send-stream b93 external reselection focus A/B — 2026-09-03", common + "- On external-live reselection b93 calls only `becomeFirstResponder()` plus `document.hasFocus()` diagnostics on the existing executor. It does not reload the page or initiate a Native continuation request.\n")
prepend("docs/project/PROJECT_PROFILE.md", "Latest DEV-send-stream candidate override — 2026-09-03", f"- Latest test candidate: `DEV-send-stream-0.1.0-b93` / `0.1.0 (93)`; exact package source `{PACKAGE_SOURCE}`; canonical Artifact `9893141097`; Runtime pending; Stable/Frozen No.\n")
