# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Bootstrap the user-provided AI Governance Rules package into `white-shark-ssw/ChatGPT-Client`.
- **User intent / acceptance criteria**: Upload the complete rules package to the current GitHub repository; initialize project-governance state from real repository evidence; do not guess unavailable product facts.
- **Baseline**: `main@91f58c10cb44477b3130527f3037bb4365ea3cf5`; repository contained only empty `占位文件.txt`; no open PRs; only branch `main`.
- **Evidence / reason**: User explicitly supplied `自启动规则包.zip`. Package contains 17 safe relative paths including `AGENTS.md` and `docs/project/START_HERE.md`; SHA-256 `63b581af2611547605a6e9982c5d7145e39189bbdc19bd29bb0c48b62ba0a143`.
- **Files in scope**: The 17 files in the supplied rules package and bootstrap updates within `docs/project/`.
- **Do-not-touch**: Existing `占位文件.txt`; no speculative product source/config creation.
- **Completed**: Read `AGENTS.md` and `START_HERE.md`; routed as Rules; inspected all governance docs; scanned real repository; checked branches/PRs; verified package paths are safe; initialized verified project-state fields while leaving unsupported facts `Unknown / Unverified`.
- **Validation state**: Rule package inspected; GitHub import pending. No product build/test/runtime validation applicable.
- **Pending**: Commit package to `main`, verify uploaded tree/content, then reset this rules checkpoint to Idle.
- **Next exact action**: Create one repository commit importing the package on top of the current `main`, then fetch the resulting files from GitHub for verification.
- **Rejected / do-not-repeat**: Do not infer language/framework/build/CI/version/deployment details from repository name or future intent. Do not remove the existing placeholder file as unrelated cleanup.
- **Open questions / risks**: Product code is not present yet, so project-specific technical fields remain unverified until future source/config is added.

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
