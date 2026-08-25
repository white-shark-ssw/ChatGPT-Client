# DEV-app-foundation

## Status

**Active**

- **Work ID**: `DEV-app-foundation`
- **Routing aliases / keywords**: `应用基础与日志系统 / 应用基础 / 日志系统 / diagnostics / app foundation`
- **Task**: 建立首个真实 iOS 原生应用基线、可审计构建身份与安全的本地结构化日志/诊断导出能力。
- **User intent / acceptance criteria**: 按 `DEVELOPMENT_PLAN.md` Phase 1 执行；产出最小真实 Xcode/iOS 应用骨架，建立可供 TrollStore 安装验证的 IPA 打包路径，从第一版即可记录有界持久化结构化日志并由用户主动导出脱敏诊断；不得把构建成功描述成实机通过。
- **Baseline**: base `main@bd9727e7a20c48c88944eff8a0f5fd0d23925ff6`; repository has no product source at this baseline.
- **Working branch / PR / head commit**: `dev/app-foundation-20260826`; PR not created; initial head equals baseline until this checkpoint commit.
- **Candidate identity**: Not allocated. Product version/build/candidate scheme must be established from this task before the first IPA artifact is claimed.
- **Evidence**: User explicitly started new development task `应用基础与日志系统`; `DEVELOPMENT_PLAN.md` names `DEV-app-foundation` as Phase 1; `TD-004` and `PROJECT_SPECIFIC_RULES.md` require diagnostics from the first executable build; real `main` and repository tree verified on 2026-08-26.
- **Files / modules in scope**: new Xcode project/application target; app shell/settings/build metadata; diagnostics event/logger/store/export; build/package scripts/config; narrow CI/build validation if added; corresponding `docs/project/` truth updates.
- **State owner / shared dependencies**: app lifecycle owner; diagnostics/log store owner; build/version/candidate identity. No ChatGPT auth/session/protocol state is in scope.
- **Frozen / do-not-touch**: no Frozen product modules exist; do not implement auth/private protocol/chat features in this task; do not weaken repository governance or logging privacy contract.
- **Parallel conflicts checked against**: `docs/project/current/dev/` contains no other Active checkpoint; no duplicate branch/candidate identity; old `dev/foundation-roadmap-20260826` branch is completed planning history and is not reused.
- **Completed**: startup governance read; current baseline/tree verified; new-task parallel preflight passed; branch created.
- **Validation state**: Governance/baseline checks only. Product code not yet written; no static/local Xcode check, CI, artifact, or runtime evidence yet.
- **Pending**: establish concrete Swift/UI framework/deployment target from the smallest implementation; create app + diagnostics; establish version/build/candidate scheme; add reproducible build/package path; run available validation; update durable docs.
- **Next exact action**: inspect compatibility/build constraints needed by the minimal implementation, then add the smallest Swift/UIKit app target and diagnostics foundation on `dev/app-foundation-20260826`.
- **Rejected / do-not-repeat**: do not inherit historical WebView chat runtime; no speculative retry/watchdog/fallback/remote telemetry; no auth secrets/full chat content in logs; do not default deployment target to iOS 17.0 merely because that is the environment ceiling.
- **Open questions / risks**: exact installed Xcode/toolchain and real-device TrollStore behavior cannot be proven from repository state alone; bundle identity/signing details are not yet user-specified; artifact/runtime claims require build/device evidence.
