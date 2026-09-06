from pathlib import Path

checkpoint_path = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
index_path = Path("docs/project/BUILD_TEST_INDEX.md")

marker = "## b105 Human Runtime Partial / b106 SSE identity + assistant-cell reset allocation — 2026-09-05"
checkpoint = checkpoint_path.read_text()
if marker not in checkpoint:
    prefix = f'''{marker}

Exact b105 Human Runtime evidence / rejection:

- Canonical b105 remains permanently reserved: product `6ef4e874d7c2c5f144ab7e784f7a81755d1b2f59`, package `93ab92a9a4a7b8a020ac209f6a82088dc77acbce`, Artifact `9956018294`, IPA `sha256:d162a7132ff830d3a2f6eb85a2b4a5b4ebc2d9f84531b01418912c99109e5095`.
- Human Runtime proved the New Chat protected-Send transport itself works: exactly one `target=new_conversation` covered Send, one `sendObserved`, HTTP200 `text/event-stream`, one local response generation, reasoning + four tool items + 4526 final characters + terminal, and no duplicate protected Send.
- b105 adopted the pre-fetch official page-route identity `sha256:893a1901dd3b` as authoritative. Terminal authoritative Detail for that ID returned HTTP400. A later successful conversation-list refresh exposed the actual newly-created conversation under different identity `sha256:8170ab408a21`; Detail for that real ID returned HTTP200 with two visible messages and latest-user length 84, matching the tested first prompt. Therefore the b105 premise "pre-fetch page route identity is the final authoritative server conversation ID" is Runtime Negative.
- User video `RPReplay_Final1788590864.mp4`, exact `sha256:c415187dfb5c2b700f17550f0d429376026d795d55aaf168c304b8586251445b`, 6,152,300 bytes, ~8.6s, confirms a second independent Runtime defect: one long assistant answer alternates between system-blue and normal label-colored text at row/block boundaries while scrolling. This is not global tint/theme behavior. Current source splits long messages into 1200-character presentation rows and explicitly assigns `UIColor.label` to assistant attributed text; Runtime therefore contradicts intended cell state. Raw Markdown/citation rendering remains later `DEV-message-rendering` scope and is not folded into this fix.

Runtime classification:

- b105 one protected New Chat Send + SSE reasoning/tools/final: **Runtime Positive**.
- b105 authoritative new-chat identity handoff + terminal Detail/list convergence: **Runtime Negative / rejected**.
- long assistant per-row color consistency: **Runtime Negative**.
- overall b105: **Runtime Partial / superseded for test priority by b106 / Stable-Frozen No**.

b106 allocation / evidence-backed minimum scope:

- Allocate and permanently reserve `DEV-send-stream-0.1.0-b106` / `0.1.0 (106)`. No existing b106 row existed before this allocation.
- Keep exactly one page-owned protected Send. Do not invent/persist a server ID and do not use the pre-fetch page route as authoritative for New Chat.
- For New Chat only, allow the one protected Send to start from the official root composer. The covered transport keeps any pre-identity lifecycle events locally until the first exact top-level `conversation_id` string observed in that same protected Send's parsed SSE payload. That SSE identity is the only new authoritative handoff source authorized by b106.
- On the first SSE identity, emit one `.conversationCreated(realID)` before replaying the transport-local pre-identity events; Root then re-keys the same executor, creates exactly one Repository generation for that real ID, and continues the existing reasoning/tools/final/terminal path. A conflicting later SSE identity is an identity error. Terminal without any SSE identity fails visibly and never fabricates an ID.
- Accepted-client hard-Web recovery remains unchanged once authoritative identity/generation exists. If WebContent dies in the narrow post-HTTP200/pre-SSE-identity window, fail/no-resend rather than guessing recovery identity.
- UI fix is limited to `ConversationMessageCell` reuse/configuration state: explicitly reset `messageLabel` highlight/text/tint semantics per configuration before assigning role-specific attributed text, while preserving actual user-link `.systemBlue` attributes. Do not replace the renderer or mix future Markdown/citation rendering into b106.
- No polling, timer/watchdog, retry loop, duplicate Send, regenerate, challenge replay, guessed Native resume/status, fake conversation identity, or second response/content store.

Resume/conflict guard:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable; verified pre-b106 branch head `623bf5c4c8bc285f3075ae98a7f9a5af6c5679d4`; target `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Parallel PR #35 remains draft research-only at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`, with no `ChatGPTClient/**` product or Candidate-number overlap.
- Intended b106 product scope remains exactly `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/RootViewController.swift`, and `ChatGPTClient/Conversation/ConversationFeature.swift`.

Batch recovery point:

- batch A: record this b105 Runtime classification + b106 reservation in checkpoint/index and push before product changes;
- batch B: apply only the exact three-product-path b106 delta, run `git diff --check` + Debug Simulator compile, then commit/push product;
- batch C: bind formal package workflow to the exact b106 product commit, require same-source Push + PR CI, canonical Artifact and independent IPA identity verification, then update durable state/rules/adapter/checkpoint/PR metadata before Human Runtime;
- recovery must not rewrite canonical b105/b104/b103 package identities, PR #35, accepted-client hard-Web recovery, Native `-1005` recovery, or previously reserved Candidates.

**Next exact action:** complete batch B only. Human Runtime b106 must prove one protected New Chat Send, authoritative handoff source `protected_send_sse_conversation_id`, terminal Detail HTTP200/list reconciliation on that same ID, and no assistant blue/black 1200-character-row alternation on a long answer.

'''
    checkpoint_path.write_text(prefix + checkpoint)

index = index_path.read_text()
if "DEV-send-stream-0.1.0-b106" not in index:
    lines = index.splitlines()
    b105_index = next((i for i, line in enumerate(lines) if line.startswith("| `DEV-send-stream-0.1.0-b105`")), None)
    if b105_index is None:
        raise SystemExit("b105 row not found")
    b106 = "| `DEV-send-stream-0.1.0-b106` | `DEV-send-stream` | `0.1.0 (106)` | allocated from b105 Runtime rejection; product source pending; PR #29 | Batch A allocation recorded before product write; intended exact product scope: Xcode Build/Candidate + `RootViewController.swift` SSE-authoritative New Chat handoff + `ConversationFeature.swift` assistant-cell state reset; validation pending | Human Runtime pending: require one New Chat protected Send, first exact protected-Send SSE `conversation_id` authoritative adoption, one Repository generation through terminal + HTTP200 Detail/list convergence, and no per-row blue assistant-text corruption | **Allocated / product staging pending / Human Runtime pending / Stable-Frozen No; permanently reserved** |"
    lines.insert(b105_index, b106)
    old = lines[b105_index + 1]
    parts = old.split("|")
    if len(parts) < 8:
        raise SystemExit("unexpected b105 row format")
    parts[5] = " Human Runtime Partial: one New Chat protected Send + HTTP200 SSE + one generation + reasoning/4 tools/4526 final chars + terminal succeeded with no duplicate Send; pre-fetch route identity `sha256:893a1901dd3b` was rejected because terminal Detail returned HTTP400 while later list/Detail identified the real new conversation as `sha256:8170ab408a21` with HTTP200/two messages/latest-user 84 chars. Exact video `sha256:c415187dfb5c2b700f17550f0d429376026d795d55aaf168c304b8586251445b` also proves long assistant text alternates blue/normal across presentation rows "
    parts[6] = " **Runtime Partial / new-chat route-ID handoff Negative + assistant row-color consistency Negative / superseded by b106 test priority / Stable-Frozen No; permanently reserved** "
    lines[b105_index + 1] = "|".join(parts)
    index_path.write_text("\n".join(lines) + "\n")

print("b106 allocation/runtime recorder complete")
