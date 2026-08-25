# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | Candidate | `AppDelegate.swift`, `RootViewController.swift`, `SettingsViewController.swift`; `DEV-app-foundation-0.1.0-b1` | Swift/UIKit baseline builds in CI; TrollStore runtime validation pending. |
| Build/runtime metadata | Candidate | `AppBuildInfo.swift`, Xcode target settings, `Info.plist` | Version/build/candidate/source commit/deployment/runtime metadata is surfaced in-app and diagnostics. |
| Diagnostics / logging | Candidate | `ChatGPTClient/Diagnostics/Diagnostics.swift` | Structured OSLog + bounded rolling JSONL persistence + trace/span + secret filtering + redacted export. CI compilation passed; runtime persistence/export not yet tested. |
| IPA build / CI packaging | Candidate | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml` | Xcode 16.4 CI build and IPA artifact production passed; TrollStore install/launch pending. |
| Authentication / session | Unknown / Unverified | Future `DEV-auth-bootstrap` | Not implemented in this task. |
| ChatGPT protocol / conversation / streaming / attachments | Unknown / Unverified | Future development tasks | Not implemented; historical protocol material remains reference-only. |

## Allowed statuses

Use concise statuses such as Active, Candidate, Stable, Frozen, Experimental, Deprecated, or Unknown / Unverified.

## Frozen rule

Before changing a Frozen or Stable core module for an unrelated task, stop and verify whether the current task truly requires it. Record the concrete reason/evidence before changing the contract.

## Current acceptance boundary

No product module is Stable/Frozen yet. `DEV-app-foundation-0.1.0-b1` has reached Code written + CI passed + Artifact produced, but has not reached Runtime/manual/real-device tested.

## Auto-refresh rule

Update this matrix when modules are added, ownership changes, a module becomes stable/frozen, a frozen decision is reopened, or a new candidate supersedes an old baseline.
