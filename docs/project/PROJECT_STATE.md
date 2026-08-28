# Project State

_Last updated: 2026-08-29 through exact b33 CI/Artifact evidence and b32 Runtime result._

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

- **Branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open.
- **Current main**: `a6e3b2bc185b8d5df90b846040387262a64e6154` at b33 Candidate production/documentation finalization.
- **Exact Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b33`, `0.1.0 (33)`.
- **Exact product/config source**: `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`. Later docs-only commits do not redefine this source.
- **Scope**: compact title-first metadata, active-branch round count, authoritative historical timestamps, visible-text Copy, adaptive previous/next round navigation, centralized persisted Preferences, first-entry latest placement, and evidence-backed list/detail presentation corrections.
- **Authority boundary**: `ConversationRepository` remains sole conversation/list authority. `AppPreferences` owns persisted presentation booleans only. `ConversationRoundProjection` is derived from authoritative visible messages and is not mutable conversation authority.
- **Type boundary**: ordinary supported detail may show `聊天 · N轮`; `工作` remains deferred until authoritative Work/Project type evidence exists.
- **Preference defaults**: `显示会话轮数` On, `显示消息时间` On, `显示轮次快速跳转` On.

## Candidate progression

- **b24**: package identity rejected/permanently reserved.
- **b25**: Runtime partial/failing. Copy function, historical timestamps and preference persistence accepted; header/jump/refresh failed and `30/29` list mismatch exposed.
- **b26**: Runtime partial/failing. Accepted authoritative-total bound (`30 -> 29`, repeated `29/29`), sequential targets and compact title-first header.
- **b27**: Runtime partial/failing. Long-conversation jump hitch persisted; right-top refresh inflated top inset; Copy visual rejected.
- **b28**: Runtime partial/failing. Large answer-target drift, programmatic direction flips, first-entry top and refresh blank band reproduced.
- **b29**: Runtime partial/failing. Right-top refresh/top blank correction accepted; `estimatedRowHeight=0` caused severe self-sizing message-layout regression and is rejected.
- **b30**: Runtime partial/failing. Automatic self-sizing restored and severe hitch improved, but Copy remained too large and assistant-answer landing was grossly inaccurate.
- **b31**: Runtime partial/failing. User-message semantic round-start targeting produced precise landing, but jump hitch remained; raw internal/tool rows and Copy visual still required correction.
- **b32**: Runtime partial/failing. Exact long/tool-heavy sample accepted recipient filtering (`filteredRecipientMessageCount=748`, ordinary visible messages `84`), compact Copy direction and precise semantic landing. Raw tool/internal rows no longer appeared as ordinary chat rows. Remaining defects: jump smoothness and physical-bottom rubber-band direction.
- **b33**: Code/source audit/CI/Artifact and current-main merge-view evidence complete; Runtime pending.

## Exact b32 Runtime evidence

- Candidate `DEV-conversation-round-count-0.1.0-b32`, `0.1.0 (32)`.
- Product/config source `ea2b7bf4ee89acbb748f2b3aec5fcfc61555b2bc`.
- Push Run / Job `33177491033` / `98869786437`, success.
- Runtime Artifact `9688235425`; ZIP `sha256:17c6639b5ec2b106cab936c5de357b65671c116701127ed88dfbe92bb8378445`.
- IPA `ChatGPTClient-0.1.0-b32-dev-conversation-round-count.ipa`; SHA `f1eb4e6fb8cda58db0216df080ea90098ce681e1ed47962eebda57f803f9be80`.
- Accepted: semantic user-round landing accuracy, recipient/tool filtering, compact Copy direction/function regression sanity.
- Rejected: long-jump smoothness and bottom-rubber-band adaptive-direction behavior.

## Exact b33 Candidate / CI / Artifact

- Candidate `DEV-conversation-round-count-0.1.0-b33`, `0.1.0 (33)`.
- Exact product/config source `0ba15ec48fe86ad0c9a3b69ac5415d128bcd8aba`.
- Scoped product correction only:
  1. physical top/bottom boundaries outrank drag delta, including rubber-band overscroll;
  2. native animated `scrollToRow` remains the movement owner;
  3. after animation, measure native landing and apply one nonanimated same-target re-anchor only when absolute error exceeds `1pt`;
  4. add privacy-safe `nativeLandingErrorPoints` and `landingCorrectionApplied` diagnostics;
  5. retain b32 recipient filtering, round derivation, Copy, list reconciliation, network semantics and state owners unchanged.
- Exact push Run / Job `33195740528` / `98932282377`, success.
- Runtime Artifact `9695669835`; Artifact name `ChatGPTClient-DEV-conversation-round-count-0.1.0-b33`; ZIP `sha256:841b682ffe27a2788b2c297225705c0b4fb6bc18b527fd4e8f30c62e10312407`.
- IPA `ChatGPTClient-0.1.0-b33-dev-conversation-round-count.ipa`; SHA `54c598e827bdfa2f1ae5a631d518f7914959e8e31aba1c687a4f0ceb24978855`.
- Independent package inspection: `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=33`, Candidate b33, source marker `0ba15ec48fe8`, minimum iOS14.0, Mach-O arm64.
- Current-main PR merge-view against `main@a6e3b2bc185b8d5df90b846040387262a64e6154`: Run / Job `33195744651` / `98932296906`, success; merge view `ca28819de6e5ed345087d04005ed05d74508881c`; merge Artifact `9695673573`; ZIP `sha256:74799aec08cbf43cedbf1dc9c1b7bb8fd75ef524c1a0335425048f90e670f608`; merge-view IPA SHA `29b578eb6c060d2e528313940e3614e476eee6c36a8d6b354f0bf8ac7f594123`.
- Merge-view output is CI evidence only. Real-device testing must use exact push Artifact `9695669835`.

## Current architecture / ownership

- `AppDelegate`: lifecycle + accepted WebKit warm-up sequencing.
- `RootViewController`: compact list/detail navigation owner.
- `ConversationRepository`: sole authoritative conversation/list/read/recovery owner.
- `ConversationListCacheStore`: storage-only persistent summary snapshot + privacy-safe last-verified scope hint.
- `ConversationDetailViewController`: Detail/recovery presentation, semantic anchors, first-entry latest placement and round navigation presentation.
- `ConversationMessageCell`: visible message/timestamp/assistant-Copy presentation.
- `ConversationSidebarViewController`: list presentation; b29 accepted the right-top refresh blank-region correction.
- `AppPreferences`: centralized persisted display/interaction preference owner.
- `ConversationRoundProjection`: derived active-branch round projection; no second mutable semantic index.
- `DiagnosticsLogger`: structured privacy-safe diagnostics authority.
- default persistent `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: sole verified auth/account-context owner.

## Current Runtime gate

Exact b33 Runtime is **Pending**. Test focus:

1. At physical bottom, including rubber-band overscroll, adaptive control resolves/stays `上一轮` when a previous round exists; overscroll delta must not flip it to `下一轮`.
2. Long previous/next jumps use one smooth native animation without the prior serious end-of-animation hitch.
3. Landing remains precise at the intended user-message round start; rapid repeated taps advance one semantic round per tap.
4. Diagnostics may show `nativeLandingErrorPoints` and `landingCorrectionApplied`; normal accurate native landings should generally avoid correction.
5. Regression sanity: tool/internal rows remain filtered; Copy remains accepted compact visual/function; A/B anchors, first-entry latest, timestamps/preferences, list reconcile, Sync/Reload remain intact.

Do not merge/close PR #27 or claim Stable until exact b33 real-device Runtime acceptance.

## Evidence boundaries

- iOS17 success does not prove iOS14–16 or iPad.
- Read/recovery/multi-conversation/cache evidence is primarily Plus/personal; non-personal workspace identity remains Unknown/Unverified.
- Supported account-switch purge, natural terminal failed-resident navigation, missing-anchor-message discard and some corrupt/provisional cache paths remain conditional Runtime-unverified.
- CI/Artifact success is not Runtime proof.

## Evidence rule

Always distinguish Code written, Static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, Stable and Frozen.