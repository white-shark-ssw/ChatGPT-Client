from pathlib import Path

DOCS = Path("docs/project")
CHECKPOINT = DOCS / "current/dev/DEV-send-stream-round7-runtime-addendum.md"
BUILD_INDEX = DOCS / "BUILD_TEST_INDEX.md"
PROJECT_STATE = DOCS / "PROJECT_STATE.md"
MODULE_STATUS = DOCS / "MODULE_STATUS.md"
PROJECT_PROFILE = DOCS / "PROJECT_PROFILE.md"
PROJECT_RULES = DOCS / "PROJECT_SPECIFIC_RULES.md"
TECH_DECISIONS = DOCS / "TECHNICAL_DECISIONS.md"
PREFLIGHT = DOCS / "SEND_STREAM_PREFLIGHT.md"


def prepend(path: Path, marker: str, section: str) -> None:
    text = path.read_text()
    if marker in text:
        raise SystemExit(f"marker already present in {path}: {marker}")
    path.write_text(section.rstrip() + "\n\n" + text)


checkpoint_section = '''## b114 Human Runtime result / b115 allocation — 2026-09-06

Latest explicit user Runtime outranks the earlier b114 test plan:

- Canonical b114 remains `DEV-send-stream-0.1.0-b114` / product `673f2905ddc7a5aba23317e81e75677b2e81edb3` / package `ef98a038a165bdcef90b0abea67c25b7ef96e57f` / Artifact `9978074978` / IPA `sha256:f2c793f8eeff3f83d30fa9fec69ee7953ff7f3e431c07a49b7b9b20931a6b192`.
- User Runtime reports the tested b114 run is otherwise acceptable, but the sent user message is visibly duplicated and active reasoning/generation disables Sync/Reload contrary to the product rule established from the start.
- Diagnostics classify the duplicate as **presentation duplication, not duplicate Send**: the tested run has one client live generation, one covered protected-Send request/submit/`sendObserved`, and one HTTP200 SSE. During the active run authoritative Detail advances past the live snapshot baseline and materializes the user turn while the same live snapshot still renders its local optimistic user row.
- b114 active-at-bottom follow-tail instrumentation is exercised (`scrollAnchor.followTailPreserved`) and the user reports no other problem in this test. Preserve that owner change.
- b114's active-response Sync/Reload disable is rejected. The older Hard Reload invariant plus the user's latest explicit requirement are authoritative: response activity alone must never disable manual Sync or Reload. Sync remains one authoritative Detail reconciliation and never resends. Reload remains a local hard reset/reload action and never claims server Stop.
- Exact b107 post-acceptance `stream_ended_without_done` did not occur in this run and remains Unexercised.

b115 is now permanently reserved before product writes:

- Candidate / Build: `DEV-send-stream-0.1.0-b115` / `0.1.0 (115)`.
- Intended exact product scope: `ChatGPTClient.xcodeproj/project.pbxproj` + `ChatGPTClient/Conversation/ConversationFeature.swift` only.
- Duplicate-user correction uses the existing `ConversationLiveResponseSnapshot.baselineVisibleMessageCount`: once the installed authoritative message suffix beyond that baseline contains the user turn, stop rendering only the live optimistic user row. Keep the same live generation/timeline/final owner; do not text-match, mutate authoritative messages or create another store.
- Active-response menu correction: Sync remains available when response activity is the only blocker; existing detail-operation exclusion may still prevent overlapping Sync. Reload remains available whenever a conversation is selected, including during an active response and an in-flight Detail operation, matching the existing hard-reset replacement semantics.
- `RootViewController.swift`, protected Send/SSE grammar, b107 recovery, Repository response authority, b112 role isolation, b113 rich rendering and server Stop remain unchanged.
- No retry, resend, regenerate, timer/watchdog, polling, guessed resume/status, second response store or fake Stop is authorized.

Batch recovery point:

- Known baseline before Batch A: `dev/send-stream-20260829@b26ed7bdcbd05680ca12130daad253c263c2b3a1`; PR #29 open against `main@94f0c5777dad262cd1fb22be49082dbd92c962f2`; b115 absent.
- Batch A: record this b114 Runtime result, correct durable Sync/Reload rules and reserve b115 in checkpoint/index/state/module/profile/rules/decisions/preflight; commit before any b115 product write.
- Batch B: apply exactly Build/Candidate + `ConversationFeature.swift` presentation/menu correction, run `git diff --check` and Debug Simulator compile, commit/push one exact product source.
- Batch C: bind formal package workflow only after the exact b115 product commit is known; require same-source Push + PR CI, canonical Artifact and independent package identity/hash verification; then record package evidence and hand one IPA to Human Runtime.
- Recovery must not replay b114, modify PR #35, alter `RootViewController.swift`, or touch protected Send/SSE/recovery/Stop transport.

**Evidence ladder now:** b114 Code/CI/Artifact/package verified; b114 Human Runtime Partial/Negative for the combined closeout scope; b115 allocated only / product pending / Runtime pending / Stable-Frozen No.

**Next exact action:** execute Batch B after this allocation commit succeeds. Do not allocate b116 before b115 Human Runtime unless a new independent blocker makes b115 untestable.'''
prepend(CHECKPOINT, "## b114 Human Runtime result / b115 allocation — 2026-09-06", checkpoint_section)

project_rules_section = '''## Active-response Sync/Reload and optimistic-user authority — b115 override 2026-09-06

- Latest explicit user requirement supersedes b114's active-response disable wording: an active local or external response by itself must **not** disable `同步最新消息` or `重载当前会话`.
- Manual Sync remains exactly one authoritative Conversation Detail reconciliation and never resends/regenerates the prompt. Existing same-target Detail-operation ownership may reject/serialize overlapping Detail work; response activity itself is not a Sync blocker.
- Manual Reload remains enabled whenever a current conversation is selected, including while a response or another Detail operation is active. It keeps the existing hard-reset semantics: release/invalidate current covered observation/executor, clear current Native live projection, replace the current Detail operation and load one authoritative Detail. It never claims that the remote server generation was stopped.
- For a client-owned live response, `baselineVisibleMessageCount` is the authority boundary for the optimistic user row. If installed authoritative messages beyond that baseline already contain the user turn, suppress only the local live-user presentation row. Keep the live assistant/reasoning/final projection on the same Repository generation until normal terminal/authoritative reconciliation clears it.
- Never text-match prompts for deduplication, delete authoritative messages, resend, retry, poll, add a timer/watchdog, synthesize Stop, or introduce another response/message store to solve this presentation overlap.'''
prepend(PROJECT_RULES, "## Active-response Sync/Reload and optimistic-user authority — b115 override 2026-09-06", project_rules_section)

tech_section = '''## DEV-send-stream b114 Runtime correction / b115 ownership decision — 2026-09-06

- b114 Runtime proves the visible duplicate user bubble is not a duplicate protected Send. Preserve the one-Send transport owner and correct the projection boundary instead: once current authoritative messages advance beyond the client live snapshot baseline and the new authoritative suffix includes the user turn, the temporary live optimistic user row has fulfilled its purpose and must no longer be presented.
- Do not deduplicate by prompt text. `baselineVisibleMessageCount` plus the already-installed authoritative message sequence is the existing identity/ownership evidence and requires no new state dictionary.
- Reject b114's active-response control disable. Response activity alone never disables manual Sync or Reload. Sync remains an authoritative read/reconcile action; Reload remains the pre-existing local hard reset + replacement Detail action and is not server Stop.
- Preserve b114 follow-tail behavior, b112 role-isolated cell reuse, b113 rich presentation, TD-029 one protected Send, b107 same-generation accepted-client recovery and `ConversationRepository` response/content authority.
- b115 may change only Xcode Build/Candidate plus `ConversationFeature.swift` for these two Runtime-selected corrections. No `RootViewController.swift`, retry, resend, timer/watchdog, polling, Stop synthesis or second store change is authorized.'''
prepend(TECH_DECISIONS, "## DEV-send-stream b114 Runtime correction / b115 ownership decision — 2026-09-06", tech_section)

state_section = '''## DEV-send-stream b114 Runtime Partial/Negative -> b115 allocated — 2026-09-06

- b114 protected Send count remains correct in the supplied Runtime: one live generation / one protected Send submit / one `sendObserved` / one HTTP200 SSE. The visible duplicated user bubble is a Native authoritative+optimistic presentation overlap.
- b114 follow-tail behavior is retained; user reports the rest of this test has no problem.
- b114 active Sync/Reload disable is rejected by explicit product requirement. Active response alone must not disable either manual action.
- `DEV-send-stream-0.1.0-b115` / Build115 is permanently reserved for the minimum presentation/menu correction. Product/CI/Artifact/Runtime pending; Stable-Frozen No.'''
prepend(PROJECT_STATE, "## DEV-send-stream b114 Runtime Partial/Negative -> b115 allocated — 2026-09-06", state_section)

module_section = '''## DEV-send-stream b115 Runtime-regression correction allocated — 2026-09-06

- Module remains Active / Runtime Partial overall / Stable-Frozen No.
- b114 Runtime: one protected Send preserved; follow-tail accepted on the tested path; duplicate user presentation and active Sync/Reload disabling rejected.
- b115 Build115 is reserved for authoritative-vs-optimistic user-row ownership plus restoration of active-response Sync/Reload availability. Exact clean EOF remains separately Unexercised.'''
prepend(MODULE_STATUS, "## DEV-send-stream b115 Runtime-regression correction allocated — 2026-09-06", module_section)

profile_section = '''## Current DEV-send-stream candidate override — b115 allocated 2026-09-06

- Current next Human Runtime candidate identity is reserved as `DEV-send-stream-0.1.0-b115` / `0.1.0 (115)`; product/package source pending guarded staging.
- Trigger is b114 Human Runtime: one protected Send remains correct, but Native duplicates the user row after authoritative Detail materializes it and b114 incorrectly disables Sync/Reload during active reasoning/generation.
- b115 exact product scope is Xcode Build/Candidate + `ConversationFeature.swift`; no Root/Send/SSE/recovery/Stop transport change. Stable-Frozen No.'''
prepend(PROJECT_PROFILE, "## Current DEV-send-stream candidate override — b115 allocated 2026-09-06", profile_section)

index_text = BUILD_INDEX.read_text()
if "`DEV-send-stream-0.1.0-b115`" in index_text:
    raise SystemExit("b115 already present in BUILD_TEST_INDEX")
lines = index_text.splitlines()
b114_index = next((i for i, line in enumerate(lines) if line.startswith("| `DEV-send-stream-0.1.0-b114` |")), None)
if b114_index is None:
    raise SystemExit("b114 row missing")
lines[b114_index] = "| `DEV-send-stream-0.1.0-b114` | `DEV-send-stream` | `0.1.0 (114)` | Phase 9 closeout product `673f2905ddc7a5aba23317e81e75677b2e81edb3`; package `ef98a038a165bdcef90b0abea67c25b7ef96e57f`; PR #29 | staging `33995851115/101386150523`; Push `33995968361/101386467170`; PR `33995970064/101386471305`; Artifact `9978074978`; ZIP `f36fb5ebe3dc8db6b41ab891e66d337fa9ebcd17b6936440490f113f0c412aa9`; IPA `f2c793f8eeff3f83d30fa9fec69ee7953ff7f3e431c07a49b7b9b20931a6b192`; package independently verified | Human Runtime Partial/Negative for combined closeout: tested protected transport remained exactly one live generation / one protected Send submit / one `sendObserved` / one HTTP200 SSE; active-at-bottom follow-tail instrumentation was exercised and user reports no other problem. Visible user message duplicated because authoritative Detail materialized the new user turn beyond the live baseline while the same live snapshot still rendered its optimistic user row. Active reasoning/generation also disabled Sync/Reload, explicitly rejected by the user as contrary to the established product rule. Exact b107 `stream_ended_without_done` did not occur and remains Unexercised | **Runtime Partial/Negative for b114 combined scope / superseded for correction priority by b115 / Stable-Frozen No; permanently reserved** |"
b115_row = "| `DEV-send-stream-0.1.0-b115` | `DEV-send-stream` | `0.1.0 (115)` | allocated from b114 Runtime evidence; exact product scope: Xcode Build/Candidate + `ConversationFeature.swift`; product/package source pending | Guarded staging/Simulator/CI/Artifact pending | Human Runtime pending: one local protected Send must render one user turn even after active manual Sync/authoritative Detail materializes it; Sync and Reload must remain available during active reasoning/generation; Reload may locally hard-reset/reacquire but must not claim server Stop; preserve b114 follow-tail and b113 presentation. Exact clean EOF qualifies only if naturally observed | **Allocated Runtime-regression correction candidate / product pending / Stable-Frozen No; permanently reserved** |"
lines.insert(b114_index, b115_row)
BUILD_INDEX.write_text("\n".join(lines) + ("\n" if index_text.endswith("\n") else ""))

preflight_text = PREFLIGHT.read_text()
old_preflight = '''## Sync / Reload while response active

Existing contract remains: Sync one conversation and never sends; Reload one conversation and never sends/regenerates; navigation invokes neither.

Do not prechoose automatic Stop-before-Sync/Reload, duplicate stream recovery or timer-deferred retry.

For the first safe production Candidate, if the exact active-response reconciliation semantics are not yet proven, it is acceptable to disable an unsafe Sync/Reload action while that conversation owns an active response, provided this is explicit UI behavior and not a hidden retry/fallback.
'''
new_preflight = '''## Sync / Reload while response active

Existing contract remains: Sync one conversation and never sends; Reload one conversation and never sends/regenerates; navigation invokes neither.

Latest explicit product requirement is authoritative: response activity alone must not disable either manual control. Manual Sync may issue one authoritative Conversation Detail reconciliation while a local/external response is active; it never resends the prompt. Existing same-target Detail-operation ownership may still prevent overlapping Sync work.

Manual Reload remains available whenever a current conversation is selected, including while a response or another Detail operation is active. It is a Native hard reset: release/invalidate the current covered executor/observation, clear the current live projection, replace the target Detail operation and load one authoritative Detail. This local action never claims the server response was stopped.

When active Sync/Detail materializes the client-owned user turn before the live response terminal, the authoritative message suffix beyond the live snapshot baseline owns that user presentation. Suppress only the redundant optimistic live-user row; keep the same Repository response generation for reasoning/final until normal reconciliation.

Do not prechoose automatic Stop-before-Sync/Reload, duplicate stream recovery, text-based prompt dedupe, resend, polling or timer-deferred retry.
'''
if preflight_text.count(old_preflight) != 1:
    raise SystemExit(f"expected exact preflight block once, found {preflight_text.count(old_preflight)}")
PREFLIGHT.write_text(preflight_text.replace(old_preflight, new_preflight))

for path in [CHECKPOINT, BUILD_INDEX, PROJECT_STATE, MODULE_STATUS, PROJECT_PROFILE, PROJECT_RULES, TECH_DECISIONS, PREFLIGHT]:
    if not path.read_text().strip():
        raise SystemExit(f"unexpected empty document: {path}")
