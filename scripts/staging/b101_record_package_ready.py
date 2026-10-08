from pathlib import Path


def prepend(path: str, marker: str, block: str) -> None:
    p = Path(path)
    text = p.read_text()
    if marker in text:
        raise SystemExit(f"marker already present: {marker}")
    p.write_text(block.strip() + "\n\n" + text)


checkpoint = r'''## b101 Native read transport renewal — package-ready 2026-09-05

Exact evidence:

- Candidate `DEV-send-stream-0.1.0-b101` / `0.1.0 (101)`, permanently reserved.
- Triggering Runtime evidence remains exact b100 diagnostics `ChatGPTClient-Diagnostics-20260904-174041.json`, `sha256:515c60b59d969ee1f33d76fec097d6163450058c5ef3fa9ccd551b2439f03818`: after ~12m37s background, foreground discovery fired but authoritative Detail, later Detail, two list GETs and manual Sync all failed `NSURLErrorDomain -1005` while covered WebSocket independently reopened; no hard WebContent-process termination signal occurred.
- Exact b101 product commit `54a9fa52a7b44a1b7418a39e4b0f7493989f999d`; exact product delta is only `ChatGPTClient.xcodeproj/project.pbxproj` plus `ChatGPTClient/Conversation/ConversationFeature.swift`.
- Product behavior: only idempotent Native conversation-list / Conversation Detail GETs gain bounded recovery. On the first exact `NSURLErrorNetworkConnectionLost (-1005)`, retire the matching cached `AuthTransientSession`, reacquire one fresh transient session from the existing default-WebKit-auth path, re-check account/operation freshness, then retry that same GET once. A second failure terminates normally. Protected Web Send, covered Web observation, b100 foreground discovery, Repository content authority and client-owned response ownership are unchanged.
- Initial staging workflow run `33903494492` had zero jobs due workflow parse failure and is invalid evidence; it emitted no product change. Corrected staging `33903822115 / 101123907440` passed exact two-product-file scope, `git diff --check` and Debug iphonesimulator compile, then committed product `54a9fa52...`.
- Exact canonical package source `da103452236e31e070eae68b9e7979a832662fc1` changes only `ios-foundation.yml` after the product commit. Formal Push `33904070096 / 101124706091` and same-source PR `33904076581 / 101124726725` both passed.
- Canonical Push Artifact `9948780963`, Artifact ZIP `sha256:df5e95d273c0a4f977b47ac7b64eb654daea99e3b797c3c54924b820fd165e64`. Same-source PR Artifact `9948785659` is CI corroboration only and is not the Human Runtime package authority.
- Canonical IPA `ChatGPTClient-0.1.0-b101-dev-send-stream.ipa`, independently recomputed `sha256:463bafd4daea37a429088e670d32474cdd9f429347d1fba336d8a091b1f31df3`, matching the package sidecar.
- Independent package inspection confirms `com.whitesharkssw.chatgptclient`, `0.1.0 (101)`, Candidate b101, source marker `da103452236e`, Release, iOS14 minimum, UIDeviceFamily `[1,2]`, iPhoneOS and Mach-O 64-bit arm64.

Evidence ladder: **Code written / exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**

Batch recovery state:

- confirmed complete: b100 `-1005` Runtime evidence classified; b101 allocated; exact two-file product committed; corrected staging passed; canonical package source fixed; Push+PR package CI passed; canonical Artifact/IPA identity independently verified;
- this recorder batch owns only checkpoint + durable project docs. Product code, b101 package source/Artifact/IPA, PR #35 and prior candidates must not be changed by recovery;
- after this docs batch, only PR #29 metadata update and Human Runtime handoff remain.

**Next exact action:** use only canonical b101 IPA. Reproduce the long-suspension scenario that produced `-1005`; on foreground do not press Sync/Reload first. If the first authoritative Detail reports `-1005`, diagnostics must show exactly one `detail.transportRecovery` request, retirement of the current transient session, one fresh auth transport acquisition, one `transportAttempt=2`, then HTTP200/convergence or a normal terminal failure with no third attempt. Also verify conversation-list refresh remains functional after the same recovery. If the first GET is already healthy, the b101 recovery branch is Unexercised rather than accepted. Export diagnostics.''' 

state = r'''## DEV-send-stream b101 Native read transport recovery package ready — 2026-09-05

- Exact b100 Runtime `sha256:515c60b59d969ee1f33d76fec097d6163450058c5ef3fa9ccd551b2439f03818` adds a new failure classification: after ~12m37s suspension, b100 foreground discovery still triggered, but Native Detail/list/manual Sync repeatedly failed exact `NSURLErrorDomain -1005` while covered Web networking independently reopened. This rejects the hard-WebContent-death hypothesis for that sample and exposes stale cached `AuthTransientSession` reuse as the Native read recovery gap.
- b101 is the evidence-scoped correction: first exact `-1005` from conversation-list or Detail GET retires only the matching cached transient session, reacquires one fresh transient session through existing WebKit auth, and retries the same idempotent read at most once under the same operation generation/account scope. No timer, cadence, reachability watcher, retry loop, background heartbeat, Send replay or second authority is added.
- Product `54a9fa52a7b44a1b7418a39e4b0f7493989f999d`; package source `da103452236e31e070eae68b9e7979a832662fc1`; staging `33903822115/101123907440`; Push `33904070096/101124706091`; PR `33904076581/101124726725`; canonical Artifact `9948780963`; ZIP `sha256:df5e95d273c0a4f977b47ac7b64eb654daea99e3b797c3c54924b820fd165e64`; IPA `sha256:463bafd4daea37a429088e670d32474cdd9f429347d1fba336d8a091b1f31df3`.
- Package identity independently verified as `com.whitesharkssw.chatgptclient`, `0.1.0 (101)`, Candidate b101, source `da103452236e`, Release/iOS14+/`[1,2]`/arm64. Human Runtime pending; Stable-Frozen No.
'''

profile = r'''## Latest DEV-send-stream candidate override — b101 2026-09-05

- Latest Human Runtime candidate: `DEV-send-stream-0.1.0-b101` / `0.1.0 (101)`, permanently reserved. It addresses the exact b100 long-suspension Native read failure where Detail/list/manual Sync repeatedly returned `NSURLErrorDomain -1005` while WebKit networking reopened independently.
- b101 changes only Native idempotent conversation-list/Detail transport recovery: retire the matching cached transient session on the first exact `-1005`, reacquire through existing default-WebKit auth, retry the same read once, then terminate normally on any further failure. Protected Web Send and response/content authority are unchanged.
- Exact product `54a9fa52a7b44a1b7418a39e4b0f7493989f999d`; package source `da103452236e31e070eae68b9e7979a832662fc1`; Artifact `9948780963`; IPA `sha256:463bafd4daea37a429088e670d32474cdd9f429347d1fba336d8a091b1f31df3`; package identity verified; Human Runtime pending; Stable/Frozen No.
'''

module = r'''## DEV-send-stream b101 Native read transport recovery override — 2026-09-05

- `ConversationRepository` remains sole Native conversation/list/detail/recovery/response-lifecycle authority. `AuthSessionStore` remains account authority and default persistent WebKit storage remains persistent auth-secret authority.
- Exact b100 Runtime proves the cached transient Native transport can remain stale after long suspension and repeatedly return `NSURLErrorNetworkConnectionLost (-1005)` even while covered Web networking reconnects. b101 fixes this at the transport owner rather than adding a second reader or lifecycle store.
- For conversation-list and Detail GET only, first exact `-1005` may retire the matching cached `AuthTransientSession`, reacquire one transient session through the existing auth path, and retry the same read once after scope/generation freshness checks. Any second error/failure terminates normally. Client-owned protected Send is untouched and never automatically replayed.
- Product/package `54a9fa52...` / `da103452...`; staging + Push + PR CI passed; Artifact `9948780963`; IPA `sha256:463bafd4daea37a429088e670d32474cdd9f429347d1fba336d8a091b1f31df3`; Human Runtime pending; module not Stable/Frozen.
'''

technical = r'''## DEV-send-stream b101 exact `-1005` Native read recovery decision — 2026-09-05

- Exact b100 Human Runtime demonstrates a concrete normal-path insufficiency: after long suspension, the Repository's cached ephemeral Native `AuthTransientSession` can repeatedly return `NSURLErrorNetworkConnectionLost (-1005)` for Detail, list and manual Sync while account scope is still valid and WebKit networking has independently recovered.
- Authorize one bounded recovery only for idempotent Conversation Detail and conversation-list GETs. On the first exact `-1005`, retire only the matching cached transient session, reacquire through existing `withTransientSession` / default-WebKit auth, revalidate account scope + operation generation, and retry that same GET once.
- Termination is deterministic: `transportRecoveryAttempted=true` prevents a second recovery. A second `-1005`, any different network error, auth failure, HTTP failure, operation supersession or account-scope change follows the existing normal failure path. This is not a general retry policy.
- This decision does not authorize timers, polling, reachability watchers, fallback loops, background heartbeat, protected-Send replay, guessed resume, challenge replay, WebSocket-body authority or a second response/content store. TD-029 and b97-b100 ownership/lifecycle rules remain unchanged.
'''

rules = r'''## Native read transport loss recovery — b101 2026-09-05

- The only automatic Native transport retry authorized by b101 is for the first exact `NSURLErrorDomain / NSURLErrorNetworkConnectionLost (-1005)` from an idempotent conversation-list or Conversation Detail GET using the current account-scoped cached transient session.
- Recovery must retire only the matching cached transient session, reacquire one fresh transient session through the existing default-WebKit-auth path, preserve the existing account scope and operation generation, then retry the same read once. There must be no third attempt.
- A second `-1005`, any other network error, auth/HTTP failure, supersession or account change terminates normally. Do not generalize b101 into a retry framework, timer, watchdog, reachability monitor, polling loop or background keepalive.
- Protected covered-Web Send is excluded. Never resend/replay/regenerate a prompt because Native list/Detail transport was renewed. `ConversationRepository` remains content/response authority; `AuthSessionStore` remains account authority.
'''

prepend('docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md', '## b101 Native read transport renewal — package-ready 2026-09-05', checkpoint)
prepend('docs/project/PROJECT_STATE.md', '## DEV-send-stream b101 Native read transport recovery package ready — 2026-09-05', state)
prepend('docs/project/PROJECT_PROFILE.md', '## Latest DEV-send-stream candidate override — b101 2026-09-05', profile)
prepend('docs/project/MODULE_STATUS.md', '## DEV-send-stream b101 Native read transport recovery override — 2026-09-05', module)
prepend('docs/project/TECHNICAL_DECISIONS.md', '## DEV-send-stream b101 exact `-1005` Native read recovery decision — 2026-09-05', technical)
prepend('docs/project/PROJECT_SPECIFIC_RULES.md', '## Native read transport loss recovery — b101 2026-09-05', rules)

index = Path('docs/project/BUILD_TEST_INDEX.md')
lines = index.read_text().splitlines()
b101_row = '| `DEV-send-stream-0.1.0-b101` | `DEV-send-stream` | `0.1.0 (101)` | bounded Native read-transport recovery product `54a9fa52a7b44a1b7418a39e4b0f7493989f999d`; package `da103452236e31e070eae68b9e7979a832662fc1`; PR #29 | initial staging `33903494492` zero-job workflow parse failure invalid; corrected staging `33903822115/101123907440` exact two-product-file scope + Simulator passed; Push `33904070096/101124706091` passed; PR `33904076581/101124726725` passed; canonical Artifact `9948780963`; ZIP `df5e95d273c0a4f977b47ac7b64eb654daea99e3b797c3c54924b820fd165e64`; IPA `463bafd4daea37a429088e670d32474cdd9f429347d1fba336d8a091b1f31df3`; b101/source/iOS14/[1,2]/arm64 verified | Human Runtime pending: reproduce long-suspension exact `-1005`; if first Detail/list GET loses connection, verify exactly one transient-session retirement + fresh-session acquisition + attempt 2 and no third attempt; healthy first GET leaves recovery branch Unexercised | **Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity verified / Runtime pending / Stable-Frozen No; permanently reserved** |'
updated_b100 = '| `DEV-send-stream-0.1.0-b100` | `DEV-send-stream` | `0.1.0 (100)` | foreground dormant discovery product `70c7dc052865ef80ca7bdec083d7621c1a297eab`; package `e88a50ad9c2098449b43fb0fce2c441a50cd20ac`; PR #29 | staging `33895020559/101095508915`; Push `33895244146/101096229135`; PR `33895249810/101096247432`; Artifact `9945483725`; ZIP `babb23c845c4da971b488b4860c043fe8471adf830688920149df254cee70fd6`; IPA `5629deedca665b7a5cfa7e36b4996b7b1e4b7a160ca5cb35a465abfbd97fbc69`; b100/source/iOS14/[1,2]/arm64 verified | Runtime sample `f0f3619e...`: dormant selected conversation survived ~19m31s background; automatic Detail materialized `8->10` with no manual Sync/Reload. Later exact sample `515c60b59d969ee1f33d76fec097d6163450058c5ef3fa9ccd551b2439f03818`: after ~12m37s background the lifecycle trigger still fired, but Detail/list/manual Sync repeatedly failed exact `-1005` while covered Web networking reopened; hard WebContent death not observed | **Dormant foreground trigger Runtime Positive / Native long-suspension read transport Runtime Negative / superseded by b101 transport-recovery gate / overall Runtime Partial / Stable-Frozen No; permanently reserved** |'

if any(line.startswith('| `DEV-send-stream-0.1.0-b101` |') for line in lines):
    raise SystemExit('b101 row already present')
found_b100 = False
out = []
for line in lines:
    if line.startswith('| `DEV-send-stream-0.1.0-b100` |'):
        if found_b100:
            raise SystemExit('duplicate b100 row')
        out.append(updated_b100)
        found_b100 = True
    else:
        out.append(line)
if not found_b100:
    raise SystemExit('b100 row not found')
separator = next(i for i, line in enumerate(out) if line.startswith('|---|---|---|---|---|---|---|'))
out.insert(separator + 1, b101_row)
index.write_text('\n'.join(out) + '\n')
