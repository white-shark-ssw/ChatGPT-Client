# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-09-01 through exact DEV-send-stream b79 Code/static/Simulator/Push+PR CI/Artifact/package verification; the next gate is b79 real-device Runtime._

## Current DEV-send-stream b79 gate — 2026-09-01

- Exact candidate `DEV-send-stream-0.1.0-b79` / `0.1.0 (79)`; source `a3d307b05d70e95568672bc29b0c939b7f3b8141`; Push `33489654106 / 99797864816`; PR `33489658656 / 99797878467`; canonical Artifact `9793240789`; IPA SHA `39f64dd9146c3a8dc28cb9b733d1c56d4fbf3ff090a442c8ecbd27c672234fb4`.
- b79 implements only the b78 Runtime-backed corrections: neutral reasoning/tool transition spacing, explicit-manual-Sync same-page re-arm after a changed latest user turn, and preservation of external stopped-thinking reasoning instead of synthesizing final body text.
- External reasoning/tool continuation remains page-snapshot granular. External progressive final still has no authorized progressive source; do not fake it. Automatic Sync remains future evidence work and must not be implemented as fixed polling.
- **Next gate is Human Runtime:** verify symmetric tool spacing, manual Sync adopts an already-open conversation's newly-started external response, stopped external reasoning displays as stopped reasoning rather than body text, and retained b67/b72 behavior where practical. Stable/Frozen remains No.

## Purpose / delivery principles

Build a genuinely usable native Swift/UIKit ChatGPT client while preserving one authority per state domain. Current real source, exact CI/Artifact evidence, exact-device Runtime evidence and the latest explicit requirements outrank stale plans.

Core rules: no speculative retry/fallback/timer/watchdog/polling/duplicate state; distinguish Code / static-local / CI / Artifact / Runtime / Stable; private Web behavior must be measured rather than guessed; full Web conversation rendering remains rejected as the daily-chat dependency.

## Accepted merged foundation

- Phase 1 `DEV-app-foundation`: merged Stable.
- Phase 2 `DEV-auth-bootstrap`: merged Stable for recorded scope.
- Phase 3 `DEV-protocol-read`: merged accepted diagnostic evidence.
- Phase 4 `DEV-native-read-path`: merged Stable b9; `ConversationRepository` is native conversation authority.
- Phase 5 `DEV-conversation-recovery`: merged Stable b15.
- Phase 6 `DEV-multi-conversation-state`: merged Stable b21; Frozen No.
- Phase 7 `DEV-conversation-list-cache-core`: merged Stable b23; Frozen No.
- Phase 8 `DEV-conversation-round-count`: merged Stable b38; exact tested product source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`; Frozen No.

Retain b38 bounded long-message chunks, deterministic geometry/manual layout, full-message Copy semantics, semantic rounds and continuous O(1)-target round navigation.

## Phase 9 — `DEV-send-stream` — Active production integration

### Current b76 candidate / next gate — 2026-09-01

- Exact candidate `DEV-send-stream-0.1.0-b76` / `0.1.0 (76)`; source `0da5a7577f2cf3b2a6882d8a0ec920b5c8f37c71`; Artifact `9775920927`; IPA SHA `b130c9059ec85d08d95105b32b71157a4be2b2ecea25112963f0a548ec252bcd`.
- Guarded scope/Simulator passed; Push `33440101178 / 99645927061` and PR `33440098527 / 99645917529` passed; package identity independently verified.
- Current external-response design observes only page-owned status/plural reads after current resume 404, validates target identity and atomically projects the latest-user-bounded service segment into the Repository response owner. No Native polling/cadence/resume construction/WebSocket body path. Actual HTTP200-SSE page-owned resume remains supported under strict validation.
- b76 also tests 30/21/21 vertical rhythm.
- **Next gate is Human Runtime:** cross-platform active-response adoption, b67 local Send regression, b72 concurrent-ownership regression, visual spacing, and worst-case Back responsiveness if reproduced. Stable/Frozen remains No.

### Durable authority / transport boundary

- `ConversationRepository` remains the sole production conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` remains sole native auth/account owner.
- `WKWebsiteDataStore.default()` remains sole persistent auth-secret authority.
- b42 proves ChatGPT-account protected Send requires browser anti-abuse challenge output; pure-native/transient-auth protected Send remains blocked.
- TD-029 is the current production architecture: Native action -> Repository response operation -> covered official page performs exactly one protected Send/challenge flow -> same-response accepted SSE -> Repository incremental reasoning/tool/final state -> Native presentation.
- Covered official Web is transport/challenge execution only. It is not a conversation/message/response/list/draft/scroll-state authority.
- Native must not solve/synthesize/replay Sentinel/PoW/Turnstile/conduit/challenge values.
- Full official-Web conversation rendering and the b44 Native->Web->Native daily-chat form remain rejected.
- Final Composer hierarchy/drafts/attachment staging remain future serialized `DEV-composer-parity`; this Work retains only the minimum validation UI required to accept Send/response semantics.

### Accepted protocol / parser progression

- b45 Runtime Confirmed official no-resend continuation behavior; b46/b47 duplicated Native Cookie+Bearer-only resume remained rejected.
- b48-b51 established Native composer -> official protected Send and compact response text continuation, including exact `title_generation` preservation.
- b52-b60 established visible reasoning/final classification, exact `reasoning_ended`, service-marked thinking preambles and exact result-parent association. `assistant:thoughts` remains non-presentational.
- b61/b62 rejected generic textarea readiness and accepted only the evidenced composer path.
- b63-b65 authorized the narrow exact-parent GitHub tool-detail mapping and passed the focused diagnostic Runtime gate.
- b67 accepted the production existing-conversation TD-029 transport: one Native Send -> one official protected `/backend-api/f/conversation` -> HTTP200 `text/event-stream` -> Repository reasoning/tool/final -> terminal/reconcile.
- b72 exact Runtime positively supports the tested A-generating + B-send/generate simultaneous-generation ownership path. This is evidence for that exact matrix, not a claim about arbitrary overlap.

### b73-b75 daily-chat / external-continuation progression

- b73 retained successful local Send while exposing long resident geometry rebuild cost, insufficient tool vertical rhythm and the external-active-response lifecycle gap.
- b74 packaged first external active-response adoption based on historical visible-Web evidence that the official page can issue matching `/backend-api/f/conversation/resume` SSE. Its Runtime exposed false external failure before response validation and additional geometry/presentation defects.
- b75 added the required response-acceptance gate and cooperative presentation-geometry scheduling while preserving b67 local Send and b72 tested multi-conversation ownership.

### Exact b75 identity / evidence

- Candidate: `DEV-send-stream-0.1.0-b75`
- Version / Build: `0.1.0 (75)`
- Exact product/config source: `b77303b8870dc25851dbffbf38ffc153a47bbcb2`
- Assembly validation: `33429163152` — exact scope + `git diff --check` + Xcode 16.4 Simulator build passed
- Push CI: `33429597213 / 99611443839` — success
- PR CI: `33429599704 / 99611451360` — success
- Canonical Push Artifact: `9772079468`
- Artifact ZIP: `sha256:6c4c4ec9de54264846376bdf7df4679daaaf33168481831698c884093b6209ad`
- IPA: `ChatGPTClient-0.1.0-b75-dev-send-stream.ipa`
- IPA SHA: `a912547a1845cae182d83d551eb51955b5060062f66ec3fbdf14be45954dab9d`
- Independent package inspection: Release `0.1.0 (75)`, Candidate b75, source marker `b77303b8870d`, minimum iOS14, arm64
- b39-b75 are permanently reserved.
- Evidence ladder: Code / exact static-local / Push CI / PR CI / Artifact / package identity passed; exact Runtime partial/rejected; Stable/Frozen Send No.

### Exact b75 iPhone/iOS17 Runtime qualification

Positive evidence:

1. **False external failure suppression passed.** A page-owned matching `/resume` request no longer creates a Repository external response before exact HTTP200 `text/event-stream` acceptance. The observed 404 cases therefore did not surface the former false Native `回答失败`.
2. **Cooperative geometry path is active.** Cache misses report `geometryMode=cooperative_main_queue`; resident reuse reports `geometryMode=resident_cache`, `geometryReused=true`. This run does not prove the former worst-case Back responsiveness because that extreme case was not reproduced.

Rejected / open evidence:

1. **Cross-platform active-response adoption failed in covered production.** While another platform's response was still actively reasoning, entering the same conversation in Native, Sync, Reload, background/foreground and process relaunch never produced Native live reasoning/tool/final rows. `livePresentationRowCount` remained 0.
2. In three separate covered-production attempts the official page itself issued a matching `/backend-api/f/conversation/resume`, but every observed response was HTTP404 `application/json` rather than an accepted SSE response.
3. Authoritative Detail later advanced visible messages, but server-backed reconciliation is not a substitute for live reasoning/tool SSE.
4. b75 typography values tool `26`, reasoning `18.2`, final `18.2` were implemented but visually rejected by the latest exact screenshot/feedback as too tight. Those numbers are not an accepted presentation baseline.

### Current Web Rule Lab evidence gate before b76

Historical visible-Web evidence showed `stream_status` HTTP200 and a page-owned `{conversation_id, offset}` resume returning HTTP200 SSE. Exact b75 covered production contradicts any assumption that this visible-Web behavior automatically applies to the covered executor.

Therefore the next step is evidence-only, using Settings -> Web Rule Lab on the same logged-in `.default()` WebKit store while another platform owns a still-active response. Capture only privacy-safe structural facts:

1. whether page-owned `GET /backend-api/conversation/{id}/stream_status` occurs and its status/content-type;
2. count/order of matching page-owned `/backend-api/f/conversation/resume` attempts;
3. resume request JSON key names only plus each response status/content-type;
4. whether any later page-owned HTTP/SSE transport follows an initial resume 404;
5. WebSocket remains structural-only unless separate exact evidence proves reasoning/final body authority.

Do not capture Cookie/Authorization/challenge values, raw account/conversation/message/response IDs, prompt/answer/reasoning bodies or tool bodies. Do not send a message from the Lab for this probe.

Until this evidence arrives, do not add Native resume/offset construction, `stream_status` polling, retry/timer/watchdog, guessed alternate route fallback, duplicate Send, delayed resend or WebSocket body parsing.

### b76 allocation rule

b76 is permitted by concrete b75 defects but remains **unallocated**. Allocate `DEV-send-stream-0.1.0-b76` / `0.1.0 (76)` only after:

- the Web Rule Lab evidence defines one minimal current continuation-transport correction;
- the rejected reasoning/tool/final vertical rhythm has one coherent visual correction;
- a fresh identity/conflict guard confirms b76 remains globally unused.

Then make one evidence-backed product change set, run static/local checks, Push/PR CI, independently verify package identity, and hand one exact b76 Artifact to the user for real-device Runtime. CI/Artifact success is not Runtime proof.

### Shortest remaining Phase 9 sequence

1. resolve the current external active-response continuation rule from Web Rule Lab evidence and, if justified, ship one b76 correction together with the already-evidenced visual-spacing correction;
2. re-accept local b67 Send and tested b72 A/B ownership regression paths on the coherent candidate as affected;
3. new-chat first Send and pending->authoritative handoff only if actual timing requires it;
4. establish exact server Stop evidence before implementing response-scoped Stop;
5. close A/B hidden-response ownership + follow-tail/history intent and Sync/Reload active-response safety;
6. run final b38 geometry/round/time/Copy regression plus daily-chat Runtime matrix;
7. final target-main synchronization, fresh CI/Artifact if tested code changes, Stable/merge decision for PR #29.

### Official-like response lifecycle target

`发送 -> 正在思考 -> 思考流 -> 可选工具调用 -> 再次正在思考/思考流 -> reasoning_ended -> 自动折叠思考 -> 完整最终回答`.

Tool phases remain optional and must follow actual service events. General Markdown/code/table/link/citation rendering remains future `DEV-message-rendering`.

### Background ordering

Background resilience remains a hard product requirement but follows accepted production response ownership. b45 positive short-background evidence remains historical support; full 5/15-minute, WebContent termination, network-transition and TrollStore true-background work remain later isolated Runtime gates. Do not create a second response owner merely for background continuation.

## Future serialized `DEV-composer-parity`

After current Send/Stream lifecycle acceptance, implement the final official-like Composer hierarchy: bounded multiline auto-growth/full-screen editor, keyboard/layout behavior, per-conversation drafts, photo/video/file staging/preview, mode/reasoning controls and final Send/Stop button presentation. Do not move Send/response authority out of `ConversationRepository`.

## Phase 10 — `DEV-attachments`

High priority but Send-boundary dependent. Preserve iOS17 native photo+video requirements; do not use unsupported private WebKit/DOM file-input injection. Native upload/handoff needs separate current evidence.

## Phase 11 — `DEV-message-rendering`

Implement native Markdown/code/table/link/citation presentation only from authoritative user-visible content; never expose hidden reasoning/tool/system content.

## Later phases

Conversation-list preview, Markdown export, long-conversation profiling beyond accepted b38 geometry, download manager, pagination, production background completion/notification, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat, settings/diagnostics refinement and later advanced capabilities remain isolated Works.

## Current next action

Keep PR #29 open/unmerged and exact b75 as the current rejected Runtime package. Perform the privacy-safe Web Rule Lab continuation re-probe described above. Do not allocate b76 and do not change production continuation code until that Human Gate returns current page-owned transport evidence.
