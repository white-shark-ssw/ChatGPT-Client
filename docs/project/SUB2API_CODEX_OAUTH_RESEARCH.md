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

Sub2API's README explicitly warns about Terms-of-Service and account-ban/service-interruption risk. Recent repository issues also contain community reports of OpenAI accounts being banned while used with this ecosystem, including reports around multi-account/high-concurrency use. Those reports are anecdotal and do **not** prove Sub2API itself caused the bans, but they are sufficient to treat account safety as a real unresolved risk rather than a theoretical one.

Current OpenAI public documentation confirms that Codex itself is included in ChatGPT plans and can be accessed by signing in with a ChatGPT account. That establishes normal first-party Codex use, but it does **not** establish that repackaging ChatGPT/Codex subscription entitlement as an arbitrary third-party Responses client or gateway is an officially supported consumer contract. OpenAI's current Terms of Use also prohibit bypassing rate limits/restrictions/protective measures and certain reverse-engineering/programmatic extraction behavior.

Therefore this source is highly valuable architectural/protocol evidence, but **it is not evidence that arbitrary third-party native use of the Codex internal endpoint is an officially supported ChatGPT consumer-client contract**.

### Primary-account safety gate

The user has explicitly raised concern about account suspension/ban risk. Treat this as an active product constraint:

- **Do not use the user's primary ChatGPT account for Sub2API-style Codex OAuth / subscription-to-Responses feasibility requests.**
- Do not allocate a Candidate that performs such requests on the primary account unless the user later explicitly accepts that account-risk experiment.
- Static source research and protocol comparison may continue.
- First-party Codex use through official OpenAI clients is not the same risk class as reproducing/internalizing Sub2API's gateway behavior.
- Do not copy Sub2API fingerprint-convergence or client-identity mimicry into ChatGPT Client as a workaround.

## Relevance to DEV-send-stream

This research materially changes the architecture search space, but account-risk currently blocks primary-account Runtime validation.

Potential architecture, **not yet accepted**:

`Native UI -> OpenAI Codex OAuth login -> subscription-backed /backend-api/codex/responses -> Native Responses stream`

Potential benefits if independently validated:

- no full mobile ChatGPT conversation page before Send;
- no dependency on the long-conversation Web composer that failed in b47 preparation;
- native input and native streaming become structurally possible;
- uses ChatGPT/Codex subscription entitlement rather than separately billed API-key billing.

Unresolved P0 questions:

1. Can a minimal single-user client use this transport without account-risk behaviors such as unsupported client-identity mimicry?
2. What exact request identity/header/body subset is genuinely required by the supported first-party Codex contract versus Sub2API-specific gateway compatibility?
3. Do Codex Responses threads appear in, or map to, ordinary ChatGPT consumer conversation history? Current source evidence does not establish this.
4. If history is separate, can the product accept a split where existing ChatGPT history remains read-only while new native conversations use Codex Responses? This is a product decision, not a technical assumption.
5. What reasoning/attachments/tools/background semantics are available through documented/first-party Codex surfaces?
6. Is there any officially supported path for third-party native integration that preserves ChatGPT subscription billing and avoids private/internal endpoint reliance? Currently Unknown / Unverified.

## Decision boundary

Do not copy Sub2API's fingerprint/identity-mimicry machinery into ChatGPT Client.

Do not allocate product Candidate b48 solely from this external source research.

Because primary-account safety is now a hard constraint, the next evidence step is **static research only** unless the user later explicitly authorizes a risk-bearing experiment on a non-critical account or otherwise changes this gate. Research should focus on documented/first-party Codex auth/transport behavior, consumer-history relationship, and whether any officially supported third-party integration exists.