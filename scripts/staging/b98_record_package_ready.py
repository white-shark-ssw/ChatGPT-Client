from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs/project"

PRODUCT = "2edd55febe2005071722ddcb9989151b427165d8"
PACKAGE = "17c65a390f2724a55cd29d466e01eaab988dcbfe"
PUSH = "33886537405/101067576599"
PR = "33886540813/101067587985"
ARTIFACT = "9942092070"
ZIP_SHA = "f290b8a4d871016ce93a186b15c10e505a2a1d41b4adce4d19859d92fb65b3ae"
IPA_SHA = "b1dc76dbe28e77ceac3468e8cfd3ca0ded41601bd02db6b228bd391a1d697b67"
STAGING = "33886277311/101066715850"


def prepend(path: Path, heading: str, section: str) -> None:
    text = path.read_text()
    marker = section.splitlines()[0]
    if marker in text:
        raise SystemExit(f"already recorded: {marker}")
    if not text.startswith(heading + "\n"):
        raise SystemExit(f"unexpected heading for {path}")
    path.write_text(heading + "\n\n" + section.rstrip() + "\n\n" + text[len(heading)+2:])


# Build / Test index
index = DOCS / "BUILD_TEST_INDEX.md"
text = index.read_text()
if "| `DEV-send-stream-0.1.0-b98` |" in text:
    raise SystemExit("b98 row already present")
anchor = "|---|---|---|---|---|---|---|\n"
if text.count(anchor) != 1:
    raise SystemExit("candidate table anchor mismatch")
row = (
    "| `DEV-send-stream-0.1.0-b98` | `DEV-send-stream` | `0.1.0 (98)` | "
    f"hard WebContent external-observation recovery product `{PRODUCT}`; exact package source `{PACKAGE}`; PR #29 | "
    f"guarded staging `{STAGING}` exact two-product-file scope + Simulator passed; Push `{PUSH}` passed; PR `{PR}` passed; canonical Artifact `{ARTIFACT}`; Artifact ZIP `sha256:{ZIP_SHA}`; IPA `sha256:{IPA_SHA}`; independent package inspection: Candidate b98 / source `17c65a390f27` / Release / iOS14 / `[1,2]` / iphoneos / arm64 | "
    "Human Runtime pending: during a cross-platform external response, a real covered-Web WebContent process termination must preserve the Repository external live response and cause exactly one immediate rebootstrap when active, or defer to the existing foreground Detail+Web rebootstrap path when background/inactive; no second Send | "
    "**Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity verified / Runtime pending / Stable-Frozen No; permanently reserved** |\n"
)
index.write_text(text.replace(anchor, anchor + row, 1))

# Current checkpoint
checkpoint = DOCS / "current/dev/DEV-send-stream-round7-runtime-addendum.md"
checkpoint_section = f'''## b98 hard WebContent termination recovery — package-ready 2026-09-04

Exact identity:

- Candidate `DEV-send-stream-0.1.0-b98` / `0.1.0 (98)`, permanently reserved;
- product code `{PRODUCT}` — guarded product delta only `ChatGPTClient.xcodeproj/project.pbxproj` and `ChatGPTClient/RootViewController.swift`;
- exact package source `{PACKAGE}`;
- guarded staging `{STAGING}` success including durable pre-write checkpoint, exact two-product-file scope, `git diff --check`, and Debug iphonesimulator compile;
- Push `{PUSH}` success; PR `{PR}` success;
- canonical Push Artifact `{ARTIFACT}` / ZIP `sha256:{ZIP_SHA}`;
- IPA `ChatGPTClient-0.1.0-b98-dev-send-stream.ipa` / `sha256:{IPA_SHA}`;
- independent unpacking: bundle `com.whitesharkssw.chatgptclient`, version/build `0.1.0 (98)`, Candidate b98, source `17c65a390f27`, Release, iOS14+, UIDeviceFamily `[1,2]`, Mach-O arm64.

Product boundary:

1. `webViewWebContentProcessDidTerminate` remains the only new recovery trigger. Silence, elapsed time, focus state, missing snapshots and ordinary navigation failures are not treated as disconnect evidence.
2. When `observingExternalResponse == true`, hard WebContent termination no longer calls `failCurrent`; external observation callbacks, current conversation identity and Repository live response remain intact.
3. If app state is active, the same executor performs exactly one existing full-page external-observation rebootstrap for that termination event. If inactive/background, no background network work is started; recovery is deferred to the existing foreground path.
4. Foreground recovery still runs b97's one authoritative `syncLatestMessages` reconcile plus one existing covered-Web page rebootstrap if the external response remains active.
5. Client-owned protected Send still treats WebContent termination as failure. No automatic resend/replay is authorized.
6. No timer, silence watchdog, retry loop, duplicate Send, regenerate, guessed `/resume`, challenge replay, Native background heartbeat or second response store.

b97 Human Runtime was explicitly **Not Executed** by user and remains permanently reserved. b98 supersedes only its test priority; b97's foreground authoritative Detail reconcile remains part of the b98 product behavior.

All later b98-named Artifacts caused only by docs/staging maintenance are **non-canonical for Human Runtime**. Canonical identity is only Push Artifact `{ARTIFACT}` / IPA `sha256:{IPA_SHA}` from package source `{PACKAGE}`.

Evidence ladder: **b97 Runtime Not Executed / b98 Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen Send No.**

**Next exact action:** install only canonical b98 IPA and collect one real hard WebContent-termination sample while a cross-platform external response is active. Verify `coveredExecutor.webProcess(state=terminated, mode=external_observation)` followed by `coveredExecutor.externalWebProcessRecovery(immediate_rebootstrap)` when foreground, or `deferred_to_foreground` followed by the existing foreground Detail reconcile + Web rebootstrap after return. The same Repository generation must survive and there must be no second Send. Do not allocate b99 before this Runtime gate.
'''
prepend(checkpoint, "# DEV-send-stream round 7 Runtime addendum", checkpoint_section)

state_section = f'''## 2026-09-04 — b98 hard WebContent external-observation recovery package ready

- User explicitly skipped b97 Human Runtime; b97 is recorded as Runtime Not Executed and remains permanently reserved. b98 is the next unique Runtime candidate.
- `DEV-send-stream-0.1.0-b98` / `0.1.0 (98)` exact product `{PRODUCT}`, package source `{PACKAGE}`, PR #29 open/unmerged.
- b98 changes hard covered-Web process death for external/cross-platform observation from response failure into transport interruption: preserve the existing external Repository live response and callbacks; immediately full-page rebootstrap once if foreground, otherwise defer to the existing foreground recovery path. Client-owned protected Send still fails on WebContent death and is never resent automatically.
- Guarded staging `{STAGING}` passed exact two-product-file scope + Simulator. Push `{PUSH}` and PR `{PR}` passed. Canonical Artifact `{ARTIFACT}`; ZIP `sha256:{ZIP_SHA}`; IPA `sha256:{IPA_SHA}`; independent package identity verified as b98/source `17c65a390f27`/Release/iOS14/arm64.
- Human Runtime Pending. This does not claim silent page-loop stall detection or true background execution; Stable/Frozen No.
'''
prepend(DOCS / "PROJECT_STATE.md", "# Project State", state_section)

profile_section = f'''## Latest DEV-send-stream candidate override — b98 2026-09-04

- Latest test candidate: `DEV-send-stream-0.1.0-b98` / `0.1.0 (98)`; exact product `{PRODUCT}`; package source `{PACKAGE}`; canonical Artifact `{ARTIFACT}`; IPA `sha256:{IPA_SHA}`; Human Runtime pending; Stable/Frozen No.
- b98 preserves b97 foreground authoritative Detail reconcile and adds only explicit hard `WKWebView` WebContent-process-death recovery for external observation. Protected Send remains TD-029 covered official-Web owned and is never automatically resent.
- b97 Human Runtime was not executed by user; its package identity remains permanently reserved.
'''
prepend(DOCS / "PROJECT_PROFILE.md", "# Project Profile", profile_section)

module_section = f'''## DEV-send-stream b98 hard WebContent recovery package-ready override — 2026-09-04

- `ConversationRepository` remains sole Native conversation/content/response-lifecycle authority. b98 does not create another response owner or Native continuation protocol.
- Covered Web now distinguishes a hard WebContent-process death during external observation from client-owned Send failure. External observation preserves its callbacks/current conversation/Repository live projection and reboots the same existing page once when active; inactive/background termination is deferred to existing foreground b97 Detail reconcile + page rebootstrap.
- Client-owned protected Send still fails on WebContent termination; no automatic resend/replay. Navigation failure semantics are unchanged. No silence timer/watchdog/retry loop was added.
- Exact product `{PRODUCT}`; package `{PACKAGE}`; staging `{STAGING}` + Push `{PUSH}` + PR `{PR}` passed; Artifact `{ARTIFACT}`; IPA `sha256:{IPA_SHA}`; Human Runtime Pending; Stable/Frozen No.
'''
prepend(DOCS / "MODULE_STATUS.md", "# Module Status", module_section)

tech_section = '''## DEV-send-stream b98 explicit WebContent-death recovery decision — 2026-09-04

- Treat `WKNavigationDelegate.webViewWebContentProcessDidTerminate` as authoritative evidence that the covered Web transport process died. For an already-established external/cross-platform observation, this is a transport interruption and is not evidence that the server-side response failed.
- Only this hard termination signal gains automatic recovery in b98. Do not infer disconnect from elapsed silence, missing snapshots, focus state, route state or ordinary navigation failure.
- Preserve external Repository live-response authority across the termination. If the app is active, perform exactly one existing full-page external-observation rebootstrap for that event; if inactive/background, defer to the existing foreground lifecycle recovery instead of initiating background work.
- This exception does not apply to client-owned protected Send. WebContent death during protected Send remains failure and must never cause automatic resend/replay.
- b97's one-shot foreground authoritative Detail reconcile remains valid and composes with b98. This decision authorizes no timers, watchdogs, retry loops, duplicate Send, guessed `/resume`, challenge replay, second response store or Native background heartbeat.
'''
prepend(DOCS / "TECHNICAL_DECISIONS.md", "# Technical Decisions", tech_section)

rule_section = '''## Hard covered-Web process recovery for external observation — b98 2026-09-04

- `webViewWebContentProcessDidTerminate` is the only new automatic recovery trigger authorized by b98. Do not use silence duration, lack of snapshots, focus state, route state or generic navigation failure as a substitute disconnect detector.
- When the executor is observing an external/cross-platform response, hard WebContent termination must preserve the current conversation identity, external observation callback and `ConversationRepository` live-response projection. It must not emit response `.failed` solely because WebContent died.
- If the app is active, issue exactly one existing full-page external-observation rebootstrap for that termination event. If inactive/background, do not start background network work; the existing foreground path owns later one-shot authoritative Detail reconcile and Web rebootstrap.
- Client-owned protected Send is excluded from this recovery rule: WebContent death remains failure and must never automatically resend, replay or regenerate the user prompt.
- b98 adds no recurring retry, timer, watchdog, Native status/resume synthesis, challenge replay, background heartbeat or second response store. TD-029 and the b97 foreground authoritative reconcile rule remain in force.
'''
prepend(DOCS / "PROJECT_SPECIFIC_RULES.md", "# Project-Specific Rules", rule_section)

print("b98 package-ready evidence recorded")
