# Sub2API Codex OAuth Research

_Date: 2026-08-30_

## Scope / evidence class

This is **external source-code research**, not ChatGPT Client Runtime proof and not an accepted product decision.

Source repository inspected:

- `Wei-Shaw/sub2api`
- upstream `main` observed at `b5827cfd54d58c248a9480b800444d0b40f0c6ea`

The purpose of this research is to determine whether Sub2API exposes an account-subscription-backed transport that could avoid rendering the full mobile ChatGPT conversation before every Send.

## What Sub2API actually does for OpenAI OAuth

### Official Codex CLI OAuth client flow

`backend/internal/pkg/openai/oauth.go` uses:

- OpenAI authorization endpoint `https://auth.openai.com/oauth/authorize`;
- token endpoint `https://auth.openai.com/oauth/token`;
- PKCE;
- official Codex CLI OAuth client ID `app_EMoamEEZ73f0CkXaXp7hrann`;
- `openid profile email offline_access` scopes;
- `codex_cli_simplified_flow=true`.

The parsed token claims include ChatGPT account/user/plan identifiers such as `chatgpt_account_id`, `chatgpt_user_id`, `chatgpt_plan_type` and organization/POID information.

`backend/internal/service/openai_oauth_service.go` stores/accesses access + refresh tokens and enriches the account with ChatGPT plan/account information.

### Subscription-backed Codex Responses endpoint

For OpenAI OAuth-like accounts, Sub2API does **not** forward ordinary Responses traffic to `api.openai.com`.

Its OpenAI gateway defines:

`https://chatgpt.com/backend-api/codex/responses`

as the ChatGPT internal Codex Responses upstream. Tests in `backend/internal/service/openai_oauth_passthrough_test.go` and `backend/internal/service/openai_gpt56_max_test.go` explicitly assert that an OAuth account with `access_token + chatgpt_account_id` forwards `/v1/responses` to this endpoint.

`backend/internal/handler/endpoint.go` treats `/v1/responses`, `/responses` and `/backend-api/codex/responses` as the same Responses-family surface for gateway normalization.

### ChatGPT subscription/Codex quota

`backend/internal/service/openai_quota_service.go` reads ChatGPT/Codex subscription quota from:

- `https://chatgpt.com/backend-api/wham/usage`
- rate-limit reset-credit endpoints under `/backend-api/wham/`.

This is strong source evidence that the OAuth route is consuming ChatGPT/Codex subscription entitlement rather than the separately billed `api.openai.com` API-key route.

### Models / streaming

Current source recognizes GPT-5.6-family Codex models including `gpt-5.6-sol`, `gpt-5.6-terra` and `gpt-5.6-luna`; plain `gpt-5.6` normalizes to `gpt-5.6-sol`.

Tests show OpenAI OAuth requests to the Codex Responses upstream with streaming and reasoning settings, including GPT-5.6 `reasoning.effort=max` for non-compact Responses requests.

This is structurally much closer to a native Responses/SSE client than the ordinary ChatGPT Web `/backend-api/f/conversation` protected-Send path currently investigated by `DEV-send-stream`.

## Important difference from the current ChatGPT Client protocol

Current `DEV-send-stream` ordinary consumer-chat evidence is based on:

- `/backend-api/f/conversation` protected Send;
- browser Sentinel / PoW / Turnstile requirements;
- `/backend-api/f/conversation/resume` post-Send continuation;
- ordinary `/backend-api/conversations` and `/backend-api/conversation/{id}` native read history.

Sub2API's OpenAI OAuth path is instead centered on:

- Codex CLI OAuth;
- `/backend-api/codex/responses`;
- Responses-style request bodies;
- Codex session/conversation/prompt-cache headers and metadata.

Repository search did not produce evidence that Sub2API writes into or continues the ordinary ChatGPT consumer `/c/<id>` conversation-history graph. No ordinary `/backend-api/conversations` integration was found in the inspected source.

Therefore **normal ChatGPT conversation-history continuity is Unknown / Unverified and must not be assumed**.

## Client-identity / risk boundary

Sub2API is not merely sending `Authorization + chatgpt-account-id`.

Its source contains substantial Codex client-identity handling:

- canonical Codex User-Agent/originator/version handling;
- a minimum Codex version gate based on observed upstream 404 behavior;
- enforced outbound Codex identity headers;
- optional installation/session/thread/turn/window fingerprint convergence;
- session/conversation ID isolation;
- Codex-specific beta/routing/metadata handling.

`openai_codex_identity.go` explicitly says upstream behavior can depend on client identity/version and that the gateway defaults to enforcing a canonical Codex identity. `openai_codex_fingerprint.go` contains optional identity-convergence logic for shared OAuth accounts.

Sub2API's README also warns users about upstream Terms-of-Service/account-risk concerns generally.

Therefore this source is highly valuable architectural/protocol evidence, but **it is not evidence that arbitrary third-party native use of the Codex internal endpoint is an officially supported ChatGPT consumer-client contract**.

## Relevance to DEV-send-stream

This research materially changes the architecture search space.

Potential architecture, **not yet accepted**:

`Native UI -> OpenAI Codex OAuth login -> subscription-backed /backend-api/codex/responses -> Native Responses stream`

Potential benefits if independently validated:

- no full mobile ChatGPT conversation page before Send;
- no dependency on the long-conversation Web composer that failed in b47 preparation;
- native input and native streaming become structurally possible;
- uses ChatGPT/Codex subscription entitlement rather than separately billed API-key billing.

Unresolved P0 questions:

1. Can the user's existing ChatGPT subscription/account obtain/use this Codex OAuth entitlement on the target device/account?
2. Can a minimal client use the OAuth/Codex transport without relying on prohibited browser/challenge bypass or unjustified client-identity spoofing?
3. What exact request identity/header/body subset is genuinely required for a single-user native client?
4. Do Codex Responses threads appear in, or map to, ordinary ChatGPT consumer conversation history? Current source evidence does not establish this.
5. If history is separate, can the product accept a split where existing ChatGPT history remains read-only while new native conversations use Codex Responses? This is a product decision, not a technical assumption.
6. What reasoning/attachments/tools/background semantics are available on the exact account and target iOS environment?

## Decision boundary

Do not copy Sub2API's fingerprint/identity-mimicry machinery into ChatGPT Client.

Do not allocate product Candidate b48 solely from this external source research.

The next evidence step, if the user wants to pursue this route, should be a **minimal diagnostic feasibility experiment** that validates the user's own account's Codex OAuth entitlement and a single safe Responses request without integrating production conversation state. Candidate identity must be newly allocated only after the current Human Architecture Gate is deliberately resolved in favor of this experiment.
