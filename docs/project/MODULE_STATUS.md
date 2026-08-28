# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable multi-conversation read-state baseline** | `AppDelegate.swift`, `RootViewController.swift`; b14/b15 + merged b21 | Compact startup/list-detail navigation and b21 title lifecycle are real-device accepted for recorded scope. Not Frozen. |
| Build/runtime metadata | Stable capability + **current b30 identity-valid Candidate** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | b30 independently verifies `0.1.0 (30)`, Candidate `DEV-conversation-round-count-0.1.0-b30`, source `a091327508d8`, iOS14 minimum and arm64. Runtime pending; not Stable/Frozen. |
| Diagnostics / logging | Stable baseline + current Runtime evidence | `Diagnostics.swift` + call sites | b28 logs proved large jump-target drift/direction issues; b29 Runtime proved message-body layout regression was presentation-side while Detail data remained present. Privacy-safe diagnostics remain; no body/secret logging. Not Frozen. |
| IPA build / CI packaging | Stable capability + **b30 identity-safe Runtime Artifact** | `scripts/build_ipa.sh`, workflow | Exact push Run `33160005440` / Job `98811893174`, Artifact `9681236213`, IPA `ChatGPTClient-0.1.0-b30-dev-conversation-round-count.ipa`, SHA `91f5ee21e904fbe66932e306b7184dc645f33006e5bb10c33f8b3e3b22639db9`; downloaded package inspection matched intended identity. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + cache-safe provisional presentation integration** | `AuthSessionStore.swift`; b6 + merged b21/b23 consumers | Sole auth/account owner and unchanged by this Work. Supported account-switch and non-personal workspace boundaries remain Unverified. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested read scope** | b7 + b9-b23 runtime | Current list/detail read path accepted for recorded Plus/personal iPhone/iOS17 scope. Metadata Work adds no new request path. Not Frozen. |
| Native conversation read path | **Stable merged multi-conversation read + merged b23 cache-core baseline** | `ConversationRepository`; b21 + b23 | `ConversationRepository` remains sole authority. b26 authoritative-total bound for `28/29 -> 29` remains unchanged through b30. Not Frozen. |
| Manual conversation recovery | **Stable / merged baseline** | `ConversationRepository` + detail UI | Existing Sync/Reload semantics unchanged; answer anchors re-derive after authoritative replacement. Runtime regression sanity remains required before Phase 8 closure. Not Frozen. |
| Multi-conversation state ownership | **Stable / merged for tested Plus/personal iPhone/iOS17 read-state scope** | `DEV-multi-conversation-state-0.1.0-b21`; PR #23 | Recorded resident/coalescing/historical-scroll/title/replacement scope accepted. Conditional account/workspace/failure paths remain Unverified. Not Frozen. |
| Conversation-list persistent cache | **Stable merged b23 + b26 bounded-reconcile correction Runtime accepted within Active Work** | `ConversationRepository` + storage-only `ConversationListCacheStore` | b23 accepted cache core; b26 accepted cold `30 -> 29` and repeated `29/29`. b29 Runtime additionally accepts the right-refresh top-blank presentation correction. b30 does not change list data or refresh code. |
| Conversation entry / reading position | **Stable historical-anchor baseline + first-entry-latest correction still Runtime pending** | `ConversationDetailViewController`; b18 + Active Work | b18 accepts established A/B anchors. Contract requires no-anchor first entry at latest/bottom. b29 body layout was too broken for honest visual acceptance of this path; b30 restores self-sizing estimate before retesting. |
| Conversation message self-sizing presentation | **Active correction — b29 Runtime failed; b30 CI/Artifact ready** | `ConversationDetailViewController` + `ConversationMessageCell` | b29 `estimatedRowHeight=0` caused severe deformed/invisible message rows despite successful Detail parsing. b30 restores `UITableView.automaticDimension` estimation only; Runtime pending. |
| Conversation metadata / Preferences / answer navigation | **Active — b29 Runtime partial/failing; b30 Code + source audit + exact CI/Artifact + PR merge-view CI; Runtime pending** | `DEV-conversation-round-count`; detail/message/sidebar presentation + `AppPreferences` + `ConversationRoundProjection` | b29 accepts list top-blank fix but rejects message layout. b30 restores self-sizing estimate without touching semantic answer authority/list owners. Official Copy reference measures ~14.7pt glyph; current 14pt regular secondary-label glyph is evidence-aligned but visual Runtime acceptance remains pending. `工作` remains deferred pending authoritative type source. Not Stable/Frozen. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Future follow-tail must consume authoritative per-conversation response ownership; current read/metadata work does not invent it. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for recorded scopes.
- b15 is merged Stable recovery baseline; b21 is merged Stable multi-conversation baseline; b23 is merged Stable cache-core baseline.
- b24: package identity rejected/permanently reserved.
- b25: partial/failing Runtime; Copy/time/preferences accepted; header/jump/refresh rejected; `30/29` exposed.
- reused-b25 source-fix output is identity-invalid for testing.
- b26: partial/failing Runtime; bounded `29/29`, sequential answer targets and compact header accepted.
- b27: partial/failing Runtime; long-conversation jump hitch persisted, right-top refresh inflated top inset and Copy visual was rejected.
- b28: partial/failing Runtime; large answer-target drift, direction flips without drag, first-entry top and blank refresh band.
- b29: **partial/failing Runtime**. Right-top list blank band fixed/accepted; message self-sizing/body presentation severely regressed after `estimatedRowHeight=0`. Jump/first-entry visual acceptance remains unresolved because body layout was broken.
- b30: **Code + scoped source/static audit + exact push CI + identity-valid Runtime Artifact + initial PR merge-view CI; Runtime pending**. Stable/Frozen No.

Still unverified as applicable: b30 message-layout restoration, official Copy visual match under normal rows, long-conversation jump accuracy/smoothness/direction, first-entry latest placement, native pull-refresh regression, runtime below iOS17, iPad, non-personal workspace, supported real account switch, provisional-row Detail-block path and corrupt/schema rejection.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, Candidate evidence, accepted Runtime behavior or stability changes.
