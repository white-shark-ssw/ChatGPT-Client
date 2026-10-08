from pathlib import Path

BUILD_INDEX = Path("docs/project/BUILD_TEST_INDEX.md")
CHECKPOINT = Path("docs/project/current/dev/DEV-message-rendering.md")
PROJECT_STATE = Path("docs/project/PROJECT_STATE.md")
MODULE_STATUS = Path("docs/project/MODULE_STATUS.md")
PROJECT_PROFILE = Path("docs/project/PROJECT_PROFILE.md")
TECHNICAL_DECISIONS = Path("docs/project/TECHNICAL_DECISIONS.md")
PROJECT_SPECIFIC_RULES = Path("docs/project/PROJECT_SPECIFIC_RULES.md")

DIAGNOSTICS_SHA = "334a2f88d284e04936f0226c3cb6bdbad0710f1af5ead9c8168301fc5581af55"
SCREENSHOT_SHA = "be52e664e6f62b49e4432e98379ff7d2280f09693c8f6a66827665c51acbb184"


def prepend_once(path: Path, marker: str, section: str) -> None:
    text = path.read_text()
    if marker in text:
        return
    path.write_text(section.rstrip() + "\n\n" + text)


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text()
    if new in text:
        return
    if old not in text:
        raise SystemExit(f"missing replacement marker in {path}: {old}")
    path.write_text(text.replace(old, new, 1))


def update_build_index() -> None:
    text = BUILD_INDEX.read_text()
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| `DEV-message-rendering-0.1.0-b113`"):
            lines[index] = (
                "| `DEV-message-rendering-0.1.0-b113` | `DEV-message-rendering` | `0.1.0 (113)` | stacked on Runtime-positive b112; product `7d1ddc8eaa164c9b307f525b00bb0e1404f395e9`; package `75ccad15208610c2b0420033846f9bb15bbdb494`; stacked PR #36 -> `dev/send-stream-20260829` | staging `33991155027/101373512529` exact two-product-path scope + `git diff --check` + Debug Simulator passed; Push `33991287459/101373866191` passed; PR `33991302325/101373908835` passed; canonical Artifact `9976713893`; ZIP `51d5bcd5e804c2877faafa67f4bb263d6d849b83a24c4c28982c6880aecc7ebf`; IPA `2cf62b87117f9279816de68f2ed3ce83768d203198b555fe4fe0042f8d367c3f`; package independently verified `com.whitesharkssw.chatgptclient` / Build113 / Candidate b113 / source `75ccad152086` / Release / iOS14+ / `[1,2]` / arm64 | Human Runtime diagnostics `sha256:%s` + screenshot `sha256:%s` on exact Release Build113 / Candidate b113 / source `75ccad152086` / iPhone iOS17.0. All 78 diagnostic events are `info`; 18 `assistantChunkColor.willDisplay` + 18 `assistantChunkRender.afterDisplay` samples cover chunk indexes 0..4. Every captured direct-attributed, UILabel-layer, UILabel-hierarchy and hierarchy-crop blue-dominant fraction is `0.000`; assistant reuse is only `none` or `assistant`, never `user`; all prior-link reuse counts are `0`. Screenshot shows only the GitHub URL blue while adjacent Chinese text is normal, assistant headings/emphasis/inline code and table content render readably without the old control delimiter row, and raw `filecite` is replaced by a readable `[文件引用 ...]` label. User explicitly reports the result has no problem. Both user and assistant Copy actions are present; diagnostics do not expose clipboard payload bytes, so Copy payload correctness is accepted from the user's overall Runtime acceptance rather than inferred from telemetry alone. | **Human Runtime Positive for the tested b113 native message-presentation scope / stacked integration pending / Stable-Frozen No; permanently reserved** |"
                % (DIAGNOSTICS_SHA, SCREENSHOT_SHA)
            )
            BUILD_INDEX.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))
            return
    raise SystemExit("b113 row not found")


update_build_index()

checkpoint_section = f"""## b113 Human Runtime Positive — native message presentation 2026-09-06

Exact Human Runtime evidence:

- Diagnostics `sha256:{DIAGNOSTICS_SHA}` and screenshot `sha256:{SCREENSHOT_SHA}` are from the exact canonical package identity: Release `0.1.0 (113)`, Candidate `DEV-message-rendering-0.1.0-b113`, source marker `75ccad152086`, bundle `com.whitesharkssw.chatgptclient`, iPhone, iOS17.0.
- All 78 exported events are `info`. The export contains 18 `assistantChunkColor.willDisplay` and 18 `assistantChunkRender.afterDisplay` samples covering chunk indexes `0...4` / rows `1...5` of the five-chunk authoritative assistant answer.
- Every captured direct-attributed, UILabel CALayer, UILabel hierarchy and hierarchy-crop blue-dominant fraction is `0.000`. Assistant reuse provenance is only `none` or `assistant`, never `user`; all 18 prior-link reuse counts are `0`; current assistant body link-run counts are also `0`. The b112 role-isolated reuse fix therefore remains intact under repeated b113 scrolling/reuse.
- Screenshot directly verifies the user-color acceptance case: `https://github.com/white-shark-ssw/ChatGPT-Client.git` is blue while the immediately following Chinese prose is normal `.label`, so the previous over-broad bare-URL range is not reproduced.
- Screenshot also shows native/readable assistant presentation: emphasis is visually bold, `ChatGPT-Client` inline code uses a code treatment, `2 分钟筛选结果` is rendered as a heading, the pipe-table delimiter control row is no longer exposed, table content remains readable, and the raw private-use `filecite` token is replaced with a readable `[文件引用 L2-L2]` label. No guessed citation click-through is claimed.
- The export contains one `message.copy` for `user` and one for `assistant`. Diagnostics prove the full-message Copy actions were invoked but do not expose clipboard payload bytes. The user explicitly reports this b113 result has no problem, so the tested interaction scenario is accepted without inventing telemetry that was not captured.

Classification:

- b113 is **Human Runtime Positive for the tested native message-presentation scope**: link-only blue user text, readable assistant rich-text/citation presentation, long-message reuse/geometry behavior in the supplied scenario, and preservation of the b112 assistant-color invariant.
- This result does not make `DEV-send-stream` Stable/Frozen and does not exercise the separate b107 accepted clean-EOF recovery gate.
- Citation destination navigation remains intentionally out of scope until authoritative annotation/resource objects are retained. Do not infer clickable source resolution from this result.
- No b114 product candidate is justified by this evidence.

Integration boundary:

- `DEV-message-rendering` remains **Active — Human Runtime Positive / stacked integration pending / Stable-Frozen No** because PR #36 is stacked onto the separate Active `DEV-send-stream` branch. This task session must not merge PR #36 and silently advance another task's branch/checkpoint from b112 to b113.
- Product/package/Artifact identities remain unchanged. The next action is PR #36 Runtime-status update and later integration coordination by the owning dependency path.

**Evidence ladder:** Code written / exact scope + static diff check + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / **Human Runtime Positive for tested b113 presentation scope** / Stable-Frozen No.
"""
prepend_once(CHECKPOINT, "## b113 Human Runtime Positive — native message presentation", checkpoint_section)
replace_once(CHECKPOINT, "- **Batch D — pending**: durably classify b113 **Human Runtime Positive for the tested message-presentation scope** in `BUILD_TEST_INDEX.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_PROFILE.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_SPECIFIC_RULES.md`, and this checkpoint. Preserve the exact evidence boundary: screenshot + user's explicit acceptance prove visual behavior; diagnostics prove candidate/device/reuse/color telemetry and that both Copy actions were invoked, but telemetry alone does not expose clipboard payload bytes.", "- **Batch D — completed**: b113 Human Runtime Positive is durably recorded in the Build/Test Index, project state/module/profile, technical decisions, project-specific rules, and this checkpoint with the exact screenshot/diagnostics evidence boundary preserved.")
replace_once(CHECKPOINT, "- **Next exact action**: complete Batch D durable Runtime settlement, verify the resulting docs-only commit, then update PR #36 body. Do not merge into the `DEV-send-stream` branch from this task session.", "- **Next exact action**: verify the Batch D docs-only Runtime commit, then complete Batch E by updating PR #36 to Human Runtime Positive. Do not merge into the `DEV-send-stream` branch from this task session.")

state_section = f"""## DEV-message-rendering b113 Human Runtime Positive — 2026-09-06

- Canonical b113 Human Runtime diagnostics `sha256:{DIAGNOSTICS_SHA}` + screenshot `sha256:{SCREENSHOT_SHA}` are exact Release Build113 / Candidate b113 / source `75ccad152086` on iPhone iOS17.0; the user explicitly reports the tested result has no problem.
- Screenshot closes the visual presentation gate in the tested conversation: only the GitHub URL is blue while adjacent Chinese prose is normal; assistant emphasis/heading/inline-code/table content is readable; raw `filecite` control syntax is replaced by a readable non-interactive file-reference label.
- Diagnostics provide 18 color + 18 rendered assistant samples across all five long-message chunks with zero captured blue-dominant fraction on direct/layer/hierarchy/crop surfaces, zero cross-role user reuse and zero prior-link reuse. b112 role isolation therefore remains Runtime-positive under the b113 renderer.
- Both user and assistant Copy actions were invoked. Clipboard payload bytes are not present in telemetry; the user accepts the overall tested result, so do not overstate independent payload inspection.
- `DEV-message-rendering` is Runtime Positive for its tested presentation scope but remains Active / stacked integration pending / Stable-Frozen No. This does not change the separate `DEV-send-stream` accepted-clean-EOF evidence status.
"""
prepend_once(PROJECT_STATE, "## DEV-message-rendering b113 Human Runtime Positive", state_section)

module_section = f"""## DEV-message-rendering b113 presentation Runtime accepted — 2026-09-06

- Exact b113 Runtime `sha256:{DIAGNOSTICS_SHA}` + screenshot `sha256:{SCREENSHOT_SHA}` accepts the tested message-presentation behavior: URL-only blue user text with adjacent normal Chinese, readable assistant rich text/table/file-reference presentation, and no reappearance of the assistant blue/normal reuse defect.
- Eighteen assistant render samples cover all five chunks and report zero blue-dominant fraction on every captured direct/layer/hierarchy/crop surface; reuse is only `none`/`assistant`, never `user`, with zero prior-link reuse.
- Raw `ConversationMessage.text` remains content/Copy authority. Citation labels remain non-interactive until authoritative resource objects are available.
- Presentation scope is Human Runtime Positive; module/task remains Active only for stacked integration coordination and is not Stable/Frozen yet. `DEV-send-stream` remains independently Runtime Partial.
"""
prepend_once(MODULE_STATUS, "## DEV-message-rendering b113 presentation Runtime accepted", module_section)

profile_section = f"""## Current DEV-message-rendering Runtime result — b113 2026-09-06

- Canonical `DEV-message-rendering-0.1.0-b113` / `0.1.0 (113)` remains product `7d1ddc8eaa164c9b307f525b00bb0e1404f395e9`, package `75ccad15208610c2b0420033846f9bb15bbdb494`, Artifact `9976713893`, IPA `sha256:2cf62b87117f9279816de68f2ed3ce83768d203198b555fe4fe0042f8d367c3f`.
- Human Runtime diagnostics `sha256:{DIAGNOSTICS_SHA}` + screenshot `sha256:{SCREENSHOT_SHA}` on exact iPhone/iOS17.0 accept the tested native message-presentation scope, including URL color boundary, rich assistant presentation and b112 color-regression safety.
- Runtime status: Positive for tested presentation scope / stacked integration pending / Stable-Frozen No. Citation source opening remains outside b113 because authoritative annotation/resource objects are not retained.
"""
prepend_once(PROJECT_PROFILE, "## Current DEV-message-rendering Runtime result — b113", profile_section)

decision_section = f"""## DEV-message-rendering b113 Runtime acceptance — 2026-09-06

- Human Runtime `sha256:{DIAGNOSTICS_SHA}` + screenshot `sha256:{SCREENSHOT_SHA}` accepts the b113 presentation ownership design on the tested iPhone/iOS17 path.
- Keep conservative HTTP(S) URL display-range coloring for user UILabels: the tested bare GitHub URL stops before immediately adjacent Chinese prose, which remains normal `.label`.
- Keep full-message rich rendering before bounded attributed chunking for terminal/authoritative assistant content. The tested five-chunk answer remains readable while repeated reuse preserves b112 role isolation and produces no blue-dominant assistant output.
- Keep raw `ConversationMessage.text` as authoritative content/Copy source. Presentation projection is not a second content store.
- Keep `filecite`/`cite` as readable non-interactive labels until authoritative citation resource/annotation objects are retained; this Runtime acceptance does not authorize guessed URLs/file openers.
- Do not generalize this presentation result into Send/SSE/recovery stability or allocate a new candidate without new evidence.
"""
prepend_once(TECHNICAL_DECISIONS, "## DEV-message-rendering b113 Runtime acceptance", decision_section)

rule_section = f"""## Native message rich-text presentation — Runtime accepted b113 2026-09-06

- The tested Runtime contract is now accepted for b113: ordinary user prose remains normal `.label`; only the actual HTTP(S) URL display span is system blue, including when Chinese/non-ASCII prose follows immediately with no whitespace.
- Preserve b112 user/assistant role-isolated reuse. Exact b113 Runtime `sha256:{DIAGNOSTICS_SHA}` covers all five assistant chunks with zero cross-role user reuse, zero prior-link reuse and zero captured blue-dominant assistant output.
- Render authoritative/terminal assistant rich text before bounded attributed chunking; preserve raw Repository text as content/Copy authority. Do not introduce a second message store or reparsing timer/state machine.
- `filecite`/`cite` may remain readable non-interactive labels. Do not invent source navigation from opaque IDs until authoritative resource annotations are retained and evidenced.
- This rule is presentation-only. It does not alter protected Send/SSE/recovery ownership or prove unrelated Runtime gates.
"""
prepend_once(PROJECT_SPECIFIC_RULES, "## Native message rich-text presentation — Runtime accepted b113", rule_section)
