from pathlib import Path

BUILD_INDEX = Path("docs/project/BUILD_TEST_INDEX.md")
CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
PROJECT_STATE = Path("docs/project/PROJECT_STATE.md")
MODULE_STATUS = Path("docs/project/MODULE_STATUS.md")
PROJECT_PROFILE = Path("docs/project/PROJECT_PROFILE.md")

PRODUCT = "3957b806f32f0995ceb9cf8f9487aba939f3b306"
PACKAGE = "b5e3164721e01ceb1fe320ebd290bda79a921fc2"
STAGING = "33988677640/101366840574"
PUSH = "33988756874/101367061209"
PR = "33988758566/101367065891"
ARTIFACT = "9975978222"
ZIP_SHA = "c2ec86afe0b4f8cd4112c437b538b4612ecdaeb8205ce57f3f63241ffa9e6922"
IPA_SHA = "f1c705b72024d7f58f9a574fa885876b0382ff5120dbf9f095177c34207a32e9"
RUNTIME_SHA = "8b3e7e627c4218f1154b3e325ec6a95b643c8f64d01c18c37693bab3aba6e811"


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
                f"| `DEV-send-stream-0.1.0-b112` | `DEV-send-stream` | `0.1.0 (112)` | role-isolated message-cell reuse product `{PRODUCT}`; package `{PACKAGE}`; PR #29 | staging `{STAGING}` exact two-product-path scope + `git diff --check` + Debug Simulator passed; Push `{PUSH}` passed; PR `{PR}` passed on exact package source; canonical Artifact `{ARTIFACT}`; ZIP `{ZIP_SHA}`; IPA `{IPA_SHA}`; package independently verified `com.whitesharkssw.chatgptclient` / Build112 / Candidate b112 / source `b5e3164721e0` / Release / iOS14+ / `[1,2]` / arm64 | Human Runtime pending: reopen the same completed 5-chunk answer, scroll all assistant chunks and export diagnostics. Require no blue/normal alternation, no assistant reuse provenance from `user`, normal assistant direct/layer/hierarchy color, and unchanged user Markdown link system-blue behavior. No new Send required | **b111 Runtime root-cause boundary selected / b112 Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity verified / Human Runtime pending / Stable-Frozen No; permanently reserved** |"
            )
            BUILD_INDEX.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))
            return
    raise SystemExit("b112 row not found")


update_build_index()

checkpoint_section = f"""## b112 role-isolated cell reuse fix — package ready 2026-09-06

Canonical identity / validation:

- Candidate `DEV-send-stream-0.1.0-b112` / `0.1.0 (112)` is permanently reserved.
- Exact product commit `{PRODUCT}` changes only `ChatGPTClient.xcodeproj/project.pbxproj` and `ChatGPTClient/Conversation/ConversationFeature.swift` after the b111 Runtime/allocation checkpoint.
- Exact package source `{PACKAGE}` changes only `.github/workflows/ios-foundation.yml` after the product commit.
- Guarded staging `{STAGING}` passed exact two-product-path scope, `git diff --check`, Debug Simulator compile and exact product commit.
- Push CI `{PUSH}` and PR CI `{PR}` both passed on exact package source `{PACKAGE}`.
- Canonical Push Artifact `{ARTIFACT}`; GitHub Artifact digest and independently recomputed ZIP SHA-256 both `{ZIP_SHA}`.
- Canonical IPA `ChatGPTClient-0.1.0-b112-dev-send-stream.ipa`; independent SHA-256 `{IPA_SHA}`, matching the packaged sidecar.
- Independent package inspection verifies `com.whitesharkssw.chatgptclient`, `0.1.0 (112)`, Candidate b112, source marker `b5e3164721e0`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS and Mach-O arm64.

Evidence-backed product behavior:

- Trigger evidence is canonical b111 Human Runtime `sha256:{RUNTIME_SHA}`. Current assistant attributed strings/direct renders are uniformly black and link-free, while system-blue first appears at `messageLabel.layer.render` and tracks cells that have previously rendered a user Markdown link. One cell was black before cross-role reuse and blue after user/link reuse; contaminated cells can remain blue on later assistant reuse; assistant-only cells remain black.
- b112 fixes only that proven reuse invariant. `ConversationMessageCell` remains one implementation class, but UITableView registration/dequeue now uses distinct user and assistant reuse identifiers. A UILabel that rendered a user link can no longer enter the assistant reuse pool.
- Existing user Markdown/link `UIColor.systemBlue`, assistant attributed body construction, b111 diagnostics, reasoning, geometry, Copy, Send/SSE parsing, `ConversationRepository`, accepted-client recovery and response authority are unchanged.
- No replacement color reset, retry, timer/watchdog, polling, duplicate Send, compatibility shim, second state store or unrelated refactor is added.

Human Runtime gate:

1. Install only canonical b112 Artifact `{ARTIFACT}` / IPA SHA `{IPA_SHA}`.
2. Reopen the same completed 5-chunk answer used for b109-b111; no new Send is required.
3. Scroll through all five assistant chunks repeatedly enough to exercise reuse, especially the regions previously blue in chunks 2/3.
4. Visually require one consistent normal label color with no blue/normal alternation.
5. Export Diagnostics. Assistant samples must never report `reusedFromRole=user`; their direct/layer/hierarchy transparent output must remain normal label color. Existing user Markdown links should remain system blue as a regression check.
6. Do not mark the color defect solved or the module Stable/Frozen until this real-device gate passes.

**Evidence ladder:** b111 diagnostic Runtime Positive / shared cross-role reuse contamination selected / b112 Code written / exact scope + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.

**Next exact action:** run the b112 Human Runtime gate above and export Diagnostics. The inherited b107 accepted clean-EOF recovery remains separately Unexercised by this color-only test.
"""
prepend_once(CHECKPOINT, "## b112 role-isolated cell reuse fix — package ready", checkpoint_section)

state_section = f"""## DEV-send-stream b112 role-isolated reuse package ready — 2026-09-06

- b111 Runtime `sha256:{RUNTIME_SHA}` selects shared cross-role cell reuse as the assistant blue-text contamination boundary: direct attributed content is black/link-free, while UILabel layer output becomes system blue after prior user-link reuse.
- Canonical b112 product `{PRODUCT}` / package `{PACKAGE}`; staging `{STAGING}`, Push `{PUSH}`, PR `{PR}` all passed.
- Artifact `{ARTIFACT}` / ZIP `sha256:{ZIP_SHA}` / IPA `sha256:{IPA_SHA}` independently verify Build112/Candidate/source/Release/iOS14+/`[1,2]`/arm64.
- b112 isolates user and assistant UITableView reuse pools without changing rendering semantics or Send/SSE/Repository ownership. Human Runtime remains pending; Stable-Frozen No.
"""
prepend_once(PROJECT_STATE, "## DEV-send-stream b112 role-isolated reuse package ready", state_section)

module_section = f"""## DEV-send-stream b112 role-isolated message-cell reuse package — 2026-09-06

- Canonical b112 product `{PRODUCT}`, package `{PACKAGE}`, Artifact `{ARTIFACT}`, IPA `sha256:{IPA_SHA}`; exact scope + Debug Simulator and both formal CI lanes passed.
- UI fix is limited to separate user/assistant reuse identifiers for the same `ConversationMessageCell` class, preventing a UILabel that rendered a user Markdown link from entering the assistant pool. b111 diagnostics remain for Runtime verification.
- User link system-blue behavior and Send/SSE/Repository/recovery owners are unchanged; accepted clean-EOF recovery remains separately Unexercised.
- Module remains Active / Runtime Partial / Human Runtime pending / Stable-Frozen No.
"""
prepend_once(MODULE_STATUS, "## DEV-send-stream b112 role-isolated message-cell reuse package", module_section)

profile_section = f"""## Current DEV-send-stream package-qualified rendering-fix candidate — b112 2026-09-06

- `DEV-send-stream-0.1.0-b112` / `0.1.0 (112)` is the current package-qualified rendering-fix candidate.
- Product `{PRODUCT}`; package `{PACKAGE}`; Artifact `{ARTIFACT}`; ZIP `sha256:{ZIP_SHA}`; IPA `sha256:{IPA_SHA}`.
- Package independently verified `com.whitesharkssw.chatgptclient`, source `b5e3164721e0`, Release, iOS14+, iPhone/iPad families `[1,2]`, arm64.
- Human Runtime must verify role-isolated reuse removes assistant blue/normal alternation while preserving user link blue. Stable/Frozen No.
"""
prepend_once(PROJECT_PROFILE, "## Current DEV-send-stream package-qualified rendering-fix candidate — b112", profile_section)
