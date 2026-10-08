from pathlib import Path


checkpoint = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
cp = checkpoint.read_text()
marker = "## b105 new-chat first-Send authoritative handoff allocation — 2026-09-05\n"
if marker in cp:
    raise SystemExit("b105 checkpoint marker already exists")
section = """## b105 new-chat first-Send authoritative handoff allocation — 2026-09-05

User requested autonomous continuation toward completing `DEV-send-stream`. Exact b104 normal/background-return Runtime remains Positive and canonical b104 is unchanged; b105 is a new isolated gate for the genuinely missing new-conversation first Send path.

Evidence / scope:

- Historical exact b62 iPhone/iOS17 Runtime opened the official root page as `new_or_other`, then on the first Native submit the official protected `/backend-api/f/conversation` interception already reported `pageKind=existing_conversation` in the same timestamp before HTTP200 `text/event-stream`; the response stream also exposed structural `conversation_id` keys. This proves the official page creates/owns the authoritative conversation identity during first Send and authorizes reading that identity from the official route; Native must not invent a server ID.
- Current b104 product has only `sendExistingConversation`, requires a selected authoritative conversation ID, has no New Chat control and no pending->authoritative handoff. Therefore this is a real missing Phase-9 product path, not a speculative enhancement.
- Allocate and permanently reserve `DEV-send-stream-0.1.0-b105` / `0.1.0 (105)`. Stable/Frozen remains No.
- b105 must keep protected Send page-owned. Root/new-chat Send is allowed only when the official page has already transitioned to a concrete `/c/{id}` (or scoped equivalent parsed by the existing route parser) before the protected fetch is allowed to proceed. If the authoritative identity is still missing, the bridge must block that first fetch rather than send an untrackable turn.
- After official identity discovery, `ConversationRepository` becomes the sole Native response owner for that real ID; no fake/persistent local conversation ID is created. The same covered executor is re-keyed to the authoritative ID, one live generation is created, and existing b103/b104 accepted-client recovery + terminal authoritative Detail reconciliation remain unchanged.
- A single authoritative list refresh after successful terminal Detail may reconcile the new conversation into the sidebar. No polling/retry/watchdog/timer/resend/challenge replay/second response store.
- Stop is explicitly excluded from b105 because current repo evidence still lacks exact response-scoped Stop route/target/ack proof. Follow-tail/Stop remain later gates; do not guess them into this candidate.

Resume/conflict guard:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable; pre-staging product/docs head `8a98e06465222bb814972318a6d8db7c25a2b20b`; target `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Parallel PR #35 remains research-only with no product/Candidate overlap. `BUILD_TEST_INDEX.md` contained no b105 before this allocation.
- Intended product scope is exactly `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/RootViewController.swift`, and `ChatGPTClient/Conversation/ConversationFeature.swift`.

Batch recovery point:

- batch A: this checkpoint + Build/Test reservation, committed before product changes;
- batch B: apply only the exact three-product-path b105 delta, run `git diff --check` and Debug Simulator compile, then commit/push product;
- batch C after product commit: bind formal packaging to the exact b105 product head, require Push + PR CI, canonical Artifact and independent IPA identity verification, then update durable package docs/PR metadata before Human Runtime;
- recovery must not alter b104 canonical Artifact/package identity, b103 recovery logic, PR #35, or previously reserved Candidates.

**Next exact action:** complete batch B only; if exact scope/Simulator passes, bind formal b105 packaging to that exact product commit.

"""
checkpoint.write_text(section + cp)

index = Path("docs/project/BUILD_TEST_INDEX.md")
lines = index.read_text().splitlines()
if any("DEV-send-stream-0.1.0-b105" in line for line in lines):
    raise SystemExit("b105 already reserved")
insert_at = next(i for i, line in enumerate(lines) if line.startswith("| `DEV-send-stream-0.1.0-b104` |"))
row = "| `DEV-send-stream-0.1.0-b105` | `DEV-send-stream` | `0.1.0 (105)` | new-chat first-Send authoritative handoff; product pending; PR #29 | b104 Runtime evidence + exact historical b62 root->official-conversation protected-Send identity evidence authorize the bounded implementation; exact three-product-path staging + Simulator pending | Human Runtime pending: root New Chat must obtain official authoritative ID before protected fetch proceeds, then one Repository generation must stream/terminal/reconcile with no duplicate Send and sidebar list convergence | **Allocated / product pending / Runtime pending / Stable-Frozen No; permanently reserved** |"
lines.insert(insert_at, row)
index.write_text("\n".join(lines) + "\n")
