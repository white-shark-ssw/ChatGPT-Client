from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

PRODUCT = "12fc1d1f5020d76d1892c25a0ced94323d5a0142"
PACKAGE = "5e43c398b52a62de9f9a6e6546de7312ba5eb1df"
STAGE_RUN = "33881577700/101051252468"
PUSH = "33881896437/101052287658"
PR = "33881905960/101052320038"
ARTIFACT = "9940228423"
ARTIFACT_SHA = "af05e9d0a522fb53c3e453bedcf9b49e44781158d7f7d8798ad1426b4c57b388"
IPA_SHA = "49f8d9a8ef425409923bf904a3134265ddfa6d90597d72e04a1e976a5a8a90c7"


def prepend_after_title(path: str, marker: str, section: str) -> None:
    p = ROOT / path
    text = p.read_text()
    if marker in text:
        return
    i = text.find("\n")
    if i < 0:
        raise SystemExit(f"missing title newline: {path}")
    p.write_text(text[: i + 1] + "\n" + section.rstrip() + "\n\n" + text[i + 1 :].lstrip("\n"))


# Build/Test Index: add b97 and rewrite the b96 row to its final Runtime result.
p = ROOT / "docs/project/BUILD_TEST_INDEX.md"
text = p.read_text()
if "DEV-send-stream-0.1.0-b97" not in text:
    divider = "|---|---|---|---|---|---|---|\n"
    pos = text.find(divider)
    if pos < 0:
        raise SystemExit("candidate table divider not found")
    pos += len(divider)
    row = (
        f"| `DEV-send-stream-0.1.0-b97` | `DEV-send-stream` | `0.1.0 (97)` | foreground authoritative Detail reconcile product `{PRODUCT}`; exact package source `{PACKAGE}`; PR #29 | "
        f"guarded staging `{STAGE_RUN}` exact four-product-file scope + Simulator passed; Push `{PUSH}` passed; PR `{PR}` passed; canonical Artifact `{ARTIFACT}`; Artifact ZIP `sha256:{ARTIFACT_SHA}`; IPA `sha256:{IPA_SHA}`; independent package inspection: Candidate b97 / source `5e43c398b52a` / iOS14 / `[1,2]` / iphoneos / arm64 | "
        "Human Runtime pending: while an external response is active, background/suspend the app until the other platform finishes, return to foreground without manual Sync/Reload, and verify one automatic authoritative Detail reconcile materializes the final assistant and clears the stale external live projection | "
        "**Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity verified / Runtime pending / Stable-Frozen No; permanently reserved** |\n"
    )
    text = text[:pos] + row + text[pos:]

lines = text.splitlines(True)
for i, line in enumerate(lines):
    if line.startswith("| `DEV-send-stream-0.1.0-b96` |"):
        parts = line.rstrip("\n").split("|")
        if len(parts) < 9:
            raise SystemExit("unexpected b96 row shape")
        # Preserve identity/validation columns, replace Runtime + Status only.
        parts[6] = " **Runtime Negative for automatic continuation/background-return convergence:** real authoritative Detail repeatedly returned `conversationAsyncStatus=missing`; app backgrounded while covered Web still reported `IS_STREAMING`; foreground only rebootstraped Web and emitted no automatic Detail request; manual `同步最新消息` later changed authoritative visible messages `46->47` and existing `liveResponse.externalDetailReconciled(reason=authoritative_assistant_materialized)` materialized the final assistant "
        parts[7] = " **b96 async-status/timer hypothesis rejected as sufficient; manual one-shot authoritative Detail recovery Runtime Positive; superseded by b97 foreground reconcile; Stable-Frozen No; permanently reserved** "
        lines[i] = "|".join(parts) + "\n"
        break
else:
    raise SystemExit("b96 row not found")
p.write_text("".join(lines))

prepend_after_title(
    "docs/project/PROJECT_STATE.md",
    "## 2026-09-04 — b97 foreground authoritative Detail reconcile package ready",
    f"""## 2026-09-04 — b97 foreground authoritative Detail reconcile package ready

- b96 Human Runtime disproved its ordinary-Detail async-status trigger as sufficient: target Detail returned `conversation_async_status` missing both before and after completion. Background return performed covered-Web rebootstrap but no automatic Native Detail; a later manual one-shot `syncLatestMessages` changed visible messages `46->47` and immediately reconciled the final assistant.
- `DEV-send-stream-0.1.0-b97` / `0.1.0 (97)` is now permanently reserved. Exact product `{PRODUCT}`; package source `{PACKAGE}`; PR #29 remains open/unmerged.
- b97 removes the b96 10-second Native `DispatchWorkItem` continuation scheduler. When the selected conversation already owns an active external live response and the app enters foreground, Root requests exactly one existing Repository `syncLatestMessages` if no Detail operation is in flight, while preserving the existing covered-Web foreground rebootstrap. If authoritative Detail already contains the final assistant, existing Repository reconciliation clears the external live projection and Root releases the idle executor.
- Guarded staging `{STAGE_RUN}` passed exact four-product-file scope + Simulator. Push `{PUSH}` and PR `{PR}` passed. Canonical Artifact `{ARTIFACT}`; Artifact ZIP `sha256:{ARTIFACT_SHA}`; IPA `sha256:{IPA_SHA}`; package identity independently verified as b97/source `5e43c398b52a`/iOS14/arm64.
- Human Runtime is Pending. This does not claim execution while iOS keeps the app suspended in background; the gate is automatic authoritative convergence when the app returns to foreground. Stable/Frozen No.""",
)

prepend_after_title(
    "docs/project/PROJECT_PROFILE.md",
    "## Latest DEV-send-stream candidate override — b97 2026-09-04",
    f"""## Latest DEV-send-stream candidate override — b97 2026-09-04

- Latest test candidate: `DEV-send-stream-0.1.0-b97` / `0.1.0 (97)`; exact product `{PRODUCT}`; package source `{PACKAGE}`; canonical Artifact `{ARTIFACT}`; IPA `sha256:{IPA_SHA}`; Human Runtime pending; Stable/Frozen No.
- b97 supersedes b96's rejected async-status/timer continuation experiment with one lifecycle-triggered authoritative Conversation Detail reconcile on foreground return for an already-active external response. Protected Send remains TD-029 covered official-Web owned.""",
)

prepend_after_title(
    "docs/project/MODULE_STATUS.md",
    "## DEV-send-stream b97 foreground reconcile package-ready override — 2026-09-04",
    f"""## DEV-send-stream b97 foreground reconcile package-ready override — 2026-09-04

- `ConversationRepository` remains sole Native conversation/content/response-lifecycle authority. b97 removes the b96 recurring Native Detail scheduler; the only new lifecycle action is one existing `syncLatestMessages` request when returning foreground with a selected active external live response and no Detail operation already in flight.
- Covered Web retains its foreground rebootstrap role if the one-shot authoritative Detail does not yet contain the final assistant. Existing Repository terminal reconciliation owns final projection removal; no second response store or Send path was added.
- Exact product `{PRODUCT}`; package source `{PACKAGE}`; guarded staging/Simulator + Push+PR CI passed; Artifact `{ARTIFACT}`; IPA `sha256:{IPA_SHA}`; Human Runtime Pending; Stable/Frozen No.
- True background execution/notification remains separate future scope; b97 only targets foreground-return convergence.""",
)

prepend_after_title(
    "docs/project/TECHNICAL_DECISIONS.md",
    "## DEV-send-stream b97 foreground authoritative reconcile decision — 2026-09-04",
    """## DEV-send-stream b97 foreground authoritative reconcile decision — 2026-09-04

- Human Runtime supersedes the b96 Native polling decision for ordinary Conversation Detail: the tested target returned no top-level `conversation_async_status`, so the b96 10-second scheduler never became active and must not remain as a speculative product mechanism.
- The evidenced recovery primitive is the already-existing authoritative `ConversationRepository.syncLatestMessages`: after background interruption, one manual call materialized the completed assistant immediately. Therefore b97 authorizes exactly one automatic call on foreground entry when the selected conversation already has an active external live response and no Detail operation is in flight.
- Existing covered-Web foreground rebootstrap remains independent and may continue live transport if the one-shot Detail is not terminal. Existing Repository Detail reconciliation remains the sole owner of terminal materialization/clearing.
- This decision does not authorize background heartbeat, recurring foreground polling, retry/watchdog/fallback, guessed `/resume`, duplicate Send, WebSocket-body authority, challenge replay, or a second response store. It does not claim iOS can execute the request while the app is suspended.""",
)

prepend_after_title(
    "docs/project/PROJECT_SPECIFIC_RULES.md",
    "## Foreground external-response authoritative reconcile — b97 2026-09-04",
    """## Foreground external-response authoritative reconcile — b97 2026-09-04

- This section **supersedes** the earlier b96 `Native cross-platform Detail continuation exception` below. Do not use the b96 10-second `DispatchWorkItem`/async-status-driven Native polling path; Human Runtime showed ordinary authoritative Detail may omit `conversation_async_status` entirely.
- When `UIApplication.willEnterForegroundNotification` fires and the currently selected conversation already has an active external live response (`phase.isActive` with empty Native prompt), Root may issue exactly one existing `ConversationRepository.syncLatestMessages` request if no Detail operation is already in flight.
- This is lifecycle-triggered authoritative reconciliation, not polling. There is no recurring schedule, retry, fallback or background keepalive. Covered-Web foreground rebootstrap may still run for the same external response if authoritative Detail has not materialized terminal state.
- If the one-shot Detail contains a newly materialized final assistant, existing Repository reconciliation must remain the sole owner that removes the external live projection; Root may then release the idle covered executor. TD-029 protected Send ownership is unchanged.
- Do not describe b97 as true background completion. iOS suspension behavior remains authoritative; b97 validates convergence after return to foreground.""",
)

prepend_after_title(
    "docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md",
    "## b97 foreground authoritative Detail reconcile — package-ready 2026-09-04",
    f"""## b97 foreground authoritative Detail reconcile — package-ready 2026-09-04

Exact identity:

- product code `{PRODUCT}` — only `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/Conversation/ConversationFeature.swift`, `ChatGPTClient/Conversation/NativeConversationContinuation.swift`, and `ChatGPTClient/RootViewController.swift` changed in the guarded product commit;
- Candidate `DEV-send-stream-0.1.0-b97` / `0.1.0 (97)`, permanently reserved;
- package source `{PACKAGE}`;
- staging `{STAGE_RUN}` success including exact scope, `git diff --check`, and Debug iphonesimulator compile;
- Push `{PUSH}` success; PR `{PR}` success;
- canonical Push Artifact `{ARTIFACT}` / ZIP `sha256:{ARTIFACT_SHA}`;
- IPA `ChatGPTClient-0.1.0-b97-dev-send-stream.ipa` / `sha256:{IPA_SHA}`;
- independent unpacking: bundle `com.whitesharkssw.chatgptclient`, version/build `0.1.0 (97)`, Candidate b97, source `5e43c398b52a`, iOS14+, UIDeviceFamily `[1,2]`, Mach-O arm64.

Product delta:

1. b96 10-second `DispatchWorkItem` Native continuation scheduling and account-reset cancellation hook are removed; authoritative Detail status remains diagnostic-only and existing Detail-to-live reconciliation is retained.
2. On foreground entry, a selected active external live response triggers exactly one existing authoritative `repository.syncLatestMessages(id:)` when no Detail operation is already running.
3. Existing covered-Web foreground page rebootstrap remains available in parallel for nonterminal live continuation.
4. If that one-shot Detail contains the final assistant, existing Repository `authoritative_assistant_materialized` reconciliation clears the stale external projection; Root then refreshes selected Detail presentation and releases an idle covered executor.
5. No background heartbeat, recurring polling, retry/watchdog/fallback, resend/regenerate, guessed `/resume`, challenge replay, or second response authority.

Pre-allocation PR workflow failures on heads before Build97 and the bot-pushed product-head `action_required` run are invalid/non-evidence because no formal b97 package job executed there. Canonical Runtime identity is only Artifact `{ARTIFACT}` / IPA `sha256:{IPA_SHA}`.

Evidence ladder: **b96 Runtime Negative for async-status automatic continuation/background-return convergence; manual authoritative Detail recovery Positive / b97 Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen Send No.**

**Next exact action:** install only canonical b97 IPA; start a long external response, enter it while active, background/suspend ChatGPTClient until the other platform finishes, return to foreground without manual Sync/Reload, and export diagnostics after observing whether `foregroundExternalDetailReconcile.requested` performs one authoritative Detail request and automatically materializes the final assistant. Do not allocate b98 before this Runtime gate.""",
)

print("b97 durable package-ready evidence staged")