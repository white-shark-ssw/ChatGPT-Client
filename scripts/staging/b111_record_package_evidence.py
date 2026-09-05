from pathlib import Path

BUILD_INDEX = Path("docs/project/BUILD_TEST_INDEX.md")
CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
PROJECT_STATE = Path("docs/project/PROJECT_STATE.md")
MODULE_STATUS = Path("docs/project/MODULE_STATUS.md")
PROJECT_PROFILE = Path("docs/project/PROJECT_PROFILE.md")

PRODUCT = "64351b96bd61a44e8566e2264c5593fae868268e"
PACKAGE = "4297846dd6889905cbc765c23f83b33ee54437f5"
STAGING = "33986923145/101362120447"
PUSH = "33987037286/101362430240"
PR = "33987039485/101362436599"
ARTIFACT = "9975489792"
ZIP_SHA = "82c512fd4d82ce5a3fcb73f9b6d9cf2314382874fa9544ae5bbbde47fcd209a6"
IPA_SHA = "071cd06933388654e0cd86ca626e1305df08f28f90e1e0626caf0f7dc10e059a"
RUNTIME_SHA = "d0a72e850469cd2bb10075c40e01cce3d5e44f20f2eac95f29474d9a2ef5ba81"


def prepend_once(path: Path, marker: str, section: str) -> None:
    text = path.read_text()
    if marker in text:
        return
    path.write_text(section.rstrip() + "\n\n" + text)


def update_build_index() -> None:
    text = BUILD_INDEX.read_text()
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| `DEV-send-stream-0.1.0-b111`"):
            lines[index] = (
                f"| `DEV-send-stream-0.1.0-b111` | `DEV-send-stream` | `0.1.0 (111)` | label-pipeline diagnostic product `{PRODUCT}`; package `{PACKAGE}`; PR #29 | staging `{STAGING}` exact two-product-path scope + `git diff --check` + Debug Simulator passed; Push `{PUSH}` passed; PR `{PR}` passed on exact package source; canonical Artifact `{ARTIFACT}`; ZIP `{ZIP_SHA}`; IPA `{IPA_SHA}`; package independently verified `com.whitesharkssw.chatgptclient` / Build111 / Candidate b111 / source `4297846dd688` / Release / iOS14+ / `[1,2]` / arm64 | Diagnostic-only Human Runtime pending: reopen the same completed 5-chunk answer, scroll all chunks once, export diagnostics; compare attributed run/link structure and reuse provenance against `directAttributedTransparent`, `labelLayerTransparent`, and `labelHierarchyTransparent`. No color fix is claimed | **Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity verified / diagnostic Human Runtime pending / Stable-Frozen No; permanently reserved** |"
            )
            BUILD_INDEX.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))
            return
    raise SystemExit("b111 row not found")


update_build_index()

checkpoint_section = f"""## b111 label-pipeline diagnostic package ready — 2026-09-06

Canonical identity:

- Candidate `DEV-send-stream-0.1.0-b111` / `0.1.0 (111)` is permanently reserved.
- Exact product commit `{PRODUCT}` changes only `ChatGPTClient.xcodeproj/project.pbxproj` and `ChatGPTClient/Conversation/ConversationFeature.swift` relative to the Batch-A b111 allocation checkpoint.
- Exact package source `{PACKAGE}` changes only `.github/workflows/ios-foundation.yml` after the product commit.
- Guarded staging `{STAGING}` passed exact two-product-path scope, `git diff --check`, and Debug Simulator compile.
- Push CI `{PUSH}` and PR CI `{PR}` both passed on exact package source `{PACKAGE}`.
- Canonical Push Artifact `{ARTIFACT}`; Artifact ZIP SHA-256 `{ZIP_SHA}`; IPA `ChatGPTClient-0.1.0-b111-dev-send-stream.ipa` SHA-256 `{IPA_SHA}`.
- Independent package inspection verifies bundle `com.whitesharkssw.chatgptclient`, `0.1.0 (111)`, Candidate b111, source marker `4297846dd688`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS, Mach-O arm64. The packaged SHA sidecar matches `{IPA_SHA}`.

Diagnostic behavior / inherited Runtime truth:

- Trigger evidence remains canonical b110 Runtime `sha256:{RUNTIME_SHA}`: all public UILabel/attributed/highlight/tint state is light-mode black `.label`, while chunk 2's UILabel-only `drawHierarchy` aggregate was repeatably system-blue-like. b110's brightness-gated sampler discarded normal black text and therefore could not select the exact label-internal owner.
- b111 preserves b110 visible rendering, b110/b109 existing probes, user-link `systemBlue`, reasoning presentation and all Send/SSE/Repository/recovery behavior.
- b111 adds privacy-safe structural attributed diagnostics (`attributeRunCount`, foreground color summary, link/attachment counts), per-cell reuse provenance, and three dark-pixel-inclusive transparent rendered aggregates: direct current attributed-string draw, `messageLabel.layer.render(in:)`, and `messageLabel.drawHierarchy`.
- No screenshot/pixel buffer/message text/message ID/URL/content hash is persisted or exported. No retry/timer/watchdog/polling/duplicate Send/response authority is added.

Human Runtime gate:

1. Install only canonical b111 Artifact `{ARTIFACT}` / IPA SHA `{IPA_SHA}`.
2. Reopen the same completed 5-chunk answer used for b109/b110; no new Send is required.
3. Scroll through all five assistant chunks once, including the visually blue region, then export Diagnostics.
4. Compare each `assistantChunkRender.afterDisplay` by chunk index: `foregroundDistinctColors`, `linkRunCount`, `cellOrdinal`, `reusedFromRole`, `reusedFromLinkRunCount`, `directAttributedTransparentInkRGB`, `labelLayerTransparentInkRGB`, and `labelHierarchyTransparentInkRGB` plus blue-dominant fractions.
5. Direct attributed draw blue or an actual blue/link run -> attributed runtime content owner. Direct black but layer blue -> UILabel layer/internal draw/cache owner. Layer black but hierarchy blue -> UIView hierarchy draw owner. Blue tracking `reusedFromRole=user` / prior link runs strengthens shared-cell reuse as the causal boundary.
6. Do not select or claim a rendering fix until this diagnostic evidence distinguishes the owner.

**Evidence ladder:** b110 UILabel draw-stage blue Runtime captured / b110 normal-black comparator incomplete / b111 Code written / exact scope + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / diagnostic Human Runtime pending / Stable-Frozen No.

**Next exact action:** run only the b111 Human Runtime diagnostic gate above and export Diagnostics. b111 intentionally does not change the visible color defect.
"""
prepend_once(CHECKPOINT, "## b111 label-pipeline diagnostic package ready", checkpoint_section)

state_section = f"""## DEV-send-stream b111 label-pipeline diagnostic package ready — 2026-09-06

- Canonical b111 product `{PRODUCT}` / package `{PACKAGE}`; staging `{STAGING}`, Push `{PUSH}`, and PR `{PR}` all passed.
- Artifact `{ARTIFACT}` / ZIP `sha256:{ZIP_SHA}` / IPA `sha256:{IPA_SHA}` independently verify Build111/Candidate/source/Release/iOS14+/`[1,2]`/arm64.
- b111 remains diagnostic-only. It preserves visible rendering and compares attributed-runtime structure plus direct attributed draw, UILabel layer render, UILabel hierarchy render, and shared-cell reuse provenance after the b110 draw-stage blue finding.
- Human Runtime diagnostic pending. Overall `DEV-send-stream`: Active / Runtime Partial / Stable-Frozen No.
"""
prepend_once(PROJECT_STATE, "## DEV-send-stream b111 label-pipeline diagnostic package ready", state_section)

module_section = f"""## DEV-send-stream b111 label-pipeline probe package — 2026-09-06

- Canonical b111 product `{PRODUCT}`, package `{PACKAGE}`, Artifact `{ARTIFACT}`, IPA `sha256:{IPA_SHA}`; exact scope + Debug Simulator and both formal CI lanes passed.
- UI scope is diagnostic-only: full attributed run/link summary, process-local cell reuse provenance, and corrected alpha-based direct-attributed/layer/hierarchy aggregate color capture. Visible rendering and user-link behavior remain unchanged.
- Send/SSE/Repository/recovery owners are unchanged; accepted clean-EOF recovery remains Unexercised by these color-only samples.
- Module remains Active / Runtime Partial / Stable-Frozen No.
"""
prepend_once(MODULE_STATUS, "## DEV-send-stream b111 label-pipeline probe package", module_section)

profile_section = f"""## Current DEV-send-stream package-qualified diagnostic candidate — b111 2026-09-06

- `DEV-send-stream-0.1.0-b111` / `0.1.0 (111)` is the current package-qualified diagnostic candidate.
- Product `{PRODUCT}`; package `{PACKAGE}`; Artifact `{ARTIFACT}`; ZIP `sha256:{ZIP_SHA}`; IPA `sha256:{IPA_SHA}`.
- Package independently verified `com.whitesharkssw.chatgptclient`, source `4297846dd688`, Release, iOS14+, iPhone/iPad families `[1,2]`, arm64.
- Human Runtime label-pipeline diagnostic gate pending; b111 makes no color-fix claim. Stable/Frozen No.
"""
prepend_once(PROJECT_PROFILE, "## Current DEV-send-stream package-qualified diagnostic candidate — b111", profile_section)
