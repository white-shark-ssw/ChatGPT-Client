from pathlib import Path

PRODUCT = "7d1ddc8eaa164c9b307f525b00bb0e1404f395e9"
PACKAGE = "75ccad15208610c2b0420033846f9bb15bbdb494"
ZIP_SHA = "51d5bcd5e804c2877faafa67f4bb263d6d849b83a24c4c28982c6880aecc7ebf"
IPA_SHA = "2cf62b87117f9279816de68f2ed3ce83768d203198b555fe4fe0042f8d367c3f"


def read(path):
    return Path(path).read_text()


def write(path, value):
    Path(path).write_text(value)


def prepend_once(path, marker, section):
    value = read(path)
    if marker in value:
        return
    write(path, section.rstrip() + "\n\n" + value)

index_path = "docs/project/BUILD_TEST_INDEX.md"
index = read(index_path)
old_row = "| `DEV-message-rendering-0.1.0-b113` | `DEV-message-rendering` | `0.1.0 (113)` | stacked on Runtime-positive b112 head `50432b8743f3391a8174a3b7aae745298082d433`; product/PR pending | Candidate allocated; exact product scope `ChatGPTClient.xcodeproj/project.pbxproj` + `ChatGPTClient/Conversation/ConversationFeature.swift`; CI/Artifact pending | Human Runtime pending: user bare URL only blue while adjacent ordinary text stays label; assistant headings/emphasis/code/table/filecite render natively/readably; preserve b112 role-isolated color behavior and full-message Copy | **Allocated / Code pending / CI pending / Artifact pending / Human Runtime pending / Stable-Frozen No; permanently reserved** |"
new_row = f"| `DEV-message-rendering-0.1.0-b113` | `DEV-message-rendering` | `0.1.0 (113)` | stacked on Runtime-positive b112; product `{PRODUCT}`; package `{PACKAGE}`; stacked PR #36 -> `dev/send-stream-20260829` | staging `33991155027/101373512529` exact two-product-path scope + `git diff --check` + Debug Simulator passed; Push `33991287459/101373866191` passed; PR `33991302325/101373908835` passed; canonical Artifact `9976713893`; ZIP `{ZIP_SHA}`; IPA `{IPA_SHA}`; package independently verified `com.whitesharkssw.chatgptclient` / Build113 / Candidate b113 / source `75ccad152086` / Release / iOS14+ / `[1,2]` / arm64 | Human Runtime pending on the exact b112 screenshot conversation: URL only blue while adjacent Chinese stays label; assistant Markdown/control syntax rendered readably; filecite shown as non-interactive citation label; b112 assistant color isolation preserved; full-message Copy unchanged | **Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No; permanently reserved** |"
if old_row not in index:
    raise SystemExit("allocated b113 index row missing or already changed")
write(index_path, index.replace(old_row, new_row, 1))

checkpoint_path = "docs/project/current/dev/DEV-message-rendering.md"
checkpoint = read(checkpoint_path)
replacements = {
    "- **Working branch / PR / head commit**: `dev/message-rendering-20260906`; exact product commit `7d1ddc8eaa164c9b307f525b00bb0e1404f395e9`; stacked PR not created yet.": "- **Working branch / PR / head commit**: `dev/message-rendering-20260906`; stacked PR #36 -> `dev/send-stream-20260829`; exact product `7d1ddc8eaa164c9b307f525b00bb0e1404f395e9`; exact package source `75ccad15208610c2b0420033846f9bb15bbdb494`. Later docs/tooling commits do not replace this canonical package identity.",
    "- **Candidate identity**: `DEV-message-rendering-0.1.0-b113` / `0.1.0 (113)` permanently reserved and now written into the product. Artifact not yet produced.": "- **Candidate identity**: `DEV-message-rendering-0.1.0-b113` / `0.1.0 (113)` permanently reserved; canonical Artifact `9976713893`; ZIP SHA-256 `51d5bcd5e804c2877faafa67f4bb263d6d849b83a24c4c28982c6880aecc7ebf`; IPA SHA-256 `2cf62b87117f9279816de68f2ed3ce83768d203198b555fe4fe0042f8d367c3f`.",
    "- **Validation state**: **Code written / exact scope + static diff check + Debug Simulator passed / Push CI pending / PR CI pending / Artifact pending / Human Runtime pending / Stable-Frozen No.**": "- **Validation state**: **Code written / exact scope + static diff check + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**",
    "- **Pending**: Bind formal stacked package workflow to exact product commit, open stacked PR, require same-source Push + PR CI, independently verify canonical IPA identity, then run Human Runtime on the exact screenshot scenario.": "- **Pending**: Human Runtime only on canonical b113: verify link-only blue user text, rich assistant Markdown/table/code/filecite presentation, b112 color regression safety, geometry/scroll behavior and full-message Copy.",
    "- **Next exact action**: Execute Batch C only: bind package CI to exact product `7d1ddc8eaa164c9b307f525b00bb0e1404f395e9`, open PR with base `dev/send-stream-20260829`, obtain exact-source Push/PR CI and Artifact, independently verify Build113/Candidate/source/Release package, update durable docs, then hand canonical IPA to Human Runtime.": "- **Next exact action**: Install only canonical b113 and run the Human Runtime gate. Do not allocate b114 unless b113 Runtime produces new evidence.",
    "- **Batch C — pending**: bind dedicated package workflow, create stacked PR against `dev/send-stream-20260829`, require Push + PR CI on one exact package source, produce/verify canonical Artifact, then update checkpoint/index/project state before Human Runtime.": "- **Batch C — completed**: package source `75ccad15208610c2b0420033846f9bb15bbdb494`; stacked PR #36; Push `33991287459/101373866191` and PR `33991302325/101373908835` passed; canonical Artifact `9976713893`; ZIP/IPA identities independently verified. Human Runtime is the next gate."
}
for old, new in replacements.items():
    if old not in checkpoint:
        raise SystemExit(f"checkpoint marker missing: {old}")
    checkpoint = checkpoint.replace(old, new, 1)
write(checkpoint_path, checkpoint)

prepend_once("docs/project/PROJECT_STATE.md", "## DEV-message-rendering b113 package-qualified Runtime gate", f'''## DEV-message-rendering b113 package-qualified Runtime gate — 2026-09-06

- New stacked Phase 11 task `DEV-message-rendering` is Active on `dev/message-rendering-20260906`, PR #36 targeting the Runtime-positive b112 `DEV-send-stream` branch because both modify `ConversationFeature.swift`.
- Canonical b113 product `{PRODUCT}` / package `{PACKAGE}`; staging `33991155027/101373512529`, Push `33991287459/101373866191` and PR `33991302325/101373908835` passed. Artifact `9976713893`; ZIP `sha256:{ZIP_SHA}`; IPA `sha256:{IPA_SHA}`; package independently verifies Build113/Candidate/source/Release/iOS14+/`[1,2]`/arm64.
- Product presentation behavior: conservative ASCII bare-URL spans only are blue in user UILabel text; assistant authoritative/terminal content renders headings/emphasis/lists/code/tables and readable non-interactive citation labels; rendering occurs before bounded attributed chunking; raw message remains Repository/Copy authority. Active growing assistant Markdown is intentionally plain until terminal/authoritative projection to avoid full reparse on every token.
- Human Runtime pending. b112 assistant-color Runtime remains accepted and role-isolated reuse is inherited. `DEV-message-rendering` Stable-Frozen No.''')

prepend_once("docs/project/MODULE_STATUS.md", "## DEV-message-rendering b113 native presentation package", f'''## DEV-message-rendering b113 native presentation package — 2026-09-06

- Message presentation is now an explicit Active stacked module/task, not part of the closed b112 color sub-gate. Canonical b113 package is product `{PRODUCT}`, package `{PACKAGE}`, Artifact `9976713893`, IPA `sha256:{IPA_SHA}`; exact scope + Debug Simulator and both formal CI lanes passed.
- `ConversationRepository` / raw `ConversationMessage.text` remain content authority; rendering is attributed presentation only. b112 user/assistant reuse pools remain isolated.
- Human Runtime must verify URL-only blue user text, native assistant Markdown/code/table/filecite presentation, long-row geometry, Copy semantics and no assistant blue-text regression. Stable-Frozen No.''')

prepend_once("docs/project/PROJECT_PROFILE.md", "## Current DEV-message-rendering candidate — b113", f'''## Current DEV-message-rendering candidate — b113 2026-09-06

- Stacked package-qualified Human Runtime candidate: `DEV-message-rendering-0.1.0-b113` / `0.1.0 (113)` on branch `dev/message-rendering-20260906`, PR #36 base `dev/send-stream-20260829`.
- Product `{PRODUCT}`; package `{PACKAGE}`; Artifact `9976713893`; ZIP `sha256:{ZIP_SHA}`; IPA `sha256:{IPA_SHA}`.
- Independent package identity: `com.whitesharkssw.chatgptclient`, source `75ccad152086`, Release iPhoneOS, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, arm64.
- Human Runtime pending; Stable-Frozen No. The underlying b112 role-isolated assistant-color fix remains Runtime Positive.''')

prepend_once("docs/project/TECHNICAL_DECISIONS.md", "## DEV-message-rendering b113 presentation ownership decision", '''## DEV-message-rendering b113 presentation ownership decision — 2026-09-06

- Keep authoritative message content and Copy semantics in raw `ConversationMessage.text` / `ConversationRepository`; rich text is a one-way presentation projection and never a second content store.
- Render the full authoritative/terminal message before applying the existing bounded ~1200-character presentation chunking, then split the attributed output. Do not parse independent raw Markdown fragments after chunk boundaries.
- For user message UILabels, color only conservatively detected actual HTTP(S) URL spans system blue. Do not rely on Foundation's over-broad bare-URL Markdown range when adjacent non-ASCII text can be absorbed, and do not add UILabel `.link` attributes merely for color.
- Preserve b112 role-isolated reuse pools. Active growing assistant responses remain plain until terminal/authoritative projection so b113 does not introduce full Markdown reparsing on every streamed token.
- Raw `filecite`/`cite` control tokens may become readable non-interactive citation labels, but current content parsing does not retain authoritative citation resource objects. Do not invent a destination URL/file opener from opaque token IDs.''')

prepend_once("docs/project/PROJECT_SPECIFIC_RULES.md", "## Native message rich-text presentation — b113", '''## Native message rich-text presentation — b113 2026-09-06

- User body color semantics: ordinary text uses normal `.label`; only actual HTTP(S) URL/link display spans are system blue. A bare URL immediately followed by Chinese/non-ASCII prose must stop before that prose. Do not color the whole remainder of the user bubble blue.
- Preserve the b112 message-role reuse invariant: user and assistant cells remain in separate reuse pools. Visual link coloring must not be used as a reason to re-merge those pools.
- Assistant authoritative/terminal visible text may render native headings, emphasis, lists, inline/fenced code and pipe tables. Render the full message first, then bounded attributed chunks; raw Repository content and full-message Copy remain unchanged.
- Exact `filecite`/`cite` controls may be presented as readable citation labels. Until authoritative annotation/resource data is retained and evidenced, citation labels are non-interactive and opaque token IDs must not be guessed into URLs or file navigation.
- Do not expose hidden reasoning/tool/system content through the renderer. Do not add recurring parsing timers, streaming retry/state machinery or a second message-content authority for rich text.''')
