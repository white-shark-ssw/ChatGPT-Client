from pathlib import Path

B106_PRODUCT = "028100bb79d82e99b62a610e9f30b9f9b3bd7f5c"
B106_PACKAGE = "a02042608911b891a4e9730a2bb3974168c4308a"
B106_STAGING = "33953874027/101273525329"
B106_PUSH = "33953950307/101273735236"
B106_PR = "33953951744/101273739204"
B106_ARTIFACT = "9965747978"
B106_ZIP_SHA = "0558f3926b921b4e06b6336e1a251a8c1cbab661038cd34a303a83046039e4e2"
B106_IPA_SHA = "65acacb62506449bb65356a561603062a0f2b5bae4dc266a811480868b052288"
B106_DIAG_SHA = "b52e6177b2d3d44c124419c18ec88a356860f8a169a12f1a4cc6e46bb8e6faec"
B106_VIDEO_SHA = "fd358795b1fb78576eaa160416defae95389055c174b04fd37a471f83f161b02"
BASELINE = "9541bcb22cab87254c881272b7226bef670d2e35"

checkpoint = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
text = checkpoint.read_text()
marker = "## b106 Human Runtime Partial / b107 accepted-SSE EOF handoff allocation — 2026-09-05"
if marker not in text:
    section = f'''{marker}

Exact b106 package identity restored from repository/package evidence:

- Candidate `DEV-send-stream-0.1.0-b106` / `0.1.0 (106)` remains permanently reserved. Product `{B106_PRODUCT}`; canonical package `{B106_PACKAGE}`; staging `{B106_STAGING}`; Push `{B106_PUSH}`; PR `{B106_PR}`; Artifact `{B106_ARTIFACT}`; ZIP `sha256:{B106_ZIP_SHA}`; IPA `sha256:{B106_IPA_SHA}`.
- Exact Human Runtime diagnostics `sha256:{B106_DIAG_SHA}`, 65,950 bytes, identify Release Build106/Candidate b106/source `a02042608911` on iPhone/iOS17.0. Exact accompanying video `sha256:{B106_VIDEO_SHA}` remains visual evidence.

b106 Human Runtime classification:

- New Chat protected-Send transport + first exact top-level protected-Send SSE `conversation_id` authoritative handoff: **Runtime Positive**. One protected `target=new_conversation` Send was observed, HTTP200 `text/event-stream` was accepted, the adopted conversation remained the same target through later authoritative Detail, and no duplicate protected Send was observed.
- Accepted client SSE clean EOF without exact `[DONE]`: **Runtime Negative**. At 08:17:37 the accepted stream emitted exact `stream_ended_without_done`; b106 routed that symbolic receive condition through `failCurrent`, marked Repository generation 1 `phase=failed`, and released the executor even though the server turn had completed.
- Authoritative recovery proves the failure was local: manual Sync of the same adopted conversation returned HTTP200 at 08:17:54 with two visible messages and latest-user length 84; the official covered page subsequently reported `COMPLETE`.
- Stale-live presentation cleanup: **Runtime Negative**. After that Sync the selected Detail had `presentationRowCount=5` while the failed live projection remained `livePresentationRowCount=2`; current table row authority concatenates both sets, matching the video where the complete answer is followed by a duplicate old prompt/reasoning/`回答失败` tail.
- b106 assistant label state-reset correction remains **Runtime Negative / insufficient**: blue assistant text is still visible in the exact b106 video. No further color patch is authorized without stronger owner evidence.
- Overall b106: **Runtime Partial / superseded for test priority by b107 / Stable-Frozen No**.

b107 evidence-backed minimum scope:

- Allocate and permanently reserve `DEV-send-stream-0.1.0-b107` / `0.1.0 (107)`. No current Build/Test entry uses b107.
- Preserve b106 SSE conversation identity handoff unchanged.
- Add one distinct covered event for exact `stream_ended_without_done` only when the client protected Send has already received HTTP200 SSE acceptance, response activity is still owned by that executor, and an authoritative conversation ID already exists. Clear/release only the ended receive executor transport; do **not** mutate the Repository generation to failed.
- Root handles that event exactly like the already Runtime-positive b103 accepted-client transport interruption: preserve the same prompt-owned Repository generation and attach one fresh covered observer while active, or leave it for the existing foreground recovery if inactive. Policy is `no_resend_same_generation`.
- Source inspection rejects using Native Detail message presence as a new terminal proof: ordinary visible assistant parsing does not retain a normal assistant `finished_successfully` bit in `ConversationDetail`, so b107 must not clear an active generation merely because a Detail currently contains assistant text.
- Fix the proven manual-Sync duplication using the existing owner primitive only: after successful manual Sync, if the current client-owned live snapshot is already non-active, call existing `clearLiveResponseAfterAuthoritativeReconcile` with the authoritative selected Detail message count before rearming observation. This removes the stale failed/terminal projection when authoritative state advanced beyond its baseline; no new response store or completion flag is added.
- Do not change `ConversationMessageCell` in b107. The blue-text defect stays open and separately evidence-gated.
- No polling, timer/watchdog, retry loop, duplicate Send, regenerate, challenge replay, guessed Native resume/status, fake conversation ID, new server-completion heuristic, or second response/content store.

Resume/conflict guard:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable. Pre-b107 safe baseline `{BASELINE}`. Four preceding connector-cleanup history commits are tree-neutral relative to `e5b8041d...`; no product path differs because of them.
- `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Parallel PR #35 remains draft research-only at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`, with no product Xcode/`ChatGPTClient/**`/Candidate overlap.
- Intended b107 product scope is exactly `ChatGPTClient.xcodeproj/project.pbxproj` and `ChatGPTClient/RootViewController.swift`.

Batch recovery point:

- Batch A: record this b106 Runtime classification, restore exact b106 package truth in Build/Test, and reserve b107 before product changes.
- Batch B: apply only the exact two-product-path b107 delta, run `git diff --check` + Debug Simulator compile, then commit/push exact product.
- Batch C: bind formal b107 package workflow to the exact b107 product commit, require same-source Push + PR CI, canonical Artifact and independent IPA identity/hash verification, then update durable state/rules/adapter/checkpoint/PR metadata before Human Runtime.
- Recovery must not alter b106/b105 canonical identities, b106 SSE-ID handoff, b103 hard-Web recovery, b101 `-1005` recovery, PR #35, or any previously reserved Candidate.

**Next exact action:** complete Batch B only after this allocation is durably committed. Human Runtime b107 must prove accepted `stream_ended_without_done` no longer creates `phase=failed` or `回答失败`, same-generation no-resend observer recovery reaches authoritative terminal convergence, and manual Sync cannot leave authoritative rows plus a stale failed live tail.
'''
    checkpoint.write_text(section.rstrip() + "\n\n" + text)

index = Path("docs/project/BUILD_TEST_INDEX.md")
lines = index.read_text().splitlines()
b106_found = False
b107_found = False
for i, line in enumerate(lines):
    if line.startswith("| `DEV-send-stream-0.1.0-b107`"):
        b107_found = True
    if line.startswith("| `DEV-send-stream-0.1.0-b106`"):
        b106_found = True
        lines[i] = f"| `DEV-send-stream-0.1.0-b106` | `DEV-send-stream` | `0.1.0 (106)` | SSE-authoritative New Chat handoff + assistant-cell state reset product `{B106_PRODUCT}`; package `{B106_PACKAGE}`; PR #29 | staging `{B106_STAGING}` exact three-product-path scope + Simulator passed; Push `{B106_PUSH}` passed; PR `{B106_PR}` passed; canonical Artifact `{B106_ARTIFACT}`; ZIP `{B106_ZIP_SHA}`; IPA `{B106_IPA_SHA}`; package independently verified `0.1.0 (106)` / Candidate b106 / source `a02042608911` / Release / iOS14+ / `[1,2]` / arm64 | Runtime `sha256:{B106_DIAG_SHA}`: one protected New Chat HTTP200 SSE Send adopted exact SSE conversation ID and later authoritative Detail used the same target, but exact accepted `stream_ended_without_done` was incorrectly converted to generation `phase=failed`; manual same-ID Sync then returned HTTP200 with two visible messages while UI retained authoritative 5 rows + stale failed live 2 rows. Video `sha256:{B106_VIDEO_SHA}` also shows blue assistant text remains | **Runtime Partial / SSE authoritative identity Positive / accepted-EOF failure + stale-live duplication Negative / assistant blue-text reset Negative / superseded by b107 test priority / Stable-Frozen No; permanently reserved** |"

if not b106_found:
    raise SystemExit("b106 row missing")
if b107_found:
    raise SystemExit("b107 already allocated")
header_index = next(i for i, line in enumerate(lines) if line.startswith("| `DEV-send-stream-0.1.0-b106`"))
b107_row = f"| `DEV-send-stream-0.1.0-b107` | `DEV-send-stream` | `0.1.0 (107)` | allocated from exact b106 Runtime accepted-SSE EOF false-failure + stale-live duplication; product source pending; PR #29 | Batch A Runtime classification/allocation recorded before product write; intended exact product scope: Xcode Build/Candidate + `RootViewController.swift` accepted EOF same-generation handoff and manual authoritative stale-live cleanup | Human Runtime pending: exact accepted `stream_ended_without_done` must preserve one Repository generation and recover through a fresh covered observer with no resend/no failure; manual Sync after any non-active client live snapshot must not leave authoritative rows plus stale live rows | **Allocated / product staging pending / Human Runtime pending / Stable-Frozen No; permanently reserved** |"
lines.insert(header_index, b107_row)
index.write_text("\n".join(lines) + "\n")

print("b106 Runtime classified; b106 package truth restored; b107 allocated")
