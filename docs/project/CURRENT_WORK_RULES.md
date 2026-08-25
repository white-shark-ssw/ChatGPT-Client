# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Record TrollStore IPA distribution and iOS compatibility constraints.
- **User intent / acceptance criteria**: The native iOS ChatGPT client is installed as an IPA through TrollStore; target user systems do not exceed iOS 17.0; compatibility should extend to the lowest practical iOS version rather than setting 17.0 as the deployment target.
- **Baseline**: `main@bf71cb1152c2b114559af0ae1d74384566cc2a64`; no active Development/Feature checkpoints; no open PRs.
- **Evidence / reason**: User explicit requirement in the current conversation on 2026-08-25.
- **Files in scope**: `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, `PROJECT_SPECIFIC_RULES.md`, `TECHNICAL_DECISIONS.md`, `BUILD_TEST_INDEX.md`, and this Rules checkpoint.
- **Do-not-touch**: Product code, Development/Feature checkpoints, historical reference evidence, and unrelated governance files.
- **Completed**: Read required repository governance/project documents; routed as Rules; verified current branch/PR/development-task baseline; created `rules/ios-trollstore-compat-20260825` from current `main`.
- **Validation state**: Documentation/rule update in progress; no product build/CI/runtime validation applies yet because no product source/Xcode project exists.
- **Pending**: Record the durable runtime/distribution constraints, verify branch diff, open/merge PR, then reset this checkpoint to Idle.
- **Next exact action**: Update the durable project documents to distinguish the iOS 17.0 target-environment ceiling from the future minimum deployment target and record TrollStore IPA distribution.
- **Rejected / do-not-repeat**: Do not interpret “iOS system highest <= 17.0” as “deployment target = iOS 17.0”. Do not guess an exact minimum iOS version before current source/toolchain/API requirements can be validated.
- **Open questions / risks**: Exact minimum deployment target remains Unknown / Unverified until implementation dependencies and runtime behavior are known.

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
