## b113 stacked integration recovery point — DEV-send-stream owner 2026-09-06

Selected owner / verified pre-integration state:

- Work ID `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable at exact pre-integration head `50432b8743f3391a8174a3b7aae745298082d433`; target `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Canonical DEV-send-stream-owned candidate remains permanently reserved b112: product `3957b806f32f0995ceb9cf8f9487aba939f3b306`, package `b5e3164721e01ceb1fe320ebd290bda79a921fc2`, Artifact `9975978222`, Human Runtime Positive for the role-isolated assistant-color fix. Overall Send/Stream remains Runtime Partial / Stable-Frozen No because accepted clean-EOF recovery is still Unexercised.
- Stacked dependency PR #36 `DEV-message-rendering` is open/mergeable with base exactly `dev/send-stream-20260829@50432b8743f3391a8174a3b7aae745298082d433` and head `d5d761bfad26bc90953488ccd5a96452bf356b3a`.
- PR #36 canonical b113 identity remains owned by `DEV-message-rendering`: Candidate `DEV-message-rendering-0.1.0-b113` / Build113, product `7d1ddc8eaa164c9b307f525b00bb0e1404f395e9`, package `75ccad15208610c2b0420033846f9bb15bbdb494`, Artifact `9976713893`, IPA `sha256:2cf62b87117f9279816de68f2ed3ce83768d203198b555fe4fe0042f8d367c3f`, Human Runtime Positive for the tested native message-presentation scope.
- Compare `75ccad15208610c2b0420033846f9bb15bbdb494..d5d761bfad26bc90953488ccd5a96452bf356b3a` proves all post-package commits are docs/tooling only; no `ChatGPTClient/**` or Xcode product path changed after the canonical b113 package source.
- Parallel PR #35 remains draft research-only at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142` and owns no product `ChatGPTClient/**`, product Xcode Candidate, or Build113 identity.

Integration batches:

- **Batch I0 — completed**: recovery point recorded; recorder run `33992571002` succeeded and bot committed `494ee22d0e9861d373207c91e6b539c8f9b26410`. Recorder was then made idempotent at tooling-only commit `d265d265a7e5382834363e1e73ca7c91a5489cc4`; idempotent run `33992707723` succeeded without product changes.
- **Batch I1 — completed**: after base advancement GitHub REST recomputed PR #36 as `mergeable=true / mergeable_state=clean / rebaseable=true`; head remains exact `d5d761bfad26bc90953488ccd5a96452bf356b3a`. No product conflict exists.
- **Batch I2 — next**: merge PR #36 into `dev/send-stream-20260829` using expected head `d5d761bfad26bc90953488ccd5a96452bf356b3a`. This integrates already-tested b113 and allocates no new `DEV-send-stream` Candidate.
- **Batch I3 — pending after merge**: verify PR #36 merged and the real `DEV-send-stream` head/product identity. Confirm Build113 / `DEV-message-rendering` b113 is the imported product baseline while b112 remains the last DEV-send-stream-owned canonical candidate. Check post-merge PR #29 CI/status; old b113 package/Runtime evidence remains valid only because product paths are unchanged from canonical source.
- **Batch I4 — pending after I3**: update this checkpoint plus shared durable project docs and PR #29 to record stacked integration truth. Preserve b107 accepted clean-EOF recovery as Unexercised and overall DEV-send-stream as Runtime Partial / Stable-Frozen No.

Recovery / ownership constraints:

- Never replay a completed merge. On resume, first inspect PR #36 merged state and `dev/send-stream-20260829` actual head.
- Do not allocate b114 merely for integration. Build113 stays permanently owned/reserved by `DEV-message-rendering`; any future DEV-send-stream product candidate requires a fresh uniqueness/evidence guard.
- Do not modify or delete `DEV-message-rendering`'s checkpoint from this selected task session. Its completion bookkeeping belongs to that Work ID.
- Preserve b112 role-isolated reuse, b113 presentation behavior, Send/SSE/Repository authority, one-Send/no-resend invariants, canonical b112/b113 package identities, PR #35, and all earlier reserved Candidates.

**Next exact action:** execute Batch I2 once with expected PR #36 head `d5d761bfad26bc90953488ccd5a96452bf356b3a`; then perform I3/I4 only.

