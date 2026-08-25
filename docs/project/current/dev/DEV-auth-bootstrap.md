# DEV-auth-bootstrap

## Status

**Active**

- **Work ID**: `DEV-auth-bootstrap`
- **Routing aliases / keywords**: `网页登录 / Google 登录 / Google 登录验证 / 登录验证 / auth bootstrap`
- **Task**: Reproduce and verify the current ChatGPT web login path, specifically Continue with Google, on-device before native private-protocol work.
- **User intent / acceptance criteria**: Provide a testable iOS path that can open current ChatGPT web login, attempt Continue with Google, preserve privacy-safe auth/navigation diagnostics, and establish real-device evidence of whether login succeeds or what current blocking/failure behavior occurs. Do not claim authenticated native protocol access until separately evidenced.
- **Baseline**: `main` at `836651a41e36feafcc2386939d70d673be6e3725`; accepted runtime foundation `DEV-app-foundation-0.1.0-b1`, version `0.1.0 (1)`, TrollStore tested on iPhone / iOS 17.0.
- **Working branch / PR / head commit**: `dev/auth-bootstrap-20260826`; PR not created; branch starts at `836651a41e36feafcc2386939d70d673be6e3725`.
- **Candidate identity**: Not allocated. Next available build/candidate must be checked immediately before artifact production.
- **Evidence**: Current project docs require auth verification before protocol work. Historical user evidence says a prior Web-based IPA could sign in and the account uses Continue with Google; this is not a current runtime contract.
- **Files / modules in scope**: Authentication/session bootstrap UI and state; minimal application-shell integration required to enter/exit login; existing diagnostics authority for privacy-safe auth/navigation evidence; build/project metadata only if required for a test candidate.
- **State owner / shared dependencies**: New authentication/session bootstrap owner to be established by this task; depends on Stable application shell and Stable diagnostics foundation.
- **Frozen / do-not-touch**: No modules are Frozen. Stable foundation modules may change only where current auth requirements justify it. Do not implement native ChatGPT private protocol in this task.
- **Parallel conflicts checked against**: `docs/project/current/dev/` contained no Active DEV checkpoint at task creation; no branch/candidate conflict found. Core roadmap serial dependency is foundation -> auth -> protocol read.
- **Completed**: Session routed as Development/Feature; repository governance/current state read; no Active task checkpoint existed; `main` head verified; dedicated branch created; checkpoint established early.
- **Validation state**: Governance/baseline evidence verified only. No auth code written, CI run, artifact, or current real-device login result yet.
- **Pending**: Inspect real application shell/diagnostics/build source; inspect current authoritative OpenAI/Google web-login constraints as needed; implement the smallest evidence-driven web-login bootstrap; run CI/build; allocate a unique candidate before artifact; real-device test Continue with Google and capture redacted diagnostics.
- **Next exact action**: Inspect `AppDelegate.swift`, `RootViewController.swift`, `SettingsViewController.swift`, `Diagnostics.swift`, Xcode project/Info.plist and current CI/build script on this branch, then choose the minimum login bootstrap integration point without speculative fallback routes.
- **Rejected / do-not-repeat**: Do not assume old WebView login still works; do not assume WebKit/system-browser/URLSession sessions are interchangeable; do not log passwords, OAuth codes, tokens, Cookie or Authorization values; do not prebuild fallback chains; do not begin private-protocol implementation before current authenticated-session evidence.
- **Open questions / risks**: Current Google OAuth may reject embedded user-agents; current ChatGPT auth navigation/cookie behavior is not yet runtime-verified; whether a system-browser/auth-session handoff is required must be decided from current failure evidence rather than assumption.
