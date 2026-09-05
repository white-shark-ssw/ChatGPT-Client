from pathlib import Path

PRODUCT = "113fa19d7264b953949770d2e44cb500ded2da6b"
PACKAGE = "4bd3501a3092dfe7aad7ea836ba0cb8e42b0d65f"
STAGING = "33960451799/101291316464"
PUSH = "33960627676/101291785599"
PR = "33960629168/101291789461"
ARTIFACT = "9967821935"
ZIP_SHA = "d2036ed0372b16c7690c9d3b324d680db6a522fd5ace26d27afa8733a95a9585"
IPA_SHA = "7195d89cb9837efc3386c5dd7e030e7f11f10233689416e59c86d1ae4cf055cd"


def insert_after_title(path: str, marker: str, section: str) -> None:
    p = Path(path)
    text = p.read_text()
    if marker in text:
        return
    lines = text.splitlines(keepends=True)
    index = next((i for i, line in enumerate(lines) if line.startswith("# ")), None)
    if index is None:
        raise SystemExit(f"missing title in {path}")
    lines.insert(index + 1, "\n" + section.rstrip() + "\n\n")
    p.write_text("".join(lines))


checkpoint_section = f'''## b107 accepted-SSE EOF convergence — package ready 2026-09-05

Canonical identity / validation:

- Candidate `DEV-send-stream-0.1.0-b107` / `0.1.0 (107)`, permanently reserved.
- Exact product commit `{PRODUCT}`; canonical package source `{PACKAGE}`.
- Guarded staging `{STAGING}` passed Batch A Runtime/allocation recording, exact two-product-path scope validation, `git diff --check`, Debug Simulator compile and exact product commit.
- Formal Push `{PUSH}` and PR `{PR}` both passed on exact package source `{PACKAGE}`.
- Canonical Push Artifact `{ARTIFACT}`; GitHub digest and independent ZIP SHA-256 both `{ZIP_SHA}`.
- Canonical IPA `ChatGPTClient-0.1.0-b107-dev-send-stream.ipa`; independent SHA-256 `{IPA_SHA}`, matching sidecar. Package inspection verifies `com.whitesharkssw.chatgptclient`, `0.1.0 (107)`, Candidate b107, source marker `4bd3501a3092`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS, Mach-O arm64.

Behavior / Runtime gate:

- b106 SSE `conversation_id` New Chat handoff remains unchanged and Runtime Positive.
- For an already HTTP200-SSE-accepted client Send, exact `stream_ended_without_done` no longer mutates the same Repository generation to failed. Root logs `acceptedClientStreamEndedWithoutDone`, releases only the ended executor transport, and reuses the already Runtime-positive accepted-client recovery primitive to attach one fresh covered observer to the **same generation** with `no_resend_same_generation` semantics.
- Successful manual Sync additionally calls the existing `clearLiveResponseAfterAuthoritativeReconcile` primitive when a client-owned live snapshot is already non-active, preventing authoritative rows plus a stale failed/terminal live tail after server state has advanced.
- b107 adds no retry loop, timer/watchdog, polling, duplicate Send, regenerate, challenge replay, guessed Native resume/status, new response authority, completion heuristic or color workaround.
- The b106 assistant blue-text defect remains separately open. b107 intentionally does not modify `ConversationMessageCell` because the b106 reset was Runtime-insufficient and the exact owner is still unproven.
- Human Runtime remains Pending; Stable/Frozen remains No.

**Next exact action:** install only canonical b107 and reproduce one New Chat first Send. If exact accepted `stream_ended_without_done` occurs, require no `phase=failed`/`回答失败`, no second protected Send, same-generation covered recovery and eventual authoritative convergence. After any manual Sync, authoritative content must not be followed by a stale prompt/reasoning/failure tail. Blue-text behavior is observed but not a b107 pass/fail claim except as an unchanged known defect.'''
insert_after_title("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md", "## b107 accepted-SSE EOF convergence — package ready", checkpoint_section)

index = Path("docs/project/BUILD_TEST_INDEX.md")
text = index.read_text()
new_row = f'''| `DEV-send-stream-0.1.0-b107` | `DEV-send-stream` | `0.1.0 (107)` | accepted-SSE EOF same-generation recovery product `{PRODUCT}`; package `{PACKAGE}`; PR #29 | staging `{STAGING}` exact two-product-path scope + `git diff --check` + Simulator passed; Push `{PUSH}` passed; PR `{PR}` passed; canonical Artifact `{ARTIFACT}`; ZIP `{ZIP_SHA}`; IPA `{IPA_SHA}`; package verified Build107/Candidate b107/source `4bd3501a3092`/Release/iOS14+/`[1,2]`/arm64 | Human Runtime pending: accepted `stream_ended_without_done` must not become local failure, must recover same generation with no resend; authoritative Sync must clear stale non-active client live projection; blue-text defect remains separately unresolved | **Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity verified / Human Runtime pending / Stable-Frozen No; permanently reserved** |'''
lines = text.splitlines()
found = False
for i, line in enumerate(lines):
    if line.startswith("| `DEV-send-stream-0.1.0-b107` |"):
        lines[i] = new_row
        found = True
        break
if not found:
    raise SystemExit("missing allocated b107 Build/Test row")
index.write_text("\n".join(lines) + "\n")

state_section = f'''## DEV-send-stream b107 package-ready Runtime gate — 2026-09-05

- b106 Runtime is Partial: SSE authoritative New Chat identity is Positive, while accepted-SSE clean EOF false-failure and stale-live double presentation are Negative; assistant blue text remains unresolved.
- b107 product `{PRODUCT}` and canonical package `{PACKAGE}` preserve the b106 SSE-ID handoff and add only same-generation accepted EOF recovery plus authoritative manual-Sync stale-live cleanup.
- Staging `{STAGING}`, Push `{PUSH}`, PR `{PR}` all passed. Canonical Artifact `{ARTIFACT}` / ZIP `{ZIP_SHA}` / IPA `{IPA_SHA}` are independently package-verified.
- Evidence ladder: Code / guarded Simulator / Push CI / PR CI / Artifact / package identity verified; Human Runtime Pending; Stable-Frozen No.'''
insert_after_title("docs/project/PROJECT_STATE.md", "## DEV-send-stream b107 package-ready Runtime gate", state_section)

module_section = '''## Send / Stream — b107 package-ready update 2026-09-05

- `DEV-send-stream` remains Active / Stable-Frozen No.
- b106 proved New Chat protected-Send SSE authoritative identity but exposed accepted clean-EOF false failure and stale-live double presentation.
- b107 is package-qualified for the narrow same-generation no-resend EOF recovery + authoritative stale-live cleanup gate. Blue assistant text remains a separate unresolved presentation defect and is not changed by b107.'''
insert_after_title("docs/project/MODULE_STATUS.md", "## Send / Stream — b107 package-ready update", module_section)

rule_section = '''## Accepted client SSE clean-EOF recovery — b107 2026-09-05

- Exact b106 Runtime proves an HTTP200 `text/event-stream` protected Send may finish server-side even when the covered filtered response ends without observing exact `[DONE]`; therefore exact `stream_ended_without_done` after explicit acceptance is a receive-transport interruption, not sufficient evidence to mark the Repository response failed.
- For that exact condition only, preserve the same prompt-owned Repository generation and reuse the existing accepted-client covered-observer recovery path. Never replay/resend/regenerate the prompt.
- A successful authoritative manual Sync may clear an already non-active client live projection only through the existing `clearLiveResponseAfterAuthoritativeReconcile` count/baseline guard. This prevents authoritative + stale-live duplication without creating another content authority.
- Do not generalize this rule to pre-acceptance failure, arbitrary navigation failure, silence, timeouts or unknown stream errors. No polling, retry loop, timer/watchdog, guessed resume/status or second response store is authorized.
- Assistant blue-text corruption remains separately evidence-gated; do not add speculative color fixes under this recovery rule.'''
insert_after_title("docs/project/PROJECT_SPECIFIC_RULES.md", "## Accepted client SSE clean-EOF recovery — b107", rule_section)

tech_section = '''## TD-accepted-client-clean-EOF-convergence — b107 Runtime gate 2026-09-05

Decision: after explicit protected-Send HTTP200 SSE acceptance, exact `stream_ended_without_done` does not by itself own terminal failure. Preserve the same `ConversationRepository` generation, release the ended covered executor transport, and reuse the previously Runtime-positive same-generation accepted-client observation recovery. Authoritative Detail remains final Native content authority; a later successful Sync can clear a non-active stale live projection through the existing reconcile primitive. This decision adds no resend/retry/polling/completion heuristic and does not address the independent blue-text defect.'''
insert_after_title("docs/project/TECHNICAL_DECISIONS.md", "## TD-accepted-client-clean-EOF-convergence", tech_section)

adapter_section = f'''## DEV-send-stream b107 accepted protected-Send SSE clean EOF — package-ready override 2026-09-05

- Exact b106 Runtime retained the correct first top-level protected-Send SSE `conversation_id` handoff but showed that a successfully accepted HTTP200 SSE can end without the bridge observing exact `[DONE]` while the authoritative server conversation is already complete.
- b107 keeps the Web adapter grammar and New Chat identity logic unchanged. Native Root handles the exact post-acceptance `stream_ended_without_done` transport result by preserving the same Repository generation and reattaching one covered observer; it never performs a second protected Send.
- Product `{PRODUCT}` / package `{PACKAGE}`; staging `{STAGING}`, Push `{PUSH}`, PR `{PR}` passed; canonical Artifact `{ARTIFACT}`, ZIP `{ZIP_SHA}`, IPA `{IPA_SHA}` verified.
- Human Runtime pending. No new Stop behavior is authorized; exact Stop route/target/ack evidence remains required.'''
insert_after_title("docs/project/WEB_SEND_ADAPTER.md", "## DEV-send-stream b107 accepted protected-Send SSE clean EOF", adapter_section)

profile_section = f'''## Current DEV-send-stream test identity — b107 2026-09-05

- Current package-qualified Human Runtime candidate: `DEV-send-stream-0.1.0-b107` / Build107.
- Canonical product `{PRODUCT}`; package source `{PACKAGE}`; Artifact `{ARTIFACT}`; IPA SHA-256 `{IPA_SHA}`.
- This is test-candidate evidence only; project Stable/Frozen state is unchanged.'''
insert_after_title("docs/project/PROJECT_PROFILE.md", "## Current DEV-send-stream test identity — b107", profile_section)
