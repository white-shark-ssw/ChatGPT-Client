from pathlib import Path
import re


def rw(path): return Path(path).read_text()
def ww(path, text): Path(path).write_text(text)
def one(text, old, new, label):
    if text.count(old) != 1: raise SystemExit(f"{label}: expected one match, got {text.count(old)}")
    return text.replace(old, new, 1)
def region(text, start, end, new, label):
    a = text.find(start); b = text.find(end, a + len(start)) if a >= 0 else -1
    if a < 0 or b < 0: raise SystemExit(f"{label}: markers missing")
    return text[:a] + new + text[b:]

# DEV-send-stream checkpoint
p = "docs/project/current/dev/DEV-send-stream.md"; t = rw(p)
t = region(t, "## Status\n\n", "## Exact b67 accepted production transport identity\n", '''## Status

**Active — exact b69 ordered reasoning/tool timeline Candidate is Code/CI/Artifact/package verified and is now at the human iPhone/iOS17 Runtime gate. b67 remains the accepted production existing-conversation transport Runtime predecessor. b68 is a valid reserved Artifact whose flattened presentation was superseded before Runtime by the user-supplied official-app recording. b69 preserves one assistant-turn chronology `思考 -> 工具 -> 再思考 -> 再工具 ... -> final` in one Repository-owned ordered timeline while keeping covered-Web transport/SSE/auth boundaries unchanged. Stable/Frozen Send remains No. PR #29 stays open / mergeable / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — keep open / evidence-only / unmerged
- Exact b69 product/config source: `5e9c2183483094304f7eaeecf4ffc7ad8e65b902`
- Current actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Stable merged predecessor: b38
- Latest accepted production Runtime pass: b67
- Latest emitted Candidate: b69 — CI/Artifact/package verified; Runtime pending
- b39-b69 identities are permanently reserved.

''', "checkpoint status")
marker = "## Evidence ladder now\n"
b69 = '''## Exact b69 identity — ordered reasoning/tool timeline Runtime candidate

- Candidate: `DEV-send-stream-0.1.0-b69`; Version / Build: `0.1.0 (69)`.
- Exact product/config source: `5e9c2183483094304f7eaeecf4ffc7ad8e65b902`; product commit `905ac2633a408cf571d25ccfe427bdd1a9a27f34`; checkpoint base `33022dc8c9fdcb17f5b462a2766ac86238417c58`.
- Push Run / Job: `33366226539 / 99407331552` — success; PR Run / Job: `33366229125 / 99407340011` — success.
- Push Artifact: `9748400171`; ZIP `sha256:b1d91179c47822a7a42bf5405ef4bbd7240b97ddff58743a8a12e5f16fb232f1`.
- IPA: `ChatGPTClient-0.1.0-b69-dev-send-stream.ipa`; IPA SHA `0c06256dc90aed86c706f8c72950528f61afa7f7fcdb504b2604d40befe3b0aa`.
- Independently inspected built `Info.plist`: Release `0.1.0`, Build `69`, Candidate b69, `DiagnosticsSourceCommit=5e9c21834830`, minimum iOS14.
- Compile note: one non-blocking unused local `index` warning; valid Artifact exists, so b69 is permanently reserved and is not rewritten merely for that warning.
- Runtime: pending on primary iPhone/iOS17 device.

b69 keeps one Repository-owned ordered response timeline. First tool activity appends at its event position; completion updates that item in place by slot; reasoning after a tool creates a new reasoning segment; exact `reasoning_ended` still owns reasoning->final; final text stays separate/incremental. Authoritative Detail reconstructs supported visible thinking/tool order while `assistant:thoughts` / `inline_cot_expandable_content` remain hidden. Covered-Web route/selectors/challenge/protected-Send/SSE grammar were not intentionally modified.

### Exact b69 Runtime gate

Install exact b69 and run one real request that naturally yields at least `reasoning A -> tool 1 -> reasoning B -> tool 2 -> final`. Accept only if live ordering is chronological, tool completion updates in place, later reasoning stays below the preceding tool, reasoning-end collapses into incremental final, authoritative reconciliation preserves the supported historical order, hidden thoughts stay absent, and the old floating overlay does not return. Export diagnostics after terminal.

'''
if marker not in t: raise SystemExit("checkpoint marker missing")
t = t.replace(marker, b69 + marker, 1)
t = region(t, "## Evidence ladder now\n", "## Next exact action\n", '''## Evidence ladder now

- b67: production existing-conversation Send/stream/terminal/reconcile Runtime passed.
- b68: Code/diff/Push+PR CI/Artifact/package verified; Runtime not accepted; flattened presentation superseded by explicit official-flow evidence.
- b69: Code written / detached diff audited / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Runtime pending.
- Stable/Frozen Send: No.

''', "checkpoint ladder")
pos = t.find("## Next exact action\n")
if pos < 0: raise SystemExit("checkpoint next missing")
t = t[:pos] + '''## Next exact action

Human-only Runtime gate: install exact `DEV-send-stream-0.1.0-b69` / Build69 / source marker `5e9c21834830` on the primary iPhone/iOS17 device, clear diagnostics, execute one real request that naturally yields at least `reasoning -> tool -> reasoning -> tool -> final`, verify chronological interleaving plus in-place tool completion and post-terminal historical preservation, then export diagnostics. Do not allocate b70 unless that exact Runtime produces a concrete defect/evidence need.
'''
ww(p, t)

# Build/Test index: b66-b69 rows after b65 if absent.
p = "docs/project/BUILD_TEST_INDEX.md"; t = rw(p)
if "DEV-send-stream-0.1.0-b69" not in t:
    a = t.find('| `DEV-send-stream-0.1.0-b65` |'); e = t.find("\n", a)
    if a < 0 or e < 0: raise SystemExit("b65 row missing")
    rows = '''
| `DEV-send-stream-0.1.0-b66` | `DEV-send-stream` | `0.1.0 (66)` | source `9ce228ad880eaf81fc23ba26fe14f4d2bf524acb`; PR #29 | Push `33337771534/99327694040`; PR `33337774136/99327701256`; Artifact `9739572172`; IPA `7f62e875bbd75d54e2d7bf76340f277d02f03e695d464d818fa5cab664c630e9` | Send reached service but duplicate submit ended in `send_transport_error` before Native HTTP Response | **Production Runtime failed; permanently reserved** |
| `DEV-send-stream-0.1.0-b67` | `DEV-send-stream` | `0.1.0 (67)` | source `52ab38f16fe914ef8316bb1dc712b77c2c87a271`; PR #29 | Push `33338865423/99330666394`; PR `33338868896/99330678769`; Artifact `9739891865`; IPA `3712dec92cddfe64e84fc797e1506d83231cd878633b932b9acf0e7381795497` | One submitted/real Send, HTTP200 SSE, Repository updates, terminal + authoritative reconcile | **Production transport Runtime accepted; permanently reserved** |
| `DEV-send-stream-0.1.0-b68` | `DEV-send-stream` | `0.1.0 (68)` | source `269d9530223f2ed59dbd06c5b14dc87fce7a742f`; PR #29 | Push `33364874077/99403338734`; PR `33364879111/99403353153`; Artifact `9747954069`; IPA `d6f81953a07f29c43e755547b344276b1e503864664325d96d16e07dd9ebcf73` | Inline response/history reasoning built; official recording exposed flattened reasoning/tools ordering mismatch | **CI/Artifact/package valid; pre-Runtime superseded; permanently reserved** |
| `DEV-send-stream-0.1.0-b69` | `DEV-send-stream` | `0.1.0 (69)` | source `5e9c2183483094304f7eaeecf4ffc7ad8e65b902`; PR #29 | Push `33366226539/99407331552`; PR `33366229125/99407340011`; Artifact `9748400171`; ZIP `sha256:b1d91179c47822a7a42bf5405ef4bbd7240b97ddff58743a8a12e5f16fb232f1`; IPA `0c06256dc90aed86c706f8c72950528f61afa7f7fcdb504b2604d40befe3b0aa` | Repository-owned ordered `reasoning -> tool -> reasoning -> tool -> final` timeline for live + authoritative history | **Code/CI/Artifact/package verified; Runtime pending; permanently reserved** |'''
    t = t[:e] + rows + t[e:]
t = t.replace("Exact b39-b65 Candidate identities are permanently reserved once emitted", "Exact b39-b69 Candidate identities are permanently reserved once emitted")
ww(p, t)

# Project State
p = "docs/project/PROJECT_STATE.md"; t = rw(p)
t = one(t, "_Last updated: 2026-08-31 through exact b66 iPhone/iOS17 Runtime failure and exact b67 Code/CI/Artifact/package verification. Phase 9 `DEV-send-stream` remains Active. Stable/Frozen Send remains No._", "_Last updated: 2026-08-31 through accepted b67 production transport Runtime, b68 superseded presentation Artifact, and exact b69 Code/CI/Artifact/package verification. Phase 9 `DEV-send-stream` remains Active at the b69 human Runtime gate. Stable/Frozen Send remains No._", "state timestamp")
t = region(t, "Latest exact product Candidate is **`DEV-send-stream-0.1.0-b67` / `0.1.0 (67)`**:\n", "## b65 accepted probe predecessor\n", '''Latest exact product Candidate is **`DEV-send-stream-0.1.0-b69` / `0.1.0 (69)`**:

- source `5e9c2183483094304f7eaeecf4ffc7ad8e65b902`;
- Push `33366226539 / 99407331552` and PR `33366229125 / 99407340011` — success;
- Artifact `9748400171`; ZIP `sha256:b1d91179c47822a7a42bf5405ef4bbd7240b97ddff58743a8a12e5f16fb232f1`;
- IPA `sha256:0c06256dc90aed86c706f8c72950528f61afa7f7fcdb504b2604d40befe3b0aa`;
- package `0.1.0 (69)` / Candidate b69 / source `5e9c21834830` / minimum iOS14.

b69 replaces b68's flattened live reasoning/tool representation with one Repository-owned ordered timeline matching `reasoning -> tool -> reasoning -> tool -> final`. Covered-Web transport remains the accepted b67 path. Evidence ladder: **Code / detached diff / Push+PR CI / Artifact / package verified / Runtime pending / Stable-Frozen No.** b39-b69 are reserved; do not allocate b70 before concrete b69 Runtime evidence.

''', "state candidate")
t = region(t, "## Current exact Runtime gate\n", "## Remaining Unknown / Unverified\n", '''## Current exact Runtime gate

Install exact b69 on the primary iPhone/iOS17 device and run one request naturally yielding at least `reasoning A -> tool 1 -> reasoning B -> tool 2 -> final`. Verify chronological live ordering, in-place tool completion, later reasoning below the preceding tool, exact reasoning-end/final transition, authoritative historical preservation, hidden-thought prohibition and no floating overlay. Export diagnostics after terminal.

''', "state gate")
t = t.replace("Exact b67 production Runtime, new-chat authoritative identity timing", "Exact b69 ordered-timeline Runtime, new-chat authoritative identity timing")
ww(p, t)

# Module Status: compact current rows/boundary.
p = "docs/project/MODULE_STATUS.md"; t = rw(p)
t = re.sub(r'^\| Build/runtime metadata \|.*$', '| Build/runtime metadata | **b69 exact identity; Runtime pending** | Xcode settings / built `Info.plist` | `0.1.0 (69)`, source `5e9c21834830...`, Artifact `9748400171`; b39-b69 reserved. |', t, count=1, flags=re.M)
t = re.sub(r'^\| IPA build / CI packaging \|.*$', '| IPA build / CI packaging | **Stable capability; b69 Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33366226539/99407331552`, PR `33366229125/99407340011`, Artifact `9748400171`, IPA `0c06256d...3b0aa`; package b69/source `5e9c21834830`/iOS14/arm64. |', t, count=1, flags=re.M)
t = re.sub(r'^\| Covered official-Web protected Send executor \|.*$', '| Covered official-Web protected Send executor | **Production transport Runtime accepted b67; unchanged by b69** | `CoveredWebSendExecutor` + TD-029 + `WEB_SEND_ADAPTER.md` | b67 passed one protected Send -> HTTP200 SSE -> terminal/reconcile. b69 changes ordered Repository presentation only. |', t, count=1, flags=re.M)
t = re.sub(r'^\| Streaming / Send \|.*$', '| Streaming / Send | **Active — b67 transport accepted; b69 ordered presentation Runtime gate** | `DEV-send-stream`; PR #29; TD-029 | b69 is Code/CI/Artifact/package verified for chronological reasoning/tool interleaving; Runtime pending. |', t, count=1, flags=re.M)
t = re.sub(r'^\| User-visible reasoning \|.*$', '| User-visible reasoning | **Production stream passed b67; ordered b69 presentation Runtime pending** | `ConversationRepository` + `DEV-send-stream` | Ordered reasoning segments interleave with tools; exact `reasoning_ended` remains final authority; hidden thoughts prohibited. |', t, count=1, flags=re.M)
t = re.sub(r'^\| Tool activity presentation \|.*$', '| Tool activity presentation | **b69 Code/CI/Artifact verified; Runtime pending** | `DEV-send-stream` | Tool appends at event position, completion updates in place by slot, later reasoning forms a segment below it. |', t, count=1, flags=re.M)
t = region(t, "## Current acceptance boundary\n", "## Auto-refresh rule\n", '''## Current acceptance boundary

- Stable merged native baseline remains b38.
- b67 production existing-conversation transport Runtime is accepted.
- b68 is a valid reserved Artifact but its flattened reasoning/tool presentation was superseded before Runtime.
- b69 source `5e9c2183483094304f7eaeecf4ffc7ad8e65b902`, Artifact `9748400171`, IPA `0c06256d...3b0aa` is the current ordered-timeline Runtime candidate.
- `ConversationRepository` remains sole response authority; `WEB_SEND_ADAPTER.md` is unchanged because b69 consumes already-emitted event order.
- b39-b69 are reserved. Phase 9 Stable/Frozen: No.

''', "module boundary")
ww(p, t)

# Project Profile
p = "docs/project/PROJECT_PROFILE.md"; t = rw(p)
t = one(t, "**Initialized — 2026-08-25; refreshed 2026-08-31 through exact b66 Runtime and exact b67 Code/CI/Artifact/package verification.**", "**Initialized — 2026-08-25; refreshed 2026-08-31 through accepted b67 production transport Runtime, b68 superseded presentation Artifact, and exact b69 Code/CI/Artifact/package verification.**", "profile stamp")
t = t.replace("current b66/b67 response runtime extension is still Repository-owned", "current b69 ordered response runtime extension is still Repository-owned")
t = region(t, "## Exact b67 current Candidate\n", "## Current product interaction target\n", '''## Exact b69 current Candidate

b69 implements the user-supplied official-app chronological requirement with one Repository-owned ordered response timeline. Reasoning/tool items keep event order; tool completion updates in place; reasoning after a tool becomes a new segment; exact `reasoning_ended` still transitions to separate incremental final; authoritative Detail preserves supported order; hidden thoughts remain prohibited; b38 deterministic/manual geometry is retained.

Identity: Candidate `DEV-send-stream-0.1.0-b69`, `0.1.0 (69)`, source `5e9c2183483094304f7eaeecf4ffc7ad8e65b902`, Push `33366226539/99407331552`, PR `33366229125/99407340011`, Artifact `9748400171`, ZIP `b1d91179...232f1`, IPA `0c06256d...3b0aa`, package source marker `5e9c21834830`, iOS14 minimum. Evidence: Code/diff/Push+PR CI/Artifact/package verified; **Runtime pending**; Stable-Frozen No.

''', "profile candidate")
t = region(t, "## Current next Candidate boundary\n", "## Remaining Unknown / Unverified\n", '''## Current next Candidate boundary

b39-b69 are permanently reserved. **Do not allocate b70 before exact b69 iPhone/iOS17 Runtime evidence.** The gate must naturally exercise at least `reasoning -> tool -> reasoning -> tool -> final` and verify chronological live/history presentation without modifying accepted b67 transport unless concrete Runtime evidence demands it.

''', "profile boundary")
t = t.replace("Exact b67 production Runtime, new-chat authoritative identity timing", "Exact b69 ordered-timeline Runtime, new-chat authoritative identity timing")
ww(p, t)

# TD-014 durable ordering contract.
p = "docs/project/TECHNICAL_DECISIONS.md"; t = rw(p)
t = one(t, "- **Status**: Confirmed requirement; diagnostic reasoning lifecycle evidenced through b65; production owner integration pending", "- **Status**: Confirmed requirement; production transport accepted b67; ordered production presentation implemented b69, Runtime pending", "TD014 status")
t = one(t, "- **Decision**: When the production `ConversationRepository` response owner receives explicitly user-visible reasoning detail/status from the accepted same-response stream, use subdued active reasoning/shimmer, explicit expand/collapse visible detail and two short haptic pulses on real-time reasoning->final transition. Never expose hidden chain-of-thought. `assistant:thoughts` remains non-presentational.", "- **Decision**: When `ConversationRepository` receives explicitly user-visible reasoning/tool events, preserve chronological order inside one assistant turn (`reasoning -> tool -> reasoning -> tool -> ... -> final`). Tool completion updates the existing tool segment in place; later reasoning remains below the preceding tool. Keep explicit expand/collapse and the accepted reasoning->final transition behavior. Never expose hidden chain-of-thought; `assistant:thoughts` / `inline_cot_expandable_content` remain non-presentational. This ordering is grounded by the user-supplied official ChatGPT recording and b69 implements it without a second response owner.", "TD014 decision")
ww(p, t)
