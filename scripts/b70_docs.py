from pathlib import Path

ROOT = Path.cwd()


def read(path):
    return (ROOT / path).read_text()


def write(path, text):
    (ROOT / path).write_text(text)


def replace_once(path, old, new):
    text = read(path)
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected one anchor, found {count}: {old[:100]!r}")
    write(path, text.replace(old, new, 1))


def replace_between(path, start, end, new):
    text = read(path)
    if text.count(start) != 1 or text.count(end) != 1:
        raise SystemExit(f"{path}: range anchor mismatch")
    i = text.index(start)
    j = text.index(end, i)
    write(path, text[:i] + new + text[j:])


def insert_after_line_prefix(path, prefix, new_line):
    text = read(path)
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(matches) != 1:
        raise SystemExit(f"{path}: expected one line prefix {prefix!r}, found {len(matches)}")
    if new_line.rstrip("\n") in text:
        raise SystemExit(f"{path}: b70 line already present")
    idx = matches[0] + 1
    lines.insert(idx, new_line if new_line.endswith("\n") else new_line + "\n")
    write(path, "".join(lines))


checkpoint = "docs/project/current/dev/DEV-send-stream.md"
write(checkpoint, r'''# DEV-send-stream

## Status

**Active — exact b70 product/config source is assembled, audited, Push+PR CI passed, Artifact/package identity independently verified, and real-device Runtime is now the only acceptance gate. b67 remains the accepted existing-conversation protected-Send transport predecessor. b69 Runtime defects justify b70 but are not themselves proof that b70 is fixed. Stable/Frozen Send remains No; PR #29 stays open/unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged at the b70 product gate
- Actual `main` at product promotion guard: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Clean b70 checkpoint parent: `5c379b3d994b28cb0ba5a3c793e4efa193a003a1`
- Exact b70 product/config source: `fb83be9163838f78abfa47903e67f27b6f66ec52`
- Candidate: `DEV-send-stream-0.1.0-b70`
- Version / Build: `0.1.0 (70)`
- b39-b70 permanently reserved; do not reuse b70 even if Runtime fails
- Stable/Frozen Send: No

## Why b70 exists

Exact b69 iPhone/iOS17 Runtime retained the b67 production transport success and validated the ordered response-timeline direction, but was Partial/Rejected for current daily-chat parity because the same test cycle exposed six concrete defects:

1. covered Web programmatic composer injection could raise the iOS keyboard after Native validation UI dismissed;
2. the current user prompt did not appear in live Native rows until terminal authoritative Sync;
3. expanded reasoning/tool presentation had excessive spacing and no reasoning/final divider;
4. production b69 dropped b65 Runtime-accepted GitHub nested `工具输入` / `工具输出` disclosures;
5. tool rows lacked bounded leading icons;
6. Native list/detail auth could become sticky after a transient 403 even while browser authentication later proved valid for the same account.

b67 remains the accepted existing-conversation protected-Send predecessor: one local Send -> one protected `/backend-api/f/conversation` -> HTTP200 `text/event-stream` -> Repository reasoning/tool/final updates -> terminal -> one authoritative reconcile.

## Exact b70 implementation boundary

Only the minimum source-backed corrections were made:

- `CoveredWebSendExecutor` keeps the verified composer selector/submit/protected-Send/SSE mechanism but suppresses the covered Web virtual keyboard during programmatic focus and blurs after injection;
- `ConversationRepository.beginLiveResponse` receives the actual trimmed prompt and stores it only in the response-local live snapshot so one optimistic user row appears immediately before the live assistant row; authoritative Detail replaces it at successful reconcile;
- b65 GitHub exact-parent detail authorization is restored inside the ordered b69 timeline: invocation `metadata.connector_tool_payload` + exact-parent GitHub result `message.content`, nested `工具输入` / `工具输出` collapsed independently, readable hierarchical output, and no raw tool body diagnostics;
- timeline items carry only response-local detail strings plus a bounded local tool icon kind; spacing and the reasoning/final separator stay inside the existing deterministic/manual message geometry;
- exact session/accounts HTTP403 is a temporary probe failure rather than persistent account absence by itself; last verified account identity is preserved while no fresh transient transport is returned from the failed probe;
- exact 401 retains unavailable/not-authenticated semantics;
- list/detail 401/403 invalidates the currently copied transient transport once and the current operation still fails visibly; the next explicit/normal read probes fresh WebKit credentials. No automatic replay/retry/poll/timer/watchdog was added;
- returning from a user-opened login flow may issue one explicit list refresh. This is a new navigation operation, not hidden retry.

State owners remain unchanged: `ConversationRepository` is the sole production conversation/response authority; `AuthSessionStore` is sole account authority; `WKWebsiteDataStore.default()` is sole persistent auth-secret authority; covered Web is challenge/protected-Send execution only.

## Exact source/scope evidence

Tooling-only assembly rebuilt b70 from clean checkpoint `5c379b3d...` with exact anchors.

- Assembly Run / Job: `33373254877 / 99428895016` — success.
- `git diff --check` passed.
- Authorized-scope audit passed and changed exactly five product/config files:
  - `.github/workflows/ios-foundation.yml`
  - `ChatGPTClient.xcodeproj/project.pbxproj`
  - `ChatGPTClient/Authentication/AuthSessionStore.swift`
  - `ChatGPTClient/Conversation/ConversationFeature.swift`
  - `ChatGPTClient/RootViewController.swift`
- Scope stat: `394 insertions / 93 deletions`; no tooling file is part of exact product commit.
- Xcode 16.4 iOS Simulator compile passed in assembly CI.
- Clean product commit `fb83be9163838f78abfa47903e67f27b6f66ec52` is exactly one commit ahead of `5c379b3d...`, direct parent `5c379b3d...`, tree `fff3ed3861ce9bad7dc848ba12a1f8b086d353de`.
- Xcode identity is `CURRENT_PROJECT_VERSION = 70`, `MARKETING_VERSION = 0.1.0`, `DIAGNOSTICS_CANDIDATE = DEV-send-stream-0.1.0-b70` in Debug and Release.

## Formal CI / Artifact evidence

Exact product head `fb83be9163838f78abfa47903e67f27b6f66ec52` was fast-forwarded to the formal Work branch without force.

- Push Run / Job: `33377045570 / 99440767755` — success.
- PR Run / Job: `33377049590 / 99440781050` — success.
- Push Artifact: `9752289536` (`ChatGPTClient-DEV-send-stream-0.1.0-b70`).
- Artifact ZIP digest: `sha256:bdf09b246ff259ee80d46acfad675713c1a0b51aee3b44f7ea9f0a7e67eafde0`.
- IPA: `ChatGPTClient-0.1.0-b70-dev-send-stream.ipa`.
- IPA SHA: `8084e2ace5926b7ee6a790f3eeb2445a2c4ce1fee67d8953300aca93a446a44a`.
- Build log source marker: `fb83be916383`.
- Independently downloaded/unpacked Push Artifact agrees with GitHub digest and sidecar SHA.
- Built `Info.plist` independently verified: Release `0.1.0`, Build `70`, Candidate `DEV-send-stream-0.1.0-b70`, `DiagnosticsSourceCommit=fb83be916383`, minimum iOS `14.0`, arm64/iPhone+iPad family.

Artifact production and package verification do **not** prove the b69 Runtime defects are fixed.

## Evidence ladder

- Code written: Yes — exact product source `fb83be9163838f78abfa47903e67f27b6f66ec52`.
- Static / source-scope / `git diff --check`: Passed.
- Assembly iOS Simulator compile: Passed.
- Push CI: Passed.
- PR CI: Passed.
- Artifact produced: Yes — `9752289536`.
- Package identity independently verified: Yes.
- Runtime/manual/real-device: **Pending b70 gate**.
- Stable/Frozen: **No**.

## Conflict / recovery guard

Before formal promotion, PR #29 remained open/mergeable/unmerged at head `5c379b3d...`, `main` remained `d323b9ee...`, and no foreign formal-branch commit intervened. The formal ref was advanced only by a non-force fast-forward to exact b70 product source.

Earlier tooling/recovery placeholder commits are not part of the formal lineage and must never be replayed. Tooling assembly/product-base refs are evidence utilities only and never Candidate authority.

## Exact b70 real-device gate

Install exact Artifact `9752289536` / IPA SHA `8084e2ac...a44a` on the primary iPhone/iOS17 device, verify Build70/Candidate/source marker, clear diagnostics, then exercise normal daily-chat behavior. Required evidence:

1. covered Web never leaves a visible iOS keyboard after the Native Send/validation transition;
2. one local Send immediately inserts exactly one optimistic user row before the live assistant row; terminal reconcile must not duplicate it;
3. reasoning/tools remain chronological (`reasoning -> tool -> reasoning -> tool -> final`) and tool completion updates the existing row in place;
4. expanded GitHub tool rows again expose independently collapsed `工具输入` / `工具输出` with readable hierarchy and bounded leading icons;
5. expanded reasoning/tool spacing is compact and a deterministic divider separates reasoning/tool content from a real final answer;
6. navigating away/back during an active response preserves the Repository-owned live response without introducing a second owner or floating overlay;
7. if Native list/detail hits transient 403 while Web auth remains valid, the current operation may fail visibly, stale transient transport is discarded, and the next explicit/normal read can recover from current WebKit credentials without automatic replay/retry;
8. hidden `assistant:thoughts` / `inline_cot_expandable_content` never appears;
9. accepted b38 long-message geometry/quick navigation and accepted b67 one-Send transport do not regress;
10. export diagnostics after the tested terminal/recovery sequence.

If any item fails, keep b70 reserved, record the exact defect/evidence, and allocate a new candidate only from that evidence. Do not patch speculatively.

## Next exact action

Hand exact b70 Artifact `9752289536` to the user for the real-device gate above. Keep PR #29 open/unmerged. Do not allocate b71 and do not begin unrelated Composer/attachment/Stop/background work before exact b70 Runtime evidence is recorded.
''')

index = "docs/project/BUILD_TEST_INDEX.md"
insert_after_line_prefix(
    index,
    "| `DEV-send-stream-0.1.0-b69` |",
    "| `DEV-send-stream-0.1.0-b70` | `DEV-send-stream` | `0.1.0 (70)` | exact source `fb83be9163838f78abfa47903e67f27b6f66ec52`; PR #29 | Assembly `33373254877/99428895016`; Push `33377045570/99440767755`; PR `33377049590/99440781050`; Artifact `9752289536`; ZIP `sha256:bdf09b246ff259ee80d46acfad675713c1a0b51aee3b44f7ea9f0a7e67eafde0`; IPA `8084e2ace5926b7ee6a790f3eeb2445a2c4ce1fee67d8953300aca93a446a44a`; Release/source `fb83be916383`/iOS14/`[1,2]`/arm64 | Daily-chat parity correction: suppress covered-Web keyboard, response-local optimistic user row, restored exact-parent GitHub nested details + bounded icons + compact spacing/divider, and stale transient 401/403 invalidation with 403 account-identity preservation/no automatic retry. | **Code/scope/static+sim compile/Push+PR CI/Artifact/package verified; Runtime pending; permanently reserved** |",
)

state = "docs/project/PROJECT_STATE.md"
replace_once(
    state,
    "_Last updated: 2026-08-31 through accepted b67 production transport Runtime, b68 superseded presentation Artifact, and exact b69 Code/CI/Artifact/package verification. Phase 9 `DEV-send-stream` remains Active at the b69 human Runtime gate. Stable/Frozen Send remains No._",
    "_Last updated: 2026-08-31 through accepted b67 production transport Runtime, b69 Runtime defect evidence, and exact b70 Code/scope/Push+PR CI/Artifact/package verification. Phase 9 `DEV-send-stream` remains Active at the b70 human Runtime gate. Stable/Frozen Send remains No._",
)
replace_between(
    state,
    "Latest exact product Candidate is **`DEV-send-stream-0.1.0-b69` / `0.1.0 (69)`**:\n",
    "## b65 accepted probe predecessor\n",
    r'''Latest exact product Candidate is **`DEV-send-stream-0.1.0-b70` / `0.1.0 (70)`**:

- exact product/config source `fb83be9163838f78abfa47903e67f27b6f66ec52`, direct parent `5c379b3d994b28cb0ba5a3c793e4efa193a003a1`;
- assembly `33373254877 / 99428895016` — exact five-file scope audit, `git diff --check` and Xcode 16.4 iOS Simulator compile passed;
- Push `33377045570 / 99440767755` and PR `33377049590 / 99440781050` — success;
- Artifact `9752289536`; ZIP `sha256:bdf09b246ff259ee80d46acfad675713c1a0b51aee3b44f7ea9f0a7e67eafde0`;
- IPA `sha256:8084e2ace5926b7ee6a790f3eeb2445a2c4ce1fee67d8953300aca93a446a44a`;
- independently unpacked package `0.1.0 (70)` / Candidate b70 / source `fb83be916383` / minimum iOS14 / arm64.

b70 retains b67 protected-Send/SSE ownership and b69 ordered timeline, while correcting the concrete b69 daily-chat defects: covered-Web keyboard focus, missing immediate user row, GitHub detail/icon/spacing/divider presentation, and stale Native transient-auth 401/403 lifecycle. No automatic retry/replay/poll/timer/watchdog or second state owner was added. Evidence ladder: **Code / exact scope / static+sim compile / Push+PR CI / Artifact / package verified / Runtime pending / Stable-Frozen No.** b39-b70 are permanently reserved.

''',
)
replace_once(
    state,
    "- `AuthSessionStore` remains sole auth/account authority; `WKWebsiteDataStore.default()` remains sole persistent auth-secret authority.",
    "- `AuthSessionStore` remains sole auth/account authority; `WKWebsiteDataStore.default()` remains sole persistent auth-secret authority. b70 treats exact probe HTTP403 as temporary failure that preserves the last verified identity, while list/detail 401/403 discards stale copied transient transport and never auto-replays the failed operation.",
)
replace_once(
    state,
    "Current source now contains the first Repository-owned existing-conversation production bridge and Web Rule Lab. Exact b67 Runtime is the immediate gate.",
    "Current source contains the Repository-owned existing-conversation production bridge and Web Rule Lab. b67 transport Runtime is accepted; exact b70 daily-chat parity/auth-lifecycle Runtime is the immediate gate.",
)
replace_between(
    state,
    "## Current exact Runtime gate\n",
    "## Remaining Unknown / Unverified\n",
    r'''## Current exact Runtime gate

Install exact b70 Artifact `9752289536` / IPA SHA `8084e2ac...a44a` on the primary iPhone/iOS17 device. Verify Candidate/source marker, clear diagnostics, then confirm: no covered-Web keyboard pop; exactly one immediate optimistic user row without terminal duplication; chronological reasoning/tools with in-place completion; restored GitHub nested input/output + bounded icons + compact spacing/divider; active response survives navigation; transient Native 403 can recover on the next explicit/normal read from current WebKit credentials without automatic replay/retry; hidden thoughts remain excluded; b38 geometry and b67 one-Send transport do not regress. Export diagnostics after terminal/recovery.

''',
)
replace_once(
    state,
    "Exact b69 ordered-timeline Runtime, new-chat authoritative identity timing, exact server Stop mechanism, cross-conversation simultaneous server generation, connector-detail schemas beyond the evidenced GitHub mapping, Native first/exclusive resume, 5/15-minute background behavior, WebContent termination recovery, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.",
    "Exact b70 daily-chat parity/auth-lifecycle Runtime, new-chat authoritative identity timing, exact server Stop mechanism, cross-conversation simultaneous server generation, connector-detail schemas beyond the evidenced GitHub mapping, Native first/exclusive resume, 5/15-minute background behavior, WebContent termination recovery, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.",
)

module = "docs/project/MODULE_STATUS.md"
replacements = {
    "| Build/runtime metadata | **b69 exact identity; Runtime pending** | Xcode settings / built `Info.plist` | `0.1.0 (69)`, source `5e9c21834830...`, Artifact `9748400171`; b39-b69 reserved. |": "| Build/runtime metadata | **b70 exact identity; Runtime pending** | Xcode settings / built `Info.plist` | `0.1.0 (70)`, source `fb83be916383...`, Artifact `9752289536`; b39-b70 reserved. |",
    "| IPA build / CI packaging | **Stable capability; b69 Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33366226539/99407331552`, PR `33366229125/99407340011`, Artifact `9748400171`, IPA `0c06256d...3b0aa`; package b69/source `5e9c21834830`/iOS14/arm64. |": "| IPA build / CI packaging | **Stable capability; b70 Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33377045570/99440767755`, PR `33377049590/99440781050`, Artifact `9752289536`, IPA `8084e2ac...a44a`; package b70/source `fb83be916383`/iOS14/arm64. |",
    "| Authentication/account context | Stable | `AuthSessionStore.swift` | Sole native auth/account owner. |": "| Authentication/account context | **Stable owner; b70 transient-403 behavior Runtime pending** | `AuthSessionStore.swift` | Sole native auth/account owner. Exact probe 403 preserves last verified identity while returning no fresh transport; 401 remains unavailable semantics. |",
    "| Covered official-Web protected Send executor | **Production transport Runtime accepted b67; unchanged by b69** | `CoveredWebSendExecutor` + TD-029 + `WEB_SEND_ADAPTER.md` | b67 passed one protected Send -> HTTP200 SSE -> terminal/reconcile. b69 changes ordered Repository presentation only. |": "| Covered official-Web protected Send executor | **Production transport Runtime accepted b67; b70 keyboard-only correction Runtime pending** | `CoveredWebSendExecutor` + TD-029 + `WEB_SEND_ADAPTER.md` | b67 passed one protected Send -> HTTP200 SSE -> terminal/reconcile. b70 retains route/selectors/SSE grammar and only suppresses covered programmatic keyboard focus. |",
    "| Native conversation read/recovery | **Stable merged baseline + production response owner implementation present** | `ConversationRepository` | Sole production conversation/list/detail/recovery/response lifecycle authority. b66/b67 add Repository-owned live response snapshot/generation; exact successful Runtime pending. |": "| Native conversation read/recovery | **Stable merged baseline + b70 response/read lifecycle candidate** | `ConversationRepository` | Sole production conversation/list/detail/recovery/response lifecycle authority. b70 invalidates stale copied transient transport on list/detail 401/403 without automatic replay; Runtime pending. |",
    "| Streaming / Send | **Active — b67 transport accepted; b69 ordered presentation Runtime gate** | `DEV-send-stream`; PR #29; TD-029 | b69 is Code/CI/Artifact/package verified for chronological reasoning/tool interleaving; Runtime pending. |": "| Streaming / Send | **Active — b67 transport accepted; b70 daily-chat Runtime gate** | `DEV-send-stream`; PR #29; TD-029 | b70 exact source/Push+PR CI/Artifact/package verified; keyboard/user-row/tool-detail/auth-lifecycle corrections remain Runtime pending. |",
    "| User-visible reasoning | **Production stream passed b67; ordered b69 presentation Runtime pending** | `ConversationRepository` + `DEV-send-stream` | Ordered reasoning segments interleave with tools; exact `reasoning_ended` remains final authority; hidden thoughts prohibited. |": "| User-visible reasoning | **Production stream passed b67; ordered b70 presentation Runtime pending** | `ConversationRepository` + `DEV-send-stream` | b69 ordered segments retained; b70 tightens spacing/divider/detail presentation only; exact `reasoning_ended` remains final authority; hidden thoughts prohibited. |",
    "| Tool activity presentation | **b69 Code/CI/Artifact verified; Runtime pending** | `DEV-send-stream` | Tool appends at event position, completion updates in place by slot, later reasoning forms a segment below it. |": "| Tool activity presentation | **b70 Code/CI/Artifact/package verified; Runtime pending** | `DEV-send-stream` | Tool event order/in-place completion retained; b70 restores authorized nested details, adds bounded local icons and compact deterministic spacing/divider. |",
    "| Expandable GitHub tool detail | **Focused b65 Runtime passed** | `DEV-send-stream` | Nested input/output disclosures + decoded hierarchy accepted for evidenced GitHub exact-parent shape; no cross-connector generalization. |": "| Expandable GitHub tool detail | **b65 Runtime mapping accepted; b70 production restoration Runtime pending** | `DEV-send-stream` | b70 restores nested input/output disclosures + decoded hierarchy only for the evidenced exact-parent GitHub shape; no cross-connector generalization. |",
    "- b69 source `5e9c2183483094304f7eaeecf4ffc7ad8e65b902`, Artifact `9748400171`, IPA `0c06256d...3b0aa` is the current ordered-timeline Runtime candidate.": "- b70 source `fb83be9163838f78abfa47903e67f27b6f66ec52`, Artifact `9752289536`, IPA `8084e2ac...a44a` is the current daily-chat parity/auth-lifecycle Runtime candidate; package identity independently verified.",
    "- `ConversationRepository` remains sole response authority; `WEB_SEND_ADAPTER.md` is unchanged because b69 consumes already-emitted event order.": "- `ConversationRepository` remains sole response authority; `AuthSessionStore` remains sole account authority; `WEB_SEND_ADAPTER.md` route/SSE contract is unchanged by b70.",
    "- b39-b69 are reserved. Phase 9 Stable/Frozen: No.": "- b39-b70 are reserved. Phase 9 Stable/Frozen: No.",
}
for old, new in replacements.items():
    replace_once(module, old, new)

profile = "docs/project/PROJECT_PROFILE.md"
replace_once(
    profile,
    "**Initialized — 2026-08-25; refreshed 2026-08-31 through accepted b67 production transport Runtime, b68 superseded presentation Artifact, and exact b69 Code/CI/Artifact/package verification.**",
    "**Initialized — 2026-08-25; refreshed 2026-08-31 through accepted b67 production transport Runtime, b69 daily-chat defect evidence, and exact b70 Code/scope/Push+PR CI/Artifact/package verification.**",
)
replace_once(
    profile,
    "- Production native conversation/list/read/recovery/**response lifecycle** authority: one `ConversationRepository` in `Conversation/ConversationFeature.swift`; current b69 ordered response runtime extension is still Repository-owned even though integration code presently lives with the first production bridge.",
    "- Production native conversation/list/read/recovery/**response lifecycle** authority: one `ConversationRepository` in `Conversation/ConversationFeature.swift`; b70 optimistic user/live assistant state, ordered reasoning/tools and stale copied-transport invalidation remain Repository-owned.",
)
replace_once(
    profile,
    "- b65 fixed only nested disclosure/readable output and passed focused iPhone/iOS17 Runtime. Exact predecessor source `44138db766d00e62cfda7f20182f6d20f1ec3352`, Artifact `9736876465`, IPA `e6a01b2eafd361b9df2567b002f9e8aa56b57dcee219c7999c65767b91138d16`.",
    "- b65 fixed only nested disclosure/readable output and passed focused iPhone/iOS17 Runtime. Exact predecessor source `44138db766d00e62cfda7f20182f6d20f1ec3352`, Artifact `9736876465`, IPA `e6a01b2eafd361b9df2567b002f9e8aa56b57dcee219c7999c65767b91138d16`.\n- b67 accepted the existing-conversation production protected-Send transport: one Send -> HTTP200 SSE -> Repository updates -> terminal/reconcile.\n- b69 established the ordered response-timeline direction but exact iPhone/iOS17 Runtime exposed keyboard, optimistic-user-row, GitHub detail/icon/spacing/divider and transient Native 403 lifecycle defects.\n- b70 is the exact correction Candidate: source `fb83be9163838f78abfa47903e67f27b6f66ec52`, Push+PR CI passed, Artifact `9752289536`, package independently verified; Runtime pending.",
)
replace_between(
    profile,
    "## Exact b69 current Candidate\n",
    "## Current product interaction target\n",
    r'''## Exact b70 current Candidate

b70 retains accepted b67 protected-Send/SSE ownership and b69 chronological timeline while applying only evidence-backed daily-chat corrections: covered programmatic Web focus no longer owns visible keyboard state; the trimmed prompt is response-local optimistic user presentation; GitHub exact-parent input/output disclosures are restored with bounded local icons and deterministic spacing/divider; exact probe 403 preserves last verified account identity; list/detail 401/403 discards stale copied transient transport without replaying the failed operation.

Identity: Candidate `DEV-send-stream-0.1.0-b70`, `0.1.0 (70)`, exact source `fb83be9163838f78abfa47903e67f27b6f66ec52`, assembly `33373254877/99428895016`, Push `33377045570/99440767755`, PR `33377049590/99440781050`, Artifact `9752289536`, ZIP `bdf09b24...afde0`, IPA `8084e2ac...a44a`, package source marker `fb83be916383`, iOS14 minimum. Evidence: Code/scope/static+sim compile/Push+PR CI/Artifact/package verified; **Runtime pending**; Stable-Frozen No.

''',
)
replace_between(
    profile,
    "## Current next Candidate boundary\n",
    "## Remaining Unknown / Unverified\n",
    r'''## Current next Candidate boundary

b39-b70 are permanently reserved. Exact b70 real-device evidence is the only current Candidate gate. Do not allocate b71 before b70 Runtime yields a concrete defect/next evidence need. The gate must verify no covered-Web keyboard pop, one immediate nonduplicated optimistic user row, chronological reasoning/tools with restored GitHub details/icons/compact divider presentation, active-response navigation preservation, and transient Native 403 recovery on the next explicit/normal read without automatic retry.

''',
)
replace_once(
    profile,
    "Exact b69 ordered-timeline Runtime, new-chat authoritative identity timing, server Stop mechanism, simultaneous cross-conversation generation, connector detail beyond the evidenced GitHub mapping, Native first/exclusive resume, 5/15-minute background execution, WebContent termination, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.",
    "Exact b70 daily-chat parity/auth-lifecycle Runtime, new-chat authoritative identity timing, server Stop mechanism, simultaneous cross-conversation generation, connector detail beyond the evidenced GitHub mapping, Native first/exclusive resume, 5/15-minute background execution, WebContent termination, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.",
)

tech = "docs/project/TECHNICAL_DECISIONS.md"
replace_once(
    tech,
    "- **Status**: Confirmed product architecture decision; implementation/production Runtime still pending",
    "- **Status**: Confirmed product architecture decision; existing-conversation production transport Runtime accepted at b67; exact b70 daily-chat parity Runtime pending",
)
replace_once(
    tech,
    "- **Evidence ladder**: architecture decision confirmed; production code/CI/Artifact/Runtime under this decision remain pending until a new unique Candidate is emitted and tested.",
    "- **Evidence ladder**: architecture decision confirmed; b67 production existing-conversation transport Runtime accepted; exact b70 Code/scope/Push+PR CI/Artifact/package verified; b70 real-device daily-chat parity/auth-lifecycle Runtime remains pending.",
)
replace_once(
    tech,
    "## Rule\n",
    r'''### TD-030 — Transient Native read HTTP403 is not persistent logout by itself; stale copied transport is discarded without automatic replay
- **Status**: Confirmed state-lifecycle decision; exact b70 Runtime pending
- **Date**: 2026-08-31
- **Evidence**: exact b69 diagnostics/source correlation showed the same browser-authenticated account could pass session/accounts, later receive Native list/detail or account-probe HTTP403, and later succeed again. b69 also cached one copied `AuthTransientSession` indefinitely for an unchanged account scope. Therefore one 403 does not prove logout/account replacement, and retaining the failed copied transport can make Native reads sticky.
- **Decision**: exact HTTP403 at session/accounts probe stages is a temporary probe failure that preserves the last verified account identity while returning no fresh transient transport from that failed probe. Exact 401 retains unavailable/not-authenticated semantics.
- **Repository behavior**: current list/detail 401/403 invalidates/discards the copied transient transport once; that operation still fails visibly. A later explicit/normal read follows the existing account-context probe and materializes current WebKit credentials. The framework does not replay the failed operation.
- **User-navigation behavior**: returning from a user-opened login screen may issue one explicit list refresh; this is a new navigation operation, not hidden retry.
- **Ownership/security retained**: `AuthSessionStore` remains sole account authority; `WKWebsiteDataStore.default()` remains sole persistent auth-secret authority; `ConversationRepository` remains sole read/response lifecycle authority. No second credential store, retry loop, polling, timer, watchdog, compatibility shim or challenge copying is authorized.
- **Evidence boundary**: b70 Code/CI/Artifact/package success proves only implementation/package identity. Recovery from a real transient 403 remains a real-device Runtime gate.

## Rule
''',
)

devplan = "docs/project/DEVELOPMENT_PLAN.md"
replace_once(
    devplan,
    "_Last updated: 2026-08-31 through exact b66 Runtime failure and exact b67 Code/CI/Artifact/package verification._",
    "_Last updated: 2026-08-31 through accepted b67 production transport Runtime, b69 daily-chat defect evidence, and exact b70 Code/scope/Push+PR CI/Artifact/package verification._",
)
replace_between(
    devplan,
    "### Exact b67 — current correction Candidate\n",
    "### Official-like response lifecycle target\n",
    r'''### b67 accepted transport predecessor / b69 daily-chat evidence

Exact b67 accepted the production existing-conversation TD-029 transport gate: one local Send -> one protected official Send -> HTTP200 `text/event-stream` -> Repository reasoning/tool/final updates -> terminal -> one authoritative reconcile. This remains the transport predecessor and b70 does not replace its route/selectors/challenge/SSE grammar.

b69 then implemented one Repository-owned chronological response timeline. Exact iPhone/iOS17 Runtime retained real Send success but exposed six concrete daily-chat defects: covered-Web keyboard pop, missing immediate user row, excessive reasoning/tool spacing/no divider, lost b65 GitHub nested details, missing tool icons, and sticky Native reads around temporary 403.

### Exact b70 — current correction Candidate

b70 makes only the evidence-backed corrections:

1. suppress covered-Web virtual keyboard during temporary programmatic composer focus and blur after injection;
2. keep the actual trimmed prompt only in the current Repository live-response snapshot and render exactly one optimistic user row before the assistant row;
3. restore b65 exact-parent GitHub `工具输入` / `工具输出` mapping inside the ordered timeline, with bounded local icons and compact deterministic spacing/divider;
4. preserve last verified account identity across exact probe 403, retain 401 unavailable semantics, and discard stale copied transient read transport on list/detail 401/403 while visibly failing the current operation;
5. next explicit/normal read probes current WebKit credentials; no automatic replay/retry/poll/timer/watchdog;
6. returning from user-opened login may perform one explicit list refresh;
7. `ConversationRepository`, `AuthSessionStore`, default WebKit auth store, b38 geometry, and accepted b67 one-Send transport remain their existing authorities.

Identity/evidence:

- Candidate `DEV-send-stream-0.1.0-b70`, `0.1.0 (70)`;
- exact product/config source `fb83be9163838f78abfa47903e67f27b6f66ec52`, direct parent clean checkpoint `5c379b3d994b28cb0ba5a3c793e4efa193a003a1`;
- assembly `33373254877 / 99428895016`: exact five-file scope audit, `git diff --check`, Xcode16.4 iOS Simulator compile passed;
- Push `33377045570 / 99440767755` and PR `33377049590 / 99440781050` — success;
- Artifact `9752289536`; ZIP `sha256:bdf09b246ff259ee80d46acfad675713c1a0b51aee3b44f7ea9f0a7e67eafde0`;
- IPA `sha256:8084e2ace5926b7ee6a790f3eeb2445a2c4ce1fee67d8953300aca93a446a44a`;
- independently unpacked package `0.1.0 (70)` / Candidate b70 / source marker `fb83be916383` / iOS14 / arm64.

Evidence ladder: **Code / exact scope/static / Simulator compile / Push CI / PR CI / Artifact / package identity passed; Runtime pending; Stable-Frozen No.**

### Current Phase 9 human Runtime gate

Install exact b70 Artifact `9752289536` on the primary iPhone/iOS17 device and verify Build70/Candidate/source marker. Clear diagnostics, then test normal daily chat and one transient-read-auth recovery opportunity if reproducible.

Required evidence: no covered-Web keyboard pop; exactly one immediate optimistic user row with no terminal duplication; chronological reasoning/tool order and in-place tool completion; restored GitHub nested input/output, bounded icons, compact spacing and final divider; active response survives navigation; a transient Native 403 does not become sticky and can recover on the next explicit/normal read from current WebKit credentials without automatic replay/retry; hidden thoughts stay excluded; b38 geometry and b67 one-Send transport do not regress. Export diagnostics after terminal/recovery.

**Do not allocate b71 before exact b70 Runtime yields a concrete next need.** CI/Artifact/package success is not Runtime proof.

### Shortest remaining Phase 9 sequence after b70 gate

1. accept/fix this daily-chat existing-conversation parity/auth-lifecycle gate from exact Runtime evidence;
2. new-chat first Send and pending->authoritative handoff only if actual timing requires it;
3. exact server Stop evidence + response-scoped Stop implementation;
4. A/B hidden-response ownership + follow-tail/history intent;
5. Sync/Reload active-response safety + b38 geometry/round/time/Copy regression;
6. final daily-chat Runtime matrix, target-main sync, Stable/merge decision.

''',
)
text = read(devplan)
marker = "## Current next action\n"
if text.count(marker) != 1:
    raise SystemExit("DEVELOPMENT_PLAN current-next anchor mismatch")
text = text[:text.index(marker)] + r'''## Current next action

Hand exact b70 Artifact `9752289536` / IPA SHA `8084e2ace5926b7ee6a790f3eeb2445a2c4ce1fee67d8953300aca93a446a44a` to the user for the focused b70 real-device daily-chat/auth-lifecycle gate. Keep PR #29 open/unmerged. Do not allocate b71 or begin unrelated Composer/attachments/Stop/background work before that Runtime evidence.
'''
write(devplan, text)

expected = {
    "docs/project/current/dev/DEV-send-stream.md",
    "docs/project/BUILD_TEST_INDEX.md",
    "docs/project/PROJECT_STATE.md",
    "docs/project/MODULE_STATUS.md",
    "docs/project/PROJECT_PROFILE.md",
    "docs/project/TECHNICAL_DECISIONS.md",
    "docs/project/DEVELOPMENT_PLAN.md",
}
for path in expected:
    if not (ROOT / path).exists():
        raise SystemExit(f"missing expected doc: {path}")

# Content guards: do not accidentally claim Runtime acceptance or redefine product source.
cp = read(checkpoint)
if "Runtime/manual/real-device: **Pending b70 gate**" not in cp:
    raise SystemExit("checkpoint runtime boundary missing")
if "fb83be9163838f78abfa47903e67f27b6f66ec52" not in cp or "9752289536" not in cp:
    raise SystemExit("checkpoint identity missing")
if "Stable/Frozen: **No**" not in cp:
    raise SystemExit("checkpoint stability boundary missing")

print("b70 evidence docs exact-anchor patch complete")
