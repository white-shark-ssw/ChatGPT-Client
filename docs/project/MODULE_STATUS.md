# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable b9 scope / b14 compact startup accepted** | `AppDelegate.swift`, `RootViewController.swift`; b9 + b12-b14 | b12 warm-up runtime-proven; b13 fixed immediate list initiation but compact navigation failed. Exact b14 is real-device accepted on iPhone/iOS17 for initial primary/list root, removal of duplicate sidebar controls and native list/detail navigation. b15 does not change shell behavior. Not Frozen. |
| Build/runtime metadata | Stable capability / **b15 active artifact** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | b15 verifies `0.1.0 (15)`, candidate b15, source `fb0c6d75362e`, min iOS14, arm64. Not Frozen. |
| Diagnostics / logging | Stable | `Diagnostics.swift` + auth/recovery call sites | Existing privacy-safe warm-up/freshness diagnostics remain. b15 adds only `detail.cancel.requested` / `detail.cancelled` generation metadata; no raw IDs/bodies/secrets. Not Frozen. |
| IPA build / CI packaging | Stable capability; **b15 produced** | `scripts/build_ipa.sh`, workflow | Run `33004536664` passed; artifact `9619988065`; IPA SHA `b2b54905cff2b67604f95d44033efd6b4b98d319b311ac06204ddec359dd905e`; tested tree `7a988bcad27d023eac77683985c5d7d92b22c176`. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + accepted public warm-up** | `AuthSessionStore.swift`; b6 + b12/b13 runtime | b15 does not change auth/account semantics. `AuthTransientSession.dataTask` only returns the same already-created/resumed transient `URLSessionDataTask` handle so the conversation owner can cancel a detail request. Authorization/cookie/endpoint behavior is unchanged. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only; existing callers ignore the new discardable task return exactly as before. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested scope** | b7 + b9-b13 runtime | Current list/detail endpoints/parsers/headers are unchanged by b15. Not Frozen. |
| Native conversation read path | **Stable b9 scope / b14 shell accepted / b15 lifecycle candidate** | `ConversationRepository` + sidebar/detail UI | b13 generation rejection is runtime-proven; b14 compact navigation accepted. b15 adds selected-detail task ownership so explicit manual replacement can cancel the old network task while retaining freshness generation. Runtime pending. Not Frozen. |
| Manual conversation recovery | **Active — b15 Artifact ready / Runtime pending** | `ConversationRepository` + detail UI + shell | b10 core recovery accepted; b12 centered toast accepted; b14 compact shell accepted. b13 exposed HTTP429 when replacement detail requests overlapped an old in-flight request. b15 tracks/cancels the old selected-detail task before manual replacement and preserves generation rejection. Code + static review + CI + Artifact; Runtime pending. PR #10 open. Not Frozen. |
| Multi-conversation state ownership | Planned / Unverified | future `DEV-multi-conversation-state` | Starts only after recovery is accepted/merged; will generalize current single-selected freshness/request lifecycle into account-scoped resident per-conversation state. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Not proven by b7-b15 read/recovery work. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for their recorded scopes.
- b10 accepted core manual recovery.
- b11 feedback presentation rejected.
- b12 = Code + CI + Artifact + Runtime partial acceptance: centered sync feedback and WebKit warm-up accepted; initial list sequencing rejected.
- b13 = Code + CI + Artifact + Runtime partial/failing: immediate list initiation and stale generation accepted; compact navigation failed; concurrent replacement requests produced HTTP429.
- b14 = **Code + static/source review + CI + Artifact + Runtime/manual accepted for compact startup/navigation**.
- b15 = **Code + static/source review + CI + Artifact; Runtime/manual pending** for selected-detail cancellation/replacement.
- `DEV-conversation-recovery` remains **Active / not Stable / not merged** until b15 real-device acceptance.

Runtime below iOS17, iPad, non-personal workspace, b15 selected-detail replacement behavior, multi-conversation ownership, send/streaming and attachments remain unverified.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, candidate evidence, accepted runtime behavior or stability changes.
