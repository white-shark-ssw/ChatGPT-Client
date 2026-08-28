# Project State

_Last updated: 2026-08-29 through exact b33 Runtime result._

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

- **Branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open/mergeable.
- **Current main**: `a6e3b2bc185b8d5df90b846040387262a64e6154` at the b33 Runtime result.
- **Latest tested Candidate**: `DEV-conversation-round-count-0.1.0-b33`, `0.1.0 (33)`.
- **Exact b33 product/config source**: `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`.
- **Next reserved corrected identity**: `DEV-conversation-round-count-0.1.0-b34`, `0.1.0 (34)`; no corrected product output exists yet.
- **Scope**: compact title-first metadata, active-branch round count, authoritative historical timestamps, visible-text Copy, adaptive previous/next round navigation, centralized persisted Preferences, first-entry latest placement, and evidence-backed list/detail presentation corrections.
- **Authority boundary**: `ConversationRepository` remains sole conversation/list authority. `AppPreferences` owns persisted presentation booleans only. `ConversationRoundProjection` is derived from authoritative visible messages and is not mutable conversation authority.

## Candidate progression

- **b24**: package identity rejected/permanently reserved.
- **b25-b30**: Runtime partial/failing iterations that established accepted Copy/time/preferences, compact header, bounded list reconciliation, right-top refresh correction and restored automatic message self-sizing while exposing navigation defects.
- **b31**: Runtime partial/failing. User-message semantic round-start targeting produced precise landing; hitch/internal-row/Copy defects remained.
- **b32**: Runtime partial/failing. Accepted recipient/tool filtering, compact Copy direction and precise semantic landing; rejected long-jump smoothness and physical-bottom rubber-band direction.
- **b33**: **Runtime partial/failing**. Physical-bottom direction and final semantic precision are accepted; long-distance smoothness remains rejected.

## Exact b33 identity / CI / Artifact

- Candidate `DEV-conversation-round-count-0.1.0-b33`, `0.1.0 (33)`.
- Exact product/config source `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`.
- Exact push Run / Job `33195740528` / `98932282377`, success.
- Runtime Artifact `9695669835`; ZIP `sha256:841b682ffe27a2788b2c297225705c0b4fb6bc18b527fd4e8f30c62e10312407`.
- IPA `ChatGPTClient-0.1.0-b33-dev-conversation-round-count.ipa`; SHA `54c598e827bdfa2f1ae5a631d518f7914959e8e31aba1c687a4f0ceb24978855`.
- Independent package inspection: `0.1.0 (33)`, Candidate b33, source marker `0ba15ec48fe8`, minimum iOS14.0, arm64.
- Product-source PR merge-view against `main@a6e3b2bc185b8d5df90b846040387262a64e6154`: Run / Job `33195744651` / `98932296906`, success; merge `ca28819de6e5ed345087d04005ed05d74508881c`; merge Artifact `9695673573` is CI evidence only.

## Exact b33 Runtime evidence

User-tested exact b33 on iPhone/iOS17; supplied diagnostics metadata identifies build 33, Candidate b33 and source `0ba15ec48fe8`.

Accepted for the tested path:

- Physical-bottom adaptive direction including rubber-band overscroll: when a previous round exists, control stays/resolves to `上一轮` rather than flipping from overscroll delta.
- Final semantic landing remains precise at the intended user-message round start.
- Existing recipient filtering remains operational; one supplied long/tool-heavy Detail response had `mappingCount=3959`, `filteredRecipientMessageCount=1639`, `visibleMessageCount=96`.

Blocking result:

- Long-distance previous/next movement still feels insufficiently smooth / has visible gear-like snapping.
- Supplied diagnostics contain 74 `answerJump.completed` events; 14 applied `landingCorrectionApplied=true`.
- Non-retarget corrections include roughly 66.67pt, 203pt, 202.33pt, 496.33pt and 504pt.
- Rapid retargeting produced much larger native landing errors before nonanimated correction, including `-1804.33`, `-2897`, `-3356.67`, `-4932.67`, `-7047.67`, `-8237` and `-8258.67` points; post-correction error was ~0.
- This directly supports the current hypothesis that end-of-animation correction contributes materially to the perceived snap. It is Runtime evidence, not yet proof of the complete root cause.

## b34 correction boundary

Current b33 source cancels an in-flight jump with nonanimated `setContentOffset`, replaces `programmaticAnswerTargetRow`, starts another native animated `scrollToRow`, and handles every `scrollViewDidEndScrollingAnimation` callback against the current target.

The next minimal correction is to allow end-of-animation landing correction only when the **current target row is visible**. A callback arriving while the newer current target is not visible is treated as stale/superseded presentation completion: no snap/correction, current cursor/animation ownership remains, and a privacy-safe ignored-completion diagnostic is emitted. The final visible-target completion may still apply the existing >1pt correction.

Do not alter accepted bottom-direction behavior, semantic user-row targets, b32 recipient filtering, Copy/timestamps/preferences/header, cache/list/network behavior or state ownership. No timer/debounce/watchdog/row-height cache/fallback owner.

## Rendering scope observation

The supplied official-app/current-client recording shows raw Markdown syntax in this client where the official app renders headings, bold, inline code and tables. Current source simply concatenates `content.text`/string `parts` and assigns the result to `UILabel.text`; no Markdown/rich-annotation renderer exists.

This formatting work belongs to roadmap Phase 11 `DEV-message-rendering`, not the current Phase 8 metadata/settings task. Boxed-question-mark glyphs adjacent to raw `filecite ...` text appear to be unparsed citation/rich-content markers rather than a plain font-only defect; investigate them with rendering/rich-content evidence instead of stripping them speculatively in Phase 8.

## Current architecture / ownership

- `AppDelegate`: lifecycle + accepted WebKit warm-up sequencing.
- `RootViewController`: compact list/detail navigation owner.
- `ConversationRepository`: sole authoritative conversation/list/read/recovery owner.
- `ConversationListCacheStore`: storage-only persistent summary snapshot + privacy-safe last-verified scope hint.
- `ConversationDetailViewController`: Detail/recovery presentation, semantic anchors, first-entry latest placement and round navigation presentation.
- `ConversationMessageCell`: plain visible message/timestamp/assistant-Copy presentation; no Markdown renderer yet.
- `ConversationSidebarViewController`: list presentation; b29 accepted the right-top refresh blank-region correction.
- `AppPreferences`: centralized persisted display/interaction preference owner.
- `ConversationRoundProjection`: derived active-branch round projection; no second mutable semantic index.
- `DiagnosticsLogger`: structured privacy-safe diagnostics authority.
- default persistent `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: sole verified auth/account-context owner.

## Current next action

b33 is permanently reserved and must not be rebuilt. Produce corrected product code only under b34 or later after exact branch/base/conflict checks. Current b34 target is the smallest stale animation-completion guard described above; then run exact CI/Artifact/merge-view validation and hand the identity-verified IPA to the user for focused smoothness testing.

## Evidence boundaries

- b33 Runtime is **partial/failing**, not Stable.
- iOS17 success does not prove iOS14–16 or iPad.
- Read/recovery/multi-conversation/cache evidence is primarily Plus/personal; non-personal workspace identity remains Unknown/Unverified.
- Supported account-switch purge, natural terminal failed-resident navigation, missing-anchor-message discard and some corrupt/provisional cache paths remain conditional Runtime-unverified.
- CI/Artifact success is not Runtime proof.

## Evidence rule

Always distinguish Code written, Static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, Stable and Frozen.