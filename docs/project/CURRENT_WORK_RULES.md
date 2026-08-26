# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Consolidate the fast-usable development sequence and official-App interaction baseline.
- **User intent / acceptance criteria**: Optimize for the earliest genuinely usable TrollStore IPA; preserve familiar official ChatGPT iOS interaction patterns unless there is an explicit product improvement; include manual latest-message sync, current-conversation reload, Markdown export, reasoning detail UI and double haptic transition; make future development sessions able to continue from durable docs without re-planning.
- **Baseline**: `main@1b277aa01006d43a5f0487d5e5626ead68308a61`; no Active development checkpoints on `main`; no open PRs; planning branch `rules/fast-usable-roadmap-ui-baseline-20260826`.
- **Evidence / reason**: User-provided official ChatGPT iOS interaction recordings plus explicit user correction that `导出 Markdown` in the recording came from the user's injected dylib, not the official app. User explicitly prefers official interaction as the default baseline and wants usable candidates as early as possible.
- **Files in scope**: `docs/project/DEVELOPMENT_PLAN.md`, new durable UI/interaction baseline document, `PROJECT_SPECIFIC_RULES.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_STATE.md`, this rules checkpoint.
- **Do-not-touch**: Product source, completed development branches/checkpoints, build/candidate identities, accepted auth/protocol evidence.
- **Completed**: Verified current governance/router; verified merged b7 read baseline; verified no Active dev checkpoint/open PR on main; created isolated rules branch.
- **Validation state**: Planning/rule documentation in progress; no product code, CI, artifact or runtime result implied.
- **Pending**: Write fast-usable milestones, official-App UI baseline, recovery semantics and candidate cadence; review branch diff; merge planning docs; reset rules checkpoint to Idle.
- **Next exact action**: Update durable roadmap and UI/interaction rules on this branch.
- **Rejected / do-not-repeat**: Do not treat injected `导出 Markdown` as an official-App feature; do not require the whole roadmap to finish before issuing usable IPA candidates; do not invent a separate UI language where the official interaction is already acceptable.
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
