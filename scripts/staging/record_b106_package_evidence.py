from pathlib import Path

PRODUCT = "028100bb79d82e99b62a610e9f30b9f9b3bd7f5c"
PACKAGE = "a02042608911b891a4e9730a2bb3974168c4308a"
STAGING = "33953874027/101273525329"
PUSH = "33953950307/101273735236"
PR = "33953951744/101273739204"
ARTIFACT = "9965747978"
ZIP_SHA = "0558f3926b921b4e06b6336e1a251a8c1cbab661038cd34a303a83046039e4e2"
IPA_SHA = "65acacb62506449bb65356a561603062a0f2b5bae4dc266a811480868b052288"
VIDEO_SHA = "c415187dfb5c2b700f17550f0d429376026d795d55aaf168c304b8586251445b"


def prepend(path: str, marker: str, section: str) -> None:
    p = Path(path)
    text = p.read_text()
    if marker not in text:
        p.write_text(section.rstrip() + "\n\n" + text)

checkpoint_section = f'''## b106 protected-Send SSE authoritative identity + assistant-cell reset — package ready 2026-09-05

Exact qualification:

- Candidate `DEV-send-stream-0.1.0-b106` / `0.1.0 (106)`, permanently reserved. Exact product `{PRODUCT}`; canonical package source `{PACKAGE}`.
- Product scope is exactly `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/RootViewController.swift`, and `ChatGPTClient/Conversation/ConversationFeature.swift`.
- Corrected b106 staging `{STAGING}` passed Batch A durable b105 Runtime/b106 allocation, exact three-product-path audit, `git diff --check`, Debug Simulator compile and exact product commit.
- Formal same-source Push `{PUSH}` and PR `{PR}` both passed.
- Canonical Push Artifact `{ARTIFACT}`; GitHub digest and independent ZIP SHA-256 both `{ZIP_SHA}`.
- Canonical IPA `ChatGPTClient-0.1.0-b106-dev-send-stream.ipa`, independent SHA-256 `{IPA_SHA}`, matching sidecar. Independent package inspection verifies `com.whitesharkssw.chatgptclient`, `0.1.0 (106)`, Candidate b106, source marker `a02042608911`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS, Mach-O arm64. Binary contains `protected_send_sse_conversation_id`, `pendingNewConversationEvents` and `new_conversation_identity_missing_at_terminal`, and contains no deterministic WebContent kill SPI.

Behavior / evidence boundary:

- b105 Runtime remains Partial: one page-owned protected New Chat Send/SSE response succeeded, but the pre-fetch route-derived ID was not the final server conversation identity and terminal Detail returned HTTP400. Exact user video `sha256:{VIDEO_SHA}` also proves per-row blue/normal assistant text corruption on a long response.
- b106 removes the rejected pre-fetch route-ID gate. New Chat still performs exactly one official page-owned protected Send from the root composer.
- Until the first exact top-level `conversation_id` in that same protected Send SSE payload, executor-local pre-identity lifecycle events are staged only as transport events. The first SSE ID emits `.conversationCreated(realID)`, re-keys the same executor, creates the sole Repository generation, then replays staged lifecycle events in order. A conflicting SSE ID is an identity error; terminal without an SSE ID fails visibly. No fake/persisted ID is created.
- The narrow HTTP200-before-SSE-identity WebContent-death window is intentionally fail/no-resend because no authoritative recovery identity exists yet. Existing accepted-client hard-Web same-generation recovery remains unchanged after adoption.
- `ConversationMessageCell` now explicitly resets label highlight/text/highlighted/tint semantics on reuse/configure before assigning role-specific attributed text. Assistant attributed text remains `UIColor.label`; user Markdown link ranges remain explicitly `.systemBlue`. This is a bounded state-reset correction for the exact video defect, not a Markdown/citation renderer redesign.
- No polling, retry loop, timer/watchdog, resend/regenerate, challenge replay, guessed Native resume/status, second response/content store or Stop implementation is added.

Evidence ladder: **b105 Runtime Partial / b106 Code written / exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / b106 Human Runtime pending / Stable-Frozen No.**

**Next exact action:** install only canonical b106. Run New Chat first Send with a long answer. Require one protected Send; `newConversation.authoritativeHandoff source=protected_send_sse_conversation_id`; one Repository generation; terminal authoritative Detail HTTP200 on that same adopted ID; one new-conversation list reconciliation; and no blue/black assistant row alternation while scrolling. Export diagnostics/video only if a visual defect remains. Stop is still outside this candidate.
'''
prepend("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md", "## b106 protected-Send SSE authoritative identity + assistant-cell reset — package ready 2026-09-05", checkpoint_section)

# Build/Test rows: correct the malformed b105 allocation write and finalize b106.
index_path = Path("docs/project/BUILD_TEST_INDEX.md")
lines = index_path.read_text().splitlines()
for i, line in enumerate(lines):
    if line.startswith("| `DEV-send-stream-0.1.0-b106`"):
        lines[i] = f"| `DEV-send-stream-0.1.0-b106` | `DEV-send-stream` | `0.1.0 (106)` | SSE-authoritative New Chat handoff + assistant-cell state reset product `{PRODUCT}`; package `{PACKAGE}`; PR #29 | staging `{STAGING}` exact three-product-path scope + Simulator passed; Push `{PUSH}` passed; PR `{PR}` passed; canonical Artifact `{ARTIFACT}`; ZIP `{ZIP_SHA}`; IPA `{IPA_SHA}`; package independently verified `0.1.0 (106)` / Candidate b106 / source `a02042608911` / Release / iOS14+ / `[1,2]` / arm64; kill SPI absent | Human Runtime pending: one New Chat protected Send must adopt the first exact protected-Send SSE `conversation_id`, keep one Repository generation through terminal + HTTP200 Detail/list convergence, and long assistant rows must remain normal label color without blue/black alternation | **Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity verified / Human Runtime pending / Stable-Frozen No; permanently reserved** |"
    elif line.startswith("| `DEV-send-stream-0.1.0-b105`"):
        lines[i] = f"| `DEV-send-stream-0.1.0-b105` | `DEV-send-stream` | `0.1.0 (105)` | authoritative new-chat first-Send product `6ef4e874d7c2c5f144ab7e784f7a81755d1b2f59`; package `93ab92a9a4a7b8a020ac209f6a82088dc77acbce`; PR #29 | corrected staging `33923512745/101186860450` exact three-product-path scope + Simulator passed; Push `33923732331/101187538891` passed; PR `33923735651/101187548902` passed; canonical Artifact `9956018294`; ZIP `ba53bc8e50e1b89056565e3a557e196ef6b9c5db76e3b40dd28a0536e81d6921`; IPA `d162a7132ff830d3a2f6eb85a2b4a5b4ebc2d9f84531b01418912c99109e5095`; package independently verified b105/source `93ab92a9a4a7`/Release/iOS14+/arm64 | Human Runtime Partial: one New Chat protected Send + HTTP200 SSE + one generation + reasoning/4 tools/4526 final chars + terminal succeeded with no duplicate Send; pre-fetch route identity `sha256:893a1901dd3b` was rejected because terminal Detail returned HTTP400 while later list/Detail identified the real new conversation as `sha256:8170ab408a21` with HTTP200/two messages/latest-user 84 chars. Video `sha256:{VIDEO_SHA}` independently proves long assistant text alternates blue/normal across presentation rows | **Runtime Partial / new-chat route-ID handoff Negative + assistant row-color consistency Negative / superseded by b106 test priority / Stable-Frozen No; permanently reserved** |"
index_path.write_text("\n".join(lines) + "\n")

state_section = f'''## DEV-send-stream b106 SSE authoritative New Chat handoff package ready — 2026-09-05

- b105 Human Runtime rejected the pre-fetch route-derived New Chat identity: one protected Send/SSE response succeeded, but terminal Detail on the adopted route ID returned HTTP400 and the actual server-created conversation appeared under a different ID. User video `sha256:{VIDEO_SHA}` also confirms per-row assistant blue/normal color corruption.
- b106 uses only the first exact top-level `conversation_id` from the same protected Send SSE as authoritative New Chat adoption. Transport-local pre-identity events are replayed only after `.conversationCreated(realID)` establishes one Repository generation. No duplicate Send or fake ID.
- Exact product `{PRODUCT}` / package `{PACKAGE}`; staging + Push + PR CI passed; Artifact `{ARTIFACT}`; IPA `sha256:{IPA_SHA}` independently verified Release Build106/source `a02042608911`/iOS14+/arm64.
- `ConversationMessageCell` now resets label reuse/highlight/tint state before role-specific attributed text; assistant `.label` semantics remain. Human Runtime is pending; Stable-Frozen No.
'''
prepend("docs/project/PROJECT_STATE.md", "## DEV-send-stream b106 SSE authoritative New Chat handoff package ready — 2026-09-05", state_section)

module_section = f'''## DEV-send-stream b106 New Chat SSE identity + assistant row-color correction — 2026-09-05

- `ConversationRepository` remains sole Native response/content authority and covered official Web remains protected-Send owner. b106 does not create a second response store.
- New Chat identity authority moves from the b105-rejected pre-fetch page route to the first exact protected-Send SSE top-level `conversation_id`; one executor and one Repository generation continue through terminal. Conflicting/missing terminal identity fails rather than guesses.
- Long assistant row-color Runtime defect from video `sha256:{VIDEO_SHA}` receives only a cell reuse/configuration state reset; Markdown/citation semantics remain later renderer scope.
- Product/package `{PRODUCT}` / `{PACKAGE}`; Artifact `{ARTIFACT}`; IPA `sha256:{IPA_SHA}`; CI/package verified; Human Runtime pending / Stable-Frozen No.
'''
prepend("docs/project/MODULE_STATUS.md", "## DEV-send-stream b106 New Chat SSE identity + assistant row-color correction — 2026-09-05", module_section)

tech_section = '''## DEV-send-stream b106 New Chat identity-source correction — 2026-09-05

- Exact b105 Runtime rejects treating the official page route observed at protected-fetch time as the final New Chat server identity. A protected Send may succeed while that route-derived ID later returns HTTP400 from authoritative Detail and the actual conversation exists under another ID.
- For New Chat, authorize the first exact top-level `conversation_id` parsed from that same protected Send SSE payload as the authoritative adoption source. Preserve exactly one protected Send and one eventual Repository response generation; executor-local event staging before identity is transport ordering only and must be drained immediately on adoption.
- Conflicting later SSE identity is an identity error. Terminal without any authoritative SSE identity is failure. Do not infer identity from title, DOM text, sidebar order, page-route timing, WebSocket body, generated UUID or another request.
- Do not auto-recover hard WebContent death in the narrow accepted-but-not-yet-identified window because no authoritative conversation target exists; fail/no-resend is safer. Existing b103 accepted-client recovery remains valid after SSE adoption.
- Exact long-answer video shows cell-boundary blue/normal alternation despite assistant attributed text specifying `UIColor.label`. Authorize only a bounded per-config/per-reuse `UILabel` highlight/text/tint state reset as the next Runtime correction; this does not authorize message-renderer refactoring or Markdown/citation work inside Send/Stream.
'''
prepend("docs/project/TECHNICAL_DECISIONS.md", "## DEV-send-stream b106 New Chat identity-source correction — 2026-09-05", tech_section)

rules_section = '''## New Chat authoritative identity — b106 SSE rule 2026-09-05

- The b105 pre-fetch page-route identity rule is superseded for New Chat. The page route at protected-fetch time is not authoritative server identity.
- New Chat still performs exactly one official page-owned protected Send. Before authoritative identity exists, only executor-local ordered lifecycle staging is allowed; no fake server ID may be persisted or routed.
- The first exact top-level `conversation_id` in that same protected Send SSE is the b106 authoritative adoption source. Emit one `.conversationCreated(realID)`, re-key the same executor once, create one Repository generation, then drain staged lifecycle events in order.
- A later conflicting SSE conversation ID is an identity error. `[DONE]`/terminal before any authoritative SSE ID fails visibly. Never recover identity by title/DOM/sidebar position/page-route timing/generated UUID/WebSocket body/second Send.
- Hard WebContent death before SSE identity has been adopted remains fail/no-resend. The normal b103 accepted-client no-resend recovery applies only after authoritative identity/generation exists.
- Assistant message cells must reset `UILabel` highlighted/text/highlightedText/tint state on reuse/configuration before applying role-specific attributed text. Assistant body color remains semantic `.label`; explicitly attributed user links may remain `.systemBlue`. Do not use a global color override to mask row-state corruption.
'''
prepend("docs/project/PROJECT_SPECIFIC_RULES.md", "## New Chat authoritative identity — b106 SSE rule 2026-09-05", rules_section)

adapter_section = f'''## DEV-send-stream b106 protected-Send SSE New Chat identity — package-ready override 2026-09-05

- b105 Runtime supersedes the earlier route-before-fetch rule: the route-derived identity used by b105 was not the final server conversation ID even though the single protected Send returned HTTP200 SSE and streamed normally.
- b106 removes the New Chat pre-fetch route-identity gate. The root composer may perform the one official protected `/backend-api/f/conversation` Send with no Native server ID.
- During that exact protected Send, the bridge examines only parsed SSE payload objects and accepts the first non-empty **top-level** `conversation_id` string as authoritative. It posts `conversation_created` before processing reasoning/tool/final data from that frame. Swift then emits `.conversationCreated`, re-keys the same executor, and drains any pre-identity lifecycle events before later content callbacks.
- Conflicting later SSE ID -> `new_conversation_identity_conflict`; terminal with no SSE ID -> `new_conversation_identity_missing_at_terminal`. Neither path creates a fake ID or starts another Send.
- Exact product `{PRODUCT}`, package `{PACKAGE}`, staging `{STAGING}`, Push `{PUSH}`, PR `{PR}`, Artifact `{ARTIFACT}`, IPA `sha256:{IPA_SHA}`. Human Runtime pending.
'''
prepend("docs/project/WEB_SEND_ADAPTER.md", "## DEV-send-stream b106 protected-Send SSE New Chat identity — package-ready override 2026-09-05", adapter_section)

profile_section = f'''## Latest DEV-send-stream candidate override — b106 2026-09-05

- Latest Human Runtime candidate is `DEV-send-stream-0.1.0-b106` / `0.1.0 (106)`, permanently reserved. Exact product `{PRODUCT}`; package source `{PACKAGE}`; Artifact `{ARTIFACT}`; IPA `sha256:{IPA_SHA}`; package independently verified Release/iOS14+/arm64.
- b105 is Runtime Partial and superseded for test priority: protected New Chat Send/SSE succeeded, but route-derived authoritative handoff failed and long assistant rows showed blue/normal color corruption. b106 moves New Chat authority to exact protected-Send SSE `conversation_id` and adds only a bounded assistant-cell state reset.
- Human Runtime pending; Stable/Frozen No.
'''
prepend("docs/project/PROJECT_PROFILE.md", "## Latest DEV-send-stream candidate override — b106 2026-09-05", profile_section)

print("b106 package evidence docs prepared")
