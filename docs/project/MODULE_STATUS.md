# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable multi-conversation read-state baseline** | `AppDelegate.swift`, `RootViewController.swift`; b14/b15 + merged b21 | Compact startup/list-detail navigation and b21 title lifecycle are real-device accepted for recorded scope. Not Frozen. |
| Build/runtime metadata | Stable capability + **current b29 identity-valid Candidate** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | b29 independently verifies `0.1.0 (29)`, Candidate `DEV-conversation-round-count-0.1.0-b29`, source `0b0c2fea4450`, iOS14 minimum and arm64. Runtime pending; not Stable/Frozen. |
| Diagnostics / logging | Stable baseline + b28 Runtime root-cause evidence + b29 scoped interaction diagnostics | `Diagnostics.swift` + call sites | b28 logs proved material long-row landing drift, direction flips without drag and first-entry top placement; b29 keeps privacy-safe answer target/offset and default-latest diagnostics only. No secret/body data or second diagnostics authority. Not Frozen. |
| IPA build / CI packaging | Stable capability + **b29 identity-safe Runtime Artifact** | `scripts/build_ipa.sh`, workflow | Exact push Run `33155124626` / Job `98795968389`, Artifact `9679291236`, IPA `ChatGPTClient-0.1.0-b29-dev-conversation-round-count.ipa`, SHA `4378fe9b6a7340ea64a5c82063b0f7e3368e92deaf567d5e0ac40c08055a5360`; downloaded ZIP/Info.plist/executable inspection matched intended identity. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + cache-safe provisional presentation integration** | `AuthSessionStore.swift`; b6 + merged b21/b23 consumers | Sole auth/account owner and unchanged by this Work. Supported account-switch and non-personal workspace boundaries remain Unverified. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested read scope** | b7 + b9-b23 runtime | Current list/detail read path accepted for recorded Plus/personal iPhone/iOS17 scope. Metadata Work adds no new request path. Not Frozen. |
| Native conversation read path | **Stable merged multi-conversation read + merged b23 cache-core baseline** | `ConversationRepository`; b21 + b23 | `ConversationRepository` remains sole authority. b26's real-device accepted authoritative-total bound for `28/29 -> 29` is unchanged in b29. Not Frozen. |
| Manual conversation recovery | **Stable / merged baseline** | `ConversationRepository` + detail UI | Existing Sync/Reload semantics unchanged; answer anchors re-derive after authoritative replacement. b29 needs regression sanity only. Not Frozen. |
| Multi-conversation state ownership | **Stable / merged for tested Plus/personal iPhone/iOS17 read-state scope** | `DEV-multi-conversation-state-0.1.0-b21`; PR #23 | Recorded resident/coalescing/historical-scroll/title/replacement scope accepted. Conditional account/workspace/failure paths remain Unverified. Not Frozen. |
| Conversation-list persistent cache | **Stable merged b23 + b26 bounded-reconcile correction Runtime accepted within Active Work** | `ConversationRepository` + storage-only `ConversationListCacheStore` | b23 accepted cache core; b26 accepted cold `30 -> 29` and repeated `29/29`. b27-b29 do not change reconcile/network logic. Full Phase 8 still Active. |
| Conversation entry / reading position | **Stable historical-anchor baseline + b29 first-entry correction Runtime pending** | `ConversationDetailViewController`; b18 + Active Work | b18 accepts independent established A/B anchors. Product/UI contract requires no-anchor first entry at latest/bottom. b28 Runtime proved current source still opened a 1577-message conversation at top; b29 implements nonanimated latest placement. Exact Runtime pending. |
| Conversation metadata / Preferences / answer navigation | **Active — b28 Runtime partial/failing; b29 Code + source audit + exact CI/Artifact + initial merge-view CI; Runtime pending** | `DEV-conversation-round-count`; detail/message/sidebar presentation + `AppPreferences` + `ConversationRoundProjection` | b28 showed material answer-offset drift, direction flips without drag, first-entry top and persistent refresh blank band. b29 disables fixed row-height estimates for target geometry, retains clicked programmatic direction until real drag/boundary, implements no-anchor latest placement and removes list-refresh use of `navigationItem.prompt`. `工作` remains deferred pending authoritative type source. Not Stable/Frozen. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Future follow-tail must consume authoritative per-conversation response ownership; current read/metadata work does not invent it. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for recorded scopes.
- b15 is merged Stable recovery baseline; b21 is merged Stable multi-conversation baseline; b23 is merged Stable cache-core baseline.
- b24 conversation-round-count: package identity rejected/permanently reserved.
- b25: identity-valid partial/failing Runtime; accepted Copy/time/preferences, rejected header/jump/refresh and exposed `30/29` reconcile.
- reused-b25 source-fix output is identity-invalid for testing.
- b26: identity-valid partial/failing Runtime; accepted bounded `29/29`, sequential answer targets and compact header; smoothness/presentation still failed.
- b27: identity-valid partial/failing Runtime; semantic targets remained sequential but long-conversation jump hitch persisted, right-top refresh inflated adjusted top inset by ~34pt and Copy visual was rejected. Superseded.
- b28: identity-valid **partial/failing Runtime**; 1577-message diagnostics showed large target landing drift, direction flips without real drag, first-entry top placement and continued blank top refresh presentation. Superseded by b29.
- b29: **Code + scoped source/static audit + exact push CI + identity-valid Runtime Artifact + initial PR merge-view CI; Runtime pending**. Stable/Frozen No.

Still unverified as applicable: b29 long-conversation jump accuracy/smoothness after real-layout geometry, direction retention under rapid taps, first-entry latest placement, right-button refresh inset regression, native pull-refresh collapse, runtime below iOS17, iPad, non-personal workspace, supported real account switch, provisional-row Detail-block path and corrupt/schema rejection. These are evidence boundaries, not accepted results.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, candidate evidence, accepted Runtime behavior or stability changes.
