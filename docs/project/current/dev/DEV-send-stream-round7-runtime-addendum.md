## b111 Human Runtime selects cross-role reuse contamination / b112 role-isolated reuse allocation — 2026-09-06

Exact b111 Human Runtime evidence:

- Export metadata is canonical Release Build111 / Candidate `DEV-send-stream-0.1.0-b111` / source `4297846dd688` on iPhone iOS17.0. Exact diagnostics SHA-256 `8b3e7e627c4218f1154b3e325ec6a95b643c8f64d01c18c37693bab3aba6e811`; 52 total events, including 12 `assistantChunkColor.willDisplay` and 12 `assistantChunkRender.afterDisplay` samples.
- The target remains the same completed authoritative answer: 2 visible messages / 6 presentation rows / 0 live rows / one 5-chunk assistant message (`chunkCharacterLimit=1200`, max chunk 1193). No new Send is involved.
- Every sampled assistant attributed string is structurally clean at capture time: `attributeRunCount=1`, `foregroundRunCount=1`, `foregroundDistinctColors=rgba:0,0,0,1`, `linkRunCount=0`, `attachmentRunCount=0`. Every direct-attributed transparent render is black `0.000,0.000,0.000` with blue-dominant fraction `0.000`. Runtime attributed content/link styling is therefore rejected as the current blue owner.
- The UILabel CALayer is the first surface that diverges. Four samples resolve exactly system-blue-like `labelLayerTransparentInkRGB=0.000,0.476,1.000`, blue-dominant fraction `1.000`: chunk 2 twice and chunk 3 twice. Normal samples from assistant-only cells resolve black with blue fraction `0.000`.
- Reuse provenance makes the causal boundary concrete. Cell ordinal 3 renders chunk 3 black on its initial `reusedFromRole=none` sample; after that same cell is reused from a `.user` row whose previous attributed value contained one link run, the next chunk-3 layer render turns pure blue and remains blue on the repeat sample. Cell ordinal 1 is first captured blue immediately after `reusedFromRole=user` / `reusedFromLinkRunCount=1`, then remains blue on a later assistant->assistant reuse even though the current assistant attributed string is black and link-free. By contrast, cell ordinals 2 and 4, which are reused only from assistant/no-link state in this export, remain black.
- Current source explains the initiating state: user and assistant rows share the single reuse identifier `ConversationMessageCell`, while user Markdown links explicitly apply `UIColor.systemBlue`. Existing `prepareForReuse` already clears text/attributedText and resets highlight/text/tint, yet the layer stays contaminated; another reset is therefore not the evidence-backed owner fix.

b112 allocation / minimum fix:

- Allocate and permanently reserve `DEV-send-stream-0.1.0-b112` / `0.1.0 (112)`. `BUILD_TEST_INDEX.md` contains no b112 before this allocation; parallel PR #35 owns no `ChatGPTClient/**`, product Xcode candidate, or Build112 identity.
- Keep `ConversationMessageCell` as the single implementation class and preserve user Markdown/link rendering, assistant attributed rendering, b111 diagnostics, geometry, reasoning, Copy, Send/SSE/Repository/recovery behavior unchanged.
- Change only reuse ownership: register distinct `.user` and `.assistant` reuse identifiers and select the identifier from the existing presentation message role before dequeue. A cell/UILabel that has rendered a user link must never be reused for an assistant row. This fixes the proven invariant at the reuse owner rather than adding another color/tint/highlight reset.
- Product scope is exactly `ChatGPTClient.xcodeproj/project.pbxproj` plus `ChatGPTClient/Conversation/ConversationFeature.swift`.
- Human Runtime b112: reopen this same completed 5-chunk answer, scroll through all chunks, and export Diagnostics. Require all assistant direct/layer/hierarchy transparent renders to stay normal `.label`, zero assistant reuse provenance from `user`, and no blue/normal alternation. Existing user link system-blue rendering must remain intact. No new Send is required.

Resume/conflict guard / batch recovery point:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable; verified pre-b112 branch head `5d2ee88331e21b7a3e186c3930717c524c2137ab`; canonical b111 product `64351b96bd61a44e8566e2264c5593fae868268e`, package `4297846dd6889905cbc765c23f83b33ee54437f5`, Artifact `9975489792`.
- `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`. Parallel PR #35 remains draft at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`, research-only with zero product/candidate overlap.
- Tooling-preparation commits may add only b112 staging scripts/workflow and do not create a b112 product or Artifact.
- Batch A: durably record this b111 Runtime classification and b112 reservation in checkpoint/index/state/module/profile/technical decisions before product changes.
- Batch B: apply only the exact two-product-path b112 reuse-isolation delta, run `git diff --check` + Debug Simulator compile, then commit exact product.
- Batch C: bind formal package CI to the exact b112 product commit, require same-source Push + PR CI, canonical Artifact and independent IPA identity/hash verification, then record package evidence and update PR #29 before Human Runtime.
- Recovery must not rewrite b111/b110/b109 identities, PR #35, user-link `systemBlue`, Send/SSE/Repository/recovery behavior, or previously reserved Candidates.

**Next exact action:** complete Batch B only after Batch A is durably committed; then package one canonical b112 for the role-isolated reuse Human Runtime gate.

## b111 label-pipeline diagnostic package ready — 2026-09-06

Canonical identity:

- Candidate `DEV-send-stream-0.1.0-b111` / `0.1.0 (111)` is permanently reserved.
- Exact product commit `64351b96bd61a44e8566e2264c5593fae868268e` changes only `ChatGPTClient.xcodeproj/project.pbxproj` and `ChatGPTClient/Conversation/ConversationFeature.swift` relative to the Batch-A b111 allocation checkpoint.
- Exact package source `4297846dd6889905cbc765c23f83b33ee54437f5` changes only `.github/workflows/ios-foundation.yml` after the product commit.
- Guarded staging `33986923145/101362120447` passed exact two-product-path scope, `git diff --check`, and Debug Simulator compile.
- Push CI `33987037286/101362430240` and PR CI `33987039485/101362436599` both passed on exact package source `4297846dd6889905cbc765c23f83b33ee54437f5`.
- Canonical Push Artifact `9975489792`; Artifact ZIP SHA-256 `82c512fd4d82ce5a3fcb73f9b6d9cf2314382874fa9544ae5bbbde47fcd209a6`; IPA `ChatGPTClient-0.1.0-b111-dev-send-stream.ipa` SHA-256 `071cd06933388654e0cd86ca626e1305df08f28f90e1e0626caf0f7dc10e059a`.
- Independent package inspection verifies bundle `com.whitesharkssw.chatgptclient`, `0.1.0 (111)`, Candidate b111, source marker `4297846dd688`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS, Mach-O arm64. The packaged SHA sidecar matches `071cd06933388654e0cd86ca626e1305df08f28f90e1e0626caf0f7dc10e059a`.

Diagnostic behavior / inherited Runtime truth:

- Trigger evidence remains canonical b110 Runtime `sha256:d0a72e850469cd2bb10075c40e01cce3d5e44f20f2eac95f29474d9a2ef5ba81`: all public UILabel/attributed/highlight/tint state is light-mode black `.label`, while chunk 2's UILabel-only `drawHierarchy` aggregate was repeatably system-blue-like. b110's brightness-gated sampler discarded normal black text and therefore could not select the exact label-internal owner.
- b111 preserves b110 visible rendering, b110/b109 existing probes, user-link `systemBlue`, reasoning presentation and all Send/SSE/Repository/recovery behavior.
- b111 adds privacy-safe structural attributed diagnostics (`attributeRunCount`, foreground color summary, link/attachment counts), per-cell reuse provenance, and three dark-pixel-inclusive transparent rendered aggregates: direct current attributed-string draw, `messageLabel.layer.render(in:)`, and `messageLabel.drawHierarchy`.
- No screenshot/pixel buffer/message text/message ID/URL/content hash is persisted or exported. No retry/timer/watchdog/polling/duplicate Send/response authority is added.

Human Runtime gate:

1. Install only canonical b111 Artifact `9975489792` / IPA SHA `071cd06933388654e0cd86ca626e1305df08f28f90e1e0626caf0f7dc10e059a`.
2. Reopen the same completed 5-chunk answer used for b109/b110; no new Send is required.
3. Scroll through all five assistant chunks once, including the visually blue region, then export Diagnostics.
4. Compare each `assistantChunkRender.afterDisplay` by chunk index: `foregroundDistinctColors`, `linkRunCount`, `cellOrdinal`, `reusedFromRole`, `reusedFromLinkRunCount`, `directAttributedTransparentInkRGB`, `labelLayerTransparentInkRGB`, and `labelHierarchyTransparentInkRGB` plus blue-dominant fractions.
5. Direct attributed draw blue or an actual blue/link run -> attributed runtime content owner. Direct black but layer blue -> UILabel layer/internal draw/cache owner. Layer black but hierarchy blue -> UIView hierarchy draw owner. Blue tracking `reusedFromRole=user` / prior link runs strengthens shared-cell reuse as the causal boundary.
6. Do not select or claim a rendering fix until this diagnostic evidence distinguishes the owner.

**Evidence ladder:** b110 UILabel draw-stage blue Runtime captured / b110 normal-black comparator incomplete / b111 Code written / exact scope + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / diagnostic Human Runtime pending / Stable-Frozen No.

**Next exact action:** run only the b111 Human Runtime diagnostic gate above and export Diagnostics. b111 intentionally does not change the visible color defect.

## b110 Human Runtime rendered-output result / b111 label-pipeline probe allocation — 2026-09-06

Exact b110 Human Runtime evidence:

- Export metadata is canonical Release Build110 / Candidate `DEV-send-stream-0.1.0-b110` / source `26ea3354998c` on iPhone iOS17.0. Exact diagnostics SHA-256 `d0a72e850469cd2bb10075c40e01cce3d5e44f20f2eac95f29474d9a2ef5ba81`.
- Target authoritative Detail remains exactly 2 visible messages / 6 presentation rows / 0 live rows with one 5-chunk assistant message (`chunkCharacterLimit=1200`, max chunk 1193). This remains a completed authoritative rendering reproduction rather than live+authoritative duplication.
- All 12 `assistantChunkColor.willDisplay` samples in this export resolve `labelTextColor`, attributed foreground at index 0, `labelHighlightedTextColor`, and `labelTintColor` to black `rgba:0,0,0,1`; label/cell highlighted and selected states are false; interface style is light. Model state still does not explain a blue chunk.
- Eleven `assistantChunkRender.afterDisplay` samples were captured. Chunk 2 was sampled twice, at separate scroll passes, and both UILabel-only `drawHierarchy` renders report `labelRenderInkRGB=0.000,0.479,1.000`, `labelRenderBlueDominantFraction=1.000`, `labelRenderNearWhiteFraction=0.000`, with 73,612 sampled pixels. The same crop through the cell hierarchy is also repeatably blue-bearing (`hierarchyCropInkRGB=0.960,0.979,1.000`, blue-dominant fraction 0.063). Therefore a compositor/sibling outside UILabel is not required to produce the captured blue pixels: the blue is already present at the UILabel `drawHierarchy` surface for this chunk.
- b110 cannot yet compare that blue chunk cleanly against the normal light-mode chunks. Its `renderedInkDiagnostics` implementation discards any pixel whose unpremultiplied `max(red, green, blue) <= 0.18`. Normal light-mode `.label` is black, so chunks 0/1/3/4 reporting `labelRenderStatus=no_ink_pixels` is an expected sampler blind spot, not proof of missing or white text. Do not interpret those `no_ink_pixels` values as a rendering result.
- Current source still constructs assistant body attributed text with one `.foregroundColor=UIColor.label`; the explicit `UIColor.systemBlue` body path is only the separate user-message Markdown-link renderer. The b110 evidence therefore narrows the next fork to (a) unexpected runtime attributed/link runs appearing after `willDisplay`, (b) UILabel layer/internal draw state, or (c) shared cell/label reuse state. It does not justify another blind color reset.

b111 allocation / evidence-backed scope:

- Allocate and permanently reserve `DEV-send-stream-0.1.0-b111` / `0.1.0 (111)`. `BUILD_TEST_INDEX.md` contains no b111 before this allocation; parallel PR #35 owns no product Candidate or `ChatGPTClient/**` path.
- b111 remains diagnostic-only and must preserve b110/b109/b108 visible rendering plus all inherited Send/SSE/Repository/recovery behavior.
- Product scope is exactly `ChatGPTClient.xcodeproj/project.pbxproj` plus `ChatGPTClient/Conversation/ConversationFeature.swift`.
- For each chunked assistant after-display sample, log privacy-safe structural attributed state only: total attribute-run count, foreground-color run/distinct-color summary, link-run count, attachment-run count, current cell ordinal, and reuse provenance (`reusedFromRole` plus whether the prior attributed value had a link run). Never log text, message ID, URL, range contents, or content hash.
- Add three transparent-background render comparisons using an alpha-only ink selector so black text is retained: direct current `NSAttributedString` drawing, `messageLabel.layer.render(in:)`, and current `messageLabel.drawHierarchy`. Keep the existing b110 metrics for continuity. These images remain in-memory only and only aggregate pixel counts/RGB/blue fraction are exported.
- Interpretation: direct attributed draw blue or link/blue run present -> runtime attributed content owns the color; direct draw black but layer render blue -> UILabel internal layer/cache owns it; layer black but drawHierarchy blue -> UIView hierarchy rendering path owns it. Cell-ordinal/reuse provenance decides whether any blue surface tracks shared user/assistant reuse. No visible fix should be selected before this distinction.

Resume/conflict guard / batch recovery point:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable; verified pre-b111 branch head `a6c38e431aff51cd11a736b6aae4922c6ca418bf`; canonical b110 product `55184f057d3303a266146ab6a76be019bf3f1c00`, package `26ea3354998c89420212315977dcf94cc3a91197`, Artifact `9975056986`.
- `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`. Parallel PR #35 remains draft at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`; its seven changed paths are research/workflow/checkpoint only and have zero product-path overlap.
- Tooling-preparation commits may add only b111 staging scripts/workflow and do not create a product/Candidate Artifact.
- Batch A: durably record this b110 Runtime classification and b111 reservation in checkpoint/index/state/module/profile/technical decisions before product changes.
- Batch B: apply only the exact two-product-path b111 diagnostic delta, run `git diff --check` + Debug Simulator compile, then commit exact product.
- Batch C: bind formal package CI to exact b111 product commit, require same-source Push + PR CI, canonical Artifact and independent IPA identity/hash verification, then record package evidence and update PR #29 before Human Runtime.
- Recovery must not rewrite b110/b109/b108 canonical identities, PR #35, Send/SSE/Repository/recovery logic, user-link styling, or previously reserved Candidates.

**Next exact action:** complete Batch B only after Batch A is durably committed. b111 Human Runtime reopens the same completed 5-chunk answer, scrolls all chunks, exports Diagnostics, and compares direct-attributed / layer / hierarchy rendered color plus attributed-run/reuse provenance. No new Send is required.

## b110 rendered-color diagnostic package ready — 2026-09-06

Canonical identity:

- Candidate `DEV-send-stream-0.1.0-b110` / `0.1.0 (110)` is permanently reserved.
- Exact product commit `55184f057d3303a266146ab6a76be019bf3f1c00` changes only `ChatGPTClient.xcodeproj/project.pbxproj` and `ChatGPTClient/Conversation/ConversationFeature.swift` relative to the b109 product baseline.
- Exact package source `26ea3354998c89420212315977dcf94cc3a91197` changes only `.github/workflows/ios-foundation.yml` after the product commit.
- Guarded staging `33985483452/101358091966` passed exact scope, `git diff --check`, and Debug Simulator compile.
- Push CI `33985567667/101358319343` and PR CI `33985569950/101358325339` both passed on exact package source `26ea3354998c89420212315977dcf94cc3a91197`.
- Canonical Push Artifact `9975056986`; Artifact ZIP SHA-256 `2c5d963f915b2b12588416cfbd71668dbb0a5b22e49b53f9a7657732ae24cb20`; IPA `ChatGPTClient-0.1.0-b110-dev-send-stream.ipa` SHA-256 `7ecb92d4e364e70e6ae9091af7a80386c06cc1aea96993227a54d76b9470fcd4`.
- Independent package inspection: bundle `com.whitesharkssw.chatgptclient`, `0.1.0 (110)`, Candidate b110, source marker `26ea3354998c`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS, Mach-O arm64.

Diagnostic behavior:

- b110 keeps b109 `assistantChunkColor.willDisplay` model-state logs unchanged.
- On the next main-queue turn after `willDisplay`, only while the same cell remains at the same index path, it emits `assistantChunkRender.afterDisplay` with aggregate rendered ink statistics for the UILabel alone and the same label rectangle from the cell hierarchy, plus alpha/layer-opacity fields.
- The renderer stores no screenshot, pixel buffer, message text, message ID, URL, or content hash. It exports only aggregate counts/fractions/colors.
- Visible body rendering, attributed content, fonts, row geometry, reasoning, user-link behavior, Send/SSE/Repository/recovery, timers/retries and response authority are unchanged.

Human Runtime gate:

1. Install only canonical b110 Artifact `9975056986` / IPA SHA `7ecb92d4e364e70e6ae9091af7a80386c06cc1aea96993227a54d76b9470fcd4`.
2. Reopen the same completed 5-chunk answer used for b109; no new Send is required.
3. Scroll through all five assistant chunks once and observe which regions are blue vs normal.
4. Export Diagnostics.
5. Compare each `assistantChunkRender.afterDisplay` by `chunkIndex`: `labelRenderInkRGB` / `labelRenderNearWhiteFraction` / `labelRenderBlueDominantFraction` against `hierarchyCropInkRGB` / `hierarchyCropNearWhiteFraction` / `hierarchyCropBlueDominantFraction`.
6. If label-only differs with screen color, investigate inside/below UILabel drawing. If label-only stays white but hierarchy crop differs, investigate sibling/cell composition. If both remain white while physical screen differs, investigate below hierarchy/window compositing. Do not allocate a rendering fix before this evidence.

**Evidence ladder:** b109 model-state diagnostic Runtime Positive for probe / visible color defect persists / b110 Code written / exact scope + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / diagnostic Human Runtime pending / Stable-Frozen No.

**Next exact action:** run the b110 Human Runtime gate above and export Diagnostics; do not judge b110 by whether the color is fixed because it intentionally does not change rendering.

## b109 Human Runtime model-state result / b110 rendered-pixel probe allocation — 2026-09-06

Exact b109 Human Runtime evidence:

- Export metadata is canonical Release Build109 / Candidate `DEV-send-stream-0.1.0-b109` / source `8c6ea43677f2` on iPhone iOS17.0. Exact diagnostics SHA-256 `37669df4cddc25db7b0d3bb1ae96d54d722aee501fcf3e55888aff636d8edcdf`.
- The export contains 16 `assistantChunkColor.willDisplay` samples across two authoritative conversations. The target completed answer is still exactly 2 authoritative messages / 6 presentation rows / 0 live rows with one 5-chunk assistant message (`chunkCharacterLimit=1200`, max chunk 1193).
- The target produced samples for every `chunkIndex` 0 through 4, with repeated rows as the user scrolled. Every target sample and every other b109 chunk sample reports the same resolved state: `labelTextColor=rgba:1,1,1,1`, attributed foreground at index 0 `rgba:1,1,1,1`, highlighted text color `rgba:1,1,1,1`, tint `rgba:1,1,1,1`, label/cell highlighted=false, selected=false, interfaceStyle=dark, surface=authoritative.
- The user still observes the answer alternating blue/normal while scrolling. Therefore b109 has successfully rejected all exposed UILabel model-state properties as the differentiating owner. Current assistant source also builds assistant body attributed text with one `.foregroundColor = UIColor.label` attribute; the only `UIColor.systemBlue` body path is the separate user-message Markdown-link renderer, not assistant body rendering.
- Do not add another blind `textColor`, tint, highlight, or attributed-foreground reset. This evidence specifically requires observing the actual rendered output after display.

b110 allocation / evidence-backed scope:

- Allocate and permanently reserve `DEV-send-stream-0.1.0-b110` / `0.1.0 (110)`. No current Build/Test entry or parallel PR #35 candidate uses Build110; PR #35 remains draft research-only with no `ChatGPTClient/**` or product Xcode candidate ownership.
- b110 is diagnostic-only. Preserve b109/b108 rendering, b109 model-state diagnostics, and all b107 Send/SSE/Repository/recovery behavior unchanged.
- Product scope is exactly `ChatGPTClient.xcodeproj/project.pbxproj` plus `ChatGPTClient/Conversation/ConversationFeature.swift`.
- On the next main-queue turn after a chunked assistant cell reaches `willDisplay`, and only if that exact cell is still at the same index path, compute privacy-safe rendered-pixel aggregates for two surfaces: the UILabel alone and the same UILabel rectangle cropped from the cell content hierarchy. Record aggregate ink RGB, near-white fraction, blue-dominant fraction, sampled-pixel count, plus alpha/layer-opacity fields. Never persist or export screenshots, message text, message IDs, pixel buffers, URLs, or content hashes.
- This probe must not change visible rendering, font, attributed content, geometry, Markdown/link behavior, reasoning view, Send behavior, Repository state, timers, retries, recovery, or response authority.

Interpretation gate:

- Label-only rendered aggregate differs blue vs white across visible chunks -> owner is inside/below the UILabel draw/presentation path despite uniform model properties.
- Label-only stays white but hierarchy-crop differs -> owner is outside the label itself, in sibling/cell hierarchy composition.
- Both rendered aggregates remain white while the physical screen still alternates -> move the next investigation below view-hierarchy drawing, toward window/compositor/display presentation; do not guess a color fix.

Resume/conflict guard:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable; pre-b110 branch head `69d9ab56e284e3a32fd3702462c4206b58372520`; canonical b109 product `11e7ec536b986c45811dc449cd2c4f6e442c28df`, package `8c6ea43677f2a0f39c08d6b9ca695c9c2e4a5267`, Artifact `9974791883`.
- `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`. Parallel PR #35 remains draft at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142` with zero product ownership overlap.

**Next exact action:** after this Runtime/allocation checkpoint is durably committed, stage only the two-path b110 rendered-pixel diagnostic, pass `git diff --check` + Debug Simulator compile, package one canonical b110 IPA, then reopen the same completed 5-chunk answer, scroll all chunks once, and export Diagnostics. b110 is not a rendering fix.

## b109 authoritative chunk-color diagnostic probe — package ready 2026-09-06

Canonical identity / validation:

- Candidate `DEV-send-stream-0.1.0-b109` / `0.1.0 (109)`, permanently reserved. This is a diagnostic probe, not a rendering fix.
- Exact product commit `11e7ec536b986c45811dc449cd2c4f6e442c28df`; canonical package source `8c6ea43677f2a0f39c08d6b9ca695c9c2e4a5267`.
- Corrected guarded staging `33984605217/101355720829` passed Batch A durable b108 Runtime/b109 allocation, exact two-product-path diagnostic scope, `git diff --check`, Debug Simulator compile and exact product commit. Earlier attempts `33984476631` and `33984523733` failed only the docs-only allocation path-order assertion before product Batch B; they produced no b109 product commit or Artifact and are not product failures.
- Formal Push `33984671709/101355898061` and PR `33984673860/101355903471` both passed on exact package source `8c6ea43677f2a0f39c08d6b9ca695c9c2e4a5267`.
- Canonical Push Artifact `9974791883`; GitHub Artifact digest and independently recomputed ZIP SHA-256 both `743e61fc4f20670d8a6cc5d5afd42f8942e40f2943abe1f9b23e4ca621b43956`.
- Canonical IPA `ChatGPTClient-0.1.0-b109-dev-send-stream.ipa`; independent SHA-256 `6c37dfb8496c533ce2d5e4878f22a5b265f7c55e87e9cbfbb9189155fa30096a`, matching the packaged sidecar.
- Independent package inspection verifies `com.whitesharkssw.chatgptclient`, `0.1.0 (109)`, Candidate b109, source marker `8c6ea43677f2`, `DiagnosticsBuildConfiguration=Release`, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS and required arm64.

Exact diagnostic behavior:

- Product scope is exactly Xcode Build/Candidate 108 -> 109 plus `ConversationFeature.swift` privacy-safe chunk color telemetry.
- b108 rendering behavior is preserved. `ConversationMessageCell.bodyColorDiagnostics()` reads only resolved UILabel `textColor`, attributed foreground at index 0, `highlightedTextColor`, tint, label/cell highlighted and selected state, and interface style; it logs no message text or IDs.
- Detail-table `willDisplay` emits `assistantChunkColor.willDisplay` only for chunked assistant rows, with `surface`, row/chunk index/count and the cell color snapshot. Both authoritative and live surfaces are distinguishable.
- No final rendering color/font/attributed content, geometry, Markdown, link styling, reasoning view, Send/SSE parsing, Repository state, timer, retry, recovery or response authority changed in b109.

Inherited Runtime truth:

- b108 diagnostics `sha256:c26f5ed8712ca63c8dae037e58330d5fa4b2f7cb47b8b0dafc078e920b4c813c` / video `sha256:6cecee7a5f249529c72c53ee08620740e9d8480b080d8914476f697ad0efdc73` remain the trigger evidence: ordinary one-Send/normal terminal/authoritative reconcile is Positive; accepted `stream_ended_without_done` remains Unexercised; completed authoritative chunk-row color consistency is Runtime Negative.
- b109 does not claim a color fix. Its Human Runtime gate is diagnostic: install only canonical b109, open the same completed long answer if available (otherwise another completed assistant answer spanning multiple 1200-character chunks), scroll across all chunks once, visually note which chunks are blue/normal, then export diagnostics. Compare `assistantChunkColor.willDisplay` fields by chunk index. A new Send is unnecessary for this gate.

Evidence ladder:

- **b108 normal Send/terminal/reconcile Runtime Positive / b107 accepted-clean-EOF recovery Unexercised / b108 authoritative chunk-row color Runtime Negative / b109 Code written / exact scope + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / diagnostic Human Runtime pending / Stable-Frozen No.**

**Next exact action:** install canonical b109 IPA `6c37dfb8496c533ce2d5e4878f22a5b265f7c55e87e9cbfbb9189155fa30096a`, open the existing completed long-answer reproduction, scroll all assistant chunks once, export diagnostics, and use `assistantChunkColor.willDisplay` to select the actual final color owner before any b110 rendering change. Do not allocate a rendering-fix candidate from guesswork.

## b108 Human Runtime Negative / b109 authoritative chunk-color probe allocation — 2026-09-06

Exact b108 Human Runtime evidence:

- Canonical b108 metadata is Release Build108 / Candidate `DEV-send-stream-0.1.0-b108` / source `d34ff4534ca7` on iPhone iOS17.0. Exact diagnostics SHA-256 `c26f5ed8712ca63c8dae037e58330d5fa4b2f7cb47b8b0dafc078e920b4c813c`; exact 7.53s screen recording SHA-256 `6cecee7a5f249529c72c53ee08620740e9d8480b080d8914476f697ad0efdc73`.
- New Chat transport/regression remains Positive: one protected Send was observed, HTTP200 `text/event-stream` was accepted, the first SSE conversation ID became authoritative, generation 1 streamed 107 reasoning characters / 8 tools / 5292 final characters, reached normal `terminal` / `phase=completed`, then authoritative Detail reconciled with `liveSnapshotCleared=true`.
- There is zero exact `stream_ended_without_done`, zero `coveredExecutor.acceptedClientStreamEndRecovery`, and zero `acceptedClientRecovery.interrupted`. Therefore the inherited b107 accepted-clean-EOF recovery branch remains Unexercised, not passed or failed by this sample.
- The color defect is Runtime Negative again with a stronger boundary. After reconcile there are `presentationRowCount=6`, `livePresentationRowCount=0`, `authoritativeMessageCount=2`, one chunked message, `chunkCharacterLimit=1200`, and max chunk length 1193. This rules out live+authoritative duplication as the color owner.
- The exact video shows the completed authoritative assistant answer alternating blue and normal label-colored text at long-message row boundaries while the reasoning area is already collapsed. Current source derives those rows from one assistant message and configures every chunk as `.assistant`, so b108's post-attributedText `messageLabel.textColor=.label` is insufficient. Do not add more blind tint/text/highlight resets.

b109 allocation / evidence-backed scope:

- Allocate and permanently reserve `DEV-send-stream-0.1.0-b109` / `0.1.0 (109)`. No current Build/Test entry or parallel PR #35 candidate uses b109.
- b109 is diagnostic-only. Preserve b108 rendering behavior and all Send/SSE/Repository/recovery behavior unchanged.
- Product scope is exactly `ChatGPTClient.xcodeproj/project.pbxproj` plus `ChatGPTClient/Conversation/ConversationFeature.swift`.
- Add a privacy-safe `ConversationMessageCell` color snapshot and log it from the detail table's `willDisplay` path for chunked assistant rows. Required fields: surface (`authoritative`/`live`), row index, chunk index/count, resolved UILabel `textColor`, attributed foreground at index 0, highlighted text color, tint color, label/cell highlighted and selected states, and interface style. Do not log message text or IDs.
- This probe must not change any final rendering color, font, attributed content, geometry, Markdown behavior, link color, reasoning view, Send behavior, Repository state, timers, retries, recovery, or response authority.

Resume/conflict guard:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable; b108 package/runtime baseline head is `810cdb6e5572b5df8584494f28db1ed335e5b97a`. `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Parallel PR #35 remains draft research-only at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`, explicitly owning no `ChatGPTClient/**`, product Xcode Candidate, or exact product-path overlap.

**Next exact action:** after this Runtime/allocation checkpoint is durably committed, stage only the two-path b109 diagnostic probe, pass `git diff --check` + Debug Simulator compile, package one canonical b109 IPA, then on real iPhone open the same completed b108 long-answer conversation, scroll across all chunk rows once, export diagnostics, and compare `assistantChunkColor.willDisplay` fields with the visible blue/normal rows. Do not claim a color fix in b109.

## b108 assistant-body color ownership — package ready 2026-09-06

Canonical identity / validation:

- Candidate `DEV-send-stream-0.1.0-b108` / `0.1.0 (108)`, permanently reserved.
- Exact product commit `eb0de74460b0bd06a6d977bf915b5e06a5c946db`; canonical package source `d34ff4534ca76ee03e2c8a3eeddb29eca011319f`.
- Guarded staging `33981732350/101348043849` passed exact two-product-path validation, `git diff --check`, Debug Simulator compile and exact product commit.
- Formal Push `33981838027/101348321052` and PR `33981839719/101348326124` both passed on exact package source `d34ff4534ca76ee03e2c8a3eeddb29eca011319f`.
- Canonical Push Artifact `9973988017`; GitHub Artifact digest and independently recomputed ZIP SHA-256 both `8e445a65346b9a32d8811645f2e21a2f1340942c9e7333beb4ddfc4c6a8a7c14`.
- Canonical IPA `ChatGPTClient-0.1.0-b108-dev-send-stream.ipa`; independent SHA-256 `a2639b5793316077c0f203bfd4dffdecd8cef74c361a4995bc8bfba05f657dbd`, matching sidecar.
- Independent package inspection verifies `com.whitesharkssw.chatgptclient`, `0.1.0 (108)`, Candidate b108, source marker `d34ff4534ca7`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS and Mach-O arm64.

Exact product behavior:

- Product change remains exactly two paths: Build/Candidate 107 -> 108 in the Xcode project, plus one assistant-body rendering statement in `ConversationFeature.swift`.
- In `ConversationMessageCell.configure`, `.assistant` assigns the existing assistant attributed body first and then sets `messageLabel.textColor = .label`, making UILabel's final body color property authoritative after attributed-text style adoption.
- `.user` attributed text and link `systemBlue` handling are unchanged. `reasoningTextView`, response timeline styling, Markdown semantics, row geometry, Send/SSE parsing, Repository state and all b107 recovery logic are unchanged.
- This delta is justified by exact b107 Runtime `sha256:8e3e10b44e8e627f60e7a831d48f11c7fa9fff4bc4b0446b71588fbc38ade7da` + screenshots: assistant placeholder/final body were blue while reasoning SSE text was normal, which maps to `messageLabel` versus the independent `reasoningTextView`. b106's pre-attributedText label reset was Runtime-insufficient.

Evidence ladder / Runtime gate:

- **Code written / exact scope + Debug Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**
- Human Runtime b108 must verify the assistant `正在思考…` placeholder and final assistant body use normal label color, while reasoning SSE remains unchanged and user-link coloring does not regress.
- Also re-run one ordinary Native New Chat Send to ensure b107 one-Send authoritative identity/normal terminal convergence has no regression. If exact accepted `stream_ended_without_done` naturally occurs, the inherited b107 same-generation/no-resend recovery gate may be evaluated; absence of that event does not qualify it.

**Next exact action:** install only canonical b108 IPA `a2639b5793316077c0f203bfd4dffdecd8cef74c361a4995bc8bfba05f657dbd` on the real iPhone, fresh-launch, run one New Chat first Send, observe placeholder/reasoning/final colors and export diagnostics. Do not allocate b109 before b108 Human Runtime evidence unless the user explicitly chooses to skip Runtime.

## b107 Human Runtime Partial / b108 assistant-body color allocation — 2026-09-06

Exact b107 Human Runtime evidence:

- Canonical candidate `DEV-send-stream-0.1.0-b107` / Release / iPhone / iOS17.0 / source marker `4bd3501a3092`; diagnostics `ChatGPTClient-Diagnostics-20260905-171244.json`, `sha256:8e3e10b44e8e627f60e7a831d48f11c7fa9fff4bc4b0446b71588fbc38ade7da`, 411 events. Screenshots `sha256:5b8d52c002a468ba6d5a79bacc1b922081c0fdc30d71880d0de0fadf9096a0b7` and `sha256:037b207c15012633a569087c2024abdd249a8646e3ad030d5726591135c20798` are the exact visual evidence supplied with this run.
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

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable; verified pre-record branch head `be286f2f8c98305d9e702252af9c73f27d6431bf`; main remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Canonical b107 product/package remain `113fa19d7264b953949770d2e44cb500ded2da6b` / `4bd3501a3092dfe7aad7ea836ba0cb8e42b0d65f`; Artifact `9967821935`; IPA `sha256:7195d89cb9837efc3386c5dd7e030e7f11f10233689416e59c86d1ae4cf055cd`.
- Parallel PR #35 remains research-only and has no `ChatGPTClient/**`, product Xcode Candidate, or exact product-path overlap with this b108 scope.

**Next exact action:** after this Runtime/allocation checkpoint is durably committed, apply only the two-path b108 delta, pass `git diff --check` + Debug Simulator compile, bind package CI to exact b108 product source, then produce one canonical b108 IPA for Human Runtime. Do not claim the inherited b107 accepted-EOF branch Runtime-positive unless exact `stream_ended_without_done` evidence occurs.

## b106 Human Runtime Partial / b107 accepted-SSE EOF handoff allocation — 2026-09-05

Exact b106 package identity restored from repository/package evidence:

- Candidate `DEV-send-stream-0.1.0-b106` / `0.1.0 (106)` remains permanently reserved. Product `028100bb79d82e99b62a610e9f30b9f9b3bd7f5c`; canonical package `a02042608911b891a4e9730a2bb3974168c4308a`; staging `33953874027/101273525329`; Push `33953950307/101273735236`; PR `33953951744/101273739204`; Artifact `9965747978`; ZIP `sha256:0558f3926b921b4e06b6336e1a251a8c1cbab661038cd34a303a83046039e4e2`; IPA `sha256:65acacb62506449bb65356a561603062a0f2b5bae4dc266a811480868b052288`.
- Exact Human Runtime diagnostics `sha256:b52e6177b2d3d44c124419c18ec88a356860f8a169a12f1a4cc6e46bb8e6faec`, 65,950 bytes, identify Release Build106/Candidate b106/source `a02042608911` on iPhone/iOS17.0. Exact accompanying video `sha256:fd358795b1fb78576eaa160416defae95389055c174b04fd37a471f83f161b02` remains visual evidence.

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

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable. Pre-b107 safe baseline `9541bcb22cab87254c881272b7226bef670d2e35`. Four preceding connector-cleanup history commits are tree-neutral relative to `e5b8041d...`; no product path differs because of them.
- `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Parallel PR #35 remains draft research-only at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`, with no product Xcode/`ChatGPTClient/**`/Candidate overlap.
- Intended b107 product scope is exactly `ChatGPTClient.xcodeproj/project.pbxproj` and `ChatGPTClient/RootViewController.swift`.

Batch recovery point:

- Batch A: record this b106 Runtime classification, restore exact b106 package truth in Build/Test, and reserve b107 before product changes.
- Batch B: apply only the exact two-product-path b107 delta, run `git diff --check` + Debug Simulator compile, then commit/push exact product.
- Batch C: bind formal b107 package workflow to the exact b107 product commit, require same-source Push + PR CI, canonical Artifact and independent IPA identity/hash verification, then update durable state/rules/adapter/checkpoint/PR metadata before Human Runtime.
- Recovery must not alter b106/b105 canonical identities, b106 SSE-ID handoff, b103 hard-Web recovery, b101 `-1005` recovery, PR #35, or any previously reserved Candidate.

**Next exact action:** complete Batch B only after this allocation is durably committed. Human Runtime b107 must prove accepted `stream_ended_without_done` no longer creates `phase=failed` or `回答失败`, same-generation no-resend observer recovery reaches authoritative terminal convergence, and manual Sync cannot leave authoritative rows plus a stale failed live tail.

## b105 Human Runtime Partial / b106 SSE identity + assistant-cell reset allocation — 2026-09-05

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

## b105 authoritative new-chat first-Send — package ready 2026-09-05

Exact product/package evidence:

- Candidate `DEV-send-stream-0.1.0-b105` / `0.1.0 (105)`, permanently reserved. Exact product `6ef4e874d7c2c5f144ab7e784f7a81755d1b2f59`; canonical package source `93ab92a9a4a7b8a020ac209f6a82088dc77acbce`.
- b105 product delta is exactly three product paths: `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/Conversation/ConversationFeature.swift`, `ChatGPTClient/RootViewController.swift`.
- Corrected staging `33923512745/101186860450` passed exact three-product-path audit, `git diff --check` and Debug Simulator compile before committing/pushing the product. Earlier run `33922377182` was a zero-job YAML parse failure and run `33923319785/101186252076` stopped at a deterministic patch-guard ambiguity after Batch A; neither wrote b105 product code and neither is product/Simulator failure evidence.
- Formal Push `33923732331/101187538891` and PR `33923735651/101187548902` both passed on exact package source `93ab92a9a4a7b8a020ac209f6a82088dc77acbce`.
- Canonical Push Artifact `9956018294`; GitHub Artifact digest and independently recomputed ZIP SHA-256 both equal `ba53bc8e50e1b89056565e3a557e196ef6b9c5db76e3b40dd28a0536e81d6921`.
- Canonical IPA `ChatGPTClient-0.1.0-b105-dev-send-stream.ipa`; independent SHA-256 `d162a7132ff830d3a2f6eb85a2b4a5b4ebc2d9f84531b01418912c99109e5095`, matching sidecar. Package inspection verifies `com.whitesharkssw.chatgptclient`, `0.1.0 (105)`, Candidate b105, source `93ab92a9a4a7`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS, Mach-O 64-bit arm64.

Behavior / evidence boundary:

- New Chat opens a Native draft with no fake server conversation ID. One covered official root-page executor owns the first protected Send/challenge flow.
- For that first Send, the bridge permits the real protected `/backend-api/f/conversation` fetch only after the official page route exposes a concrete authoritative conversation ID. Missing identity emits `new_conversation_identity_missing` and blocks the protected fetch rather than creating an untrackable server turn.
- `.conversationCreated(realID)` re-keys the same covered executor to the real server ID, selects it only if the draft is still the visible surface, and starts exactly one `ConversationRepository` live generation for that ID. Existing b103/b104 accepted-client hard-Web recovery and terminal authoritative Detail reconciliation remain unchanged.
- After successful terminal Detail for a newly created conversation, exactly one forced conversation-list refresh reconciles the server conversation into the sidebar. No polling, retry loop, timer/watchdog, resend/regenerate, challenge replay, guessed Native resume, fake persisted ID or second response/content store is added.
- Stop is not implemented by b105; exact response-scoped Stop route/target/ack evidence remains required before a later change.
- b105 is package-qualified only. Human Runtime is Pending; Stable/Frozen remains No.
- Any later docs/staging commit or Artifact does not replace canonical b105 package source `93ab92a9a4a7b8a020ac209f6a82088dc77acbce`, Artifact `9956018294` or IPA SHA `d162a7132ff830d3a2f6eb85a2b4a5b4ebc2d9f84531b01418912c99109e5095`.

Evidence ladder: **Code written / exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**

**Next exact action:** install only canonical b105 and run one new-conversation first Send from the Native draft. Require one official authoritative-ID handoff before protected fetch, exactly one HTTP200 SSE protected Send, one Repository generation through terminal + authoritative Detail, and one sidebar list reconciliation. Export diagnostics. Do not test/claim Stop in this candidate.

## b105 new-chat first-Send authoritative handoff allocation — 2026-09-05

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

## b104 background-return ordinary Send Runtime Positive — 2026-09-05

Exact Human Runtime evidence:

- Canonical Candidate `DEV-send-stream-0.1.0-b104` / Build104 / source marker `08fab73ab9a6`; diagnostics `ChatGPTClient-Diagnostics-20260904-205521.json`, exact `sha256:3789dc478c0bdf46c0f2ca2f572ebc618b4f53299e39fe68086e6dc936387216`, 136663 bytes, iPhone / iOS17.0 / Release.
- No `coveredExecutor.killProbe` event exists. The run contains exactly one `coveredExecutor.requested`, one `submitResult`, one `sendObserved`, and one `sendResponse`; protected Send was explicitly accepted as HTTP200 `text/event-stream` and there was no duplicate Send.
- The response was active on `responseGeneration=1` before `willResignActive` at `20:53:33Z` and `didEnterBackground` at `20:53:39Z`. One final background-side tool event was logged at `20:53:41Z`; then there are no response events until foreground at `20:55:15Z`, so this sample does not prove continuous app/WebKit execution while iOS was suspended.
- On `willEnterForeground` / `didBecomeActive` at `20:55:15Z`, the same generation immediately delivered a 123-event backlog in that timestamp: remaining tool/reasoning events, 94 final deltas, `finalCharacters=3333`, then `terminal phase=completed`. This explains why the completed answer was already visible immediately on return before the authoritative sync finished.
- Terminal automatically emitted `authoritativeReconcile.requested` and exactly one `latestSync.start` in the same second. The authoritative Detail GET returned HTTP200 at `20:55:17Z`, changed visible messages `21 -> 23` (`addedVisibleMessageCount=2`), then `liveResponse.reconciled responseGeneration=1` and `authoritativeReconcile.completed liveSnapshotCleared=true` completed automatically.
- Therefore the user's observed post-return loading indicator is consistent with the automatic authoritative Detail reconciliation that follows the already-present live/backlog answer. The live backlog supplies immediate visible content; the one-shot Native Detail sync then replaces/confirms it with server-backed authoritative state.
- A covered observer was recreated after reconciliation and its status returned HTTP200 `COMPLETE` at `20:55:20Z`. This is a redundant post-return observation in this sample, but it caused no second Send and no incorrect content/state result; do not allocate b105 or change product solely from this observation without a demonstrated user-impacting defect.

Evidence boundary:

- b104 ordinary no-probe Send regression is **Human Runtime Positive**, including foreground return after ~96s background and automatic terminal authoritative convergence.
- This result does not prove true response execution while the iOS app is suspended; the absence of response events during most of the background interval is consistent with suspension and later backlog delivery on foreground.
- b103 hard-Web accepted-client recovery remains separately Runtime Positive. The b101 exact `-1005` recovery remains Unexercised. Stable-Frozen remains No.

Evidence ladder: **b103 hard-Web recovery Runtime Positive / b104 ordinary no-probe + background-return Runtime Positive / CI+Artifact/package identity already verified / Stable-Frozen No.**

**Next exact action:** no product change and no b105 allocation from this sample. Preserve canonical b104. If a future Runtime sample shows the post-return loading/redundant observer causes a concrete UX or correctness failure, scope that exact defect from new evidence; otherwise keep the current automatic authoritative convergence path.

## b104 normal no-probe accepted-client recovery — package ready 2026-09-05

Exact Runtime / package evidence:

- b103 Human Runtime diagnostics `sha256:99049f500c129571d33aa628720f7d23ce5cf6d183e887938cd7fa621a3bbc51` is decisive for the accepted-client hard-Web recovery gate. The exact run had one protected Send, explicit HTTP200 `text/event-stream` acceptance, deterministic hard WebContent death, immediate `acceptedClientWebProcessRecovery` / `acceptedClientRecovery.started` on the same `responseGeneration=1`, no lifecycle nudge, HTTP200 `IS_STREAMING`, matching external snapshot, HTTP200 SSE resume, natural terminal, and automatic authoritative Detail `19 -> 21` reconciliation with live state cleared. There was no second protected Send.
- `DEV-send-stream-0.1.0-b104` / `0.1.0 (104)` is permanently reserved as the first normal candidate after that deterministic test. Exact product `4aebb546f3be6b71de0a67f466e6557a357dbfdc`; canonical package source `08fab73ab9a6fb83f6aa97702d2d4cd358b6ec43`.
- b104 product delta from the b103 Runtime checkpoint is exactly three product paths: Build/Candidate 103 -> 104 plus removal of kill-probe Xcode membership, one AppDelegate installer line removal, and deletion of `CoveredWebProcessKillProbe.swift`. `RootViewController.swift` accepted-client recovery logic is unchanged.
- Staging `33917182143 / 101166941594` passed exact three-product-path audit and Debug Simulator compile before committing product `4aebb546f3be6b71de0a67f466e6557a357dbfdc`.
- Formal Push `33917342654 / 101167460031` and PR `33917346052 / 101167471587` both passed on exact package source `08fab73ab9a6fb83f6aa97702d2d4cd358b6ec43`.
- Canonical Push Artifact `9953695815`; downloaded Artifact ZIP independently recomputed `sha256:2ef6278a72fd46e86cb279a97e0e84b2228b5c78eb390cdc7582229b84e3d82e`, matching GitHub's Artifact digest.
- Canonical IPA `ChatGPTClient-0.1.0-b104-dev-send-stream.ipa`; independently recomputed `sha256:9c35141e9877621d3a7e39245982cba6722acbb17a19f5ebabd8734d2b94df04`, matching the emitted sidecar.
- Independent package inspection confirms `com.whitesharkssw.chatgptclient`, `0.1.0 (104)`, Candidate b104, source marker `08fab73ab9a6`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS, Mach-O 64-bit arm64. Binary contains the accepted-client recovery diagnostics and contains no `_killWebContentProcessAndResetState`, `coveredExecutor.killProbe`, `CoveredWebProcessKillProbe`, or b103 swizzle method.

Evidence boundary:

- b103 accepted-client hard-Web recovery is **Human Runtime Positive for the tested foreground iPhone/iOS17 path**. This does not prove true execution while iOS suspends the app, pre-acceptance Web death recovery, silent-but-alive Web stalls, generic navigation failure recovery, or the separate b101 exact `-1005` branch.
- b104 contains no deterministic kill instrumentation. Its Human Runtime gate is an ordinary no-probe Send regression only; do not expect or force a 120-second Web kill.
- No resend/replay/regenerate, timer/watchdog, polling, heartbeat, challenge replay, guessed Native resume, or second response/content authority is added.

Evidence ladder: **b103 recovery Runtime Positive / b104 Code written / exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / b104 ordinary Runtime pending / Stable-Frozen No.**

**Next exact action:** install only canonical b104 and run an ordinary existing-conversation Native Send. Confirm there is no `coveredExecutor.killProbe`, protected Send is HTTP200 SSE accepted once, normal reasoning/tools/final reaches terminal and automatic authoritative reconcile, with no artificial WebContent death. Export diagnostics. Do not allocate b105 unless b104 Runtime exposes new evidence.

## b103 accepted-client hard-Web recovery Runtime Positive + b104 probe-removal allocation — 2026-09-05

Exact b103 Human Runtime evidence:

- Canonical Candidate `DEV-send-stream-0.1.0-b103` / Build103, source marker `e1cca160e9c4`; diagnostics `ChatGPTClient-Diagnostics-20260904-202930.json`, exact `sha256:99049f500c129571d33aa628720f7d23ce5cf6d183e887938cd7fa621a3bbc51`, 405144 bytes, iPhone / iOS17.0 / Release.
- The tested Native Send produced exactly one `coveredExecutor.requested`, one `submitResult`, one `sendObserved`, and one `sendResponse`. Send acceptance was explicit HTTP200 `text/event-stream` at `20:26:24Z`; there was no second protected Send anywhere in the export.
- The b103 probe fired at `20:28:23Z` while generation `1` remained active. In the same second Runtime recorded `webProcess terminated mode=client_send_or_idle`, `acceptedClientWebProcessRecovery state=handoff_requested policy=no_resend_same_generation`, executor release, and `acceptedClientRecovery.started trigger=web_process_terminated responseGeneration=1`.
- There was no `willResignActive`, `didEnterBackground`, `willEnterForeground`, or `didBecomeActive` event after the kill. Recovery therefore required no lifecycle nudge.
- The fresh observer returned HTTP200 `IS_STREAMING` at `20:28:26Z`, an external snapshot at `20:28:27Z` with the exact pre-kill continuity point `reasoningCharacters=884 / toolCount=21 / responseGeneration=1`, and `/resume` HTTP200 `text/event-stream` at `20:28:32Z`.
- Every post-kill event carrying a response generation used generation `1`. The same generation advanced to `reasoningCharacters=1768`, `toolCount=24`, `finalCharacters=7649`, then natural `terminal phase=completed` at `20:29:26Z`.
- Automatic authoritative reconcile immediately followed: one Detail HTTP200 changed authoritative visible messages `19 -> 21`; `liveResponse.reconciled responseGeneration=1` and `authoritativeReconcile.completed liveSnapshotCleared=true` occurred at `20:29:28Z`.
- Therefore b103 accepted-client hard-Web recovery is **Human Runtime Positive** for the tested foreground iPhone/iOS17 path: explicit accepted Send survives hard WebContent death, the same Repository generation automatically reattaches without resend or lifecycle nudge, live reasoning/tools/final continue, and terminal authoritative convergence clears the live projection.

b104 allocation / minimal next product action:

- Allocate and permanently reserve `DEV-send-stream-0.1.0-b104` / `0.1.0 (104)`. b104 is the first normal candidate after the deterministic b102/b103 kill experiment; Stable/Frozen remains No.
- Preserve the exact b103 accepted-client recovery logic in `RootViewController.swift` unchanged.
- Remove only the test instrumentation: delete `CoveredWebProcessKillProbe.swift`, remove its AppDelegate installer and Xcode file/build membership, then advance Build/Candidate 103 -> 104.
- Do not retain `_killWebContentProcessAndResetState`, the 120-second timer, swizzling or any probe-only behavior in b104. Do not add replacement timers, retries, polling, watchdogs, resend, challenge replay, guessed Native resume or a second response owner.
- Human Runtime for b104 should be an ordinary no-probe Send regression, not another forced-kill test. Hard-death recovery mechanism itself is already Runtime Positive on exact b103.

Resume/conflict guard before b104 product write:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 remains open/unmerged/mergeable at pre-stage head `964143043fa12e7902008bc6ef57a98e8c658393`; base `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Parallel PR #35 / `DEV-official-sync-reload` remains draft at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`, research-only, with no product/Candidate conflict.
- `BUILD_TEST_INDEX.md` contains no b104 before this allocation.

Batch recovery point:

- batch A in this staging run: record this b103 Runtime result + b104 allocation in checkpoint/index and push it before product changes;
- batch B: remove only the b103 kill probe, advance Build/Candidate to b104, run exact-scope audit + Simulator compile, then commit/push product;
- after batch B, formal packaging must bind `ios-foundation.yml` to the exact b104 product commit, then Push/PR CI + canonical Artifact/package verification must complete before Human Runtime;
- recovery must not alter b103 canonical product/package/Artifact, PR #35, accepted-client recovery logic, TD-029 one-Send ownership, or earlier reserved Candidate identities.

**Next exact action:** complete batch B only: remove the diagnostic kill probe and advance Build/Candidate to b104 without touching accepted-client recovery; exact-scope audit + Simulator compile before product commit.

## b103 accepted-client hard-Web recovery — package ready 2026-09-05

Exact package evidence:

- Candidate `DEV-send-stream-0.1.0-b103` / `0.1.0 (103)`, permanently reserved. Exact product `d514e9a5bde01bf3243d81016bf8cbda533fd5bf`; canonical package source `e1cca160e9c466ab98a2aeffc038e94f58335cab`. b103 is a Runtime recovery test candidate, not Stable/Frozen.
- Corrected guarded staging `33913972639 / 101156743875` passed b102 Runtime/checkpoint allocation, exact three-product-file scope audit and Debug Simulator compile, then committed product `d514e9a5bde01bf3243d81016bf8cbda533fd5bf`. Earlier staging `33913633892 / 101155651591` stopped before product write while matching the docs allocation marker and emitted no b103 product commit.
- Formal Push `33914210593 / 101157497020` and PR `33914214638 / 101157509705` both passed on exact package source `e1cca160e9c466ab98a2aeffc038e94f58335cab`.
- Canonical Push Artifact `9952548424`; downloaded Artifact ZIP independently recomputed `sha256:27fc23f1cb48d585ab3ffc0b181ec0dffafc42ccb3069fd72cbf5a0ba647f77a`, matching GitHub's Artifact digest.
- Canonical IPA `ChatGPTClient-0.1.0-b103-dev-send-stream.ipa`; independently recomputed `sha256:f41c81a89552027fb4c42152eb3864c1732494465230ffd4787c6bba56d746c3`, matching the emitted sidecar.
- Independent package inspection confirms `com.whitesharkssw.chatgptclient`, `0.1.0 (103)`, Candidate b103, source marker `e1cca160e9c4`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, `iPhoneOS`, Mach-O 64-bit arm64. Binary strings include the exact b103 Candidate, `coveredExecutor.acceptedClientWebProcessRecovery`, `acceptedClientRecovery.started`, and `_killWebContentProcessAndResetState`.

Behavior / evidence boundary:

- b102 Human Runtime `sha256:6d2fde277427d3bbad6549946855c68b8df7e0433389b2d5c9e7d98212a3a6a6` proved the original client Send had exactly one protected Send and explicit HTTP200 SSE acceptance before deterministic WebContent death; server generation survived, and the same turn later resumed through existing covered observation/Detail with no second Send and reached terminal/final convergence.
- b103 therefore changes hard WebContent death only after exact client SSE acceptance: preserve the same prompt-owned Repository generation, emit `acceptedClientWebProcessInterrupted` instead of `.failed`, release the dead executor, and attach one fresh covered observer to the same generation immediately while active or on next foreground when inactive. It never resends/replays/regenerates the prompt.
- The one-shot 120-second kill remains Candidate-gated deterministic Human Runtime instrumentation only. It is not a production timeout/watchdog and must be removed/disabled before a later normal/Stable candidate.

Evidence ladder: **Code written / exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / b102 causal Runtime Positive / b103 recovery Runtime pending / Stable-Frozen No.**

**Next exact action:** install only canonical b103. Fresh-launch, open an existing conversation, start one deliberately >2-minute Native Send, keep the app foreground, and do not touch Sync/Reload/Stop or background the app. At ~120s expect `killProbe firing -> webProcess terminated -> acceptedClientWebProcessRecovery state=handoff_requested -> acceptedClientRecovery.started` with the same `responseGeneration`, followed by covered `IS_STREAMING`/snapshot/resume/live continuation and final terminal reconcile. There must be exactly one protected Send and no lifecycle nudge.

## b102 Human Runtime decisive + b103 accepted-client hard-Web recovery allocation — 2026-09-05

Exact b102 Human Runtime evidence:

- Canonical Candidate `DEV-send-stream-0.1.0-b102` / Build102, source marker `78bd3d2f3e45`; diagnostics `ChatGPTClient-Diagnostics-20260904-193801.json`, exact `sha256:6d2fde277427d3bbad6549946855c68b8df7e0433389b2d5c9e7d98212a3a6a6`, 460465 bytes, iPhone / iOS17.0 / Release.
- One Native protected Send started at `19:33:48Z`; exact counts are one `coveredExecutor.requested`, one `submitResult`, one `sendObserved`, one `sendResponse`. `sendResponse` was HTTP200 `text/event-stream`, so server acceptance is explicit before transport death.
- The deterministic probe fired at `19:35:54Z` while the response was still active: `coveredExecutor.webProcess state=terminated mode=client_send_or_idle`. Legacy behavior then marked the client-owned generation failed and released the executor.
- The server-side turn survived. After the user briefly backgrounded/foregrounded, existing b100 foreground discovery issued one authoritative Detail HTTP200, changed visible messages `17 -> 18`, observed `latestUserChanged=true` / `rearmDiscoveredRemoteTurn=true`, and created an external authoritative projection.
- A fresh covered observer then returned HTTP200 `IS_STREAMING`; `/resume` returned HTTP200 `text/event-stream`; reasoning/tool/final events continued to terminal with final 6079 chars, reasoning 2924 chars and 31 tools. Automatic terminal reconcile then changed authoritative visible messages `18 -> 19` and cleared the live projection.
- There was no second protected Send. Therefore hard WebContent death after explicit Send acceptance is now **Runtime proven to be transport loss, not server-turn failure** for this scenario. The remaining product defect is that current b102 requires a lifecycle nudge because it converts the client-owned generation to failed/released at the kill.

b103 allocation / minimal product direction:

- Allocate and permanently reserve `DEV-send-stream-0.1.0-b103` / `0.1.0 (103)`. b103 is a recovery test candidate, not Stable/Frozen.
- Only exact client Send HTTP200 `text/event-stream` acceptance may arm automatic hard-Web recovery. WebContent death before explicit acceptance remains failure and must never auto-resend/replay/regenerate.
- On accepted-client `webViewWebContentProcessDidTerminate`, preserve the existing Repository generation and prompt-owned live response; emit a transport-interruption event instead of `.failed`, release the dead executor, and when active create one fresh covered observer for the same conversation using the same Repository generation. No second Send occurs.
- If the app is inactive when the hard death callback arrives, do no background network work. The live client-owned snapshot remains active with no executor; on the next foreground lifecycle, one fresh covered observer is attached to that same generation.
- Reuse the already-proven external observation parsing path for `IS_STREAMING`, snapshot, `/resume`, reasoning/tool/final/terminal. `ConversationRepository` remains the sole response/content authority and the existing terminal authoritative Detail reconcile remains final authority.
- b103 may reuse the already-proven one-shot 120-second kill probe, Candidate-gated to exact b103, only to deterministically validate this new recovery path. It remains diagnostic instrumentation, not product timeout/watchdog policy, and must be removed/disabled before any later normal/Stable candidate.
- No timer beyond that explicit test probe, no polling, retry loop, heartbeat, duplicate Send, challenge replay, guessed resume, second response store or Native protected-Send implementation is authorized.

Resume/conflict guard before product write:

- Work `DEV-send-stream`; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable; verified pre-allocation head `8081203d587d04e058d91e7985c45f36a361a99d`; base `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Parallel PR #35 / `DEV-official-sync-reload` remains draft research-only at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`, with no `ChatGPTClient/**` product overlap or Candidate ownership conflict.
- `BUILD_TEST_INDEX.md` has no b103 identity before this allocation.

**Next exact action:** apply only Build/Candidate 103, exact b103 Candidate gate for the already-proven kill probe, and accepted-client hard-Web transport handoff in `RootViewController.swift`; run exact-scope audit + Simulator compile before formal packaging.

## b102 deterministic client-owned WebContent-death probe — package-ready 2026-09-05

Exact evidence:

- Candidate `DEV-send-stream-0.1.0-b102` / `0.1.0 (102)`, permanently reserved. This is a **diagnostic-only** candidate requested to make hard covered-Web death reproducible; it does not add client-owned response recovery.
- Exact product head `670310b4e8b15176f721291f4f96e46feadec46a`; canonical package source `78bd3d2f3e45c8e0061865d3133b92a274139110`. Relative to the verified pre-allocation head, product scope is exactly Xcode Build/Candidate + `AppDelegate.swift` installer + new `Protocol/CoveredWebProcessKillProbe.swift`; the package-source child changes only `ios-foundation.yml`.
- Probe behavior: only exact b102 installs a runtime interception of `WKWebView.evaluateJavaScript`; the first script containing the fixed `window.__coveredWebSendExecutor.submit(` marker arms one 120-second main-queue diagnostic action without logging prompt/script content. At fire it invokes `_killWebContentProcessAndResetState` only when that exact `WKWebView` responds to the selector. No Send/retry/resume API exists in the probe.
- Push `33910845721 / 101146639944` and PR `33910858535 / 101146674919` passed guard + unsigned TrollStore build. Canonical Push Artifact `9951331101`, ZIP `sha256:2da6bb66d0c5eba55d93463881e0ff5d0d55a9d7844f068d024e5cee31dff24a`. Same-source PR Artifact `9951329921` is CI corroboration only.
- Canonical IPA `ChatGPTClient-0.1.0-b102-dev-send-stream.ipa`, independently recomputed `sha256:53eb1845a3fbd4543ebdb5e9a69e078b3f07866c2c395a666dca9b2928ecd8af`, matching sidecar.
- Independent package inspection confirms `com.whitesharkssw.chatgptclient`, `0.1.0 (102)`, Candidate b102, source marker `78bd3d2f3e45`, Release, iOS14 minimum, UIDeviceFamily `[1,2]`, iPhoneOS, Mach-O arm64. Binary strings contain the exact b102 Candidate, `coveredExecutor.killProbe` and `_killWebContentProcessAndResetState`.

Evidence ladder: **Code written / exact diagnostic scope audited / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**

**Next exact action:** install only canonical b102. Fresh-launch the app, choose an existing conversation, start exactly one deliberately >2-minute Native `测试发送…` response and keep the app foreground. Do not press Sync/Reload/Stop and do not send a second prompt. Expect `coveredExecutor.killProbe` `installed -> armed -> firing` at ~120s, followed by `coveredExecutor.webProcess state=terminated mode=client_send_or_idle` while the response is still active. Current product behavior is expected to mark that client-owned live response failed and release the executor; let the server-side generation finish, then export diagnostics. If the response finishes before `firing`, the run does not qualify and must be repeated with a longer response. Do not interpret this diagnostic timer as production timeout/retry policy.

## b102 deterministic client-owned WebContent-death diagnostic allocation — 2026-09-05

User explicitly pivots the next `DEV-send-stream` gate from waiting for another naturally occurring b101 `-1005` sample to a deterministic client-owned WebContent-process-death test. The 120-second termination is **diagnostic instrumentation only**, not production recovery policy.

Resume / conflict guard:

- Work `DEV-send-stream` remains selected; branch `dev/send-stream-20260829`; PR #29 is open / unmerged / mergeable.
- Verified pre-allocation branch head `18c1ff13c2ae3c3191414afc89e86ff73b5b78ac`; current target `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Canonical b101 remains permanently reserved: product `54a9fa52a7b44a1b7418a39e4b0f7493989f999d`, package `da103452236e31e070eae68b9e7979a832662fc1`, Artifact `9948780963`, IPA `sha256:463bafd4daea37a429088e670d32474cdd9f429347d1fba336d8a091b1f31df3`. Its exact `-1005` recovery branch remains Unexercised; b102 does not replace or rewrite that evidence.
- Parallel PR #35 / `DEV-official-sync-reload` remains draft/open at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`, research-only, with no `ChatGPTClient/**` product overlap or Candidate-number ownership conflict.
- Repository search found no existing `DEV-send-stream-0.1.0-b102`; `DEV-send-stream-0.1.0-b102` / `0.1.0 (102)` is now allocated and permanently reserved.

Evidence-backed diagnostic boundary:

1. Do **not** add client-owned recovery behavior yet. Current b98 rule intentionally still treats client-owned protected-Send WebContent death as failure; b102 exists to force that exact Runtime path before deciding the smallest recovery change.
2. Add one Candidate-gated Runtime probe that observes only the existing `CoveredWebSendExecutor` JavaScript submit invocation. The probe must not inspect/log prompt text; it only recognizes the fixed bridge call prefix.
3. On the first matching covered protected-Send submit for one `WKWebView`, schedule exactly one main-queue action 120 seconds later. This explicit timer exists only because the user requested a deterministic forced-death test; it is not a timeout, watchdog, keepalive, retry or production lifecycle signal.
4. At fire time, call the WebKit SPI selector `_killWebContentProcessAndResetState` on that exact `WKWebView` only when `responds(to:)` is true. Use Objective-C runtime dispatch so the app does not hard-link a private symbol. WebKit upstream exposes `_killWebContentProcess` / `_killWebContentProcessAndResetState` specifically as Web-process termination SPI/test surface.
5. Expected diagnostic chain if the answer is still active: `coveredExecutor.killProbe state=firing` -> `coveredExecutor.webProcess state=terminated mode=client_send_or_idle` -> existing client-owned `.failed(web_process_terminated)` / executor release. No prompt resend/regenerate, no duplicate protected Send, no Native guessed resume, no polling and no second response authority.
6. If the response naturally finishes before 120 seconds, a later forced idle Web kill does **not** qualify the client-owned active-response gate; repeat with a deliberately >2-minute response. Keep the app foreground for the deterministic first test so iOS suspension does not postpone the diagnostic timer.
7. b102 Runtime evidence decides the next product action. If server generation survives while Native marks the response failed, the next candidate may test no-resend conversion to page-owned observation / authoritative Detail reconciliation using only already-evidenced mechanisms. Do not implement that recovery in the same diagnostic candidate.

Intended b102 source scope:

- `ChatGPTClient.xcodeproj/project.pbxproj` — Build102 / Candidate b102 and compile membership for one diagnostic source;
- `ChatGPTClient/AppDelegate.swift` — install the probe once at launch; exact b102 Candidate guard remains inside the probe;
- `ChatGPTClient/Protocol/CoveredWebProcessKillProbe.swift` — one-shot submit-observer + 120-second WebContent termination instrumentation.

Batch recovery point:

- confirmed complete: task routing; AGENTS/START_HERE and required Send/background plans re-read; branch/PR/base/b101 identity verified; PR #35 conflict checked; b102 uniqueness checked; user explicitly authorized the 120-second forced-Web test; WebKit SPI existence verified from current upstream source/header;
- pending batch A: create the new diagnostic Swift file, wire AppDelegate + Xcode Build102 membership, verify exact three-product-file scope and Swift/Xcode compile;
- pending batch B: formal Push/PR CI and canonical b102 Artifact/IPA identity verification;
- pending batch C: update BUILD_TEST_INDEX / PROJECT_STATE / MODULE_STATUS / relevant rule/decision docs and PR #29 metadata, then hand exact IPA to Human Runtime;
- recovery must not touch PR #35, canonical b101 product/package/Artifact, earlier reserved Candidates, protected-Send/challenge rules, or `ConversationRepository` response ownership.

**Next exact action:** implement only the three-file b102 deterministic kill probe described above; compile before packaging. Human Runtime must launch b102 fresh, start exactly one deliberately >2-minute Native `测试发送…` response, keep the app foreground, do not press Sync/Reload/Stop, wait for the automatic 120-second WebContent kill, then let the server-side answer finish and export diagnostics.

## b101 Human Runtime — healthy long-suspension path; b100 rearm/reconcile gates Positive — 2026-09-05

Exact tested evidence:

- Candidate `DEV-send-stream-0.1.0-b101` / `0.1.0 (101)`; source marker `da103452236e`; Release / iPhone / iOS17.0; diagnostics `ChatGPTClient-Diagnostics-20260904-185039.json`, `sha256:f7209546f3f2d1dd8ad08458b0dea8adbef522af100deb2f5de90cbe26180b9d`, 95964 bytes / 182 events.
- This sample contains zero exact `NSURLErrorDomain -1005`, zero `detail.transportRecovery` / `list.transportRecovery`, zero `authTransport.retired` / `authTransport.recoveryReady`, zero `coveredExecutor.webProcess`, and zero client-owned protected-Send evidence (`sendObserved`). Therefore the b101 bounded `-1005` recovery branch is **Unexercised / Unverified**, hard WebContent-process death is **Unexercised**, and this is **not** a client-owned accepted-Send death-recovery test.
- Dormant unfinished-turn discovery/rearm is Runtime Positive. App backgrounded `18:27:51Z -> 18:30:30Z` (~2m39s). Automatic `foregroundConversationDiscovery` issued one authoritative Detail, HTTP200 changed visible messages `13 -> 14`, and completed with `latestUserChanged=true` / `rearmDiscoveredRemoteTurn=true`. Covered observation then rearmed; a new user WebSocket opened, `externalStreamStatusResponse` returned HTTP200 `IS_STREAMING`, and Repository started `source=external_page_owned`; the next snapshot reached reasoning 112 chars / service messages 6 / tools 2.
- Known-active external foreground reconcile is Runtime Positive. While that external response was active, app backgrounded `18:30:44Z -> 18:32:40Z` (~1m56s). Foreground automatically emitted `foregroundExternalDetailReconcile.requested` plus Web page rebootstrap. Authoritative Detail HTTP200 changed `14 -> 15`, emitted `liveResponse.externalDetailReconciled(reason=authoritative_assistant_materialized)`, cleared the live projection and released the executor.
- WebSocket transport interruption was real but distinct from WebContent death: on both `18:30:30Z` and `18:32:40Z` the user socket emitted `error` + `close(1006)`. The first was followed by a new socket `created/open/message` and live continuation; the second coincided with Native authoritative final convergence. No `webViewWebContentProcessDidTerminate` callback occurred.
- Long dormant foreground discovery remained healthy after `18:32:48Z -> 18:50:23Z` (~17m35s): one automatic Detail returned HTTP200 and materialized `15 -> 17` (`addedVisibleMessageCount=2`, `latestUserChanged=true`, `rearmDiscoveredRemoteTurn=false`). This is normal-path long-suspension regression evidence only; because no `-1005` occurred, it does not accept the new b101 recovery branch.

Runtime classification:

- b101 bounded Native `-1005` recovery: **Unexercised / Unverified**;
- b100 unfinished remote-turn discovery + one covered rearm: **Runtime Positive**;
- b100 known-active external foreground Detail reconcile: **Runtime Positive**;
- b100 long dormant foreground discovery: **Runtime Positive again**, including ~17m35s in this sample;
- WebSocket `1006` interruption tolerance for the tested external flow: **Runtime Positive** via observer rearm / authoritative Detail convergence;
- b98 hard WebContent-process recovery: **Unexercised / Unverified**;
- client-owned accepted protected-Send recovery after Web/WebContent death: **Unexercised / future gate**;
- overall `DEV-send-stream`: **Runtime Partial / Stable-Frozen No**.

**Next exact action:** keep canonical b101 unchanged; no b102/product change is justified by this sample. Continue b101 only until an exact `-1005` sample exercises its bounded recovery branch, or explicitly pivot to the separately scoped client-owned accepted-Send transport-death gate. Never treat WebSocket code1006 as proof of `WKWebView` WebContent-process death and never auto-resend a protected Send.

## b101 Native read transport renewal — package-ready 2026-09-05

Exact evidence:

- Candidate `DEV-send-stream-0.1.0-b101` / `0.1.0 (101)`, permanently reserved.
- Triggering Runtime evidence remains exact b100 diagnostics `ChatGPTClient-Diagnostics-20260904-174041.json`, `sha256:515c60b59d969ee1f33d76fec097d6163450058c5ef3fa9ccd551b2439f03818`: after ~12m37s background, foreground discovery fired but authoritative Detail, later Detail, two conversation-list GETs and manual Sync all failed `NSURLErrorDomain -1005` while covered WebSocket independently reopened; no hard WebContent-process termination signal occurred.
- Exact b101 product commit `54a9fa52a7b44a1b7418a39e4b0f7493989f999d`; exact product delta is only `ChatGPTClient.xcodeproj/project.pbxproj` plus `ChatGPTClient/Conversation/ConversationFeature.swift`.
- Product behavior: only idempotent Native conversation-list / Conversation Detail GETs gain bounded recovery. On the first exact `NSURLErrorNetworkConnectionLost (-1005)`, retire the matching cached `AuthTransientSession`, reacquire one fresh transient session from the existing default-WebKit-auth path, re-check account/operation freshness, then retry that same GET once. A second failure terminates normally. Protected Web Send, covered Web observation, b100 foreground discovery, Repository content authority and client-owned response ownership are unchanged.
- Initial staging workflow run `33903494492` had zero jobs due workflow parse failure and is invalid evidence; it emitted no product change. Corrected staging `33903822115 / 101123907440` passed exact two-product-file scope, `git diff --check` and Debug iphonesimulator compile, then committed product `54a9fa52...`.
- Exact canonical package source `da103452236e31e070eae68b9e7979a832662fc1` changes only `ios-foundation.yml` after the product commit. Formal Push `33904070096 / 101124706091` and same-source PR `33904076581 / 101124726725` both passed.
- Canonical Push Artifact `9948780963`, Artifact ZIP `sha256:df5e95d273c0a4f977b47ac7b64eb654daea99e3b797c3c54924b820fd165e64`. Same-source PR Artifact `9948785659` is CI corroboration only and is not the Human Runtime package authority.
- Canonical IPA `ChatGPTClient-0.1.0-b101-dev-send-stream.ipa`, independently recomputed `sha256:463bafd4daea37a429088e670d32474cdd9f429347d1fba336d8a091b1f31df3`, matching the package sidecar.
- Independent package inspection confirms `com.whitesharkssw.chatgptclient`, `0.1.0 (101)`, Candidate b101, source marker `da103452236e`, Release, iOS14 minimum, UIDeviceFamily `[1,2]`, iPhoneOS and Mach-O 64-bit arm64.

Evidence ladder: **Code written / exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**

Batch recovery state:

- confirmed complete: b100 `-1005` Runtime evidence classified; b101 allocated; exact two-file product committed; corrected staging passed; canonical package source fixed; Push+PR package CI passed; canonical Artifact/IPA identity independently verified;
- this recorder batch owns only checkpoint + durable project docs. Product code, b101 package source/Artifact/IPA, PR #35 and prior candidates must not be changed by recovery;
- after this docs batch, only PR #29 metadata update and Human Runtime handoff remain.

**Next exact action:** use only canonical b101 IPA. Reproduce the long-suspension scenario that produced `-1005`; on foreground do not press Sync/Reload first. If the first authoritative Detail reports `-1005`, diagnostics must show exactly one `detail.transportRecovery` request, retirement of the current transient session, one fresh auth transport acquisition, one `transportAttempt=2`, then HTTP200/convergence or a normal terminal failure with no third attempt. Also verify conversation-list refresh remains functional after the same recovery. If the first GET is already healthy, the b101 recovery branch is Unexercised rather than accepted. Export diagnostics.

## b100 Human Runtime — Native transient transport failure / b101 allocation 2026-09-05

Exact tested evidence:

- Candidate `DEV-send-stream-0.1.0-b100` / `0.1.0 (100)`; Release / iPhone / iOS17.0; source marker `e88a50ad9c20`; diagnostics `ChatGPTClient-Diagnostics-20260904-174041.json`, `sha256:515c60b59d969ee1f33d76fec097d6163450058c5ef3fa9ccd551b2439f03818`, 77816 bytes / 146 events.
- Before the long background interval, authoritative Detail was healthy at HTTP200 / 10 visible messages. The app entered background at `17:26:58Z` and returned at `17:39:35Z` after about 12m37s.
- b100 foreground discovery itself fired correctly: `foregroundConversationDiscovery.requested` immediately started authoritative Detail generation 7. That GET failed after ~5s with exact `NSURLErrorDomain -1005` (`network connection lost`).
- This is **not evidence of hard WKWebView WebContent-process death**. The diagnostic contains zero `coveredExecutor.webProcess` and zero `coveredExecutor.externalWebProcessRecovery` events. On the same foreground return, covered Web created a user WebSocket at `17:39:35Z`, then opened and received a message at `17:39:36Z`.
- The failure persisted specifically across Native reads: foreground Detail generation 8 again failed `-1005`; two manual conversation-list GETs failed `-1005`; manual Sync Detail generation 9 also failed `-1005`. Meanwhile the covered Web user socket still emitted messages and later created/opened again at `17:40:13-14Z`.
- Current source explains the persistence. `ConversationRepository` caches one `AuthTransientSession` and `withTransientSession` reuses it indefinitely while account scope matches. The current transport is retired only for HTTP401/403; `normalizedTransportError` leaves `NSURLErrorNetworkConnectionLost` unchanged. Therefore a stale/broken ephemeral Native `URLSession` after suspension can be reused by Detail, list and manual Sync even while WebKit networking has independently recovered.

Runtime classification:

- b100 dormant foreground-discovery trigger: **still Runtime Positive as a lifecycle mechanism**;
- Native authoritative read transport after long suspension in this sample: **Runtime Negative** — repeated `NSURLErrorDomain -1005` across Detail/list/manual Sync with no successful Native HTTP recovery before export;
- b98 hard WebContent termination recovery: **still Unexercised / Unverified** because the hard termination callback did not occur;
- overall `DEV-send-stream`: **Runtime Partial / Stable-Frozen No**.

### b101 allocation / batch recovery point

- Work `DEV-send-stream` remains selected; branch `dev/send-stream-20260829`; PR #29 is open/unmerged/mergeable.
- Verified pre-allocation branch head `ff204bdd5874862e5b250f39bc0762bc1b94056f`; `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Parallel PR #35 / `DEV-official-sync-reload` remains draft/open at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`; it is research-only and has no `ChatGPTClient/**` product overlap.
- `BUILD_TEST_INDEX.md` has no b101 identity. `DEV-send-stream-0.1.0-b101` / `0.1.0 (101)` is now permanently allocated/reserved.

Evidence-backed minimum b101 product boundary:

1. Change only the Native read transport owner. Protected Web Send, covered-Web observation/rebootstrap, Repository content/response authority and b100 foreground-discovery conditions remain unchanged.
2. On the **first exact** `NSURLErrorDomain / NSURLErrorNetworkConnectionLost (-1005)` from an idempotent Native Conversation Detail or conversation-list GET, retire only the matching cached `AuthTransientSession` with existing in-flight tasks allowed to finish, then obtain one fresh transient session through the existing `withTransientSession` / default-WebKit-auth path.
3. Retry that same read operation **at most once** with the fresh transport. The retry stays under the same Detail/list operation generation and must re-check account scope and operation freshness before issuing the replacement GET.
4. A second `-1005`, any other network error, auth failure, HTTP failure, supersession or scope change terminates normally. No timer, cadence, retry loop, reachability watcher, background heartbeat, Send replay, guessed resume or second state authority.
5. Add privacy-safe diagnostics proving transport retirement, one fresh-session acquisition/recovery attempt, and whether that bounded attempt succeeds or fails.

Intended product scope:

- `ChatGPTClient.xcodeproj/project.pbxproj` — Build101 / Candidate b101 only;
- `ChatGPTClient/Conversation/ConversationFeature.swift` — exact `-1005` stale-transient retirement plus one bounded read recovery for list/Detail only.

Batch state:

- confirmed complete: new b100 diagnostics analyzed; Web-process-death hypothesis rejected for this sample; exact Native `-1005` persistence tied to current `AuthTransientSession` reuse; branch/base/PR29 verified; PR35 product-overlap checked; b101 uniqueness checked and allocated by this checkpoint;
- pending: apply exact two-product-file b101 delta; run exact-scope + `git diff --check` + Debug iphonesimulator compile; bind formal Push/PR package CI to the exact product head; verify canonical Artifact/IPA identity; update durable project docs and PR #29 metadata;
- do not touch PR #35, protected-Send/challenge transport, Web process-recovery semantics, b100 canonical Artifact/IPA identity, or any earlier reserved candidate identity.

**Next exact action:** implement only the two-file b101 bounded Native-read transport renewal above and validate it before packaging.

## b100 Human Runtime — dormant foreground discovery Positive 2026-09-05

Exact tested evidence:

- Candidate `DEV-send-stream-0.1.0-b100` / `0.1.0 (100)`; Release / iPhone / iOS17.0; source marker `e88a50ad9c20`; diagnostics `ChatGPTClient-Diagnostics-20260904-171109.json`, `sha256:f0f3619ea61f30f9bcbaadbb577f3a99839a032dfcd95503e22b4a7bdb984696`, 72063 bytes / 127 events.
- The selected conversation was complete/idle at authoritative visible message count `8`. App entered background at `16:45:36Z` with no active external live response and returned at `17:05:07Z` after 1171s (~19m31s).
- On foreground, without any preceding `conversation.latestSync.requested`, b100 emitted `foregroundConversationDiscovery.requested` and exactly one automatic authoritative Detail operation (`operationGeneration=2`). HTTP200 Detail changed visible messages `8 -> 10`; `latestSync.end` recorded `addedVisibleMessageCount=2`.
- `foregroundConversationDiscovery.completed` reported `latestUserChanged=true`, `activeExternalAfterSync=false`, `liveResponseActive=false`, `rearmDiscoveredRemoteTurn=false`, `visibleMessageCount=10`. This is the expected completed-remote-turn branch: the assistant was already authoritative, so no covered observer rearm was required.
- A second background interval lasted 327s (~5m27s). Foreground again issued exactly one dormant discovery and converged `10 -> 10` with `latestUserChanged=false` / `rearmDiscoveredRemoteTurn=false`. A later explicit manual Sync at `17:10:59Z` also remained `10 -> 10`, so it was not required for convergence.
- The user WebSocket produced `error` + `close` code `1006` on the long foreground return, then a new socket was `created/open` within seconds. No `coveredExecutor.webProcess` / `externalWebProcessRecovery` event occurred. This proves dormant authoritative discovery works despite a stale/broken WebSocket, but does not exercise hard WKWebView WebContent-process termination recovery.
- One iOS memory warning occurred on the long foreground return; the protected resident was retained and the app continued normally with no crash/relaunch in this diagnostic. This is sample-local stability evidence only.
- This run contains zero `liveResponse.event` / `liveResponse.presentationApplied`, so b99 backlog-coalescing stress is still Unexercised here. It also does not exercise `rearmDiscoveredRemoteTurn=true` for an unfinished newly discovered remote turn, nor the exact-b100 known-active `foregroundExternalDetailReconcile` branch.

Runtime classification:

- b100 primary dormant cross-platform foreground discovery: **Runtime Positive**, including ~19m31s background and automatic authoritative materialization `8 -> 10` with no manual Sync/Reload;
- no-change foreground discovery: **Runtime Positive / one-shot no-op**;
- unfinished remote-turn rearm: **Unexercised / Unverified**;
- exact-b100 known-active external reconcile regression: **Unexercised in this sample**;
- b99 backlog coalescing: **Unexercised / Unverified in this sample**;
- b98 hard WebContent termination recovery: **Unexercised / Unverified**;
- overall `DEV-send-stream`: **Runtime Partial / Stable-Frozen No**.

**Next exact action:** no product change or b101 is justified by this sample. Keep canonical b100. If further qualification is desired, return foreground while a newly created remote turn is still unfinished and verify `rearmDiscoveredRemoteTurn=true` + one covered rearm; separately regression-check exact-b100 known-active `foregroundExternalDetailReconcile`. Do not add polling/timers/heartbeat/retries.

## b100 foreground dormant discovery — package-ready 2026-09-05

- Candidate `DEV-send-stream-0.1.0-b100` / `0.1.0 (100)`, permanently reserved.
- Product `70c7dc052865ef80ca7bdec083d7621c1a297eab`; exact delta: Xcode Build/Candidate + `ChatGPTClient/RootViewController.swift` only. Canonical package source `e88a50ad9c2098449b43fb0fce2c441a50cd20ac`.
- Initial staging `33894741044` was YAML parse failure with zero jobs/product writes and is invalid evidence. Corrected staging `33895020559/101095508915` passed exact scope, `git diff --check`, Simulator and product commit.
- Push `33895244146/101096229135` and PR `33895249810/101096247432` passed. Canonical Push Artifact `9945483725`, ZIP `sha256:babb23c845c4da971b488b4860c043fe8471adf830688920149df254cee70fd6`; IPA `sha256:5629deedca665b7a5cfa7e36b4996b7b1e4b7a160ca5cb35a465abfbd97fbc69`.
- Package inspection: `com.whitesharkssw.chatgptclient`, `0.1.0 (100)`, Candidate b100, source `e88a50ad9c20`, iOS14+, `[1,2]`, arm64.
- b99 Runtime `sha256:4a0d3925a4abf6ef24dc6743f9efb63a4dffcd049f3e41eb7a547f2b1d33d271`: known-active ~7m32s automatic Detail `5->6` Positive; later no-active-snapshot ~12m54s remote changes required manual Sync `6->8`, so dormant discovery Negative. b99 backlog coalescing Inconclusive in this sample; hard WebContent death Unverified.
- b100 adds exactly one foreground authoritative discovery without an active-snapshot precondition. It may rearm one existing covered observer only for an unfinished newly discovered remote turn. No polling/timer/retry/watchdog/background heartbeat/resend/second authority.

Evidence ladder: **b99 Runtime Partial / b100 Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity verified / Human Runtime pending / Stable-Frozen No.**

**Next exact action:** test canonical b100. Keep a selected completed conversation idle, background app, create a new remote turn elsewhere, then foreground without Sync/Reload. Expect `foregroundConversationDiscovery.requested` + exactly one Detail; complete response should materialize, unfinished remote turn should set `rearmDiscoveredRemoteTurn=true` and rearm once. Regression-check known-active `foregroundExternalDetailReconcile` too.

## b99 Human Runtime — dormant foreground discovery gap / b100 allocation 2026-09-05

Exact tested b99 evidence:

- Candidate `DEV-send-stream-0.1.0-b99` / `0.1.0 (99)`, canonical package source `313c4c3bf2ac0dc729d4793198fe462ada5a14eb`, canonical IPA `sha256:68b7f99eac8fd1d3ab14c6085abd4a084f2b4759dc630f94044017c9a4aecf02`.
- Human Runtime diagnostics `ChatGPTClient-Diagnostics-20260904-161157.json`, `sha256:4a0d3925a4abf6ef24dc6743f9efb63a4dffcd049f3e41eb7a547f2b1d33d271`, 74674 bytes / 149 events / Release / iPhone / iOS17.0.
- First external response was acquired at `15:50:36Z`; app backgrounded at `15:50:38Z` and returned at `15:58:10Z` after 452s (~7m32s). Because an active external live snapshot still existed, b97-style foreground authoritative reconciliation ran automatically; Detail changed visible messages `5 -> 6`, emitted `liveResponse.externalDetailReconciled(reason=authoritative_assistant_materialized)`, cleared the live response and released the covered executor. This path is Runtime Positive.
- App backgrounded again at `15:58:25Z`, now with **no active live response and no covered executor**, and returned at `16:11:19Z` after 774s (~12m54s). No `foregroundExternalDetailReconcile` and no covered rebootstrap occurred because current `applicationWillEnterForeground` requires a pre-existing active external snapshot.
- Manual `同步最新消息` at `16:11:43Z` immediately found authoritative server change: visible messages `6 -> 8` (`addedVisibleMessageCount=2`). This proves the server state advanced while the client had no active receive owner, and the existing authoritative Detail request is sufficient to discover it once invoked.
- This sample contains zero `coveredExecutor.webProcess` / `externalWebProcessRecovery` events. b98 hard WebContent termination recovery remains Unexercised / Unverified.
- This sample contains only one `liveResponse.event` and one `liveResponse.presentationApplied`; therefore the b99 backlog-coalescing performance fix is not meaningfully exercised by this run. No freeze/crash was observed, but coalescing is not accepted from this sample.

Runtime classification:

- known-active external foreground final convergence: **Runtime Positive**, including ~7m32s background;
- b99 live-presentation backlog coalescing: **Unexercised / Inconclusive** in this sample;
- remote changes that begin/occur while the selected conversation has no active external snapshot/executor: **Runtime Negative for automatic foreground discovery**; manual one-shot Detail recovery Positive;
- b98 hard WebContent termination recovery: **Unexercised / Unverified**;
- overall b99: **Runtime Partial / Stable-Frozen No**.

Exact source explanation:

- `RootViewController.applicationWillEnterForeground` currently starts with `guard let conversationID = repository.selectedConversationID, let snapshot = repository.liveResponse(for: conversationID), snapshot.phase.isActive, snapshot.promptText.isEmpty else { return }`.
- Therefore a completed/released external response leaves no foreground discovery trigger for later cross-platform server changes.
- `ConversationDetailViewController` manual Sync already proves the normal authoritative `ConversationRepository.syncLatestMessages` request can recover those changes, and its existing Root callback can rearm covered observation when needed.

b100 allocation / batch recovery point:

- Work `DEV-send-stream` remains selected; branch `dev/send-stream-20260829`; PR #29 open/unmerged/mergeable.
- Verified pre-allocation branch head `6d8d99166d4e36c1b27ca84c842df3be84de21a1`; `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.
- Product files remain exact b99 package product relative to `313c4c3...`; intervening branch commits are workflow/docs only.
- Parallel PR #35 / `DEV-official-sync-reload` remains draft/open at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`; its seven changed paths remain research/workflow/checkpoint only, with zero `ChatGPTClient/**` or product Xcode overlap.
- `DEV-send-stream-0.1.0-b100` / `0.1.0 (100)` is the next unique product candidate and is now permanently allocated/reserved.

Evidence-backed b100 product boundary:

1. Keep client-owned active protected Send behavior unchanged: an active local response is not auto-Synced/replayed on foreground.
2. For a selected conversation with no client-owned active response, foreground entry may issue exactly one existing authoritative `ConversationRepository.syncLatestMessages` when no Detail operation is already in flight, even if no external live snapshot currently exists.
3. Preserve the existing b97 path and diagnostics when an external live snapshot already exists.
4. For the new no-snapshot discovery path, compare the authoritative latest-user identity before/after the one-shot Detail. If the server exposes a newly added latest user whose visible tail still ends in `.user`, or authoritative Detail itself recreates an active external live projection, reuse the existing covered observer with one force page reload so an in-progress remote response can continue. If the final assistant is already materialized, Detail alone is sufficient and no observer is required.
5. Do not poll. Do not add a timer, cadence, retry, watchdog, background heartbeat, guessed `/resume`, WebSocket-body authority, duplicate Send, challenge replay, response cache or second response owner.
6. Preserve b99 UIKit coalescing, b98 hard WebContent recovery, b97 authoritative reconcile, TD-029 protected Send ownership and Sync/Reload semantics.

Intended product scope:

- `ChatGPTClient.xcodeproj/project.pbxproj` — Build100 / Candidate b100 only;
- `ChatGPTClient/RootViewController.swift` — foreground one-shot authoritative discovery/rearm only.

Batch state:

- confirmed complete: b99 diagnostics analyzed; exact failure mechanism tied to source; branch/base/PR #29 verified; PR #35 overlap checked; b100 candidate uniqueness checked; this checkpoint written;
- pending: apply exact two-product-file delta; exact-scope + `git diff --check` + Debug iphonesimulator compile; bind formal b100 Push/PR package CI to exact product head; verify canonical Artifact/IPA identity; update durable project docs and PR #29 metadata;
- do not touch PR #35, protected-Send transport/challenge logic, Repository response authority, b99 canonical Artifact, or b98/b99 reserved candidate identities.

**Next exact action:** apply only the two-file b100 foreground-discovery delta above and validate it before packaging.

## b99 live-presentation coalescing — package-ready 2026-09-04

- Candidate `DEV-send-stream-0.1.0-b99` / `0.1.0 (99)`, permanently reserved.
- Exact product `ec05c284010cb0f2de066bd1cfc3968e07730779`; product commit changes only `ChatGPTClient.xcodeproj/project.pbxproj` and `ChatGPTClient/Conversation/ConversationFeature.swift`.
- Exact canonical package source `313c4c3bf2ac0dc729d4793198fe462ada5a14eb`.
- Initial staging workflow run `33890559324` parsed invalidly and created zero jobs/product changes; it is invalid evidence. Corrected guarded staging `33890678564/101081289220` passed baseline guard, exact two-product-file scope, `git diff --check`, and Debug iphonesimulator compile.
- Formal Push `33890809275/101081720750` and PR `33890812345/101081730258` both passed.
- Canonical Push Artifact `9943798885`; Artifact ZIP `sha256:303bad6e93b8dfdc48ecd77559ed42d6a03058e5d6db676dcd24c65c537df8b5`.
- Canonical IPA `ChatGPTClient-0.1.0-b99-dev-send-stream.ipa`, `sha256:68b7f99eac8fd1d3ab14c6085abd4a084f2b4759dc630f94044017c9a4aecf02`.
- Independent package inspection confirms `com.whitesharkssw.chatgptclient`, `0.1.0 (99)`, Candidate b99, source `313c4c3bf2ac`, iOS14+, UIDeviceFamily `[1,2]`, `iphoneos`, Mach-O arm64.

b99 changes only the selected-conversation UIKit consumer: Repository still accepts/logs every live event, while `ConversationDetailViewController.liveResponseDidChange` schedules at most one pending main-queue presentation application and rebuilds from the latest Repository snapshot when that block runs. No timer/cadence, retry, watchdog, polling, Send replay, transport mutation or second response store is added. b98 WebContent recovery and b97 foreground Detail reconcile remain unchanged.

Evidence ladder: **b98 Runtime Partial / stability rejected; b99 Code written / exact scope+Simulator passed / Push+PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen Send No.**

**Next exact action:** use only canonical b99 IPA. Start one client-owned response, background for several minutes while it remains active, then foreground. Many `liveResponse.event` records may arrive, but `liveResponse.presentationApplied` must be materially coalesced and the app must remain responsive through terminal/final completion. Verify no second Send and no response-state loss. A separate real `webViewWebContentProcessDidTerminate` sample is still required before accepting b98 hard-process recovery.

# DEV-send-stream round 7 Runtime addendum

## b107 accepted-SSE EOF convergence — package ready 2026-09-05

Canonical identity / validation:

- Candidate `DEV-send-stream-0.1.0-b107` / `0.1.0 (107)`, permanently reserved.
- Exact product commit `113fa19d7264b953949770d2e44cb500ded2da6b`; canonical package source `4bd3501a3092dfe7aad7ea836ba0cb8e42b0d65f`.
- Guarded staging `33960451799/101291316464` passed Batch A Runtime/allocation recording, exact two-product-path scope validation, `git diff --check`, Debug Simulator compile and exact product commit.
- Formal Push `33960627676/101291785599` and PR `33960629168/101291789461` both passed on exact package source `4bd3501a3092dfe7aad7ea836ba0cb8e42b0d65f`.
- Canonical Push Artifact `9967821935`; GitHub digest and independent ZIP SHA-256 both `d2036ed0372b16c7690c9d3b324d680db6a522fd5ace26d27afa8733a95a9585`.
- Canonical IPA `ChatGPTClient-0.1.0-b107-dev-send-stream.ipa`; independent SHA-256 `7195d89cb9837efc3386c5dd7e030e7f11f10233689416e59c86d1ae4cf055cd`, matching sidecar. Package inspection verifies `com.whitesharkssw.chatgptclient`, `0.1.0 (107)`, Candidate b107, source marker `4bd3501a3092`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, iPhoneOS, Mach-O arm64.

Behavior / Runtime gate:

- b106 SSE `conversation_id` New Chat handoff remains unchanged and Runtime Positive.
- For an already HTTP200-SSE-accepted client Send, exact `stream_ended_without_done` no longer mutates the same Repository generation to failed. Covered executor emits `.acceptedClientStreamEndedWithoutTerminal`; Root releases only the ended executor transport and reuses the already Runtime-positive accepted-client recovery primitive to attach one fresh covered observer to the **same generation** with `no_resend_same_generation` semantics.
- Successful manual Sync additionally calls the existing `clearLiveResponseAfterAuthoritativeReconcile` primitive when a client-owned live snapshot is already non-active, preventing authoritative rows plus a stale failed/terminal live tail after server state has advanced.
- b107 adds no retry loop, timer/watchdog, polling, duplicate Send, regenerate, challenge replay, guessed Native resume/status, new response authority, completion heuristic or color workaround.
- The b106 assistant blue-text defect remains separately open. b107 intentionally does not modify `ConversationMessageCell` because the b106 reset was Runtime-insufficient and the exact owner is still unproven.
- Human Runtime remains Pending; Stable/Frozen remains No.

**Next exact action:** install only canonical b107 and reproduce one New Chat first Send. If exact accepted `stream_ended_without_done` occurs, require no `phase=failed`/`回答失败`, no second protected Send, same-generation covered recovery and eventual authoritative convergence. After any manual Sync, authoritative content must not be followed by a stale prompt/reasoning/failure tail. Blue-text behavior is observed but not a b107 pass/fail claim except as an unchanged known defect.


## b98 Human Runtime — foreground backlog freeze/crash 2026-09-04

Exact tested identity:

- Candidate `DEV-send-stream-0.1.0-b98` / `0.1.0 (98)`, permanently reserved;
- product `2edd55febe2005071722ddcb9989151b427165d8`;
- canonical package source `17c65a390f2724a55cd29d466e01eaab988dcbfe`;
- canonical Artifact `9942092070`;
- canonical IPA `sha256:b1dc76dbe28e77ceac3468e8cfd3ca0ded41601bd02db6b228bd391a1d697b67`;
- Human Runtime diagnostics `ChatGPTClient-Diagnostics-20260904-152557.json`, `sha256:e0a0bd2c42168d0c3f8a6dd681bbad1bb571d4061b0f2958131cae5f8e059105`, 269552 bytes / 548 events / Candidate b98 / source `17c65a390f27` / Release / iPhone / iOS17.0.

Observed Runtime facts:

1. The b98 hard WebContent-death branch was **not exercised**: the entire diagnostic contains zero `coveredExecutor.webProcess` events and therefore no `coveredExecutor.externalWebProcessRecovery` event. This sample cannot accept or reject that exact hard-termination recovery behavior.
2. The b97 foreground authoritative Detail reconcile carried inside b98 is **Runtime Positive** for the external/cross-platform response. After the app spent roughly 7m51s in background, foreground return automatically issued one authoritative Detail request; visible messages advanced `1 -> 2`, `liveResponse.externalDetailReconciled(reason=authoritative_assistant_materialized)` cleared the external live projection, and the executor was released without manual Sync/Reload.
3. A later client-owned protected Send was accepted once through the covered official Web path (`submitResult=submitted`, `sendResponse` HTTP200 `text/event-stream`) and was still active when the app backgrounded at `15:20:35Z`.
4. After roughly 5m04s background, foreground at `15:25:39Z` delivered a large buffered same-response event backlog. From `15:25:39Z` through `15:25:49Z`, 170 Repository `liveResponse.event` callbacks and 169 `liveResponse.presentationApplied` callbacks were recorded. The peak second was 39 live events plus 39 full live-presentation applications. The burst included 119 `final_delta`, 24 `reasoning_delta`, 18 tool transitions, and the final text reached 4750 characters.
5. Current source explains the UI pressure: every accepted Repository event calls `responseRuntime.onChange`, Root immediately calls `ConversationDetailViewController.liveResponseDidChange`, and that method synchronously rebuilds the full live projection/metrics, `tableView.reloadData()`, and `tableView.layoutIfNeeded()` for every event.
6. The user observed the app freeze and crash. The last pre-crash live event is at `15:25:49Z`; a fresh `launch.start` appears at `15:25:52Z`, followed by Candidate b98 ready at `15:25:55Z`. There is no graceful lifecycle shutdown record between them. This proves an abnormal process exit/relaunch in the tested window, but the exact OS termination class (watchdog, memory pressure, uncaught exception, other) remains **Unverified** without an iOS crash report.

Runtime classification:

- b98 hard WebContent termination recovery: **Unexercised / Unverified** in this sample;
- b97-style foreground authoritative final convergence inside b98: **Runtime Positive**;
- client-owned covered-Web response buffering/survival across ~5m background: **Runtime Positive transport signal**;
- foreground backlog presentation stability: **Runtime Negative — freeze/crash**;
- overall b98: **Runtime Partial / stability rejected; Stable-Frozen No**.

## b99 live-presentation main-queue coalescing — allocation / batch recovery point 2026-09-04

Exact resume guard before product writes:

- Work `DEV-send-stream`;
- branch `dev/send-stream-20260829`;
- PR #29 open / unmerged / mergeable;
- verified branch head before this checkpoint write `97bb33032a44edab4fbe65e2c4c7be75a1eac175`;
- `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`;
- parallel PR #35 / `DEV-official-sync-reload` remains draft/open at `5ab7af84fab78bd1ffa5e13342fb2af9d4395142`; its seven changed paths are research/workflow/checkpoint only, with zero `ChatGPTClient/**` or product-Xcode overlap;
- b98 identity above remains permanently reserved and must not be reused;
- `DEV-send-stream-0.1.0-b99` / Build99 is the next unique product candidate and is allocated by this checkpoint.

Evidence-backed minimum product delta:

1. Keep every live response event flowing into the sole `ConversationRepository` owner exactly as today. Do not coalesce, drop, synthesize or reorder Repository state transitions.
2. Coalesce only the expensive selected-conversation UIKit presentation consumer in `ConversationDetailViewController` by scheduling at most one `DispatchQueue.main.async` live-presentation application for the current main-queue drain. Multiple live-state changes before that block executes collapse into one rebuild using the latest Repository snapshot.
3. The scheduled block must re-check displayed/selected conversation identity. If the live projection disappeared and authoritative Detail replaced it, preserve the existing `apply(detail)` path.
4. Normal sparse foreground streaming still presents on the next main turn. No timer, delay interval, retry, watchdog, polling, response cache or second response authority is introduced.
5. b98 WebContent termination logic, b97 foreground Detail reconcile, TD-029 protected Send ownership, one-Send invariant, Sync/Reload behavior and all transport parsing remain unchanged.

Intended product scope:

- `ChatGPTClient.xcodeproj/project.pbxproj` — Build99 / Candidate b99 only;
- `ChatGPTClient/Conversation/ConversationFeature.swift` — UI-only main-queue live-presentation coalescing only.

Batch recovery state:

- confirmed complete: b98 diagnostics analyzed; branch/base/PR #29 verified; PR #35 conflict check verified; b99 candidate uniqueness checked; this checkpoint written;
- pending: historical pre-package note; superseded by the b99 package-ready section at the top of this checkpoint.
- do not touch PR #35, official research package identities, b98 canonical package, protected-Send transport rules, or Repository response authority during recovery.

**Next exact action:** use the package-ready b99 Human Runtime gate at the top of this checkpoint.
