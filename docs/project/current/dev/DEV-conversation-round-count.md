# DEV-conversation-round-count

## Status

**Active — exact b36 Runtime partial/failing; b37 reserved for deterministic message geometry + long-message presentation virtualization**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Phase 8 conversation metadata/settings bundle with compact header, round count, timestamps, Copy, adaptive round navigation, persisted Preferences, first-entry latest placement and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open/mergeable, not merged.
- **Branch head before this Runtime checkpoint write**: `4d7041834cdd9be5ec0c28c1a39771acc89b6020`.
- **Exact b36 product/config source**: `8f8614508eef5197f9fff4bb9d10c14354d5821e`.
- **Current main**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- Only this development checkpoint is Active. No parallel Work/candidate conflict exists in `docs/project/current/dev/`.

## Accepted scope that must remain unchanged

- Physical-bottom/rubber-band adaptive direction.
- Each visible authoritative user message starts one round and remains the semantic quick-navigation target.
- Sequential round targeting derives from one `ConversationRoundProjection` plus transient presentation cursor only.
- Recipient/tool/internal filtering, compact assistant Copy, timestamps/preferences/header, first-entry latest, A/B anchors, list/cache reconciliation, Sync/Reload and existing state owners remain.
- `ConversationRepository` remains sole conversation/list/read authority; any b37 display segmentation/geometry is presentation-only and derived from authoritative `messages`.
- Rich Markdown/citation rendering remains future `DEV-message-rendering`; b37 may optimize plain-text presentation only and must not reinterpret message content.

## Candidate progression

- b24 identity rejected/reserved; b25-b30 Runtime partial/failing.
- b31 accepted precise user-message semantic landing but retained hitch/internal-row/Copy defects.
- b32 accepted recipient filtering, compact Copy direction and semantic landing; smoothness + bottom direction still failed.
- b33 accepted physical-bottom direction and final precision; long-distance/rapid smoothness failed.
- b34 removed stale completion correction; exact Runtime still rejected movement feel with 42 requested / 42 completed and 0 corrections/ignored completions.
- b35 unified short/long navigation to direct target position + about 120pt / 0.22s ease-out; Runtime exposed multi-second synchronous positioning stalls.
- b36 removed explicit root/table forced layouts, added `定位中` feedback and direct-position timing. Exact Runtime proves the blocking work remains inside table/message geometry itself; ordinary scrollbar dragging is also severely affected.

## Exact b36 identity / CI / Artifact

- Candidate `DEV-conversation-round-count-0.1.0-b36`, version/build `0.1.0 (36)`.
- Exact product/config source `8f8614508eef5197f9fff4bb9d10c14354d5821e`.
- Exact push Run / Job `33207505424` / `98972194770` — success.
- Runtime Artifact `9700254733`; ZIP `sha256:718e8500ea41bcc73b41f5bebd9a4850b93246368a87304be0b2c4751702e576`.
- IPA `ChatGPTClient-0.1.0-b36-dev-conversation-round-count.ipa`; SHA `cdf2c7278ec0a4f6f5125a711f78d7bbda8c606a32dda87f614d710f662bd867`.
- Independent package verification: `0.1.0 (36)`, Candidate b36, source `8f8614508eef`, iOS14 minimum, arm64.
- Current-main merge-view Run / Job `33207508869` / `98972206567` succeeded on synthetic merge `e7ff5b368faaea3debbe5d5547c0424996653fa0` against unchanged `main@a6e3b2bc...`. Merge-view is CI evidence only.

## Exact b36 Runtime result — 2026-08-29

User-tested the exact b36 iPhone/iOS17 Candidate and supplied `ChatGPTClient-Diagnostics-20260828-203253.json`; metadata identifies build 36, Candidate `DEV-conversation-round-count-0.1.0-b36`, source `8f8614508eef`, iOS17.0.

User feedback:

- Severe stutter remains during round navigation.
- Dragging the right-side scroll indicator/scrollbar is also severely stuttery.
- Current direct-position presentation therefore provides no meaningful experience advantage over normal long-distance scrolling and can feel worse.

Trace facts from the supplied exact b36 file:

- 47 `answerJump.positioned` events.
- Direct-position duration: median `187.18ms`, P90 about `780.39ms`, P95 about `957.94ms`, max `3952.37ms`.
- 33/47 exceed `100ms`; 18/47 exceed `250ms`; 10/47 exceed `500ms`; 2/47 exceed `1000ms`.
- Representative slow targets: row 43 `3952.37ms`, row 49 `1551.88ms`, row 15 `962.40ms` and again `947.53ms`, row 86 `837.88ms`.
- Revisited geometry can become almost free: row 157 goes from `165.45/142.96ms` to `0.37/0.28ms`; row 5 goes from `51.35ms` to `0.34ms`; row 10 from `49.30ms` to `0.34ms` on a later visit.
- Some targets remain repeatedly expensive (row 15 near `950ms` twice), so an offscreen row-height cache alone is not sufficient evidence-backed treatment; large visible message text layout also repeats.
- First no-anchor latest presentation logged row 160 at `contentOffsetY=13823.33`. Later interaction reached `currentOffsetY=154611.67` in the same 161-visible-message conversation. Since the source uses `rowHeight = automaticDimension` and `estimatedRowHeight = automaticDimension`, this >11x geometry expansion while rows become realized is direct evidence that initial estimated table geometry is far from the eventual realized long-message geometry.
- The Detail itself is long/tool-heavy (`9,754,540` bytes, `mappingCount=2371`, `filteredRecipientMessageCount=920`, `visibleMessageCount=161`); a second loaded Detail in the same trace is `19,023,941` bytes / `3959` mapping nodes. These payload sizes are protocol evidence only; the current blocking interaction path is the main-thread presentation geometry after authoritative messages are already loaded.

Source facts matching Runtime:

- `UITableView` still uses `rowHeight = UITableView.automaticDimension` and `estimatedRowHeight = UITableView.automaticDimension`.
- Each authoritative visible message is one table row.
- Each row uses one unbounded `UILabel(numberOfLines=0)` containing the entire message text and Auto Layout constraints.
- `scrollToRow(false)` and scrollbar movement therefore cause UIKit to realize/replace estimated row geometry; a very long visible message also requires laying out the whole label even when only a small viewport portion is visible.

Conclusion: b36 is **Runtime partial/failing**, permanently reserved, not Stable/Frozen. The b35/b36 jump-animation hypotheses are no longer the primary blocker. Exact b36 Runtime now justifies replacing deferred full-message self-sizing with deterministic derived presentation geometry and bounded long-message virtualization.

## b37 reserved identity

- **Reserved Candidate**: `DEV-conversation-round-count-0.1.0-b37`
- **Version / Build**: `0.1.0 (37)`
- Exact repository code search returned no existing b37 Candidate match before reservation.
- Only one Active development checkpoint exists; branch/PR/main identities match this Work; b24-b36 remain permanently reserved.
- `BUILD_TEST_INDEX.md` is currently stale at b34 because the prior b36 documentation batch was interrupted; b35/b36 exact evidence is authoritative in this checkpoint and durable Profile/State/Module/Rules/Plan. Before b37 handoff the index must be repaired with b35/b36/b37 identities.

## b37 evidence-backed product direction

The b37 goal is not another animation tweak. It is to make conversation geometry deterministic before the user scrolls.

1. Add a **derived presentation projection** over authoritative `messages`. It owns no message/round/network state.
2. Split very long plain-text messages into bounded presentation chunks (target bound about 1200 Swift `Character`s per chunk, preferring a nearby newline when possible). Concatenated source text remains unchanged; Copy still uses the full authoritative message text. Chunking is visual virtualization only.
3. Preserve message semantics across chunks: timestamp only on the first chunk; assistant Copy only on the last chunk; user context Copy still copies the full authoritative user message; a round target maps to the first presentation row of its authoritative user message.
4. Replace deferred table self-sizing geometry with an exact lightweight row-height calculation using the same fonts/insets as the cell. Build one ephemeral per-detail height array plus prefix row offsets/content height. This is presentation geometry, not a persistent state store.
5. Use those prefix offsets for round targets, historical anchor row positions and latest/bottom placement. Do not call `scrollToRow` to discover geometry during a quick jump.
6. Quick navigation should set the direction-consistent lead offset directly from O(1) derived geometry, then keep the accepted single ~120pt / 0.22s ease-out finish. Short and long distances still use one method.
7. Replace the message cell's Auto Layout/self-sizing hot path with deterministic frame layout shared with the height calculator, so visible bounded chunks do not trigger full-message constraint sizing.
8. Remove b36 `定位中`/`CATransaction.flush` feedback from the normal jump path. Exact b36 shows main-thread geometry can block for seconds; flushing a tiny button does not solve a blocked run loop and the user reports the current experience is worse.
9. Extend `ScrollAnchor` with presentation chunk index so A/B historical reading remains semantic to the same authoritative message while preserving position inside a long virtualized message.
10. Add privacy-safe `messagePresentation.rebuilt` diagnostics: authoritative message count, presentation row count, chunked-message count, chunk limit, geometry-build duration, layout width and derived content height only. No text/body/identity.
11. Do not add retry, timer, watchdog, background prefetch loop, retained cell/ViewController hierarchy cache, second semantic index, network change, Markdown parsing or unrelated refactor.

## Rejected b37 routes

- Merely increasing/decreasing `estimatedRowHeight`: exact b36 proves realized geometry can differ by >11x and large rows remain repeatedly expensive.
- Row-height cache only while retaining one giant UILabel per message: row 15 remains about 950ms on repeated visits, showing visible full-message layout can still dominate.
- Another full-distance/native scroll animation parameter change: scrollbar dragging is also affected, so animation is not the root owner.
- Persisting row heights: width/font/preference-dependent geometry is presentation-only and should be rebuilt, not stored as conversation truth.

## Batch recovery point

- **Batch A — b36 Runtime failure + b37 reservation/architecture**: this checkpoint write.
- **Batch B pending**: implement/audit only the derived presentation projection, bounded message chunks, deterministic geometry/manual message-cell layout, semantic anchor adaptation and O(1) round offset path; allocate product identity b37 atomically with Xcode/workflow.
- **Batch C pending**: exact b37 push CI, Artifact, independent package verification and current-main PR merge-view.
- **Batch D pending**: synchronize `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `BUILD_TEST_INDEX.md`, `PROJECT_SPECIFIC_RULES.md`, `DEVELOPMENT_PLAN.md` to exact b36 Runtime + b37 truth, verify docs-only diff, then hand exact b37 IPA to user.
- **Must not replay/touch**: b24-b36 identities; exact b36 product source; repository/list/cache/network ownership; accepted round/filter/Copy/bottom-direction behavior; rich-rendering scope; any other task checkpoint.
- **Next exact action**: inspect the exact b36 `ConversationFeature.swift` presentation/cell paths, implement the smallest b37 deterministic-geometry/virtualization patch on a tooling-only assembly branch, parse/build-audit it, then create one clean formal b37 product/config commit from this checkpoint parent.

## Validation state

- **b36 Runtime/manual/real-device**: Partial/failing — severe table geometry/text-layout stutter remains and affects both quick navigation and scrollbar dragging.
- **b37 Code written**: No.
- **b37 Static/source audit**: Pending.
- **b37 CI**: Pending.
- **b37 Artifact produced**: Pending.
- **b37 Runtime/manual/real-device**: Pending.
- **Stable/Frozen**: No.

## b37 Runtime focus

1. Drag the right-side scroll indicator rapidly from bottom to top and back; it should remain responsive without multi-second freezes or massive geometry jumps.
2. Repeat long-message previous/next targets including the b36 slow regions; tap-to-motion should be effectively immediate relative to b36.
3. Verify long assistant messages remain complete/readable across chunk boundaries; no duplicated/dropped text.
4. Final quick-navigation landing remains at the first presentation row of the intended authoritative user message.
5. Rapid taps remain one semantic round per tap; real drag retakes ownership immediately.
6. First-entry latest/bottom and A/B historical anchors remain correct inside long virtualized content.
7. Copy/timestamps/preferences/recipient filtering/list reconcile/Sync/Reload regressions remain intact.
8. Export diagnostics if any stall remains; b37 presentation-build and jump geometry timings should isolate residual cell rendering cost.