# Current Work — Rules

This is the rolling checkpoint for repository governance, documentation policy, AI instructions and collaboration rules.

## Status

**Active**

- **Task**: Integrate project-level ChatGPT-Notify / Bark completion notification rules.
- **User intent / acceptance criteria**: Adopt the fixed `white-shark-ssw/ChatGPT-Notify` PR #1 / `BARK_NOTIFY_V1` rules for ChatGPT-Client; make the first startup rule require notification handling for every final user-facing reply; keep Bark Key outside this repository; do not modify product code.
- **Baseline**: synchronized to `main@9be1f0bd159887ced2a54c1925dec219ef1c5e01`; rules branch `rules/chatgpt-notify-bark-20260828`; no open ChatGPT-Client PR at preflight.
- **Evidence / reason**: User supplied `快速接入通知仓库.md`; notification hub `BOOTSTRAP.md`, `templates/CHATGPT_NOTIFY_RULES.md` and `templates/PROJECT_RULE_SNIPPET.md` were read from `white-shark-ssw/ChatGPT-Notify`. Bark upstream documentation confirms the `url` parameter opens a specified URL when the notification is tapped; future app deep-link support remains a separate product feature.
- **Files in scope**: `AGENTS.md`, `docs/automation/CHATGPT_NOTIFY_RULES.md`, `docs/project/START_HERE.md`, this rules checkpoint.
- **Do-not-touch**: product source, development checkpoints, build/version/candidate/CI/artifact configuration, Bark Key/secret storage.
- **Completed**: first-startup rule updated; detailed project notification rules added with `ChatGPT-Client`; `START_HERE.md` wired to read them; branch resynchronized after `main` advanced by unrelated cache-core closeout commits.
- **Validation state**: Rules documented on branch; no product Code/CI/Artifact/Runtime changes.
- **Pending**: final diff review, open/merge rules PR, verify merged files, reset this checkpoint to Idle, then execute the newly installed completion-notification sequence for this final reply.
- **Next exact action**: Compare rules branch against current `main`; if only intended governance files differ, open PR and merge.
- **Rejected / do-not-repeat**: Bark Key in business repo; guessing GitHub comment tools; notification payload containing auth secrets/private download URLs; treating notification delivery as CI/runtime/stability proof; product-code changes during this rules task.
- **Open questions / risks**: Current `BARK_NOTIFY_V1` project payload still uses `url=https://chatgpt.com/`. Future `ChatGPT-Client` deep-link routing could replace that with an app URL only after the client has a real routed deep-link contract; do not represent it as implemented now.

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
