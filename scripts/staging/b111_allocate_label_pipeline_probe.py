from pathlib import Path

BUILD_INDEX = Path("docs/project/BUILD_TEST_INDEX.md")
CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
PROJECT_STATE = Path("docs/project/PROJECT_STATE.md")
MODULE_STATUS = Path("docs/project/MODULE_STATUS.md")
PROJECT_PROFILE = Path("docs/project/PROJECT_PROFILE.md")
TECHNICAL_DECISIONS = Path("docs/project/TECHNICAL_DECISIONS.md")

DIAGNOSTICS_SHA = "d0a72e850469cd2bb10075c40e01cce3d5e44f20f2eac95f29474d9a2ef5ba81"


def prepend_once(path: Path, marker: str, section: str) -> None:
    text = path.read_text()
    if marker in text:
        return
    path.write_text(section.rstrip() + "\n\n" + text)


def update_build_index() -> None:
    text = BUILD_INDEX.read_text()
    if "DEV-send-stream-0.1.0-b111" in text:
        return
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| `DEV-send-stream-0.1.0-b110`"):
            lines[index] = (
                "| `DEV-send-stream-0.1.0-b110` | `DEV-send-stream` | `0.1.0 (110)` | rendered-color diagnostic product `55184f057d3303a266146ab6a76be019bf3f1c00`; package `26ea3354998c89420212315977dcf94cc3a91197`; PR #29 | staging `33985483452/101358091966` exact two-product-path scope + `git diff --check` + Debug Simulator passed; Push `33985567667/101358319343` passed; PR `33985569950/101358325339` passed on exact package source; canonical Artifact `9975056986`; ZIP `2c5d963f915b2b12588416cfbd71668dbb0a5b22e49b53f9a7657732ae24cb20`; IPA `7ecb92d4e364e70e6ae9091af7a80386c06cc1aea96993227a54d76b9470fcd4`; package independently verified `com.whitesharkssw.chatgptclient` / Build110 / Candidate b110 / source `26ea3354998c` / Release / iOS14+ / `[1,2]` / arm64 | Runtime diagnostics `sha256:%s` on canonical b110, light appearance: target detail remains 2 authoritative messages / 6 presentation rows / 0 live rows / one 5-chunk assistant message. All 12 `assistantChunkColor.willDisplay` samples report black `.label` model/attributed/highlight/tint state with no selection/highlight. Eleven `assistantChunkRender.afterDisplay` samples were captured. Chunk 2 was sampled twice and both UILabel-only `drawHierarchy` renders resolved exactly `0.000,0.479,1.000` with blue-dominant fraction `1.000`; corresponding hierarchy crop was repeatably blue-bearing (`0.960,0.979,1.000`, blue fraction `0.063`). Other label-only samples reported `no_ink_pixels`, but b110 source filters rendered pixels with `max(red,green,blue)>0.18`, so normal black text in light mode is intentionally discarded and those samples cannot be used as a black-vs-blue comparator. This proves blue pixels are already present by UILabel `drawHierarchy` for chunk 2, while the b110 dark-pixel sampler is insufficient to select the exact internal owner | **Diagnostic Runtime Partial / UILabel draw-stage blue captured / exposed model state still black / light-mode dark-pixel comparator invalid / superseded for diagnostic priority by b111 / Stable-Frozen No; permanently reserved** |"
                % DIAGNOSTICS_SHA
            )
            b111 = (
                "| `DEV-send-stream-0.1.0-b111` | `DEV-send-stream` | `0.1.0 (111)` | allocated from b110 UILabel draw-stage system-blue evidence plus b110 light-mode sampler defect; product source pending; PR #29 | diagnostic-only intended scope: Xcode Build/Candidate + `ConversationFeature.swift`; preserve visible rendering, then record privacy-safe full attributed-run summary, cell-reuse provenance, dark-pixel-inclusive transparent label render, direct attributed-string render, CALayer render, and UILabel `drawHierarchy` render for the same chunk | Human Runtime pending: reopen the same completed 5-chunk answer, scroll all chunks, export diagnostics; compare direct attributed draw vs layer render vs hierarchy render and current attributed/link runs. No new Send required | **Allocated diagnostic probe / product staging pending / Human Runtime pending / Stable-Frozen No; permanently reserved** |"
            )
            lines.insert(index, b111)
            BUILD_INDEX.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))
            return
    raise SystemExit("b110 row not found")


update_build_index()

checkpoint_section = f"""## b110 Human Runtime rendered-output result / b111 label-pipeline probe allocation — 2026-09-06

Exact b110 Human Runtime evidence:

- Export metadata is canonical Release Build110 / Candidate `DEV-send-stream-0.1.0-b110` / source `26ea3354998c` on iPhone iOS17.0. Exact diagnostics SHA-256 `{DIAGNOSTICS_SHA}`.
- Target authoritative Detail remains exactly 2 visible messages / 6 presentation rows / 0 live rows with one 5-chunk assistant message (`chunkCharacterLimit=1200`, max chunk 1193). This remains a completed authoritative rendering reproduction rather than live+authoritative duplication.
- All 12 `assistantChunkColor.willDisplay` samples in this export resolve `labelTextColor`, attributed foreground at index 0, `labelHighlightedTextColor`, and `labelTintColor` to black `rgba:0,0,0,1`; label/cell highlighted and selected states are false; interface style is light. Model state still does not explain a blue chunk.
- Eleven `assistantChunkRender.afterDisplay` samples were captured. Chunk 2 was sampled twice, at separate scroll passes, and both UILabel-only `drawHierarchy` renders report `labelRenderInkRGB=0.000,0.479,1.000`, `labelRenderBlueDominantFraction=1.000`, `labelRenderNearWhiteFraction=0.000`, with 73,612 sampled pixels. The same crop through the cell hierarchy is also repeatably blue-bearing (`hierarchyCropInkRGB=0.960,0.979,1.000`, blue-dominant fraction 0.063). Therefore a compositor/sibling outside UILabel is not required to produce the captured blue pixels: the blue is already present at the UILabel `drawHierarchy` surface for this chunk.
- b110 cannot yet compare that blue chunk cleanly against the normal light-mode chunks. Its `renderedInkDiagnostics` implementation discards any pixel whose unpremultiplied `max(red, green, blue) <= 0.18`. Normal light-mode `.label` is black, so chunks 0/1/3/4 reporting `labelRenderStatus=no_ink_pixels` is an expected sampler blind spot, not proof of missing or white text. Do not interpret those `no_ink_pixels` values as a rendering result.
- Current source still constructs assistant body attributed text with one `.foregroundColor=UIColor.label`; the explicit `UIColor.systemBlue` body path is only the separate user-message Markdown-link renderer. The b110 evidence therefore narrows the next fork to (a) unexpected runtime attributed/link runs appearing after `willDisplay`, (b) UILabel layer/internal draw state, or (c) shared cell/label reuse state. It does not justify another blind color reset.

b111 allocation / evidence-backed scope:

- Allocate and permanently reserve `DEV-send-stream-0.1.0-b111` / `0.1.0 (111)`. `BUILD_TEST_INDEX.md` contains no b111 before this allocation; parallel PR #35 owns no product Candidate or `ChatGPTClient/**` path.
- b111 remains diagnostic-only and must preserve b110/b109/b108 visible rendering plus all inherited Send/SSE/Repository/recovery behavior.
- Product scope is exactly `ChatGPTClient.xcodeproj/project.pbxproj` plus `ChatGPTClient/Conversation/ConversationFeature.swift`.
- For each chunked assistant after-display sample, log privacy-safe structural attributed state only: total attribute-run count, foreground-color run/distinct-color summary, link-run count, attachment-run count, current cell ordinal, and reuse provenance (`reusedFromRole` plus whether the prior attributed value had a link run). Never log text, message ID, URL, range contents, or content hash.
- Add three transparent-background render comparisons using an alpha-only ink selector so black text is retained: direct current `NSAttributedString` drawing, `messageLabel.layer.render(in:)`, and current `messageLabel.drawHierarchy`. Keep the existing b110 metrics for continuity. These images remain in-memory only and only aggregate pixel counts/RGB/blue fraction are exported.
- Interpretation: direct attributed draw blue or link/blue run present -> runtime attributed content owns the color; direct draw black but layer render blue -> UILabel internal layer/cache owns it; layer black but drawHierarchy blue -> UIView hierarchy rendering path owns it. Cell-ordinal/reuse provenance decides whether any blue surface tracks shared user/assistant reuse. No visible fix should be selected before this distinction.

Resume/conflict guard / batch recovery point:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable; verified pre-b111 branch head `a6c38e431aff51cd11a736b6aae4922c6ca418bf`; canonical b110 product `55184f057d3303a266146ab6a76be019bf3f1c00`, package `26ea3354998c89420212315977dcf94cc3a91197`, Artifact `9975056986`.
- `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`. Parallel PR #35 remains draft at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`; its seven changed paths are research/workflow/checkpoint only and have zero product-path overlap.
- Tooling-preparation commits may add only b111 staging scripts/workflow and do not create a product/Candidate Artifact.
- Batch A: durably record this b110 Runtime classification and b111 reservation in checkpoint/index/state/module/profile/technical decisions before product changes.
- Batch B: apply only the exact two-product-path b111 diagnostic delta, run `git diff --check` + Debug Simulator compile, then commit exact product.
- Batch C: bind formal package CI to exact b111 product commit, require same-source Push + PR CI, canonical Artifact and independent IPA identity/hash verification, then record package evidence and update PR #29 before Human Runtime.
- Recovery must not rewrite b110/b109/b108 canonical identities, PR #35, Send/SSE/Repository/recovery logic, user-link styling, or previously reserved Candidates.

**Next exact action:** complete Batch B only after Batch A is durably committed. b111 Human Runtime reopens the same completed 5-chunk answer, scrolls all chunks, exports Diagnostics, and compares direct-attributed / layer / hierarchy rendered color plus attributed-run/reuse provenance. No new Send is required.
"""
prepend_once(CHECKPOINT, "## b110 Human Runtime rendered-output result / b111 label-pipeline probe allocation", checkpoint_section)

state_section = f"""## DEV-send-stream b110 rendered-output Runtime / b111 label-pipeline probe — 2026-09-06

- Canonical b110 diagnostics `sha256:{DIAGNOSTICS_SHA}` keep the target completed answer at 2 authoritative messages / 6 rows / 0 live rows / one 5-chunk assistant message.
- All exposed model-state colors are black `.label` in light appearance. Nevertheless chunk 2's UILabel-only `drawHierarchy` output was independently sampled twice as exact system-blue-like `0.000,0.479,1.000`, so blue is already present by the UILabel drawing surface rather than requiring outer cell/window composition.
- b110's comparator is incomplete for normal light-mode chunks because its ink filter intentionally drops dark pixels (`max RGB <= 0.18`), producing `no_ink_pixels` for black text. Those samples are not a valid black-vs-blue comparison.
- b111 Build111 is reserved as a diagnostic-only label-pipeline probe: full attributed-run summary plus direct attributed draw / CALayer render / UILabel hierarchy render with dark-pixel-inclusive transparent sampling and cell reuse provenance. No color fix is claimed.
- Overall `DEV-send-stream`: Active / Runtime Partial / Stable-Frozen No.
"""
prepend_once(PROJECT_STATE, "## DEV-send-stream b110 rendered-output Runtime / b111 label-pipeline probe", state_section)

module_section = f"""## DEV-send-stream b110 UILabel draw-stage blue / b111 pipeline probe — 2026-09-06

- b110 exact Runtime `sha256:{DIAGNOSTICS_SHA}` captured chunk 2 twice with UILabel-only rendered RGB `0.000,0.479,1.000` while the same row's public UILabel/attributed/highlight/tint state remained black `.label`. Outer cell/window composition is therefore not required for the captured blue pixels.
- The b110 light-mode sampler cannot classify normal black chunks because it filters `max RGB <= 0.18`; `no_ink_pixels` on chunks 0/1/3/4 is a diagnostic blind spot, not a product rendering conclusion.
- b111 will preserve rendering and distinguish runtime attributed data vs UILabel layer/internal draw vs UIView hierarchy draw, with cell reuse provenance. Send/SSE/Repository/recovery owners are unchanged.
- Module remains Active / Runtime Partial / Stable-Frozen No.
"""
prepend_once(MODULE_STATUS, "## DEV-send-stream b110 UILabel draw-stage blue / b111 pipeline probe", module_section)

profile_section = f"""## Current DEV-send-stream diagnostic candidate — b111 2026-09-06

- `DEV-send-stream-0.1.0-b111` / `0.1.0 (111)` is permanently reserved as a label-pipeline diagnostic probe; product/package source pending staging.
- Trigger evidence is canonical b110 diagnostics `sha256:{DIAGNOSTICS_SHA}`: UILabel public model state remains black `.label`, but chunk 2's UILabel `drawHierarchy` aggregate is repeatably system-blue-like. b110's dark-pixel filter makes the normal light-mode comparator incomplete.
- b111 must not change visible rendering. It adds only privacy-safe structural attributed-run/reuse diagnostics and corrected transparent direct-attributed/layer/hierarchy rendered-color aggregates.
- Stable/Frozen No.
"""
prepend_once(PROJECT_PROFILE, "## Current DEV-send-stream diagnostic candidate — b111", profile_section)

decision_section = f"""## DEV-send-stream b110 rendered-output interpretation / b111 diagnostic decision — 2026-09-06

- Exact b110 Runtime `sha256:{DIAGNOSTICS_SHA}` proves at least one authoritative assistant chunk reaches UILabel `drawHierarchy` with system-blue-like output while all exposed UILabel model-state fields still resolve to light-mode black `.label`. Do not attribute that captured blue sample solely to an outer cell/window compositor and do not add another blind text/tint/highlight reset.
- b110's existing `renderedInkDiagnostics` is not a valid normal-black comparator in light appearance because it excludes unpremultiplied pixels with `max RGB <= 0.18`. Treat `no_ink_pixels` from normal black chunks as probe insufficiency, not product absence/whiteness.
- Authorize one diagnostic-only b111 split of the label pipeline: summarize current attributed color/link runs without content, render the current attributed string directly, render the UILabel layer, and render the UILabel hierarchy using transparent alpha-based ink selection that retains black. Add process-local cell reuse provenance solely to test whether exact systemBlue follows shared user/assistant cell state.
- b111 changes no visible rendering, role styling, user-link behavior, Send/SSE/Repository/recovery state, retry/timer policy or response authority. A rendering fix remains unauthorized until this probe selects the internal owner.
"""
prepend_once(TECHNICAL_DECISIONS, "## DEV-send-stream b110 rendered-output interpretation / b111 diagnostic decision", decision_section)
