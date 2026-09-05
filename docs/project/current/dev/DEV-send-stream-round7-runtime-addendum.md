## b113 stacked integration recovery point — DEV-send-stream owner 2026-09-06

Selected owner / verified pre-integration state:

- Work ID `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable at exact pre-integration head `50432b8743f3391a8174a3b7aae745298082d433`; target `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Canonical DEV-send-stream-owned candidate remains permanently reserved b112: product `3957b806f32f0995ceb9cf8f9487aba939f3b306`, package `b5e3164721e01ceb1fe320ebd290bda79a921fc2`, Artifact `9975978222`, Human Runtime Positive for the role-isolated assistant-color fix. Overall Send/Stream remains Runtime Partial / Stable-Frozen No because accepted clean-EOF recovery is still Unexercised.
- Stacked dependency PR #36 `DEV-message-rendering` is open/mergeable with base exactly `dev/send-stream-20260829@50432b8743f3391a8174a3b7aae745298082d433` and head `d5d761bfad26bc90953488ccd5a96452bf356b3a`.
- PR #36 canonical b113 identity remains owned by `DEV-message-rendering`: Candidate `DEV-message-rendering-0.1.0-b113` / Build113, product `7d1ddc8eaa164c9b307f525b00bb0e1404f395e9`, package `75ccad15208610c2b0420033846f9bb15bbdb494`, Artifact `9976713893`, IPA `sha256:2cf62b87117f9279816de68f2ed3ce83768d203198b555fe4fe0042f8d367c3f`, Human Runtime Positive for the tested native message-presentation scope.
- Compare `75ccad15208610c2b0420033846f9bb15bbdb494..d5d761bfad26bc90953488ccd5a96452bf356b3a` proves all post-package commits are docs/tooling only; no `ChatGPTClient/**` or Xcode product path changed after the canonical b113 package source.
- Parallel PR #35 remains draft research-only at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142` and owns no product `ChatGPTClient/**`, product Xcode Candidate, or Build113 identity.

Integration batches:

- **Batch I0 — completed**: recovery point recorded; recorder run `33992571002` succeeded and bot committed `494ee22d0e9861d373207c91e6b539c8f9b26410`. Recorder was then made idempotent at tooling-only commit `d265d265a7e5382834363e1e73ca7c91a5489cc4`; run `33992707723` succeeded without product changes.
- **Batch I1 — completed**: after base advancement GitHub REST recomputed PR #36 as `mergeable=true / mergeable_state=clean / rebaseable=true`; head remains exact `d5d761bfad26bc90953488ccd5a96452bf356b3a`. No product conflict exists.
- **Batch I2 — next**: merge PR #36 into `dev/send-stream-20260829` using expected head `d5d761bfad26bc90953488ccd5a96452bf356b3a`. This integrates already-tested b113; it does not allocate a new `DEV-send-stream` candidate and does not create new Runtime evidence.
- **Batch I3 — pending**: verify PR #36 merged and the real `DEV-send-stream` head/product identity. Confirm the integrated branch carries Build113 / `DEV-message-rendering` b113 as the imported product baseline while b112 remains the last DEV-send-stream-owned canonical candidate. Check post-merge PR #29 CI/status; old b113 package/Runtime evidence remains valid only because product paths are unchanged.
- **Batch I4 — pending**: update this checkpoint plus shared durable project docs and PR #29 to record stacked integration truth. Preserve the b107 accepted clean-EOF recovery as Unexercised and overall DEV-send-stream as Runtime Partial / Stable-Frozen No.

Recovery / ownership constraints:

- Never replay a completed merge. On resume, first inspect PR #36 merged state and `dev/send-stream-20260829` actual head.
- Do not allocate b114 merely for integration. Build113 stays permanently owned/reserved by `DEV-message-rendering`; any future DEV-send-stream product candidate requires a fresh uniqueness/evidence guard.
- Do not modify or delete `DEV-message-rendering`'s checkpoint from this selected task session. Its completion bookkeeping belongs to that Work ID.
- Preserve b112 role-isolated reuse, b113 presentation behavior, Send/SSE/Repository authority, one-Send/no-resend invariants, canonical b112/b113 package identities, PR #35, and all earlier reserved Candidates.

**Next exact action:** execute Batch I2 once with expected PR #36 head `d5d761bfad26bc90953488ccd5a96452bf356b3a`; then perform I3/I4 only.

## b112 Human Runtime Positive — role-isolated reuse color fix 2026-09-06

Exact Human Runtime evidence:

- Canonical export metadata is Release Build112 / Candidate `DEV-send-stream-0.1.0-b112` / source marker `b5e3164721e0` / bundle `com.whitesharkssw.chatgptclient` on iPhone iOS17.0. Exact diagnostics SHA-256 `36fd01529ee522fd0646f7bdf6e6f409dca3f55a4b17ff21c88e4e19d16e23b2`; exact screenshot SHA-256 `7a689bca421c01af25aeb19dc9e3a19d1e9a7f47fe431533be760d3eaa1db243`.
- The same completed authoritative target remains 2 visible messages / 6 presentation rows / 0 live rows with one 5-chunk assistant answer (`chunkCharacterLimit=1200`, max chunk 1193). No new Send was required for this gate.
- The export contains 10 `assistantChunkColor.willDisplay` and 9 `assistantChunkRender.afterDisplay` samples. Every visible assistant model-state sample resolves text/attributed/highlight/tint to light-mode black `.label` with no selected/highlighted state.
- Every rendered assistant sample has exactly one black foreground run, zero link runs and zero attachment runs. Every direct-attributed transparent render is `0.000,0.000,0.000` with blue-dominant fraction `0.000`. Every UILabel CALayer transparent render is also `0.000,0.000,0.000` with blue-dominant fraction `0.000`. Where UILabel hierarchy transparent pixels are available, they are likewise black with blue fraction `0.000`; two chunk-3 hierarchy captures report `no_ink_pixels`, but their direct and CALayer captures are valid black and contain no system-blue signal.
- Reuse provenance now matches the intended invariant: all assistant rendered samples report `reusedFromRole=none` or `assistant`; there is zero `reusedFromRole=user`, and every `reusedFromLinkRunCount` is `0`. The b111 contamination path is therefore absent under the role-isolated pools.
- The supplied screenshot visually matches the telemetry: the long assistant body is consistently normal/black across the visible chunked answer, with no blue/normal alternation. The user GitHub URL remains system blue, so the user-link styling regression check also passes in this sample.

Classification:

- b112 is **Human Runtime Positive for the assistant blue-text defect** on the tested iPhone/iOS17 light-appearance path. The b111 root-cause boundary and b112 role-isolated reuse correction are accepted for this scope.
- Do not allocate b113 for the color defect from this evidence. No further color reset or reuse workaround is justified.
- Overall `DEV-send-stream` remains **Active / Runtime Partial / Stable-Frozen No** because the inherited b107 accepted `stream_ended_without_done` same-generation recovery branch is still Unexercised / Unverified by these color-only samples.
- Separate screenshot observation: Native assistant presentation still displays raw Markdown control syntax (`**`, `###`, pipe-table markup) and a raw/unrendered `filecite` control token. This is not a recurrence of the blue-color defect and is not evidence against b112; treat rich-text/citation rendering as a separate presentation scope rather than folding it into the color fix.

Resume/conflict state:

- Branch before this docs-only Runtime record: `dev/send-stream-20260829` head `abaf3cd4cd902f42d2f8ad2836a4e17115a78389`; PR #29 open/unmerged/mergeable; canonical product/package/Artifact identities remain `3957b806...` / `b5e31647...` / `9975978222`.
- `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`. No product/Candidate identity changes are made by this Runtime record.

**Evidence ladder:** b111 diagnostic Runtime Positive / root-cause boundary selected / b112 Code written / exact scope + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / **Human Runtime Positive for assistant color consistency + user-link regression** / overall `DEV-send-stream` Runtime Partial / Stable-Frozen No.

**Next exact action:** close the blue-text sub-gate at b112. Do not create another color candidate. Continue only from a separately evidenced remaining `DEV-send-stream` gate (notably accepted clean-EOF recovery if it occurs) or a separately selected presentation task for Markdown/citation rendering.
