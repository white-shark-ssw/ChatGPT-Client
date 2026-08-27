# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Promote persistent conversation-list cache core earlier in the development sequence.
- **User intent / acceptance criteria**: avoid blank cold starts and reduce unnecessary repeated list requests during frequent App restarts; keep full Conversation Detail/body persistence out of this early cache scope.
- **Baseline**: `main` at `ad5ff308fd868ec9abee0747dd6b87a529f8fd13`; planning branch `rules/promote-list-cache-core-20260827`; active development task remains `DEV-multi-conversation-state` on its own branch/checkpoint.
- **Evidence / reason**: current list state is in-memory only; existing cache plan would still issue one automatic list refresh on every cold start, so cache-first presentation alone would not reduce rapid-relaunch request frequency.
- **Files in scope**: durable planning/cache/UI routing docs only.
- **Do-not-touch**: `DEV-multi-conversation-state` product source, checkpoint, Candidate/build/CI/artifact/runtime state.
- **Completed**: governance/startup reads; current plan/cache review; active branch conflict scan; target sequencing decision.
- **Validation state**: Rules planning active; no product code/build/runtime changes.
- **Pending**: document split between early cache core and later preview enhancement; document rapid-relaunch freshness suppression; PR/merge.
- **Next exact action**: update durable development/cache/UI sequencing without touching the active multi-conversation branch.
- **Rejected / do-not-repeat**: do not treat full Conversation Detail/body disk caching as implied; do not use per-row Detail prefetch, polling, retry loops, or present another account's cache before verified scope.
- **Open questions / risks**: exact rapid-relaunch freshness interval should remain an implementation decision until the cache Work starts; manual refresh must always bypass the suppression rule.

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

When complete, move durable rules to permanent files, reset only this file to `Idle`, and do not modify/delete/reset any Active development checkpoint merely to finish rules work.
