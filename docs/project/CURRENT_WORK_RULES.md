# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Consolidate the fast-usable development sequence and official-App interaction baseline.
- **User intent / acceptance criteria**: Optimize for the earliest genuinely usable TrollStore IPA; preserve familiar official ChatGPT iOS interaction patterns unless there is an explicit product improvement; include manual latest-message sync, current-conversation reload, Markdown export, reasoning detail UI and double haptic transition; make future development sessions able to continue from durable docs without re-planning.
- **Baseline**: `main@1b277aa01006d43a5f0487d5e5626ead68308a61`; no Active development checkpoints on `main`; no open PRs at task start; planning branch `rules/fast-usable-roadmap-ui-baseline-20260826`; PR #8.
- **Evidence / reason**: User-provided official ChatGPT iOS interaction recordings plus explicit user correction that `导出 Markdown` in the recording came from the user's injected dylib, not the official app. User explicitly prefers official interaction as the default baseline and wants usable candidates as early as possible.
- **Files in scope**: `docs/project/DEVELOPMENT_PLAN.md`, `docs/project/UI_INTERACTION_BASELINE.md`, `PROJECT_SPECIFIC_RULES.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_STATE.md`, this rules checkpoint.
- **Do-not-touch**: Product source, completed development branches/checkpoints, build/candidate identities, accepted auth/protocol evidence.
- **Completed**: Verified current governance/router and merged b7 baseline; verified no Active dev checkpoint/open PR on main at task start; created isolated rules branch; rewrote roadmap around V0.1/V0.2/V0.3 usable milestones; documented official-App UI baseline and dylib Markdown correction; documented manual recovery semantics; recorded reasoning shimmer/detail and two-pulse haptic requirement; updated durable product rules/decisions/state; branch diff contained only intended planning docs; opened PR #8.
- **Validation state**: Durable planning/rule docs written and PR #8 opened; no product code, CI, artifact or runtime result implied.
- **Pending**: Re-check current main/base advance and PR mergeability; reset this rules checkpoint to Idle in final branch state; merge PR #8.
- **Next exact action**: Verify `main` has not materially advanced and PR #8 remains docs-only, then finalize the rules checkpoint and merge.
- **Rejected / do-not-repeat**: Do not treat injected `导出 Markdown` as an official-App feature; do not require the whole roadmap to finish before issuing usable IPA candidates; do not invent a separate UI language where the official interaction is already acceptable; do not add automatic resend/retry/watchdog recovery chains.
- **Open questions / risks**: Exact send/stream/reasoning protocol remains Unverified until its dedicated development task; exact haptic intensity/timing must be tuned against real-device behavior rather than guessed from screen recording.

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
