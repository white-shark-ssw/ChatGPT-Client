from pathlib import Path
from textwrap import dedent


def prepend_once(path_str: str, marker: str, block: str) -> None:
    path = Path(path_str)
    text = path.read_text()
    if marker in text:
        return
    path.write_text(dedent(block).strip() + "\n\n" + text)


def insert_after_once(path_str: str, anchor: str, marker: str, block: str) -> None:
    path = Path(path_str)
    text = path.read_text()
    if marker in text:
        return
    if anchor not in text:
        raise SystemExit(f"missing anchor in {path_str}: {anchor!r}")
    replacement = anchor + "\n\n" + dedent(block).strip()
    path.write_text(text.replace(anchor, replacement, 1))


prepend_once(
    "docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md",
    "## b113 stacked integration completed — DEV-send-stream owner 2026-09-06",
    """
    ## b113 stacked integration completed — DEV-send-stream owner 2026-09-06

    Exact integration result:

    - Work ID remains `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 remains open against unchanged `main@94f0c5777dad262cd1fb22be49082dbd92c962f2`.
    - Batch I2 completed exactly once: PR #36 `DEV-message-rendering` head `d5d761bfad26bc90953488ccd5a96452bf356b3a` merged normally into the owning branch at merge commit `4a22086f7ccab39427c46a163854e8f68530c65f`. PR #36 is closed/merged.
    - Batch I3 passed: current integrated product is Build113 with `DIAGNOSTICS_CANDIDATE = \"DEV-message-rendering-0.1.0-b113\"` in both Debug and Release. Candidate b113 remains permanently owned/reserved by `DEV-message-rendering`; b112 remains the last `DEV-send-stream`-owned canonical candidate.
    - Canonical b113 product/package/Runtime identity remains product `7d1ddc8eaa164c9b307f525b00bb0e1404f395e9`, package source `75ccad15208610c2b0420033846f9bb15bbdb494`, Artifact `9976713893`, IPA `sha256:2cf62b87117f9279816de68f2ed3ce83768d203198b555fe4fe0042f8d367c3f`, Human Runtime Positive for the tested native message-presentation scope.
    - Compare `75ccad15208610c2b0420033846f9bb15bbdb494..4a22086f7ccab39427c46a163854e8f68530c65f` contains only docs/tooling changes after the canonical package source; there are zero `ChatGPTClient/**` or `ChatGPTClient.xcodeproj/project.pbxproj` product-path changes. Existing b113 package/Runtime evidence therefore remains applicable to the integrated product bits; integration itself creates no new Runtime evidence.
    - PR #29 post-merge PR CI `33993974639` (`ios-foundation.yml`, head `4a22086f7ccab39427c46a163854e8f68530c65f`) completed successfully.
    - Parallel PR #35 remains draft research-only at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142` and owns no product `ChatGPTClient/**`, product Xcode Candidate, or Build113 identity.

    Integration classification:

    - I0 recovery point: completed.
    - I1 merge/conflict guard: completed.
    - I2 PR #36 merge: completed.
    - I3 post-merge identity/product-equivalence/PR-CI verification: completed.
    - I4 durable state recording: completed by the guarded integration recorder that added this section and the corresponding shared durable records; PR #29 metadata is updated separately in the same work cycle.
    - No b114 was allocated. No new Send/Stream product behavior was written by integration.
    - b112 assistant-color correction remains Human Runtime Positive. b113 native message presentation remains Human Runtime Positive for its tested scope. The inherited b107 accepted `stream_ended_without_done` clean-EOF same-generation recovery remains Unexercised / Unverified, so overall `DEV-send-stream` remains Active / Runtime Partial / Stable-Frozen No.

    The older `b113 stacked integration recovery point` below is historical recovery state and must not be replayed. On resume, first read this completed section and current GitHub state.

    **Evidence ladder:** b112 Send-owned candidate Runtime Positive for assistant color / b113 imported product Code written + exact scope + Debug Simulator passed + Push CI passed + PR CI passed + Artifact produced + package identity independently verified + Human Runtime Positive for tested presentation scope / stacked integration merge completed + post-merge PR #29 CI passed / accepted clean-EOF recovery Unexercised / overall `DEV-send-stream` Runtime Partial / Stable-Frozen No.

    **Next exact action:** do not allocate a new Send/Stream Candidate merely because b113 is now integrated. Continue `DEV-send-stream` only from new evidence for an actually open Send/Stream gate; notably, if exact post-acceptance `stream_ended_without_done` occurs, capture canonical diagnostics and classify the inherited b107 clean-EOF recovery. Otherwise preserve the integrated b113 baseline and existing one-Send/Repository authority invariants.
    """,
)

prepend_once(
    "docs/project/PROJECT_PROFILE.md",
    "## Current DEV-send-stream integrated product baseline — imported b113 2026-09-06",
    """
    ## Current DEV-send-stream integrated product baseline — imported b113 2026-09-06

    - `dev/send-stream-20260829` now carries merged PR #36 at integration commit `4a22086f7ccab39427c46a163854e8f68530c65f`; product settings are `0.1.0 (113)` / Candidate `DEV-message-rendering-0.1.0-b113`.
    - Build113/Candidate b113 remains owned by `DEV-message-rendering`; integration does not reassign it to `DEV-send-stream`. The last `DEV-send-stream`-owned canonical candidate remains b112 (`3957b806...` / package `b5e31647...` / Artifact `9975978222`).
    - Canonical imported b113 package remains source `75ccad15208610c2b0420033846f9bb15bbdb494`, Artifact `9976713893`, IPA `sha256:2cf62b87117f9279816de68f2ed3ce83768d203198b555fe4fe0042f8d367c3f`; its tested presentation scope is Human Runtime Positive.
    - `75ccad... -> 4a22086...` changes only docs/tooling, so integration has no new product delta relative to the tested b113 package bits. Post-merge PR #29 CI `33993974639` passed.
    - No b114 is allocated. Overall `DEV-send-stream` remains Runtime Partial / Stable-Frozen No because accepted clean-EOF recovery remains Unexercised.
    """,
)

prepend_once(
    "docs/project/PROJECT_STATE.md",
    "## DEV-send-stream stacked b113 integration complete — 2026-09-06",
    """
    ## DEV-send-stream stacked b113 integration complete — 2026-09-06

    - PR #36 `DEV-message-rendering` merged exactly once into `dev/send-stream-20260829` at `4a22086f7ccab39427c46a163854e8f68530c65f`; PR #29 remains the owning Send/Stream PR against unchanged `main@94f0c5777dad262cd1fb22be49082dbd92c962f2`.
    - Integrated Xcode product identity is Build113 / Candidate `DEV-message-rendering-0.1.0-b113`. Candidate ownership stays with `DEV-message-rendering`; b112 remains the last `DEV-send-stream`-owned canonical Candidate.
    - No product path changed after canonical b113 package source `75ccad15208610c2b0420033846f9bb15bbdb494`; the merge only combines already-tested b113 product bits with later docs/tooling. PR #29 post-merge CI `33993974639` passed on merge head `4a22086f...`.
    - b113 Human Runtime remains Positive only for its tested native presentation scope; integration is not a new Runtime test. b112 assistant-color evidence remains accepted.
    - The b107 exact accepted `stream_ended_without_done` clean-EOF recovery is still Unexercised / Unverified. `DEV-send-stream` remains Active / Runtime Partial / Stable-Frozen No. No b114 is justified by integration alone.
    """,
)

prepend_once(
    "docs/project/MODULE_STATUS.md",
    "## DEV-send-stream imported b113 presentation baseline integrated — 2026-09-06",
    """
    ## DEV-send-stream imported b113 presentation baseline integrated — 2026-09-06

    - PR #36 is merged into the Send/Stream branch at `4a22086f7ccab39427c46a163854e8f68530c65f`. The branch now carries Build113 / `DEV-message-rendering-0.1.0-b113` as an imported product baseline, not as a new `DEV-send-stream` Candidate.
    - Product equivalence to canonical b113 package source `75ccad15208610c2b0420033846f9bb15bbdb494` is preserved: subsequent/integration changes are docs/tooling only. Post-merge PR #29 CI `33993974639` passed.
    - b112 role-isolated assistant-color behavior remains Runtime accepted; b113 rich Markdown/link/citation presentation remains Runtime Positive for the tested scope.
    - Send/Stream module remains Active / Runtime Partial / Stable-Frozen No because accepted clean-EOF recovery remains Unexercised. Integration adds no resend/retry/polling/second authority and allocates no b114.
    """,
)

prepend_once(
    "docs/project/TECHNICAL_DECISIONS.md",
    "## DEV-send-stream stacked candidate ownership after b113 integration — 2026-09-06",
    """
    ## DEV-send-stream stacked candidate ownership after b113 integration — 2026-09-06

    - Accept PR #36's tested b113 product into the owning `DEV-send-stream` branch by ordinary merge at `4a22086f7ccab39427c46a163854e8f68530c65f` because the dependency was explicitly stacked and the current base advanced only through docs/tooling.
    - Preserve Candidate ownership across integration: Build113 / `DEV-message-rendering-0.1.0-b113` remains owned/reserved by `DEV-message-rendering`; importing those exact product bits does not silently create or rename a `DEV-send-stream` Candidate. b112 remains the last Send-owned canonical Candidate.
    - Existing b113 package/Runtime evidence may be carried into the integrated branch only because compare proves zero product-path change after canonical package source `75ccad15208610c2b0420033846f9bb15bbdb494`. Integration CI is compile/package evidence, not new Human Runtime proof.
    - No b114, retry, fallback, timer/watchdog, polling, duplicate Send, second response/content authority or new completion heuristic is authorized by the merge. The b107 accepted clean-EOF Runtime gate remains separately open.
    """,
)

prepend_once(
    "docs/project/PROJECT_SPECIFIC_RULES.md",
    "## Stacked tested-Candidate integration ownership — b113 2026-09-06",
    """
    ## Stacked tested-Candidate integration ownership — b113 2026-09-06

    - When an already-tested stacked task is integrated into its owning dependency branch, keep the original Candidate/Build ownership. For the current integration, Build113 / `DEV-message-rendering-0.1.0-b113` remains a `DEV-message-rendering` identity even though `dev/send-stream-20260829` now carries those product bits.
    - Do not allocate or rename a new `DEV-send-stream` Candidate solely to represent an ownership-preserving merge. The last Send-owned Candidate remains b112 until new Send/Stream product evidence justifies a fresh unique Candidate.
    - Existing Runtime evidence may be inherited across the merge only when source comparison proves the tested product paths are unchanged. CI on an integration commit is not a substitute for Human Runtime evidence.
    - This rule does not change Send/SSE/Repository ownership: one protected Send remains one Send, `ConversationRepository` remains Native response/content authority, and the inherited b107 accepted clean-EOF gate stays separate until exercised.
    """,
)

insert_after_once(
    "docs/project/BUILD_TEST_INDEX.md",
    "# Build / Test / Release Index",
    "## Stacked integration record — b113 into DEV-send-stream 2026-09-06",
    """
    ## Stacked integration record — b113 into DEV-send-stream 2026-09-06

    - `DEV-message-rendering-0.1.0-b113` remains permanently owned by `DEV-message-rendering`; its canonical package identity remains product `7d1ddc8eaa164c9b307f525b00bb0e1404f395e9`, package `75ccad15208610c2b0420033846f9bb15bbdb494`, Artifact `9976713893`, IPA `sha256:2cf62b87117f9279816de68f2ed3ce83768d203198b555fe4fe0042f8d367c3f`, Human Runtime Positive for the tested presentation scope.
    - PR #36 merged into `dev/send-stream-20260829` at `4a22086f7ccab39427c46a163854e8f68530c65f`. Compare from canonical b113 package source to this merge head contains no product/Xcode path changes, so this is an integration of the same tested product bits, not a new Candidate or Artifact identity.
    - PR #29 post-merge CI run `33993974639` passed on merge head. Treat it as integration CI only; it does not replace the canonical b113 Artifact or create new Runtime evidence.
    - b112 remains the last `DEV-send-stream`-owned canonical Candidate. No b114 is allocated by this integration. Overall Send/Stream remains Runtime Partial because the b107 accepted clean-EOF recovery is still Unexercised.
    """,
)
