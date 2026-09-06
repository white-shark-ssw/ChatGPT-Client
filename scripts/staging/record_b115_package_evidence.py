from pathlib import Path

CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
BUILD_INDEX = Path("docs/project/BUILD_TEST_INDEX.md")
PROJECT_STATE = Path("docs/project/PROJECT_STATE.md")
MODULE_STATUS = Path("docs/project/MODULE_STATUS.md")
PROJECT_PROFILE = Path("docs/project/PROJECT_PROFILE.md")

PRODUCT = "2346c2d4ab26d40ef720b7850ae34316acb3cc62"
PACKAGE = "2dc0a4155f3549f32b1b08a9e4d8e6fb87495692"
STAGING = "34042595946/101511928494"
PUSH = "34042793058/101512446124"
PR = "34042795253/101512452040"
ARTIFACT = "9992196070"
ZIP_SHA = "19df7bac1354735cab404d81433b5818380da3e28b73dadaf29cb12f351fbd31"
IPA_SHA = "073b202ba26e400e7da0777fffa362f55f864be78a394a19258bfd027744dd41"
SOURCE_MARKER = "2dc0a4155f35"


def prepend_once(path: Path, marker: str, section: str) -> None:
    text = path.read_text()
    if marker in text:
        return
    path.write_text(section.rstrip() + "\n\n" + text)


def update_b115_row() -> None:
    text = BUILD_INDEX.read_text()
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| `DEV-send-stream-0.1.0-b115`"):
            lines[index] = (
                f"| `DEV-send-stream-0.1.0-b115` | `DEV-send-stream` | `0.1.0 (115)` | Runtime-regression correction product `{PRODUCT}`; package `{PACKAGE}`; PR #29 | corrected staging `{STAGING}` passed durable b114 Runtime recording/b115 allocation, exact two-product-path scope, `git diff --check`, exact behavior guards and Debug Simulator; Push `{PUSH}` passed; PR `{PR}` passed; canonical Artifact `{ARTIFACT}`; ZIP `{ZIP_SHA}`; IPA `{IPA_SHA}`; package independently verified `com.whitesharkssw.chatgptclient` / Build115 / Candidate b115 / source `{SOURCE_MARKER}` / Release / iOS14+ / `[1,2]` / arm64 | Human Runtime pending: one local protected Send must render exactly one user turn when active manual Sync materializes the authoritative user beyond the live baseline; Sync and Reload must remain available during active reasoning/generation; active Reload keeps existing local hard-reset/reacquire semantics and must not claim server Stop; preserve b114 follow-tail, b112 role isolation and b113 rich presentation. Exact clean EOF qualifies only if naturally observed | **Package-qualified b114 Runtime-regression correction candidate / Human Runtime pending / Stable-Frozen No; permanently reserved** |"
            )
            BUILD_INDEX.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))
            return
    raise SystemExit("b115 row not found")


update_b115_row()

checkpoint = f"""## b115 Runtime-regression correction — package ready 2026-09-06

Canonical identity / validation:

- Candidate `DEV-send-stream-0.1.0-b115` / `0.1.0 (115)` is permanently reserved from the b114 Runtime result.
- Exact product commit `{PRODUCT}` changes only `ChatGPTClient.xcodeproj/project.pbxproj` and `ChatGPTClient/Conversation/ConversationFeature.swift` after the b115 allocation checkpoint. `RootViewController.swift` is unchanged.
- Exact package source `{PACKAGE}` changes only `.github/workflows/ios-foundation.yml` after the product commit.
- Corrected guarded staging `{STAGING}` passed exact b114-product equivalence/b115-uniqueness, durable b114 Runtime recording + b115 allocation, exact two-product-path delta, `git diff --check`, behavior guards, Debug Simulator compile and exact product commit. Earlier staging attempts stopped in pre-product guards and produced neither b115 allocation nor product bits.
- Formal Push `{PUSH}` and PR `{PR}` both passed on exact package source `{PACKAGE}`.
- Canonical Push Artifact `{ARTIFACT}`; GitHub Artifact digest and independently recomputed ZIP SHA-256 both `{ZIP_SHA}`.
- Canonical IPA `ChatGPTClient-0.1.0-b115-dev-send-stream.ipa`; independently recomputed SHA-256 `{IPA_SHA}`, matching the packaged sidecar.
- Independent package inspection verifies `com.whitesharkssw.chatgptclient`, `0.1.0 (115)`, Candidate b115, source marker `{SOURCE_MARKER}`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS and Mach-O arm64.

Exact product behavior / negative scope:

- Manual `同步最新消息` is available during a local active response. Response activity is not a disable condition; only an already-running Detail sync/reload operation temporarily disables Sync. The Sync path remains one authoritative Detail read and never resends/regenerates the user prompt.
- Manual `重载当前会话` is available while a response is active. b114's active-response menu/handler block is removed. Existing Root hard-reload semantics remain authoritative: release the local covered executor when present, clear the local live projection, perform authoritative Detail reload and then re-arm external observation as needed. This is a local client reset/reacquire action and does not claim or synthesize server Stop.
- The live optimistic user row is presentation-only until the authoritative Detail suffix beyond `baselineVisibleMessageCount` contains a user turn. Once that authoritative user materializes, the same live generation stops rendering `local-live-user-*` while keeping its assistant reasoning/final presentation. This fixes the b114 duplicate user bubble without text matching, second message authority or any additional Send.
- b114 active-at-bottom follow-tail behavior remains intact. b112 user/assistant reuse isolation, b113 rich message presentation/Copy and b109-b111 diagnostic retirement remain intact.
- `RootViewController.swift`, protected Send count, covered official-Web/SSE parsing, b107 accepted clean-EOF same-generation recovery, Repository content/response ownership, auth/read transport and server Stop transport are unchanged.
- No retry, fallback, timer/watchdog, polling, duplicate Send, regenerate, guessed resume/status, second response store, compatibility shim or fake Stop is added.

Human Runtime gate:

1. Install only canonical b115 Artifact `{ARTIFACT}` / IPA `{IPA_SHA}` and fresh-launch.
2. In an existing conversation start one deliberately long local protected response. While reasoning/generation is active, open the menu: both `同步最新消息` and `重载当前会话` must be enabled.
3. During that active response tap `同步最新消息` once after the server-side user turn has had time to materialize. The UI must continue to show exactly one user bubble for that turn; diagnostics should show the authoritative message count advance while `liveUserPresentationCount` becomes/remains `0` for the overlapping live generation. There must still be exactly one protected Send / one `sendObserved` for the user action and no local `phase=failed` merely because Sync was used.
4. Regression-check b114 hidden follow-tail: active A left at bottom -> B -> A returns to current latest tail; deliberate upward reading -> B -> A restores the historical anchor.
5. In a separate long active response tap `重载当前会话`. The action must execute rather than be disabled. It may release the local executor/live projection and reacquire authoritative Detail/external observation, but must not issue a second protected Send and must not be described as server Stop. The visible user turn must still not duplicate after authoritative reload.
6. Let at least one ordinary protected Send reach natural terminal + authoritative Detail convergence without duplicate user bubbles or `回答失败`. Regression-check b113 link/Markdown/file-reference rendering, normal assistant color and Copy.
7. Export Diagnostics. If exact accepted post-HTTP200-SSE `stream_ended_without_done` naturally appears, additionally classify inherited b107 same-generation/no-resend clean-EOF recovery; otherwise keep that branch Unexercised.

Remaining evidence boundaries:

- Exact b107 accepted clean EOF remains Unexercised until the event naturally occurs; b115 does not alter that code.
- Server Stop remains unimplemented. Existing Reload is explicitly a local hard reset/reacquire and must not be used as evidence that `/stop_conversation` semantics are known.
- b101 exact `-1005` renewal and natural b98 external WebContent-death remain conditional evidence debts only and are not manufactured as closeout blockers.

**Evidence ladder:** Code written / exact scope + `git diff --check` + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / overall `DEV-send-stream` Runtime Partial / Stable-Frozen No.

**Next exact action:** install only canonical b115 and execute the Human Runtime gate above. Do not allocate b116 before b115 Runtime unless a new independent blocker makes b115 untestable.
"""
prepend_once(CHECKPOINT, "## b115 Runtime-regression correction — package ready", checkpoint)

state = f"""## DEV-send-stream b115 package-qualified Runtime correction — 2026-09-06

- Canonical b115 product `{PRODUCT}` / package `{PACKAGE}` passed corrected staging `{STAGING}`, same-source Push `{PUSH}` and PR `{PR}` CI.
- Artifact `{ARTIFACT}` / ZIP `sha256:{ZIP_SHA}` / IPA `sha256:{IPA_SHA}` independently verify Build115 / Candidate b115 / source `{SOURCE_MARKER}` / Release / iOS14+ / `[1,2]` / arm64.
- b115 corrects two b114 Runtime regressions only: optimistic user presentation yields to the authoritative user turn beyond the live baseline, and active reasoning/generation no longer disables manual Sync/Reload. b114 follow-tail and all Send/SSE/Repository/recovery owners remain unchanged.
- Human Runtime is pending. Exact accepted clean EOF and server Stop remain separately evidence-gated; Stable-Frozen No.
"""
prepend_once(PROJECT_STATE, "## DEV-send-stream b115 package-qualified Runtime correction", state)

module = f"""## DEV-send-stream b115 package-qualified Runtime correction — 2026-09-06

- Product `{PRODUCT}` / package `{PACKAGE}` / Artifact `{ARTIFACT}` is the current Send-owned Human Runtime candidate.
- Exact scope: restore active Sync/Reload availability and suppress only the optimistic live-user presentation after authoritative user materialization beyond `baselineVisibleMessageCount`; preserve b114 follow-tail, b112 reuse isolation, b113 rich presentation and all protected Send/SSE/recovery owners.
- Simulator + Push + PR CI + Artifact/package verification are complete. Human Runtime pending; clean EOF and server Stop remain unverified; Stable-Frozen No.
"""
prepend_once(MODULE_STATUS, "## DEV-send-stream b115 package-qualified Runtime correction", module)

profile = f"""## Current DEV-send-stream package-qualified candidate — b115 2026-09-06

- `DEV-send-stream-0.1.0-b115` / `0.1.0 (115)` is canonical at product `{PRODUCT}`, package `{PACKAGE}`, Artifact `{ARTIFACT}`, ZIP `sha256:{ZIP_SHA}`, IPA `sha256:{IPA_SHA}`.
- Package independently verifies bundle `com.whitesharkssw.chatgptclient`, source `{SOURCE_MARKER}`, Release iPhoneOS, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, arm64.
- Human Runtime pending; Stable/Frozen No.
"""
prepend_once(PROJECT_PROFILE, "## Current DEV-send-stream package-qualified candidate — b115", profile)
