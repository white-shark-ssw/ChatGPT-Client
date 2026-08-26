# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | Stable | `AppDelegate.swift`, `RootViewController.swift`, `SettingsViewController.swift`; `DEV-app-foundation-0.1.0-b1` | Swift/UIKit baseline real-device tested on iPhone / iOS 17.0. Settings includes the diagnostics-clear control. Not Frozen. |
| Build/runtime metadata | Stable | `AppBuildInfo.swift`, Xcode target settings, `Info.plist` | Exact candidate/source/deployment/runtime identity is embedded in test candidates. Accepted auth candidate is b6/build 6. Not Frozen. |
| Diagnostics / logging | Stable | `ChatGPTClient/Diagnostics/Diagnostics.swift`; foundation + b6 extension | Structured OSLog + bounded rolling JSONL + trace/span + secret filtering + redacted export + explicit clearing of current/rotated files through the same owner. Clearing does not affect WebKit/auth state. Supplied b6 export contains only the fresh test cycle, consistent with the requested clean-log workflow. Not Frozen. |
| IPA build / CI packaging | Stable | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml` | b6 push run `32934821144` passed; artifact ID `9594474567`; IPA SHA-256 `c7109f691c1de675ef55da1a08695c10663b62030853453ee2fafd01fb070c8b`. Embedded candidate/source/build were locally rechecked. Not Frozen. |
| Embedded web login | Stable | `AuthWebViewController.swift`; b2 + later device evidence | Continue with Google and persistence are accepted. WebKit can pass the observed Cloudflare challenge and still reach authenticated ChatGPT. Default persistent `WKWebsiteDataStore` remains the persistent auth-secret authority. Not Frozen. |
| Authentication evidence / native `/auth/login` bridge | Stable | `AuthSessionStore.swift`; b3/b4 evidence | Native `/auth/login` is route-specific evidence only: b3 once succeeded, b4 later returned Cloudflare 403 while WebKit remained authenticated. It is not an account-context gate or session authority. Not Frozen. |
| Account / workspace context | **Stable** | `AuthSessionStore.swift`; `DEV-auth-bootstrap-0.1.0-b6` | b6 real-device second attempt returned `/api/auth/session` HTTP 200 and accounts-check HTTP 200, parsed ordered account context from `account_ordering` + keyed `accounts` + `account.account_id`, observed accountCount=2/orderCount=1, selected plus/personal context, set `session.accountState=verified`, and ended `status=ok`. First attempt returned session HTTP 403; successful second attempt was user-triggered via `重新开始`, not automatic retry. Stable for this exact iPhone / iOS 17.0 scope; not Frozen. |
| ChatGPT protocol / conversation / streaming / attachments | Unknown / Unverified | Future development tasks | Authentication/account-context gate is now satisfied, but current conversation-list/detail/streaming protocol is not implemented or evidenced yet. |

## Allowed statuses

Use concise statuses such as Active, Candidate, Stable, Frozen, Experimental, Deprecated, or Unknown / Unverified.

## Frozen rule

Before changing a Frozen or Stable core module for an unrelated task, verify that the current task truly requires it and record the concrete reason/evidence. Stable does not mean Frozen.

## Current acceptance boundary

- `DEV-app-foundation-0.1.0-b1`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; foundation Stable, not Frozen.
- `DEV-auth-bootstrap-0.1.0-b2`: same evidence level for embedded Google login and WebKit session persistence on iPhone / iOS 17.0.
- `DEV-auth-bootstrap-0.1.0-b3`: same evidence level for transient native `/auth/login` success under its tested conditions; later b4 evidence limits that conclusion.
- `DEV-auth-bootstrap-0.1.0-b4`: same evidence level with authenticated WebKit but native `/auth/login` HTTP 403; account probe never ran.
- `DEV-auth-bootstrap-0.1.0-b5`: same evidence level; a successful second direct probe established session HTTP 200 + accounts-check HTTP 200, then exposed the obsolete parser.
- `DEV-auth-bootstrap-0.1.0-b6`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**. Ordered account parsing passed on the user device and account/workspace context is accepted/Stable for the current path.

Runtime compatibility below iOS 17.0 and on iPad remains unverified.

## Auto-refresh rule

Update this matrix when modules are added, ownership changes, a module becomes stable/frozen, a frozen decision is reopened, or a new candidate supersedes an old baseline.
