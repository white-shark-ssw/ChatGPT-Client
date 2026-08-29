# Project State

_Last updated: 2026-08-29 through valid b43 hybrid CI/Artifact; exact-device Runtime pending._

## Current accepted merged baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account context for recorded iPhone/iOS17 Plus/personal scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted diagnostic read evidence.
- `DEV-native-read-path-0.1.0-b9`: merged Stable native read path.
- `DEV-conversation-recovery-0.1.0-b15`: merged Stable recovery; PR #10.
- `DEV-multi-conversation-state-0.1.0-b21`: merged Stable multi-conversation read state; PR #23; Frozen No.
- `DEV-conversation-list-cache-core-0.1.0-b23`: merged Stable list-cache core; PR #24; Frozen No.
- **`DEV-conversation-round-count-0.1.0-b38`: merged Stable Phase 8 metadata/settings/round-navigation baseline; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`; Frozen No.**

## Completed Phase 8 — DEV-conversation-round-count

- **PR**: #27 merged 2026-08-29.
- **Actual merge commit / merged main baseline**: `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- **Accepted Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b38`, `0.1.0 (38)`.
- **Exact tested product/config source**: `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- **Runtime Artifact**: `9708425762`; IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- **Runtime result**: accepted on recorded iPhone/iOS17 scope; user feedback **“没问题了”**.
- **Stable/Frozen**: Stable / No for the recorded accepted Phase 8 scope.

## Current Phase 9 — DEV-send-stream

### b42 security/transport decision retained

- Exact b42 Candidate `DEV-send-stream-0.1.0-b42`, version/build `0.1.0 (42)`.
- Exact product/config source `e8946e48a0b5ad86b402faf5eabba627e3393adf`; Artifact `9709824510`; IPA SHA `c6d1d421ab05a2294784223400291f0dc1683b638b2647ae85b2d9d4f3fcb85b`.
- Exact iPhone/iOS17 default-primary-assistant Runtime proved Sentinel `proofOfWorkRequired=true`, `turnstileRequired=true`, `soRequired=true` and non-empty PoW/Turnstile finalize submissions before successful Send.
- Therefore **pure-native/transient-WebKit-auth ChatGPT-account Send remains blocked**. No PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay, captured proof/token replay, hidden challenge-harvesting WebView or guessed fallback endpoint.

### Explicit architecture change selected

The user selected **Option 2: native shell + user-visible official ChatGPT Web Send surface**. This is an intentional hybrid product architecture, not a claim of pure native Send.

- Native list/detail/recovery/round-navigation remain owned by the accepted native shell and `ConversationRepository`.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- The visible official-Web surface performs its own normal browser Send/challenge flow while the user is on that surface.
- Hidden/shadow Web transport remains prohibited.
- Web smoothness close to native and immediate attachment-entry response are hard Runtime gates.

### Current b43 Candidate

- **Status**: Code written; exact push CI passed; exact PR CI passed; valid Artifact produced and independently identity-verified. **Runtime/manual/real-device pending; Stable/Frozen No.**
- **Branch / PR**: `dev/send-stream-20260829`; PR #29 remains open; do not merge as accepted hybrid Send before Runtime acceptance.
- **Candidate**: `DEV-send-stream-0.1.0-b43`, version/build `0.1.0 (43)`.
- **Exact product/config source**: `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`; later docs-only commits do not redefine it.
- **Push Run / Job**: `33241032864` / `99070294478`, success.
- **PR Run / Job**: `33241035013` / `99070299776`, success.
- **Artifact**: `9711364573`; ZIP `sha256:1a9516221ec5ece59741f9f2af2483815f09fa47f051ff6a97a67a12d40d4c23`.
- **IPA**: `ChatGPTClient-0.1.0-b43-dev-send-stream.ipa`; SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.
- **Independent package identity**: `0.1.0 (43)`, Candidate b43, source `f602d68ae95d`, Release, MinimumOSVersion 14.0, UIDeviceFamily `[1,2]`, Mach-O arm64.
- **Implementation scope**: one shared process-resident visible `AuthWebViewController.hybridChat` + Settings entry. First presentation loads official `https://chatgpt.com/`; ordinary pop/re-entry reuses the same controller/WebView without automatic reload. No DOM automation, text scraping or challenge/token capture.

### Invalid accidental emission retained as rejected evidence

Product commit `8be4da4e6af3dad146bc43888ddeb3f4cd2037b8` was initially auto-built while workflow/Xcode metadata still identified b42:

- Run `33238065644`; Artifact `9710515489`; ZIP digest `sha256:d76747ea3c524f31e9a6e512119ab3a85172c5c7fc3492d4264a57f93bd86f7f`.
- **Permanently rejected / never install / never cite as Runtime.** Legitimate b42 remains Artifact `9709824510`.

### Next gate

Exact-device iPhone/iOS17 Runtime must validate:

- first visible hybrid entry latency;
- resident Back -> re-entry reuse (`residentReuse=true`, no avoidable reload);
- keyboard/typing response;
- ordinary visible-Web Send and streamed-response scrolling;
- rapid scrolling smoothness;
- official Web `+` / attachment-entry responsiveness;
- native-return regression check;
- privacy-safe diagnostics only.

## Authority / architecture

- `ConversationRepository` remains sole native conversation/list/read/recovery authority.
- `AuthSessionStore` remains sole verified native auth/account owner; default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- `ConversationListCacheStore` remains storage-only.
- `AppPreferences` remains sole persisted display/interaction settings owner.
- `ConversationRoundProjection` is derived semantic round data only.
- `ConversationMessagePresentationProjection` is ephemeral native presentation geometry only; b43 does not change it.
- `ConversationMessageCell` deterministic manual frame layout remains the Stable native read baseline.
- `RootViewController` remains the native shell navigation owner; b43 makes no Root product change.
- The visible official-Web surface is a Web Send surface, not a second native conversation repository/response authority.

## Stable Phase 8 behavior retained

- b26 authoritative-total cap: stale `30 -> 29`, repeated `29/29`.
- b29 right-top refresh/top blank-region correction.
- b31 semantic landing at authoritative user-message round start.
- b32 recipient/tool/internal filtering and compact assistant Copy direction.
- b33 physical-bottom/rubber-band direction.
- first-entry latest/bottom, independent A/B historical anchors and Sync/Reload anchor re-derivation.
- b37/b38 deterministic long-message geometry: bounded chunks + exact derived metrics/prefix offsets + manual frame layout.
- b38 continuous 0.35s `.easeInOut` full-distance round animation from current viewport to O(1) deterministic target; no pre-jump teleport or final correction snap.

## Phase 9 protocol evidence retained

- Existing/new Web Send route: `POST /backend-api/f/conversation`; existing includes `conversation_id`, new omits it.
- Normal stream: `v1`, early authoritative conversation identity, message/patch events, `message_stream_complete`, trailing conversation metadata and `[DONE]`; new chat emits `title_generation`.
- Official server Stop: `POST /backend-api/stop_conversation` with `{ conversation_id, exclude_async_types: [] }`; successful Stop may close the Send stream without normal completion tail.
- These facts remain protocol evidence. b43 does not convert them into a native private-API transport.

## Evidence boundaries

- Exact b38 Runtime remains Stable/merged for recorded iPhone/iOS17 scope; Frozen No.
- Exact b42 Runtime remains accepted security/transport-boundary evidence only.
- Exact b43 is **CI/Artifact evidence only until user real-device Runtime**.
- iOS17 evidence does not prove iOS14–16 or iPad.
- Non-personal workspace identity, supported account switch, native-to-Web attachment handoff and other explicitly untested branches remain Unknown/Unverified.

## Evidence rule

Always distinguish Code written, Static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, Stable and Frozen.
