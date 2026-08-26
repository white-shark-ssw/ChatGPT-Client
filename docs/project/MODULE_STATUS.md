# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | Stable | `AppDelegate.swift`, `RootViewController.swift`, `SettingsViewController.swift`; `DEV-app-foundation-0.1.0-b1` | Swift/UIKit baseline real-device tested on iPhone / iOS 17.0. Current shell also exposes the explicit protocol-read diagnostic entry. Not Frozen. |
| Build/runtime metadata | Stable | `AppBuildInfo.swift`, Xcode target settings, `Info.plist` | Exact candidate/source/deployment/runtime identity is embedded in test candidates. Current Active candidate is b7/build 7; accepted runtime auth baseline remains b6/build 6. Not Frozen. |
| Diagnostics / logging | Stable | `ChatGPTClient/Diagnostics/Diagnostics.swift`; foundation + b6 extension | Structured OSLog + bounded rolling JSONL + trace/span + secret filtering + redacted export + explicit clearing through the same owner. b7 reuses this authority unchanged. Not Frozen. |
| IPA build / CI packaging | Stable | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml` | b7 exact-source push run `32938912018` passed Xcode 16.4 build/inspect/upload; artifact ID `9595827498`; IPA SHA-256 `64b0cc055bc9da27bc887698ba18ae5cb2cc0fdb9f15a3a59eb09e55c5fcb4ae`; ZIP digest independently rechecked. Not Frozen. |
| Embedded web login | Stable | `AuthWebViewController.swift`; b2 + later device evidence | Continue with Google and persistence are accepted. Default persistent `WKWebsiteDataStore` remains the persistent auth-secret authority. b7 consumes this path without adding another authority. Not Frozen. |
| Authentication evidence / native `/auth/login` bridge | Stable | `AuthSessionStore.swift`; b3/b4 evidence | Native `/auth/login` is route-specific evidence only and is not an account-context gate or session authority. Not Frozen. |
| Account / workspace context | **Stable** | `AuthSessionStore.swift`; `DEV-auth-bootstrap-0.1.0-b6` | b6 real-device account context accepted for the tested plus/personal account. b7 adds only creation of a short-lived authorized transport after successful account verification; persistent ownership and ordered parsing remain unchanged. Not Frozen. |
| Protocol-read diagnostic transport | **Candidate** | `AuthTransientSession` + `ProtocolReadProbe.swift`; `DEV-protocol-read-0.1.0-b7` | Code written + CI passed + artifact produced. One list/one detail diagnostic path exists with privacy-safe structural logging only. Runtime list/detail behavior is still Unverified; this is not a production conversation repository. |
| Native conversation read path | Unknown / Unverified | Future `DEV-native-read-path` | Blocked until b7 or a later protocol-read candidate establishes accepted real-device list/detail semantics. |
| Streaming / send / attachments | Unknown / Unverified | Future development tasks | Auth/account gate is satisfied, but current streaming/send/attachment protocol has not been implemented or evidenced. |

## Allowed statuses

Use concise statuses such as Active, Candidate, Stable, Frozen, Experimental, Deprecated, or Unknown / Unverified.

## Frozen rule

Before changing a Frozen or Stable core module for an unrelated task, verify that the current task truly requires it and record the concrete reason/evidence. Stable does not mean Frozen.

## Current acceptance boundary

- `DEV-app-foundation-0.1.0-b1`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; foundation Stable, not Frozen.
- `DEV-auth-bootstrap-0.1.0-b6`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; authentication/account context Stable for the accepted iPhone / iOS 17.0 scope.
- `DEV-protocol-read-0.1.0-b7`: **Code written + CI passed + Artifact produced; Runtime/manual/real-device test pending**. Protocol-read remains Candidate, not Stable.

Runtime compatibility below iOS 17.0 and on iPad remains unverified.

## Auto-refresh rule

Update this matrix when modules are added, ownership changes, a module becomes stable/frozen, a frozen decision is reopened, or a new candidate supersedes an old baseline.
