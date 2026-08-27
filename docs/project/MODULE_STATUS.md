# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable multi-conversation read-state baseline** | `AppDelegate.swift`, `RootViewController.swift`; b14/b15 + merged b21 | b14 compact startup/list-detail navigation accepted. b17 core switching/resident return and b18 historical scroll accepted. b20 exposed first Detail-view-load title lifecycle overwrite; b21's one-line lifecycle-order correction is real-device accepted. PR #23 merged. Not Frozen. |
| Build/runtime metadata | **Stable capability / merged b21 identity** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | b21 verifies `0.1.0 (21)`, candidate/source identity, iOS14 minimum, `[1,2]` and arm64. PR #23 merged; exact Runtime Candidate identity remains tied to source `6b50ead...`. Not Frozen. |
| Diagnostics / logging | Stable baseline + **b19 process-memory measurement Runtime evidence** | `Diagnostics.swift` + auth/recovery/residency/scroll call sites | b19 process-footprint sampling is real-device accepted for observed 0→8 resident matrix; exact process-limit headroom remained unavailable. b20/b21 do not change Diagnostics. Privacy boundary unchanged. Not Frozen. |
| IPA build / CI packaging | Stable capability + **b21 identity-valid Artifact and PR merge-view CI** | `scripts/build_ipa.sh`, workflow | Exact b21 Run `33070183417` / Job `98510113281`, Artifact `9645439329`; PR #23 merge-view Run `33093117645` / Job `98590935774` also succeeded. Merge-view Artifact `9655230149` is CI evidence only, not a replacement Runtime Candidate. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + merged minimum scope-signal integration** | `AuthSessionStore.swift`; b6 + b12/b13 + merged b21 source | Multi-conversation changes preserve `AuthSessionStore` as sole account/auth owner. Supported account-switch purge remains Runtime-unverified and non-personal workspace scope remains Unknown / Unverified. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested scope** | b7 + b9-b21 runtime | Current list/detail endpoints/parsers/headers accepted for recorded Plus/personal iPhone/iOS17 read-state scope. Multi-conversation work did not change protocol routes/headers. Not Frozen. |
| Native conversation read path | **Stable / merged multi-conversation read-state baseline** | `ConversationRepository` + sidebar/detail UI; b21 / PR #23 | b17 core resident/coalescing behavior accepted; b18 historical scroll accepted; b19 memory matrix accepted; b21 title lifecycle and same-target Reload replacement-under-load/hidden-rejoin coalescing accepted. Conditional natural-failure/account/workspace/missing-anchor boundaries remain explicitly Unverified. Not Frozen. |
| Manual conversation recovery | **Stable / merged baseline with multi-conversation Runtime evidence** | `ConversationRepository` + detail UI + shell | b17 Sync A->B->A rejoined same active Sync. b18 visible Sync/Reload anchor preservation and active Sync return coalescing accepted. Exact b21 diagnostics accept same-target ordinary-load→Reload replacement, old-task cancellation, hidden unrelated-conversation independence, and return coalescing onto the same Reload. Not Frozen. |
| Multi-conversation state ownership | **Stable / merged for tested Plus/personal iPhone/iOS17 read-state scope** | `DEV-multi-conversation-state-0.1.0-b21`; PR #23 | Exact b21 source `6b50ead167bfde305d2ad58dd16fee6edaabf597`; Artifact `9645439329`; PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`. Natural failed-resident navigation, supported account-switch purge, non-personal workspace identity and missing-anchor-message discard remain explicit Unknown / Unverified boundaries; no ordinary LRU capacity is frozen. Not Frozen. |
| Conversation-list persistent cache | Planned next Work | `DEV-conversation-list-cache-core` / `CONVERSATION_LIST_CACHE_PLAN.md` | Current roadmap priority after multi-conversation Stable/merged. Activation/implementation belongs to its own session/checkpoint. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Future follow-tail scroll semantics must consume real per-conversation Send/Stream response ownership; completed read-state work does not invent it. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for recorded scopes.
- b10 accepted core manual recovery.
- b12 accepted centered sync feedback and public WebKit warm-up for tested cold starts.
- b14 accepted compact startup/navigation.
- b15 = **Code + static/source review + CI + Artifact + Runtime/manual/real-device accepted** and merged Stable recovery baseline.
- b16 multi-conversation = historical/rejected before Runtime.
- b17 multi-conversation = **Code + static/local + CI + Artifact + core Runtime accepted; historical scroll defect reproduced**.
- b18 multi-conversation = **Code + static/source + CI + Artifact + real-device historical-scroll/Sync/Reload-preservation/resident-regression matrix accepted**.
- b19 multi-conversation = **Code + static/source + CI + Artifact + real-device process-footprint 0→8 resident matrix accepted; process-limit headroom Unverified; no normal LRU capacity frozen**.
- b20 multi-conversation = **Code + static/source + CI + Artifact + partial/failing Runtime; first unloaded Detail entry title was overwritten to `新对话` by first view lifecycle**.
- b21 multi-conversation = **Code + static/source + CI + identity-valid Artifact + real-device title matrix + same-target Reload replacement-under-load/hidden-rejoin coalescing accepted; PR #23 merged; Stable for recorded tested scope**.

Still unverified as applicable: runtime below iOS17, iPad, non-personal workspace, supported account-switch purge, natural failure residency, normal bounded LRU/process-limit headroom policy and missing-anchor-message discard Runtime path. These are evidence boundaries, not current known defects. Send/Stream and attachments are later Work.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, candidate evidence, accepted Runtime behavior or stability changes.