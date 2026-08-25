# DEV-foundation-roadmap

## Status

**Active — ready to complete**

- **Work ID**: `DEV-foundation-roadmap`
- **Routing aliases / keywords**: `开发步骤 / 功能规划 / 路线图 / 日志埋点 / foundation roadmap`
- **Task**: Define the implementation sequence for the native iOS ChatGPT client, make diagnostics/logging a first-class foundation requirement, and record the previous Web IPA / Google-login experience with the correct evidence boundary.
- **User intent / acceptance criteria**: Establish a durable development order before product coding; include sufficient structured logging/diagnostic instrumentation from the first executable build; use the previous successful web-login IPA as historical evidence, while revalidating current Google/OpenAI login behavior before depending on it.
- **Baseline**: `main@5e346232cfef0bdb41bab5f6023e89bd8c18a17e`; no product source; no other active development checkpoints; no open PR at task start.
- **Working branch / PR / head commit**: `dev/foundation-roadmap-20260826`; PR #4 `Define native client development roadmap and diagnostics foundation`; PR-open head `65b501f951ae78c30bed338b25d10e05ac185a67`.
- **Candidate identity**: `Not allocated` — planning/documentation task produces no IPA.
- **Evidence**: User explicitly authorized setting the development steps and required logging/instrumentation; user reports prior Web IPA successfully used web login and their account uses Google login. Current Google OAuth documentation warns embedded `WKWebView` authorization can be rejected as `disallowed_useragent`; current OpenAI documentation continues to support Google social authentication. Present behavior must be verified on-device before adopting a login route.
- **Files / modules in scope**: durable final diff should contain `docs/project/DEVELOPMENT_PLAN.md`, `PROJECT_STATE.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_SPECIFIC_RULES.md`, `HISTORICAL_REFERENCE.md`, `BUILD_TEST_INDEX.md`. This checkpoint is temporary and will be deleted before merge.
- **State owner / shared dependencies**: Durable product planning under `docs/project/`; future auth/session state and diagnostics architecture are not implemented yet.
- **Frozen / do-not-touch**: No product code exists; do not invent current ChatGPT private endpoints, auth-cookie transfer behavior, framework APIs, or minimum deployment target.
- **Parallel conflicts checked against**: `docs/project/current/dev/` contained only `README.md`; GitHub had no open PRs at task start; branch compare showed base not advanced and branch behind by 0 before PR open.
- **Completed**: Governance startup/read; real main/PR/checkpoint baseline verified; current Google/OpenAI login policy risk checked; branch/checkpoint created; durable phased roadmap added; logging/diagnostics contract defined; previous Google web-login success recorded with current-evidence boundary; build/log candidate identity rule added; PR #4 opened.
- **Validation state**: Documentation/planning written and branch diff reviewed. No product code/build/CI/artifact/runtime validation applies. Current Google login has not been tested in the new client.
- **Pending**: Delete this checkpoint as the task's completion step; compare final branch against current `main`; verify PR/base/head; squash merge; verify durable docs on `main`.
- **Next exact action**: Delete `docs/project/current/dev/DEV-foundation-roadmap.md`, then run the final compare/merge guard.
- **Rejected / do-not-repeat**: Do not treat historical Web IPA login success as proof current embedded Google OAuth works; do not log cookies/tokens/full chat payloads by default; do not build multiple speculative auth fallbacks before reproducing the current failure/success path; do not start native private-protocol implementation before authenticated-session evidence exists.
- **Open questions / risks**: Current Google sign-in may leave `WKWebView` for a supported browser/system auth context; exact ChatGPT session handoff/cookie behavior must be observed. Exact UIKit/SwiftUI choice and minimum deployment target remain unverified until `DEV-app-foundation`.
