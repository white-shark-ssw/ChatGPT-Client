# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | Stable | `AppDelegate.swift`, `RootViewController.swift`, `SettingsViewController.swift`; `DEV-app-foundation-0.1.0-b1` | Swift/UIKit baseline real-device tested on iPhone / iOS 17.0. Settings now includes the user-requested diagnostics-clear control; shell remains Stable, not Frozen. |
| Build/runtime metadata | Stable | `AppBuildInfo.swift`, Xcode target settings, `Info.plist` | Exact candidate/source/deployment/runtime identity is embedded in test candidates. Current account-context candidate is b6/build 6. Not Frozen. |
| Diagnostics / logging | Stable | `ChatGPTClient/Diagnostics/Diagnostics.swift`; foundation + b6 extension | Structured OSLog + bounded rolling JSONL + trace/span + secret filtering + redacted export. b6 adds user-triggered clearing of the same store's current and rotated files; it does not introduce a second store or clear auth state. Code + CI + artifact passed; clear-button runtime behavior not yet separately tested. Not Frozen. |
| IPA build / CI packaging | Stable | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml` | b6 push run `32934821144` passed; artifact ID `9594474567`; IPA SHA-256 `c7109f691c1de675ef55da1a08695c10663b62030853453ee2fafd01fb070c8b`. Embedded candidate/source/build were locally rechecked. Not Frozen. |
| Embedded web login | Stable | `AuthWebViewController.swift`; b2 + later device evidence | Continue with Google and persistence are accepted. WebKit can pass the observed Cloudflare challenge and still reach authenticated non-`/auth` `chatgpt.com` HTTP 200. Default persistent `WKWebsiteDataStore` remains the persistent auth-secret authority. Not Frozen. |
| Authentication evidence / native `/auth/login` bridge | Stable | `AuthSessionStore.swift`; b3/b4 evidence | b3 proved transient native `/auth/login` success once; b4 proved the same route can return Cloudflare HTTP 403 while WebKit is authenticated. It is historical route-specific evidence, not an account-context gate or session authority. Not Frozen. |
| Account / workspace context | Candidate | `AuthSessionStore.swift`; `DEV-auth-bootstrap-0.1.0-b6` | b5 real-device second probe reached `/api/auth/session` HTTP 200 and accounts-check HTTP 200, then failed the old `accounts.default.account.id` parser. b6 parses current evidenced `account_ordering` + keyed `accounts` + nested `account.account_id`. Code written + CI passed + Artifact produced; runtime parser result pending. |
| ChatGPT protocol / conversation / streaming / attachments | Unknown / Unverified | Future development tasks | Not implemented; historical protocol material remains reference-only. |

## Allowed statuses

Use concise statuses such as Active, Candidate, Stable, Frozen, Experimental, Deprecated, or Unknown / Unverified.

## Frozen rule

Before changing a Frozen or Stable core module for an unrelated task, verify that the current task truly requires it and record the concrete reason/evidence. Stable does not mean Frozen.

## Current acceptance boundary

- `DEV-app-foundation-0.1.0-b1`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; foundation Stable, not Frozen.
- `DEV-auth-bootstrap-0.1.0-b2`: same evidence level for embedded Google login and WebKit session persistence on iPhone / iOS 17.0.
- `DEV-auth-bootstrap-0.1.0-b3`: same evidence level for transient native `/auth/login` success under its tested conditions; later b4 evidence limits that conclusion and prevents using the route as a durable gate.
- `DEV-auth-bootstrap-0.1.0-b4`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** with authenticated WebKit but native `/auth/login` HTTP 403; account probe never ran.
- `DEV-auth-bootstrap-0.1.0-b5`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**. Second direct probe established session HTTP 200 + accounts-check HTTP 200, then parser failure `missing_default_account`.
- `DEV-auth-bootstrap-0.1.0-b6`: **Code written + CI passed + Artifact produced; Runtime/manual/real-device not yet tested** for ordered account parsing and diagnostics-clear UI.

Runtime compatibility below iOS 17.0 and on iPad remains unverified.

## Auto-refresh rule

Update this matrix when modules are added, ownership changes, a module becomes stable/frozen, a frozen decision is reopened, or a new candidate supersedes an old baseline.
