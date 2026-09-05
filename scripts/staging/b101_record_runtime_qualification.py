from pathlib import Path

runtime_sha = "f7209546f3f2d1dd8ad08458b0dea8adbef522af100deb2f5de90cbe26180b9d"

checkpoint = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
build_index = Path("docs/project/BUILD_TEST_INDEX.md")
project_state = Path("docs/project/PROJECT_STATE.md")
module_status = Path("docs/project/MODULE_STATUS.md")

checkpoint_section = f'''## b101 Human Runtime — healthy long-suspension path; b100 rearm/reconcile gates Positive — 2026-09-05

Exact tested evidence:

- Candidate `DEV-send-stream-0.1.0-b101` / `0.1.0 (101)`; source marker `da103452236e`; Release / iPhone / iOS17.0; diagnostics `ChatGPTClient-Diagnostics-20260904-185039.json`, `sha256:{runtime_sha}`, 95964 bytes / 182 events.
- This sample contains zero exact `NSURLErrorDomain -1005`, zero `detail.transportRecovery` / `list.transportRecovery`, zero `authTransport.retired` / `authTransport.recoveryReady`, zero `coveredExecutor.webProcess`, and zero client-owned protected-Send evidence (`sendObserved`). Therefore the b101 bounded `-1005` recovery branch is **Unexercised / Unverified**, hard WebContent-process death is **Unexercised**, and this is **not** a client-owned accepted-Send death-recovery test.
- Dormant unfinished-turn discovery/rearm is Runtime Positive. App backgrounded `18:27:51Z -> 18:30:30Z` (~2m39s). Automatic `foregroundConversationDiscovery` issued one authoritative Detail, HTTP200 changed visible messages `13 -> 14`, and completed with `latestUserChanged=true` / `rearmDiscoveredRemoteTurn=true`. Covered observation then rearmed; a new user WebSocket opened, `externalStreamStatusResponse` returned HTTP200 `IS_STREAMING`, and Repository started `source=external_page_owned`; the next snapshot reached reasoning 112 chars / service messages 6 / tools 2.
- Known-active external foreground reconcile is Runtime Positive. While that external response was active, app backgrounded `18:30:44Z -> 18:32:40Z` (~1m56s). Foreground automatically emitted `foregroundExternalDetailReconcile.requested` plus Web page rebootstrap. Authoritative Detail HTTP200 changed `14 -> 15`, emitted `liveResponse.externalDetailReconciled(reason=authoritative_assistant_materialized)`, cleared the live projection and released the executor.
- WebSocket transport interruption was real but distinct from WebContent death: on both `18:30:30Z` and `18:32:40Z` the user socket emitted `error` + `close(1006)`. The first was followed by a new socket `created/open/message` and live continuation; the second coincided with Native authoritative final convergence. No `webViewWebContentProcessDidTerminate` callback occurred.
- Long dormant foreground discovery remained healthy after `18:32:48Z -> 18:50:23Z` (~17m35s): one automatic Detail returned HTTP200 and materialized `15 -> 17` (`addedVisibleMessageCount=2`, `latestUserChanged=true`, `rearmDiscoveredRemoteTurn=false`). This is normal-path long-suspension regression evidence only; because no `-1005` occurred, it does not accept the new b101 recovery branch.

Runtime classification:

- b101 bounded Native `-1005` recovery: **Unexercised / Unverified**;
- b100 unfinished remote-turn discovery + one covered rearm: **Runtime Positive**;
- b100 known-active external foreground Detail reconcile: **Runtime Positive**;
- b100 long dormant foreground discovery: **Runtime Positive again**, including ~17m35s in this sample;
- WebSocket `1006` interruption tolerance for the tested external flow: **Runtime Positive** via observer rearm / authoritative Detail convergence;
- b98 hard WebContent-process recovery: **Unexercised / Unverified**;
- client-owned accepted protected-Send recovery after Web/WebContent death: **Unexercised / future gate**;
- overall `DEV-send-stream`: **Runtime Partial / Stable-Frozen No**.

**Next exact action:** keep canonical b101 unchanged; no b102/product change is justified by this sample. Continue b101 only until an exact `-1005` sample exercises its bounded recovery branch, or explicitly pivot to the separately scoped client-owned accepted-Send transport-death gate. Never treat WebSocket code1006 as proof of `WKWebView` WebContent-process death and never auto-resend a protected Send.

'''

state_section = f'''## DEV-send-stream b101 Human Runtime normal-path/regression update — 2026-09-05

- Exact b101 diagnostics `sha256:{runtime_sha}` / 95964 bytes / 182 events / Release / iPhone / iOS17.0 / source `da103452236e` contains no `-1005` and no b101 transport-recovery diagnostic, so the bounded Native read recovery remains Unexercised rather than accepted.
- Previously-open b100 gates are now Runtime Positive: dormant unfinished remote turn auto-discovered `13 -> 14` with `rearmDiscoveredRemoteTurn=true`, then covered observation reacquired HTTP200 `IS_STREAMING` and a reasoning/tool snapshot; a later known-active foreground return auto-reconciled `14 -> 15` with `authoritative_assistant_materialized`.
- A later ~17m35s dormant interval auto-discovered authoritative `15 -> 17` via HTTP200 with no manual Sync/Reload. Two user-WebSocket `error/close(1006)` events occurred during earlier foreground returns, but no hard WebContent-process termination callback occurred.
- This sample has zero client-owned protected-Send evidence, so it does not qualify accepted-Send recovery after Web/WebContent death. No product/b102 change is justified; canonical b101 remains the Runtime candidate, overall Runtime Partial / Stable-Frozen No.

'''

module_section = f'''## DEV-send-stream b101 Runtime qualification update — 2026-09-05

- `ConversationRepository` remains sole Native conversation/list/detail/recovery/response-lifecycle authority. Exact b101 Runtime `sha256:{runtime_sha}` keeps the new `-1005` transport-renewal branch Unexercised because every authoritative Detail in the sample returned HTTP200 and no transport-recovery diagnostic occurred.
- The same sample closes two external-flow module gates as Runtime Positive: no-active unfinished remote discovery (`13 -> 14`, `rearmDiscoveredRemoteTurn=true`, covered `IS_STREAMING` + reasoning/tool snapshot) and known-active foreground final reconcile (`14 -> 15`, `authoritative_assistant_materialized`). A later ~17m35s dormant discovery also converged `15 -> 17` automatically.
- User WebSocket `close(1006)` occurred twice, but no `webViewWebContentProcessDidTerminate` signal occurred. Hard WebContent recovery and client-owned accepted-Send transport-death recovery remain separate Unverified gates; this sample contains no client-owned Send.
- Module remains Active / Runtime Partial / Stable-Frozen No. No b102 or product delta is authorized from this evidence alone.

'''

for path, section in ((checkpoint, checkpoint_section), (project_state, state_section), (module_status, module_section)):
    text = path.read_text()
    if runtime_sha not in text:
        path.write_text(section + text)

text = build_index.read_text()
lines = text.splitlines()
new_lines = []
seen_b101 = seen_b100 = False
for line in lines:
    if line.startswith("| `DEV-send-stream-0.1.0-b101` |"):
        seen_b101 = True
        line = "| `DEV-send-stream-0.1.0-b101` | `DEV-send-stream` | `0.1.0 (101)` | bounded Native read-transport recovery product `54a9fa52a7b44a1b7418a39e4b0f7493989f999d`; package `da103452236e31e070eae68b9e7979a832662fc1`; PR #29 | initial staging `33903494492` zero-job workflow parse failure invalid; corrected staging `33903822115/101123907440` exact two-product-file scope + Simulator passed; Push `33904070096/101124706091` passed; PR `33904076581/101124726725` passed; canonical Artifact `9948780963`; ZIP `df5e95d273c0a4f977b47ac7b64eb654daea99e3b797c3c54924b820fd165e64`; IPA `463bafd4daea37a429088e670d32474cdd9f429347d1fba336d8a091b1f31df3`; b101/source/iOS14/[1,2]/arm64 verified | Runtime `f7209546...`: no `-1005` or transport-recovery event, so b101 recovery branch Unexercised; normal path positive. ~2m39s dormant return auto Detail `13->14`, `rearmDiscoveredRemoteTurn=true`, then covered HTTP200 `IS_STREAMING` + reasoning/tool snapshot; ~1m56s known-active return auto Detail `14->15` and `authoritative_assistant_materialized`; later ~17m35s dormant return auto Detail `15->17` HTTP200. WebSocket `1006` occurred, hard WebContent death/client-owned Send did not | **Runtime Partial: normal-path + b100 rearm/reconcile regressions Positive / b101 `-1005` recovery Unexercised / hard-WebContent + client-owned death recovery Unverified / Stable-Frozen No; permanently reserved** |"
    elif line.startswith("| `DEV-send-stream-0.1.0-b100` |"):
        seen_b100 = True
        line = "| `DEV-send-stream-0.1.0-b100` | `DEV-send-stream` | `0.1.0 (100)` | foreground dormant discovery product `70c7dc052865ef80ca7bdec083d7621c1a297eab`; package `e88a50ad9c2098449b43fb0fce2c441a50cd20ac`; PR #29 | staging `33895020559/101095508915`; Push `33895244146/101096229135`; PR `33895249810/101096247432`; Artifact `9945483725`; ZIP `babb23c845c4da971b488b4860c043fe8471adf830688920149df254cee70fd6`; IPA `5629deedca665b7a5cfa7e36b4996b7b1e4b7a160ca5cb35a465abfbd97fbc69`; b100/source/iOS14/[1,2]/arm64 verified | Runtime: dormant discovery `8->10` after ~19m31s Positive; later b100 sample exposed repeated Native `-1005` after ~12m37s and was superseded by b101 transport gate. Exact b101 regression sample `f7209546...` additionally closes b100 unfinished-turn rearm (`13->14`, rearm=true, live `IS_STREAMING`/snapshot) and known-active foreground reconcile (`14->15`, authoritative assistant materialized) as Runtime Positive | **Dormant discovery + unfinished-turn rearm + known-active foreground reconcile Runtime Positive; stale Native read failure superseded by b101 recovery gate / Stable-Frozen No; permanently reserved** |"
    new_lines.append(line)
if not seen_b101 or not seen_b100:
    raise SystemExit(f"candidate rows missing: b101={seen_b101} b100={seen_b100}")
new_text = "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")
build_index.write_text(new_text)
