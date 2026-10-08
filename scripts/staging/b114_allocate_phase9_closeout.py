from pathlib import Path

BUILD_INDEX = Path("docs/project/BUILD_TEST_INDEX.md")
CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
PROJECT_STATE = Path("docs/project/PROJECT_STATE.md")
MODULE_STATUS = Path("docs/project/MODULE_STATUS.md")
PROJECT_PROFILE = Path("docs/project/PROJECT_PROFILE.md")
TECHNICAL_DECISIONS = Path("docs/project/TECHNICAL_DECISIONS.md")
PROJECT_RULES = Path("docs/project/PROJECT_SPECIFIC_RULES.md")

BASE_HEAD = "cce8a7b5d9208e45e9f83cd169ed91f68acca3ad"
B113_PACKAGE = "75ccad15208610c2b0420033846f9bb15bbdb494"
B113_ARTIFACT = "9976713893"


def prepend_once(path: Path, marker: str, section: str) -> None:
    text = path.read_text()
    if marker in text:
        return
    path.write_text(section.rstrip() + "\n\n" + text)


def update_build_index() -> None:
    text = BUILD_INDEX.read_text()
    if "DEV-send-stream-0.1.0-b114" in text:
        return
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| `DEV-message-rendering-0.1.0-b113`"):
            row = (
                "| `DEV-send-stream-0.1.0-b114` | `DEV-send-stream` | `0.1.0 (114)` | Phase 9 closeout candidate allocated from current integrated b113 baseline; product source pending; PR #29 | intended exact product scope: Xcode Build/Candidate + `ConversationFeature.swift`. Preserve b112 role-isolated reuse, b113 rich presentation and all Send/SSE/Repository/recovery transport behavior. Fix only active-at-bottom hidden follow-tail via the existing semantic-anchor owner, block manual Reload while any response is active, and retire b109-b111 assistant color/render diagnostics whose Runtime purpose is complete | Human Runtime pending: long local A response left at bottom -> B -> A must return to current tail; user-scrolled-up A -> B -> A must restore history anchor; local-active Sync/Reload must remain unavailable; after terminal Reload returns; ordinary one-Send terminal/reconcile, b113 rendering, Copy and no-blue regression must remain intact. Exact b107 clean EOF qualifies only if `stream_ended_without_done` naturally occurs | **Allocated evidence-backed Phase 9 closeout candidate / product staging pending / Human Runtime pending / Stable-Frozen No; permanently reserved** |"
            )
            lines.insert(index, row)
            BUILD_INDEX.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))
            return
    raise SystemExit("b113 row not found")


update_build_index()

checkpoint_section = f"""## Phase 9 closeout audit / b114 allocation — 2026-09-06

Current owner / identity guard:

- Selected Work remains `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 remains open against unchanged `main@94f0c5777dad262cd1fb22be49082dbd92c962f2`. Audit baseline before tooling is `{BASE_HEAD}`.
- Current integrated product is exact Build113 / Candidate `DEV-message-rendering-0.1.0-b113`, imported from Runtime-positive PR #36. Candidate b113 remains owned by `DEV-message-rendering`; b112 remains the last Send-owned canonical Candidate before this allocation. Canonical b113 package `{B113_PACKAGE}` / Artifact `{B113_ARTIFACT}` remains the tested product baseline.
- Parallel PR #35 remains research-only and owns no product `ChatGPTClient/**`, product Xcode Candidate, or Build114 identity. `BUILD_TEST_INDEX.md` contains no b114 before this allocation.

Phase 9 audit — later evidence closes old historical gates:

- Existing-conversation protected Send is already Runtime accepted from b67: one Native Send -> one page-owned protected Send -> HTTP200 SSE -> Repository reasoning/tool/final -> terminal/reconcile. b72 Runtime accepts the tested simultaneous A-generating + B-send ownership matrix.
- New Chat identity/handoff and ordinary terminal convergence are Runtime Positive again in b107/b108: one protected Send, first protected-SSE conversation ID adopted once, no fake server ID, normal terminal then authoritative Detail reconcile.
- b112 is Human Runtime Positive for role-isolated assistant color. Imported b113 is Human Runtime Positive for the tested native Markdown/link/table/file-reference/Copy presentation scope and preserves b112 reuse isolation.
- b97/b100/b101 evidence already covers foreground authoritative convergence and dormant remote discovery for their tested paths. Exact b101 `-1005` renewal and natural b98 external WebContent-death branches remain conditional evidence debts only; do not manufacture failures or block ordinary Phase 9 closeout solely to force those rare branches.

Current-source gaps selected for one coherent b114 closeout candidate:

1. **Hidden active follow-tail intent is structurally incomplete.** `captureScrollAnchor(for:)` currently always persists a normal historical anchor when an authoritative row is visible. Root switches Repository selection before Detail captures the old displayed conversation, so an active A left at physical bottom is saved as history; hidden growth then returns to that stale anchor. Reuse the existing semantic owner instead of adding state: while the displayed conversation has an active Repository live response and is at the already-used exact physical-bottom threshold, remove/do not save its anchor. Existing `restoreScrollAnchor` already interprets no anchor as `scrollToLatestMessage`, while a user who scrolls upward still gets the ordinary message/chunk-relative anchor.
2. **Manual Reload is unsafe while a response is active.** Sync is already disabled/guarded for client-owned active responses, but Reload is currently enabled for every selected conversation. Root's current manual-reload callback releases the executor and removes the live snapshot. Because exact server Stop is not yet authorized, b114 must disable Reload for any active response and defensively reject a direct reload invocation while active. External-active manual Sync remains allowed because later Runtime uses it as authoritative recovery; local-active Sync remains blocked.
3. **b109-b111 color probes have fulfilled their purpose.** b112/b113 Human Runtime closed the cross-role color defect, yet current long assistant chunks still execute `assistantChunkColor.willDisplay` plus main-thread drawHierarchy/CALayer/direct-attributed pixel aggregation. Retire only that diagnostic plumbing. Preserve separate user/assistant reuse identifiers, visible rendering, b113 rich-text projection and ordinary Diagnostics.

b114 allocation / exact negative scope:

- Allocate and permanently reserve `DEV-send-stream-0.1.0-b114` / `0.1.0 (114)` before product writes.
- Product scope is exactly `ChatGPTClient.xcodeproj/project.pbxproj` + `ChatGPTClient/Conversation/ConversationFeature.swift`. `RootViewController.swift`, covered Web bridge/SSE grammar, b107 clean-EOF recovery, Repository response ownership, b112 reuse pools, b113 rich rendering, Copy content authority and auth/network owners remain unchanged.
- No retry, fallback, timer/watchdog, polling, duplicate Send, regenerate, guessed Native resume/status, second response store, fake Stop or new follow-tail state dictionary is authorized.

Still evidence-gated after b114:

- b107 exact post-acceptance `stream_ended_without_done` same-generation/no-resend recovery remains Unexercised unless the exact event occurs. b114 does not change it.
- Server Stop is still not implemented. Static inspection of the exact supplied/decrypted official iOS app independently exposes `StopConversationRequest`, `/stop_conversation`, `stopConversation(id:requestTrackingData:)` and `Failed to stop conversation`, which narrows the official owner/path but does not prove HTTP method, request body/target token, acknowledgement or terminal semantics. Do not synthesize a Stop request from strings alone; obtain current Runtime request/ack evidence before product implementation.

Batch recovery point:

- Batch A: this script records the audit and reserves b114 in checkpoint/index/state/module/profile/decisions/rules. No product write occurs before that commit.
- Batch B: apply only the exact two-product-path b114 delta, pass `git diff --check` + Debug Simulator compile, commit/push one exact product source.
- Batch C: bind formal package workflow to the exact b114 product source, require same-source Push + PR CI, canonical Artifact and independent IPA identity/hash verification, then record package truth and hand one IPA to Human Runtime.
- Never replay completed b113 integration, reassign b113 Candidate ownership, modify PR #35, or alter the b107 recovery/Stop transport from this closeout patch.

**Next exact action:** after Batch A is durably committed, execute Batch B only; then package one canonical b114 for the combined follow-tail / active-Reload-safety / diagnostics-retirement Human Runtime gate.
"""
prepend_once(CHECKPOINT, "## Phase 9 closeout audit / b114 allocation", checkpoint_section)

state_section = """## DEV-send-stream Phase 9 closeout audit / b114 — 2026-09-06

- Later Runtime evidence closes the old local-Send, tested A/B simultaneous ownership, New Chat handoff, assistant-color and native-presentation gates. The integrated b113 product remains the b114 baseline.
- Current source still has two product-level closeout gaps: active A left at physical bottom is saved as an ordinary historical anchor before B selection, and manual Reload can release executor/live state while a response is active despite server Stop remaining unproven.
- b114 is reserved for the minimum owner fixes plus retirement of the b109-b111 expensive color-render diagnostics after b112/b113 Runtime acceptance. No Send/SSE/Repository/Stop transport change is included.
- Exact accepted clean-EOF recovery remains Unexercised; server Stop method/body/ack remains Runtime-unverified. Overall task stays Active / Runtime Partial / Stable-Frozen No until the remaining closeout gates are classified.
"""
prepend_once(PROJECT_STATE, "## DEV-send-stream Phase 9 closeout audit / b114", state_section)

module_section = """## DEV-send-stream b114 closeout candidate — 2026-09-06

- Preserve `ConversationRepository` as sole Native response/content owner, b112 role-isolated message-cell reuse and b113 native rich presentation.
- b114 closes only source-proven presentation/action safety gaps: active-at-bottom hidden follow-tail via existing semantic anchor absence, active-response Reload disable/guard, and removal of fulfilled b109-b111 per-chunk pixel diagnostics.
- Server Stop and exact accepted clean-EOF Runtime qualification remain evidence-gated; b114 adds no transport behavior for either.
- Module remains Active / Runtime Partial / Stable-Frozen No pending b114 Human Runtime and final evidence settlement.
"""
prepend_once(MODULE_STATUS, "## DEV-send-stream b114 closeout candidate", module_section)

profile_section = """## Current DEV-send-stream closeout candidate — b114 2026-09-06

- `DEV-send-stream-0.1.0-b114` / `0.1.0 (114)` is permanently reserved before product staging.
- Baseline is the integrated, Runtime-positive b113 product. Intended exact scope is Xcode identity + `ConversationFeature.swift` only: hidden active follow-tail intent, active-response Reload safety, and retirement of fulfilled color-render probes.
- No b114 package/Artifact exists until guarded staging and formal CI complete. Stable/Frozen No.
"""
prepend_once(PROJECT_PROFILE, "## Current DEV-send-stream closeout candidate — b114", profile_section)

decision_section = """## DEV-send-stream Phase 9 follow-tail / active Reload closeout decision — b114 2026-09-06

- Do not add a second follow-tail state store. The existing semantic scroll-anchor owner already represents historical intent; absence of an anchor already means return to latest. Therefore an active displayed conversation left at the existing physical-bottom threshold must not persist a historical anchor, while any deliberate upward position continues to persist message ID + chunk + relative offset.
- Until server Stop is proven, manual Reload must not discard an active response/executor. Disable Reload whenever the selected conversation owns any active live response and enforce the same rule inside the reload handler. Keep the existing client-owned active Sync block; keep external-active manual Sync available because Runtime uses authoritative Sync for recovery/reconciliation.
- Retire b109-b111 assistant chunk color/render instrumentation after b112/b113 Runtime acceptance. Do not remove the b112 role-specific reuse pools or b113 presentation code with the probes.
- This decision changes no protected Send count, SSE parser, accepted-client clean-EOF recovery, response authority, polling/retry policy or server Stop transport.
"""
prepend_once(TECHNICAL_DECISIONS, "## DEV-send-stream Phase 9 follow-tail / active Reload closeout decision — b114", decision_section)

rules_section = """## Phase 9 active-response navigation/reload closeout — b114 test candidate 2026-09-06

- While a conversation has an active Repository live response, leaving it at the current physical bottom preserves follow-tail by keeping no historical anchor; returning uses the existing latest-message path. Deliberate upward reading continues to save/restore the existing semantic message/chunk anchor. No parallel follow-tail dictionary or global streaming flag is allowed.
- Manual Reload is unavailable while any response is active because current Reload releases covered execution and clears live state, while server Stop is not yet proven. Local client-owned active Sync remains blocked; external-active manual Sync remains permitted as the already-evidenced authoritative recovery action.
- Completed color diagnostics are test instrumentation, not a permanent rendering dependency. Once b112/b113 Runtime is accepted, remove the b109-b111 per-chunk rendered-pixel probes without weakening the separate user/assistant reuse-pool invariant.
- Static official-app strings identifying `/stop_conversation` are not sufficient authorization to issue that request. Stop still requires current method/body/target/ack/terminal Runtime evidence.
"""
prepend_once(PROJECT_RULES, "## Phase 9 active-response navigation/reload closeout — b114 test candidate", rules_section)
