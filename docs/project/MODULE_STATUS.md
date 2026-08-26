# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | Stable | `AppDelegate.swift`, `RootViewController.swift`, `SettingsViewController.swift`; foundation + b7 diagnostic entry | Swift/UIKit shell real-device tested on iPhone / iOS 17.0. Not Frozen. |
| Build/runtime metadata | Stable | `AppBuildInfo.swift`, Xcode settings, `Info.plist` | Exact candidate/source/deployment/runtime identity is embedded. Current accepted protocol candidate is b7/build 7. Not Frozen. |
| Diagnostics / logging | Stable | `Diagnostics.swift` | Structured OSLog + bounded JSONL + redacted export + clear control. b7 reused this authority and exported privacy-safe protocol evidence. Not Frozen. |
| IPA build / CI packaging | Stable | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml` | b7 exact-source push run `32938912018` passed; artifact ID `9595827498`; IPA SHA-256 `64b0cc055bc9da27bc887698ba18ae5cb2cc0fdb9f15a3a59eb09e55c5fcb4ae`. Not Frozen. |
| Embedded web login | Stable | `AuthWebViewController.swift`; b2+ | Continue with Google and persistent default `WKWebsiteDataStore` authentication accepted. Not Frozen. |
| Authentication/account context | Stable | `AuthSessionStore.swift`; b6 + b7 regression evidence | Ordered plus/personal account context accepted. b7 again observed first-attempt session 403 then explicit user restart -> session/accounts HTTP 200. No automatic retry. Not Frozen. |
| Protocol-read diagnostic transport | **Stable for accepted diagnostic scope** | `AuthTransientSession` + `ProtocolReadProbe.swift`; `DEV-protocol-read-0.1.0-b7` | **Code + CI + Artifact + real-device tested.** Personal-account list HTTP 200 and first detail HTTP 200 using transient bearer + copied ephemeral cookies, with no account header required in the tested run. Diagnostic-only; not a production repository. Not Frozen. |
| Conversation-list/detail protocol evidence | **Stable for tested scope** | `DEV-protocol-read-0.1.0-b7` | List: 28/29 items, HTTP 200. Detail: 13,152,411 bytes, mapping 2068 / messages 2067, current node mapped and identity matched. iPhone / iOS 17.0, plus/personal only. Not Frozen. |
| Native conversation read path | Unknown / Unverified | Future `DEV-native-read-path` | Next core task. Must establish production repository/selected-conversation/message-tree ownership and handle the evidenced large detail payload without identity mixing or naive unbounded rendering. |
| Streaming / send / attachments | Unknown / Unverified | Future development tasks | Not proven by b7 read evidence. |

## Allowed statuses

Use concise statuses such as Active, Candidate, Stable, Frozen, Experimental, Deprecated, or Unknown / Unverified.

## Frozen rule

Before changing a Frozen or Stable core module for an unrelated task, verify the task truly requires it and record the evidence. Stable does not mean Frozen.

## Current acceptance boundary

- `DEV-app-foundation-0.1.0-b1`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; foundation Stable, not Frozen.
- `DEV-auth-bootstrap-0.1.0-b6`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; auth/account context Stable for the tested iPhone / iOS 17.0 scope.
- `DEV-protocol-read-0.1.0-b7`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; current Plus/personal conversation-list + one-detail read protocol accepted on iPhone / iOS 17.0. Diagnostic owner remains separate from future production conversation state.

Runtime compatibility below iOS 17.0, iPad, non-personal workspace behavior, send/streaming and attachments remain unverified.

## Auto-refresh rule

Update this matrix when modules are added, ownership changes, a module becomes stable/frozen, a frozen decision is reopened, or a new candidate supersedes an old baseline.
