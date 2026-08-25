# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Record the current product direction as an iOS native ChatGPT client and preserve the user-provided historical project pack as reference-only project knowledge.
- **User intent / acceptance criteria**: Treat the current project as development of an iOS native ChatGPT client. Use `ChatGPT_iOS_Native_Client_History_Pack_2026-08-25.zip` as prior-project experience/reference, not as current source truth.
- **Baseline**: `main@f4ba767fde90c0258da19a92283e9f337532ca35`; no product source yet; no active Development/Feature checkpoints; no open PRs.
- **Evidence / reason**: User explicitly stated the current project theme. Historical pack SHA-256: `571c6d100091792a85917c6451fb1b6d7d430b3eeaf798b8724a9bd7b90c3b98`; 22 files inspected, with high-value summaries covering native architecture, long-conversation performance, auth/network, attachments, do-not-repeat routes, and MVP acceptance.
- **Files in scope**: `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, `PROJECT_SPECIFIC_RULES.md`, `TECHNICAL_DECISIONS.md`, new historical-reference summary, and this Rules checkpoint.
- **Do-not-touch**: Product source/code, development checkpoints, build/test candidate records, and unverified language/framework/build details.
- **Completed**: Read `AGENTS.md`, `START_HERE.md`, router and project state; routed as Rules; checked active dev checkpoints/PRs/branches; inspected the history pack and separated current user requirements from historical suggestions.
- **Validation state**: Documentation/rule update in progress; no product build/test/runtime validation applicable.
- **Pending**: Write durable project-context updates, compare branch to `main`, open/merge PR, verify final `main`, reset this checkpoint to Idle.
- **Next exact action**: Update project profile/state/rules/technical decisions and add a concise historical reference summary on `rules/ios-native-project-context-20260825`.
- **Rejected / do-not-repeat**: Do not treat old private ChatGPT endpoint names, old WebView code, historical architecture suggestions, or old diagnoses as current API contracts or current implementation facts.
- **Open questions / risks**: Product language/framework and authentication/protocol details remain unverified until current source/traffic evidence exists.

## Active task template

When a multi-step rules task starts, switch to `Active` early and maintain:

- **Task**
- **User intent / acceptance criteria**
- **Baseline**: rule files / branch / PR / commit
- **Evidence / reason**
- **Files in scope**
- **Do-not-touch**
- **Completed**
- **Validation state**: Rule drafted / documented / PR opened / merged
- **Pending**
- **Next exact action**
- **Rejected / do-not-repeat**
- **Open questions / risks**

## Proactive checkpoint rule

The conversation/context limit is unpredictable. Once the rules problem and usable direction are clear, establish an Active checkpoint. Refresh at meaningful rule decisions, permanent-rule edits, PR state changes, or direction changes.

## Completion

When complete, move durable rules to permanent rule files, reset only this file to `Idle`, and do not modify/delete/reset any Active development checkpoint merely to finish rules work.
