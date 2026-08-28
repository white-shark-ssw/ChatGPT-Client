# Project State

_Last updated: 2026-08-29 through exact b33 Runtime result and exact b34 CI/Artifact/merge-view evidence._

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
- **Current main at b34 validation**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- **Latest tested Candidate**: b33, Runtime partial/failing.
- **Current Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b34`, `0.1.0 (34)`; Runtime pending.
- **Exact b34 product/config source**: `bf66c7080347660e0154952a261230a24bb94f7d`. Later docs/checkpoint commits do not redefine this source.
- **Scope**: compact title-first metadata, active-branch round count, authoritative historical timestamps, visible-text Copy, adaptive previous/next round navigation, centralized persisted Preferences, first-entry latest placement, and evidence-backed list/detail presentation corrections.
- **Authority boundary**: `ConversationRepository` remains sole conversation/list authority. `AppPreferences` owns persisted presentation booleans only. `ConversationRoundProjection` is derived from authoritative visible messages and is not mutable conversation authority.

## Candidate progression

- **b24**: package identity rejected/permanently reserved.
- **b25-b30**: Runtime partial/failing iterations that established accepted Copy/time/preferences, compact header, bounded list reconciliation, right-top refresh correction and restored automatic message self-sizing while exposing navigation defects.
- **b31**: Runtime partial/failing. User-message semantic round-start targeting produced precise landing; hitch/internal-row/Copy defects remained.
- **b32**: Runtime partial/failing. Accepted recipient/tool filtering, compact Copy direction and precise semantic landing; rejected long-jump smoothness and physical-bottom rubber-band direction.
- **b33**: Runtime partial/failing. Physical-bottom direction and final semantic precision accepted; long-distance/rapid jump smoothness rejected.
- **b34**: Code/source audit/CI/Artifact/current-main merge-view complete; Runtime pending.

## Exact b33 Runtime evidence

- Candidate `DEV-conversation-round-count-0.1.0-b33`, `0.1.0 (33)`; exact source `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`.
- Push Run / Job `33195740528` / `98932282377`; Runtime Artifact `9695669835`; IPA SHA `54c598e827bdfa2f1ae5a631d518f7914959e8e31aba1c687a4f0ceb24978855`.
- User-tested exact b33 on iPhone/iOS17; supplied diagnostics metadata identifies build 33, Candidate b33 and source `0ba15ec48fe8`.
- Accepted: physical-bottom adaptive direction including rubber-band overscroll; final landing remains precise at intended user-message round start.
- Existing recipient filtering remained operational; one supplied long/tool-heavy Detail response had `mappingCount=3959`, `filteredRecipientMessageCount=1639`, `visibleMessageCount=96`.
- Rejected: long-distance previous/next movement still feels gear-like.
- Diagnostics contain 74 `answerJump.completed` events; 14 applied `landingCorrectionApplied=true`. Ordinary corrections include about 66.67–504pt; rapid retargeting produced pre-correction native errors including `-1804.33`, `-2897`, `-3356.67`, `-4932.67`, `-7047.67`, `-8237`, `-8258.67` points while final corrected error returned to ~0.
- This supports the hypothesis that an old/cancelled animation completion can act on a newer current target and materially contribute to snap/gear behavior. It is not proof that every remaining smoothness issue has the same cause.

## Exact b34 product correction

- Candidate `DEV-conversation-round-count-0.1.0-b34`, `0.1.0 (34)`.
- Exact product/config source `bf66c7080347660e0154952a261230a24bb94f7d`.
- Parent→product diff from checkpoint head `b891cffb47ba4ed469d38b590bfdb30d75b2d34e` is exactly three files:
  - workflow identity b33→b34;
  - Xcode build/Candidate identity 33→34;
  - `ConversationFeature.swift` 7 additions / 1 deletion.
- Swift behavior change: `scrollViewDidEndScrollingAnimation` may run the existing >1pt landing correction only when the **current target row is visible**. If current target is not visible, log privacy-safe `answerJump.completionIgnored` / `current_target_not_visible`, preserve the newer animation/cursor ownership and do not snap/correct.
- Native animated `scrollToRow(..., .top, animated:true)` remains the movement owner. No timer, debounce, watchdog, row-height cache, alternate navigation authority or new state store was added.
- Accepted b33 physical-bottom direction, semantic user-row target derivation, b32 recipient filtering, Copy/timestamps/preferences/header, list/cache/network behavior and ownership remain unchanged.

## Exact b34 CI / Artifact

- Push Run / Job `33200768537` / `98949366655` — success on exact `head_sha=bf66c7080347660e0154952a261230a24bb94f7d`.
- Xcode 16.4 / iPhoneOS18.5 SDK; target `arm64-apple-ios14.0`.
- Exact Runtime Artifact `9697664416`; Artifact name `ChatGPTClient-DEV-conversation-round-count-0.1.0-b34`.
- Artifact ZIP digest `sha256:0b05a435888c041286b331c554f31f7e64dda0a30d214014bf2a144d8b696c65`.
- IPA `ChatGPTClient-0.1.0-b34-dev-conversation-round-count.ipa`; SHA `1705a2a39941ab6aee88e13b53d68d55b2fd9ff3d43d1c50d9cdcb6613c2b9b6`.
- Independent package inspection matches `0.1.0 (34)`, Candidate b34, source marker `bf66c7080347`, MinimumOSVersion 14.0, bundle `com.whitesharkssw.chatgptclient`, Mach-O arm64.

## Current-main merge-view evidence

- Main remained `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- PR head used for merge-view: docs/checkpoint head `d9b3a4846e05bf04a2bce962beeef918d7b91d26`; product/config source remains exact `bf66c708...`.
- PR Run / Job `33200813591` / `98949517057`, success.
- GitHub checkout explicitly used merge `a42408a64a4ff7fba7d799f39c897ae6930daf6f` = `d9b3a484...` into `main@a6e3b2...`.
- Merge-view Artifact `9697686876`; ZIP digest `sha256:82efb395840a01403fba0b4dad61c2957e6cc84c2c70b0f34f94fcfa19cc192c`; merge-view IPA SHA `54614e6a1f995b8232bc81c6af518984cc7f286bbc9d98fbd0844aba7d7e6e9e`.
- Merge-view output is CI evidence only and never replaces exact Runtime Artifact `9697664416` from product source `bf66c708...`.

## Rendering scope observation

The supplied official-app/current-client recording shows raw Markdown syntax in this client where the official app renders headings, bold, inline code and tables. Current source simply concatenates `content.text`/string `parts` and assigns the result to `UILabel.text`; no Markdown/rich-annotation renderer exists.

This work belongs to roadmap Phase 11 `DEV-message-rendering`, not current Phase 8. Boxed-question-mark glyphs adjacent to raw `filecite ...` text appear to be unparsed citation/rich-content markers rather than a plain font-only defect; investigate with rendering/rich-content evidence instead of stripping speculatively in Phase 8.

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

## Current Runtime gate

Install/test exact Runtime Artifact `9697664416` / b34 IPA SHA `1705a2a39941ab6aee88e13b53d68d55b2fd9ff3d43d1c50d9cdcb6613c2b9b6` on the accepted iPhone/iOS17 scope.

Acceptance focus:

1. Long-distance previous/next jumps and rapid repeated taps should no longer show the b33 stale-completion hard snap/gear effect.
2. Final semantic landing must remain precise.
3. Physical-bottom/rubber-band direction must remain accepted.
4. `answerJump.completionIgnored` may appear for stale completions whose current target is not visible; huge correction against a not-yet-visible newer target should no longer occur.
5. Regression sanity: recipient/tool filtering, Copy, first-entry latest, A/B anchors, timestamps/preferences, list reconcile, Sync/Reload remain intact.

Do not merge/close PR #27 or claim Stable until exact b34 Runtime is accepted. If a defect remains, record it first and allocate b35 or later; never rebuild b34.

## Evidence boundaries

- b33 Runtime is partial/failing; b34 Runtime is Pending.
- iOS17 success does not prove iOS14–16 or iPad.
- Read/recovery/multi-conversation/cache evidence is primarily Plus/personal; non-personal workspace identity remains Unknown/Unverified.
- Supported account-switch purge, natural terminal failed-resident navigation, missing-anchor-message discard and some corrupt/provisional cache paths remain conditional Runtime-unverified.
- CI/Artifact success is not Runtime proof.

## Evidence rule

Always distinguish Code written, Static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, Stable and Frozen.
