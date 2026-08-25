# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | Stable | `AppDelegate.swift`, `RootViewController.swift`, `SettingsViewController.swift`; `DEV-app-foundation-0.1.0-b1` | Swift/UIKit baseline real-device tested on iPhone / iOS 17.0. Auth task changes remain limited to evidence-backed verification UI. Not Frozen. |
| Build/runtime metadata | Stable | `AppBuildInfo.swift`, Xcode target settings, `Info.plist` | Exact candidate/source/deployment/runtime identity is embedded in test candidates. Current auth runtime evidence candidate is b3/build 3. Not Frozen. |
| Diagnostics / logging | Stable | `ChatGPTClient/Diagnostics/Diagnostics.swift`; `DEV-app-foundation-0.1.0-b1` | Structured OSLog + bounded rolling JSONL + trace/span + secret filtering + redacted export. Auth uses the same authority. Not Frozen. |
| IPA build / CI packaging | Stable | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml` | b3 push run `32889095904` passed and produced artifact ID `9578766019`, IPA SHA-256 `b377d3f085d1877c16baf79d3969af21d5345517261b6eda87a7637aef292860`. Not Frozen. |
| Embedded web login | Stable | `AuthWebViewController.swift`; b2 runtime evidence | Continue with Google succeeded on iPhone / iOS 17.0. Force-close/relaunch retained authenticated WebKit state; diagnostics corroborated direct `/auth/login` -> logged-in `chatgpt.com`. Default persistent `WKWebsiteDataStore` is the current persistent auth-secret authority. No browser fallback justified. Not Frozen. |
| Authentication evidence / native session bridge | Stable | `AuthSessionStore.swift`; `DEV-auth-bootstrap-0.1.0-b3` | Real-device b3 test on iPhone / iOS 17.0 reached `session.nativeState=verified`; transient WebKit ChatGPT/OpenAI cookies in an ephemeral native `URLSession` resolved `/auth/login` to `chatgpt.com` HTTP 200. The bridge persists no copied auth secrets. Stable only for this tested session-consumption scope; not proof of conversation/private protocol. Not Frozen. |
| Account / workspace context | Unknown / Unverified | Current `DEV-auth-bootstrap` continuation | Current account/workspace identity/context, endpoint/shape and explicit owner required by later native requests have not yet been established. |
| ChatGPT protocol / conversation / streaming / attachments | Unknown / Unverified | Future development tasks | Not implemented; historical protocol material remains reference-only. |

## Allowed statuses

Use concise statuses such as Active, Candidate, Stable, Frozen, Experimental, Deprecated, or Unknown / Unverified.

## Frozen rule

Before changing a Frozen or Stable core module for an unrelated task, verify that the current task truly requires it and record the concrete reason/evidence. Stable does not mean Frozen.

## Current acceptance boundary

- `DEV-app-foundation-0.1.0-b1`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; foundation Stable, not Frozen.
- `DEV-auth-bootstrap-0.1.0-b2`: same evidence level for embedded Google login and WebKit session persistence on iPhone / iOS 17.0; web-login/persistence Stable, not Frozen.
- `DEV-auth-bootstrap-0.1.0-b3`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** for the transient native session bridge to the tested `/auth/login` route. Screenshot and diagnostics corroborate `session.nativeState=verified`, final `chatgpt.com` HTTP 200. This does not promote account/workspace context or private protocol, which remain Unknown / Unverified.

Runtime compatibility below iOS 17.0 and on iPad remains unverified.

## Auto-refresh rule

Update this matrix when modules are added, ownership changes, a module becomes stable/frozen, a frozen decision is reopened, or a new candidate supersedes an old baseline.
