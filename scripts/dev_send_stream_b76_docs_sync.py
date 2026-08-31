from pathlib import Path

EXACT_SOURCE = "0da5a7577f2cf3b2a6882d8a0ec920b5c8f37c71"
PUSH = "33440101178 / 99645927061"
PR = "33440098527 / 99645917529"
ARTIFACT = "9775920927"
ZIP_SHA = "52f94ed7dbfbe311e37656fcce9a60bb5f8cc9c6b2af29434f7020d47729e944"
IPA_SHA = "b130c9059ec85d08d95105b32b71157a4be2b2ecea25112963f0a548ec252bcd"


def read(path): return Path(path).read_text()
def write(path, value): Path(path).write_text(value)

def prepend_after_title(path, block):
    value = read(path)
    first, sep, rest = value.partition("\n")
    if not sep or not first.startswith("# "): raise SystemExit(f"bad title: {path}")
    marker = block.strip().splitlines()[0]
    if marker in value: raise SystemExit(f"block already exists: {path}")
    write(path, first + "\n\n" + block.strip() + "\n\n" + rest.lstrip("\n"))

prepend_after_title("docs/project/PROJECT_STATE.md", f'''## DEV-send-stream b76 candidate override — 2026-09-01

Exact b76 `DEV-send-stream-0.1.0-b76` / `0.1.0 (76)` is the current test candidate. Exact product/config source `{EXACT_SOURCE}` passed guarded exact-scope assembly plus Xcode 16.4 Simulator build, formal Push CI `{PUSH}` and PR CI `{PR}`. Canonical Push Artifact `{ARTIFACT}` has ZIP `sha256:{ZIP_SHA}` and IPA `sha256:{IPA_SHA}`. Independent package inspection confirms Release 0.1.0 (76), Candidate b76, source marker `0da5a7577f2c`, MinimumOSVersion 14.0, arm64, iPhone+iPad family.

- Current visible official Web can receive matching page-owned `/resume` HTTP404 JSON and then follow the active response through its own already-issued `stream_status` + plural `/backend-api/conversations/{{conversation}}` reads.
- The plural rolling `messages[]` window exposes the required service-message family during `IS_STREAMING` and the finished final message after `COMPLETE`; raw message count is not a cursor.
- b76 observes only those page-owned responses, validates target identity, derives entries after the latest user, and atomically projects them into the existing `ConversationRepository` live-response owner. It adds no Native polling/cadence, Native resume/offset request, WebSocket body authority or second state store. Actual page-owned `/resume` HTTP200 SSE support remains strictly validated and retained when it occurs.
- Typography candidate is tool 30 / reasoning 21 / final 21. Runtime visual acceptance is pending.
- Runtime/manual/real-device b76: **Pending / Unverified**. Stable/Frozen Send: **No**. b39-b76 are permanently reserved.''')

prepend_after_title("docs/project/MODULE_STATUS.md", f'''## DEV-send-stream b76 candidate override — 2026-09-01

- Build/runtime metadata: exact b76 source `{EXACT_SOURCE}`; Push `{PUSH}` and PR `{PR}` success; Artifact `{ARTIFACT}`; IPA `sha256:{IPA_SHA}`; package independently verified as Release 0.1.0 (76), Candidate b76, source `0da5a7577f2c`, iOS14 minimum, arm64. Runtime pending.
- Covered external continuation: current official page may `/resume` -> 404, then use its own `stream_status` + plural conversation reads. b76 observes only that existing page traffic and atomically projects the latest-user-bounded service segment into `ConversationRepository`; no Native polling/resume construction/WebSocket body path.
- User-visible reasoning/tool/final: current probe evidence contains thinking preambles, exact-parent tools/results, reasoning recap/end and final in-progress/completed message structures. b76 Code/CI/Artifact is verified but device presentation remains unverified.
- Typography: b76 candidate increases 26/18.2/18.2 -> 30/21/21 while preserving the 0.70 relationship and shared measurement/rendering style.
- Geometry: b75 cooperative path evidence remains; worst-case Back responsiveness is still an open real-device gate if reproduced.''')

prepend_after_title("docs/project/TECHNICAL_DECISIONS.md", '''## b76 qualification — 2026-09-01

- **TD-029 current external-continuation rule:** a page-owned matching `/backend-api/f/conversation/resume` is accepted only on exact HTTP200 `text/event-stream`. Current visible-Web evidence also proves official Web can receive resume HTTP404 JSON and then follow the same active response through its own already-issued `stream_status` and plural `/backend-api/conversations/{conversation}` responses. Native must not reproduce either request or cadence. b76 may observe matching page-owned responses, validate target identity, derive service messages after the latest user, and atomically project them into the sole Repository response runtime. WebSocket remains non-authoritative. Raw plural message count is not a cursor because the response is rolling/paged.
- **TD-014 presentation qualification:** b75 26/18.2/18.2 remains rejected. b76 tests 30/21/21 while preserving the 0.70 relationship and shared reasoning/final measurement/rendering behavior; visual acceptance is Runtime-only.
- b67 local protected-Send Runtime and b72 tested concurrent ownership remain accepted predecessors. b76 CI/Artifact success does not establish Runtime success.''')

prepend_after_title("docs/project/PROJECT_SPECIFIC_RULES.md", f'''## b76 current candidate override — 2026-09-01

- Exact b76 is allocated and permanently reserved: `DEV-send-stream-0.1.0-b76`, Build76, exact product/config source `{EXACT_SOURCE}`, Artifact `{ARTIFACT}`, IPA SHA `{IPA_SHA}`.
- Current official-page external continuation is not `/resume`-SSE-only. A page-owned resume still requires exact HTTP200 SSE before SSE adoption; current evidence also allows official page-owned resume 404 followed by its own status/plural read path.
- Production may observe only the page's already-issued matching status/plural responses. It must not construct/schedule Native polling, copy cadence, construct resume/offset, parse WebSocket bodies, resend, add retry/watchdog behavior or create a second conversation/message/response store.
- Plural `messages[]` is rolling/paged; raw count is not a cursor. Bound the active segment by the latest user service message, validate target identity and project snapshots atomically into the sole `ConversationRepository` response owner.
- `assistant:thoughts` / inline COT remain non-presentational; exact-parent tool association and narrow GitHub detail mapping remain unchanged.
- b76 tool/reasoning/final line heights are candidate 30/21/21. Runtime visual acceptance pending.
- Code/static/Simulator/Push+PR CI/Artifact/package are passed; real-device Runtime and Stable/Frozen remain **No / Unverified**.''')

web_path = "docs/project/WEB_SEND_ADAPTER.md"
web = read(web_path)
old_last = "_Last established: 2026-09-01 through DEV-send-stream b67 accepted local transport, b72 tested concurrent ownership, and current cross-device page-owned `/resume` evidence used by exact b74._"
new_last = "_Last established: 2026-09-01 through b67 accepted local transport, b72 tested concurrent ownership, b75 visible-Web continuation probes, and exact b76 Code/CI/Artifact/package verification; b76 Runtime remains pending._"
if web.count(old_last) != 1: raise SystemExit("WEB_SEND_ADAPTER last-established mismatch")
web = web.replace(old_last, new_last, 1)
marker = "## Current b76 external-response read rule — 2026-09-01"
if marker in web: raise SystemExit("WEB_SEND_ADAPTER block exists")
insert_at = web.index("\n## Purpose")
block = '''\n\n## Current b76 external-response read rule — 2026-09-01

Fresh visible official-Web evidence supersedes the older same-day assumption that cross-device adoption must receive a successful `/backend-api/f/conversation/resume` SSE. Current official-page behavior can be:

`page-owned stream_status=IS_STREAMING -> page-owned /resume -> HTTP404 JSON -> repeated page-owned stream_status + plural /backend-api/conversations/{conversation} JSON -> stream_status=COMPLETE -> final plural snapshot`

The plural response is a rolling/paged top-level `messages[]` window. Its raw count is not monotonic and is not a response cursor. Entries are the same service-message family already evidenced by the native parser. While streaming, the active segment can contain visible thinking preambles, assistant/non-all tool invocations, exact-parent tool results, hidden thoughts/inline COT, reasoning recap/end and an assistant final message with `status=in_progress`; after `COMPLETE`, the final assistant is `finished_successfully`, `end_turn=true` with completed body.

**Current b76 production rule:** observe only page-owned matching requests/responses already issued by official Web; never construct or schedule Native status/plural reads and never reproduce cadence. Validate returned conversation identity, find the latest user service message, project only following entries atomically into the existing `ConversationRepository` live-response runtime, preserve existing reasoning/tool/final semantics, and terminal/reconcile once after page-owned COMPLETE plus the following plural snapshot. Historical page-owned `/resume` remains supported only when that exact response is HTTP200 `text/event-stream`. User-level WebSocket remains structural-only and is not a response-body source.

Exact b76 has passed guarded scope/Simulator, Push+PR CI, Artifact and package identity checks. Those checks do not prove Runtime behavior; real-device adoption remains the Human Gate.'''
web = web[:insert_at] + block + web[insert_at:]
write(web_path, web)

plan_path = "docs/project/DEVELOPMENT_PLAN.md"
plan = read(plan_path)
old_plan_last = "_Last updated: 2026-09-01 through exact DEV-send-stream b75 Runtime qualification and the current Web Rule Lab continuation re-probe gate._"
new_plan_last = "_Last updated: 2026-09-01 through exact DEV-send-stream b76 Code/static/Simulator/Push+PR CI/Artifact/package verification; the next gate is b76 real-device Runtime._"
if plan.count(old_plan_last) != 1: raise SystemExit("DEVELOPMENT_PLAN last-updated mismatch")
plan = plan.replace(old_plan_last, new_plan_last, 1)
phase = "## Phase 9 — `DEV-send-stream` — Active production integration\n"
if plan.count(phase) != 1: raise SystemExit("DEVELOPMENT_PLAN phase mismatch")
current = f'''\n### Current b76 candidate / next gate — 2026-09-01\n\n- Exact candidate `DEV-send-stream-0.1.0-b76` / `0.1.0 (76)`; source `{EXACT_SOURCE}`; Artifact `{ARTIFACT}`; IPA SHA `{IPA_SHA}`.\n- Guarded scope/Simulator passed; Push `{PUSH}` and PR `{PR}` passed; package identity independently verified.\n- Current external-response design observes only page-owned status/plural reads after current resume 404, validates target identity and atomically projects the latest-user-bounded service segment into the Repository response owner. No Native polling/cadence/resume construction/WebSocket body path. Actual HTTP200-SSE page-owned resume remains supported under strict validation.\n- b76 also tests 30/21/21 vertical rhythm.\n- **Next gate is Human Runtime:** cross-platform active-response adoption, b67 local Send regression, b72 concurrent-ownership regression, visual spacing, and worst-case Back responsiveness if reproduced. Stable/Frozen remains No.\n'''
plan = plan.replace(phase, phase + current, 1)
write(plan_path, plan)

index_path = "docs/project/BUILD_TEST_INDEX.md"
index = read(index_path)
if "DEV-send-stream-0.1.0-b76" in index: raise SystemExit("b76 already in BUILD_TEST_INDEX")
sep = "|---|---|---|---|---|---|---|\n"
if index.count(sep) != 1: raise SystemExit("BUILD_TEST_INDEX separator mismatch")
row = f'''| `DEV-send-stream-0.1.0-b76` | `DEV-send-stream` | `0.1.0 (76)` | `{EXACT_SOURCE}`; PR #29 | Assembly `33439797547/99644929642`; Push `{PUSH}`; PR `{PR}`; Artifact `{ARTIFACT}`; ZIP `{ZIP_SHA}`; IPA `{IPA_SHA}`; package Release/source `0da5a7577f2c`/iOS14/arm64 | Runtime pending: page-owned plural snapshot adoption + 30/21/21 spacing + regressions | **Code/CI/Artifact/package verified; Runtime Unverified; reserved** |\n'''
index = index.replace(sep, sep + row, 1)
write(index_path, index)

cp_path = "docs/project/current/dev/DEV-send-stream.md"
cp = read(cp_path)
repls = {
    "- Push CI: Pending": f"- Push CI: `{PUSH}` — success",
    "- PR CI: Pending": f"- PR CI: `{PR}` — success",
    "- Artifact/package identity: Pending": f"- Canonical Push Artifact: `{ARTIFACT}`\n- ZIP SHA: `{ZIP_SHA}`\n- IPA: `ChatGPTClient-0.1.0-b76-dev-send-stream.ipa`\n- IPA SHA: `{IPA_SHA}`\n- Package independently verified: Release `0.1.0 (76)`, Candidate b76, source marker `0da5a7577f2c`, MinimumOSVersion 14.0, arm64, iPhone+iPad family",
    "- Formal Push CI: **Pending**": f"- Formal Push CI: **Passed — `{PUSH}`**",
    "- Formal PR CI: **Pending**": f"- Formal PR CI: **Passed — `{PR}`**",
    "- Artifact produced: **Pending**": f"- Artifact produced: **Yes — canonical Push Artifact `{ARTIFACT}`**",
    "- Package identity verified: **Pending**": "- Package identity verified: **Yes — ZIP/IPA SHA and built Info.plist independently checked**",
}
for old, new in repls.items():
    if cp.count(old) != 1: raise SystemExit(f"checkpoint mismatch: {old}")
    cp = cp.replace(old, new, 1)
old_next = "AI-owned: verify formal Push + PR CI for exact `0da5a757...`, obtain canonical Push Artifact, independently verify Build76/Candidate/source marker/package hashes, update `WEB_SEND_ADAPTER.md`, `BUILD_TEST_INDEX.md`, project/module state and PR metadata, then provide the exact b76 IPA."
if cp.count(old_next) != 1: raise SystemExit("checkpoint next action mismatch")
cp = cp.replace(old_next, "AI-owned build/CI/package/documentation work is complete. Next exact action is the Human b76 device gate using the canonical IPA; record Runtime evidence before any further product candidate.", 1)
write(cp_path, cp)

evidence = Path("docs/project/runtime-evidence/DEV-send-stream-b76-candidate.md")
if evidence.exists(): raise SystemExit("b76 candidate evidence exists")
evidence.write_text(f'''# DEV-send-stream b76 Candidate Evidence\n\n_Date: 2026-09-01_\n\n## Exact identity\n\n- Candidate: `DEV-send-stream-0.1.0-b76`\n- Version/build: `0.1.0 (76)`\n- Exact product/config source: `{EXACT_SOURCE}`\n- Clean product commit: `60bebc9e5b2296f6426ad264d7b57979781360b7`, parent exact checkpoint `dd18b5beca16af34b075295dc3fc0782c714f26b`\n- Guarded assembly: `33439797547 / 99644929642` — patch, `git diff --check`, exact three-product-file scope and Xcode 16.4 Simulator build passed\n- Push CI: `{PUSH}` — success\n- PR CI: `{PR}` — success\n- Canonical Push Artifact: `{ARTIFACT}`\n- Artifact ZIP SHA-256: `{ZIP_SHA}`\n- IPA: `ChatGPTClient-0.1.0-b76-dev-send-stream.ipa`\n- IPA SHA-256: `{IPA_SHA}`\n- Independent package inspection: Release 0.1.0 (76), Candidate b76, source marker `0da5a7577f2c`, MinimumOSVersion 14.0, iPhone+iPad family, Mach-O arm64\n\n## Code scope / boundary\n\nClean product compare changes exactly `ChatGPTClient/RootViewController.swift`, `ChatGPTClient/Conversation/ConversationFeature.swift`, and `ChatGPTClient.xcodeproj/project.pbxproj`; exact source adds `.github/workflows/ios-foundation.yml` only for b76 Artifact identity.\n\nThe covered executor observes only official page-owned matching status/plural responses when external observation is active. The plural rolling window is bounded after the latest user service message and projected atomically into the existing Repository live-response runtime. No Native polling/cadence, Native resume/offset construction, WebSocket response-body parsing or duplicate Send is added. Strict actual HTTP200-SSE page-owned resume support remains. Typography candidate changes 26/18.2/18.2 -> 30/21/21.\n\n## Evidence classification\n\n- Code written: Yes\n- Static/exact scope: Passed\n- Xcode 16.4 Simulator: Passed\n- Push CI: Passed\n- PR CI: Passed\n- Artifact produced: Yes\n- Package identity: Independently verified\n- Runtime/manual/real-device: **No / Pending**\n- Stable/Frozen Send: **No**\n\n## Human gate\n\nInstall exact b76 IPA and test cross-platform live adoption, terminal once, b67 local Send regression, b72-style concurrent ownership regression, 30/21/21 visual spacing, and the prior extreme Back stall if reproducible. Diagnostics must remain privacy-safe.\n''')
