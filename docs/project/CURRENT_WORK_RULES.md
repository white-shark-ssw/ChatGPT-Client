# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: 将“上一轮回答 / 下一轮回答”快速滚动导航及其设置开关纳入开发路线，并确定与当前多会话滚动锚点、未来 Send/Stream follow-tail 的交互边界。
- **User intent / acceptance criteria**: 会话页提供可选快速跳转控件；根据用户最近的实际滑动方向显示上一轮或下一轮回答方向；点击后以可见动画滚动到目标回答起点而非瞬移；设置中可关闭；按钮位置不遮挡正文与未来 composer；不破坏多会话独立滚动位置。
- **Baseline**: `main@2c33dacbefa613292eb89cbf606b0172a241e81e`; rules branch `rules/turn-jump-plan-20260827`; active development branch `dev/multi-conversation-state-20260827@ca2a18224d4fa10d724380144a21532f3c574da6` remains independently owned.
- **Evidence / reason**: b18 has real-device accepted per-conversation semantic scroll restoration, so quick answer navigation should consume the same conversation presentation surface rather than create a second scroll owner. Current round-count plan already derives active-branch turns and establishes the first centralized preference owner.
- **Files in scope**: `DEVELOPMENT_PLAN.md`, `UI_INTERACTION_BASELINE.md`, this rules checkpoint.
- **Do-not-touch**: active multi-conversation checkpoint/branch/product code, b18 Candidate/Artifact/runtime evidence, overlapping `PROJECT_STATE` / `MODULE_STATUS` / `PROJECT_SPECIFIC_RULES` / `CLIENT_ARCHITECTURE_GAP_REVIEW` currently modified by the active development branch.
- **Completed**: governance startup; main/head/open-PR and active multi-conversation head checked; conflict scan shows `DEVELOPMENT_PLAN.md` and `UI_INTERACTION_BASELINE.md` are not modified by the active branch; interaction direction selected.
- **Validation state**: Planning only; no product Code/CI/Artifact/Runtime changes.
- **Pending**: persist exact answer-anchor semantics, adaptive button placement/direction, animated scrolling and settings ownership; review diff; reset rules checkpoint to Idle; open/merge planning PR.
- **Next exact action**: update the two non-overlapping durable planning/UI documents on this rules branch only.
- **Rejected / do-not-repeat**: two always-visible large buttons covering content; raw pixel jump/instant `contentOffset` teleport; timer-driven auto-hide/watchdog; per-cell/per-screen preference keys; scanning the full long conversation on every scroll event; using this rules session to modify b18 product code.
- **Open questions / risks**: exact default of the new toggle remains unfrozen; active-stream/follow-tail integration belongs to future real Send/Stream owner and must not be guessed into b18.

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
