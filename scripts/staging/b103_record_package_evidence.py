from pathlib import Path
import sys

PRODUCT = "d514e9a5bde01bf3243d81016bf8cbda533fd5bf"
PACKAGE = "e1cca160e9c466ab98a2aeffc038e94f58335cab"
RUNTIME_SHA = "6d2fde277427d3bbad6549946855c68b8df7e0433389b2d5c9e7d98212a3a6a6"
ZIP_SHA = "27fc23f1cb48d585ab3ffc0b181ec0dffafc42ccb3069fd72cbf5a0ba647f77a"
IPA_SHA = "f41c81a89552027fb4c42152eb3864c1732494465230ffd4787c6bba56d746c3"
CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
RECOVERY_HEADING = "## b103 package-evidence batch recovery point — 2026-09-05"
FINAL_HEADING = "## b103 accepted-client hard-Web recovery — package ready 2026-09-05"


def prepend(path: str, heading: str, section: str) -> None:
    p = Path(path)
    text = p.read_text()
    if heading not in text:
        p.write_text(section + text)


def checkpoint_mode() -> None:
    text = CHECKPOINT.read_text()
    if RECOVERY_HEADING in text:
        return
    section = f"""{RECOVERY_HEADING}

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29; canonical product `{PRODUCT}`; canonical package source `{PACKAGE}`; Candidate `DEV-send-stream-0.1.0-b103` / Build103.
- Canonical Push `33914210593 / 101157497020` and PR `33914214638 / 101157509705` are success. Canonical Push Artifact `9952548424`; ZIP `sha256:{ZIP_SHA}`; IPA `sha256:{IPA_SHA}` independently matches sidecar and package metadata.
- Intended write batches: (A) this checkpoint recovery point; (B) update this checkpoint plus BUILD_TEST_INDEX / PROJECT_PROFILE / PROJECT_STATE / MODULE_STATUS / TECHNICAL_DECISIONS with b102 Runtime + b103 package evidence; (C) update PR #29 metadata after GitHub state is re-read.
- Confirmed before batch A: product/package/CI/Artifact/package identity are verified; main remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`; parallel PR #35 remains draft at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142` with no product/candidate conflict.
- Recovery must not alter b103 product/package identity, rebuild/repackage the canonical Artifact, allocate b104, touch PR #35, or rewrite earlier reserved Candidate identities.

**Next exact action:** finish docs batch B only, verify branch state, then update PR #29 metadata as batch C and hand canonical b103 IPA to Human Runtime.

"""
    CHECKPOINT.write_text(section + text)


def final_mode() -> None:
    text = CHECKPOINT.read_text()
    if RECOVERY_HEADING in text:
        start = text.index(RECOVERY_HEADING)
        next_heading = text.find("\n## ", start + len(RECOVERY_HEADING))
        if next_heading < 0:
            raise SystemExit("cannot locate end of b103 recovery section")
        text = text[:start] + text[next_heading + 1:]
    if FINAL_HEADING not in text:
        section = f"""{FINAL_HEADING}

Exact package evidence:

- Candidate `DEV-send-stream-0.1.0-b103` / `0.1.0 (103)`, permanently reserved. Exact product `{PRODUCT}`; canonical package source `{PACKAGE}`. b103 is a Runtime recovery test candidate, not Stable/Frozen.
- Corrected guarded staging `33913972639 / 101156743875` passed b102 Runtime/checkpoint allocation, exact three-product-file scope audit and Debug Simulator compile, then committed product `{PRODUCT}`. Earlier staging `33913633892 / 101155651591` stopped before product write while matching the docs allocation marker and emitted no b103 product commit.
- Formal Push `33914210593 / 101157497020` and PR `33914214638 / 101157509705` both passed on exact package source `{PACKAGE}`.
- Canonical Push Artifact `9952548424`; downloaded Artifact ZIP independently recomputed `sha256:{ZIP_SHA}`, matching GitHub's Artifact digest.
- Canonical IPA `ChatGPTClient-0.1.0-b103-dev-send-stream.ipa`; independently recomputed `sha256:{IPA_SHA}`, matching the emitted sidecar.
- Independent package inspection confirms `com.whitesharkssw.chatgptclient`, `0.1.0 (103)`, Candidate b103, source marker `e1cca160e9c4`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, `iPhoneOS`, Mach-O 64-bit arm64. Binary strings include the exact b103 Candidate, `coveredExecutor.acceptedClientWebProcessRecovery`, `acceptedClientRecovery.started`, and `_killWebContentProcessAndResetState`.

Behavior / evidence boundary:

- b102 Human Runtime `sha256:{RUNTIME_SHA}` proved the original client Send had exactly one protected Send and explicit HTTP200 SSE acceptance before deterministic WebContent death; server generation survived, and the same turn later resumed through existing covered observation/Detail with no second Send and reached terminal/final convergence.
- b103 therefore changes hard WebContent death only after exact client SSE acceptance: preserve the same prompt-owned Repository generation, emit `acceptedClientWebProcessInterrupted` instead of `.failed`, release the dead executor, and attach one fresh covered observer to the same generation immediately while active or on next foreground when inactive. It never resends/replays/regenerates the prompt.
- The one-shot 120-second kill remains Candidate-gated deterministic Human Runtime instrumentation only. It is not a production timeout/watchdog and must be removed/disabled before a later normal/Stable candidate.

Evidence ladder: **Code written / exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / b102 causal Runtime Positive / b103 recovery Runtime pending / Stable-Frozen No.**

**Next exact action:** install only canonical b103. Fresh-launch, open an existing conversation, start one deliberately >2-minute Native Send, keep the app foreground, and do not touch Sync/Reload/Stop or background the app. At ~120s expect `killProbe firing -> webProcess terminated -> acceptedClientWebProcessRecovery state=handoff_requested -> acceptedClientRecovery.started` with the same `responseGeneration`, followed by covered `IS_STREAMING`/snapshot/resume/live continuation and final terminal reconcile. There must be exactly one protected Send and no lifecycle nudge.

"""
        text = section + text
    CHECKPOINT.write_text(text)

    index = Path("docs/project/BUILD_TEST_INDEX.md")
    lines = index.read_text().splitlines()
    b103 = f"| `DEV-send-stream-0.1.0-b103` | `DEV-send-stream` | `0.1.0 (103)` | accepted-client hard-Web recovery product `{PRODUCT}`; package `{PACKAGE}`; PR #29 | corrected staging `33913972639/101156743875` exact three-product-file scope + Simulator passed; initial `33913633892/101155651591` stopped before product write; Push `33914210593/101157497020` passed; PR `33914214638/101157509705` passed; canonical Artifact `9952548424`; ZIP `{ZIP_SHA}`; IPA `{IPA_SHA}`; b103/source/iOS14/[1,2]/arm64 verified | Human Runtime pending: exact b103 retains one 120s diagnostic forced-Web kill. After explicit client Send HTTP200 SSE acceptance, hard WebContent death must preserve the same Repository generation and automatically attach one fresh covered observer with no second Send and no foreground/background nudge | **Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity verified / Runtime pending / Stable-Frozen No; permanently reserved** |"
    b102 = f"| `DEV-send-stream-0.1.0-b102` | `DEV-send-stream` | `0.1.0 (102)` | deterministic client-owned covered-Web kill probe product `670310b4e8b15176f721291f4f96e46feadec46a`; package `78bd3d2f3e45c8e0061865d3133b92a274139110`; PR #29 | Push `33910845721/101146639944` passed; PR `33910858535/101146674919` passed; canonical Artifact `9951331101`; ZIP `2da6bb66d0c5eba55d93463881e0ff5d0d55a9d7844f068d024e5cee31dff24a`; IPA `53eb1845a3fbd4543ebdb5e9a69e078b3f07866c2c395a666dca9b2928ecd8af`; b102/source/iOS14/[1,2]/arm64 verified | Runtime `sha256:{RUNTIME_SHA}` decisive: one protected Send received HTTP200 SSE, 120s probe killed WebContent while active, old local generation failed/released, but server turn survived. One later lifecycle return rediscovered the same unfinished turn; covered `IS_STREAMING` + HTTP200 SSE resume/live events reached terminal/final, authoritative Detail converged, and there was no second Send | **Diagnostic Runtime Positive for accepted-turn server survival + existing no-resend reacquisition primitive / b102 local failure behavior superseded by b103 recovery gate / Stable-Frozen No; permanently reserved** |"
    found103 = found102 = False
    for i, line in enumerate(lines):
        if line.startswith("| `DEV-send-stream-0.1.0-b103` |"):
            lines[i] = b103
            found103 = True
        elif line.startswith("| `DEV-send-stream-0.1.0-b102` |"):
            lines[i] = b102
            found102 = True
    if not found103 or not found102:
        raise SystemExit("b102/b103 index row not found")
    index.write_text("\n".join(lines) + "\n")

    profile_heading = "## Latest DEV-send-stream candidate override — b103 2026-09-05"
    profile_section = f"""{profile_heading}

- Latest Human Runtime candidate is now `DEV-send-stream-0.1.0-b103` / `0.1.0 (103)`, permanently reserved. b103 converts only explicitly accepted client-owned hard WebContent death into same-generation covered-observer handoff; it never resends the prompt. Exact product `{PRODUCT}`; package source `{PACKAGE}`.
- Corrected staging `33913972639/101156743875`, Push `33914210593/101157497020` and PR `33914214638/101157509705` passed. Canonical Artifact `9952548424`; ZIP `sha256:{ZIP_SHA}`; IPA `sha256:{IPA_SHA}`; package identity independently verified as Release b103/source `e1cca160e9c4`/iOS14+/`[1,2]`/arm64.
- b102 Runtime `sha256:{RUNTIME_SHA}` is decisive for the causal premise: exact client Send was accepted once, WebContent death did not kill the server turn, and existing covered/Detail reacquisition completed the same turn without a second Send. b103 recovery itself remains Human Runtime pending; Stable/Frozen No.

"""
    prepend("docs/project/PROJECT_PROFILE.md", profile_heading, profile_section)

    state_heading = "## DEV-send-stream b103 accepted-client hard-Web recovery package ready — 2026-09-05"
    state_section = f"""{state_heading}

- b102 Human Runtime `sha256:{RUNTIME_SHA}` proves an explicitly accepted client-owned protected Send can survive hard WebContent death server-side and later finish through the existing covered observation + authoritative Detail chain without a second Send. The remaining defect was local: b102 marked the prompt-owned generation failed and required a lifecycle nudge to rediscover it.
- b103 preserves that same Repository generation after hard WebContent death **only after** HTTP200 `text/event-stream` Send acceptance. While active it immediately releases the dead executor and attaches one fresh covered observer; while inactive it defers the reattach until foreground. Pre-acceptance death remains failure. No prompt replay/regenerate, retry loop, polling, heartbeat, guessed resume or second response store is added.
- Exact product `{PRODUCT}`; package `{PACKAGE}`; corrected staging `33913972639/101156743875`; Push `33914210593/101157497020`; PR `33914214638/101157509705`; canonical Artifact `9952548424`; ZIP `sha256:{ZIP_SHA}`; IPA `sha256:{IPA_SHA}`. Independent package inspection verifies b103/source `e1cca160e9c4`/Release/iOS14+/arm64.
- Human Runtime pending. The b103 120-second kill is still explicit test instrumentation only; no true background-execution claim. Stable-Frozen No.

"""
    prepend("docs/project/PROJECT_STATE.md", state_heading, state_section)

    module_heading = "## DEV-send-stream b103 accepted-client hard-Web recovery — 2026-09-05"
    module_section = f"""{module_heading}

- `ConversationRepository` remains sole Native response/content/lifecycle authority. b103 does not create a second response object when the covered WebContent process dies after Send acceptance; the existing prompt-owned generation remains active and receives the fresh covered observer's already-evidenced external continuation events.
- `CoveredWebSendExecutor` now distinguishes explicit accepted-client transport death from pre-acceptance failure. Accepted-client death emits `acceptedClientWebProcessInterrupted`, clears only the dead executor transport state, and Root replaces it with one observer for the same conversation/generation. No protected Send is repeated.
- b102 Runtime proves the server-turn survival/no-second-Send premise. b103 exact product/package `{PRODUCT}` / `{PACKAGE}`; staging + Push + PR CI passed; Artifact `9952548424`; IPA `sha256:{IPA_SHA}`; package identity verified. Recovery Runtime pending; module remains Active / Runtime Partial / Stable-Frozen No.

"""
    prepend("docs/project/MODULE_STATUS.md", module_heading, module_section)

    decision_heading = "## DEV-send-stream b103 accepted-client hard-Web recovery decision — 2026-09-05"
    decision_section = f"""{decision_heading}

- b102 Runtime changes the evidence boundary: after one exact protected Send returned HTTP200 `text/event-stream`, deterministic `webViewWebContentProcessDidTerminate` caused only local transport/lifecycle failure; the server turn stayed alive and the existing covered observation/Detail path later reacquired and completed it with no second Send. Hard death after explicit acceptance is therefore a recoverable receive-transport interruption for this tested scenario, not proof that the server response failed.
- Authorize b103 to preserve the same prompt-owned `ConversationRepository` generation on that exact hard signal **only when client Send acceptance has already been observed**. Release the dead executor and attach one fresh covered observer for the same conversation/generation immediately if active or on next foreground if inactive. Feed only the existing evidenced external streaming/snapshot/resume/terminal events back into the same Repository owner.
- Before Send acceptance, existing failure semantics remain. Navigation errors, silence, focus/route state and elapsed time are not promoted to disconnect signals. No resend/regenerate, retry loop, polling, heartbeat, challenge replay, guessed Native resume or second response/content authority is authorized.
- The b103 120-second kill remains Candidate-gated test instrumentation, not product timeout policy, and must not continue into a later normal/Stable candidate after this Runtime gate is closed.

"""
    prepend("docs/project/TECHNICAL_DECISIONS.md", decision_heading, decision_section)


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in {"checkpoint", "final"}:
        raise SystemExit("usage: b103_record_package_evidence.py checkpoint|final")
    if sys.argv[1] == "checkpoint":
        checkpoint_mode()
    else:
        final_mode()


if __name__ == "__main__":
    main()
