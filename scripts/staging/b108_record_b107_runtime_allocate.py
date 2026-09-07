from pathlib import Path

RUNTIME_SHA = "8e3e10b44e8e627f60e7a831d48f11c7fa9fff4bc4b0446b71588fbc38ade7da"
SCREEN_STREAM_SHA = "5b8d52c002a468ba6d5a79bacc1b922081c0fdc30d71880d0de0fadf9096a0b7"
SCREEN_FINAL_SHA = "037b207c15012633a569087c2024abdd249a8646e3ad030d5726591135c20798"
BASELINE_HEAD = "be286f2f8c98305d9e702252af9c73f27d6431bf"

checkpoint = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
build_index = Path("docs/project/BUILD_TEST_INDEX.md")
project_state = Path("docs/project/PROJECT_STATE.md")
module_status = Path("docs/project/MODULE_STATUS.md")

checkpoint_section = f'''## b107 Human Runtime Partial / b108 assistant-body color allocation — 2026-09-06

Exact b107 Human Runtime evidence:

- Canonical candidate `DEV-send-stream-0.1.0-b107` / Release / iPhone / iOS17.0 / source marker `4bd3501a3092`; diagnostics `ChatGPTClient-Diagnostics-20260905-171244.json`, `sha256:{RUNTIME_SHA}`, 411 events. Screenshots `sha256:{SCREEN_STREAM_SHA}` and `sha256:{SCREEN_FINAL_SHA}` are the exact visual evidence supplied with this run.
- New Chat first protected Send remained Runtime Positive: exactly one `coveredExecutor.requested(target=new_conversation)`, one `sendObserved`, HTTP200 `text/event-stream`, and one `newConversation.authoritativeHandoff(source=protected_send_sse_conversation_id)` started Repository response generation 1 on the adopted authoritative conversation.
- This run did **not** exercise b107 accepted clean-EOF recovery. There is zero exact `stream_ended_without_done`, zero `coveredExecutor.acceptedClientStreamEndRecovery`, zero `acceptedClientRecovery.interrupted`, and zero local `phase=failed`. Instead generation 1 followed normal reasoning/final SSE, reached `event=terminal` / `phase=completed`, and the covered executor emitted normal terminal.
- Normal terminal authoritative convergence is Runtime Positive. Automatic authoritative Detail Sync returned HTTP200 with two visible messages; `liveResponse.reconciled` then `authoritativeReconcile.completed(liveSnapshotCleared=true)` cleared the live projection. This is not proof of the b107 manual-Sync stale-non-active cleanup branch because the tested live generation completed normally rather than entering the b106 accepted-EOF false-failure state.
- Blue body text is Runtime Negative again, now with stronger owner evidence. User reports the assistant body placeholder shown while thinking is blue, SSE reasoning text is normal, and final SSE answer text is blue. The supplied screenshots show the final answer body in the same system-blue family as normal app tint while reasoning/header controls remain independently styled.
- Current source maps that exact visual split to `ConversationMessageCell`: live placeholder and final answer both render through `UILabel messageLabel`; reasoning SSE renders through the separate `UITextView reasoningTextView`. b106 already reset `messageLabel.isHighlighted`, `textColor`, `highlightedTextColor`, and `tintColor` before assigning body `attributedText`, yet b107 reproduces the defect. Therefore residual cell highlight/tint state is rejected as the sufficient owner hypothesis.
- UIKit `UILabel` contract is relevant to the next minimum delta: assigning `attributedText` can update style properties including `textColor`, while assigning `textColor` to a label displaying styled text applies that color to the entire attributed string. Current source establishes `.label` before `attributedText`; b108 will establish the assistant body's final color owner after `attributedText` assignment. User-link styling remains outside this change.

b107 Runtime classification:

- New Chat SSE authoritative identity: **Runtime Positive again**;
- normal reasoning/final/terminal SSE + authoritative post-terminal reconcile: **Runtime Positive**;
- b107 accepted `stream_ended_without_done` same-generation recovery: **Unexercised / Unverified** in this sample;
- b107 manual-Sync stale non-active live cleanup: **Unexercised as the target failure state** in this sample;
- assistant body color consistency: **Runtime Negative**;
- overall `DEV-send-stream`: **Runtime Partial / Stable-Frozen No**.

b108 allocation / minimum scope:

- Allocate and permanently reserve `DEV-send-stream-0.1.0-b108` / `0.1.0 (108)`. No current Build/Test entry uses b108 and parallel PR #35 owns no product build/Candidate identity.
- Preserve all b107 Send/SSE/Repository/recovery behavior unchanged.
- Product scope is exactly `ChatGPTClient.xcodeproj/project.pbxproj` and `ChatGPTClient/Conversation/ConversationFeature.swift`.
- In `ConversationMessageCell.configure`, after assigning `.assistant` body `attributedText`, re-establish `messageLabel.textColor = .label` so the UILabel property is the final uniform body-color owner. Do not alter `reasoningTextView`, response timeline colors, user-link `systemBlue`, markdown semantics, row geometry, SSE parsing, Repository state, retry/recovery, timers, or transport.
- b108 Human Runtime must verify `正在思考…` / assistant final body are normal label color while expanded/live reasoning stays unchanged. The inherited b107 accepted-EOF recovery gate remains open and should be observed if that exact condition naturally occurs; no forced resend or synthetic EOF is added.

Resume/conflict guard:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable; verified pre-record branch head `{BASELINE_HEAD}`; main remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Canonical b107 product/package remain `113fa19d7264b953949770d2e44cb500ded2da6b` / `4bd3501a3092dfe7aad7ea836ba0cb8e42b0d65f`; Artifact `9967821935`; IPA `sha256:7195d89cb9837efc3386c5dd7e030e7f11f10233689416e59c86d1ae4cf055cd`.
- Parallel PR #35 remains research-only and has no `ChatGPTClient/**`, product Xcode Candidate, or exact product-path overlap with this b108 scope.

**Next exact action:** after this Runtime/allocation checkpoint is durably committed, apply only the two-path b108 delta, pass `git diff --check` + Debug Simulator compile, bind package CI to exact b108 product source, then produce one canonical b108 IPA for Human Runtime. Do not claim the inherited b107 accepted-EOF branch Runtime-positive unless exact `stream_ended_without_done` evidence occurs.

'''

state_section = f'''## DEV-send-stream b107 Runtime Partial / b108 body-color gate — 2026-09-06

- Exact canonical b107 diagnostics `sha256:{RUNTIME_SHA}` / 411 events / Release / iPhone / iOS17.0 / source `4bd3501a3092` shows one New Chat protected HTTP200 SSE Send, authoritative SSE conversation-ID handoff, normal reasoning/final stream, `terminal` / generation `phase=completed`, then automatic HTTP200 authoritative Detail reconcile with `liveSnapshotCleared=true`.
- Zero `stream_ended_without_done` / accepted-client EOF recovery diagnostics occurred, so the b107 accepted clean-EOF same-generation branch remains Unexercised. The b107 manual-Sync stale-live target state also did not occur because the generation terminated normally.
- Exact screenshots `sha256:{SCREEN_STREAM_SHA}` / `sha256:{SCREEN_FINAL_SHA}` plus user observation reproduce the assistant body blue-text defect: placeholder/final body blue while reasoning SSE text is normal. Current source maps the split to `ConversationMessageCell.messageLabel` versus `reasoningTextView`; b106 pre-attributedText color/tint reset is Runtime-insufficient.
- b108 is allocated as `0.1.0 (108)` for one narrow `UILabel` body-color ownership correction only. Overall Send/Stream remains Runtime Partial / Stable-Frozen No.

'''

module_section = f'''## DEV-send-stream b107 UI-owner Runtime update / b108 allocation — 2026-09-06

- `ConversationRepository` / covered Send transport remain unchanged by the new defect evidence. b107 normal New Chat Send/terminal/authoritative convergence is Runtime Positive in `sha256:{RUNTIME_SHA}`, but its exact accepted `stream_ended_without_done` recovery branch remains Unexercised.
- UI ownership is now narrower: assistant placeholder/final body uses `ConversationMessageCell.messageLabel` (`UILabel`), while reasoning SSE text uses `reasoningTextView` (`UITextView`). User Runtime reports body blue / reasoning normal and supplied screenshots reproduce final body blue. b106's pre-assignment `messageLabel` reset did not fix it.
- b108 is reserved for the smallest body-rendering correction: reassert assistant `messageLabel.textColor = .label` after its attributed body assignment; do not change reasoning, user-link coloring, row geometry, Repository, SSE, or recovery ownership.
- Module remains Active / Runtime Partial / Stable-Frozen No.

'''

for path, section in ((checkpoint, checkpoint_section), (project_state, state_section), (module_status, module_section)):
    text = path.read_text()
    if RUNTIME_SHA not in text:
        path.write_text(section + text)

text = build_index.read_text()
lines = text.splitlines()
b107_index = None
b108_found = False
for i, line in enumerate(lines):
    if line.startswith("| `DEV-send-stream-0.1.0-b108` |"):
        b108_found = True
    if line.startswith("| `DEV-send-stream-0.1.0-b107` |"):
        b107_index = i
        lines[i] = f"| `DEV-send-stream-0.1.0-b107` | `DEV-send-stream` | `0.1.0 (107)` | accepted-SSE EOF same-generation recovery product `113fa19d7264b953949770d2e44cb500ded2da6b`; package `4bd3501a3092dfe7aad7ea836ba0cb8e42b0d65f`; PR #29 | staging `33960451799/101291316464` exact two-product-path scope + `git diff --check` + Simulator passed; Push `33960627676/101291785599` passed; PR `33960629168/101291789461` passed; canonical Artifact `9967821935`; ZIP `d2036ed0372b16c7690c9d3b324d680db6a522fd5ace26d27afa8733a95a9585`; IPA `7195d89cb9837efc3386c5dd7e030e7f11f10233689416e59c86d1ae4cf055cd`; package verified Build107/Candidate/source/Release/iOS14+/`[1,2]`/arm64 | Runtime `sha256:{RUNTIME_SHA}` / 411 events: New Chat one-Send SSE authoritative ID + normal reasoning/final/terminal + automatic HTTP200 authoritative reconcile with `liveSnapshotCleared=true` Positive. Zero exact `stream_ended_without_done` / accepted EOF recovery diagnostics, so b107 EOF branch Unexercised; target stale-non-active manual-Sync state also Unexercised. Screenshots `{SCREEN_STREAM_SHA[:12]}...` / `{SCREEN_FINAL_SHA[:12]}...` reproduce assistant body blue while reasoning SSE is normal; b106 cell-state reset remains insufficient | **Runtime Partial / normal New Chat terminal+reconcile Positive / accepted-EOF recovery Unexercised / assistant body color Negative / superseded for test priority by b108 / Stable-Frozen No; permanently reserved** |"

if b107_index is None:
    raise SystemExit("b107 row missing")
if b108_found:
    raise SystemExit("b108 already allocated")
b108_row = "| `DEV-send-stream-0.1.0-b108` | `DEV-send-stream` | `0.1.0 (108)` | allocated from exact b107 assistant body-vs-reasoning color split; product source pending; PR #29 | Runtime/allocation recorded before product write; intended exact product scope: Xcode Build/Candidate + `ConversationFeature.swift` assistant UILabel post-attributedText color ownership | Human Runtime pending: assistant `正在思考…` and final body must render normal label color while reasoning SSE remains unchanged; inherited b107 accepted-EOF branch remains evidence-gated if naturally exercised | **Allocated / product staging pending / Human Runtime pending / Stable-Frozen No; permanently reserved** |"
lines.insert(b107_index, b108_row)
build_index.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))

print("b107 Runtime recorded; b108 allocated")
