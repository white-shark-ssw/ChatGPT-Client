from pathlib import Path

CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
BUILD_INDEX = Path("docs/project/BUILD_TEST_INDEX.md")
PROJECT_STATE = Path("docs/project/PROJECT_STATE.md")
MODULE_STATUS = Path("docs/project/MODULE_STATUS.md")
PROJECT_PROFILE = Path("docs/project/PROJECT_PROFILE.md")

DIAGNOSTICS_SHA = "59f70c74feb099024ce9be7e9d1650df21f98bd9d02f6bc05051877d16b45bf5"


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
                "| `DEV-send-stream-0.1.0-b115` | `DEV-send-stream` | `0.1.0 (115)` | Runtime-regression correction product `2346c2d4ab26d40ef720b7850ae34316acb3cc62`; package `2dc0a4155f3549f32b1b08a9e4d8e6fb87495692`; PR #29 | corrected staging `34042595946/101511928494` passed durable b114 Runtime recording/b115 allocation, exact two-product-path scope, `git diff --check`, exact behavior guards and Debug Simulator; Push `34042793058/101512446124` passed; PR `34042795253/101512452040` passed; canonical Artifact `9992196070`; ZIP `19df7bac1354735cab404d81433b5818380da3e28b73dadaf29cb12f351fbd31`; IPA `073b202ba26e400e7da0777fffa362f55f864be78a394a19258bfd027744dd41`; package independently verified `com.whitesharkssw.chatgptclient` / Build115 / Candidate b115 / source `2dc0a4155f35` / Release / iOS14+ / `[1,2]` / arm64 | Human Runtime Partial on diagnostics `sha256:59f70c74feb099024ce9be7e9d1650df21f98bd9d02f6bc05051877d16b45bf5`: exact b115 identity; one protected Send request / one `sendObserved` / one HTTP200 SSE; live optimistic user transitions from `liveUserPresentationCount=1` to `0` once authoritative Detail materializes the user, with no second Send; active manual Reload executes and performs the existing local hard-reset/reacquire path. User reports a new non-blocking UI defect: an already-open top-right menu is auto-dismissed while reasoning messages stream. Current source calls `updateConversationMenu()` after every live presentation and replaces the entire bar-button/menu object each time, a source-supported likely owner. User explicitly requests deferring this fix to a later version together with other justified work, not a standalone Candidate. Active manual Sync was not separately proven by this diagnostics sample; exact clean EOF remains Unexercised | **Human Runtime Partial for b115 correction / menu-persistence defect deferred without b116 allocation / Stable-Frozen No; permanently reserved** |"
            )
            BUILD_INDEX.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))
            return
    raise SystemExit("b115 row not found")


update_b115_row()

checkpoint = f"""## b115 Human Runtime partial + deferred open-menu dismissal — 2026-09-07

Latest user Runtime / diagnostics:

- User reports that while reasoning messages are actively streaming, an already-expanded top-right conversation menu can automatically close. The user explicitly requests that this be fixed together with a later justified version and **not** receive a standalone Candidate/build.
- Supplied diagnostics SHA-256 `{DIAGNOSTICS_SHA}` contain 1752 events and identify exact canonical `0.1.0 (115)` / `DEV-send-stream-0.1.0-b115` / source `2dc0a4155f35` / Release / iPhone / iOS17.0.
- The tested protected user action still has exactly one `coveredExecutor.requested`, one `coveredExecutor.sendObserved` and one HTTP200 SSE response; there is no second protected Send.
- b115 optimistic-user ownership is exercised: live presentation begins with `liveUserPresentationCount=1`; after authoritative Detail materializes the user turn, it transitions to `liveUserPresentationCount=0` while the live assistant/reasoning presentation continues. This is Runtime-positive telemetry for the b115 ownership correction; no screenshot was supplied in this sample, so do not overstate independent visual proof beyond the user's report and telemetry.
- Active manual Reload is exercised during reasoning: `manualReload.hardReset` releases the local executor/live projection, `conversation.detailReload.requested` executes, authoritative Detail returns HTTP200, and external observation/reasoning is reacquired without another protected Send. This remains a local reset/reacquire action, not server Stop.
- This sample contains no `stream_ended_without_done` / accepted clean-EOF recovery event. The inherited b107 branch remains Unexercised.
- Active manual Sync is not separately proven by this sample: the observed `latestSync` operations are foreground/authoritative reconciliation paths, not sufficient evidence that the user successfully invoked the menu Sync action while the response was active.

Deferred menu issue source boundary:

- `applyLiveResponse` / live presentation completion calls `updateConversationMenu()` on every reasoning/final presentation refresh.
- `updateConversationMenu()` constructs fresh `UIAction` objects, a fresh `UIMenu`, and a fresh `UIBarButtonItem`, then replaces `navigationItem.rightBarButtonItem` every time.
- Replacing the menu host on every SSE-driven presentation update is a source-supported likely owner for the observed dismissal. Runtime does not instrument UIKit's actual menu-dismiss callback, so record this as **likely/source-supported**, not as a fully instrumented causal proof.
- Deferred correction intent for a later justified product version: keep the menu host stable across ordinary live-response presentation refreshes and only change action/menu state when materially necessary. Do not add timers, debouncing, retries, duplicate state stores or a standalone build solely for this issue.

**Evidence ladder now:** b115 Code/Simulator/Push CI/PR CI/Artifact/package verified; Human Runtime Partial with optimistic-user ownership and active Reload exercised; open-menu persistence Runtime Negative/deferred; active manual Sync still not separately proven; accepted clean EOF Unexercised; Stable-Frozen No.

**Next exact action:** do not allocate b116 for the menu dismissal alone. Keep this defect queued for the next independently justified product Candidate, where it should be included in that Candidate's exact scope and Human Runtime matrix. Until then, no product change is authorized solely by this defect.
"""
prepend_once(CHECKPOINT, "## b115 Human Runtime partial + deferred open-menu dismissal", checkpoint)

state = f"""## DEV-send-stream b115 Human Runtime partial / deferred menu persistence — 2026-09-07

- Exact canonical b115 diagnostics `sha256:{DIAGNOSTICS_SHA}` exercise one protected Send only, authoritative/live optimistic-user handoff (`liveUserPresentationCount` 1 -> 0) and active manual Reload hard-reset/reacquire without a second Send.
- New user-observed UI defect: an already-expanded top-right menu may close as reasoning SSE presentation updates arrive. Source repeatedly rebuilds/replaces the bar-button/menu from `updateConversationMenu()` after every live presentation refresh, which is the current likely owner.
- User explicitly defers this menu-persistence fix to a later independently justified version; no b116 allocation or standalone product build is authorized by this issue alone. Active manual Sync and exact accepted clean EOF remain separately unproven.
"""
prepend_once(PROJECT_STATE, "## DEV-send-stream b115 Human Runtime partial / deferred menu persistence", state)

module = f"""## DEV-send-stream b115 Runtime follow-up — menu persistence deferred 2026-09-07

- Diagnostics `sha256:{DIAGNOSTICS_SHA}` are exact Release Build115 / Candidate b115 / source `2dc0a4155f35` on iPhone iOS17.0.
- b115 optimistic-user presentation ownership and active Reload are exercised; protected Send remains single-submit. Human Runtime remains Partial because active manual Sync is not separately proven and the user found a new menu-persistence UI defect.
- Menu dismissal is queued for a later justified Candidate, not a standalone version. Current source-supported likely owner is per-live-update replacement of the top-right `UIBarButtonItem`/`UIMenu` in `updateConversationMenu()`.
"""
prepend_once(MODULE_STATUS, "## DEV-send-stream b115 Runtime follow-up — menu persistence deferred", module)

profile = f"""## Current DEV-send-stream Runtime note — b115 2026-09-07

- Canonical b115 remains the current tested package identity. Diagnostics `sha256:{DIAGNOSTICS_SHA}` confirm Build115 / Candidate b115 / source `2dc0a4155f35` / Release iPhone iOS17.0.
- Human Runtime is Partial: optimistic-user ownership and active Reload are exercised; open-menu persistence has a user-observed deferred defect; active manual Sync and accepted clean EOF are not yet separately proven. Stable/Frozen No.
"""
prepend_once(PROJECT_PROFILE, "## Current DEV-send-stream Runtime note — b115 2026-09-07", profile)
