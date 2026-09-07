from pathlib import Path


def prepend(path: str, marker: str, block: str) -> None:
    p = Path(path)
    text = p.read_text()
    if marker in text:
        raise SystemExit(f"marker already present: {marker}")
    p.write_text(block.strip() + "\n\n" + text)


checkpoint = r'''## b102 deterministic client-owned WebContent-death probe — package-ready 2026-09-05

Exact evidence:

- Candidate `DEV-send-stream-0.1.0-b102` / `0.1.0 (102)`, permanently reserved. This is a **diagnostic-only** candidate requested to make hard covered-Web death reproducible; it does not add client-owned response recovery.
- Exact product head `670310b4e8b15176f721291f4f96e46feadec46a`; canonical package source `78bd3d2f3e45c8e0061865d3133b92a274139110`. Relative to the verified pre-allocation head, product scope is exactly Xcode Build/Candidate + `AppDelegate.swift` installer + new `Protocol/CoveredWebProcessKillProbe.swift`; the package-source child changes only `ios-foundation.yml`.
- Probe behavior: only exact b102 installs a runtime interception of `WKWebView.evaluateJavaScript`; the first script containing the fixed `window.__coveredWebSendExecutor.submit(` marker arms one 120-second main-queue diagnostic action without logging prompt/script content. At fire it invokes `_killWebContentProcessAndResetState` only when that exact `WKWebView` responds to the selector. No Send/retry/resume API exists in the probe.
- Push `33910845721 / 101146639944` and PR `33910858535 / 101146674919` passed guard + unsigned TrollStore build. Canonical Push Artifact `9951331101`, ZIP `sha256:2da6bb66d0c5eba55d93463881e0ff5d0d55a9d7844f068d024e5cee31dff24a`. Same-source PR Artifact `9951329921` is CI corroboration only.
- Canonical IPA `ChatGPTClient-0.1.0-b102-dev-send-stream.ipa`, independently recomputed `sha256:53eb1845a3fbd4543ebdb5e9a69e078b3f07866c2c395a666dca9b2928ecd8af`, matching sidecar.
- Independent package inspection confirms `com.whitesharkssw.chatgptclient`, `0.1.0 (102)`, Candidate b102, source marker `78bd3d2f3e45`, Release, iOS14 minimum, UIDeviceFamily `[1,2]`, iPhoneOS, Mach-O arm64. Binary strings contain the exact b102 Candidate, `coveredExecutor.killProbe` and `_killWebContentProcessAndResetState`.

Evidence ladder: **Code written / exact diagnostic scope audited / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**

**Next exact action:** install only canonical b102. Fresh-launch the app, choose an existing conversation, start exactly one deliberately >2-minute Native `测试发送…` response and keep the app foreground. Do not press Sync/Reload/Stop and do not send a second prompt. Expect `coveredExecutor.killProbe` `installed -> armed -> firing` at ~120s, followed by `coveredExecutor.webProcess state=terminated mode=client_send_or_idle` while the response is still active. Current product behavior is expected to mark that client-owned live response failed and release the executor; let the server-side generation finish, then export diagnostics. If the response finishes before `firing`, the run does not qualify and must be repeated with a longer response. Do not interpret this diagnostic timer as production timeout/retry policy.'''

state = r'''## DEV-send-stream b102 deterministic hard-Web kill probe package ready — 2026-09-05

- User explicitly authorized a deterministic two-minute forced-Web test because natural `WKWebView` WebContent termination is difficult to reproduce. b102 is diagnostic instrumentation only; current client-owned WebContent-death failure semantics are intentionally unchanged until Runtime proves the server/Native outcome.
- Exact product `670310b4e8b15176f721291f4f96e46feadec46a`; package source `78bd3d2f3e45c8e0061865d3133b92a274139110`; Push `33910845721/101146639944`; PR `33910858535/101146674919`; canonical Artifact `9951331101`; ZIP `sha256:2da6bb66d0c5eba55d93463881e0ff5d0d55a9d7844f068d024e5cee31dff24a`; IPA `sha256:53eb1845a3fbd4543ebdb5e9a69e078b3f07866c2c395a666dca9b2928ecd8af`.
- The first covered protected-Send submit in exact b102 arms one 120s action on that `WKWebView`; it calls WebKit `_killWebContentProcessAndResetState` only if available. It adds no resend/regenerate, no retry, no Native resume/status, no background keepalive and no second response/content authority.
- Human Runtime pending. b101 exact `-1005` transport renewal remains separately Unexercised; b102 does not supersede or claim it. Stable-Frozen No.
'''

profile = r'''## Latest DEV-send-stream candidate override — b102 2026-09-05

- Latest Human Runtime candidate: `DEV-send-stream-0.1.0-b102` / `0.1.0 (102)`, permanently reserved. It is a test-only deterministic WebContent-death probe, not a production recovery change.
- One exact b102 covered protected-Send submit arms one 120-second action that kills only that covered `WKWebView` WebContent process through runtime-dispatched `_killWebContentProcessAndResetState`; prompt/script content is not logged. Existing client-owned Web death still fails normally and never resends.
- Exact product `670310b4e8b15176f721291f4f96e46feadec46a`; package source `78bd3d2f3e45c8e0061865d3133b92a274139110`; Artifact `9951331101`; IPA `sha256:53eb1845a3fbd4543ebdb5e9a69e078b3f07866c2c395a666dca9b2928ecd8af`; package identity verified; Human Runtime pending; Stable/Frozen No.
'''

module = r'''## DEV-send-stream b102 deterministic client-owned WebContent-death probe — 2026-09-05

- `ConversationRepository` remains sole Native response/content owner and `CoveredWebSendExecutor` remains the protected-Send Web transport. b102 adds no recovery owner or alternate transport.
- Exact b102 installs one Candidate-gated diagnostic probe: first covered submit arms one 120-second main-queue action and then requests WebKit to kill/reset only that covered WebContent process. Current `webViewWebContentProcessDidTerminate` handling is intentionally unchanged: external observation may rebootstrap under b98, while client-owned Send still fails and is never replayed.
- Push+PR CI passed; canonical Artifact `9951331101`; IPA `sha256:53eb1845a3fbd4543ebdb5e9a69e078b3f07866c2c395a666dca9b2928ecd8af`; Human Runtime pending. Module remains Active / Runtime Partial / Stable-Frozen No.
'''

technical = r'''## DEV-send-stream b102 deterministic WebContent-death diagnostic decision — 2026-09-05

- Natural hard WebContent death is too intermittent to be an efficient acceptance gate, while exact `webViewWebContentProcessDidTerminate` remains the only approved hard-disconnect signal. The user explicitly authorizes one deterministic 120-second forced-kill diagnostic candidate to exercise that signal.
- The timer is an instrumentation trigger only: exact b102 arms once from the existing covered protected-Send submit invocation and kills that exact `WKWebView` through runtime-dispatched WebKit `_killWebContentProcessAndResetState`. It is not a response timeout, watchdog, retry, keepalive or production scheduler.
- b102 intentionally does **not** change client-owned recovery. A hard death while client-owned Send/response is active still follows the existing `.failed(web_process_terminated)` path and never resends/replays/regenerates. Runtime must first establish whether server generation continues and which existing authoritative/page-owned recovery primitive is sufficient.
- b101 Native `-1005` read renewal, b100/b97 foreground Detail convergence, b98 external-observation hard-death recovery, TD-029 protected-Send ownership and one-Send invariants remain unchanged.
'''

rules = r'''## Deterministic covered-Web kill probe — b102 test-only 2026-09-05

- The b102 120-second `WKWebView` kill is allowed **only** as Candidate-gated Human Runtime instrumentation for the explicit client-owned WebContent-death test. Never carry this timer into a later normal product candidate or treat elapsed time as disconnect evidence.
- Arm once from the existing covered protected-Send submit marker; do not read/log prompt or script body. Kill only the exact observed `WKWebView`, only through `_killWebContentProcessAndResetState` when `responds(to:)` succeeds.
- The probe must not call protected Send, resume, status, Sync, Reload, retry, regenerate or any response API. Current client-owned death failure semantics remain unchanged during b102 so Runtime evidence is causal.
- A qualifying run requires the client-owned response still active when `coveredExecutor.killProbe state=firing` occurs. If the answer already completed, an idle Web kill is not evidence for active-response death recovery.
'''

prepend('docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md', '## b102 deterministic client-owned WebContent-death probe — package-ready 2026-09-05', checkpoint)
prepend('docs/project/PROJECT_STATE.md', '## DEV-send-stream b102 deterministic hard-Web kill probe package ready — 2026-09-05', state)
prepend('docs/project/PROJECT_PROFILE.md', '## Latest DEV-send-stream candidate override — b102 2026-09-05', profile)
prepend('docs/project/MODULE_STATUS.md', '## DEV-send-stream b102 deterministic client-owned WebContent-death probe — 2026-09-05', module)
prepend('docs/project/TECHNICAL_DECISIONS.md', '## DEV-send-stream b102 deterministic WebContent-death diagnostic decision — 2026-09-05', technical)
prepend('docs/project/PROJECT_SPECIFIC_RULES.md', '## Deterministic covered-Web kill probe — b102 test-only 2026-09-05', rules)

index = Path('docs/project/BUILD_TEST_INDEX.md')
lines = index.read_text().splitlines()
if any(line.startswith('| `DEV-send-stream-0.1.0-b102` |') for line in lines):
    raise SystemExit('b102 row already present')
row = '| `DEV-send-stream-0.1.0-b102` | `DEV-send-stream` | `0.1.0 (102)` | deterministic client-owned covered-Web kill probe product `670310b4e8b15176f721291f4f96e46feadec46a`; package `78bd3d2f3e45c8e0061865d3133b92a274139110`; PR #29 | Push `33910845721/101146639944` passed; PR `33910858535/101146674919` passed; canonical Artifact `9951331101`; ZIP `2da6bb66d0c5eba55d93463881e0ff5d0d55a9d7844f068d024e5cee31dff24a`; IPA `53eb1845a3fbd4543ebdb5e9a69e078b3f07866c2c395a666dca9b2928ecd8af`; b102/source/iOS14/[1,2]/arm64 verified | Human Runtime pending: one deliberately >2m client-owned protected Send; exact b102 arms a single 120s forced WebContent kill, then observe `webProcess terminated` and current no-resend failure/server continuation outcome. If response completes before kill, gate Unexercised | **Diagnostic Code written / Push+PR CI passed / Artifact produced / package identity verified / Runtime pending / no client-owned recovery change / Stable-Frozen No; permanently reserved** |'
separator = next(i for i, line in enumerate(lines) if line.startswith('|---|---|---|---|---|---|---|'))
lines.insert(separator + 1, row)
index.write_text('\n'.join(lines) + '\n')
