# DEV-send-stream

## Status

**Active — exact b65 passed the focused iPhone/iOS17 structured GitHub tool-detail Runtime gate. The b64 formatting defect is closed for the tested shapes; remaining input/output spacing and legal escaped-slash display are non-blocking polish and do not justify b66. The next Phase 9 blocker is no longer Web/SSE/tool parsing: it is the production Send architecture boundary. Current TD-024/TD-025/TD-028 explicitly prohibit promoting the b48-b65 covered/hidden Web composer automation into production. `ConversationRepository` must remain the production response owner. Stable/Frozen Send remains No. PR #29 remains evidence-only / open / mergeable / unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / not merged; evidence-only
- Other Active development checkpoints: none at latest guard
- Current actual `main`: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`
- Current branch head before this checkpoint update: b65 Runtime evidence commit `8af400f859b12406310596eba87daac215c34c94`
- Stable native predecessor: b38
- Exact latest Runtime-tested Candidate: `DEV-send-stream-0.1.0-b65`
- Exact b65 product/config source: `44138db766d00e62cfda7f20182f6d20f1ec3352`
- Exact b65 product tree: `fb02dfa7512e9c8428c4b0e9b7184a56d602f688`
- b65 Push Run / Job: `33328232044 / 99302071335` — success
- b65 PR Run / Job: `33328233842 / 99302076369` — success
- b65 Push Artifact: `9736876465`
- b65 PR Artifact: `9736874445`
- b65 Push Artifact ZIP SHA-256: `d9a52ecb0cd7d5131e22fc399bc5db0d573a9de3e5d80838f3a8d2b3164ceb7a`
- b65 IPA SHA-256: `e6a01b2eafd361b9df2567b002f9e8aa56b57dcee219c7999c65767b91138d16`
- b65 package: Release / `0.1.0 (65)` / Candidate `DEV-send-stream-0.1.0-b65` / source marker `44138db766d0` / iOS14 / `[1,2]` / arm64
- b39-b65 emitted identities: permanently reserved
- b66: **not allocated**

## Exact b65 Runtime — focused pass

User export: `ChatGPTClient-Diagnostics-20260830-191806.json`.

Package identity matched exact b65: Release / build65 / Candidate b65 / source `44138db766d0` / iPhone / iOS17.0.

Observed path:

`ready=false/none -> ready=true/prompt_textarea -> nativeSubmit -> submitted -> sendObserved(existing_conversation) -> HTTP200 text/event-stream -> thinking/reasoning/tool/final -> terminal`.

Terminal metrics:

- frameCount `132`, terminal `true`;
- exact reasoning-end `1`, fallback false;
- Native reasoning `14 deltas / 295 chars`;
- Native final answer `71 deltas / 2827 chars`;
- Native total `85 deltas / 3122 chars`;
- thinking preambles `2 / 13 chars`;
- reasoning-active signals `2`;
- service/native reasoning segment breaks `1/1`;
- invocation identities `10`, results `10`;
- parent present/matched/unmatched/missing `10/10/0/0`;
- Native tool presentations/completion updates `10/10`;
- Native detail-available rows `9`.

User directly reported no apparent reasoning/final truncation. Completed tool rows expanded/collapsed; `工具输入` and `工具输出` appeared as independent second-level disclosures; decoded output no longer showed b64's second-layer JSON escape wall.

Observed remaining polish only: child-section vertical spacing is looser than desired and pretty JSON may display legal `\/` slash escaping. These do not indicate data loss or protocol/ownership failure and do not justify another Candidate by themselves.

Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b65-runtime.md`.

Classification: **b65 focused Runtime pass. Formatting defect closed for tested GitHub shapes. Stable/Frozen No.**

## Diagnostic evidence now accepted for production design

The b48-b65 diagnostic series has established, for the tested primary account/device scope:

- page-owned official protected `/backend-api/f/conversation` Send can be triggered and observed;
- accepted compact SSE text grammar including `title_generation` continuation;
- explicit thinking-preamble inclusion and exact `reasoning_ended` transition;
- event-driven `正在思考` / reasoning / final presentation ordering;
- exact invocation -> result association only by response-local `parent_id`;
- bounded GitHub connector input/output mapping and readable nested tool detail;
- verified-composer authority is `#prompt-textarea` or explicit contenteditable role=textbox; generic textarea is rejected;
- no retry/timer/watchdog/polling is required for the accepted diagnostic path.

These are protocol/presentation evidence, not automatic production-architecture approval.

## Production architecture gate — requires explicit product decision

Current source truth:

- `RootViewController` production detail still exposes a `发送消息…` toolbar that pushes the visible full-page `AuthWebViewController.hybridChat`, then performs explicit Native Sync.
- `ConversationRepository` has accepted per-conversation resident/detail ownership but no production response/send lifecycle yet.
- `NativeWebSendEngineProbeViewController` drives a page-owned composer from Native while the official Web content is covered by a Native surface. That is a diagnostic exception only.

Current durable TD boundary:

- TD-023: pure-native/transient-auth protected Send is blocked by browser anti-abuse challenge output.
- TD-024: a **user-visible official-Web Send surface** is security-permitted; hidden/shadow Send automation is rejected.
- TD-025: the b44 full-page Native -> Web -> Native product form is rejected; Native input forwarding into a covered/hidden official Web composer is explicitly not accepted.
- TD-028: full existing-conversation mobile-Web rendering is not viable as the daily-chat dependency after long-conversation composer failure.

Therefore the production response-owner integration cannot safely start by silently copying the b65 covered-Web engine into `ConversationRepository`. One explicit product architecture choice is required before product code proceeds:

### Option A — retain current TD security/product boundary

Use a genuinely user-visible official Web composer/Send region for protected Send, while Native owns conversation history, streamed response state, reasoning/tool/final presentation and per-conversation lifecycle. Avoid rendering the full Web conversation. This keeps the browser challenge flow user-visible and avoids promoting hidden Web automation.

### Option B — explicitly revise TD-024/TD-025

Authorize the currently tested Native-composer -> covered official-Web composer/page-owned Send engine as the production transport mechanism, while `ConversationRepository` becomes the sole response/conversation state owner and Web remains transport/challenge execution only. This is the shortest engineering path from b65 to a native-looking daily-chat loop, but it is a deliberate reversal of the current hidden/shadow-Web prohibition and must be user-approved before implementation.

No third evidence-backed ChatGPT-account Send route currently exists. Pure-native and separately billed/subscription bridge routes remain rejected by existing decisions.

## After architecture choice — shortest completion order

1. Existing-conversation production Send/stream slice: add Repository-owned response lifecycle and drive one selected existing conversation through the chosen protected-Send surface; update Native detail incrementally without a second message owner.
2. New-chat first Send: establish pending -> authoritative conversation identity only if current observed identity timing requires it; no fake server IDs.
3. Stop evidence + exact response-scoped Stop implementation; local task cancel alone is not server Stop.
4. Active-response navigation/follow-tail: A may continue while B visible; intentional upward scroll exits follow-tail; hidden growth never mutates B viewport.
5. Sync/Reload active-response safety and b38 geometry/round/timestamp/Copy regression.
6. Final exact daily-chat Runtime matrix, target-main synchronization, then decide Stable/merge. Background-notify remains next Work after accepted production response ownership and does not block this Phase 9 closure.

## Recovery point

b65 is permanently reserved and accepted for the focused diagnostic Runtime scope. Do not allocate b66 for spacing or escaped-slash polish. Do not modify production Send code until Option A vs Option B is explicitly resolved. Once resolved, update the relevant TD before or in the same product-code cycle and allocate the next unique Candidate only when a coherent testable production slice exists.

## Next exact action

Ask the user to choose Option A or Option B. This is a genuine product/security architecture gate under repository governance, not a routine progress approval. After the choice, continue autonomously through the smallest existing-chat production Send/stream Candidate, CI/Artifact/package verification, then hand the exact IPA for Runtime testing.
