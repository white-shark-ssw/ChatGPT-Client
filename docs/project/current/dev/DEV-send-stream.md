# DEV-send-stream

## Status

**Active — Option 2 hybrid user-visible Web Send selected**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail / 官方 Web / hybrid`
- **Task**: deliver a usable ChatGPT-account Send path without circumventing browser anti-abuse protections. Native read/navigation remains the product shell; Send is now explicitly allowed to use a **user-visible official ChatGPT Web surface**.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; Stable predecessor b38 remains the merged native read/metadata/round-navigation baseline.
- **Working branch / PR**: `dev/send-stream-20260829`; PR #29 open + mergeable. Resume guard on 2026-08-29 verified branch/PR head `582cc67f3628cdf9cb33c7b5ea0a6b52b9a43ea3`, base `main@34811877896ca88c6656be6676f5466a19931ce6`, and no peer Active development checkpoint.
- **Candidate identity**: b39-b42 are permanently reserved. `DEV-send-stream-0.1.0-b43` is not present in the repository/build index at this selection point and is the next available identity if this implementation reaches a testable Artifact milestone.

## Exact b42 decision evidence retained

Exact `DEV-send-stream-0.1.0-b42`, source `e8946e48a0b5ad86b402faf5eabba627e3393adf`, Artifact `9709824510`, exact iPhone/iOS17 default `primary_assistant` new-chat Runtime established:

- `proofOfWorkRequired=true`;
- `turnstileRequired=true`;
- `soRequired=true`;
- Sentinel finalize submitted non-empty PoW and Turnstile before successful `POST /backend-api/f/conversation` SSE Send.

Therefore pure native/transient-auth Send remains blocked. This Work must not implement PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoints, or a hidden WebView used only to harvest challenge output.

## User architecture decision — Option 2

The user explicitly chose to proceed with the **Native shell + user-visible official-Web Send** direction after b42 Path B.

Hard product requirements:

1. The Web portion must feel as close as practical to native iOS controls on the primary exact device (iPhone 15 Pro Max / iOS 17.0). Functional Send alone is insufficient.
2. Ordinary return/re-entry must avoid unnecessary page reconstruction/reload. Keep the visible official-Web session resident/warm where lifecycle and memory evidence permit.
3. Native UIKit remains navigation/container owner around the Web surface.
4. No continuous DOM-observation/JS bridge chatter solely to mirror Web state into native UI.
5. Attachment entry is a hard UX gate: tapping `+` must not wait on Web/network/Sentinel/upload work before local selection UI begins presenting. Exact native-to-Web file handoff remains Unknown / Unverified until separately evidenced.

## First hybrid implementation milestone — planned b43

The first testable implementation is deliberately narrow and evidence-backed. It validates the hybrid surface before deeper integration:

- add one **user-visible official ChatGPT Web chat surface** using `WKWebView` + the existing default persistent `WKWebsiteDataStore`;
- the surface loads the already evidenced official root `https://chatgpt.com/` only while being presented; no hidden preload/challenge harvesting;
- Root owns one persistent controller/WebView instance so pop -> re-enter can reuse the same loaded session rather than reconstructing the page;
- expose native entry from the conversation list and selected-conversation overflow menu;
- do **not** guess a `/c/<conversation-id>` deep-link or DOM automation in this milestone; current-conversation Web targeting remains separately Unverified;
- no protocol-probe injection, prompt/answer scraping, token capture, or browser proof extraction;
- safe diagnostics may record surface presentation/reuse, navigation class/host, first-load/reload duration and failure class only;
- existing native list/detail/recovery/round navigation remains unchanged except for the explicit Web entry affordance.

### b43 exact-device Runtime focus

- first entry: native transition appears promptly and official page becomes usable without app-level UI stall;
- resident re-entry: pop -> re-enter does not perform avoidable full-page reconstruction/reload;
- keyboard show/hide, typing, Send, streamed response scrolling and rapid scrolling feel acceptably close to native;
- official Web `+` / attachment entry is exercised for responsiveness observation; if it materially lags, do not call hybrid UX accepted and investigate a safe native-picker path separately;
- native Back/return is smooth and native read UI remains intact;
- no hidden challenge/proof/token data appears in diagnostics.

## State-owner boundary

- `ConversationRepository` remains sole native conversation/list/detail/recovery authority.
- `AuthSessionStore` remains auth/account authority.
- default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- `RootViewController` remains single native compact navigation owner.
- The user-visible official-Web surface owns its own browser-side Web Send/challenge execution while visible; it is **not** a second native conversation repository and does not become native message authority.
- Native Sync/Reload continue to never resend/regenerate.

## Non-atomic batch recovery point — hybrid implementation

Known start state:

- branch/PR head: `582cc67f3628cdf9cb33c7b5ea0a6b52b9a43ea3`;
- base: `main@34811877896ca88c6656be6676f5466a19931ce6`;
- PR #29 open + mergeable;
- exact b42 product source/Artifact remain `e8946e48a0b5ad86b402faf5eabba627e3393adf` / `9709824510`;
- no peer Active dev task;
- b43 identity available but not yet emitted.

Planned batches:

- **Batch A — complete by this write**: record user selection of Option 2, hard smoothness/attachment requirements, first hybrid milestone and recovery state.
- **Batch B — pending**: minimal product code for persistent user-visible official-Web chat surface + native entry affordances; inspect diff for Stable b38 regressions.
- **Batch C — pending**: if code is testable, allocate unique b43 in Xcode/workflow metadata, then run CI/package path. Once emitted, b43 becomes permanently reserved.
- **Batch D — pending**: verify exact Artifact/IPA identity and hand exact IPA to user for real-device hybrid smoothness/attachment-entry test.
- **Batch E — pending**: record CI/Artifact/Runtime evidence and update durable docs/PR body according to actual results.

Recovery rules:

- never replay or rewrite b39-b42 identities/Artifacts;
- do not redefine exact b42 product source;
- do not weaken Stable b38 geometry/round/navigation contracts;
- do not merge PR #29 as production Send acceptance before exact hybrid Runtime evidence supports the claimed scope;
- do not implement unverified deep-link/file-input/DOM automation merely to accelerate the milestone.

## Next exact action

Implement Batch B from the real branch source: add the persistent visible official-Web chat controller under Root ownership and native entry actions with privacy-safe diagnostics. Then inspect the exact diff before allocating b43.
