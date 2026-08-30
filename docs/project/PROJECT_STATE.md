# Project State

_Last updated: 2026-08-31 through exact b65 Runtime pass and TD-029 production Send architecture selection. Phase 9 `DEV-send-stream` remains Active. Stable/Frozen Send remains No._

## Current accepted merged baseline

Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21, list-cache b23 and **Phase 8 b38** remain accepted merged baselines for their recorded scopes. Exact b38 tested source is `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`. Stable does not mean Frozen.

## Current Work / target

`DEV-send-stream` is Active on `dev/send-stream-20260829`; PR #29 remains open / mergeable / unmerged. Current actual `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; final target-main synchronization is required before any future merge.

Latest emitted/tested Candidate is **`DEV-send-stream-0.1.0-b65` / `0.1.0 (65)`**:

- exact product/config source `44138db766d00e62cfda7f20182f6d20f1ec3352`;
- product tree `fb02dfa7512e9c8428c4b0e9b7184a56d602f688`;
- Push `33328232044 / 99302071335` — success;
- PR `33328233842 / 99302076369` — success;
- Push Artifact `9736876465`;
- PR Artifact `9736874445`;
- Push ZIP `sha256:d9a52ecb0cd7d5131e22fc399bc5db0d573a9de3e5d80838f3a8d2b3164ceb7a`;
- IPA `sha256:e6a01b2eafd361b9df2567b002f9e8aa56b57dcee219c7999c65767b91138d16`;
- package Release / source marker `44138db766d0` / minimum iOS14 / UIDeviceFamily `[1,2]` / arm64.

Exact b65 Runtime on the primary iPhone/iOS17 passed the focused probe lifecycle: real protected Send -> HTTP200 SSE -> terminal, complete-looking reasoning/final, exact parent tool association `10/10`, and independent nested `工具输入` / `工具输出` disclosures with readable decoded output. Remaining spacing and legal slash escaping are non-blocking polish.

Evidence ladder for b65: **Code / diff audit / Push+PR CI / Artifact / package identity / focused Runtime passed; production Repository-owned Send still pending; Stable/Frozen No.**

## Durable Phase 9 architecture/security boundary

- Exact b42 proves successful ChatGPT-account protected Send requires browser anti-abuse challenge output. Pure-native/transient-auth account Send remains blocked.
- Separately billed API-product route remains rejected; primary-account Sub2API/Codex-subscription route remains blocked by the existing account-safety decision.
- **TD-029 is now the current production Send decision.** The user explicitly authorized the b48-b65 proven Native-composer -> covered official-Web page-owned protected-Send executor as the production transport mechanism.
- Native history/composer/reasoning/tool/final UI remains the product surface. Full existing-conversation mobile-Web rendering remains rejected by TD-025/TD-028.
- Covered official Web uses the existing default persistent `WKWebsiteDataStore`, owns only browser challenge/protected request execution, and is not a conversation/message/response authority.
- `ConversationRepository` remains sole native production conversation/list/detail/recovery/**response lifecycle** authority.
- `AuthSessionStore` remains auth/account authority; default persistent WebKit store remains sole persistent auth-secret authority.
- No challenge solving/replay, no second persistent credential store, no duplicate Send merely to obtain streaming data.
- Sync/Reload never resend/regenerate.

## Web Send maintenance capability

`docs/project/WEB_SEND_ADAPTER.md` is now the durable authority for:

- current evidenced official composer/protected-Send/SSE/reasoning/tool rules;
- exact boundaries that remain prohibited;
- future ChatGPT Web-rule change classification;
- the in-app development **Web Rule Lab** contract;
- the maintenance loop `reproduce -> user runs small JS probe in Lab -> evidence -> one minimal adapter update -> one coherent product build`.

The Web Rule Lab uses the same default persistent WebKit data store, is visibly presented while probing, accepts only user-triggered temporary JS, displays/copies/shares temporary results, and does not persist probe/result bodies into diagnostics or app storage.

## Current Send/stream evidence progression

- b45 Runtime Confirmed official no-resend `POST /backend-api/f/conversation/resume` with `{conversation_id, offset}` -> HTTP200 SSE; b46/b47 duplicated Native Cookie+Bearer-only resume returned HTTP404 JSON. Native first/exclusive resume remains Unknown / Unverified.
- b48-b51 established Native composer -> official protected Send and compact incremental text grammar, including fresh-new-chat continuation across `title_generation`.
- b52-b56 isolated reasoning/tool grammar and exact `reasoning_ended`, while keeping raw `assistant:thoughts` non-presentational.
- b57-b59 established Native reasoning/final split and exact service-marked thinking-preamble inclusion.
- b60 preserved later reasoning paragraph boundaries, presented event-driven `正在思考`, and proved exact invocation->result `parent_id` association.
- b61 exposed generic-textarea false readiness; b62 removed that selector and passed the verified-composer cold-launch path.
- b63 + same-run official-Web evidence authorized the bounded GitHub connector input/output mapping.
- b64 proved exact-parent GitHub detail lifecycle; Runtime rejected only escaped/dense detail rendering.
- b65 corrected only presentation and passed the focused structured-detail Runtime gate.

## Current implementation gap

Production source still uses the old transitional path in `RootViewController`: Native detail `发送消息…` pushes full-page `AuthWebViewController.hybridChat`, then returns and explicitly Syncs. `ConversationRepository` has no production Send/response lifecycle yet.

The next implementation must replace that normal path with:

`Native composer -> Repository response operation -> covered official Web one protected Send -> same-response SSE -> Repository-owned incremental response -> Native detail`.

Do not copy the Probe VC as a state owner; extract/reuse only the evidenced Web execution/interception logic.

## Shortest remaining Phase 9 sequence

1. Complete core docs + Web Rule Lab foundation.
2. Existing-conversation production Repository-owned Send/stream Candidate.
3. New-chat first Send and pending->authoritative handoff only if timing requires it.
4. Exact server Stop evidence and one response-scoped Stop implementation.
5. A/B hidden-response ownership + follow-tail/history intent.
6. Sync/Reload active-response safety + b38 geometry/round/time/Copy regression.
7. Final daily-chat Runtime matrix, target-main synchronization, Stable/merge decision.

Background notification/true-background and attachments remain subsequent Works after accepted text Send/Stream ownership.

## Remaining Unknown / Unverified

Production Repository-owned incremental-response Runtime, new-chat authoritative identity timing, exact server Stop mechanism, cross-conversation simultaneous server generation, cross-tool expandable-detail schema beyond the evidenced GitHub mapping, Native first/exclusive resume, full 5/15-minute background behavior, WebContent termination recovery, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified where not explicitly tested. CI/Artifact success is never Runtime proof.
