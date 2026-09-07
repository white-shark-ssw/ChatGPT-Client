from pathlib import Path


PRODUCT = "6ef4e874d7c2c5f144ab7e784f7a81755d1b2f59"
PACKAGE = "93ab92a9a4a7b8a020ac209f6a82088dc77acbce"
STAGING = "33923512745/101186860450"
PUSH = "33923732331/101187538891"
PR = "33923735651/101187548902"
ARTIFACT = "9956018294"
ZIP_SHA = "ba53bc8e50e1b89056565e3a557e196ef6b9c5db76e3b40dd28a0536e81d6921"
IPA_SHA = "d162a7132ff830d3a2f6eb85a2b4a5b4ebc2d9f84531b01418912c99109e5095"


def prepend(path: str, marker: str, section: str) -> None:
    file = Path(path)
    text = file.read_text()
    if marker in text:
        raise SystemExit(f"marker already present: {marker}")
    file.write_text(section + text)


index = Path("docs/project/BUILD_TEST_INDEX.md")
lines = index.read_text().splitlines()
matches = [i for i, line in enumerate(lines) if line.startswith("| `DEV-send-stream-0.1.0-b105` |")]
if len(matches) != 1:
    raise SystemExit(f"expected one b105 index row, found {len(matches)}")
lines[matches[0]] = f"| `DEV-send-stream-0.1.0-b105` | `DEV-send-stream` | `0.1.0 (105)` | authoritative new-chat first-Send product `{PRODUCT}`; package `{PACKAGE}`; PR #29 | corrected staging `{STAGING}` exact three-product-path scope + Simulator passed; Push `{PUSH}` passed; PR `{PR}` passed; canonical Artifact `{ARTIFACT}`; ZIP `{ZIP_SHA}`; IPA `{IPA_SHA}`; package independently verified `0.1.0 (105)` / Candidate b105 / source `93ab92a9a4a7` / Release / iOS14+ / `[1,2]` / arm64 | Human Runtime pending: root New Chat must obtain the official authoritative conversation ID before protected fetch proceeds, hand off the same visible draft to one Repository generation, complete reasoning/tools/final + terminal Detail reconcile, and automatically reconcile the new conversation into the sidebar with no duplicate Send | **Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity verified / Human Runtime pending / Stable-Frozen No; permanently reserved** |"
index.write_text("\n".join(lines) + "\n")

checkpoint_section = f"""## b105 authoritative new-chat first-Send — package ready 2026-09-05

Exact product/package evidence:

- Candidate `DEV-send-stream-0.1.0-b105` / `0.1.0 (105)`, permanently reserved. Exact product `{PRODUCT}`; canonical package source `{PACKAGE}`.
- b105 product delta is exactly three product paths: `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/Conversation/ConversationFeature.swift`, `ChatGPTClient/RootViewController.swift`.
- Corrected staging `{STAGING}` passed exact three-product-path audit, `git diff --check` and Debug Simulator compile before committing/pushing the product. Earlier run `33922377182` was a zero-job YAML parse failure and run `33923319785/101186252076` stopped at a deterministic patch-guard ambiguity after Batch A; neither wrote b105 product code and neither is product/Simulator failure evidence.
- Formal Push `{PUSH}` and PR `{PR}` both passed on exact package source `{PACKAGE}`.
- Canonical Push Artifact `{ARTIFACT}`; GitHub Artifact digest and independently recomputed ZIP SHA-256 both equal `{ZIP_SHA}`.
- Canonical IPA `ChatGPTClient-0.1.0-b105-dev-send-stream.ipa`; independent SHA-256 `{IPA_SHA}`, matching sidecar. Package inspection verifies `com.whitesharkssw.chatgptclient`, `0.1.0 (105)`, Candidate b105, source `93ab92a9a4a7`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS, Mach-O 64-bit arm64.

Behavior / evidence boundary:

- New Chat opens a Native draft with no fake server conversation ID. One covered official root-page executor owns the first protected Send/challenge flow.
- For that first Send, the bridge permits the real protected `/backend-api/f/conversation` fetch only after the official page route exposes a concrete authoritative conversation ID. Missing identity emits `new_conversation_identity_missing` and blocks the protected fetch rather than creating an untrackable server turn.
- `.conversationCreated(realID)` re-keys the same covered executor to the real server ID, selects it only if the draft is still the visible surface, and starts exactly one `ConversationRepository` live generation for that ID. Existing b103/b104 accepted-client hard-Web recovery and terminal authoritative Detail reconciliation remain unchanged.
- After successful terminal Detail for a newly created conversation, exactly one forced conversation-list refresh reconciles the server conversation into the sidebar. No polling, retry loop, timer/watchdog, resend/regenerate, challenge replay, guessed Native resume, fake persisted ID or second response/content store is added.
- Stop is not implemented by b105; exact response-scoped Stop route/target/ack evidence remains required before a later change.
- b105 is package-qualified only. Human Runtime is Pending; Stable/Frozen remains No.
- Any later docs/staging commit or Artifact does not replace canonical b105 package source `{PACKAGE}`, Artifact `{ARTIFACT}` or IPA SHA `{IPA_SHA}`.

Evidence ladder: **Code written / exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**

**Next exact action:** install only canonical b105 and run one new-conversation first Send from the Native draft. Require one official authoritative-ID handoff before protected fetch, exactly one HTTP200 SSE protected Send, one Repository generation through terminal + authoritative Detail, and one sidebar list reconciliation. Export diagnostics. Do not test/claim Stop in this candidate.

"""
prepend("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md", "## b105 authoritative new-chat first-Send — package ready 2026-09-05", checkpoint_section)

state_section = f"""## DEV-send-stream b105 authoritative new-chat first Send package ready — 2026-09-05

- b105 fills the missing new-conversation first-Send path without changing TD-029 ownership: official Web still owns protected Send/challenge; `ConversationRepository` remains sole Native response/content authority. Native creates no fake server conversation ID.
- Product `{PRODUCT}` is exact three-product-path scope. Corrected staging `{STAGING}`, Push `{PUSH}` and PR `{PR}` passed. Canonical Artifact `{ARTIFACT}`, ZIP `sha256:{ZIP_SHA}`, IPA `sha256:{IPA_SHA}`; package independently verified Build105/Candidate b105/source `93ab92a9a4a7`/Release/iOS14+/arm64.
- First new-chat protected fetch is gated on a real official-page route conversation identity. Missing identity blocks the fetch with `new_conversation_identity_missing`; successful identity handoff re-keys the same executor and starts one Repository generation. Terminal Detail then performs one list refresh for sidebar convergence.
- Human Runtime pending. Stop remains unimplemented pending exact route/target/ack evidence; true background execution and b101 exact `-1005` branch remain separate evidence boundaries. Stable-Frozen No.

"""
prepend("docs/project/PROJECT_STATE.md", "## DEV-send-stream b105 authoritative new-chat first Send package ready — 2026-09-05", state_section)

module_section = f"""## DEV-send-stream b105 new-chat authoritative identity handoff — 2026-09-05

- `ConversationRepository` remains sole Native conversation/response/content authority; `CoveredWebSendExecutor` remains official-page protected-Send transport. b105 adds no second store and no fake persisted conversation identity.
- New Chat draft starts with no selected server ID. The official root page may submit only after its own route yields the real conversation ID; then the same executor is re-keyed and exactly one Repository live generation is created for that real ID. Successful terminal Detail triggers one authoritative list refresh so the server-created conversation enters the sidebar.
- Exact product/package `{PRODUCT}` / `{PACKAGE}`; staging + Push + PR CI passed; Artifact `{ARTIFACT}`; IPA `sha256:{IPA_SHA}` independently verified. Human Runtime pending; module remains Active / Runtime Partial overall / Stable-Frozen No.

"""
prepend("docs/project/MODULE_STATUS.md", "## DEV-send-stream b105 new-chat authoritative identity handoff — 2026-09-05", module_section)

rules_section = """## New-chat first Send authoritative identity — b105 package rule 2026-09-05

- A Native New Chat draft has no server conversation identity and must not synthesize, persist or route on a fake ID.
- The first protected Send remains page-owned. Before the official `/backend-api/f/conversation` fetch is allowed to proceed for a new-chat Send, the official page itself must expose a concrete conversation ID through the already-evidenced conversation route parser (`/c/{id}` or scoped `/g/{scope}/c/{id}`).
- If the official identity is absent at that protected-fetch boundary, block that fetch and fail visibly with the symbolic `new_conversation_identity_missing`; do not send first and recover/guess identity later.
- Once the official ID is observed, re-key the same covered executor exactly once and create exactly one `ConversationRepository` live response generation for the real ID. Do not start a second protected Send or second response owner during handoff.
- If the user left the draft before identity adoption, the new server turn may continue hidden under its real ID; do not force visible selection back. A successful terminal authoritative Detail may trigger one conversation-list refresh to reconcile the real server conversation into the sidebar.
- Existing accepted-client hard-Web no-resend recovery applies after explicit HTTP200 SSE acceptance. No polling, timer/watchdog, guessed Native resume/status, challenge replay, duplicate Send/regenerate or second response/content store is authorized.
- Stop remains evidence-gated and is not part of b105.

"""
prepend("docs/project/PROJECT_SPECIFIC_RULES.md", "## New-chat first Send authoritative identity — b105 package rule 2026-09-05", rules_section)

adapter_section = f"""# Web Send Adapter / Rule Update Playbook

## DEV-send-stream b105 authoritative new-chat first Send — package-ready override 2026-09-05

- Historical b62 Runtime is the identity evidence: an official root/new-chat page transitioned to an existing-conversation route before the first protected `/backend-api/f/conversation` fetch and then returned HTTP200 `text/event-stream`. b105 consumes that official route identity; Native does not invent one.
- Exact product `{PRODUCT}`; canonical package source `{PACKAGE}`; corrected staging `{STAGING}`, Push `{PUSH}`, PR `{PR}` all passed. Canonical Artifact `{ARTIFACT}`, ZIP `{ZIP_SHA}`, IPA `{IPA_SHA}`; Build105/Candidate b105/source `93ab92a9a4a7`/Release/iOS14+/arm64 independently verified.
- New-chat bridge rule: when `submit(text, newConversation=true)` reaches the protected fetch interception, `currentConversationID()` must already resolve from the official route. If absent, clear the local submit marker, emit only symbolic `new_conversation_identity_missing`, throw before `originalFetch`, and never create an untracked protected turn.
- When present, emit `send_observed` with that official conversation ID before forwarding the one real protected fetch. Native `.conversationCreated(realID)` re-keys the same executor and starts one Repository generation; normal protected-Send SSE filtering and b103/b104 post-acceptance hard-Web recovery remain unchanged.
- Do not infer new-chat identity from title text, DOM message text, list position, generated UUID, guessed route, WebSocket body, elapsed time or a second request. No retry/poll/watchdog/resend/challenge replay.
- Human Runtime pending; Stop is outside this override and remains evidence-gated.

"""
adapter = Path("docs/project/WEB_SEND_ADAPTER.md")
adapter_text = adapter.read_text()
header = "# Web Send Adapter / Rule Update Playbook\n\n"
if not adapter_text.startswith(header):
    raise SystemExit("WEB_SEND_ADAPTER header mismatch")
if "## DEV-send-stream b105 authoritative new-chat first Send — package-ready override 2026-09-05" in adapter_text:
    raise SystemExit("b105 adapter marker already present")
adapter.write_text(adapter_section + adapter_text[len(header):])
