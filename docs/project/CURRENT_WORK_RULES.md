# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Plan conversation round-count display and persist the updated development/UI route.
- **User intent / acceptance criteria**: Add an optional conversation-round count beside the existing conversation type subtitle (`聊天` / `工作`), keep the official-style title layout, and define a small implementation Work that new sessions can pick up without guessing.
- **Baseline**: `main@3f37db66cd5ee36b632497d247c43e5f944737a0`; no open PRs; no Active development checkpoints; accepted production native-read baseline is b9.
- **Evidence / reason**: User screenshot and explicit requirement. `ConversationRepository` already owns the active visible branch, so round count can be derived without a new network request or second state authority.
- **Files in scope**: `docs/project/DEVELOPMENT_PLAN.md`, `docs/project/UI_INTERACTION_BASELINE.md`, `docs/project/PROJECT_SPECIFIC_RULES.md`, `docs/project/PROJECT_STATE.md`, this rules checkpoint.
- **Do-not-touch**: Product source, build/version/candidate identity, development checkpoints.
- **Completed**: Governance and current b9 baseline re-read; planning branch created.
- **Validation state**: Planning/docs only; no product-code validation implied.
- **Pending**: Persist exact round-count semantics, UI placement, settings behavior, task ordering; review diff; open/merge planning PR; return checkpoint to Idle.
- **Next exact action**: Update durable planning/UI documents with `DEV-conversation-round-count`.
- **Rejected / do-not-repeat**: Do not count raw mapping nodes, tool/reasoning/system nodes, or maintain a separately mutable round counter. Do not parallelize against another task that edits the same conversation detail/repository surfaces without a conflict check.
- **Open questions / risks**: Exact visual spacing can be tuned during implementation; counting semantics are planned as active-branch user turns so regenerate does not inflate the count.

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
