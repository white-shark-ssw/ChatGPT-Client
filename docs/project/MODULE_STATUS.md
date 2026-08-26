# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | Stable | `AppDelegate.swift`, `RootViewController.swift`, `SettingsViewController.swift`; `DEV-app-foundation-0.1.0-b1` | Swift/UIKit baseline real-device tested on iPhone / iOS 17.0. Auth task changes remain limited to evidence-backed verification UI. Not Frozen. |
| Build/runtime metadata | Stable | `AppBuildInfo.swift`, Xcode target settings, `Info.plist` | Exact candidate/source/deployment/runtime identity is embedded in test candidates. Current account-context candidate is b5/build 5. Not Frozen. |
| Diagnostics / logging | Stable | `ChatGPTClient/Diagnostics/Diagnostics.swift`; `DEV-app-foundation-0.1.0-b1` | Structured OSLog + bounded rolling JSONL + trace/span + secret filtering + redacted export. Auth uses the same authority. Not Frozen. |
| IPA build / CI packaging | Stable | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml` | b5 push run `32932389742` passed; artifact ID `9593649485`; IPA SHA-256 `d9a22635cc6ac05d2ba09a0a627eaa74d38d1a690b5e9affe2f318d2aa204f15`. Embedded candidate/source/build were locally rechecked. Not Frozen. |
| Embedded web login | Stable | `AuthWebViewController.swift`; b2 + b4 runtime evidence | Continue with Google and persistence are accepted. b4 additionally shows WebKit can pass a Cloudflare challenge and still reach authenticated non-`/auth` `chatgpt.com` HTTP 200. Default persistent `WKWebsiteDataStore` remains the persistent auth-secret authority. Not Frozen. |
| Authentication evidence / native `/auth/login` bridge | Stable | `AuthSessionStore.swift`; b3/b4 evidence | b3 proved the transient cookie-copy `URLSession` could resolve `/auth/login` under its tested conditions. b4 later showed the same route can return Cloudflare HTTP 403 even while WebKit is authenticated. Therefore this remains historical route-specific evidence but is no longer a prerequisite gate or session authority. Not Frozen. |
| Account / workspace context | Candidate | `AuthSessionStore.swift`; `DEV-auth-bootstrap-0.1.0-b5` | b5 directly probes `/api/auth/session` after authenticated WebKit navigation, logs only safe cookie counts, then uses a transient bearer for accounts-check. Code written + CI passed + Artifact produced; runtime pending. |
| ChatGPT protocol / conversation / streaming / attachments | Unknown / Unverified | Future development tasks | Not implemented; historical protocol material remains reference-only. |

## Allowed statuses

Use concise statuses such as Active, Candidate, Stable, Frozen, Experimental, Deprecated, or Unknown / Unverified.

## Frozen rule

Before changing a Frozen or Stable core module for an unrelated task, verify that the current task truly requires it and record the concrete reason/evidence. Stable does not mean Frozen.

## Current acceptance boundary

- `DEV-app-foundation-0.1.0-b1`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; foundation Stable, not Frozen.
- `DEV-auth-bootstrap-0.1.0-b2`: same evidence level for embedded Google login and WebKit session persistence on iPhone / iOS 17.0.
- `DEV-auth-bootstrap-0.1.0-b3`: same evidence level for transient native `/auth/login` success under its tested conditions; later b4 evidence limits that conclusion and prevents using the route as a durable gate.
- `DEV-auth-bootstrap-0.1.0-b4`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** with result `session.webState=authenticated` but native `/auth/login` HTTP 403 / `session.nativeState=notAuthenticated`; account probe never ran.
- `DEV-auth-bootstrap-0.1.0-b5`: **Code written + CI passed + Artifact produced; Runtime/manual/real-device not yet tested** for direct account-context acquisition.

Runtime compatibility below iOS 17.0 and on iPad remains unverified.

## Auto-refresh rule

Update this matrix when modules are added, ownership changes, a module becomes stable/frozen, a frozen decision is reopened, or a new candidate supersedes an old baseline.
