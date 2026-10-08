from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "ChatGPTClient.xcodeproj/project.pbxproj"
ROOT_VC = ROOT / "ChatGPTClient/RootViewController.swift"
INDEX = ROOT / "docs/project/BUILD_TEST_INDEX.md"
CHECKPOINT = ROOT / "docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md"


def replace_exact(text: str, old: str, new: str, count: int = 1) -> str:
    actual = text.count(old)
    if actual != count:
        raise SystemExit(f"anchor mismatch: expected {count}, found {actual}: {old[:180]!r}")
    return text.replace(old, new, count)


def checkpoint() -> None:
    index = INDEX.read_text()
    lines = index.splitlines()
    found = False
    for i, line in enumerate(lines):
        if line.startswith("| `DEV-send-stream-0.1.0-b97`"):
            if "Human Runtime pending:" not in line or "Runtime pending" not in line:
                raise SystemExit("b97 index row is not in expected Runtime-pending state")
            line = line.replace("Human Runtime pending: while an external response is active, background/suspend the app until the other platform finishes, return to foreground without manual Sync/Reload, and verify one automatic authoritative Detail reconcile materializes the final assistant and clears the stale external live projection", "Human Runtime not executed by user; b97 package remains valid and permanently reserved, but its foreground Detail-only gate was intentionally skipped in favor of b98 hard WebContent-termination recovery")
            line = line.replace("Runtime pending", "Runtime not executed / superseded by b98 test priority", 1)
            lines[i] = line
            found = True
            break
    if not found:
        raise SystemExit("b97 candidate row not found")
    INDEX.write_text("\n".join(lines) + "\n")

    current = CHECKPOINT.read_text()
    section = '''## b98 hard WebContent termination recovery — checkpoint 2026-09-04

User explicitly chose not to run the b97 Human Runtime gate and asked to advance directly to b98. b97 remains a valid, permanently reserved package identity, but its Human Runtime result is **Not Executed**, not Positive or Negative.

Exact baseline before b98 product writes:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable.
- branch head before this checkpoint staging: `beba08deb0f0803f74417bd6026dd11ec8f4fa38`; base `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- parallel PR #35 / `DEV-official-sync-reload` remains draft research-only, head `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`, with no product `ChatGPTClient/**` ownership or candidate-number conflict.
- b97 canonical product/package/Artifact remain `12fc1d1f5020d76d1892c25a0ced94323d5a0142` / `5e43c398b52a62de9f9a6e6546de7312ba5eb1df` / `9940228423`; never reuse or overwrite.
- `DEV-send-stream-0.1.0-b98` / Build98 is not yet allocated at this checkpoint and is the next unique candidate.

Evidence-backed defect and recovery boundary:

1. Current `CoveredWebSendExecutor.webViewWebContentProcessDidTerminate` is an explicit hard WebContent-death signal, but it currently calls `failCurrent("web_process_terminated")`; `failCurrent` clears `observingExternalResponse`/active events and Root then treats `.failed` as response failure and releases the executor.
2. For an **external/cross-platform observation only**, WebContent death is a transport interruption, not evidence that the server-side response failed. Existing Repository external live state must remain authoritative.
3. b94 Runtime already observed real covered-Web WebContent termination. b95 Runtime separately proved full-page existing-conversation rebootstrap can restart page-owned continuation. b96 Runtime proved one authoritative Detail request can materialize an already-finished final assistant; b97 preserves that foreground Detail reconcile.
4. For a **client-owned protected Send**, WebContent termination remains a failure. b98 must never automatically resend/replay a Send.

Intended minimal b98 product delta:

- allocate Build98 / Candidate `DEV-send-stream-0.1.0-b98`;
- only when `observingExternalResponse == true`, intercept `webViewWebContentProcessDidTerminate` before `failCurrent`;
- preserve external observation callbacks, current conversation identity and Repository live response;
- if the app is active, immediately issue exactly one existing full-page external-observation rebootstrap for that hard termination event;
- if the app is background/inactive, do not start background network work; defer to the existing foreground path, which already performs b97 authoritative Detail reconcile plus one external page rebootstrap;
- leave ordinary navigation failure semantics unchanged in b98; do not infer a disconnect from silence, elapsed time, focus state or missing snapshots;
- no timer/watchdog, retry loop, duplicate Send, resend/regenerate, guessed `/resume`, challenge replay, second response store or Native background heartbeat.

**Next exact action:** allocate `DEV-send-stream-0.1.0-b98`, apply only the two-file product delta above, run exact-scope checks + Debug Simulator compile, then bind formal b98 Push/PR package CI to the exact product head. Human Runtime should force/observe a real WebContent process termination while a cross-platform response is active and verify the same external live response survives and resumes, without a second Send.

'''
    if "## b98 hard WebContent termination recovery — checkpoint 2026-09-04" in current:
        raise SystemExit("b98 checkpoint already present")
    CHECKPOINT.write_text(current.replace("# DEV-send-stream round 7 Runtime addendum\n\n", "# DEV-send-stream round 7 Runtime addendum\n\n" + section, 1))
    print("b98 checkpoint staged")


def product() -> None:
    project = PROJECT.read_text()
    project = replace_exact(project, "CURRENT_PROJECT_VERSION = 97;", "CURRENT_PROJECT_VERSION = 98;", 2)
    project = replace_exact(project, 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b97";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b98";', 2)
    PROJECT.write_text(project)

    root = ROOT_VC.read_text()
    old = '''    func webViewWebContentProcessDidTerminate(_ webView: WKWebView) {
        manualSyncFocusProbePending = false
        diagnostics.error(category: "webSend", name: "coveredExecutor.webProcess", fields: ["state": "terminated"])
        failCurrent("web_process_terminated")
    }
'''
    new = '''    func webViewWebContentProcessDidTerminate(_ webView: WKWebView) {
        manualSyncFocusProbePending = false
        diagnostics.error(category: "webSend", name: "coveredExecutor.webProcess", fields: ["state": "terminated", "mode": observingExternalResponse ? "external_observation" : "client_send_or_idle"])
        if observingExternalResponse {
            composerReadyConversationID = nil
            if UIApplication.shared.applicationState == .active {
                diagnostics.warning(category: "webSend", name: "coveredExecutor.externalWebProcessRecovery", fields: ["state": "immediate_rebootstrap"])
                rebootstrapExternalObservationPageOnForeground()
            } else {
                diagnostics.warning(category: "webSend", name: "coveredExecutor.externalWebProcessRecovery", fields: ["state": "deferred_to_foreground"])
            }
            return
        }
        failCurrent("web_process_terminated")
    }
'''
    root = replace_exact(root, old, new)
    ROOT_VC.write_text(root)
    print("b98 hard WebContent termination recovery applied")


if len(sys.argv) != 2 or sys.argv[1] not in {"checkpoint", "product"}:
    raise SystemExit("usage: b98_web_process_recovery.py checkpoint|product")
checkpoint() if sys.argv[1] == "checkpoint" else product()
