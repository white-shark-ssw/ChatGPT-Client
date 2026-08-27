# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable recovery baseline + active multi-conversation integration** | `AppDelegate.swift`, `RootViewController.swift`; b14/b15 Stable, active b17 source | b14 compact startup/list-detail navigation accepted on iPhone/iOS17. Active branch keeps Root as the single selection write path and account-reset UI clearing; b17 is CI/Artifact-valid but not Runtime-accepted. Not Frozen. |
| Build/runtime metadata | Stable capability / **b15 merged baseline + valid b17 Candidate identity** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | Stable accepted identity remains `0.1.0 (15)` b15. b17 exact package independently verifies `0.1.0 (17)`, multi-conversation candidate/source identity, iOS14 minimum and arm64; runtime pending. Not Frozen. |
| Diagnostics / logging | Stable baseline + active multi-conversation diagnostics | `Diagnostics.swift` + auth/recovery/residency call sites | Accepted b15 cancellation diagnostics remain. b17 adds old->new selection hash, resident/active/protected counts, coalescing/operation lifecycle, account reset and resident first-visible timing without raw conversation IDs/bodies/secrets. Runtime usefulness still unverified. Not Frozen. |
| IPA build / CI packaging | Stable recovery capability + **b17 identity-valid Artifact** | `scripts/build_ipa.sh`, workflow | b15 packaging accepted. b16 identity rejected historically. b17 Run `33045536770` succeeded and Artifact `9635486304` independently matches filename/candidate/source/version/build/SHA/arm64/iOS14 identity. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + active minimum scope-signal integration** | `AuthSessionStore.swift`; b6 + b12/b13 runtime; active b17 source | Public default-WebKit warm-up remains accepted for tested cold starts. Active branch exposes read-only verified context/change notification and transient-session cancel support; b17 repository revalidates the Auth owner's current scope instead of allowing stale transport context to re-adopt scope. Account endpoint/header/cookie semantics are unchanged. Non-personal workspace scope remains Unverified. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested scope** | b7 + b9-b15 runtime | Current list/detail endpoints/parsers/headers accepted for recorded Plus/personal iPhone/iOS17 scope. b17 changes ownership/freshness only; protocol routes/headers remain unchanged. Not Frozen. |
| Native conversation read path | **Stable merged recovery baseline + active multi-conversation owner rewrite** | `ConversationRepository` + sidebar/detail UI | b9-b15 read/recovery behavior is Stable for tested scope. b17 compiles/packages an account-scoped per-conversation resident/operation owner with list/detail/presentation freshness and deterministic waiter lifecycle. CI/Artifact-valid only; multi-conversation Runtime acceptance pending. Not Frozen. |
| Manual conversation recovery | **Stable / merged baseline; active target-isolation rewrite CI/Artifact-valid, Runtime Unverified** | `ConversationRepository` + detail UI + shell; PR #10 baseline | b10/b12/b14/b15 recovery behavior remains accepted. b17 makes Sync/Reload target-specific, operation-first on return, and preserves same-target cancel-before-replace ordering. A -> B -> A during active recovery still requires real-device validation. Not Frozen. |
| Multi-conversation state ownership | **Active implementation / static + CI + Artifact passed / Runtime Unverified** | `DEV-multi-conversation-state`; branch `dev/multi-conversation-state-20260827`; b17 | b17 exact source `bc69d58b...` / tree `3451585f...` is the first identity-valid runtime Candidate. Core owner fixes compile/package and Artifact identity is accepted; real-device A/B/C concurrency/residency/recovery and memory/LRU evidence remain pending. Not Frozen. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Not proven by read/recovery/multi-conversation CI work. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for their recorded scopes.
- b10 accepted core manual recovery.
- b12 accepted centered sync feedback and public WebKit warm-up for tested cold starts.
- b14 accepted compact startup/navigation.
- b15 = **Code + static/source review + CI + Artifact + Runtime/manual/real-device accepted** for selected-detail cancellation/replacement.
- `DEV-conversation-recovery` = **Stable / merged** at `a089fb0448f1c0282e634e5cccf3d0a47199d81f` for the recorded Plus/personal iPhone/iOS17 scope.
- b16 multi-conversation = historical/rejected before runtime.
- b17 multi-conversation = **Code + static/local + CI + Artifact identity accepted; Runtime/manual/real-device not yet tested; Stable/Frozen = No**.

Runtime below iOS17, iPad, non-personal workspace, multi-conversation runtime ownership, send/streaming and attachments remain unverified.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, candidate evidence, accepted runtime behavior or stability changes.
