from pathlib import Path

root = Path('.')

def prepend_after_title(path: Path, title: str, section: str):
    text = path.read_text()
    anchor = title + '\n\n'
    assert text.startswith(anchor), f'{path}: title anchor mismatch'
    marker = section.splitlines()[0]
    assert marker not in text, f'{path}: section already present'
    path.write_text(anchor + section.rstrip() + '\n\n' + text[len(anchor):])

# Durable visible-Web A/B evidence.
evidence = root / 'docs/project/runtime-evidence/DEV-send-stream-visible-web-focus-sse-ab-20260902.md'
assert not evidence.exists(), 'evidence file already exists'
evidence.write_text('''# DEV-send-stream visible Web focus / cross-platform continuation A/B — 2026-09-02

## Evidence class

User-observed real-device Web Rule Lab Runtime evidence using the same `WKWebsiteDataStore.default()` browser login/session authority as production covered Web execution. This is a visible official-Web diagnostic sample, not b88 product Runtime.

## Known-good sample

The user started a new response on another official client, opened Web Rule Lab, visibly entered that active cross-platform conversation, and immediately observed the official Web UI continuing the in-progress response live. The composer control was already the active-response **Stop** control rather than Send, showing that the official page had acquired the active response lifecycle state.

The privacy-safe page probe returned:

```json
{
  "hasFocus": true,
  "hidden": false,
  "readyState": "complete",
  "route": "other",
  "visibilityState": "visible"
}
```

The screenshot and user observation establish that the visible page was inside the active target conversation despite the coarse probe returning `route=other`. Therefore the current `^/c/` route classifier is too narrow for current official-Web navigation shapes and must not be treated as conversation-state authority.

## Differential against b87 covered production

Exact b87 covered Runtime had the target page attached to the key window, structurally visible, loaded and geometrically valid, but `document.hasFocus=false` throughout and produced zero page-owned `stream_status`, `/resume`, snapshots or SSE for approximately 161 seconds foreground.

This visible-Web sample supplies the missing known-good differential:

- visible official Web: `document.hasFocus=true` + immediate live cross-platform continuation + active Stop state;
- covered b87 Web: `document.hasFocus=false` + no continuation.

This supports the user's earlier hypothesis that server-side cross-platform continuation capability itself is not the fundamental blocker for this account/session path.

## Causality boundary

Focus is **not yet proven causal** because the known-good visible sample also included a genuine user-driven SPA/router conversation-entry transition. The evidence authorizes a one-variable causal A/B only: keep the production programmatic target load unchanged and test whether making the covered WKWebView first responder changes `document.hasFocus` and official page-owned continuation behavior.

It does not authorize Native construction of `stream_status`, `/resume`, offset, polling, retries, timers, watchdogs, duplicate Send, WebSocket-body authority, a second response store, or an SPA/router workaround in the same candidate.

## Resulting candidate

`DEV-send-stream-0.1.0-b88` is the focus-only causal A/B. Code/CI/Artifact/package are separately verified; real-device b88 Runtime remains Pending.
''')

# Candidate index row.
index = root / 'docs/project/BUILD_TEST_INDEX.md'
text = index.read_text()
anchor = '| `DEV-send-stream-0.1.0-b87` |'
assert text.count(anchor) == 1, 'b87 row anchor mismatch'
assert 'DEV-send-stream-0.1.0-b88' not in text, 'b88 already indexed'
row = '| `DEV-send-stream-0.1.0-b88` | `DEV-send-stream` | `0.1.0 (88)` | exact focus-A/B product source `31d24e8b9ab4676effd757a793162abbdb0d7012`; clean package head `378811691ccbd6f44b232d8cc5564628e9b021e1`; PR #29 | guarded exact staging `33636270267` passed; Push `33636383827/100268195218` passed; PR `33636390081/100268217481` passed; canonical Artifact `9848999246`; ZIP `sha256:7ae1c816a9300825fc2d0c726a822278abbe1af20735f1310f0f27328617baa7`; IPA `sha256:cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`; package `0.1.0 (88)` / Candidate b88 / source `378811691ccb` / iOS14 / arm64 | Runtime Pending: one-shot manual-Sync rearm first-responder A/B; determine whether covered `document.hasFocus` becomes true and official page-owned continuation begins | **Code/guarded staging/Push+PR CI/Artifact/package verified; Runtime Pending; permanently reserved** |\n'
text = text.replace(anchor, row + anchor, 1)
index.write_text(text)

prepend_after_title(root / 'docs/project/MODULE_STATUS.md', '# Module Status', '''## DEV-send-stream b88 focus-causality candidate override — 2026-09-02

- Known-good visible Web Rule Lab Runtime: user visibly entered a newly active cross-platform conversation and immediately observed live continuation with the composer already in Stop state; privacy-safe probe was `visibilityState=visible`, `hidden=false`, `readyState=complete`, `document.hasFocus=true`.
- The same visible sample returned coarse `route=other` despite visibly being in the active conversation; the current `^/c/` route-shape probe is diagnostic-only and is not conversation-state authority.
- Differential against b87: covered target page was visible/loaded/attached but remained `document.hasFocus=false` and never started page-owned continuation during ~161 seconds foreground.
- b88 identity: exact product source `31d24e8b9ab4676effd757a793162abbdb0d7012`; clean package head `378811691ccbd6f44b232d8cc5564628e9b021e1`; Candidate/Build `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`; Push+PR CI passed; Artifact `9848999246`; IPA `sha256:cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`.
- b88 changes one variable only: explicit manual-Sync rearm attempts `WKWebView.becomeFirstResponder()` once after target load and logs Native + `document.hasFocus` results. The programmatic target load remains unchanged and Web interaction remains disabled.
- b88 does not issue `stream_status`, `/resume`, offsets, polling/timers/retries/watchdogs, duplicate Send, router workarounds or a second response store. Runtime/manual/real-device remains Pending; Stable/Frozen Send remains No.''')

prepend_after_title(root / 'docs/project/TECHNICAL_DECISIONS.md', '# Technical Decisions', '''## b88 visible-Web focus differential / causal A-B qualification — 2026-09-02

- A current known-good visible official-Web sample using the same default persistent WebKit store immediately acquired a newly active cross-platform response: live continuation was visible and the composer was already in Stop state. The page probe reported `visible`, `hidden=false`, `complete`, `document.hasFocus=true`.
- This directly contrasts with exact b87 covered production, which was visible/loaded/attached but stayed `document.hasFocus=false` and never started official continuation during ~161 seconds foreground.
- Focus remains a correlation, not a proven cause, because the visible sample also included a genuine user-driven SPA/router conversation-entry transition. b88 is authorized only as a one-variable causal test: keep the covered programmatic target load unchanged and attempt first-responder activation once after explicit manual-Sync rearm.
- The visible sample's `route=other` despite visibly being inside the active conversation proves the current coarse `^/c/` route classifier is not authoritative for conversation state.
- b88 must not combine focus testing with Web interaction enablement, router emulation, Native `stream_status`/`resume`/offset construction, polling, timers, retries/watchdogs, duplicate Send or a second state owner. `/resume` offset remains downstream until official page-owned continuation actually starts.''')

prepend_after_title(root / 'docs/project/WEB_SEND_ADAPTER.md', '# Web Send Adapter / Rule Update Playbook', '''## b88 visible-Web continuation activation qualification — 2026-09-02

Current visible Web Rule Lab evidence establishes a known-good cross-platform continuation case on the same `WKWebsiteDataStore.default()` authority used by the covered executor. When the user visibly entered a newly active remote conversation, the official Web UI immediately continued the response live and already showed the active-response Stop control. A privacy-safe probe returned `visibilityState=visible`, `hidden=false`, `readyState=complete`, `document.hasFocus=true`.

The same page returned coarse `route=other` even though screenshot/user observation established that it was visibly inside the active conversation. Therefore the current `^/c/` route-shape classifier is only a diagnostic hint and must not be used as conversation-state authority.

Exact b87 provides the negative counterpart: the covered target page was visible/loaded/attached but continuously `document.hasFocus=false` and never emitted page-owned `stream_status`, `/resume`, snapshot or SSE during ~161 seconds foreground. This makes focus/activation an evidence-backed causal A/B target, but not a proven production rule because the known-good visible sample also involved genuine SPA/router entry.

b88 may vary only Native first-responder activation after explicit manual-Sync rearm while keeping the existing programmatic target load unchanged. It must not synthesize protocol requests, guess offsets, poll, retry, add timers/watchdogs, enable a router workaround, use WebSocket bodies as response authority or create another response store.''')

# Basic safeguards.
for path in [index, root/'docs/project/MODULE_STATUS.md', root/'docs/project/TECHNICAL_DECISIONS.md', root/'docs/project/WEB_SEND_ADAPTER.md', evidence]:
    assert path.read_text().endswith('\n'), f'{path}: missing final newline'
