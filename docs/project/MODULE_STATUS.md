# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | Stable | `AppDelegate.swift`, `RootViewController.swift`, `SettingsViewController.swift`; `DEV-app-foundation-0.1.0-b1` | Swift/UIKit baseline builds in CI and was installed/launched successfully through TrollStore on iPhone / iOS 17.0. Auth bootstrap adds only the evidenced login entry. Not Frozen. |
| Build/runtime metadata | Stable | `AppBuildInfo.swift`, Xcode target settings, `Info.plist`; foundation baseline + current b2 candidate | Version/build/candidate/source/deployment/runtime identity is embedded in generated candidates. Not Frozen. |
| Diagnostics / logging | Stable | `ChatGPTClient/Diagnostics/Diagnostics.swift`; `DEV-app-foundation-0.1.0-b1` | Structured OSLog + bounded rolling JSONL persistence + trace/span + secret filtering + redacted export. Real-device Settings/export and cross-restart persistence passed on iPhone / iOS 17.0. Auth bootstrap extends the same authority with safe navigation metadata. Not Frozen. |
| IPA build / CI packaging | Stable | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml`; foundation + auth b2 | Xcode 16.4 CI builds/artifacts passed. Auth b2 also verified deterministic app-icon reconstruction and produced artifact ID `9577612707` / IPA SHA-256 `426c5f9b...61465`. Not Frozen. |
| Embedded web login | Candidate | `AuthWebViewController.swift`; `DEV-auth-bootstrap-0.1.0-b2` | User real-device test successfully completed ChatGPT Continue with Google in the embedded `WKWebView` flow on the tested iPhone / iOS 17.0 candidate. No system-browser fallback is currently justified. Not yet Stable because relaunch persistence/auth-state evidence remains pending. |
| Authenticated session / account context | Unknown / Unverified | Current `DEV-auth-bootstrap` continuation | Successful WebView login does not prove a native session owner, authenticated-state detector, account/workspace context, or `URLSession` consumability. These remain the next authentication evidence targets. |
| ChatGPT protocol / conversation / streaming / attachments | Unknown / Unverified | Future development tasks | Not implemented; historical protocol material remains reference-only. |

## Allowed statuses

Use concise statuses such as Active, Candidate, Stable, Frozen, Experimental, Deprecated, or Unknown / Unverified.

## Frozen rule

Before changing a Frozen or Stable core module for an unrelated task, stop and verify whether the current task truly requires it. Record the concrete reason/evidence before changing the contract.

## Current acceptance boundary

`DEV-app-foundation-0.1.0-b1` has reached **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** and the foundation modules above are accepted as Stable. They are **not Frozen**.

`DEV-auth-bootstrap-0.1.0-b2` has reached **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** specifically for the embedded ChatGPT/Google web-login route. That result does not yet promote the broader authentication/session module to Stable; session persistence, authenticated-state ownership and native session/account consumption remain unverified.

Runtime validation currently covers iPhone / iOS 17.0; lower iOS versions and iPad remain unverified.

## Auto-refresh rule

Update this matrix when modules are added, ownership changes, a module becomes stable/frozen, a frozen decision is reopened, or a new candidate supersedes an old baseline.
