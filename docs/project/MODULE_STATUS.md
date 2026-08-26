# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | **Stable b9 scope / b13 candidate startup change** | `AppDelegate.swift`, `RootViewController.swift`; b9 + b12/b13 | b9 split shell is accepted. b12 WebKit warm-up is now runtime-proven for one iPhone/iOS17 cold start. b13 forces sidebar initialization/list start after warm-up and uses an explicit sidebar action; Runtime pending. Not Frozen. |
| Build/runtime metadata | Stable capability / **b13 active** | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | b13 package verifies `0.1.0 (13)`, candidate `DEV-conversation-recovery-0.1.0-b13`, source `57187c0d0fd3`, iOS min 14.0, arm64. Not Frozen. |
| Diagnostics / logging | Stable | `Diagnostics.swift` + auth/recovery call sites | Structured/redacted diagnostics retained. b12 warm-up counts are runtime-useful; b13 adds integer detail-operation generation/discard reason only. No secrets/raw chat bodies. Not Frozen. |
| IPA build / CI packaging | Stable capability; **b13 produced** | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml` | Run `32997544435` passed; artifact `9617184873`; IPA SHA `2af6334278bcb88683cc123d47617e6956c0efb83aceb9b294961827f3e80040`; head/tested-merge tree `2068ab4dc8f4bd9f94f1cb89e21b8dab29436ebf`. Not Frozen. |
| Embedded web login | Stable explicit fallback | `AuthWebViewController.swift`; b2+ | Visible Login remains fallback only. b12 proved one cold start can hydrate auth without opening it. No hidden/shadow WebView. Not Frozen. |
| Authentication/account context | **Stable baseline + b12 cold-start warm-up accepted for tested run** | `AuthSessionStore.swift`; b6 baseline + b12 runtime | Default persistent WebKit store remains sole persistent secret authority. b12 0/0 -> 41/22 warm-up then normal account/list probe succeeded without Login on iPhone/iOS17. Do not generalize beyond tested scope; no retry/watchdog. Not Frozen. |
| Protocol-read diagnostic transport | **Stable for accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; b7 | Diagnostic-only; not production state owner. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable for tested scope** | b7 + b9-b12 runtime | b12 list/detail/sync transport remained successful; endpoints/headers unchanged by b13. Not Frozen. |
| Native conversation read path | **Stable b9 scope / b13 candidate startup-freshness change** | `ConversationRepository` + sidebar/detail UI | b9 core read is Stable. b13 adds immediate initial list initiation and selected-detail stale-operation rejection required by explicit manual recovery during load. Runtime pending. Not Frozen. |
| Manual conversation recovery | **Candidate — b13 Artifact ready** | `ConversationRepository` + `ConversationDetailViewController` + startup sequencing | b10 core sync/full reload accepted; b11 prompt rejected; b12 centered toast accepted and warm-up works, but lazy list startup rejected. b13 enables sync/reload during ordinary detail loading and prevents an older load completion overwriting newer manual recovery. Code + static review + CI + Artifact; Runtime pending. PR #10 open. Not Frozen. |
| Multi-conversation state ownership | Planned / Unverified | future `DEV-multi-conversation-state` | Next serialized Work after recovery. It will generalize current single-selected freshness behavior into account-scoped resident per-conversation state. |
| Streaming / send / attachments | Unknown / Unverified | Future Work | Not proven by b7-b13 read/recovery work. |

## Current acceptance boundary

- b1 foundation, b6 auth/account, b7 diagnostic read and b9 production native-read are Stable/accepted for their recorded tested scopes.
- b10 is accepted real-device core manual recovery behavior.
- b11 request path worked but required feedback presentation was rejected.
- b12 = **Code + CI + Artifact + Runtime/manual/real-device tested, partial acceptance**: centered sync feedback and public WebKit cold-start warm-up accepted; initial list/sidebar sequencing rejected.
- b13 = **Code written + static/source review + CI passed + Artifact produced; Runtime/manual pending**. Not Stable.

Runtime compatibility below iOS17, iPad, non-personal workspace behavior, b13 startup/recovery-during-load behavior, multi-conversation ownership, send/streaming and attachments remain unverified.

## Frozen rule

Stable does not mean Frozen. Before changing a Stable/Frozen core for unrelated work, verify the requirement and update evidence/status.

## Auto-refresh rule

Update this matrix when ownership, candidate evidence, accepted runtime behavior or module stability changes.