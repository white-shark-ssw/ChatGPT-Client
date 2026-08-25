# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | Stable | `AppDelegate.swift`, `RootViewController.swift`, `SettingsViewController.swift`; `DEV-app-foundation-0.1.0-b1` | Swift/UIKit baseline builds in CI and was installed/launched successfully through TrollStore on iPhone / iOS 17.0. Not Frozen. |
| Build/runtime metadata | Stable | `AppBuildInfo.swift`, Xcode target settings, `Info.plist`; `DEV-app-foundation-0.1.0-b1` | Version/build/candidate/source/deployment/runtime identity was verified in the generated IPA and supplied real-device diagnostic export. Not Frozen. |
| Diagnostics / logging | Stable | `ChatGPTClient/Diagnostics/Diagnostics.swift`; `DEV-app-foundation-0.1.0-b1` | Structured OSLog + bounded rolling JSONL persistence + trace/span + secret filtering + redacted export. Real-device Settings/export and cross-restart persistence passed on iPhone / iOS 17.0. Not Frozen. |
| IPA build / CI packaging | Stable | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml`; `DEV-app-foundation-0.1.0-b1` | Xcode 16.4 CI build/artifact production passed; accepted IPA installed/launched successfully through TrollStore on iPhone / iOS 17.0. Not Frozen. |
| Authentication / session | Unknown / Unverified | Future `DEV-auth-bootstrap` | Not implemented in foundation; next serial development phase. |
| ChatGPT protocol / conversation / streaming / attachments | Unknown / Unverified | Future development tasks | Not implemented; historical protocol material remains reference-only. |

## Allowed statuses

Use concise statuses such as Active, Candidate, Stable, Frozen, Experimental, Deprecated, or Unknown / Unverified.

## Frozen rule

Before changing a Frozen or Stable core module for an unrelated task, stop and verify whether the current task truly requires it. Record the concrete reason/evidence before changing the contract.

## Current acceptance boundary

`DEV-app-foundation-0.1.0-b1` has reached **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** and the foundation modules above are accepted as Stable. They are **not Frozen**: later tasks may change them when a concrete current requirement/evidence justifies it. Runtime validation currently covers iPhone / iOS 17.0; lower iOS versions and iPad remain unverified.

## Auto-refresh rule

Update this matrix when modules are added, ownership changes, a module becomes stable/frozen, a frozen decision is reopened, or a new candidate supersedes an old baseline.
