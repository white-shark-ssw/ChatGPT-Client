# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap/routing/checkpoint rules remain authoritative. |
| Native application shell | **Stable multi-conversation read-state baseline** | `AppDelegate.swift`, `RootViewController.swift`; merged b21 | Compact startup/list-detail navigation and b21 title lifecycle accepted for recorded scope. Not Frozen. |
| Build/runtime metadata | Stable capability + **current b33 identity-valid Candidate** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | Exact b33 package independently verifies `0.1.0 (33)`, Candidate b33, source `0ba15ec48fe8`, iOS14 minimum and arm64. Runtime pending; not Stable/Frozen. |
| Diagnostics / logging | Stable baseline + active answer-navigation diagnostics | `Diagnostics.swift` + call sites | b33 adds privacy-safe `nativeLandingErrorPoints` / `landingCorrectionApplied`; no body/secret logging. Not Frozen. |
| IPA build / CI packaging | Stable capability + **b33 identity-safe Runtime Artifact** | `scripts/build_ipa.sh`, workflow | Push Run `33195740528`, Artifact `9695669835`, IPA SHA `54c598e827bdfa2f1ae5a631d518f7914959e8e31aba1c687a4f0ceb24978855`; package identity independently verified. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + cache-safe provisional presentation integration** | `AuthSessionStore.swift`; b6 + merged consumers | Sole auth/account owner and unchanged by this Work. Supported account-switch/non-personal workspace boundaries remain Unverified. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested read scope** | b7 + b9-b23 Runtime | Current list/detail read path accepted for recorded Plus/personal iPhone/iOS17 scope. Metadata Work adds no new request path. Not Frozen. |
| Native conversation read path | **Stable merged multi-conversation read + merged b23 cache-core baseline** | `ConversationRepository`; b21 + b23 | Sole authority. b26 authoritative-total bound and b29 refresh-presentation correction remain unchanged through b33. Not Frozen. |
| Manual conversation recovery | **Stable / merged baseline** | `ConversationRepository` + detail UI | Sync/Reload semantics unchanged; round projection/anchors re-derive after authoritative replacement. Not Frozen. |
| Multi-conversation state ownership | **Stable / merged for tested read-state scope** | b21; PR #23 | Resident/coalescing/historical-scroll/title/replacement scope accepted. Conditional account/workspace/failure paths remain Unverified. Not Frozen. |
| Conversation-list persistent cache | **Stable merged b23 + active accepted reconcile/presentation corrections** | `ConversationRepository` + `ConversationListCacheStore` | b23 cache core Stable; b26 accepted `30 -> 29` bound; b29 accepted right-top refresh blank-region fix. b33 does not change list data/network/cache ownership. |
| Conversation entry / reading position | **Stable historical-anchor baseline + active first-entry-latest correction** | `ConversationDetailViewController`; b18 + Active Work | Historical A/B anchors accepted. First no-anchor entry must show latest/bottom. Retain as regression gate in b33. |
| Conversation message self-sizing presentation | **Active but b30 correction retained** | `ConversationDetailViewController` + `ConversationMessageCell` | b29 `estimatedRowHeight=0` route rejected; automatic self-sizing restored in b30 and retained through b33. |
| Conversation metadata / Preferences / round navigation | **Active — b32 Runtime partial/failing; exact b33 CI/Artifact ready; Runtime pending** | `DEV-conversation-round-count`; `AppPreferences` + `ConversationRoundProjection` + detail/message/sidebar presentation | b32 accepts recipient/tool filtering, compact Copy direction and precise user-round landing; rejects jump smoothness and bottom-rubber-band direction. b33 fixes only physical-boundary direction and conditional >1pt landing re-anchor/diagnostics. Not Stable/Frozen. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Future follow-tail must consume authoritative per-conversation response ownership; current metadata Work does not invent it. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for recorded scopes.
- b15 is merged Stable recovery; b21 merged Stable multi-conversation; b23 merged Stable cache core.
- b24 package identity rejected/permanently reserved.
- b25-b31 are historical partial/failing or superseded candidates; exact identities remain reserved.
- b32 is **Runtime partial/failing**: semantic landing, recipient/tool filtering and compact Copy direction accepted; jump smoothness + physical-bottom rubber-band direction rejected.
- b33 is **Code written + scoped source audit + exact push CI + identity-valid Runtime Artifact + current-main PR merge-view CI**. Runtime pending. Stable/Frozen No.

Still unverified as applicable: b33 bottom-rubber-band direction, long-jump smoothness/landing correction behavior, first-entry latest regression, iPad, iOS below 17, non-personal workspace, supported real account switch, provisional-row Detail-block path and corrupt/schema rejection.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.