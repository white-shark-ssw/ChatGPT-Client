from pathlib import Path

block = '''## DEV-send-stream b91 project live-continuation Runtime Positive override — 2026-09-03

- Exact b91 Runtime on iPhone / iOS 17.0 matches Candidate `DEV-send-stream-0.1.0-b91`, Build 91, source marker `c5985f1e2e5d`.
- Project route identity is Runtime Positive: every recorded `coveredExecutor.pageActivation` remained `route=conversation`; the prior scoped-project degradation to `route=other` did not recur.
- After one explicit Sync established the active authoritative response, the official page itself issued matching `stream_status`; HTTP200 repeatedly returned `IS_STREAMING`, `externalStreamingObserved` fired, and the page-owned `/resume` offset 0 returned HTTP404 JSON before the already-existing page-owned read path continued via `stream_status` plus plural conversation snapshots.
- Web -> bridge -> `ConversationRepository` live progression is Runtime Positive without a second manual Sync: external snapshots advanced from service messages/tools `6 / 2` to `47 / 14`, while reasoning characters advanced `194 -> 909`; Native live presentation was repeatedly applied.
- The user-visible inability to return from the official Web page is explained by the intentionally retained b90 diagnostic `bringSubviewToFront(webView)`. It is a presentation artifact, not a continuation failure; source has no balancing send-to-back in that diagnostic path.
- The app was force-quit/relaunched while the response still reported `IS_STREAMING` and `finalCharacters=0`, so automatic terminal/final convergence remains Unverified in this run.
- Evidence ladder: **Code/guarded scope+Simulator/Push+PR CI/Artifact/package verified; project route identity Runtime Positive; page-owned live continuation Runtime Positive; Native progressive projection Runtime Positive; terminal/final Unverified; Stable-Frozen No.**
- Next exact product action: retain b91 route parser and continuation observation, remove only the b90 frontmost diagnostic so the executor remains covered, then validate live progression plus natural terminal/final completion. Do not add retry/polling/timer/watchdog/Native resume or status synthesis.

'''

for name in [
    'docs/project/PROJECT_STATE.md',
    'docs/project/MODULE_STATUS.md',
    'docs/project/DEVELOPMENT_PLAN.md',
    'docs/project/WEB_SEND_ADAPTER.md',
    'docs/project/TECHNICAL_DECISIONS.md',
]:
    p = Path(name)
    text = p.read_text()
    marker = block.splitlines()[0]
    if marker in text:
        continue
    pos = text.find('\n\n')
    if pos < 0:
        raise SystemExit(f'no top heading separator: {name}')
    p.write_text(text[:pos + 2] + block + text[pos + 2:])

idx = Path('docs/project/BUILD_TEST_INDEX.md')
text = idx.read_text()
old = '| `DEV-send-stream-0.1.0-b91` | `DEV-send-stream` | `0.1.0 (91)` | exact scoped-route identity parser product `cdab4e091683dc179753ed114c9ab5993a6c2d24`; exact product/config package source `c5985f1e2e5daec7bbc0a011ed70a8dd80904f7c`; PR #29 | staging `33746622538/100620460993` exact guard+scope+Simulator passed; Push `33746881658/100621278207` passed; PR `33746886896/100621297087` passed; canonical Push Artifact `9890000591`; Artifact `sha256:6062b02f9f1332744816d01a58e13c1a8c82017ee50828051f014ef79b943350`; IPA `sha256:abbd27370665fb97dd1ee5edd239c0a5fa1ea0694cbb329a81c32ee86867c140`; package `0.1.0 (91)` / Candidate b91 / source `c5985f1e2e5d` / iOS14 / `[1,2]` / arm64 | Runtime pending: project `/g/{scope}/c/{id}` must remain target-recognized after canonicalization; test existing page-owned status/resume/snapshot continuation without changing transport ownership | **Code/guarded scope+Simulator/Push+PR CI/Artifact/package verified; Runtime Unverified; Stable-Frozen No; permanently reserved** |'
new = '| `DEV-send-stream-0.1.0-b91` | `DEV-send-stream` | `0.1.0 (91)` | exact scoped-route identity parser product `cdab4e091683dc179753ed114c9ab5993a6c2d24`; exact product/config package source `c5985f1e2e5daec7bbc0a011ed70a8dd80904f7c`; PR #29 | staging `33746622538/100620460993` exact guard+scope+Simulator passed; Push `33746881658/100621278207` passed; PR `33746886896/100621297087` passed; canonical Push Artifact `9890000591`; Artifact `sha256:6062b02f9f1332744816d01a58e13c1a8c82017ee50828051f014ef79b943350`; IPA `sha256:abbd27370665fb97dd1ee5edd239c0a5fa1ea0694cbb329a81c32ee86867c140`; package `0.1.0 (91)` / Candidate b91 / source `c5985f1e2e5d` / iOS14 / `[1,2]` / arm64 | **Runtime Positive for project live continuation:** route stayed `conversation`; page-owned `stream_status` returned `IS_STREAMING`; `externalStreamingObserved` and plural snapshots advanced service messages/tools `6/2 -> 47/14` without second Sync. Frontmost Web cannot return because b90 diagnostic remains; run ended by force-quit while streaming, so terminal/final remains Unverified | **Route identity + page-owned live continuation + Native progressive projection Runtime Positive; terminal/final Unverified; Stable-Frozen No; permanently reserved** |'
if old not in text:
    raise SystemExit('b91 build-index row marker missing')
idx.write_text(text.replace(old, new, 1))

cp = Path('docs/project/current/dev/DEV-send-stream.md')
text = cp.read_text()
old_status = '**Active — b90 frontmost presentation is Runtime Positive as a mechanism, but project-specific source/Runtime correlation proves the old bridge loses conversation identity after official `/g/{scope}/c/{conversation}` canonicalization. Exact b91 fixes only that scoped-route identity parser and is Code/guarded scope+Simulator/Push+PR CI/Artifact/package verified; Human Runtime is pending. Stable/Frozen Send remains No.**'
new_status = '**Active — exact b91 project route identity and official page-owned live continuation are Runtime Positive on iPhone/iOS17. Web -> bridge -> `ConversationRepository` progressive projection works without a second Sync. The remaining visible Web-page trap is the intentionally retained b90 `bringSubviewToFront` diagnostic, not a transport failure. Automatic terminal/final convergence remains Unverified because the app was force-quit while still streaming. Stable/Frozen Send remains No.**'
if old_status not in text:
    raise SystemExit('checkpoint status marker missing')
text = text.replace(old_status, new_status, 1)
runtime_block = '''## b91 Human Runtime result — 2026-09-03\n\nExact b91 Runtime is decisive for live continuation. Metadata matches Candidate b91 / Build 91 / source `c5985f1e2e5d`. After one explicit Sync established response generation 1, the official project page remained `route=conversation`, issued matching page-owned `stream_status`, repeatedly returned HTTP200 `IS_STREAMING`, emitted `externalStreamingObserved`, and continued after its own `/resume` offset 0 returned HTTP404 through the already-observed page-owned `stream_status` + plural conversation read path.\n\nNative live state advanced automatically without another Sync: service messages/tools `6 / 2 -> 47 / 14`, reasoning characters `194 -> 909`, with repeated `externalSnapshot`, `liveResponse.externalSnapshot` and `liveResponse.presentationApplied`. Therefore the scoped-route parser and existing page-owned live continuation path are Runtime Positive.\n\nThe user could not return from the visible official Web because b91 intentionally retains b90's `hostView.bringSubviewToFront(webView)` diagnostic. That line changes z-order and has no balancing send-to-back in the rearm path; it is now a confirmed diagnostic presentation artifact.\n\nThe run does **not** validate automatic terminal/final convergence: the last pre-exit status was still `IS_STREAMING`, last snapshot had `finalCharacters=0`, then the app was force-quit/relaunched.\n\n'''
anchor = '## Validation / identity state\n'
if runtime_block.splitlines()[0] not in text:
    pos = text.find(anchor)
    if pos < 0:
        raise SystemExit('checkpoint validation anchor missing')
    text = text[:pos] + runtime_block + text[pos:]
old_batch = '**Closed for b91 product/package/docs preparation. Next exact action:** install exact b91 and perform the project-scoped Human Runtime gate. No product/config change is permitted before that Runtime evidence.'
new_batch = '**Closed for b91 Runtime evidence. Next exact action:** allocate the next unique candidate for one isolated presentation cleanup only: retain b91 scoped-route parsing and page-owned continuation, remove b90 `bringSubviewToFront(webView)` so the executor stays covered, then run project live + natural terminal/final Runtime. No retry/polling/timer/watchdog/Native status or resume synthesis.'
if old_batch not in text:
    raise SystemExit('checkpoint batch marker missing')
cp.write_text(text.replace(old_batch, new_batch, 1))
