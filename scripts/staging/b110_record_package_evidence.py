from pathlib import Path

BUILD_INDEX = Path("docs/project/BUILD_TEST_INDEX.md")
CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
PROJECT_STATE = Path("docs/project/PROJECT_STATE.md")
MODULE_STATUS = Path("docs/project/MODULE_STATUS.md")
PROJECT_PROFILE = Path("docs/project/PROJECT_PROFILE.md")

PRODUCT = "55184f057d3303a266146ab6a76be019bf3f1c00"
PACKAGE = "26ea3354998c89420212315977dcf94cc3a91197"
STAGING = "33985483452/101358091966"
PUSH = "33985567667/101358319343"
PR = "33985569950/101358325339"
ARTIFACT = "9975056986"
ZIP_SHA = "2c5d963f915b2b12588416cfbd71668dbb0a5b22e49b53f9a7657732ae24cb20"
IPA_SHA = "7ecb92d4e364e70e6ae9091af7a80386c06cc1aea96993227a54d76b9470fcd4"


def prepend_once(path: Path, marker: str, section: str) -> None:
    text = path.read_text()
    if marker in text:
        return
    path.write_text(section.rstrip() + "\n\n" + text)


def update_build_index() -> None:
    text = BUILD_INDEX.read_text()
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| `DEV-send-stream-0.1.0-b110`"):
            lines[index] = (
                f"| `DEV-send-stream-0.1.0-b110` | `DEV-send-stream` | `0.1.0 (110)` | rendered-color diagnostic product `{PRODUCT}`; package `{PACKAGE}`; PR #29 | staging `{STAGING}` exact two-product-path scope + `git diff --check` + Debug Simulator passed; Push `{PUSH}` passed; PR `{PR}` passed on exact package source; canonical Artifact `{ARTIFACT}`; ZIP `{ZIP_SHA}`; IPA `{IPA_SHA}`; package independently verified `com.whitesharkssw.chatgptclient` / Build110 / Candidate b110 / source `26ea3354998c` / Release / iOS14+ / `[1,2]` / arm64 | Diagnostic-only Human Runtime pending: reopen the same completed 5-chunk answer, scroll all chunks once, export diagnostics; compare `assistantChunkRender.afterDisplay` label-only versus hierarchy-crop aggregate ink RGB / near-white / blue-dominant fractions. No color fix is claimed | **Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity verified / diagnostic Human Runtime pending / Stable-Frozen No; permanently reserved** |"
            )
            BUILD_INDEX.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))
            return
    raise SystemExit("b110 row not found")


update_build_index()

checkpoint_section = f"""## b110 rendered-color diagnostic package ready — 2026-09-06

Canonical identity:

- Candidate `DEV-send-stream-0.1.0-b110` / `0.1.0 (110)` is permanently reserved.
- Exact product commit `{PRODUCT}` changes only `ChatGPTClient.xcodeproj/project.pbxproj` and `ChatGPTClient/Conversation/ConversationFeature.swift` relative to the b109 product baseline.
- Exact package source `{PACKAGE}` changes only `.github/workflows/ios-foundation.yml` after the product commit.
- Guarded staging `{STAGING}` passed exact scope, `git diff --check`, and Debug Simulator compile.
- Push CI `{PUSH}` and PR CI `{PR}` both passed on exact package source `{PACKAGE}`.
- Canonical Push Artifact `{ARTIFACT}`; Artifact ZIP SHA-256 `{ZIP_SHA}`; IPA `ChatGPTClient-0.1.0-b110-dev-send-stream.ipa` SHA-256 `{IPA_SHA}`.
- Independent package inspection: bundle `com.whitesharkssw.chatgptclient`, `0.1.0 (110)`, Candidate b110, source marker `26ea3354998c`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS, Mach-O arm64.

Diagnostic behavior:

- b110 keeps b109 `assistantChunkColor.willDisplay` model-state logs unchanged.
- On the next main-queue turn after `willDisplay`, only while the same cell remains at the same index path, it emits `assistantChunkRender.afterDisplay` with aggregate rendered ink statistics for the UILabel alone and the same label rectangle from the cell hierarchy, plus alpha/layer-opacity fields.
- The renderer stores no screenshot, pixel buffer, message text, message ID, URL, or content hash. It exports only aggregate counts/fractions/colors.
- Visible body rendering, attributed content, fonts, row geometry, reasoning, user-link behavior, Send/SSE/Repository/recovery, timers/retries and response authority are unchanged.

Human Runtime gate:

1. Install only canonical b110 Artifact `{ARTIFACT}` / IPA SHA `{IPA_SHA}`.
2. Reopen the same completed 5-chunk answer used for b109; no new Send is required.
3. Scroll through all five assistant chunks once and observe which regions are blue vs normal.
4. Export Diagnostics.
5. Compare each `assistantChunkRender.afterDisplay` by `chunkIndex`: `labelRenderInkRGB` / `labelRenderNearWhiteFraction` / `labelRenderBlueDominantFraction` against `hierarchyCropInkRGB` / `hierarchyCropNearWhiteFraction` / `hierarchyCropBlueDominantFraction`.
6. If label-only differs with screen color, investigate inside/below UILabel drawing. If label-only stays white but hierarchy crop differs, investigate sibling/cell composition. If both remain white while physical screen differs, investigate below hierarchy/window compositing. Do not allocate a rendering fix before this evidence.

**Evidence ladder:** b109 model-state diagnostic Runtime Positive for probe / visible color defect persists / b110 Code written / exact scope + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / diagnostic Human Runtime pending / Stable-Frozen No.

**Next exact action:** run the b110 Human Runtime gate above and export Diagnostics; do not judge b110 by whether the color is fixed because it intentionally does not change rendering.
"""
prepend_once(CHECKPOINT, "## b110 rendered-color diagnostic package ready", checkpoint_section)

state_section = f"""## DEV-send-stream b110 rendered-color diagnostic package ready — 2026-09-06

- Canonical b110 product `{PRODUCT}` / package `{PACKAGE}`; staging `{STAGING}`, Push `{PUSH}`, PR `{PR}` all passed.
- Artifact `{ARTIFACT}` / ZIP `sha256:{ZIP_SHA}` / IPA `sha256:{IPA_SHA}` independently verify Build110/Candidate/source/Release/iOS14+/`[1,2]`/arm64.
- b110 is diagnostic-only and compares after-display rendered ink for UILabel-only versus the same cell-hierarchy crop; Human Runtime remains pending and no color fix is claimed.
- Overall `DEV-send-stream`: Active / Runtime Partial / Stable-Frozen No.
"""
prepend_once(PROJECT_STATE, "## DEV-send-stream b110 rendered-color diagnostic package ready", state_section)

module_section = f"""## DEV-send-stream b110 rendered-output probe package — 2026-09-06

- UI probe package is canonical at product `{PRODUCT}`, package `{PACKAGE}`, Artifact `{ARTIFACT}`, IPA `sha256:{IPA_SHA}`; Simulator and both formal CI lanes passed.
- Scope remains diagnostic only: preserve b109 model-state logging and compare rendered UILabel-only versus cell-hierarchy-crop aggregate ink colors after display. No screenshot/content persistence and no visible rendering mutation.
- Send/SSE/Repository/recovery owners are unchanged; accepted clean-EOF recovery remains Unexercised by this color investigation.
- Module remains Active / Runtime Partial / Stable-Frozen No.
"""
prepend_once(MODULE_STATUS, "## DEV-send-stream b110 rendered-output probe package", module_section)

profile_section = f"""## Current DEV-send-stream package-qualified diagnostic candidate — b110 2026-09-06

- `DEV-send-stream-0.1.0-b110` / `0.1.0 (110)` is the current package-qualified diagnostic candidate.
- Product `{PRODUCT}`; package `{PACKAGE}`; Artifact `{ARTIFACT}`; ZIP `sha256:{ZIP_SHA}`; IPA `sha256:{IPA_SHA}`.
- Package independently verified `com.whitesharkssw.chatgptclient`, source `26ea3354998c`, Release, iOS14+, iPhone/iPad families `[1,2]`, arm64.
- Human Runtime diagnostic gate pending; b110 makes no color-fix claim. Stable/Frozen No.
"""
prepend_once(PROJECT_PROFILE, "## Current DEV-send-stream package-qualified diagnostic candidate — b110", profile_section)
