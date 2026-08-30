# Project State

_Last updated: 2026-08-31 through exact b64 Runtime and exact b65 Code/CI/Artifact/package verification. Phase 9 `DEV-send-stream` remains Active. Stable/Frozen Send remains No._

## Current accepted merged baseline

Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21, list-cache b23 and **Phase 8 b38** remain accepted merged baselines for their recorded scopes. Exact b38 tested source is `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`. Stable does not mean Frozen.

## Current Work / target

`DEV-send-stream` is Active on `dev/send-stream-20260829`; PR #29 remains open / mergeable / unmerged and evidence-only. Current actual `main` remains `1ac202c972f2dee6945fe8d0688df8e10f5d462c`; final target-main synchronization is required before any future merge.

Current exact Artifact Candidate is **`DEV-send-stream-0.1.0-b65` / `0.1.0 (65)`**:

- exact product/config source `44138db766d00e62cfda7f20182f6d20f1ec3352`;
- product tree `fb02dfa7512e9c8428c4b0e9b7184a56d602f688`;
- Push `33328232044 / 99302071335` — success;
- PR `33328233842 / 99302076369` — success;
- Push Artifact `9736876465`;
- PR Artifact `9736874445`;
- Push ZIP `sha256:d9a52ecb0cd7d5131e22fc399bc5db0d573a9de3e5d80838f3a8d2b3164ceb7a`;
- IPA `sha256:e6a01b2eafd361b9df2567b002f9e8aa56b57dcee219c7999c65767b91138d16`;
- package Release / source marker `44138db766d0` / minimum iOS14 / UIDeviceFamily `[1,2]` / arm64.

Evidence ladder: **Code written / detached diff audited / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Runtime pending; Stable/Frozen No.**

## Durable Phase 9 architecture/security boundary

- Exact b42 proves successful ChatGPT-account protected Send requires browser anti-abuse challenge output. Pure-native/transient-auth account Send remains blocked.
- The separately billed API-product route remains rejected; primary-account Sub2API/Codex-subscription Runtime remains blocked by the account-safety gate.
- TD-024/TD-025/TD-028 remain unchanged. Full existing-conversation mobile-Web rendering is not an accepted daily-chat dependency after the b47 long-answer composer failure.
- b48-b65 are **diagnostic exceptions only**. Their success does not approve hidden/shadow Web as production architecture and does not transfer production response ownership away from `ConversationRepository`.
- `ConversationRepository` remains sole native production conversation/list/detail/recovery/future accepted response authority; `AuthSessionStore` remains auth/account authority; default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Sync/Reload never resend/regenerate; no second Send may be created merely to obtain a stream.

## Current Send/stream evidence progression

- b45 Runtime Confirmed official no-resend `POST /backend-api/f/conversation/resume` with `{conversation_id, offset}` -> HTTP200 SSE; b46/b47 duplicated Native Cookie+Bearer-only resume returned HTTP404 JSON. Native first/exclusive resume remains Unknown / Unverified.
- b48-b51 established Native composer -> official protected Send and compact incremental text grammar, including fresh-new-chat continuation across `title_generation`.
- b52-b56 isolated reasoning/tool grammar and exact `reasoning_ended`, while keeping raw `assistant:thoughts` non-presentational.
- b57-b59 established Native reasoning/final split and exact service-marked thinking-preamble inclusion.
- b60 preserved later reasoning paragraph boundaries, presented event-driven `正在思考`, and proved exact invocation→result `parent_id` association for tested traffic.
- b61 passed the successful parent-paired tool-row lifecycle but also exposed generic-`textarea` false readiness; b62 removed only that exact authority and passed the focused verified-composer path.
- b63 captured the minimum safe structural evidence; same-run Runtime + official-Web evidence authorized the GitHub connector payload / exact-parent result-content mapping.
- b64 implemented that mapping and exact iPhone/iOS17 Runtime confirmed real protected Send, complete-looking reasoning/final, 30/30 Native tool completion updates, 26 detail-capable rows and multiple successful detail expand/collapse interactions. Runtime rejected only formatting/density: nested result strings remained JSON-escaped and both detail sections dumped at once.
- b65 is the presentation-only correction: second-level independent `工具输入` / `工具输出` disclosures and decoded hierarchical result formatting. It does not change Send, stream parsing, reasoning state, exact-parent association, GitHub-only authorization, diagnostics privacy or production ownership.

## Exact b64 Runtime retained

User export `ChatGPTClient-Diagnostics-20260830-174329.json` matched exact Release b64 / source `6ce1fbd242c9` / iPhone / iOS17.0.

Observed path reached `prompt_textarea -> submitted -> sendObserved -> HTTP200 text/event-stream -> terminal`; terminal metrics included reasoning `27/440`, final `215/6716`, exact reasoning-end `1`, parent matches `30`, unmatched `5`, missing `0`, Native tool presentations/completion updates `30/30`, and detail-capable rows `26`. The user reported no apparent truncation. Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b64-runtime.md`.

## Exact b65 Runtime gate

Install exact b65 on the primary iPhone/iOS17 device and run one GitHub/repository request that naturally creates multiple tool rows. Verify the accepted Send/reasoning/final/tool lifecycle still passes, then confirm one completed GitHub row initially exposes only collapsed second-level `工具输入` / `工具输出`, each expands independently, and decoded output no longer shows b64's second-layer escape wall. Export diagnostics after terminal.

Do not allocate b66 by guess. If b65 passes this focused presentation gate, close the formatting defect without another Candidate. Any product-code correction after this emitted b65 Artifact must use b66+.

## Remaining Unknown / Unverified

Accepted production incremental-response ownership, cross-tool expandable-detail schema beyond the currently evidenced GitHub mapping, Native first/exclusive resume, existing-conversation pre-React history virtualization, full 5/15-minute background behavior, WebContent termination, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified where not explicitly tested. CI/Artifact success is never Runtime proof.
