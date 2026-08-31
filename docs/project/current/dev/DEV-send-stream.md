# DEV-send-stream

## Status

**Active — b67 protected-Send transport remains Runtime accepted. Exact b71 package is valid/reserved but the user's current iPhone/iOS17 recording rejects its reasoning/tool interaction hierarchy and exposes a cross-conversation send serialization defect. b72 is now justified by exact Runtime + explicit product requirements. Stable/Frozen Send remains No; PR #29 stays open/unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Formal branch head before this duration-format checkpoint write: `d078b681b03063981f711c24f3422bd34f44693e`
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Exact b71 product/config source: `af8d4a4b291c05fb63a50cee0261c06d7ce474d3`
- Candidate: `DEV-send-stream-0.1.0-b71`
- Version / Build: `0.1.0 (71)`
- b71 Push CI: `33388396118 / 99476130099` — success
- b71 PR CI: `33388399484 / 99476140778` — success
- b71 Artifact: `9756491305`; ZIP `sha256:74b554c98333e365b03073a39b0286f966b98c94ec2a695d62b81cb4f8f7bda0`
- b71 IPA SHA: `a9322dba9351842ac2d2374a1f8792129fe64750a1c79da514e2444bb785fd65`
- Built identity independently verified: Release `0.1.0`, Build `71`, Candidate b71, source marker `af8d4a4b291c`, minimum iOS14, arm64
- b39-b71 permanently reserved; never rewrite/reuse b71
- Repository search found no existing `DEV-send-stream-0.1.0-b72` before allocation
- Stable/Frozen Send: No

## Exact b71 Runtime rejection / latest explicit requirements — 2026-08-31

User evidence:

- current mixed recording `RPReplay_Final1788178603.mp4`: first section is Build71 client interaction/presentation; later section is the official ChatGPT iOS app on the same answer;
- current official screenshots extracted from that comparison;
- user-supplied decrypted official app archive `ChatGPT_Decrypted.zip` used only as local UI/resource evidence;
- official asset probe already confirmed real local resources including GitHub, browse/search, terminal/code/file-code/globe and connector-family icons plus official chevrons. Asset existence does not itself prove event->icon mapping.

The latest user requirements supersede b71's reasoning-sheet interaction assumption.

### 1. Main-conversation reasoning disclosure

- `思考了 <duration>` / `思考过程` is the expand/collapse control for the **entire visible reasoning/tool timeline of that assistant turn**.
- Expanded conversation content stays inline and preserves actual chronology: `reasoning -> tool -> reasoning -> tool -> ...`.
- Collapsing hides both reasoning text and all tool rows for that turn.
- Tapping the thinking disclosure never opens the secondary sheet.
- Visible reasoning text belongs only to this first-level conversation expansion. It must not be copied into the tool sheet.
- `assistant:thoughts` / `inline_cot_expandable_content` remain strictly non-presentational.

### 1.1 Official reasoning-duration format

Latest explicit user requirement:

- keep using the exact service-backed `finished_duration_sec` / `reasoningEnded(durationSec)` value only; do not infer elapsed time from wall-clock gaps;
- below one minute, display seconds only: e.g. `7s`, `59s`;
- at the minute threshold and above, stop rendering one large pure-seconds value and format as accumulated minutes plus remaining seconds: e.g. `1m`, `1m 5s`, `25m 32s`;
- when the remaining seconds are zero, omit the trailing `0s` (`60s -> 1m`);
- the largest display unit remains **minutes**. Never switch to hours; e.g. `3632s -> 60m 32s`;
- the same formatter must be used everywhere the reasoning duration appears, including the first-level summary and any status row in the secondary tool sheet.

### 2. Tool row -> secondary sheet

- The sheet entry is tapping **any concrete tool operation row**.
- Regardless of which tool row was tapped, the sheet represents the current assistant turn's **ordered tool-call list** and shows every eligible tool operation in real invocation order.
- Do not invent auto-scroll-to-clicked behavior until the user supplies that requirement; default presentation begins from the list's natural top.
- Sheet title/presentation follows the supplied official reference (`正在思考`, rounded/dimmed sheet semantics).
- The sheet contains tool operations only; no reasoning prose appears there.
- For each eligible tool item, show icon + tool title and then the authorized **tool input content directly**.
- Remove the `工具输入` heading and its disclosure affordance. Input is expanded by default.
- Hide tool output completely in this product presentation: no `工具输出` heading, disclosure, body or nested output scroll container.
- One outer sheet scroll surface owns overflow. Tool input grows intrinsically and pushes later tool items downward.

### 3. Tool icons / disclosure icon parity

- All tool rows must not reuse the GitHub mark.
- Use the real tool/connector identity already present in current service/event data when available. Do not guess an API or pair by title when an identity field exists.
- User-supplied official app assets may be used as visual evidence/local resources for exact icon shape. The decrypted archive contains built-in GitHub/browse/code/terminal/globe/connector-family assets and official chevrons.
- Before implementation, correlate currently available response metadata/recipient/tool identity with a bounded local icon enum. Unknown tool identity uses one neutral generic mark; it never masquerades as GitHub.
- `思考了 <duration>` chevron must be brought to the official visual scale/baseline rather than the current oversized/rough presentation.
- No remote icon loader, persistent icon cache or second state owner is authorized by this requirement.

### 4. Cross-conversation simultaneous generation

- Current Build71 behavior that changes B's send control to `其他会话回答中` while A is generating is rejected.
- Official product behavior required by the user: A may keep generating while B independently sends/generates.
- The send control for B is governed by **B's own active-response state**, not a global active response in A.
- At most one active response per conversation remains the initial ownership guard; unrelated conversations must not be globally serialized.
- This requirement is consistent with TD-019 / SEND_STREAM_PREFLIGHT: foreground selection is presentation only, hiding A never cancels A, and response ownership is per conversation.
- The current covered-Web executor is known to have a single `activeEvents` busy gate from b67. Do not guess that one WKWebView can safely run two page-owned protected Sends simultaneously. Inspect the real executor/Repository bridge first and make the smallest evidence-backed ownership change. No retry, queue timer, polling, fallback or duplicate Send is allowed.

## Retained accepted boundaries

- b67 one local Send -> one real protected official-page Send -> HTTP200 same-response SSE -> Repository updates -> terminal/reconcile remains the accepted production transport predecessor.
- `ConversationRepository` remains sole conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` remains sole account authority; default `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Covered official Web remains browser challenge/protected-Send executor only; full Web conversation rendering stays rejected.
- b69 chronological response timeline and exact-parent result association remain retained.
- b38 deterministic long-message geometry/quick navigation remains accepted and must not regress.
- No retry/polling/timer/watchdog/fallback/compatibility shim/second message or response store.

## b72 source-inspection / implementation scope

Exact b71 source inspection now establishes:

1. main-conversation `思考了 Ns` currently binds directly to `presentReasoningDetail(...)`, and main cells always pass `reasoningExpanded: false`; this is the wrong first-level owner for the latest requirement;
2. the current secondary sheet iterates the entire reasoning+tool timeline and renders nested `工具输入` / `工具输出` disclosures; this is the wrong second-level hierarchy;
3. `ConversationRepository` already stores live response snapshots per conversation ID and only rejects another response in the **same** conversation;
4. current cross-conversation serialization is introduced by Root's single process-wide `CoveredWebSendExecutor.isBusy` gate and its `其他会话回答中…` send-control state;
5. current bridge carries response-local invocation recipient, exact-parent result metadata, `invoked_resource.app_name` for evidenced connector results, and a bounded `ConversationToolIconKind`; current mapping is too coarse (`GitHub` only after exact matched result; most other connector calls generic; non-connector invocations code);
6. current reasoning-duration presentation inserts raw seconds directly in more than one place and therefore must be centralized behind the b72 minute-level formatter above.

Frozen minimum b72 product/config surface from those facts:

- `ChatGPTClient/Conversation/ConversationFeature.swift` — first-level inline reasoning/tool disclosure, local row-delta geometry update, tool-row sheet entry, ordered input-only tool list, centralized duration formatting, bounded icon presentation;
- `ChatGPTClient/RootViewController.swift` — per-conversation covered-executor ownership/send availability and any bounded icon identity pass-through required by existing event data; no protected route/selector/challenge/SSE grammar change;
- bounded local image resources + asset catalog metadata only for official-provided icon shapes that have direct identity evidence;
- `ChatGPTClient.xcodeproj/project.pbxproj` and `.github/workflows/ios-foundation.yml` only when allocating Build72/Candidate identity.

Do not touch `AuthSessionStore.swift`, Stop/new-chat/background/attachments/Composer work unless direct source evidence proves this b72 requirement cannot be implemented without that owner.

## b72 batch recovery point

Known facts before product writes:

- formal branch head before this duration-format checkpoint write was `d078b681b03063981f711c24f3422bd34f44693e`; its parent is exact b71 product source `af8d4a4b291c05fb63a50cee0261c06d7ce474d3` and the `d078...` delta is checkpoint/docs only;
- b71 Artifact/package identity is valid and permanently reserved;
- PR #29 is open/mergeable/unmerged; its body is stale and will be synchronized only after the next actual candidate evidence milestone;
- `main` remains `d323b9eed2dda75b9986fc06e14014d3e9b365fb`;
- `docs/project/current/dev/` contains only this Active checkpoint plus README;
- b72 Candidate search was empty before allocation;
- source owner inspection described above is complete; no product write has yet been claimed for b72;
- orphan/tooling/docs assembly refs from b71 are not formal Work/Candidate authority and must not be replayed onto the formal branch.

Planned non-atomic batches:

1. this checkpoint now contains b71 Runtime rejection, b72 hierarchy/concurrency/icon requirements, exact minute-level duration formatting, owner inspection and recovery state;
2. re-read resulting formal head, PR/main/current-dev/candidate state;
3. allocate earliest unique Build72/Candidate after Guard and assemble the minimal product/config change on an isolated tooling/product ref;
4. run exact scope audit, `git diff --check` and real Xcode Simulator compile before formal advance;
5. emit a clean product/config commit with no tooling files, audit semantics, repeat formal Guard, then non-force fast-forward formal branch;
6. obtain exact Push + PR CI and one canonical Build72 Artifact; independently verify ZIP/IPA/Info.plist/source marker/arm64/iOS minimum;
7. update checkpoint + durable project docs + PR #29 from actual evidence;
8. stop only at exact iPhone/iOS17 Runtime gate: compare inline reasoning disclosure, minute-level duration, ordered tool-list sheet/input-only details/icon mapping/chevron scale and A+B simultaneous generation behavior against the supplied official app evidence.

## Evidence ladder

- b67 protected-Send transport: Runtime accepted.
- b69 ordered timeline direction: retained.
- b70: package valid/reserved; presentation Runtime rejected.
- b71: Code/scope/Simulator/Push+PR CI/Artifact/package verified; current user recording **Runtime rejects interaction hierarchy and cross-conversation serialization**; package remains reserved.
- b72: justified by exact Runtime + explicit requirement; product source/CI/Artifact/Runtime not yet claimed.
- Stable/Frozen Send: No.

## Next exact action

Re-read the resulting formal branch head and run the Resume/Conflict/Candidate Guard. Then allocate Build72 and assemble the smallest product/config candidate implementing the now-frozen b72 source scope, including the shared minute-level reasoning-duration formatter. Do not modify b71 identity or accepted b67 transport grammar.