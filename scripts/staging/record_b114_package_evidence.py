from pathlib import Path

CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
BUILD_INDEX = Path("docs/project/BUILD_TEST_INDEX.md")
PROJECT_STATE = Path("docs/project/PROJECT_STATE.md")
MODULE_STATUS = Path("docs/project/MODULE_STATUS.md")
PROJECT_PROFILE = Path("docs/project/PROJECT_PROFILE.md")

PRODUCT = "673f2905ddc7a5aba23317e81e75677b2e81edb3"
PACKAGE = "ef98a038a165bdcef90b0abea67c25b7ef96e57f"
STAGING = "33995851115/101386150523"
PUSH = "33995968361/101386467170"
PR = "33995970064/101386471305"
ARTIFACT = "9978074978"
ZIP_SHA = "f36fb5ebe3dc8db6b41ab891e66d337fa9ebcd17b6936440490f113f0c412aa9"
IPA_SHA = "f2c793f8eeff3f83d30fa9fec69ee7953ff7f3e431c07a49b7b9b20931a6b192"


def prepend_once(path: Path, marker: str, section: str) -> None:
    text = path.read_text()
    if marker in text:
        return
    path.write_text(section.rstrip() + "\n\n" + text)


def update_b114_row() -> None:
    text = BUILD_INDEX.read_text()
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| `DEV-send-stream-0.1.0-b114`"):
            lines[index] = (
                f"| `DEV-send-stream-0.1.0-b114` | `DEV-send-stream` | `0.1.0 (114)` | Phase 9 closeout product `{PRODUCT}`; package `{PACKAGE}`; PR #29 | staging `{STAGING}` exact two-product-path scope + `git diff --check` + Debug Simulator passed; Push `{PUSH}` passed; PR `{PR}` passed; canonical Artifact `{ARTIFACT}`; ZIP `{ZIP_SHA}`; IPA `{IPA_SHA}`; package independently verified `com.whitesharkssw.chatgptclient` / Build114 / Candidate b114 / source `ef98a038a165` / Release / iOS14+ / `[1,2]` / arm64 | Human Runtime pending: long local A response left at bottom -> B -> A must return to current tail; user-scrolled-up A -> B -> A must restore history anchor; local-active Sync/Reload must remain unavailable; after terminal Reload returns; ordinary one-Send terminal/reconcile, b113 rendering, Copy and no-blue regression must remain intact. Exact b107 clean EOF qualifies only if `stream_ended_without_done` naturally occurs | **Package-qualified Phase 9 closeout Human Runtime candidate / Stable-Frozen No; permanently reserved** |"
            )
            BUILD_INDEX.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))
            return
    raise SystemExit("b114 row not found")


update_b114_row()

checkpoint = f"""## b114 Phase 9 closeout — package ready 2026-09-06

Canonical identity / validation:

- Candidate `DEV-send-stream-0.1.0-b114` / `0.1.0 (114)` is permanently reserved.
- Exact product commit `{PRODUCT}` changes only `ChatGPTClient.xcodeproj/project.pbxproj` and `ChatGPTClient/Conversation/ConversationFeature.swift` after the b114 allocation checkpoint.
- Exact package source `{PACKAGE}` changes only `.github/workflows/ios-foundation.yml` after the product commit.
- Guarded staging `{STAGING}` passed b113-baseline/b114-uniqueness guards, durable b114 allocation, exact two-product-path scope, `git diff --check`, Debug Simulator compile and exact product commit.
- Formal Push `{PUSH}` and PR `{PR}` both passed on exact package source `{PACKAGE}`.
- Canonical Push Artifact `{ARTIFACT}`; GitHub Artifact digest and independently recomputed ZIP SHA-256 both `{ZIP_SHA}`.
- Canonical IPA `ChatGPTClient-0.1.0-b114-dev-send-stream.ipa`; independently recomputed SHA-256 `{IPA_SHA}`, matching the packaged sidecar.
- Independent package inspection verifies `com.whitesharkssw.chatgptclient`, `0.1.0 (114)`, Candidate b114, source marker `ef98a038a165`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS and Mach-O arm64.

Exact product behavior / negative scope:

- Active displayed conversation left at the already-existing exact physical-bottom threshold no longer persists a historical scroll anchor. Existing anchor absence continues to mean `scrollToLatestMessage`, so hidden active growth may return at current tail without a second follow-tail state store. Deliberate upward reading still records the existing message/chunk-relative semantic anchor.
- Conversation menu Reload is disabled while any live response is active; the reload handler independently rejects a direct active invocation. This prevents manual Reload from releasing covered execution and clearing live projection while server Stop remains unproven. Existing client-owned active Sync block is preserved; external-active manual Sync remains available as the already-evidenced authoritative recovery action.
- b109-b111 per-chunk UILabel/pixel diagnostics are removed after b112/b113 Runtime acceptance. b112 user/assistant reuse isolation and b113 rich presentation remain intact.
- `RootViewController.swift`, covered protected Send, SSE parsing, b107 clean-EOF same-generation recovery, one-Send/no-resend policy, Repository response/content ownership, auth/read transport and server Stop behavior are unchanged.
- No retry, fallback, timer/watchdog, polling, duplicate Send, regenerate, guessed resume/status, new response store or fake Stop is added.

Human Runtime gate:

1. Install only canonical b114 Artifact `{ARTIFACT}` / IPA `{IPA_SHA}` and fresh-launch.
2. In conversation A start one deliberately long local/client-owned response while at the physical bottom. While it is active, open the conversation menu: both Sync and Reload must be unavailable.
3. While still at bottom, switch A -> B -> A after A has grown or completed. A must return to the current latest tail rather than the old departure position.
4. Repeat with A active but intentionally scroll upward before A -> B -> A. Return must restore the historical message/chunk-relative reading position rather than snap to bottom.
5. Let one ordinary protected Send reach natural terminal + authoritative Detail convergence; require no duplicate protected Send and no `回答失败`. After the response is no longer active, Reload must become available again.
6. Regression-check b113 Markdown/link/file-reference rendering, normal assistant color, and Copy interaction; export Diagnostics.
7. If exact accepted post-HTTP200-SSE `stream_ended_without_done` naturally appears, additionally classify b107 same-generation/no-resend clean-EOF recovery. If it does not occur, keep that branch Unexercised.

Remaining evidence gates after b114 package:

- Exact b107 accepted clean EOF remains Unexercised until the event occurs; b114 does not alter that code.
- Server Stop remains unimplemented. Official-app static strings expose `StopConversationRequest`, `/stop_conversation`, `stopConversation(id:requestTrackingData:)` and failure text, but method/body/target/ack/terminal semantics remain Runtime-unverified and must not be guessed.

**Evidence ladder:** Code written / exact scope + `git diff --check` + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / overall `DEV-send-stream` Runtime Partial / Stable-Frozen No.

**Next exact action:** install only canonical b114 and execute the Human Runtime matrix above. Do not allocate b115 before b114 Runtime unless a new independent blocker makes b114 untestable.
"""
prepend_once(CHECKPOINT, "## b114 Phase 9 closeout — package ready", checkpoint)

state = f"""## DEV-send-stream b114 package-qualified closeout gate — 2026-09-06

- Canonical b114 product `{PRODUCT}` / package `{PACKAGE}` passed guarded staging `{STAGING}`, same-source Push `{PUSH}` and PR `{PR}` CI.
- Artifact `{ARTIFACT}` / ZIP `sha256:{ZIP_SHA}` / IPA `sha256:{IPA_SHA}` independently verify Build114 / Candidate b114 / source `ef98a038a165` / Release / iOS14+ / `[1,2]` / arm64.
- b114 closes only source-proven follow-tail intent and active-Reload safety gaps and removes fulfilled color probes; Human Runtime is pending. Server Stop and exact accepted clean EOF remain separately evidence-gated.
"""
prepend_once(PROJECT_STATE, "## DEV-send-stream b114 package-qualified closeout gate", state)

module = f"""## DEV-send-stream b114 package-qualified Phase 9 closeout — 2026-09-06

- Product `{PRODUCT}` / package `{PACKAGE}` / Artifact `{ARTIFACT}` is the current Send-owned Human Runtime candidate.
- Exact scope: active-at-bottom hidden follow-tail through existing anchor semantics, disable/guard Reload while any response is active, retire fulfilled b109-b111 color diagnostics; preserve b112/b113 presentation and all Send/SSE/Repository/recovery transport owners.
- Simulator + Push + PR CI + Artifact/package verification are complete. Human Runtime pending; clean EOF and server Stop remain unverified; Stable-Frozen No.
"""
prepend_once(MODULE_STATUS, "## DEV-send-stream b114 package-qualified Phase 9 closeout", module)

profile = f"""## Current DEV-send-stream package-qualified closeout candidate — b114 2026-09-06

- `DEV-send-stream-0.1.0-b114` / `0.1.0 (114)` is canonical at product `{PRODUCT}`, package `{PACKAGE}`, Artifact `{ARTIFACT}`, ZIP `sha256:{ZIP_SHA}`, IPA `sha256:{IPA_SHA}`.
- Package independently verifies bundle `com.whitesharkssw.chatgptclient`, source `ef98a038a165`, Release iPhoneOS, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, arm64.
- Human Runtime pending; Stable/Frozen No.
"""
prepend_once(PROJECT_PROFILE, "## Current DEV-send-stream package-qualified closeout candidate — b114", profile)
