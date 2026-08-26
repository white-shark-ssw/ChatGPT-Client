# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable b9 scope / b14 compact startup accepted** | `AppDelegate.swift`, `RootViewController.swift`; b9 + b12-b14 | b12 warm-up runtime-proven; b13 fixed immediate list initiation but compact navigation failed. Exact b14 is now real-device accepted on iPhone/iOS17 for initial primary/list root, removal of duplicate sidebar controls and native list/detail navigation. Not Frozen. |
| Build/runtime metadata | Stable capability / **b14 accepted artifact** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | b14 verifies `0.1.0 (14)`, candidate b14, source `5b2f60dc8b30`, min iOS14, arm64. Not Frozen. |
| Diagnostics / logging | Stable | `Diagnostics.swift` + auth/recovery call sites | Warm-up counts and detail-operation generation/discard reason remain privacy-safe. b13 runtime diagnostics proved immediate list start, stale-operation rejection and replacement HTTP429. Not Frozen. |
| IPA build / CI packaging | Stable capability; **b14 produced** | `scripts/build_ipa.sh`, workflow | Run `33000566633`; artifact `9618410313`; IPA SHA `b9100deb1d59b8ce22e15e72f766f0313be2903ec96ed2cda3d397986ba89182`; tested tree `4d0ddb24ba6e261cdb7a4057ce47e73f199ad481`. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + b12 warm-up accepted for tested run** | `AuthSessionStore.swift`; b6 + b12/b13 runtime | Public default-WebKit warm-up accepted for tested cold starts. b14 only changes when the product root is installed relative to that accepted warm-up. No retry/watchdog. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only; not production state owner. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested scope** | b7 + b9-b13 runtime | b13 list HTTP200 28/29 and ordinary detail HTTP200 remain current evidence. Endpoints/headers unchanged by b14. Not Frozen. |
| Native conversation read path | **Stable b9 scope / b14 shell accepted** | `ConversationRepository` + sidebar/detail UI | b13 immediate list initiation/freshness guard runtime-proven; b14 compact list/detail presentation now accepted. Not Frozen. |
| Manual conversation recovery | **Active — core/shell accepted; selected-detail overlap pending** | `ConversationRepository` + detail UI + shell | b10 core recovery accepted; b12 centered toast accepted; b13 recovery-during-load and stale-generation rejection worked but overlapping replacement requests produced HTTP429. b14 compact startup/navigation is accepted but intentionally did not change this request-lifecycle defect. Continue in the same Work/PR with a fresh candidate. Not Frozen. |
| Multi-conversation state ownership | Planned / Unverified | future `DEV-multi-conversation-state` | Starts only after recovery is accepted/merged; will generalize freshness into account-scoped resident per-conversation state. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Not proven by b7-b14 read/recovery work. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for their recorded scopes.
- b10 accepted core manual recovery.
- b11 feedback presentation rejected.
- b12 = Code + CI + Artifact + Runtime partial acceptance: centered sync feedback and WebKit warm-up accepted; initial list sequencing rejected.
- b13 = Code + CI + Artifact + Runtime partial/failing: immediate list initiation and stale generation accepted; compact navigation failed; concurrent replacement requests produced HTTP429.
- b14 = **Code + static/source review + CI + Artifact + Runtime/manual accepted for compact startup/navigation**.
- `DEV-conversation-recovery` remains **Active / not Stable / not merged** until selected-detail cancellation/replacement is implemented and accepted.

Runtime below iOS17, iPad, non-personal workspace, selected-detail replacement correction, multi-conversation ownership, send/streaming and attachments remain unverified.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, candidate evidence, accepted runtime behavior or stability changes.
