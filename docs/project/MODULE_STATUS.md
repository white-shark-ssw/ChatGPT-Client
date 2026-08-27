# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable multi-conversation read-state baseline** | `AppDelegate.swift`, `RootViewController.swift`; b14/b15 + merged b21 | b14 compact startup/list-detail navigation accepted. b17 core switching/resident return and b18 historical scroll accepted. b21 title lifecycle correction is real-device accepted. PR #23 merged. Not Frozen. |
| Build/runtime metadata | Stable capability + **b23 identity-valid Candidate** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | b23 verifies `0.1.0 (23)`, Candidate/source identity, iOS14 minimum, `[1,2]` and arm64 for the cache-core Runtime Candidate. Not Frozen. |
| Diagnostics / logging | Stable baseline + b23 cache diagnostics Runtime evidence | `Diagnostics.swift` + auth/recovery/residency/scroll/cache call sites | b23 export records privacy-safe provisional-cache, freshness, offline-cache, reconciliation and write evidence without raw titles/IDs/auth secrets. Not Frozen. |
| IPA build / CI packaging | Stable capability + **b23 identity-valid Artifact** | `scripts/build_ipa.sh`, workflow | Exact b23 Run `33101116431` / Job `98618762016`, Artifact `9658508764`; IPA SHA `8f6911616fff1e93885191fcaec0f31a1e3c9488b7f4522fdbdb7dc5518be516`. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + cache-safe provisional presentation integration** | `AuthSessionStore.swift`; b6 + b12/b13 + merged b21 + b23 consumer behavior | `AuthSessionStore` remains sole auth/account owner and is unchanged by cache-core. b23 distinguishes temporary auth transport failure from confirmed auth unavailability only at the repository consumer boundary. Supported account-switch purge remains Runtime-unverified and non-personal workspace scope remains Unknown / Unverified. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested scope** | b7 + b9-b23 runtime | Current list/detail endpoints/parsers/headers accepted for recorded Plus/personal iPhone/iOS17 read-state scope. Cache-core does not change routes/headers. Not Frozen. |
| Native conversation read path | **Stable merged multi-conversation read baseline + b23 cache-core Runtime accepted** | `ConversationRepository` + sidebar/detail UI; b21 merged + b23 cache candidate | b23 preserves the same repository authority while adding persistent list presentation/reconciliation. Detail protocol/residency/scroll ownership remains unchanged. Not Frozen. |
| Manual conversation recovery | **Stable / merged baseline with multi-conversation Runtime evidence** | `ConversationRepository` + detail UI + shell | Existing Sync/Reload behavior unchanged by cache-core. Not Frozen. |
| Multi-conversation state ownership | **Stable / merged for tested Plus/personal iPhone/iOS17 read-state scope** | `DEV-multi-conversation-state-0.1.0-b21`; PR #23 | Exact b21 source `6b50ead167bfde305d2ad58dd16fee6edaabf597`; PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`. Conditional account/workspace/natural-failure boundaries remain Unverified. Not Frozen. |
| Conversation-list persistent cache | **b23 Runtime accepted for tested Plus/personal iPhone/iOS17 cache-core scope; merge pending** | `DEV-conversation-list-cache-core-0.1.0-b23` / `ConversationRepository` + storage-only `ConversationListCacheStore` | Exact b23 source `d2af0fc157f6e2d037636c55f963c18071a332d5`; Run `33101116431`; Artifact `9658508764`. Real device proves provisional cache in ~4 ms before ~4.5 s account verification, `recent_skip`, offline `-1005 -> offline_cache`, retained-list failure feedback, stale/manual refresh, and real first-page safety `28 + preservedOffPageCount=1 -> 29`. Account-switch/corrupt-schema/provisional-row-tap remain conditional Unverified. Not Frozen. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Future follow-tail scroll semantics must consume real per-conversation Send/Stream response ownership; completed read/cache work does not invent it. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for recorded scopes.
- b10-b15 recovery history remains recorded in `BUILD_TEST_INDEX.md`; b15 is merged Stable recovery baseline.
- b16-b21 multi-conversation history remains recorded in `BUILD_TEST_INDEX.md`; b21 is merged Stable for its recorded tested scope.
- b22 conversation-list-cache-core = **Code + static/source + CI + Artifact + partial/failing Runtime**. Disk snapshot/freshness mechanics worked, but cache display waited for auth, offline auth failure bypassed cache and manual refresh lacked explicit terminal feedback.
- b23 conversation-list-cache-core = **Code + source review + CI + identity-valid Artifact + real-device Runtime accepted for recorded cache-core matrix**. User reported no new issue; screenshot directly confirms retained offline list with `刷新失败 · 当前显示缓存`.

Still unverified as applicable: runtime below iOS17, iPad, non-personal workspace, supported verified account-switch mismatch, provisional-row Detail-block tap path and corrupt/schema-incompatible cache rejection. These are evidence boundaries, not current known defects.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, candidate evidence, accepted Runtime behavior or stability changes.