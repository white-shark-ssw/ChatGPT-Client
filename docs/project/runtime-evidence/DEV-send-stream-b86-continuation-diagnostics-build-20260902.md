# DEV-send-stream b86 continuation diagnostics build — 2026-09-02

## Purpose

b86 is diagnostics-only. It does not change Send, Sync, re-arm, response ownership, polling, retry, resume, offset selection or page navigation behavior. It only exposes structural facts that b85 Runtime could not distinguish after a manual Sync/re-arm.

## Identity

- Candidate: `DEV-send-stream-0.1.0-b86`
- Version / Build: `0.1.0 (86)`
- Exact diagnostics product commit: `dc77a94be5b2f7eecd822480f759358ad6a0ad25`
- Clean Push CI/package head: `f90caca0419f13254567485171fac7d970aa8c95`
- Push run/job: `33566939415 / 100052171917` — success
- PR run/job: `33566968066 / 100052259409` — success
- Canonical Push Artifact: `9823485856`
- Artifact ZIP digest: `sha256:cdccdcd034964b99e98e62c2e79a9bece96c190138c774e6f1590896d54fbacb`
- IPA: `ChatGPTClient-0.1.0-b86-dev-send-stream.ipa`
- IPA SHA-256: `25d483ac31473b124e6ad555b79c488e78da91ec1761ee8a40076b6e978bee6f`
- Package metadata independently verified: `0.1.0 (86)` / Candidate b86 / `DiagnosticsSourceCommit=f90caca0419f` / minimum iOS14.0 / arm64

## Exact product diff

Relative to the staging parent, exact b86 product commit changes only:

- `ChatGPTClient/RootViewController.swift`: 29 additions / 1 deletion;
- `ChatGPTClient.xcodeproj/project.pbxproj`: 4 additions / 4 deletions for Debug+Release build/Candidate identity.

Temporary staging workflow/script commits are not part of the product source identity and the script was removed after the product commit.

## New diagnostics

For the currently targeted external conversation only:

- `coveredExecutor.externalStreamStatusRequest`
  - proves the page issued a matching `GET .../stream_status` request;
- `coveredExecutor.externalStreamStatusResponse`
  - logs HTTP status and bounded `streamState` token only;
- `coveredExecutor.externalResumeRequest`
  - logs `hasOffset`, primitive `offsetType`, and safe integer `offsetValue` when available;
- existing `coveredExecutor.externalResumeObserved` and `coveredExecutor.resumeResponse`
  - continue to log the matching resume lifecycle and HTTP status/content type.

No response body, prompt, reasoning text, final text, tool body, Cookie, Authorization, challenge value or raw conversation ID is added.

## Behavior invariants

- no new network request;
- no Native constructed `/resume`;
- no guessed offset;
- no polling/timer/retry/watchdog;
- no duplicate Send/resend;
- no second response owner;
- b85 authoritative Detail projection behavior is unchanged;
- client-owned protected-Send SSE is unchanged.

## Human Runtime gate

Use exact b86 on a sufficiently long external response.

1. Press explicit `同步最新消息` once while the remote response is active.
2. Keep ChatGPTClient foreground after the covered page reports loaded; do not switch away immediately.
3. Export diagnostics after enough time for the page to settle, regardless of whether reasoning continues automatically.

Interpretation:

- **No `externalStreamStatusRequest`**: official page never activated continuation for that target; investigate the exact page state/action that causes official Web to start the continuation path.
- **Request exists, state not `IS_STREAMING`**: compare page-owned status/timing against authoritative Detail that already proves active reasoning.
- **`IS_STREAMING` + `externalResumeRequest`**: inspect offset/request ordering and resume response.
- **resume HTTP200 `text/event-stream`**: validate the existing SSE parser and response-owner continuation on the same generation before any new behavior change.
- **resume 404 + subsequent page-owned plural snapshots**: retain genuine block-level continuation as current page-owned fallback evidence; do not synthesize SSE.

## Validation classification

- Code written: **Yes**
- guarded staging / exact matches / `git diff --check`: **Passed**
- Push CI: **Passed**
- PR CI: **Passed**
- Artifact produced/package identity: **Verified**
- Runtime/manual/real-device: **Pending**
- Stable/Frozen Send: **No**
