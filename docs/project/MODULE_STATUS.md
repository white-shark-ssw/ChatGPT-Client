# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable recovery baseline + active multi-conversation integration** | `AppDelegate.swift`, `RootViewController.swift`; b14/b15 Stable, active multi-conversation source | b14 compact startup/list-detail navigation accepted on iPhone/iOS17. b17 core switching/resident return accepted. b18 per-conversation historical scroll presentation is real-device accepted for tested matrix. b19 does not change shell behavior. Not Frozen. |
| Build/runtime metadata | Stable capability / **b15 merged baseline + valid b19 Candidate identity** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | Stable merged product baseline remains b15. b19 exact package independently verifies `0.1.0 (19)`, candidate/source identity, iOS14 minimum, `[1,2]` and arm64. Not Frozen. |
| Diagnostics / logging | Stable baseline + **b19 process-memory measurement capability** | `Diagnostics.swift` + auth/recovery/residency/scroll call sites | b19 adds process footprint/resident-size/memory-limit-remaining/device-memory fields to existing `conversation / resident.*` diagnostics only. CI + Artifact identity accepted; real-device memory values pending. Privacy boundary unchanged. Not Frozen. |
| IPA build / CI packaging | Stable recovery capability + **b19 identity-valid Artifact** | `scripts/build_ipa.sh`, workflow | b19 Run `33063446367` / Job `98487641474` succeeded; Artifact `9642715296` independently matches filename/candidate/source/version/build/SHA/arm64/iOS14 identity. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + active minimum scope-signal integration** | `AuthSessionStore.swift`; b6 + b12/b13 runtime; active multi-conversation source | b19 does not change auth/account ownership. Supported account-switch purge remains runtime-unverified. Non-personal workspace scope Unverified. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested scope** | b7 + b9-b15 runtime | Current list/detail endpoints/parsers/headers accepted for recorded Plus/personal iPhone/iOS17 scope. b17-b19 do not change protocol routes/headers. Not Frozen. |
| Native conversation read path | **Stable merged recovery baseline + active multi-conversation Runtime evidence** | `ConversationRepository` + sidebar/detail UI | b17 core resident/coalescing behavior accepted. b18 keeps repository ownership unchanged and adds Runtime-accepted presentation-only historical scroll state. b19 does not change Repository or residency behavior. Work remains Active for remaining failure/account/LRU/replacement gates. Not Frozen. |
| Manual conversation recovery | **Stable / merged baseline + multi-conversation recovery Runtime evidence** | `ConversationRepository` + detail UI + shell | b17 Sync A->B->A rejoined same active Sync. b18 visible Sync and Reload preserve historical anchor when same message remains; B Sync return re-coalesced. b19 does not change recovery behavior. Not Frozen. |
| Multi-conversation state ownership | **Active / b17 core Runtime accepted; b18 historical-scroll Runtime accepted; b19 measurement Artifact ready; not Stable** | `DEV-multi-conversation-state`; branch `dev/multi-conversation-state-20260827`; b19 | Exact b19 source `c6accf16c8cf80c719f1e569e356b2bbe664e91e`; Artifact `9642715296`. b19 is measurement-only and adds no LRU/capacity behavior. Real iPhone footprint/headroom, natural failure, supported account-switch and one isolated replacement gate remain open. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Future follow-tail scroll semantics must consume real per-conversation Send/Stream response ownership; b18/b19 do not invent it. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for recorded scopes.
- b10 accepted core manual recovery.
- b12 accepted centered sync feedback and public WebKit warm-up for tested cold starts.
- b14 accepted compact startup/navigation.
- b15 = **Code + static/source review + CI + Artifact + Runtime/manual/real-device accepted** for selected-detail cancellation/replacement and is merged Stable recovery baseline.
- b16 multi-conversation = historical/rejected before runtime.
- b17 multi-conversation = **Code + static/local + CI + Artifact + core Runtime accepted; historical scroll defect reproduced**.
- b18 multi-conversation = **Code + static/source + CI + Artifact + real-device historical-scroll/Sync/Reload-preservation/resident-regression matrix accepted**.
- b19 multi-conversation = **Code + static/source + CI + identity-valid Artifact; Runtime process-memory measurement pending; no LRU behavior implemented**.

Still unverified/open as applicable: runtime below iOS17, iPad, non-personal workspace, supported account-switch purge, natural failure residency, normal bounded LRU/process-memory policy, missing-anchor-message discard runtime path, isolated same-target Reload replacement under an older in-flight Detail, Send/Stream and attachments.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, candidate evidence, accepted Runtime behavior or stability changes.
