# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable recovery baseline + active multi-conversation integration** | `AppDelegate.swift`, `RootViewController.swift`; b14/b15 Stable, active branch b16 source | b14 compact startup/list-detail navigation accepted on iPhone/iOS17. Active branch moves foreground selection to Root as the single write path and adds account-reset UI clearing; not Runtime-accepted yet. Not Frozen. |
| Build/runtime metadata | Stable capability / **b15 merged baseline**; active b16 historical | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | Stable accepted identity remains `0.1.0 (15)` b15. b16 advanced source/build to 16 but its packaged candidate identity was wrong and is rejected. Not Frozen. |
| Diagnostics / logging | Stable baseline + active multi-conversation diagnostics | `Diagnostics.swift` + auth/recovery/residency call sites | Accepted b15 cancellation diagnostics remain. Active source adds resident/coalescing/account-reset/memory-warning metrics; selection transition timing/protected-count coverage is still incomplete. No raw conversation IDs/bodies/secrets. Not Frozen. |
| IPA build / CI packaging | Stable recovery capability; **active Work packaging defect found** | `scripts/build_ipa.sh`, workflow | b15 packaging is accepted. b16 Run `33009246356` succeeded, Artifact `9621830284` exists, but IPA/candidate identity is rejected because the script still hard-coded recovery-b15 candidate/slug. b16 must not be reused; next valid candidate needs corrected unique identity. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + active minimum scope-signal integration** | `AuthSessionStore.swift`; b6 + b12/b13 runtime; active b16 source | Public default-WebKit warm-up remains accepted for tested cold starts. Active branch exposes read-only verified context/change notification and transient-session cancel support; account endpoint/header/cookie semantics are unchanged. Non-personal workspace scope remains Unverified. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested scope** | b7 + b9-b15 runtime | Current list/detail endpoints/parsers/headers accepted for recorded Plus/personal iPhone/iOS17 scope. Active multi-conversation code does not change protocol routes/headers. Not Frozen. |
| Native conversation read path | **Stable merged recovery baseline + active multi-conversation owner rewrite** | `ConversationRepository` + sidebar/detail UI | b9-b15 read/recovery behavior is Stable for tested scope. Active branch generalizes detail ownership to per-conversation residents/operations, but second static review found unresolved stale-scope/waiter/presentation/list-freshness/execution-domain defects; no multi-conversation runtime acceptance yet. Not Frozen. |
| Manual conversation recovery | **Stable / merged baseline; active target-isolation rewrite unverified** | `ConversationRepository` + detail UI + shell; PR #10 baseline | b10/b12/b14/b15 recovery behavior remains accepted. Active branch makes recovery target-specific by per-conversation operation ownership, but hidden Sync A -> B -> A presentation is not yet closed and must be fixed before multi-conversation runtime Candidate. Not Frozen. |
| Multi-conversation state ownership | **Active implementation / CI-evidenced / Runtime Unverified** | `DEV-multi-conversation-state`; branch `dev/multi-conversation-state-20260827` | b16 source compiled/packaged in CI but Artifact identity rejected. Core direction exists: account-scoped residents, per-conversation generations/tasks, coalescing, failed terminal state, current-node retention, memory-warning trim. P0 source defects remain; no Stable claim. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Not proven by read/recovery/multi-conversation CI work. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for their recorded scopes.
- b10 accepted core manual recovery.
- b12 accepted centered sync feedback and public WebKit warm-up for tested cold starts.
- b14 accepted compact startup/navigation.
- b15 = **Code + static/source review + CI + Artifact + Runtime/manual/real-device accepted** for selected-detail cancellation/replacement.
- `DEV-conversation-recovery` = **Stable / merged** at `a089fb0448f1c0282e634e5cccf3d0a47199d81f` for the recorded Plus/personal iPhone/iOS17 scope.
- `DEV-multi-conversation-state` currently = **Code + CI evidence only, Artifact identity rejected, second static review has unresolved findings, Runtime not tested**.

Runtime below iOS17, iPad, non-personal workspace, multi-conversation runtime ownership, send/streaming and attachments remain unverified.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, candidate evidence, accepted runtime behavior or stability changes.
