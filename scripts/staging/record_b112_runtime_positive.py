from pathlib import Path

BUILD_INDEX = Path("docs/project/BUILD_TEST_INDEX.md")
CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
PROJECT_STATE = Path("docs/project/PROJECT_STATE.md")
MODULE_STATUS = Path("docs/project/MODULE_STATUS.md")
PROJECT_PROFILE = Path("docs/project/PROJECT_PROFILE.md")
TECHNICAL_DECISIONS = Path("docs/project/TECHNICAL_DECISIONS.md")
PROJECT_SPECIFIC_RULES = Path("docs/project/PROJECT_SPECIFIC_RULES.md")

DIAGNOSTICS_SHA = "36fd01529ee522fd0646f7bdf6e6f409dca3f55a4b17ff21c88e4e19d16e23b2"
SCREENSHOT_SHA = "7a689bca421c01af25aeb19dc9e3a19d1e9a7f47fe431533be760d3eaa1db243"


def prepend_once(path: Path, marker: str, section: str) -> None:
    text = path.read_text()
    if marker in text:
        return
    path.write_text(section.rstrip() + "\n\n" + text)


def update_build_index() -> None:
    text = BUILD_INDEX.read_text()
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| `DEV-send-stream-0.1.0-b112`"):
            lines[index] = (
                "| `DEV-send-stream-0.1.0-b112` | `DEV-send-stream` | `0.1.0 (112)` | role-isolated message-cell reuse product `3957b806f32f0995ceb9cf8f9487aba939f3b306`; package `b5e3164721e01ceb1fe320ebd290bda79a921fc2`; PR #29 | staging `33988677640/101366840574` exact two-product-path scope + `git diff --check` + Debug Simulator passed; Push `33988756874/101367061209` passed; PR `33988758566/101367065891` passed on exact package source; canonical Artifact `9975978222`; ZIP `c2ec86afe0b4f8cd4112c437b538b4612ecdaeb8205ce57f3f63241ffa9e6922`; IPA `f1c705b72024d7f58f9a574fa885876b0382ff5120dbf9f095177c34207a32e9`; package independently verified `com.whitesharkssw.chatgptclient` / Build112 / Candidate b112 / source `b5e3164721e0` / Release / iOS14+ / `[1,2]` / arm64 | Runtime diagnostics `sha256:%s` plus screenshot `sha256:%s` on canonical b112: same completed authoritative target remains 2 visible messages / 6 presentation rows / 0 live rows / one 5-chunk assistant message. Ten assistant `willDisplay` samples remain black `.label`. Nine `assistantChunkRender.afterDisplay` samples all have one black foreground run, zero link/attachment runs, direct attributed RGB `0,0,0`, UILabel CALayer RGB `0,0,0`, and blue-dominant fraction `0.000`; available UILabel hierarchy samples are also black with blue fraction `0.000`. Assistant reuse provenance is only `none` or `assistant`, never `user`, and every prior-link count is zero. Screenshot visually shows the long assistant body consistently normal/black while the user GitHub link remains system blue. The same screenshot also exposes raw Markdown syntax and a raw `filecite` control token; those are separate rich-text/citation-renderer gaps and are not a b112 color-fix failure | **Runtime Positive for role-isolated assistant color fix / blue-normal alternation not reproduced / overall DEV-send-stream remains Runtime Partial because accepted clean-EOF recovery is still Unexercised / Stable-Frozen No; permanently reserved** |"
                % (DIAGNOSTICS_SHA, SCREENSHOT_SHA)
            )
            BUILD_INDEX.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))
            return
    raise SystemExit("b112 row not found")


update_build_index()

checkpoint_section = f"""## b112 Human Runtime Positive — role-isolated reuse color fix 2026-09-06

Exact Human Runtime evidence:

- Canonical export metadata is Release Build112 / Candidate `DEV-send-stream-0.1.0-b112` / source marker `b5e3164721e0` / bundle `com.whitesharkssw.chatgptclient` on iPhone iOS17.0. Exact diagnostics SHA-256 `{DIAGNOSTICS_SHA}`; exact screenshot SHA-256 `{SCREENSHOT_SHA}`.
- The same completed authoritative target remains 2 visible messages / 6 presentation rows / 0 live rows with one 5-chunk assistant answer (`chunkCharacterLimit=1200`, max chunk 1193). No new Send was required for this gate.
- The export contains 10 `assistantChunkColor.willDisplay` and 9 `assistantChunkRender.afterDisplay` samples. Every visible assistant model-state sample resolves text/attributed/highlight/tint to light-mode black `.label` with no selected/highlighted state.
- Every rendered assistant sample has exactly one black foreground run, zero link runs and zero attachment runs. Every direct-attributed transparent render is `0.000,0.000,0.000` with blue-dominant fraction `0.000`. Every UILabel CALayer transparent render is also `0.000,0.000,0.000` with blue-dominant fraction `0.000`. Where UILabel hierarchy transparent pixels are available, they are likewise black with blue fraction `0.000`; two chunk-3 hierarchy captures report `no_ink_pixels`, but their direct and CALayer captures are valid black and contain no system-blue signal.
- Reuse provenance now matches the intended invariant: all assistant rendered samples report `reusedFromRole=none` or `assistant`; there is zero `reusedFromRole=user`, and every `reusedFromLinkRunCount` is `0`. The b111 contamination path is therefore absent under the role-isolated pools.
- The supplied screenshot visually matches the telemetry: the long assistant body is consistently normal/black across the visible chunked answer, with no blue/normal alternation. The user GitHub URL remains system blue, so the user-link styling regression check also passes in this sample.

Classification:

- b112 is **Human Runtime Positive for the assistant blue-text defect** on the tested iPhone/iOS17 light-appearance path. The b111 root-cause boundary and b112 role-isolated reuse correction are accepted for this scope.
- Do not allocate b113 for the color defect from this evidence. No further color reset or reuse workaround is justified.
- Overall `DEV-send-stream` remains **Active / Runtime Partial / Stable-Frozen No** because the inherited b107 accepted `stream_ended_without_done` same-generation recovery branch is still Unexercised / Unverified by these color-only samples.
- Separate screenshot observation: Native assistant presentation still displays raw Markdown control syntax (`**`, `###`, pipe-table markup) and a raw/unrendered `filecite` control token. This is not a recurrence of the blue-color defect and is not evidence against b112; treat rich-text/citation rendering as a separate presentation scope rather than folding it into the color fix.

Resume/conflict state:

- Branch before this docs-only Runtime record: `dev/send-stream-20260829` head `abaf3cd4cd902f42d2f8ad2836a4e17115a78389`; PR #29 open/unmerged/mergeable; canonical product/package/Artifact identities remain `3957b806...` / `b5e31647...` / `9975978222`.
- `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`. No product/Candidate identity changes are made by this Runtime record.

**Evidence ladder:** b111 diagnostic Runtime Positive / root-cause boundary selected / b112 Code written / exact scope + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / **Human Runtime Positive for assistant color consistency + user-link regression** / overall `DEV-send-stream` Runtime Partial / Stable-Frozen No.

**Next exact action:** close the blue-text sub-gate at b112. Do not create another color candidate. Continue only from a separately evidenced remaining `DEV-send-stream` gate (notably accepted clean-EOF recovery if it occurs) or a separately selected presentation task for Markdown/citation rendering.
"""
prepend_once(CHECKPOINT, "## b112 Human Runtime Positive — role-isolated reuse color fix", checkpoint_section)

state_section = f"""## DEV-send-stream b112 assistant-color Runtime Positive — 2026-09-06

- Canonical b112 diagnostics `sha256:{DIAGNOSTICS_SHA}` and screenshot `sha256:{SCREENSHOT_SHA}` close the tested assistant blue/normal alternation gate as Runtime Positive on iPhone/iOS17 light appearance.
- Nine rendered assistant samples keep current attributed content and UILabel CALayer output black with blue fraction `0.000`; assistant reuse provenance never crosses from `user`, matching the b112 role-isolated reuse invariant. The screenshot visually shows consistent black assistant body text and preserved system-blue user-link styling.
- Raw Markdown syntax and an unrendered `filecite` token are separately visible in the screenshot; they are presentation/rich-text gaps, not a b112 color regression.
- Overall `DEV-send-stream` remains Active / Runtime Partial / Stable-Frozen No because accepted clean-EOF recovery remains Unexercised.
"""
prepend_once(PROJECT_STATE, "## DEV-send-stream b112 assistant-color Runtime Positive", state_section)

module_section = f"""## DEV-send-stream b112 role-isolated reuse Runtime accepted — 2026-09-06

- Exact b112 Runtime `sha256:{DIAGNOSTICS_SHA}` has zero assistant `reusedFromRole=user`, zero prior-link reuse counts, and zero blue-dominant CALayer output across 9 rendered assistant samples. The supplied screenshot `sha256:{SCREENSHOT_SHA}` visually confirms the assistant body remains normal/black while user link styling stays blue.
- The assistant blue-text defect is Runtime Positive for the tested path. Keep user/assistant message-cell reuse ownership isolated; do not replace this with another blind color reset.
- Separate raw Markdown/file-citation rendering remains outside this color sub-gate.
- Module remains Active / Runtime Partial overall / Stable-Frozen No because other Send/Stream gates remain open, including accepted clean-EOF recovery.
"""
prepend_once(MODULE_STATUS, "## DEV-send-stream b112 role-isolated reuse Runtime accepted", module_section)

profile_section = f"""## Current DEV-send-stream Runtime candidate — b112 2026-09-06

- `DEV-send-stream-0.1.0-b112` / `0.1.0 (112)` remains the package-qualified candidate; product `3957b806f32f0995ceb9cf8f9487aba939f3b306`, package `b5e3164721e01ceb1fe320ebd290bda79a921fc2`, Artifact `9975978222`, IPA `sha256:f1c705b72024d7f58f9a574fa885876b0382ff5120dbf9f095177c34207a32e9`.
- Human Runtime `sha256:{DIAGNOSTICS_SHA}` + screenshot `sha256:{SCREENSHOT_SHA}` accepts the role-isolated assistant-color fix on the tested iPhone/iOS17 light-appearance path. No b113 color candidate is authorized.
- Overall `DEV-send-stream` remains Runtime Partial / Stable-Frozen No because separate recovery/presentation gates remain outside this color result.
"""
prepend_once(PROJECT_PROFILE, "## Current DEV-send-stream Runtime candidate — b112", profile_section)

decision_section = f"""## DEV-send-stream b112 role-isolated message-cell reuse accepted — 2026-09-06

- Exact b111 Runtime selected cross-role reuse as the source of persistent UILabel layer system-blue contamination. Exact b112 Runtime `sha256:{DIAGNOSTICS_SHA}` removes that path: assistant samples never reuse from `user`, all prior-link counts are zero, and every valid assistant CALayer aggregate is black with blue fraction `0.000`.
- Accept separate user and assistant UITableView reuse identifiers as the Runtime-backed fix for this defect while retaining one `ConversationMessageCell` implementation class. Preserve user-link system-blue styling and assistant `.label` rendering.
- Do not regress to one shared cross-role reuse pool or replace the owner fix with repeated text/tint/highlight resets without new Runtime evidence.
- This decision is presentation-only and changes no Send/SSE/Repository/recovery authority. Raw Markdown/file-citation rendering visible in the screenshot is a separate scope.
"""
prepend_once(TECHNICAL_DECISIONS, "## DEV-send-stream b112 role-isolated message-cell reuse accepted", decision_section)

rule_section = f"""## Message-cell role reuse isolation — Runtime accepted b112 2026-09-06

- User and assistant rows may share the `ConversationMessageCell` implementation class, but they must not share the same UITableView reuse identifier while user rows can render system-blue Markdown links. b111 proved user-link rendering can persist as UILabel layer/cache color across cross-role reuse; b112 Runtime `sha256:{DIAGNOSTICS_SHA}` proves role-isolated pools remove that contamination on the tested path.
- Assistant cells must therefore be dequeued from the assistant reuse pool and user cells from the user reuse pool. Preserve normal same-role reuse.
- Do not substitute repeated `textColor`/`tintColor`/highlight resets for this ownership invariant without new contrary Runtime evidence.
- This rule governs message presentation only. It does not create response/content authority and does not change user-link color semantics.
"""
prepend_once(PROJECT_SPECIFIC_RULES, "## Message-cell role reuse isolation — Runtime accepted b112", rule_section)
