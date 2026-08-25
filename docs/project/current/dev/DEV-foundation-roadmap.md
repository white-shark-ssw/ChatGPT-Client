# DEV-foundation-roadmap

## Status

**Active**

- **Work ID**: `DEV-foundation-roadmap`
- **Routing aliases / keywords**: `开发步骤 / 功能规划 / 路线图 / 日志埋点 / foundation roadmap`
- **Task**: Define the implementation sequence for the native iOS ChatGPT client, make diagnostics/logging a first-class foundation requirement, and record the previous Web IPA / Google-login experience with the correct evidence boundary.
- **User intent / acceptance criteria**: Establish a durable development order before product coding; include sufficient structured logging/diagnostic instrumentation from the first executable build; use the previous successful web-login IPA as historical evidence, while revalidating current Google/OpenAI login behavior before depending on it.
- **Baseline**: `main@5e346232cfef0bdb41bab5f6023e89bd8c18a17e`; no product source; no other active development checkpoints; no open PR at task start.
- **Working branch / PR / head commit**: `dev/foundation-roadmap-20260826`; PR not opened yet; latest durable-doc commit `9b6baecfa40913d2f6e28082191b596a84724527`.
- **Candidate identity**: `Not allocated` — planning/documentation task produces no IPA.
- **Evidence**: User explicitly authorized setting the development steps and required logging/instrumentation; user reports prior Web IPA successfully used web login and their account uses Google login. Current Google OAuth documentation warns embedded `WKWebView` authorization can be rejected as `disallowed_useragent`; current OpenAI documentation continues to support Google social authentication. Present behavior must be verified on-device before adopting a login route.
- **Files / modules in scope**: `docs/project/DEVELOPMENT_PLAN.md` (new), `PROJECT_STATE.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_SPECIFIC_RULES.md`, `HISTORICAL_REFERENCE.md`, `BUILD_TEST_INDEX.md`, this checkpoint.
- **State owner / shared dependencies**: Durable product planning under `docs/project/`; future auth/session state and diagnostics architecture are not implemented yet.
- **Frozen / do-not-touch**: No product code exists; do not invent current ChatGPT private endpoints, auth-cookie transfer behavior, framework APIs, or minimum deployment target.
- **Parallel conflicts checked against**: `docs/project/current/dev/` contained only `README.md`; GitHub had no open PRs at task start.
- **Completed**: Governance startup/read; real main/PR/checkpoint baseline verified; current Google/OpenAI login policy risk checked; branch/checkpoint created; durable phased roadmap added; logging/diagnostics contract defined; previous Google web-login success recorded with current-evidence boundary; build/log candidate identity rule added.
- **Validation state**: Documentation/planning written; no product code/build/CI/artifact/runtime validation applies. Current Google login has not been tested in the new client.
- **Pending**: Compare branch against current `main`; verify no unrelated changes/base advance; open PR; record PR/head; delete this checkpoint only after planning work is ready to complete; merge and verify durable docs on `main`.
- **Next exact action**: Compare `dev/foundation-roadmap-20260826` against `main` and verify the final documentation scope before opening the PR.
- **Rejected / do-not-repeat**: Do not treat historical Web IPA login success as proof current embedded Google OAuth works; do not log cookies/tokens/full chat payloads by default; do not build multiple speculative auth fallbacks before reproducing the current failure/success path; do not start native private-protocol implementation before authenticated-session evidence exists.
- **Open questions / risks**: Current Google sign-in may leave `WKWebView` for a supported browser/system auth context; exact ChatGPT session handoff/cookie behavior must be observed. Exact UIKit/SwiftUI choice and minimum deployment target remain unverified until `DEV-app-foundation`.
