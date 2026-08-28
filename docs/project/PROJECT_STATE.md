# Project State

_Last updated: 2026-08-29 through exact b35 Runtime result and exact b36 Code/Static/CI/Artifact/current-main merge-view evidence._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone/iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic read evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: merged Stable production native-read baseline.
- `DEV-conversation-recovery-0.1.0-b15`: merged Stable recovery baseline; PR #10.
- `DEV-multi-conversation-state-0.1.0-b21`: merged Stable multi-conversation read-state baseline; PR #23.
- `DEV-conversation-list-cache-core-0.1.0-b23`: merged Stable list-cache-core baseline; PR #24.

The merged accepted read/cache baseline remains b23. `DEV-conversation-round-count` is the current Active Work layered on it and is not Stable/Frozen.

## Active development — DEV-conversation-round-count

- **Branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open/mergeable, not merged.
- **Current main at b36 validation**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- **Latest tested Candidate**: b35, Runtime partial/failing.
- **Current Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b36`, `0.1.0 (36)`; Runtime pending.
- **Exact b36 product/config source**: `8f8614508eef5197f9fff4bb9d10c14354d5821e`. Later docs/checkpoint commits do not redefine this source.
- **Scope**: compact title-first metadata, active-branch round count, authoritative historical timestamps, visible-text Copy, adaptive previous/next round navigation, centralized persisted Preferences, first-entry latest placement and evidence-backed list/detail presentation corrections.
- **Authority boundary**: `ConversationRepository` remains sole conversation/list authority. `AppPreferences` owns persisted presentation booleans only. `ConversationRoundProjection` is derived from authoritative visible messages and is not mutable conversation authority. Round-jump feedback/animator are presentation-only inside `ConversationDetailViewController`.

## Candidate progression

- **b24**: package identity rejected/permanently reserved.
- **b25-b30**: Runtime partial/failing iterations that established accepted Copy/time/preferences, compact header, bounded list reconciliation, right-top refresh correction and automatic message self-sizing while exposing navigation defects.
- **b31**: Runtime partial/failing. User-message semantic round-start targeting produced precise landing; hitch/internal-row/Copy defects remained.
- **b32**: Runtime partial/failing. Accepted recipient/tool filtering, compact Copy direction and precise semantic landing; rejected long-jump smoothness and physical-bottom rubber-band direction.
- **b33**: Runtime partial/failing. Physical-bottom direction and final semantic precision accepted; long-distance/rapid jump smoothness rejected.
- **b34**: Runtime partial/failing. Tested trace had 42 requested / 42 completed jumps, 0 landing corrections and 0 ignored completions, yet movement feel remained rejected; the old final-correction snap was therefore not the remaining tested cause.
- **b35**: Runtime partial/failing. Unified direct-position + 120pt/0.22s ease-out removed full-distance traversal and retained precise completed landings, but several-second tap-to-position stalls remained around long-message regions.
- **b36**: Code/source audit/CI/Artifact/current-main merge-view complete; Runtime pending.

## Exact b35 Runtime evidence

- Candidate `DEV-conversation-round-count-0.1.0-b35`, `0.1.0 (35)`; exact source `c3addf775483de17a0a0a9eb81d602fc18ebe611`.
- Push Run / Job `33203663621` / `98959137672`; Runtime Artifact `9698781544`; ZIP `sha256:903b2e51608af144097f2880d1bbb301de29d8b4a21477a74d16523e26bc473d`; IPA SHA `b1391d06f81bc8c57d124e16a22ef138dd8151e0bd8e338db601729c6f583b0f`.
- User-tested exact b35 on iPhone/iOS17; supplied diagnostics metadata identifies build 35, Candidate b35 and source `c3addf775483`.
- Completed jumps that finish report `landingErrorPoints=0.00` and `leadDistancePoints=120.00`.
- Blocking Runtime defect: some accepted taps appear frozen for several seconds, especially around long-message regions; user explicitly requires immediate visual feedback whenever positioning is not immediate.
- Trace contains 52 `answerJump.requested` / 36 `answerJump.completed`; suspicious request-to-next-interaction gaps include about 4s, 10s and 8s.
- b35 source logs the request before synchronous main-thread `view.layoutIfNeeded() -> tableView.layoutIfNeeded() -> scrollToRow(false) -> tableView.layoutIfNeeded()`. Rows are UIKit self-sizing Auto Layout with multiline UILabel. Exact Runtime + source therefore justified removing explicit forced jump preparation before introducing any geometry cache.

## Exact b36 product correction

- Candidate `DEV-conversation-round-count-0.1.0-b36`, `0.1.0 (36)`.
- Exact product/config source `8f8614508eef5197f9fff4bb9d10c14354d5821e`.
- Parent→product diff from checkpoint head `c6c21e0f1d032c28451f36506cd4c90936dba1cb` is exactly three files:
  - workflow identity b35→b36: 2 additions / 2 deletions;
  - Xcode build/Candidate 35→36: 4 additions / 4 deletions;
  - `ConversationFeature.swift`: 25 additions / 6 deletions.
- Jump handler no longer calls root/table `layoutIfNeeded()` around direct target positioning.
- It reuses the existing quick-navigation button for immediate `定位中` / accessibility `正在定位` presentation; only that button/layer is flushed. There is no second status/state owner.
- It retains exactly one nonanimated `scrollToRow(..., .top, animated:false)`, then the same direction lead of about 120pt and about 0.22s ease-out to the captured final offset.
- New `answerJump.positioned` diagnostics record privacy-safe `directPositionDurationMs`, `preparationDurationMs`, `targetVisible`, row/role and presentation mode only.
- No row-height cache, retry, timer, watchdog, alternate semantic index, list/network change or rendering change was added.
- Accepted physical-bottom direction, semantic user-message round targets, recipient filtering, Copy/timestamps/preferences/header, list/cache/network ownership and Sync/Reload remain unchanged.

## Exact b36 CI / Artifact

- Push Run / Job `33207505424` / `98972194770` — success on exact `head_sha=8f8614508eef5197f9fff4bb9d10c14354d5821e`.
- Exact Runtime Artifact `9700254733`; Artifact name `ChatGPTClient-DEV-conversation-round-count-0.1.0-b36`.
- Artifact ZIP digest `sha256:718e8500ea41bcc73b41f5bebd9a4850b93246368a87304be0b2c4751702e576`.
- IPA `ChatGPTClient-0.1.0-b36-dev-conversation-round-count.ipa`; SHA `cdf2c7278ec0a4f6f5125a711f78d7bbda8c606a32dda87f614d710f662bd867`.
- Independent package inspection matches `0.1.0 (36)`, Candidate b36, source marker `8f8614508eef`, MinimumOSVersion 14.0, bundle `com.whitesharkssw.chatgptclient`, Mach-O arm64.

## Current-main merge-view evidence

- Main remained `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- PR #27 remains open, mergeable and not merged.
- PR Run / Job `33207508869` / `98972206567`, success.
- GitHub synthetic merge `e7ff5b368faaea3debbe5d5547c0424996653fa0` explicitly merges exact b36 source `8f861450...` into `main@a6e3b2...`.
- Merge-view output is CI evidence only and never replaces exact Runtime Artifact `9700254733`.

## Rendering scope observation

The supplied official-app/current-client recording shows raw Markdown syntax in this client where the official app renders headings, bold, inline code and tables. Current source simply concatenates `content.text`/string `parts` and assigns the result to `UILabel.text`; no Markdown/rich-annotation renderer exists.

This work belongs to future `DEV-message-rendering`, not current Phase 8. Boxed-question-mark glyphs adjacent to raw `filecite ...` text appear to require citation/rich-content rendering evidence rather than a Phase 8 font workaround; do not strip speculatively.

## Current architecture / ownership

- `AppDelegate`: lifecycle + accepted WebKit warm-up sequencing.
- `RootViewController`: compact list/detail navigation owner.
- `ConversationRepository`: sole authoritative conversation/list/read/recovery owner.
- `ConversationListCacheStore`: storage-only persistent summary snapshot + privacy-safe last-verified scope hint.
- `ConversationDetailViewController`: Detail/recovery presentation, semantic anchors, first-entry latest placement and round navigation presentation.
- `ConversationMessageCell`: plain visible message/timestamp/assistant-Copy presentation; UIKit self-sizing; no Markdown renderer yet.
- `ConversationSidebarViewController`: list presentation; b29 accepted right-top refresh blank-region correction.
- `AppPreferences`: centralized persisted display/interaction preference owner.
- `ConversationRoundProjection`: derived active-branch round projection; no second mutable semantic index.
- `DiagnosticsLogger`: structured privacy-safe diagnostics authority.
- default persistent `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: sole verified auth/account-context owner.

## Current Runtime gate

Install/test exact Runtime Artifact `9700254733` / b36 IPA SHA `cdf2c7278ec0a4f6f5125a711f78d7bbda8c606a32dda87f614d710f662bd867` on the accepted iPhone/iOS17 scope.

Acceptance focus:

1. Repeat b35 long-message regions; tap-to-position several-second stalls should disappear or materially reduce.
2. If direct positioning is not immediate, the existing round button must visibly show `定位中` so the accepted tap is unmistakable.
3. If any stall remains, inspect/export `answerJump.positioned.directPositionDurationMs` / `preparationDurationMs` to determine whether the remaining cost is the direct `scrollToRow(false)` operation itself.
4. Final semantic landing remains precise at the intended user-message round start.
5. Rapid taps remain one semantic round per tap; real drag immediately retakes ownership.
6. Physical-bottom/rubber-band direction and recipient/tool filtering, Copy, first-entry latest, A/B anchors, timestamps/preferences, list reconcile and Sync/Reload remain intact.

Do not merge/close PR #27 or claim Stable until exact b36 Runtime is accepted. If b36 proves direct positioning itself is still multi-second, record that evidence first and allocate b37; never rebuild b36.

## Evidence boundaries

- b35 Runtime is partial/failing; b36 Runtime is Pending.
- iOS17 success does not prove iOS14–16 or iPad.
- Read/recovery/multi-conversation/cache evidence is primarily Plus/personal; non-personal workspace identity remains Unknown/Unverified.
- Supported account-switch purge, natural terminal failed-resident navigation, missing-anchor-message discard and some corrupt/provisional cache paths remain conditional Runtime-unverified.
- CI/Artifact success is not Runtime proof.

## Evidence rule

Always distinguish Code written, Static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, Stable and Frozen.
