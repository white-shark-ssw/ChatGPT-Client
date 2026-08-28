# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap/routing/checkpoint rules remain authoritative. |
| Native application shell | **Stable multi-conversation read-state baseline** | `AppDelegate.swift`, `RootViewController.swift`; merged b21 | Compact startup/list-detail navigation and b21 title lifecycle accepted for recorded scope. Not Frozen. |
| Build/runtime metadata | Stable capability + **b36 identity-valid Runtime Candidate** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | Exact b36 package independently verifies `0.1.0 (36)`, Candidate b36, source `8f8614508eef`, iOS14 minimum and arm64. Runtime pending; b24-b36 identities remain reserved. |
| Diagnostics / logging | Stable baseline + active b36 answer-navigation timing diagnostics | `Diagnostics.swift` + call sites | b36 adds privacy-safe `answerJump.positioned` direct-position/preparation duration + target visibility/row. Existing request/completed diagnostics remain. No body/secret logging. Not Frozen. |
| IPA build / CI packaging | Stable capability + **b36 identity-safe Runtime Artifact** | `scripts/build_ipa.sh`, workflow | Exact push Run `33207505424`, Job `98972194770`, Artifact `9700254733`, ZIP `sha256:718e8500ea41bcc73b41f5bebd9a4850b93246368a87304be0b2c4751702e576`, IPA SHA `cdf2c7278ec0a4f6f5125a711f78d7bbda8c606a32dda87f614d710f662bd867`; identity independently verified. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + cache-safe provisional presentation integration** | `AuthSessionStore.swift`; b6 + merged consumers | Sole auth/account owner and unchanged by this Work. Supported account-switch/non-personal workspace boundaries remain Unverified. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested read scope** | b7 + b9-b23 Runtime | Current list/detail read path accepted for recorded Plus/personal iPhone/iOS17 scope. Metadata Work adds no new request path. Not Frozen. |
| Native conversation read path | **Stable merged multi-conversation read + merged b23 cache-core baseline** | `ConversationRepository`; b21 + b23 | Sole authority. b26 authoritative-total bound and b29 refresh-presentation correction remain unchanged through b36. Not Frozen. |
| Manual conversation recovery | **Stable / merged baseline** | `ConversationRepository` + detail UI | Sync/Reload semantics unchanged; round projection/anchors re-derive after authoritative replacement. Not Frozen. |
| Multi-conversation state ownership | **Stable / merged for tested read-state scope** | b21; PR #23 | Resident/coalescing/historical-scroll/title/replacement scope accepted. Conditional account/workspace/failure paths remain Unverified. Not Frozen. |
| Conversation-list persistent cache | **Stable merged b23 + active accepted reconcile/presentation corrections** | `ConversationRepository` + `ConversationListCacheStore` | b23 cache core Stable; b26 accepted `30 -> 29` bound; b29 accepted right-top refresh blank-region fix. b36 does not change list data/network/cache ownership. |
| Conversation entry / reading position | **Stable historical-anchor baseline + active first-entry-latest correction** | `ConversationDetailViewController`; b18 + Active Work | Historical A/B anchors accepted. First no-anchor entry must show latest/bottom. Retain as b36 regression gate. |
| Conversation message self-sizing presentation | **Active correction retained** | `ConversationDetailViewController` + `ConversationMessageCell` | b29 `estimatedRowHeight=0` route rejected; automatic self-sizing restored in b30 and retained through b36. b36 removes only explicit jump-path root/table forced layouts, not self-sizing. |
| Conversation metadata / Preferences / round navigation | **Active — b35 Runtime partial/failing; exact b36 CI/Artifact/merge-view ready; Runtime pending** | `DEV-conversation-round-count`; `AppPreferences` + `ConversationRoundProjection` + detail/message/sidebar presentation | b35 unified short/long direct+ease-out but exposed multi-second jump preparation stalls. b36 removes explicit forced jump layouts, reuses existing round button for `定位中` feedback, and times direct positioning. Exact product source `8f861450...`; Artifact `9700254733`. Not Stable/Frozen. |
| Conversation message rich rendering | **Planned / not implemented** | Future `DEV-message-rendering` | Current cell uses plain `UILabel.text`. Supplied recording confirms raw Markdown/table syntax and raw `filecite`-adjacent boxed glyphs. Formatting/rich annotation belongs future rendering work, not current metadata Work. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Future follow-tail must consume authoritative per-conversation response ownership; current metadata Work does not invent it. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for recorded scopes.
- b15 merged Stable recovery; b21 merged Stable multi-conversation; b23 merged Stable cache core.
- b24 package identity rejected/permanently reserved.
- b25-b34 are historical partial/failing or superseded candidates; exact identities remain reserved.
- b35 is **Runtime partial/failing**: direct+ease-out completed landings remain precise, but several-second tap-to-position stalls were observed around long-message regions.
- b36 is **Code written + exact source audit + exact push CI + identity-valid Runtime Artifact + current-main PR merge-view CI**. Runtime pending. Stable/Frozen No.

Still unverified as applicable: b36 tap-to-position latency/feedback Runtime behavior, first-entry-latest regression under b36, iPad, iOS below 17, non-personal workspace, supported real account switch, provisional-row Detail-block path and corrupt/schema rejection.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.
