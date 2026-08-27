# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable recovery baseline + active multi-conversation integration** | `AppDelegate.swift`, `RootViewController.swift`; b14/b15 Stable, active b17 source | b14 compact startup/list-detail navigation accepted on iPhone/iOS17. b17 core switching/resident return is now real-device evidenced for the supplied run. Per-conversation semantic scroll restoration is missing and reproduced as P1. Not Frozen. |
| Build/runtime metadata | Stable capability / **b15 merged baseline + valid b17 Candidate identity** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | Stable accepted identity remains `0.1.0 (15)` b15. b17 exact package independently verifies `0.1.0 (17)`, multi-conversation candidate/source identity, iOS14 minimum and arm64. Not Frozen. |
| Diagnostics / logging | Stable baseline + active multi-conversation diagnostics | `Diagnostics.swift` + auth/recovery/residency call sites | b17 runtime confirms old->new selection hashes, resident/active/protected counts, coalescing, hidden stores and `resident.firstVisible` usefulness. Current schema does not log semantic scroll anchor; scroll defect is grounded by direct user observation. No raw conversation IDs/bodies/secrets. Not Frozen. |
| IPA build / CI packaging | Stable recovery capability + **b17 identity-valid Artifact** | `scripts/build_ipa.sh`, workflow | b15 packaging accepted. b16 identity rejected historically. b17 Run `33045536770` succeeded and Artifact `9635486304` independently matches filename/candidate/source/version/build/SHA/arm64/iOS14 identity. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + active minimum scope-signal integration** | `AuthSessionStore.swift`; b6 + b12/b13 runtime; active b17 source | Public default-WebKit warm-up remains accepted for tested cold starts. b17 repository revalidates the Auth owner's current scope instead of allowing stale transport context to re-adopt scope. Supported account-switch purge is still runtime-unverified. Non-personal workspace scope remains Unverified. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested scope** | b7 + b9-b15 runtime | Current list/detail endpoints/parsers/headers accepted for recorded Plus/personal iPhone/iOS17 scope. b17 changes ownership/freshness only; protocol routes/headers remain unchanged. Not Frozen. |
| Native conversation read path | **Stable merged recovery baseline + active multi-conversation core runtime evidence** | `ConversationRepository` + sidebar/detail UI | b17 exact runtime accepts resident return, hidden completion and same-target coalescing for the supplied iPhone/iOS17 run. Work remains Active because scroll anchor, failure/account-switch and measured LRU acceptance are not complete. Not Frozen. |
| Manual conversation recovery | **Stable / merged baseline + b17 Sync target isolation runtime-evidenced** | `ConversationRepository` + detail UI + shell; PR #10 baseline | b10/b12/b14/b15 recovery remains accepted. b17 Sync A->B->A rejoined the same active Sync and completed HTTP200/ok in the supplied run. Isolated b17 Reload replacement remains open. Not Frozen. |
| Multi-conversation state ownership | **Active / Code + static + CI + Artifact + core Runtime evidence; P1 scroll defect** | `DEV-multi-conversation-state`; branch `dev/multi-conversation-state-20260827`; b17 | Exact b17 core runtime shows resident hits, hidden stores, coalescing, Sync return and rapid overlap up to 3 active operations with no HTTP429 in export. User reproduced A≈10% -> B scroll -> return A position shift; semantic per-conversation scroll-anchor restoration is now a confirmed P1 gap. Stable/Frozen = No. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Not proven by read/recovery/multi-conversation work. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for their recorded scopes.
- b10 accepted core manual recovery.
- b12 accepted centered sync feedback and public WebKit warm-up for tested cold starts.
- b14 accepted compact startup/navigation.
- b15 = **Code + static/source review + CI + Artifact + Runtime/manual/real-device accepted** for selected-detail cancellation/replacement.
- `DEV-conversation-recovery` = **Stable / merged** at `a089fb0448f1c0282e634e5cccf3d0a47199d81f` for the recorded Plus/personal iPhone/iOS17 scope.
- b16 multi-conversation = historical/rejected before runtime.
- b17 multi-conversation = **Code + static/local + CI + Artifact + core real-device sequences accepted for the supplied iPhone/iOS17 run; P1 semantic scroll-anchor defect reproduced; Work Active; Stable/Frozen = No**.

Runtime below iOS17, iPad, non-personal workspace, account-switch purge, failure residency, normal LRU capacity, send/streaming and attachments remain unverified.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, candidate evidence, accepted runtime behavior or stability changes.
