from pathlib import Path

BUILD_INDEX = Path("docs/project/BUILD_TEST_INDEX.md")
CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
PROJECT_STATE = Path("docs/project/PROJECT_STATE.md")
MODULE_STATUS = Path("docs/project/MODULE_STATUS.md")
PROJECT_PROFILE = Path("docs/project/PROJECT_PROFILE.md")
TECHNICAL_DECISIONS = Path("docs/project/TECHNICAL_DECISIONS.md")

DIAGNOSTICS_SHA = "8b3e7e627c4218f1154b3e325ec6a95b643c8f64d01c18c37693bab3aba6e811"
B111_PRODUCT = "64351b96bd61a44e8566e2264c5593fae868268e"
B111_PACKAGE = "4297846dd6889905cbc765c23f83b33ee54437f5"
B111_ARTIFACT = "9975489792"


def prepend_once(path: Path, marker: str, section: str) -> None:
    text = path.read_text()
    if marker in text:
        return
    path.write_text(section.rstrip() + "\n\n" + text)


def update_build_index() -> None:
    text = BUILD_INDEX.read_text()
    if "DEV-send-stream-0.1.0-b112" in text:
        return
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| `DEV-send-stream-0.1.0-b111`"):
            lines[index] = (
                f"| `DEV-send-stream-0.1.0-b111` | `DEV-send-stream` | `0.1.0 (111)` | label-pipeline diagnostic product `{B111_PRODUCT}`; package `{B111_PACKAGE}`; PR #29 | staging `33986923145/101362120447` exact two-product-path scope + `git diff --check` + Debug Simulator passed; Push `33987037286/101362430240` passed; PR `33987039485/101362436599` passed on exact package source; canonical Artifact `{B111_ARTIFACT}`; ZIP `82c512fd4d82ce5a3fcb73f9b6d9cf2314382874fa9544ae5bbbde47fcd209a6`; IPA `071cd06933388654e0cd86ca626e1305df08f28f90e1e0626caf0f7dc10e059a`; package independently verified `com.whitesharkssw.chatgptclient` / Build111 / Candidate b111 / source `4297846dd688` / Release / iOS14+ / `[1,2]` / arm64 | Runtime diagnostics `sha256:{DIAGNOSTICS_SHA}`: 12 assistant render samples on the same completed 5-chunk authoritative answer. Every current attributed string has exactly one black foreground run, zero link runs and zero attachments; every direct-attributed transparent render is black with blue fraction 0.000. Four CALayer samples are pure system-blue-like (`0.000,0.476,1.000`, blue fraction 1.000): chunk 2 twice and chunk 3 twice. Cell ordinal 3 is black before reuse, then turns blue immediately after reuse from a user row with one prior link run; cell ordinal 1 is first blue after user+link reuse and stays blue on later assistant->assistant reuse. Assistant-only cell ordinals 2 and 4 remain black. This rejects current attributed content as the blue owner and selects persistent UILabel layer/cache contamination initiated by shared user/assistant cell reuse | **Diagnostic Runtime Positive / root-cause boundary selected: shared cross-role cell reuse contaminates UILabel layer state / superseded for fix priority by b112 / Stable-Frozen No; permanently reserved** |"
            )
            b112 = (
                "| `DEV-send-stream-0.1.0-b112` | `DEV-send-stream` | `0.1.0 (112)` | allocated from b111 layer/reuse Runtime evidence; product source pending; PR #29 | intended fix scope: Xcode Build/Candidate + `ConversationFeature.swift`; keep one cell class and all existing rendering/diagnostics, but register/dequeue separate UITableView reuse identifiers for `.user` and `.assistant` so a UILabel that rendered a user Markdown link can never enter the assistant reuse pool | Human Runtime pending: reopen the same completed 5-chunk answer and scroll through all chunks; assistant chunks must remain normal label color and diagnostics must show no assistant cell reused from `user`; existing user link blue behavior must remain intact. No new Send required | **Allocated evidence-backed rendering fix / product staging pending / Human Runtime pending / Stable-Frozen No; permanently reserved** |"
            )
            lines.insert(index, b112)
            BUILD_INDEX.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))
            return
    raise SystemExit("b111 row not found")


update_build_index()

checkpoint_section = f"""## b111 Human Runtime selects cross-role reuse contamination / b112 role-isolated reuse allocation — 2026-09-06

Exact b111 Human Runtime evidence:

- Export metadata is canonical Release Build111 / Candidate `DEV-send-stream-0.1.0-b111` / source `4297846dd688` on iPhone iOS17.0. Exact diagnostics SHA-256 `{DIAGNOSTICS_SHA}`; 52 total events, including 12 `assistantChunkColor.willDisplay` and 12 `assistantChunkRender.afterDisplay` samples.
- The target remains the same completed authoritative answer: 2 visible messages / 6 presentation rows / 0 live rows / one 5-chunk assistant message (`chunkCharacterLimit=1200`, max chunk 1193). No new Send is involved.
- Every sampled assistant attributed string is structurally clean at capture time: `attributeRunCount=1`, `foregroundRunCount=1`, `foregroundDistinctColors=rgba:0,0,0,1`, `linkRunCount=0`, `attachmentRunCount=0`. Every direct-attributed transparent render is black `0.000,0.000,0.000` with blue-dominant fraction `0.000`. Runtime attributed content/link styling is therefore rejected as the current blue owner.
- The UILabel CALayer is the first surface that diverges. Four samples resolve exactly system-blue-like `labelLayerTransparentInkRGB=0.000,0.476,1.000`, blue-dominant fraction `1.000`: chunk 2 twice and chunk 3 twice. Normal samples from assistant-only cells resolve black with blue fraction `0.000`.
- Reuse provenance makes the causal boundary concrete. Cell ordinal 3 renders chunk 3 black on its initial `reusedFromRole=none` sample; after that same cell is reused from a `.user` row whose previous attributed value contained one link run, the next chunk-3 layer render turns pure blue and remains blue on the repeat sample. Cell ordinal 1 is first captured blue immediately after `reusedFromRole=user` / `reusedFromLinkRunCount=1`, then remains blue on a later assistant->assistant reuse even though the current assistant attributed string is black and link-free. By contrast, cell ordinals 2 and 4, which are reused only from assistant/no-link state in this export, remain black.
- Current source explains the initiating state: user and assistant rows share the single reuse identifier `ConversationMessageCell`, while user Markdown links explicitly apply `UIColor.systemBlue`. Existing `prepareForReuse` already clears text/attributedText and resets highlight/text/tint, yet the layer stays contaminated; another reset is therefore not the evidence-backed owner fix.

b112 allocation / minimum fix:

- Allocate and permanently reserve `DEV-send-stream-0.1.0-b112` / `0.1.0 (112)`. `BUILD_TEST_INDEX.md` contains no b112 before this allocation; parallel PR #35 owns no `ChatGPTClient/**`, product Xcode candidate, or Build112 identity.
- Keep `ConversationMessageCell` as the single implementation class and preserve user Markdown/link rendering, assistant attributed rendering, b111 diagnostics, geometry, reasoning, Copy, Send/SSE/Repository/recovery behavior unchanged.
- Change only reuse ownership: register distinct `.user` and `.assistant` reuse identifiers and select the identifier from the existing presentation message role before dequeue. A cell/UILabel that has rendered a user link must never be reused for an assistant row. This fixes the proven invariant at the reuse owner rather than adding another color/tint/highlight reset.
- Product scope is exactly `ChatGPTClient.xcodeproj/project.pbxproj` plus `ChatGPTClient/Conversation/ConversationFeature.swift`.
- Human Runtime b112: reopen this same completed 5-chunk answer, scroll through all chunks, and export Diagnostics. Require all assistant direct/layer/hierarchy transparent renders to stay normal `.label`, zero assistant reuse provenance from `user`, and no blue/normal alternation. Existing user link system-blue rendering must remain intact. No new Send is required.

Resume/conflict guard / batch recovery point:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable; verified pre-b112 branch head `5d2ee88331e21b7a3e186c3930717c524c2137ab`; canonical b111 product `{B111_PRODUCT}`, package `{B111_PACKAGE}`, Artifact `{B111_ARTIFACT}`.
- `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`. Parallel PR #35 remains draft at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`, research-only with zero product/candidate overlap.
- Tooling-preparation commits may add only b112 staging scripts/workflow and do not create a b112 product or Artifact.
- Batch A: durably record this b111 Runtime classification and b112 reservation in checkpoint/index/state/module/profile/technical decisions before product changes.
- Batch B: apply only the exact two-product-path b112 reuse-isolation delta, run `git diff --check` + Debug Simulator compile, then commit exact product.
- Batch C: bind formal package CI to the exact b112 product commit, require same-source Push + PR CI, canonical Artifact and independent IPA identity/hash verification, then record package evidence and update PR #29 before Human Runtime.
- Recovery must not rewrite b111/b110/b109 identities, PR #35, user-link `systemBlue`, Send/SSE/Repository/recovery behavior, or previously reserved Candidates.

**Next exact action:** complete Batch B only after Batch A is durably committed; then package one canonical b112 for the role-isolated reuse Human Runtime gate.
"""
prepend_once(CHECKPOINT, "## b111 Human Runtime selects cross-role reuse contamination / b112 role-isolated reuse allocation", checkpoint_section)

state_section = f"""## DEV-send-stream b111 Runtime root-cause boundary / b112 role reuse fix — 2026-09-06

- Canonical b111 diagnostics `sha256:{DIAGNOSTICS_SHA}` select the color owner: current assistant attributed content is uniformly black/link-free, but UILabel CALayer output turns pure system-blue after the same cell/label is reused from a user row with a Markdown link and can remain blue on later assistant->assistant reuse.
- One cell ordinal is observed black before cross-role reuse and blue immediately after `user + prior link` reuse; assistant-only reuse cells remain black. This is direct Runtime evidence for shared cross-role cell reuse contamination, not a tint/model-state hypothesis.
- b112 Build112 is reserved for the minimum owner fix: separate user and assistant UITableView reuse identifiers while keeping the same cell class/renderers and all Send/SSE/Repository behavior unchanged.
- Overall `DEV-send-stream`: Active / Runtime Partial / Stable-Frozen No.
"""
prepend_once(PROJECT_STATE, "## DEV-send-stream b111 Runtime root-cause boundary / b112 role reuse fix", state_section)

module_section = f"""## DEV-send-stream b111 shared-cell contamination selected / b112 reuse isolation — 2026-09-06

- b111 exact Runtime `sha256:{DIAGNOSTICS_SHA}` rejects current attributed content as the assistant blue owner: all direct attributed renders are black with zero current link runs. Blue first appears in the UILabel layer.
- Reuse provenance is causal in the captured sample: cell 3 transitions from black to blue only after user/link reuse; cell 1 enters blue after user/link reuse and remains blue on later assistant reuse; assistant-only cells remain black.
- b112 isolates UITableView reuse pools by message role without changing the cell implementation, user link styling, geometry, reasoning, or Send/SSE/Repository/recovery ownership.
- Module remains Active / Runtime Partial / Stable-Frozen No.
"""
prepend_once(MODULE_STATUS, "## DEV-send-stream b111 shared-cell contamination selected / b112 reuse isolation", module_section)

profile_section = f"""## Current DEV-send-stream rendering-fix candidate — b112 2026-09-06

- `DEV-send-stream-0.1.0-b112` / `0.1.0 (112)` is permanently reserved as the evidence-backed cross-role cell-reuse isolation candidate; product/package source pending staging.
- Trigger evidence is canonical b111 diagnostics `sha256:{DIAGNOSTICS_SHA}`: assistant attributed/direct rendering stays black and link-free, while UILabel layer output becomes system-blue only on cells contaminated by prior user-link reuse and persists on the contaminated cell.
- b112 changes only Build/Candidate plus role-specific UITableView reuse identifiers in `ConversationFeature.swift`; user link styling and Send/SSE/Repository owners remain unchanged.
- Stable/Frozen No.
"""
prepend_once(PROJECT_PROFILE, "## Current DEV-send-stream rendering-fix candidate — b112", profile_section)

decision_section = f"""## DEV-send-stream b111 layer/reuse diagnosis / b112 role-isolated reuse decision — 2026-09-06

- Exact b111 Runtime `sha256:{DIAGNOSTICS_SHA}` resolves the b109-b111 color investigation. Current assistant attributed state is one black foreground run with zero links, and direct attributed rendering is black; therefore another text/tint/highlight reset or attributed-color rewrite is not authorized.
- The first divergent surface is `messageLabel.layer.render`: system-blue appears only on contaminated cell ordinals. One cell is black before cross-role reuse and blue after reuse from a user row with one link run; another first appears blue after user-link reuse and remains blue on subsequent assistant reuse. Assistant-only reuse cells remain black.
- Fix the invariant at the reuse owner: keep the same `ConversationMessageCell` implementation but maintain separate UITableView reuse identifiers/pools for user and assistant roles. User cells may continue rendering Markdown links with `UIColor.systemBlue`; assistant cells must never inherit a UILabel that previously rendered that user-link state.
- Preserve b111 diagnostics through the b112 Runtime gate so the fix is observable. Do not add a replacement color reset, separate message store, timer/retry/watchdog, or Send/Repository change.
"""
prepend_once(TECHNICAL_DECISIONS, "## DEV-send-stream b111 layer/reuse diagnosis / b112 role-isolated reuse decision", decision_section)
