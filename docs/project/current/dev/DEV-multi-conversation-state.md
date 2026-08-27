# DEV-multi-conversation-state

## Status

**Active — b17 core real-device multi-conversation sequences accepted; b18 exact semantic-scroll Candidate has Code + static review + CI + identity-valid Artifact; b18 real-device scroll validation pending; Stable/Frozen = No**

- **Work ID**: `DEV-multi-conversation-state`
- **Routing aliases / keywords**: `多会话 / 多会话驻留 / 多会话状态 / 快速切换 / multi-conversation`
- **Task**: 将单 selected conversation detail/request owner 演进为 account-scoped per-conversation resident state，并建立后续 send/stream 所需的多会话 freshness 与异步所有权基线。
- **Baseline**: `0.1.0 (15)` Stable recovery; `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011`; recovery PR #10 merged.
- **Working branch / PR**: `dev/multi-conversation-state-20260827`; PR `Not created`.
- **Last runtime-tested candidate**: `DEV-multi-conversation-state-0.1.0-b17`, version `0.1.0 (17)`.
- **Current exact Candidate**: `DEV-multi-conversation-state-0.1.0-b18`, version `0.1.0 (18)`.
- **Exact b18 product/config source**: `f30c13b4ac2c40dcda829585682825ca906dceae`; tree `c2797f05a8b8c43bdd1a5064177e3b7c49606614`.
- **Atomicity evidence**: b18 was assembled off-branch from parent `49be4de3b2918ae72b22e3de7a386136d92c2523`, reviewed, then branch ref moved once. Exact diff contains only `.github/workflows/ios-foundation.yml`, `ChatGPTClient.xcodeproj/project.pbxproj`, `ChatGPTClient/Conversation/ConversationFeature.swift`, and `scripts/build_ipa.sh`.
- **Conflict gate at publication**: `main` remained `f155ddb873540f7c80d6e66ebbfeb59ded26f011`; no open PR; `current/dev/` contained only this Active Work plus README; no duplicate b18 identity existed.

## Candidate history

### b16 — historical / rejected before runtime

- Exact source `81e6774ae1f5eb1f0c6c3b514dfdf29d7611fa08`; CI Run `33009246356` succeeded.
- Artifact `9621830284` embedded wrong recovery candidate/slug and is permanently rejected/superseded before runtime.
- Second source review also found stale-scope, waiter, hidden-Sync, list-freshness, task-handle and owner-domain gaps.
- Never reuse b16.

### b17 — identity-valid / core runtime-evidenced

- Exact product/config source `bc69d58b3245a1ab21b250e16612c11d39ddbf33`; tree `3451585f83c7bac69368709fe6273b90a0294d29`.
- Static/local: final `ConversationFeature.swift` blob `1034cff72dea36d6d7e835bdf52dcfe2cdc8e38d`; local Git-blob hash matched; `swiftc -frontend -parse` passed.
- CI Run `33045536770`, job `98428537619`, success.
- Artifact `9635486304`; ZIP `sha256:bf6aed8cebcb08153fbe8fac6868ce60c0ef4bd7876340246912ba8edbed1c33`.
- IPA `ChatGPTClient-0.1.0-b17-dev-multi-conversation-state.ipa`; SHA `ed551deac0335e47da56da36ec2a8a20550613ac072ac1ddf0b84790278318dc`.
- Real-device iPhone/iOS17 accepted resident return, hidden completion, same-target coalescing, Sync A->B->A rejoin, and rapid different-conversation overlap up to three active operations with no HTTP429 in supplied export.
- User reproduced P1 scroll defect: A near ~10% -> B scroll -> A returns shifted.

### b18 — semantic historical scroll-anchor Candidate

#### Code / design

- `ConversationRepository` and network/protocol ownership are unchanged.
- `ConversationDetailViewController` now owns lightweight per-conversation scroll presentation metadata only.
- Added `displayedConversationID` so the actually displayed A can be captured even though `RootViewController` has already changed repository selection to B.
- Anchor representation is `messageID + relativeOffset`; no global raw offset is copied between conversations.
- `showConversation` captures the old displayed conversation before replacing rows, then restores the target's own anchor after reload.
- If the target has no anchor, presentation starts from normal top instead of inheriting another conversation's offset.
- Account-scope reset clears all presentation anchors.
- Same-visible-conversation Sync captures the current historical anchor immediately before rows are refreshed and restores it if the anchored message still exists.
- Reload captures before clearing rows; successful rebuilt detail restores only if the same anchored message still exists.
- If an anchored message is absent from the refreshed current branch, the anchor is discarded and the view returns to top; no speculative cross-message fallback.
- Added privacy-safe `scrollAnchor.saved`, `scrollAnchor.restored`, and `scrollAnchor.discarded` diagnostics with row index/relative offset only; no raw message/conversation ID or body.
- No fake `isStreaming`, response flag, timer, retry, fallback, watchdog, or future follow-tail enum was added. Future follow-tail eligibility must come from the real Send/Stream response owner.

#### Static/source review

- Prepared final `ConversationFeature.swift` Git blob: `daf60d76b1295a9662a119b28766511039a52e8e`.
- Source patch reviewed before publication for A->B capture order, target-independent anchors, Sync/Reload preservation, missing-anchor behavior, and account reset.
- Exact product diff: 4 expected files only; `ConversationRepository` source body is not modified by b18.
- Xcode Release CI subsequently compiled the exact `ConversationFeature.swift` as part of the exact Candidate source.

#### CI

- Run `33054012226`, job `98456174184`: **success**.
- Exact checkout: `f30c13b4ac2c40dcda829585682825ca906dceae`.
- Toolchain: macOS 15.7.7 runner, Xcode 16.4 / build 16F6, iPhoneOS18.5 SDK.
- Exact build inputs: `DIAGNOSTICS_CANDIDATE=DEV-multi-conversation-state-0.1.0-b18`; `SOURCE_COMMIT=f30c13b4ac2c`.
- Swift compile target: `arm64-apple-ios14.0`.
- Log ends `BUILD SUCCEEDED`.
- Exactly one intended b18 push workflow run exists; historical branch product runs remain b16/b17.

#### Artifact / independent package inspection

- Artifact ID `9638821912`, name `ChatGPTClient-DEV-multi-conversation-state-0.1.0-b18`.
- Artifact ZIP digest from GitHub and independent local SHA: `sha256:36b59b8c4d3bdcadedd463a3554528452ff46478651671b50f4bd9f7fa2b5d2c`.
- IPA: `ChatGPTClient-0.1.0-b18-dev-multi-conversation-state.ipa`.
- IPA SHA-256: `296870630ac57f439d559a2b8b823094885d0362f547a190e48982696187877c`; independently matches generated `.sha256` sidecar.
- Embedded identity: `CFBundleShortVersionString=0.1.0`; `CFBundleVersion=18`; `DiagnosticsCandidate=DEV-multi-conversation-state-0.1.0-b18`; `DiagnosticsSourceCommit=f30c13b4ac2c`; `MinimumOSVersion=14.0`; `UIDeviceFamily=[1,2]`; executable = Mach-O 64-bit arm64.
- Artifact identity is accepted. This is not runtime proof of the scroll fix.

## User-confirmed future Send/Stream scroll semantics

- Per-conversation scroll presentation must distinguish **historical-reading anchor** from future **follow-tail** intent.
- If A is at/near bottom and A has an authoritative active response, hidden growth/completion must make return-to-A land at A's current latest bottom.
- If the user intentionally scrolls upward while A is generating, that exits follow-tail and later return restores historical reading anchor.
- B scrolling never mutates A presentation state and hidden A growth never mutates B.
- b18 intentionally does not invent response lifecycle state; these follow-tail gates remain for `DEV-send-stream`.

## Evidence labels

### b17
- **Code written**: Yes.
- **Static/local checks**: Passed.
- **CI passed**: Yes.
- **Artifact produced**: Yes, identity accepted.
- **Runtime/manual/real-device**: Core tested sequences accepted; P1 scroll defect reproduced.
- **Stable/Frozen**: No.

### b18
- **Code written**: **Yes — exact source published**.
- **Static/source checks**: **Passed — exact diff/source review; exact source compiled in Release CI**.
- **CI passed**: **Yes — Run `33054012226`, Job `98456174184`**.
- **Artifact produced**: **Yes — Artifact `9638821912`, identity independently accepted**.
- **Runtime/manual/real-device**: **Pending**.
- **Stable/Frozen**: **No**.

## b18 real-device acceptance matrix

1. A long resident conversation: scroll A to a clearly identifiable historical point around ~10%; switch to B; scroll B elsewhere; return A. A should restore the same message/visual offset and diagnostics should show `scrollAnchor.saved` then `scrollAnchor.restored` for A.
2. Scroll B to a distinct point; switch A -> B repeatedly. A and B must each return to their own independent anchor; neither may inherit the other's raw offset.
3. Open a conversation C for the first time with no saved anchor after leaving a deeply scrolled A/B. C must start at its normal top.
4. While reading historical A, run `同步最新消息`. If the anchor message still exists after Sync, A must remain at the same semantic/visual point after refresh.
5. While reading historical A, run `重载当前会话`. If the anchor message still exists after rebuilt detail, restore it; if not, return to top and emit `scrollAnchor.discarded reason=message_not_found` rather than guessing another message.
6. Re-run b17 core regression spot checks: resident A->B->A must still avoid navigation-only refetch; hidden/coalesced operation behavior must not regress.

## Remaining Work before Stable

- b18 real-device semantic anchor acceptance above.
- Isolated target-only Reload replacement regression as applicable.
- Failed resident navigation with no implicit retry when a natural failure is available.
- Supported account-switch purge only when a real supported switch/logout path exists.
- Real process/system memory evidence before choosing a bounded normal LRU capacity; approximate text bytes remain insufficient.
- Non-personal workspace isolation remains Unknown / Unverified.

## Next exact action

Install/test exact Artifact `9638821912` / IPA SHA `296870630ac57f439d559a2b8b823094885d0362f547a190e48982696187877c` on the target iPhone/iOS17 device. Execute the b18 real-device acceptance matrix above and export diagnostics if any anchor case fails or if exact save/restore evidence is needed. Do not claim Runtime or Stable until that result exists; do not rebuild/reuse b18 for corrected code after this Artifact identity has been produced.
