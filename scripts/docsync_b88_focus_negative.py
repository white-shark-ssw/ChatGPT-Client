from pathlib import Path

root = Path('.')

def ensure_nl(path: Path):
    text = path.read_text()
    if not text.endswith('\n'):
        path.write_text(text + '\n')

def prepend(path: Path, title: str, section: str):
    ensure_nl(path)
    text = path.read_text()
    anchor = title + '\n\n'
    assert text.startswith(anchor), f'{path}: title mismatch'
    marker = section.splitlines()[0]
    assert marker not in text, f'{path}: already updated'
    path.write_text(anchor + section.rstrip() + '\n\n' + text[len(anchor):])

# New durable Runtime evidence.
evidence = root / 'docs/project/runtime-evidence/DEV-send-stream-b88-focus-sufficient-rejected-20260902.md'
assert not evidence.exists(), 'evidence already exists'
evidence.write_text('''# DEV-send-stream b88 focus-sufficient rejected Runtime — 2026-09-02

## Identity

- Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- Exact product source: `31d24e8b9ab4676effd757a793162abbdb0d7012`
- Clean package head / diagnostics source: `378811691ccbd6f44b232d8cc5564628e9b021e1` / `378811691ccb`
- Canonical Artifact: `9848999246`
- IPA SHA-256: `cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`
- Device: iPhone / iOS17.0
- Mid-run diagnostics: `ChatGPTClient-Diagnostics-20260902-150016.json`
- Final diagnostics: `ChatGPTClient-Diagnostics-20260902-150109.json`
- Target conversation hash: `sha256:38ede68b30d8`

## Runtime timeline

- `14:58:06Z` initial authoritative Detail: visible `12`, mapping `479`, trailing timeline/tools `5/5`.
- Explicit Sync at `14:58:14Z`; Detail returned `14:58:16Z`: visible still `12`, mapping `481`, trailing timeline/tools `6/6`. Existing authoritative-Detail projection started external response generation `1` with six tool items.
- Manual-Sync rearm loaded the target page. `14:58:17Z` `becomeFirstResponder()` returned true; `14:58:18Z` direct probe returned `documentHasFocus=true` with the page visible and complete.
- From focus acquisition until first background at `14:59:10Z` there were about 52 seconds of clean foreground. No matching page-owned `stream_status`, `/resume`, resume response, external streaming or external snapshot event occurred.
- The user directly observed the same remote generation on PC continue through multiple additional tool rounds after focus acquisition. ChatGPTClient remained on the six-tool snapshot and did not advance. This is the independent post-focus active/progress evidence missing from the earlier near-terminal b88 sample.
- User-socket frames remained `targetMatch=false` and provided no automatic acquisition trigger.
- Mid-run export at `15:00:16Z` still had no page-owned continuation/SSE event. Returning to the target conversation restored the resident live row; no newer authoritative Detail had been fetched.
- Final explicit Sync at `15:01:04Z` returned at `15:01:06Z` with visible `12 -> 13`, mapping `507`, trailing timeline/tools `0/0`. `liveResponse.externalDetailReconciled(reason=authoritative_assistant_materialized)` then cleared response generation `1` and exposed the completed assistant.
- A later rearm again produced `nativeFirstResponder=true` / `documentHasFocus=true` at `15:01:07Z`, after final materialization; it was not the source of completion acquisition.

## Classification

- First-responder activation: **Runtime Positive**.
- Covered `document.hasFocus=true`: **Runtime Positive**.
- Focus as a sufficient condition for official cross-platform continuation under the current programmatic full conversation load: **Rejected**.
- Page-owned continuation in this decisive sample: **Rejected**; remote tool progress continued while covered Web emitted zero status/resume/SSE/snapshot events.
- Automatic final convergence: **Rejected again**; the completed assistant required explicit Sync.
- Genuine official SPA/router conversation-entry transition: **next evidence target / causality Unverified**.
- Visible official Web server capability remains **Runtime Positive** from the separate known-good Web Rule Lab sample.

This result does not prove focus is universally irrelevant or unnecessary. It proves focus alone is not sufficient with the current covered executor's direct full `/c/<conversation>` navigation.

## Next evidence target

Investigate the smallest privacy-safe difference between a genuine user-driven official SPA/router conversation entry and the covered executor's programmatic full navigation. Do not synthesize Native `stream_status`/`resume` requests, guess offsets, poll, add timers/retries/watchdogs, use WebSocket bodies as content authority, duplicate Send, or create a second response store.
''')

# Update b88 row in Build/Test index.
index = root / 'docs/project/BUILD_TEST_INDEX.md'
ensure_nl(index)
text = index.read_text()
old = '| `DEV-send-stream-0.1.0-b88` | `DEV-send-stream` | `0.1.0 (88)` | exact focus-A/B product source `31d24e8b9ab4676effd757a793162abbdb0d7012`; clean package head `378811691ccbd6f44b232d8cc5564628e9b021e1`; PR #29 | guarded exact staging `33636270267` passed; Push `33636383827/100268195218` passed; PR `33636390081/100268217481` passed; canonical Artifact `9848999246`; ZIP `sha256:7ae1c816a9300825fc2d0c726a822278abbe1af20735f1310f0f27328617baa7`; IPA `sha256:cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`; package `0.1.0 (88)` / Candidate b88 / source `378811691ccb` / iOS14 / arm64 | Runtime Partial/Diagnostic Positive: manual-Sync rearm made WKWebView first responder and `document.hasFocus=true`; no page-owned continuation was observed, but the response was already at its final tool phase and active Detail proof preceded focus by only ~1s. Final assistant required a later explicit Sync | **Focus activation Runtime Positive; focus causality Inconclusive; automatic final convergence rejected in this run; permanently reserved** |'
new = '| `DEV-send-stream-0.1.0-b88` | `DEV-send-stream` | `0.1.0 (88)` | exact focus-A/B product source `31d24e8b9ab4676effd757a793162abbdb0d7012`; clean package head `378811691ccbd6f44b232d8cc5564628e9b021e1`; PR #29 | guarded exact staging `33636270267` passed; Push `33636383827/100268195218` passed; PR `33636390081/100268217481` passed; canonical Artifact `9848999246`; ZIP `sha256:7ae1c816a9300825fc2d0c726a822278abbe1af20735f1310f0f27328617baa7`; IPA `sha256:cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`; package `0.1.0 (88)` / Candidate b88 / source `378811691ccb` / iOS14 / arm64 | Runtime Diagnostic Positive / focus-sufficient Rejected: first-responder activation and `document.hasFocus=true` are proven. In a clean early/mid-generation sample the user observed multiple later PC tool rounds after focus while covered Web emitted zero `stream_status`, `/resume`, SSE or page-owned snapshot; final assistant still required explicit Sync | **Focus mechanism Runtime Positive; focus alone rejected as sufficient for continuation; automatic final convergence rejected; SPA/router entry is next Unverified differential; permanently reserved** |'
assert text.count(old) == 1, 'b88 row mismatch'
index.write_text(text.replace(old, new, 1))

prepend(root / 'docs/project/MODULE_STATUS.md', '# Module Status', '''## DEV-send-stream b88 decisive focus-negative override — 2026-09-02

- Exact b88 identity remains unchanged: product `31d24e8b9ab4676effd757a793162abbdb0d7012`, clean package head `378811691ccbd6f44b232d8cc5564628e9b021e1`, Candidate/Build `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`, Artifact `9848999246`, IPA `sha256:cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`.
- Second real-device b88 sample is decisive: manual-Sync rearm produced `nativeFirstResponder=true` and `documentHasFocus=true`; the user then observed multiple additional PC tool rounds from the same remote generation while ChatGPTClient stayed on the six-tool snapshot and covered Web emitted zero `stream_status`, `/resume`, external SSE or page-owned snapshot.
- Focus is therefore rejected as a **sufficient** condition for continuation under the current direct full conversation navigation. This does not prove focus is universally irrelevant.
- Completed assistant still required explicit Sync (`visible 12 -> 13`, mapping `507`, trailing `0/0`, `authoritative_assistant_materialized`). Automatic final convergence remains rejected.
- Next evidence target is genuine official SPA/router conversation-entry behavior; causality remains Unverified. No b89 until one exact router-entry variable is evidenced. Stable/Frozen Send remains No.''')

prepend(root / 'docs/project/TECHNICAL_DECISIONS.md', '# Technical Decisions', '''## b88 decisive focus-negative qualification — 2026-09-02

- The clean second b88 Runtime sample closes the focus A/B. Covered first-responder activation and `document.hasFocus=true` are Runtime Positive, but focus alone is **not sufficient** for official cross-platform continuation with the current programmatic full `/c/<conversation>` load.
- Evidence: authoritative Detail advanced to six tool items before focus; after focus the user directly observed multiple additional PC tool rounds from the same remote generation, while covered Web produced zero page-owned `stream_status`, `/resume`, external SSE or snapshot and Native remained on the six-tool live snapshot.
- Final materialization again required explicit Sync. Therefore neither focus nor the current generic user-socket structural frames provide reliable continuation/final convergence for this path.
- The remaining known-good differential is genuine official SPA/router conversation entry versus direct full navigation. Treat router causality as **Unverified** until a privacy-safe causal A/B identifies one exact variable. Do not jump directly to a router workaround from correlation alone.
- Existing boundaries remain: no Native protocol synthesis or guessed offsets, no polling/timers/retries/watchdogs, no duplicate Send, no WebSocket body authority, no second response store.''')

prepend(root / 'docs/project/WEB_SEND_ADAPTER.md', '# Web Send Adapter / Rule Update Playbook', '''## b88 decisive focus-negative continuation qualification — 2026-09-02

The second exact b88 real-device sample resolves the earlier near-terminal ambiguity. Manual-Sync rearm successfully made the covered WKWebView first responder and direct `document.hasFocus()` returned true. The same remote generation then visibly continued through multiple additional tool rounds on PC, but the covered page issued no matching `stream_status`, `/resume`, external SSE or page-owned snapshot and ChatGPTClient remained on the six-tool authoritative Detail snapshot.

Therefore **focus is rejected as a sufficient activation condition** for the current covered executor's direct full conversation navigation. This does not establish that focus is irrelevant to the known-good visible Web path; it only removes focus-alone as the missing variable.

The next maintenance target is the remaining differential: a genuine user-driven official SPA/router conversation-entry transition versus programmatic full `/c/<conversation>` load. Do not implement a router workaround until a privacy-safe experiment identifies the exact official transition behavior. The existing prohibitions on Native status/resume synthesis, offset guessing, polling, timers, retries/watchdogs, duplicate Send, WebSocket-body authority and second response stores remain in force.''')

for path in [index, root/'docs/project/MODULE_STATUS.md', root/'docs/project/TECHNICAL_DECISIONS.md', root/'docs/project/WEB_SEND_ADAPTER.md', evidence]:
    ensure_nl(path)
    assert path.read_text().endswith('\n')
