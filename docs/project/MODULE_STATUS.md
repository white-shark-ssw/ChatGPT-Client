# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap/routing/checkpoint rules remain authoritative. |
| Native application shell | **Stable multi-conversation read-state baseline** | `AppDelegate.swift`, `RootViewController.swift`; merged b21 | Compact startup/list-detail navigation and b21 title lifecycle accepted for recorded scope. Not Frozen. |
| Build/runtime metadata | Stable capability + **b34 identity-valid Runtime Candidate** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | Exact b34 package independently verifies `0.1.0 (34)`, Candidate b34, source `bf66c7080347`, iOS14 minimum and arm64. Runtime pending; b24-b34 identities remain reserved. |
| Diagnostics / logging | Stable baseline + active b34 answer-navigation diagnostics | `Diagnostics.swift` + call sites | b33 `nativeLandingErrorPoints` / `landingCorrectionApplied` exposed correction behavior; b34 adds privacy-safe `answerJump.completionIgnored` for stale current-target-not-visible callbacks. No body/secret logging. Not Frozen. |
| IPA build / CI packaging | Stable capability + **b34 identity-safe Runtime Artifact** | `scripts/build_ipa.sh`, workflow | Exact push Run `33200768537`, Job `98949366655`, Artifact `9697664416`, ZIP `sha256:0b05a435...`, IPA SHA `1705a2a39941ab6aee88e13b53d68d55b2fd9ff3d43d1c50d9cdcb6613c2b9b6`; identity independently verified. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + cache-safe provisional presentation integration** | `AuthSessionStore.swift`; b6 + merged consumers | Sole auth/account owner and unchanged by this Work. Supported account-switch/non-personal workspace boundaries remain Unverified. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested read scope** | b7 + b9-b23 Runtime | Current list/detail read path accepted for recorded Plus/personal iPhone/iOS17 scope. Metadata Work adds no new request path. Not Frozen. |
| Native conversation read path | **Stable merged multi-conversation read + merged b23 cache-core baseline** | `ConversationRepository`; b21 + b23 | Sole authority. b26 authoritative-total bound and b29 refresh-presentation correction remain unchanged through b34. Not Frozen. |
| Manual conversation recovery | **Stable / merged baseline** | `ConversationRepository` + detail UI | Sync/Reload semantics unchanged; round projection/anchors re-derive after authoritative replacement. Not Frozen. |
| Multi-conversation state ownership | **Stable / merged for tested read-state scope** | b21; PR #23 | Resident/coalescing/historical-scroll/title/replacement scope accepted. Conditional account/workspace/failure paths remain Unverified. Not Frozen. |
| Conversation-list persistent cache | **Stable merged b23 + active accepted reconcile/presentation corrections** | `ConversationRepository` + `ConversationListCacheStore` | b23 cache core Stable; b26 accepted `30 -> 29` bound; b29 accepted right-top refresh blank-region fix. b34 does not change list data/network/cache ownership. |
| Conversation entry / reading position | **Stable historical-anchor baseline + active first-entry-latest correction** | `ConversationDetailViewController`; b18 + Active Work | Historical A/B anchors accepted. First no-anchor entry must show latest/bottom. Retain as b34 regression gate. |
| Conversation message self-sizing presentation | **Active correction retained** | `ConversationDetailViewController` + `ConversationMessageCell` | b29 `estimatedRowHeight=0` route rejected; automatic self-sizing restored in b30 and retained through b34. |
| Conversation metadata / Preferences / round navigation | **Active — b33 Runtime partial/failing; exact b34 CI/Artifact ready; Runtime pending** | `DEV-conversation-round-count`; `AppPreferences` + `ConversationRoundProjection` + detail/message/sidebar presentation | b33 accepts physical-bottom direction and final user-round landing but rejects long-distance smoothness. b34 prevents stale completion correction/reset while the newer current target is not visible; exact product source `bf66c708...`; Artifact `9697664416`. Not Stable/Frozen. |
| Conversation message rich rendering | **Planned / not implemented** | Future `DEV-message-rendering` | Current cell uses plain `UILabel.text`. Supplied recording confirms raw Markdown/table syntax and raw `filecite`-adjacent boxed glyphs. Formatting/rich annotation belongs Phase 11, not current metadata Work. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Future follow-tail must consume authoritative per-conversation response ownership; current metadata Work does not invent it. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for recorded scopes.
- b15 merged Stable recovery; b21 merged Stable multi-conversation; b23 merged Stable cache core.
- b24 package identity rejected/permanently reserved.
- b25-b32 are historical partial/failing or superseded candidates; exact identities remain reserved.
- b33 is **Runtime partial/failing**: bottom rubber-band direction and final semantic landing accepted; long-distance smoothness rejected. Diagnostics prove visible end corrections and extreme correction candidates during rapid retargeting.
- b34 is **Code written + exact source audit + exact push CI + identity-valid Runtime Artifact + current-main PR merge-view CI**. Runtime pending. Stable/Frozen No.

Still unverified as applicable: b34 smoothness/ignored-completion Runtime behavior, first-entry-latest regression under b34, iPad, iOS below 17, non-personal workspace, supported real account switch, provisional-row Detail-block path and corrupt/schema rejection.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.
