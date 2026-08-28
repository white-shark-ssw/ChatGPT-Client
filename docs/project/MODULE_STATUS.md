# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable multi-conversation read-state baseline** | `AppDelegate.swift`, `RootViewController.swift`; b14/b15 + merged b21 | Compact startup/list-detail navigation and b21 title lifecycle are real-device accepted for recorded scope. Not Frozen. |
| Build/runtime metadata | Stable capability + **current b28 identity-valid Candidate** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | b28 independently verifies `0.1.0 (28)`, Candidate `DEV-conversation-round-count-0.1.0-b28`, source `eacd3e68469e`, iOS14 minimum and arm64. Runtime pending; not Stable/Frozen. |
| Diagnostics / logging | Stable baseline + b27 Runtime root-cause evidence + b28 scoped interaction diagnostics | `Diagnostics.swift` + call sites | b27 proved sequential semantic targets despite hitch and proved refresh top inset itself grew ~34pt after right-button refresh. b28 logs refresh source and answer target/offset/landing error only; no secret/body data and no second diagnostics authority. Not Frozen. |
| IPA build / CI packaging | Stable capability + **b28 identity-safe Runtime Artifact** | `scripts/build_ipa.sh`, workflow | Exact push Run `33149698659` / Job `98778576898`, Artifact `9677214430`, IPA `ChatGPTClient-0.1.0-b28-dev-conversation-round-count.ipa`, SHA `9ab99321e08695a8298fd3e40231110303d47bd6bbb75d4e9814dc4e275d962f`; independent ZIP/Info.plist/executable inspection matched intended identity. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + cache-safe provisional presentation integration** | `AuthSessionStore.swift`; b6 + merged b21/b23 consumers | Sole auth/account owner and unchanged by this Work. Supported account-switch and non-personal workspace boundaries remain Unverified. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested read scope** | b7 + b9-b23 runtime | Current list/detail read path accepted for recorded Plus/personal iPhone/iOS17 scope. Metadata Work adds no new request path. Not Frozen. |
| Native conversation read path | **Stable merged multi-conversation read + merged b23 cache-core baseline** | `ConversationRepository`; b21 + b23 | `ConversationRepository` remains sole authority. b26's real-device accepted authoritative-total bound for `28/29 -> 29` is unchanged in b28. Not Frozen. |
| Manual conversation recovery | **Stable / merged baseline** | `ConversationRepository` + detail UI | Existing Sync/Reload semantics unchanged; answer anchors re-derive after authoritative replacement. b28 needs regression sanity only. Not Frozen. |
| Multi-conversation state ownership | **Stable / merged for tested Plus/personal iPhone/iOS17 read-state scope** | `DEV-multi-conversation-state-0.1.0-b21`; PR #23 | Recorded resident/coalescing/historical-scroll/title/replacement scope accepted. Conditional account/workspace/failure paths remain Unverified. Not Frozen. |
| Conversation-list persistent cache | **Stable merged b23 + b26 bounded-reconcile correction Runtime accepted within Active Work** | `ConversationRepository` + storage-only `ConversationListCacheStore` | b23 accepted cache core; b26 accepted cold `30 -> 29` and repeated `29/29`. b27/b28 do not change reconcile/network logic. Full Phase 8 still Active. |
| Conversation metadata / Preferences / answer navigation | **Active — b27 Runtime partial/failing; b28 Code + source audit + exact CI/Artifact + initial merge-view CI; Runtime pending** | `DEV-conversation-round-count`; detail/message/sidebar presentation + `AppPreferences` + `ConversationRoundProjection` | b27 retained sequential answer targets but still hitched; right-top refresh inflated `adjustedInsetTop` ~97.67→131.67; Copy visual too large. b28 uses interruptible native offset retargeting, separates right-button vs native pull refresh and removes refresh attributed-title/top-normalization workaround, and shrinks Copy to 14pt/28×28. Runtime unverified. `工作` remains deferred pending authoritative type source. Not Stable/Frozen. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Future follow-tail must consume authoritative per-conversation response ownership; current read/metadata work does not invent it. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for recorded scopes.
- b15 is merged Stable recovery baseline; b21 is merged Stable multi-conversation baseline; b23 is merged Stable cache-core baseline.
- b24 conversation-round-count: package identity rejected/permanently reserved.
- b25: identity-valid partial/failing Runtime; accepted Copy/time/preferences, rejected header/jump/refresh and exposed `30/29` reconcile.
- reused-b25 source-fix output is identity-invalid for testing.
- b26: identity-valid partial/failing Runtime; accepted bounded `29/29`, sequential answer targets and compact header; smoothness/presentation still failed.
- b27: identity-valid **partial/failing Runtime**; sequential targets remained correct, but long-conversation jump hitch persisted; right-top refresh inflated adjusted top inset by ~34pt while list data stayed correct; Copy visual rejected. Superseded.
- b28: **Code + scoped source/static audit + exact push CI + identity-valid Runtime Artifact + initial PR merge-view CI; Runtime pending**. Stable/Frozen No.

Still unverified as applicable: b28 jump smoothness under rapid retarget/manual drag, right-button refresh inset regression, native pull-refresh collapse, smaller Copy appearance in Light/Dark, runtime below iOS17, iPad, non-personal workspace, supported real account switch, provisional-row Detail-block path and corrupt/schema rejection. These are evidence boundaries, not accepted results.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, candidate evidence, accepted Runtime behavior or stability changes.
