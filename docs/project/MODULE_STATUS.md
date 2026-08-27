# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable recovery baseline + active multi-conversation integration** | `AppDelegate.swift`, `RootViewController.swift`; b14/b15 Stable, active b21 source | b14 compact startup/list-detail navigation accepted. b17 core switching/resident return and b18 historical scroll accepted. b20 exposed first Detail-view-load title lifecycle overwrite; b21 changes Root lifecycle ordering by one line and awaits Runtime. Not Frozen. |
| Build/runtime metadata | Stable capability / **b15 merged baseline + valid b21 Candidate identity** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | Stable merged product baseline remains b15. b21 independently verifies `0.1.0 (21)`, candidate/source identity, iOS14 minimum, `[1,2]` and arm64. Not Frozen. |
| Diagnostics / logging | Stable baseline + **b19 process-memory measurement Runtime evidence** | `Diagnostics.swift` + auth/recovery/residency/scroll call sites | b19 process-footprint sampling is real-device accepted for observed 0→8 resident matrix; exact process-limit headroom remained unavailable. b20/b21 do not change Diagnostics. Privacy boundary unchanged. Not Frozen. |
| IPA build / CI packaging | Stable recovery capability + **b21 identity-valid Artifact** | `scripts/build_ipa.sh`, workflow | b21 Run `33070183417` / Job `98510113281` succeeded; Artifact `9645439329` independently matches filename/candidate/source/version/build/SHA/arm64/iOS14 identity. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + active minimum scope-signal integration** | `AuthSessionStore.swift`; b6 + b12/b13 runtime; active multi-conversation source | b19-b21 do not change auth/account ownership. One b20 cold-start probe HTTP403 recovered through a later explicit list generation before title reproduction; no automatic retry/fallback was added. Supported account-switch purge remains Runtime-unverified. Non-personal workspace scope Unverified. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested scope** | b7 + b9-b15 runtime | Current list/detail endpoints/parsers/headers accepted for recorded Plus/personal iPhone/iOS17 scope. b17-b21 do not change protocol routes/headers. Not Frozen. |
| Native conversation read path | **Stable merged recovery baseline + active multi-conversation Runtime evidence** | `ConversationRepository` + sidebar/detail UI | b17 core resident/coalescing behavior accepted; b18 presentation-only historical scroll accepted; b19 memory matrix accepted. b20/b21 title work does not change Repository. Remaining failure/account/LRU/replacement gates stay open. Not Frozen. |
| Manual conversation recovery | **Stable / merged baseline + multi-conversation recovery Runtime evidence** | `ConversationRepository` + detail UI + shell | b17 Sync A->B->A rejoined same active Sync. b18 visible Sync/Reload anchor preservation and active Sync return coalescing accepted. b19-b21 do not change recovery behavior. Not Frozen. |
| Multi-conversation state ownership | **Active / b17 core + b18 scroll + b19 memory Runtime accepted; b20 title lifecycle defect reproduced; b21 Artifact ready; not Stable** | `DEV-multi-conversation-state`; branch `dev/multi-conversation-state-20260827`; b21 | Exact b21 source `6b50ead167bfde305d2ad58dd16fee6edaabf597`; Artifact `9645439329`. b21 only orders first Detail view initialization before summary-title assignment. Runtime title proof, natural failure, supported account-switch, normal LRU headroom decision and one isolated replacement gate remain open. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Future follow-tail scroll semantics must consume real per-conversation Send/Stream response ownership; current work does not invent it. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for recorded scopes.
- b10 accepted core manual recovery.
- b12 accepted centered sync feedback and public WebKit warm-up for tested cold starts.
- b14 accepted compact startup/navigation.
- b15 = **Code + static/source review + CI + Artifact + Runtime/manual/real-device accepted** for selected-detail cancellation/replacement and is merged Stable recovery baseline.
- b16 multi-conversation = historical/rejected before Runtime.
- b17 multi-conversation = **Code + static/local + CI + Artifact + core Runtime accepted; historical scroll defect reproduced**.
- b18 multi-conversation = **Code + static/source + CI + Artifact + real-device historical-scroll/Sync/Reload-preservation/resident-regression matrix accepted**.
- b19 multi-conversation = **Code + static/source + CI + Artifact + real-device process-footprint 0→8 resident matrix accepted; process-limit headroom Unverified; no normal LRU capacity frozen**.
- b20 multi-conversation = **Code + static/source + CI + Artifact + partial/failing Runtime; first unloaded Detail entry title was overwritten to `新对话` by first view lifecycle**.
- b21 multi-conversation = **Code + static/source + CI + identity-valid Artifact; Runtime pending**.

Still unverified/open as applicable: b21 exact first-entry/rapid-switch title Runtime, runtime below iOS17, iPad, non-personal workspace, supported account-switch purge, natural failure residency, normal bounded LRU/process-limit headroom policy, missing-anchor-message discard Runtime path, isolated same-target Reload replacement under an older in-flight Detail, Send/Stream and attachments.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, candidate evidence, accepted Runtime behavior or stability changes.
