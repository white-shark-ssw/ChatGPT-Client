# Project Profile

## Initialization

**Initialized — 2026-08-25; product/runtime profile refreshed 2026-08-29 through exact b35 Runtime and exact b36 Candidate/CI/Artifact/current-main merge-view evidence.**

Unsupported compatibility/protocol details remain `Unknown / Unverified` unless explicitly accepted below.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Purpose**: iOS native third-party ChatGPT client.
- **Primary runtime**: iOS; intended user-device ceiling iOS17.0; lower compatibility preferred where practical.

## Technology stack

- Swift 5 + UIKit.
- Foundation, WebKit, OSLog, CryptoKit; QuartzCore is used only for lightweight b36 quick-navigation button presentation flush.
- No third-party dependencies.
- Important config: `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/Info.plist`, shared Xcode scheme, `.github/workflows/ios-foundation.yml`.

## Repository structure and state owners

- **App entry**: `AppDelegate.swift`; accepted recovery baseline warms public default WebKit data store before product root.
- **Shell**: `RootViewController.swift`, `SettingsViewController.swift`; compact iPhone startup uses native list/detail navigation.
- **Build/runtime metadata**: `Support/AppBuildInfo.swift` + Xcode/Info.plist settings.
- **Diagnostics**: `Diagnostics/Diagnostics.swift` and privacy-safe call sites.
- **Embedded login**: `Authentication/AuthWebViewController.swift`.
- **Persistent auth-secret authority**: default persistent `WKWebsiteDataStore` only.
- **Auth/account authority**: `Authentication/AuthSessionStore.swift`; copied cookies/session bearer are transient only.
- **Diagnostic protocol probe**: `Protocol/ProtocolReadProbe.swift`; diagnostic-only.
- **Production conversation/list/read/recovery authority**: single `ConversationRepository` in `Conversation/ConversationFeature.swift`.
- **Conversation-list persistent storage**: private `ConversationListCacheStore`; storage-only, schema-versioned summary snapshot + privacy-safe last-verified scope namespace hint. It is not list/account authority.
- **Conversation presentation**: `ConversationDetailViewController`; owns lightweight per-conversation historical reading anchors, no-anchor first-entry placement, metadata and round-jump presentation.
- **Sidebar presentation**: `ConversationSidebarViewController`; presentation only. b29 Runtime accepts the right-top refresh blank-region correction.
- **Message presentation**: `ConversationMessageCell`; visible plain message body, authoritative timestamp and assistant Copy visual only. UIKit automatic self-sizing was restored in b30 and remains through b36. Markdown/rich annotation is not implemented yet.
- **Settings owner**: `AppPreferences` in `SettingsViewController.swift`; persisted display/interaction booleans only.
- **Round derivation**: `ConversationRoundProjection`; derived from authoritative visible `ConversationDetail.messages`, not mutable conversation authority.
- **Round-jump presentation**: one transient target cursor + one `UIViewPropertyAnimator`; b36 also reuses the existing quick-nav button for `定位中` presentation. None of these own conversation semantics.
- **Test roots**: no XCTest/UI-test target yet.

## Build and validation

- Packaging: `bash scripts/build_ipa.sh`.
- Underlying build: Release `xcodebuild` for iphoneos, signing disabled for TrollStore packaging.
- CI: GitHub Actions macOS15; current pipeline compiles arm64 iOS application with deployment target iOS14.0.
- Artifact scheme: `build/artifacts/ChatGPTClient-<version>-b<build>-dev-<work-slug>.ipa` + SHA-256 sidecar.
- Package identity authority: expanded built `Info.plist` is authoritative for version/build/Candidate. Build script validates Candidate/version/build agreement and emitted IPA identity. Workflow container label alone is not identity proof.
- Historical packaging defects: b16 and b24 had identity mismatches and are permanently rejected. Exact produced identities are never reused after Artifact production.

## Accepted baselines

- Foundation b1 Stable/merged.
- Auth/account b6 Stable/merged for recorded Plus/personal iPhone/iOS17 scope.
- Diagnostic read b7 accepted/merged.
- Production native read b9 Stable/merged.
- Recovery b15 Stable/merged; PR #10.
- Multi-conversation read state b21 Stable/merged; PR #23; recorded resident/coalescing/historical-scroll/title/replacement scope accepted. Frozen No.
- Conversation-list cache core b23 Stable/merged; PR #24; provisional cache/recent-skip/offline/manual-refresh/real `28 + 1 -> 29` behavior accepted. Frozen No.
- Active metadata Work additionally carries b26 Runtime acceptance for authoritative-total stale-row cap (`30 -> 29`, repeated `29/29`) and b29 Runtime acceptance for right-top list refresh/top-blank correction. These active corrections remain unmerged.

## Current conversation-metadata Work

`DEV-conversation-round-count` remains Active on `dev/conversation-round-count-20260828`, PR #27. Stable/Frozen No.

### Runtime progression

- b24: Artifact identity rejected/permanently reserved.
- b25-b30: partial/failing iterations that established accepted Copy/time/preferences, compact header, bounded list reconciliation, right-top refresh correction and automatic message self-sizing while exposing navigation defects.
- b31: precise user-message round-start landing accepted; remaining hitch/internal-row/Copy issues required correction.
- b32: accepted recipient/tool filtering, compact Copy direction and precise semantic user-round landing; smoothness and physical-bottom direction still failed.
- b33: accepted physical-bottom/rubber-band direction and final semantic precision; long-distance/rapid jump remained gear-like.
- b34: exact Runtime still rejected movement feel even though its tested trace had 42 requested / 42 completed jumps, 0 landing corrections and 0 ignored completions. This ruled out the old final-correction snap as the remaining tested cause.
- b35: unified every short/long jump to direct target position + about 120pt / 0.22s ease-out. Exact Runtime retained final precision but exposed several-second tap-to-position stalls around long-message regions; trace had 52 requests / 36 completions and suspicious gaps around 4s, 10s and 8s.
- b36: removes explicit root/table `layoutIfNeeded` calls from the jump path, reuses the existing quick-nav button for immediate `定位中` feedback, and logs direct-position/preparation timing. Runtime pending.

### Current b36 Runtime Candidate

- Candidate `DEV-conversation-round-count-0.1.0-b36`.
- Version/build `0.1.0 (36)`.
- Exact product/config source `8f8614508eef5197f9fff4bb9d10c14354d5821e`.
- Product diff from the b36 checkpoint parent is exactly three files: workflow identity 2+/2-, Xcode identity 4+/4-, `ConversationFeature.swift` 25+/6-.
- The jump path no longer forces `view.layoutIfNeeded()` or `tableView.layoutIfNeeded()` around direct positioning. One nonanimated `scrollToRow(..., .top, animated:false)` remains, followed by the same short direction-consistent ease-out.
- Immediate feedback is presentation-only on the existing 44pt round button (`定位中` / `正在定位`), not a second state owner.
- New privacy-safe `answerJump.positioned` records direct-position/preparation duration, target visibility and row/role only; no message text/identity.
- No row-height cache, timer, retry, watchdog, alternate semantic authority, network change or rendering change was added.
- Exact push Run/Job `33207505424` / `98972194770`, success on exact product source.
- Runtime Artifact `9700254733`; ZIP `sha256:718e8500ea41bcc73b41f5bebd9a4850b93246368a87304be0b2c4751702e576`.
- IPA `ChatGPTClient-0.1.0-b36-dev-conversation-round-count.ipa`; SHA `cdf2c7278ec0a4f6f5125a711f78d7bbda8c606a32dda87f614d710f662bd867`.
- Independent package inspection: `0.1.0 (36)`, Candidate b36, source `8f8614508eef`, MinimumOSVersion 14.0, bundle `com.whitesharkssw.chatgptclient`, Mach-O arm64.
- Current-main PR merge-view against unchanged `main@a6e3b2bc185b8d5df90b846040387262a64e6154`: Run/Job `33207508869` / `98972206567`, success on synthetic merge `e7ff5b368faaea3debbe5d5547c0424996653fa0` which explicitly merges exact b36 source into main.
- Evidence level: **Code written + Static/source audit + exact push CI + identity-valid Runtime Artifact + current-main merge-view CI. Runtime/manual Pending. Stable/Frozen No.**

## Rendering scope boundary

The current client has plain `UILabel.text` message presentation and no Markdown/rich-annotation renderer. The supplied official-app comparison recording showed raw Markdown/table syntax and raw `filecite`-adjacent boxed glyphs in this client. Markdown/rich citation presentation belongs to future `DEV-message-rendering`, not current metadata/settings Work; do not strip or reinterpret those markers speculatively here.

## Versioning and candidate identity

- Marketing version source: `MARKETING_VERSION`.
- Build source: `CURRENT_PROJECT_VERSION`.
- Candidate scheme: `DEV-<work-slug>-<marketing-version>-b<build>`.
- Bundle ID: `com.whitesharkssw.chatgptclient`; accepted, not Frozen.
- Current active Candidate: `0.1.0 (36)` / `DEV-conversation-round-count-0.1.0-b36`.
- Exact produced identities b24-b36 are reserved and are never reused for corrected product output.

## Runtime / deployment

- Native iOS application, TrollStore IPA.
- Deployment target iOS14.0; intended environment ceiling iOS17.0.
- Build device families iPhone+iPad; real-device evidence currently covers iPhone only unless explicitly stated.
- Artifact architecture arm64.

## Evidence boundaries

- b35 Runtime is partial/failing; b36 Runtime is Pending.
- iOS17 success does not prove iOS14–16 or iPad.
- Recorded read/recovery/multi-conversation/cache evidence is primarily Plus/personal; non-personal workspace identity remains Unknown/Unverified.
- Supported account-switch purge, natural terminal failed-resident navigation, missing-anchor-message discard and some corrupt/provisional cache paths remain conditional Runtime-unverified.
- Current source has no evidenced authoritative Chat/Work type owner; do not infer `工作` from title/presentation text.
- CI/Artifact success does not prove b36 latency or feedback behavior on device.

## Auto-refresh rule

Update this file proactively when purpose, stack, build/test commands, version/Candidate, deployment/runtime, state ownership, accepted baseline or current validation evidence changes.
