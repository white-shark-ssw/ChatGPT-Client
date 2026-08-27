# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable recovery baseline + active multi-conversation integration** | `AppDelegate.swift`, `RootViewController.swift`; b14/b15 Stable, active b18 source | b14 compact startup/list-detail navigation accepted on iPhone/iOS17. b17 core switching/resident return is real-device evidenced. b18 adds lightweight per-conversation historical scroll presentation in the existing detail VC only. Not Frozen. |
| Build/runtime metadata | Stable capability / **b15 merged baseline + valid b18 Candidate identity** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | Stable accepted identity remains `0.1.0 (15)` b15. b18 exact package independently verifies `0.1.0 (18)`, candidate/source identity, iOS14 minimum and arm64. Not Frozen. |
| Diagnostics / logging | Stable baseline + active multi-conversation diagnostics | `Diagnostics.swift` + auth/recovery/residency/scroll call sites | b17 runtime confirms selection hashes, resident/active/protected counts, coalescing, hidden stores and first-visible timing. b18 adds privacy-safe scroll anchor saved/restored/discarded diagnostics without raw message IDs/bodies. Runtime anchor evidence pending. Not Frozen. |
| IPA build / CI packaging | Stable recovery capability + **b18 identity-valid Artifact** | `scripts/build_ipa.sh`, workflow | b15 packaging accepted. b16 identity rejected historically. b18 Run `33054012226` succeeded and Artifact `9638821912` independently matches filename/candidate/source/version/build/SHA/arm64/iOS14 identity. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + active minimum scope-signal integration** | `AuthSessionStore.swift`; b6 + b12/b13 runtime; active b17/b18 source | Public default-WebKit warm-up remains accepted for tested cold starts. b17 repository revalidates current Auth scope; b18 does not change auth/account ownership. Supported account-switch purge still runtime-unverified. Non-personal workspace scope Unverified. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested scope** | b7 + b9-b15 runtime | Current list/detail endpoints/parsers/headers accepted for recorded Plus/personal iPhone/iOS17 scope. b17/b18 do not change protocol routes/headers. Not Frozen. |
| Native conversation read path | **Stable merged recovery baseline + active multi-conversation core runtime evidence** | `ConversationRepository` + sidebar/detail UI | b17 exact runtime accepts resident return, hidden completion and same-target coalescing. b18 preserves repository ownership and adds presentation-only scroll state. Work remains Active pending b18 scroll runtime plus remaining failure/account-switch/LRU gates. Not Frozen. |
| Manual conversation recovery | **Stable / merged baseline + b17 Sync target isolation runtime-evidenced** | `ConversationRepository` + detail UI + shell; PR #10 baseline | b10/b12/b14/b15 recovery remains accepted. b17 Sync A->B->A rejoined same active Sync. b18 preserves historical anchor across visible Sync/Reload when the anchor message remains; runtime validation pending. Not Frozen. |
| Multi-conversation state ownership | **Active / b17 core Runtime accepted; b18 Code + static/source + CI + Artifact; b18 Runtime pending** | `DEV-multi-conversation-state`; branch `dev/multi-conversation-state-20260827`; b18 | Exact b18 source `f30c13b4...` adds per-conversation historical message anchor + relative offset without changing Repository/protocol authority. Artifact `9638821912` is identity-valid. Stable/Frozen = No. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Not proven by read/recovery/multi-conversation work. Future follow-tail scroll semantics must consume real Send/Stream response ownership; b18 does not invent it. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for recorded scopes.
- b10 accepted core manual recovery.
- b12 accepted centered sync feedback and public WebKit warm-up for tested cold starts.
- b14 accepted compact startup/navigation.
- b15 = **Code + static/source review + CI + Artifact + Runtime/manual/real-device accepted** for selected-detail cancellation/replacement.
- `DEV-conversation-recovery` = Stable / merged for recorded Plus/personal iPhone/iOS17 scope.
- b16 multi-conversation = historical/rejected before runtime.
- b17 multi-conversation = **Code + static/local + CI + Artifact + core real-device sequences accepted; P1 scroll-anchor defect reproduced**.
- b18 multi-conversation = **Code + static/source review + CI + Artifact identity accepted; Runtime/manual/real-device pending; Work Active; Stable/Frozen = No**.

Runtime below iOS17, iPad, non-personal workspace, account-switch purge, failure residency, normal LRU capacity, b18 scroll semantics, send/streaming and attachments remain unverified as applicable.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, candidate evidence, accepted runtime behavior or stability changes.
