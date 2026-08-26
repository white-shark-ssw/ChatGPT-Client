# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable b9 scope / b14 candidate compact-startup change** | `AppDelegate.swift`, `RootViewController.swift`; b9 + b12-b14 | b12 warm-up runtime-proven for one cold start. b13 fixed immediate list initiation but compact navigation stayed on blank detail and duplicated sidebar controls. b14 warms before root installation, constructs split columns synchronously, starts compact on primary/list and removes custom duplicate sidebar item. Runtime pending. Not Frozen. |
| Build/runtime metadata | Stable capability / **b14 active** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | b14 package verifies `0.1.0 (14)`, candidate b14, source `5b2f60dc8b30`, min iOS14, arm64. Not Frozen. |
| Diagnostics / logging | Stable | `Diagnostics.swift` + auth/recovery call sites | Warm-up counts and detail-operation generation/discard reason remain privacy-safe. b13 runtime diagnostics proved immediate list start, long account/list timing, stale-operation rejection and replacement HTTP429. Not Frozen. |
| IPA build / CI packaging | Stable capability; **b14 produced** | `scripts/build_ipa.sh`, workflow | Run `33000566633` passed; artifact `9618410313`; IPA SHA `b9100deb1d59b8ce22e15e72f766f0313be2903ec96ed2cda3d397986ba89182`; tested head/merge tree `4d0ddb24ba6e261cdb7a4057ce47e73f199ad481`. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. b12 proved one cold start can hydrate auth without opening it. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + b12 warm-up accepted for tested run** | `AuthSessionStore.swift`; b6 + b12 runtime | b12 0/0 -> 41/22 warm-up then normal account/list probe succeeded without Login. b13 repeated warm-up success 0/0 -> 39/20. b14 changes only when the product root is installed relative to that accepted warm-up. No retry/watchdog. Not Frozen. |
| Protocol-read diagnostic transport | **Stable accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only; not production state owner. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable tested scope** | b7 + b9-b13 runtime | b13 list HTTP200 28/29 and ordinary large detail HTTP200 remain current evidence. Endpoints/headers unchanged by b14. Not Frozen. |
| Native conversation read path | **Stable b9 scope / b14 shell candidate** | `ConversationRepository` + sidebar/detail UI | b13 immediate list initiation and selected-detail generation guard runtime-proven; compact list/detail navigation failed. b14 changes shell presentation only. Not Frozen. |
| Manual conversation recovery | **Candidate — b14 Artifact ready / overlap defect pending** | `ConversationRepository` + detail UI + shell | b10 core accepted; b12 centered toast accepted; b13 makes recovery actions available during ordinary detail loading and stale generation rejection worked. b13 also exposed HTTP429 when replacement requests overlapped the old in-flight detail request. b14 does not fix that overlap; it only addresses compact startup/navigation. PR #10 open. Not Frozen. |
| Multi-conversation state ownership | Planned / Unverified | future `DEV-multi-conversation-state` | Next serialized Work only after recovery is accepted/merged; will generalize current freshness into account-scoped resident per-conversation state. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Not proven by b7-b14 read/recovery work. |

## Current acceptance boundary

- b1/b6/b7/b9 are Stable/accepted for their recorded scopes.
- b10 is accepted real-device core manual recovery.
- b11 request path worked but required feedback presentation was rejected.
- b12 = **Code + CI + Artifact + Runtime/manual tested, partial acceptance**: centered sync feedback and public WebKit warm-up accepted; initial list/sidebar sequencing rejected.
- b13 = **Code + CI + Artifact + Runtime/manual tested, partial/failing**: initial list starts immediately and stale generation is rejected, but compact startup/navigation failed and concurrent replacement requests produced HTTP429.
- b14 = **Code + static/source review + CI + Artifact; Runtime pending**. It addresses only compact startup/navigation; not Stable.

Runtime below iOS17, iPad, non-personal workspace, b14 compact navigation, the selected-detail overlap correction, multi-conversation ownership, send/streaming and attachments remain unverified.

## Frozen / auto-refresh rule

Stable does not mean Frozen. Update this matrix when ownership, candidate evidence, accepted runtime behavior or stability changes.