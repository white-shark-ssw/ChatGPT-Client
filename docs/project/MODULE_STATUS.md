# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable recovery baseline** | `AppDelegate.swift`, `RootViewController.swift`; b14/b15 | b14 compact startup/list-detail navigation accepted on iPhone/iOS17. b15 did not change shell behavior. Not Frozen. |
| Build/runtime metadata | Stable capability / **b15 merged baseline** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | `0.1.0 (15)`, candidate b15, source `fb0c6d75362e`, min iOS14, arm64. Not Frozen. |
| Diagnostics / logging | Stable | `Diagnostics.swift` + auth/recovery call sites | Privacy-safe warm-up/freshness diagnostics plus accepted `detail.cancel.requested` / `detail.cancelled` generation metadata. No raw IDs/bodies/secrets. Not Frozen. |
| IPA build / CI packaging | Stable capability | `scripts/build_ipa.sh`, workflow | b15 run `33004536664`; artifact `9619988065`; IPA SHA `b2b54905cff2b67604f95d44033efd6b4b98d319b311ac06204ddec359dd905e`; tested tree `7a988bcad27d023eac77683985c5d7d92b22c176`. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + accepted public warm-up** | `AuthSessionStore.swift`; b6 + b12/b13 runtime | Public default-WebKit warm-up accepted for tested cold starts. b15 only exposes the same already-created transient `URLSessionDataTask`; auth/header/cookie/endpoint semantics unchanged. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only; existing callers may ignore discardable task return exactly as before. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested scope** | b7 + b9-b15 runtime | Current list/detail endpoints/parsers/headers accepted for recorded Plus/personal iPhone/iOS17 scope. Not Frozen. |
| Native conversation read path | **Stable merged recovery baseline** | `ConversationRepository` + sidebar/detail UI; b9-b15 | Initial list/detail read, cold-start hydration sequencing, compact navigation, stale-generation rejection and selected-detail replacement lifecycle are accepted for tested scope. Not Frozen. |
| Manual conversation recovery | **Stable / merged** | `ConversationRepository` + detail UI + shell; PR #10 | b10 core recovery, b12 centered toast, b14 compact shell and b15 cancellation/replacement are real-device accepted. b15 replacement cases cancelled obsolete generations and replacements returned HTTP200 without HTTP429. Merge `a089fb0448f1c0282e634e5cccf3d0a47199d81f`. Not Frozen. |
| Multi-conversation state ownership | Planned / Unverified | future `DEV-multi-conversation-state` | Next serialized Work when requested; will generalize current single-selected freshness/request lifecycle into account-scoped resident per-conversation state. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Not proven by b7-b15 read/recovery work. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for their recorded scopes.
- b10 accepted core manual recovery.
- b12 accepted centered sync feedback and public WebKit warm-up for tested cold starts.
- b14 accepted compact startup/navigation.
- b15 = **Code + static/source review + CI + Artifact + Runtime/manual/real-device accepted** for selected-detail cancellation/replacement.
- `DEV-conversation-recovery` = **Stable / merged** at `a089fb0448f1c0282e634e5cccf3d0a47199d81f` for the recorded Plus/personal iPhone/iOS17 scope.

Runtime below iOS17, iPad, non-personal workspace, multi-conversation ownership, send/streaming and attachments remain unverified.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, candidate evidence, accepted runtime behavior or stability changes.
