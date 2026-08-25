# Module Status

| Module | Status | Owner / baseline | Notes |
|---|---|---|---|
| Repository AI governance | Active | `AGENTS.md` + `docs/project/` | Governance bootstrap remains authoritative. |
| Native application shell | Stable | `AppDelegate.swift`, `RootViewController.swift`, `SettingsViewController.swift`; `DEV-app-foundation-0.1.0-b1` | Swift/UIKit baseline real-device tested on iPhone / iOS 17.0. Auth task changes remain limited to evidence-backed verification UI. Not Frozen. |
| Build/runtime metadata | Stable | `AppBuildInfo.swift`, Xcode target settings, `Info.plist` | Exact candidate/source/deployment/runtime identity is embedded in test candidates. b3 is the accepted runtime auth evidence candidate; b4/build 4 is the current identity-correct account-context test candidate. Not Frozen. |
| Diagnostics / logging | Stable | `ChatGPTClient/Diagnostics/Diagnostics.swift`; `DEV-app-foundation-0.1.0-b1` | Structured OSLog + bounded rolling JSONL + trace/span + secret filtering + redacted export. Auth uses the same authority. Not Frozen. |
| IPA build / CI packaging | Stable | `scripts/build_ipa.sh`, `.github/workflows/ios-foundation.yml` | Identity-correct b4 push run `32891798350` passed and produced artifact ID `9579720453`, IPA SHA-256 `f918b1f5762458e55e89a1f0d23e5c2bf46be11d7f4599c692627a07043dab03`. Earlier artifact `9579620441` is rejected because embedded candidate remained b3. Not Frozen. |
| Embedded web login | Stable | `AuthWebViewController.swift`; b2 runtime evidence | Continue with Google succeeded on iPhone / iOS 17.0. Force-close/relaunch retained authenticated WebKit state; diagnostics corroborated direct `/auth/login` -> logged-in `chatgpt.com`. Default persistent `WKWebsiteDataStore` is the current persistent auth-secret authority. No browser fallback justified. Not Frozen. |
| Authentication evidence / native session bridge | Stable | `AuthSessionStore.swift`; `DEV-auth-bootstrap-0.1.0-b3` | Real-device b3 test on iPhone / iOS 17.0 reached `session.nativeState=verified`; transient WebKit ChatGPT/OpenAI cookies in an ephemeral native `URLSession` resolved `/auth/login` to `chatgpt.com` HTTP 200. The bridge persists no copied auth secrets. Stable only for this tested session-consumption scope; not proof of conversation/private protocol. Not Frozen. |
| Account / workspace context | Candidate | `AuthSessionStore.swift`; `DEV-auth-bootstrap-0.1.0-b4` | Minimal in-memory account-context owner/probe is Code written + CI passed + Artifact produced. Valid b4 artifact ID `9579720453` embeds candidate b4/source `33ea1b96f755`. Runtime response shape, bearer acceptance, default-account extraction and workspace semantics remain unverified until exact b4 device test. |
| ChatGPT protocol / conversation / streaming / attachments | Unknown / Unverified | Future development tasks | Not implemented; historical protocol material remains reference-only. |

## Allowed statuses

Use concise statuses such as Active, Candidate, Stable, Frozen, Experimental, Deprecated, or Unknown / Unverified.

## Frozen rule

Before changing a Frozen or Stable core module for an unrelated task, verify that the current task truly requires it and record the concrete reason/evidence. Stable does not mean Frozen.

## Current acceptance boundary

- `DEV-app-foundation-0.1.0-b1`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested**; foundation Stable, not Frozen.
- `DEV-auth-bootstrap-0.1.0-b2`: same evidence level for embedded Google login and WebKit session persistence on iPhone / iOS 17.0; web-login/persistence Stable, not Frozen.
- `DEV-auth-bootstrap-0.1.0-b3`: **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** for the transient native session bridge to the tested `/auth/login` route. Screenshot and diagnostics corroborate `session.nativeState=verified`, final `chatgpt.com` HTTP 200.
- `DEV-auth-bootstrap-0.1.0-b4`: **Code written + CI passed + Artifact produced; Runtime/manual/real-device not yet tested** for account-context acquisition. Therefore account/workspace remains Candidate, not Stable.

Runtime compatibility below iOS 17.0 and on iPad remains unverified.

## Auto-refresh rule

Update this matrix when modules are added, ownership changes, a module becomes stable/frozen, a frozen decision is reopened, or a new candidate supersedes an old baseline.
