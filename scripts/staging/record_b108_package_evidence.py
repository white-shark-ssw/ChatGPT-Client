from pathlib import Path

PRODUCT = "eb0de74460b0bd06a6d977bf915b5e06a5c946db"
PACKAGE = "d34ff4534ca76ee03e2c8a3eeddb29eca011319f"
STAGING = "33981732350/101348043849"
PUSH = "33981838027/101348321052"
PR = "33981839719/101348326124"
ARTIFACT = "9973988017"
ZIP_SHA = "8e445a65346b9a32d8811645f2e21a2f1340942c9e7333beb4ddfc4c6a8a7c14"
IPA_SHA = "a2639b5793316077c0f203bfd4dffdecd8cef74c361a4995bc8bfba05f657dbd"
RUNTIME107 = "8e3e10b44e8e627f60e7a831d48f11c7fa9fff4bc4b0446b71588fbc38ade7da"

checkpoint = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
build_index = Path("docs/project/BUILD_TEST_INDEX.md")
project_state = Path("docs/project/PROJECT_STATE.md")
module_status = Path("docs/project/MODULE_STATUS.md")
profile = Path("docs/project/PROJECT_PROFILE.md")
decisions = Path("docs/project/TECHNICAL_DECISIONS.md")

checkpoint_section = f'''## b108 assistant-body color ownership — package ready 2026-09-06

Canonical identity / validation:

- Candidate `DEV-send-stream-0.1.0-b108` / `0.1.0 (108)`, permanently reserved.
- Exact product commit `{PRODUCT}`; canonical package source `{PACKAGE}`.
- Guarded staging `{STAGING}` passed exact two-product-path validation, `git diff --check`, Debug Simulator compile and exact product commit.
- Formal Push `{PUSH}` and PR `{PR}` both passed on exact package source `{PACKAGE}`.
- Canonical Push Artifact `{ARTIFACT}`; GitHub Artifact digest and independently recomputed ZIP SHA-256 both `{ZIP_SHA}`.
- Canonical IPA `ChatGPTClient-0.1.0-b108-dev-send-stream.ipa`; independent SHA-256 `{IPA_SHA}`, matching sidecar.
- Independent package inspection verifies `com.whitesharkssw.chatgptclient`, `0.1.0 (108)`, Candidate b108, source marker `d34ff4534ca7`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS and Mach-O arm64.

Exact product behavior:

- Product change remains exactly two paths: Build/Candidate 107 -> 108 in the Xcode project, plus one assistant-body rendering statement in `ConversationFeature.swift`.
- In `ConversationMessageCell.configure`, `.assistant` assigns the existing assistant attributed body first and then sets `messageLabel.textColor = .label`, making UILabel's final body color property authoritative after attributed-text style adoption.
- `.user` attributed text and link `systemBlue` handling are unchanged. `reasoningTextView`, response timeline styling, Markdown semantics, row geometry, Send/SSE parsing, Repository state and all b107 recovery logic are unchanged.
- This delta is justified by exact b107 Runtime `sha256:{RUNTIME107}` + screenshots: assistant placeholder/final body were blue while reasoning SSE text was normal, which maps to `messageLabel` versus the independent `reasoningTextView`. b106's pre-attributedText label reset was Runtime-insufficient.

Evidence ladder / Runtime gate:

- **Code written / exact scope + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**
- Human Runtime b108 must verify the assistant `正在思考…` placeholder and final assistant body use normal label color, while reasoning SSE remains unchanged and user-link coloring does not regress.
- Also re-run one ordinary Native New Chat Send to ensure b107 one-Send authoritative identity/normal terminal convergence has no regression. If exact accepted `stream_ended_without_done` naturally occurs, the inherited b107 same-generation/no-resend recovery gate may be evaluated; absence of that event does not qualify it.

**Next exact action:** install only canonical b108 IPA `{IPA_SHA}` on the real iPhone, fresh-launch, run one New Chat first Send, observe placeholder/reasoning/final colors and export diagnostics. Do not allocate b109 before b108 Human Runtime evidence unless the user explicitly chooses to skip Runtime.

'''

state_section = f'''## DEV-send-stream b108 package-qualified Human Runtime gate — 2026-09-06

- Candidate `DEV-send-stream-0.1.0-b108` / product `{PRODUCT}` / package `{PACKAGE}` is package-qualified after staging `{STAGING}`, Push `{PUSH}` and PR `{PR}` success.
- Canonical Artifact `{ARTIFACT}` / ZIP `{ZIP_SHA}` / IPA `{IPA_SHA}` independently verifies Build108, Candidate b108, source `d34ff4534ca7`, Release, iOS14+, iPhone/iPad and arm64.
- Product scope is only Xcode Build/Candidate plus `ConversationMessageCell` assistant-body post-attributedText `messageLabel.textColor = .label`. Send/SSE/Repository/recovery and reasoning/user-link rendering are unchanged.
- b108 Human Runtime is Pending. Exact gate is normal assistant placeholder/final body color with reasoning SSE unchanged, plus ordinary New Chat Send regression. Inherited b107 accepted clean-EOF recovery remains Unexercised until exact `stream_ended_without_done` occurs.
- Overall `DEV-send-stream`: Active / Runtime Partial / Stable-Frozen No.

'''

module_section = f'''## DEV-send-stream b108 package qualification — 2026-09-06

- UI delta is confined to `ConversationMessageCell.messageLabel`: assistant body attributed text is assigned first, then UILabel `textColor=.label` becomes the final uniform body-color owner. Separate `reasoningTextView`, user links and response timeline styles are unchanged.
- `ConversationRepository`, covered Send executor, New Chat authoritative handoff and b107 accepted-client recovery owners are unchanged.
- Exact product `{PRODUCT}` / package `{PACKAGE}` passed guarded Simulator staging and same-source Push + PR packaging; canonical Artifact `{ARTIFACT}` / IPA `{IPA_SHA}` is verified. Runtime color correction remains Pending.
- Module remains Active / Runtime Partial / Stable-Frozen No.

'''

profile_section = f'''## Current DEV-send-stream test candidate — b108 2026-09-06

- Package-qualified Human Runtime candidate: `DEV-send-stream-0.1.0-b108` / `0.1.0 (108)`.
- Exact product `{PRODUCT}`; canonical package source `{PACKAGE}`; canonical Artifact `{ARTIFACT}`; IPA `sha256:{IPA_SHA}`.
- Package identity independently verified: `com.whitesharkssw.chatgptclient`, Release iPhoneOS, iOS14+, UIDeviceFamily `[1,2]`, arm64, diagnostics source marker `d34ff4534ca7`.
- Human Runtime pending; Stable/Frozen No. b107 remains permanently reserved and its exact accepted-clean-EOF recovery is still Runtime-unexercised.

'''

decision_section = '''## Assistant body color ownership after attributed text — b108

- Exact b107 Runtime isolated the blue-text defect to assistant body presentation: `UILabel messageLabel` rendered placeholder/final blue while the separate reasoning `UITextView` remained normal. The prior pre-assignment highlight/text/tint reset was therefore insufficient.
- For the b108 test candidate, assistant body color ownership stays inside the existing `ConversationMessageCell`: assign the existing assistant attributed text first, then set the UILabel `textColor` to `.label` as the final uniform body-color property. Do not move color ownership into SSE/Repository state and do not alter the separate reasoning view or user-link tint behavior.
- This is a package-qualified implementation decision, not a Runtime-proven stable contract until b108 real-device evidence passes.

'''

for path, section in ((checkpoint, checkpoint_section), (project_state, state_section), (module_status, module_section), (profile, profile_section), (decisions, decision_section)):
    text = path.read_text()
    if PRODUCT not in text:
        path.write_text(section + text)

text = build_index.read_text()
lines = text.splitlines()
found = False
for i, line in enumerate(lines):
    if line.startswith("| `DEV-send-stream-0.1.0-b108` |"):
        found = True
        lines[i] = f"| `DEV-send-stream-0.1.0-b108` | `DEV-send-stream` | `0.1.0 (108)` | assistant body post-attributedText color ownership product `{PRODUCT}`; package `{PACKAGE}`; PR #29 | staging `{STAGING}` exact two-product-path scope + `git diff --check` + Debug Simulator passed; Push `{PUSH}` passed; PR `{PR}` passed; canonical Artifact `{ARTIFACT}`; ZIP `{ZIP_SHA}`; IPA `{IPA_SHA}`; package independently verified Build108/Candidate/source `d34ff4534ca7`/Release/iOS14+/`[1,2]`/arm64 | Human Runtime pending: assistant `正在思考…` placeholder + final body must use normal label color while reasoning SSE and user-link styling remain unchanged; ordinary New Chat Send regression required; inherited b107 accepted-EOF recovery remains evidence-gated if exact event occurs | **Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity verified / Human Runtime pending / Stable-Frozen No; permanently reserved** |"
        break
if not found:
    raise SystemExit("b108 row missing")
build_index.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))

print("b108 package evidence recorded")
