from pathlib import Path

BUILD_INDEX = Path("docs/project/BUILD_TEST_INDEX.md")
CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
PROJECT_STATE = Path("docs/project/PROJECT_STATE.md")
MODULE_STATUS = Path("docs/project/MODULE_STATUS.md")
PROJECT_PROFILE = Path("docs/project/PROJECT_PROFILE.md")

PRODUCT = "11e7ec536b986c45811dc449cd2c4f6e442c28df"
PACKAGE = "8c6ea43677f2a0f39c08d6b9ca695c9c2e4a5267"
STAGING_RUN = "33984605217/101355720829"
PUSH_RUN = "33984671709/101355898061"
PR_RUN = "33984673860/101355903471"
ARTIFACT = "9974791883"
ZIP_SHA = "743e61fc4f20670d8a6cc5d5afd42f8942e40f2943abe1f9b23e4ca621b43956"
IPA_SHA = "6c37dfb8496c533ce2d5e4878f22a5b265f7c55e87e9cbfbb9189155fa30096a"
RUNTIME_SHA = "c26f5ed8712ca63c8dae037e58330d5fa4b2f7cb47b8b0dafc078e920b4c813c"
VIDEO_SHA = "6cecee7a5f249529c72c53ee08620740e9d8480b080d8914476f697ad0efdc73"


def prepend_once(path: Path, marker: str, section: str) -> None:
    text = path.read_text()
    if marker in text:
        return
    path.write_text(section.rstrip() + "\n\n" + text)


def update_build_index() -> None:
    text = BUILD_INDEX.read_text()
    lines = text.splitlines()
    prefix = "| `DEV-send-stream-0.1.0-b109`"
    matches = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(matches) != 1:
        raise SystemExit(f"expected one b109 row, found {len(matches)}")
    lines[matches[0]] = (
        f"| `DEV-send-stream-0.1.0-b109` | `DEV-send-stream` | `0.1.0 (109)` | diagnostic chunk-color product `{PRODUCT}`; package `{PACKAGE}`; PR #29 | corrected staging `{STAGING_RUN}` exact two-product-path scope + `git diff --check` + Debug Simulator passed; Push `{PUSH_RUN}` passed; PR `{PR_RUN}` passed on exact package source; canonical Artifact `{ARTIFACT}`; ZIP `{ZIP_SHA}`; IPA `{IPA_SHA}`; package independently verified `com.whitesharkssw.chatgptclient` / Build109 / Candidate b109 / source `8c6ea43677f2` / Release / iOS14+ / `[1,2]` / arm64. Earlier staging `33984476631` and `33984523733` stopped in docs-only allocation scope guards before product Batch B and produced no candidate Artifact | Diagnostic-only Human Runtime pending: open the same completed long authoritative answer (or another completed assistant answer with multiple 1200-char chunks), scroll through all assistant chunks once, export diagnostics, and correlate `assistantChunkColor.willDisplay` `labelTextColor` / `attributedForegroundColor` / highlighted/tint/selection state with visible blue/normal chunk rows. No color rendering change is claimed and no new Send is required | **Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity verified / diagnostic Human Runtime pending / Stable-Frozen No; permanently reserved** |"
    )
    BUILD_INDEX.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))


update_build_index()

checkpoint_section = f"""## b109 authoritative chunk-color diagnostic probe — package ready 2026-09-06

Canonical identity / validation:

- Candidate `DEV-send-stream-0.1.0-b109` / `0.1.0 (109)`, permanently reserved. This is a diagnostic probe, not a rendering fix.
- Exact product commit `{PRODUCT}`; canonical package source `{PACKAGE}`.
- Corrected guarded staging `{STAGING_RUN}` passed Batch A durable b108 Runtime/b109 allocation, exact two-product-path diagnostic scope, `git diff --check`, Debug Simulator compile and exact product commit. Earlier attempts `33984476631` and `33984523733` failed only the docs-only allocation path-order assertion before product Batch B; they produced no b109 product commit or Artifact and are not product failures.
- Formal Push `{PUSH_RUN}` and PR `{PR_RUN}` both passed on exact package source `{PACKAGE}`.
- Canonical Push Artifact `{ARTIFACT}`; GitHub Artifact digest and independently recomputed ZIP SHA-256 both `{ZIP_SHA}`.
- Canonical IPA `ChatGPTClient-0.1.0-b109-dev-send-stream.ipa`; independent SHA-256 `{IPA_SHA}`, matching the packaged sidecar.
- Independent package inspection verifies `com.whitesharkssw.chatgptclient`, `0.1.0 (109)`, Candidate b109, source marker `8c6ea43677f2`, `DiagnosticsBuildConfiguration=Release`, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS and required arm64.

Exact diagnostic behavior:

- Product scope is exactly Xcode Build/Candidate 108 -> 109 plus `ConversationFeature.swift` privacy-safe chunk color telemetry.
- b108 rendering behavior is preserved. `ConversationMessageCell.bodyColorDiagnostics()` reads only resolved UILabel `textColor`, attributed foreground at index 0, `highlightedTextColor`, tint, label/cell highlighted and selected state, and interface style; it logs no message text or IDs.
- Detail-table `willDisplay` emits `assistantChunkColor.willDisplay` only for chunked assistant rows, with `surface`, row/chunk index/count and the cell color snapshot. Both authoritative and live surfaces are distinguishable.
- No final rendering color/font/attributed content, geometry, Markdown, link styling, reasoning view, Send/SSE parsing, Repository state, timer, retry, recovery or response authority changed in b109.

Inherited Runtime truth:

- b108 diagnostics `sha256:{RUNTIME_SHA}` / video `sha256:{VIDEO_SHA}` remain the trigger evidence: ordinary one-Send/normal terminal/authoritative reconcile is Positive; accepted `stream_ended_without_done` remains Unexercised; completed authoritative chunk-row color consistency is Runtime Negative.
- b109 does not claim a color fix. Its Human Runtime gate is diagnostic: install only canonical b109, open the same completed long answer if available (otherwise another completed assistant answer spanning multiple 1200-character chunks), scroll across all chunks once, visually note which chunks are blue/normal, then export diagnostics. Compare `assistantChunkColor.willDisplay` fields by chunk index. A new Send is unnecessary for this gate.

Evidence ladder:

- **b108 normal Send/terminal/reconcile Runtime Positive / b107 accepted-clean-EOF recovery Unexercised / b108 authoritative chunk-row color Runtime Negative / b109 Code written / exact scope + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / diagnostic Human Runtime pending / Stable-Frozen No.**

**Next exact action:** install canonical b109 IPA `{IPA_SHA}`, open the existing completed long-answer reproduction, scroll all assistant chunks once, export diagnostics, and use `assistantChunkColor.willDisplay` to select the actual final color owner before any b110 rendering change. Do not allocate a rendering-fix candidate from guesswork.
"""
prepend_once(CHECKPOINT, "## b109 authoritative chunk-color diagnostic probe — package ready", checkpoint_section)

state_section = f"""## DEV-send-stream b109 package-qualified diagnostic Runtime gate — 2026-09-06

- Candidate `DEV-send-stream-0.1.0-b109` / product `{PRODUCT}` / package `{PACKAGE}` is package-qualified after corrected staging `{STAGING_RUN}`, Push `{PUSH_RUN}` and PR `{PR_RUN}` success.
- Canonical Artifact `{ARTIFACT}` / ZIP `{ZIP_SHA}` / IPA `{IPA_SHA}` independently verifies Build109, Candidate b109, source `8c6ea43677f2`, Release, iOS14+, iPhone/iPad and arm64.
- b109 is diagnostic-only: per-chunk assistant `willDisplay` logs final UILabel/attributed/highlight/tint/selection state without message text/IDs and without changing rendering or Send/SSE/Repository/recovery behavior.
- Human Runtime diagnostic pending. b108 chunk-row color remains Runtime Negative; b107 accepted clean-EOF recovery remains Unexercised.
- Overall `DEV-send-stream`: Active / Runtime Partial / Stable-Frozen No.
"""
prepend_once(PROJECT_STATE, "## DEV-send-stream b109 package-qualified diagnostic Runtime gate", state_section)

module_section = f"""## DEV-send-stream b109 chunk-color diagnostic package qualification — 2026-09-06

- UI behavior is unchanged from b108; b109 only exposes privacy-safe final color state for each chunked assistant cell at `willDisplay` so blue/normal authoritative chunks can be compared with their actual UILabel/attributed/highlight/tint/selection state.
- `ConversationRepository`, covered Send executor, New Chat authoritative handoff, b107 accepted-client recovery, row geometry and message content authority are unchanged.
- Exact product `{PRODUCT}` / package `{PACKAGE}` passed corrected staging and same-source Push + PR packaging; canonical Artifact `{ARTIFACT}` / IPA `{IPA_SHA}` is verified.
- Diagnostic Human Runtime remains Pending; module remains Active / Runtime Partial / Stable-Frozen No.
"""
prepend_once(MODULE_STATUS, "## DEV-send-stream b109 chunk-color diagnostic package qualification", module_section)

profile_section = f"""## Current DEV-send-stream diagnostic candidate — b109 package ready 2026-09-06

- Package-qualified diagnostic Human Runtime candidate: `DEV-send-stream-0.1.0-b109` / `0.1.0 (109)`.
- Exact product `{PRODUCT}`; canonical package source `{PACKAGE}`; canonical Artifact `{ARTIFACT}`; ZIP `sha256:{ZIP_SHA}`; IPA `sha256:{IPA_SHA}`.
- Package identity independently verified: `com.whitesharkssw.chatgptclient`, Release iPhoneOS, iOS14+, UIDeviceFamily `[1,2]`, arm64, diagnostics source marker `8c6ea43677f2`.
- b109 is diagnostics-only and must not be reported as a color fix. Human Runtime must correlate chunk-indexed `assistantChunkColor.willDisplay` state with visible blue/normal authoritative chunks before any rendering correction is selected.
- Stable/Frozen No; inherited accepted-clean-EOF recovery remains Unexercised.
"""
prepend_once(PROJECT_PROFILE, "## Current DEV-send-stream diagnostic candidate — b109 package ready", profile_section)
