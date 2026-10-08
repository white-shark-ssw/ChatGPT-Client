from pathlib import Path

BUILD_INDEX = Path("docs/project/BUILD_TEST_INDEX.md")
CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
PROJECT_STATE = Path("docs/project/PROJECT_STATE.md")
MODULE_STATUS = Path("docs/project/MODULE_STATUS.md")
PROJECT_PROFILE = Path("docs/project/PROJECT_PROFILE.md")

DIAGNOSTICS_SHA = "37669df4cddc25db7b0d3bb1ae96d54d722aee501fcf3e55888aff636d8edcdf"


def prepend_once(path: Path, marker: str, section: str) -> None:
    text = path.read_text()
    if marker in text:
        return
    path.write_text(section.rstrip() + "\n\n" + text)


def update_build_index() -> None:
    text = BUILD_INDEX.read_text()
    if "DEV-send-stream-0.1.0-b110" in text:
        return
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| `DEV-send-stream-0.1.0-b109`"):
            lines[index] = (
                "| `DEV-send-stream-0.1.0-b109` | `DEV-send-stream` | `0.1.0 (109)` | diagnostic chunk-color product `11e7ec536b986c45811dc449cd2c4f6e442c28df`; package `8c6ea43677f2a0f39c08d6b9ca695c9c2e4a5267`; PR #29 | corrected staging `33984605217/101355720829` exact two-product-path scope + `git diff --check` + Debug Simulator passed; Push `33984671709/101355898061` passed; PR `33984673860/101355903471` passed on exact package source; canonical Artifact `9974791883`; ZIP `743e61fc4f20670d8a6cc5d5afd42f8942e40f2943abe1f9b23e4ca621b43956`; IPA `6c37dfb8496c533ce2d5e4878f22a5b265f7c55e87e9cbfbb9189155fa30096a`; package independently verified `com.whitesharkssw.chatgptclient` / Build109 / Candidate b109 / source `8c6ea43677f2` / Release / iOS14+ / `[1,2]` / arm64 | Runtime diagnostics `sha256:%s` on canonical b109: 16 `assistantChunkColor.willDisplay` samples across two authoritative conversations. The target 5-chunk assistant message produced samples for chunkIndex 0..4, including repeated scroll passes. Every sample resolved `labelTextColor`, attributed foreground at index 0, `labelHighlightedTextColor`, and `labelTintColor` to `rgba:1.000,1.000,1.000,1.000`; label/cell highlighted and selected states were always false; interface style dark; surface authoritative. Target detail remained 2 authoritative messages / 6 presentation rows / 0 live rows / one 5-chunk assistant message / max chunk 1193. User still observed blue/normal alternation, so the exposed UILabel model-state properties do not distinguish the visible colors | **Diagnostic Runtime Positive for probe / visual color defect persists / exposed UILabel model-state owner rejected / superseded for diagnostic priority by b110 / Stable-Frozen No; permanently reserved** |"
                % DIAGNOSTICS_SHA
            )
            b110 = (
                "| `DEV-send-stream-0.1.0-b110` | `DEV-send-stream` | `0.1.0 (110)` | allocated from b109 uniform-white model-state evidence; product source pending; PR #29 | diagnostic-only intended scope: Xcode Build/Candidate + `ConversationFeature.swift`; preserve b109 model-state probe and add privacy-safe after-display rendered-pixel aggregates for the message label and the same label rectangle as drawn by the cell hierarchy; no screenshots or message text persisted | Human Runtime pending: reopen the same completed 5-chunk answer, scroll all chunks once, export diagnostics; compare `assistantChunkRender.afterDisplay` label-only vs hierarchy-crop ink RGB/blue/white fractions. If label render differs, owner is inside/below label draw; if only hierarchy crop differs, owner is sibling/cell compositing; if both remain white while screen differs, move below hierarchy/window compositor | **Allocated diagnostic probe / product staging pending / Human Runtime pending / Stable-Frozen No; permanently reserved** |"
            )
            lines.insert(index, b110)
            BUILD_INDEX.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))
            return
    raise SystemExit("b109 row not found")


update_build_index()

checkpoint_section = f"""## b109 Human Runtime model-state result / b110 rendered-pixel probe allocation — 2026-09-06

Exact b109 Human Runtime evidence:

- Export metadata is canonical Release Build109 / Candidate `DEV-send-stream-0.1.0-b109` / source `8c6ea43677f2` on iPhone iOS17.0. Exact diagnostics SHA-256 `{DIAGNOSTICS_SHA}`.
- The export contains 16 `assistantChunkColor.willDisplay` samples across two authoritative conversations. The target completed answer is still exactly 2 authoritative messages / 6 presentation rows / 0 live rows with one 5-chunk assistant message (`chunkCharacterLimit=1200`, max chunk 1193).
- The target produced samples for every `chunkIndex` 0 through 4, with repeated rows as the user scrolled. Every target sample and every other b109 chunk sample reports the same resolved state: `labelTextColor=rgba:1,1,1,1`, attributed foreground at index 0 `rgba:1,1,1,1`, highlighted text color `rgba:1,1,1,1`, tint `rgba:1,1,1,1`, label/cell highlighted=false, selected=false, interfaceStyle=dark, surface=authoritative.
- The user still observes the answer alternating blue/normal while scrolling. Therefore b109 has successfully rejected all exposed UILabel model-state properties as the differentiating owner. Current assistant source also builds assistant body attributed text with one `.foregroundColor = UIColor.label` attribute; the only `UIColor.systemBlue` body path is the separate user-message Markdown-link renderer, not assistant body rendering.
- Do not add another blind `textColor`, tint, highlight, or attributed-foreground reset. This evidence specifically requires observing the actual rendered output after display.

b110 allocation / evidence-backed scope:

- Allocate and permanently reserve `DEV-send-stream-0.1.0-b110` / `0.1.0 (110)`. No current Build/Test entry or parallel PR #35 candidate uses Build110; PR #35 remains draft research-only with no `ChatGPTClient/**` or product Xcode candidate ownership.
- b110 is diagnostic-only. Preserve b109/b108 rendering, b109 model-state diagnostics, and all b107 Send/SSE/Repository/recovery behavior unchanged.
- Product scope is exactly `ChatGPTClient.xcodeproj/project.pbxproj` plus `ChatGPTClient/Conversation/ConversationFeature.swift`.
- On the next main-queue turn after a chunked assistant cell reaches `willDisplay`, and only if that exact cell is still at the same index path, compute privacy-safe rendered-pixel aggregates for two surfaces: the UILabel alone and the same UILabel rectangle cropped from the cell content hierarchy. Record aggregate ink RGB, near-white fraction, blue-dominant fraction, sampled-pixel count, plus alpha/layer-opacity fields. Never persist or export screenshots, message text, message IDs, pixel buffers, URLs, or content hashes.
- This probe must not change visible rendering, font, attributed content, geometry, Markdown/link behavior, reasoning view, Send behavior, Repository state, timers, retries, recovery, or response authority.

Interpretation gate:

- Label-only rendered aggregate differs blue vs white across visible chunks -> owner is inside/below the UILabel draw/presentation path despite uniform model properties.
- Label-only stays white but hierarchy-crop differs -> owner is outside the label itself, in sibling/cell hierarchy composition.
- Both rendered aggregates remain white while the physical screen still alternates -> move the next investigation below view-hierarchy drawing, toward window/compositor/display presentation; do not guess a color fix.

Resume/conflict guard:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable; pre-b110 branch head `69d9ab56e284e3a32fd3702462c4206b58372520`; canonical b109 product `11e7ec536b986c45811dc449cd2c4f6e442c28df`, package `8c6ea43677f2a0f39c08d6b9ca695c9c2e4a5267`, Artifact `9974791883`.
- `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`. Parallel PR #35 remains draft at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142` with zero product ownership overlap.

**Next exact action:** after this Runtime/allocation checkpoint is durably committed, stage only the two-path b110 rendered-pixel diagnostic, pass `git diff --check` + Debug Simulator compile, package one canonical b110 IPA, then reopen the same completed 5-chunk answer, scroll all chunks once, and export Diagnostics. b110 is not a rendering fix.
"""
prepend_once(CHECKPOINT, "## b109 Human Runtime model-state result / b110 rendered-pixel probe allocation", checkpoint_section)

state_section = f"""## DEV-send-stream b109 model-state Runtime result / b110 render probe — 2026-09-06

- Canonical b109 diagnostics `sha256:{DIAGNOSTICS_SHA}` contain 16 chunk `willDisplay` samples. The target completed authoritative answer remains 2 messages / 6 rows / 0 live rows / one 5-chunk assistant message.
- Every sampled assistant chunk resolves all exposed UILabel text/attributed/highlight/tint colors to white with no highlight/selection state, while the user still observes blue/normal alternation. Exposed UILabel model state is therefore rejected as the differentiating color owner.
- b110 Build110 is reserved as a diagnostic-only after-display rendered-pixel aggregate probe for UILabel-only versus the same rectangle in the cell hierarchy. No color fix is claimed.
- Overall `DEV-send-stream`: Active / Runtime Partial / Stable-Frozen No.
"""
prepend_once(PROJECT_STATE, "## DEV-send-stream b109 model-state Runtime result / b110 render probe", state_section)

module_section = f"""## DEV-send-stream b109 model-state owner rejected / b110 render probe — 2026-09-06

- b109 exact Runtime `sha256:{DIAGNOSTICS_SHA}` proves chunked assistant UILabel model-state fields are uniform white across the target 5 chunks and across 16 total samples, despite visible blue/normal alternation.
- UI investigation moves one layer down: b110 will compare after-display rendered ink aggregates for the UILabel itself versus its rectangle as composited in the cell hierarchy. It must not alter visible rendering.
- Send/SSE/Repository/recovery owners are unchanged; accepted clean-EOF recovery is still Unexercised by these color-only samples.
- Module remains Active / Runtime Partial / Stable-Frozen No.
"""
prepend_once(MODULE_STATUS, "## DEV-send-stream b109 model-state owner rejected / b110 render probe", module_section)

profile_section = f"""## Current DEV-send-stream diagnostic candidate — b110 2026-09-06

- `DEV-send-stream-0.1.0-b110` / `0.1.0 (110)` is permanently reserved as a rendered-output diagnostic probe; product/package source pending staging.
- Trigger evidence is canonical b109 diagnostics `sha256:{DIAGNOSTICS_SHA}`: all exposed UILabel model-state color/highlight/tint values are identical white across the visually divergent long-answer chunks.
- b110 must preserve rendering and log only privacy-safe after-display aggregate pixel/color statistics for label-only and cell-hierarchy crop surfaces. No screenshot/pixel buffer/message content is persisted.
- Stable/Frozen No.
"""
prepend_once(PROJECT_PROFILE, "## Current DEV-send-stream diagnostic candidate — b110", profile_section)
