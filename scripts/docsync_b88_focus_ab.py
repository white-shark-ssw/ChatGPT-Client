from pathlib import Path

root = Path('.')

def ensure_final_newline(path: Path):
    text = path.read_text()
    if not text.endswith('\n'):
        path.write_text(text + '\n')

def prepend_after_title(path: Path, title: str, section: str):
    ensure_final_newline(path)
    text = path.read_text()
    anchor = title + '\n\n'
    assert text.startswith(anchor), f'{path}: title anchor mismatch'
    marker = section.splitlines()[0]
    assert marker not in text, f'{path}: section already present'
    path.write_text(anchor + section.rstrip() + '\n\n' + text[len(anchor):])

visible_evidence = root / 'docs/project/runtime-evidence/DEV-send-stream-visible-web-focus-sse-ab-20260902.md'
assert not visible_evidence.exists(), 'visible Web evidence already exists'
visible_evidence.write_text('''# DEV-send-stream visible Web focus / cross-platform continuation A/B — 2026-09-02

## Evidence class

User-observed real-device Web Rule Lab Runtime evidence using the same `WKWebsiteDataStore.default()` browser login/session authority as production covered Web execution. This is a visible official-Web diagnostic sample, not b88 product Runtime.

## Known-good sample

The user started a new response on another official client, opened Web Rule Lab, visibly entered that active cross-platform conversation, and immediately observed the official Web UI continuing the in-progress response live. The composer control was already the active-response **Stop** control rather than Send, showing that the official page had acquired the active response lifecycle state.

The privacy-safe page probe returned `visibilityState=visible`, `hidden=false`, `readyState=complete`, `document.hasFocus=true`. The coarse probe returned `route=other`, but screenshot/user observation proves the page was visibly inside the target conversation, so the current `^/c/` classifier is diagnostic-only and is not conversation-state authority.

Exact b87 supplies the negative counterpart: covered production was visible/loaded/attached but stayed `document.hasFocus=false` and produced zero page-owned continuation for about 161 seconds foreground.

Focus remained correlation rather than causality because the known-good visible sample also included a genuine user-driven SPA/router conversation-entry transition. This evidence authorized b88 as a one-variable first-responder A/B only; it did not authorize Native request synthesis, offset guessing, polling, timers, retries/watchdogs, duplicate Send, WebSocket-body authority or a second response store.
''')

runtime_evidence = root / 'docs/project/runtime-evidence/DEV-send-stream-b88-focus-positive-near-terminal-inconclusive-20260902.md'
assert not runtime_evidence.exists(), 'b88 runtime evidence already exists'
runtime_evidence.write_text('''# DEV-send-stream b88 focus-positive near-terminal Runtime — 2026-09-02

## Identity

- Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- Exact product source: `31d24e8b9ab4676effd757a793162abbdb0d7012`
- Clean package head / diagnostics source: `378811691ccbd6f44b232d8cc5564628e9b021e1` / `378811691ccb`
- Canonical Artifact: `9848999246`
- IPA SHA-256: `cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`
- Device: iPhone / iOS17.0
- Uploaded diagnostics: `ChatGPTClient-Diagnostics-20260902-144605.json`

## Runtime timeline

- Selection covered page loaded visible/complete on the target conversation but initially had `document.hasFocus=false`.
- `14:44:25Z` authoritative Detail: visible `10`, mapping `450`, trailing timeline/tools `24/24`.
- Explicit Sync returned at `14:44:36Z`: visible still `10`, mapping `452`, trailing timeline/tools `25/25`. The remote turn had advanced one additional tool and no final assistant had materialized at that authoritative fetch.
- Existing Detail projection started response generation `1` with `25` timeline/tool items.
- Manual-Sync re-arm completed at `14:44:37Z`; `WKWebView.becomeFirstResponder()` returned true, page emitted a focus event with `hasFocus=true`, and direct evaluation returned `documentHasFocus=true`.
- From focus acquisition until the user's second explicit Sync at `14:46:00Z` (~83 seconds), no matching `stream_status`, `/resume`, resume response, external streaming or external snapshot event appeared. User-socket messages remained `targetMatch=false`.
- A memory warning did not evict the protected resident and no WebContent-process termination was recorded.
- Second explicit Sync returned at `14:46:02Z`: visible messages `10 -> 11`, mapping `465`, trailing timeline/tools `0/0`; `externalDetailReconciled(reason=authoritative_assistant_materialized)` correctly cleared the live row.

## Classification

- First-responder activation mechanism: **Runtime Positive**.
- Covered `document.hasFocus=true`: **Runtime Positive**.
- Automatic page-owned continuation after focus: **Not observed in this run**.
- Automatic final convergence: **Rejected in this run**; final materialization required another explicit Sync.
- Focus causality: **Inconclusive**, not Rejected. The user reports entering at the final tool call, and the last authoritative proof of active generation at `14:44:36Z` preceded actual focus acquisition at `14:44:37Z` by only about one second. The response may have completed in that narrow interval, so this sample cannot prove that focus is insufficient.
- SPA/router causality: **Unverified**.

## Next gate

Reuse the exact canonical b88 IPA. Start a deliberately long remote response and enter while it is clearly early or mid-generation. Press Sync once, keep ChatGPTClient foregrounded for 30–60 seconds without another Sync, then export diagnostics. Do not allocate b89 or change product code until that clean focus A/B is collected.
''')

index = root / 'docs/project/BUILD_TEST_INDEX.md'
ensure_final_newline(index)
text = index.read_text()
anchor = '| `DEV-send-stream-0.1.0-b87` |'
assert text.count(anchor) == 1, 'b87 row anchor mismatch'
assert 'DEV-send-stream-0.1.0-b88' not in text, 'b88 already indexed'
row = '| `DEV-send-stream-0.1.0-b88` | `DEV-send-stream` | `0.1.0 (88)` | exact focus-A/B product source `31d24e8b9ab4676effd757a793162abbdb0d7012`; clean package head `378811691ccbd6f44b232d8cc5564628e9b021e1`; PR #29 | guarded exact staging `33636270267` passed; Push `33636383827/100268195218` passed; PR `33636390081/100268217481` passed; canonical Artifact `9848999246`; ZIP `sha256:7ae1c816a9300825fc2d0c726a822278abbe1af20735f1310f0f27328617baa7`; IPA `sha256:cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`; package `0.1.0 (88)` / Candidate b88 / source `378811691ccb` / iOS14 / arm64 | Runtime Partial/Diagnostic Positive: manual-Sync rearm made WKWebView first responder and `document.hasFocus=true`; no page-owned continuation was observed, but the response was already at its final tool phase and active Detail proof preceded focus by only ~1s. Final assistant required a later explicit Sync | **Focus activation Runtime Positive; focus causality Inconclusive; automatic final convergence rejected in this run; permanently reserved** |\n'
index.write_text(text.replace(anchor, row + anchor, 1))

prepend_after_title(root / 'docs/project/MODULE_STATUS.md', '# Module Status', '''## DEV-send-stream b88 focus Runtime override — 2026-09-02

- Known-good visible official Web can immediately acquire/live-continue a newly active cross-platform response and shows Stop while `document.hasFocus=true`; the coarse route probe is not conversation-state authority.
- b88 identity: exact product source `31d24e8b9ab4676effd757a793162abbdb0d7012`; clean package head `378811691ccbd6f44b232d8cc5564628e9b021e1`; Candidate/Build `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`; Push+PR CI passed; Artifact `9848999246`; IPA `sha256:cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`.
- Exact b88 Runtime proves the one-shot focus mechanism works: `nativeFirstResponder=true` and direct `documentHasFocus=true` after manual-Sync rearm.
- No `stream_status`, `/resume`, external streaming or snapshot followed in the supplied run, and final materialization still required another explicit Sync. However the response was already at the final tool phase; the last authoritative active Detail proof preceded focus by only ~1 second, so focus causality remains Inconclusive rather than Rejected.
- Reuse exact b88 for one earlier/mid-generation A/B. No b89/product change yet. Stable/Frozen Send remains No.''')

prepend_after_title(root / 'docs/project/TECHNICAL_DECISIONS.md', '# Technical Decisions', '''## b88 focus Runtime qualification — 2026-09-02

- b88 real-device Runtime proves covered first-responder activation is technically effective: manual-Sync rearm produced `nativeFirstResponder=true`, a page focus event, and direct `document.hasFocus=true`.
- The same run produced no official page-owned continuation traffic and final materialization still required a later explicit Sync. This is not yet sufficient to reject focus because the user entered at the final tool call and authoritative active Detail at `14:44:36Z` preceded focus at `14:44:37Z` by only about one second.
- Therefore focus causality remains **Inconclusive**. Do not promote SPA/router entry as causal yet and do not allocate b89. Repeat exact b88 earlier in a long remote generation.
- The visible-Web known-good sample remains valid: current official Web can acquire/live-continue cross-platform active responses under the same persistent WebKit session authority. The remaining problem is covered-page activation/entry behavior, not server capability or Repository response ownership.
- Existing prohibitions remain: no Native `stream_status`/`resume`/offset construction, polling, timers, retries/watchdogs, duplicate Send, WebSocket body authority or second response store.''')

prepend_after_title(root / 'docs/project/WEB_SEND_ADAPTER.md', '# Web Send Adapter / Rule Update Playbook', '''## b88 focus activation Runtime qualification — 2026-09-02

A known-good visible Web Rule Lab sample on the same `WKWebsiteDataStore.default()` authority immediately acquired/live-continued a newly active cross-platform response and showed the active Stop control while `document.hasFocus=true`. Its coarse `route=other` result confirms route shape is diagnostic-only.

Exact b88 then changed only first-responder activation after manual-Sync rearm. Real-device Runtime produced `nativeFirstResponder=true` and direct `document.hasFocus=true`, proving the covered page can obtain focus without enabling Web interaction or changing the programmatic target load.

No page-owned `stream_status`, `/resume`, external streaming or snapshot followed in that run; final authoritative materialization required another explicit Sync. Do **not** yet conclude that focus is insufficient: the target was already at its final tool call, and the last authoritative proof that the generation was active preceded focus by only ~1 second. Repeat exact b88 earlier in a long generation before moving to SPA/router entry work.

This evidence still does not authorize Native protocol synthesis, guessed offsets, polling, timers, retries/watchdogs, duplicate Send, WebSocket-body authority or a second response store.''')

for path in [index, root/'docs/project/MODULE_STATUS.md', root/'docs/project/TECHNICAL_DECISIONS.md', root/'docs/project/WEB_SEND_ADAPTER.md', visible_evidence, runtime_evidence]:
    ensure_final_newline(path)
    assert path.read_text().endswith('\n'), f'{path}: missing final newline'
