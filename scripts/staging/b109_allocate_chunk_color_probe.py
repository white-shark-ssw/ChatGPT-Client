from pathlib import Path

BUILD_INDEX = Path("docs/project/BUILD_TEST_INDEX.md")
CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
PROJECT_STATE = Path("docs/project/PROJECT_STATE.md")
MODULE_STATUS = Path("docs/project/MODULE_STATUS.md")
PROJECT_PROFILE = Path("docs/project/PROJECT_PROFILE.md")

DIAGNOSTICS_SHA = "c26f5ed8712ca63c8dae037e58330d5fa4b2f7cb47b8b0dafc078e920b4c813c"
VIDEO_SHA = "6cecee7a5f249529c72c53ee08620740e9d8480b080d8914476f697ad0efdc73"


def prepend_once(path: Path, marker: str, section: str) -> None:
    text = path.read_text()
    if marker in text:
        return
    path.write_text(section.rstrip() + "\n\n" + text)


def update_build_index() -> None:
    text = BUILD_INDEX.read_text()
    if "DEV-send-stream-0.1.0-b109" in text:
        return
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| `DEV-send-stream-0.1.0-b108`"):
            lines[index] = (
                "| `DEV-send-stream-0.1.0-b108` | `DEV-send-stream` | `0.1.0 (108)` | assistant body post-attributedText color ownership product `eb0de74460b0bd06a6d977bf915b5e06a5c946db`; package `d34ff4534ca76ee03e2c8a3eeddb29eca011319f`; PR #29 | staging `33981732350/101348043849` exact two-product-path scope + `git diff --check` + Debug Simulator passed; Push `33981838027/101348321052` passed; PR `33981839719/101348326124` passed; canonical Artifact `9973988017`; ZIP `8e445a65346b9a32d8811645f2e21a2f1340942c9e7333beb4ddfc4c6a8a7c14`; IPA `a2639b5793316077c0f203bfd4dffdecd8cef74c361a4995bc8bfba05f657dbd`; package independently verified Build108/Candidate/source `d34ff4534ca7`/Release/iOS14+/`[1,2]`/arm64 | Runtime `sha256:%s`: one New Chat protected HTTP200 SSE Send, authoritative SSE identity, 107 reasoning chars / 8 tools / 5292 final chars, normal terminal and `authoritativeReconcile.completed(liveSnapshotCleared=true)` Positive; zero `stream_ended_without_done`, so inherited b107 EOF recovery remains Unexercised. After authoritative reconcile the completed answer is exactly 6 presentation rows with `livePresentationRowCount=0`, one chunked assistant message, `chunkCharacterLimit=1200`, max chunk 1193. Video `sha256:%s` shows the same authoritative assistant answer alternating blue/normal text across long-message chunk rows, so b108 post-attributedText `textColor=.label` is Runtime-insufficient | **Runtime Partial / normal Send+terminal+authoritative reconcile Positive / accepted-EOF recovery Unexercised / authoritative chunk-row color consistency Negative / superseded for diagnostic priority by b109 / Stable-Frozen No; permanently reserved** |"
                % (DIAGNOSTICS_SHA, VIDEO_SHA)
            )
            b109 = (
                "| `DEV-send-stream-0.1.0-b109` | `DEV-send-stream` | `0.1.0 (109)` | allocated from exact b108 authoritative chunk-row color divergence; product source pending; PR #29 | diagnostic-only intended scope: Xcode Build/Candidate + `ConversationFeature.swift` per-chunk `willDisplay` color-state audit; no rendering fix yet | Human Runtime pending: open the same completed long authoritative answer, scroll through its chunks once, export diagnostics; compare each chunk's UILabel text/attributed/highlight/tint state with visible blue/normal rows. No new Send is required for this diagnostic gate | **Allocated diagnostic probe / product staging pending / Human Runtime pending / Stable-Frozen No; permanently reserved** |"
            )
            lines.insert(index, b109)
            BUILD_INDEX.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))
            return
    raise SystemExit("b108 row not found")


update_build_index()

checkpoint_section = f"""## b108 Human Runtime Negative / b109 authoritative chunk-color probe allocation — 2026-09-06

Exact b108 Human Runtime evidence:

- Canonical b108 metadata is Release Build108 / Candidate `DEV-send-stream-0.1.0-b108` / source `d34ff4534ca7` on iPhone iOS17.0. Exact diagnostics SHA-256 `{DIAGNOSTICS_SHA}`; exact 7.53s screen recording SHA-256 `{VIDEO_SHA}`.
- New Chat transport/regression remains Positive: one protected Send was observed, HTTP200 `text/event-stream` was accepted, the first SSE conversation ID became authoritative, generation 1 streamed 107 reasoning characters / 8 tools / 5292 final characters, reached normal `terminal` / `phase=completed`, then authoritative Detail reconciled with `liveSnapshotCleared=true`.
- There is zero exact `stream_ended_without_done`, zero `coveredExecutor.acceptedClientStreamEndRecovery`, and zero `acceptedClientRecovery.interrupted`. Therefore the inherited b107 accepted-clean-EOF recovery branch remains Unexercised, not passed or failed by this sample.
- The color defect is Runtime Negative again with a stronger boundary. After reconcile there are `presentationRowCount=6`, `livePresentationRowCount=0`, `authoritativeMessageCount=2`, one chunked message, `chunkCharacterLimit=1200`, and max chunk length 1193. This rules out live+authoritative duplication as the color owner.
- The exact video shows the completed authoritative assistant answer alternating blue and normal label-colored text at long-message row boundaries while the reasoning area is already collapsed. Current source derives those rows from one assistant message and configures every chunk as `.assistant`, so b108's post-attributedText `messageLabel.textColor=.label` is insufficient. Do not add more blind tint/text/highlight resets.

b109 allocation / evidence-backed scope:

- Allocate and permanently reserve `DEV-send-stream-0.1.0-b109` / `0.1.0 (109)`. No current Build/Test entry or parallel PR #35 candidate uses b109.
- b109 is diagnostic-only. Preserve b108 rendering behavior and all Send/SSE/Repository/recovery behavior unchanged.
- Product scope is exactly `ChatGPTClient.xcodeproj/project.pbxproj` plus `ChatGPTClient/Conversation/ConversationFeature.swift`.
- Add a privacy-safe `ConversationMessageCell` color snapshot and log it from the detail table's `willDisplay` path for chunked assistant rows. Required fields: surface (`authoritative`/`live`), row index, chunk index/count, resolved UILabel `textColor`, attributed foreground at index 0, highlighted text color, tint color, label/cell highlighted and selected states, and interface style. Do not log message text or IDs.
- This probe must not change any final rendering color, font, attributed content, geometry, Markdown behavior, link color, reasoning view, Send behavior, Repository state, timers, retries, recovery, or response authority.

Resume/conflict guard:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable; b108 package/runtime baseline head is `810cdb6e5572b5df8584494f28db1ed335e5b97a`. `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Parallel PR #35 remains draft research-only at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`, explicitly owning no `ChatGPTClient/**`, product Xcode Candidate, or exact product-path overlap.

**Next exact action:** after this Runtime/allocation checkpoint is durably committed, stage only the two-path b109 diagnostic probe, pass `git diff --check` + Debug Simulator compile, package one canonical b109 IPA, then on real iPhone open the same completed b108 long-answer conversation, scroll across all chunk rows once, export diagnostics, and compare `assistantChunkColor.willDisplay` fields with the visible blue/normal rows. Do not claim a color fix in b109.
"""
prepend_once(CHECKPOINT, "## b108 Human Runtime Negative / b109 authoritative chunk-color probe allocation", checkpoint_section)

state_section = f"""## DEV-send-stream b108 Runtime Negative / b109 diagnostic gate — 2026-09-06

- Exact b108 diagnostics `sha256:{DIAGNOSTICS_SHA}` keep ordinary New Chat one-Send/terminal/authoritative reconcile Positive and keep b107 accepted clean-EOF recovery Unexercised because `stream_ended_without_done` did not occur.
- Exact video `sha256:{VIDEO_SHA}` proves the completed authoritative assistant answer alternates blue/normal across long-message presentation chunks even after `liveSnapshotCleared=true`; post-reconcile state is 6 authoritative rows / 0 live rows with one 1200-character-chunked assistant message.
- b108 color ownership correction is Runtime-insufficient. b109 Build109 is reserved as a diagnostic-only per-chunk UILabel final-state probe; no new color fix is claimed yet.
- Overall `DEV-send-stream`: Active / Runtime Partial / Stable-Frozen No.
"""
prepend_once(PROJECT_STATE, "## DEV-send-stream b108 Runtime Negative / b109 diagnostic gate", state_section)

module_section = f"""## DEV-send-stream b108 chunk-row color Runtime Negative / b109 probe — 2026-09-06

- Repository/Send/recovery owners remain unchanged. b108 normal New Chat transport, terminal, and authoritative reconcile are Runtime Positive in `sha256:{DIAGNOSTICS_SHA}`; accepted clean-EOF recovery remains Unexercised.
- UI evidence is now chunk-row-specific: completed authoritative state has 6 presentation rows / 0 live rows, and video `sha256:{VIDEO_SHA}` shows one assistant message alternating blue/normal between long-message chunks. b108's final UILabel `textColor=.label` assignment is insufficient.
- b109 is diagnostic-only and will audit each chunk cell's resolved UILabel/attributed/highlight/tint state from `willDisplay`; rendering behavior itself must remain unchanged.
- Module remains Active / Runtime Partial / Stable-Frozen No.
"""
prepend_once(MODULE_STATUS, "## DEV-send-stream b108 chunk-row color Runtime Negative / b109 probe", module_section)

profile_section = f"""## Current DEV-send-stream diagnostic candidate — b109 2026-09-06

- `DEV-send-stream-0.1.0-b109` / `0.1.0 (109)` is permanently reserved as an authoritative long-message chunk-color diagnostic probe; product/package source pending staging.
- Trigger evidence: b108 diagnostics `sha256:{DIAGNOSTICS_SHA}` + video `sha256:{VIDEO_SHA}`. b108 ordinary Send/terminal/reconcile remains Positive, accepted clean-EOF recovery remains Unexercised, and completed authoritative chunk-row color consistency is Runtime Negative.
- b109 must not claim a rendering fix. Its sole product purpose is privacy-safe per-chunk UILabel/attributed/highlight/tint state capture for the existing completed long-answer reproduction.
- Stable/Frozen No.
"""
prepend_once(PROJECT_PROFILE, "## Current DEV-send-stream diagnostic candidate — b109", profile_section)
