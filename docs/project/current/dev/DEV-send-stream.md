# DEV-send-stream

## Status

**Active — exact b48 product/config source published; CI/Artifact gate in progress. Long-term TD-024/TD-025 hidden/shadow-Web boundary remains unchanged. b48 is one isolated diagnostic exception explicitly requested by the user to measure real-device feasibility before any durable architecture decision.**

- **Work ID**: `DEV-send-stream`
- **Branch**: `dev/send-stream-20260829`
- **PR**: #29 — open / mergeable / not merged; evidence branch only.
- **Target main**: `1ac202c972f2dee6945fe8d0688df8e10f5d462c`.
- **Stable native predecessor**: b38.
- **Exact b47 product source**: `21028bbff7982abeb42f130c56fcb21e6ef44d7a`; immutable/reserved.
- **b47 Runtime Artifact**: `9716878034`.
- **Candidate**: `DEV-send-stream-0.1.0-b48`.
- **Version / Build**: `0.1.0 (48)`.
- **Exact b48 product/config source**: `6ccba03cefaa32a1186f1f468c3e696ed9457699`.
- **Stable/Frozen Send**: No.

## Resume / identity guard

Current-session Light Resume Guard passed before b48:

- latest `AGENTS.md` + `docs/project/START_HERE.md` reread;
- unique Active Work remains `DEV-send-stream`;
- branch/PR identity matched;
- `main` remained `1ac202c...`;
- no peer Active checkpoint conflict;
- repository search found no prior b48 allocation;
- b47 product source had only later docs/evidence changes.

## Why b48 exists

Prior exact-device evidence established two independent ceilings:

1. b42: ordinary `/backend-api/f/conversation` protected Send depends on browser-owned anti-abuse challenge output; pure Native Send remains blocked without bypass/replay.
2. b47 preparation + the user's older wrapped-Web experiment: full existing-conversation mobile Web can become unusably heavy, and loading the full page then hiding most historical DOM does not adequately fix `+`/composer UX.

The user therefore requested one experiment that keeps the official Web runtime only as a Send engine while the visible input/output interaction is Native.

This does **not** change durable production policy yet. Do not edit TD-024/TD-025 merely because b48 exists.

## b48 implementation scope

Exact source `6ccba03...` changes exactly four product/config paths relative to the allocation checkpoint:

- `.github/workflows/ios-foundation.yml`
- `ChatGPTClient.xcodeproj/project.pbxproj`
- `ChatGPTClient/Protocol/NativeWebSendEngineProbe.swift`
- `ChatGPTClient/SettingsViewController.swift`

Assembly audit confirmed no change to `ConversationFeature.swift`, `AuthSessionStore.swift`, `RootViewController.swift`, scripts, or stable b38 presentation code.

The b48 diagnostic controller:

- keeps a full-size official `WKWebView` on the default persistent `WKWebsiteDataStore` behind an opaque Native surface;
- exposes a Native `UITextView` composer + Native Send button;
- at document start, discovers the Web composer and transfers the Native text into its real editable state, then invokes the page's own form/Send control;
- leaves all login/Sentinel/Turnstile/PoW/protected-Send construction to the official Web page;
- wraps only `/backend-api/f/conversation` fetch responses;
- consumes the real SSE once, with no `response.clone()` branch;
- forwards evidenced append `/message/content/parts/0` text deltas to Native memory/UI and removes those text patch operations from the SSE returned to Web React;
- preserves the remaining structural lifecycle frames and `[DONE]` for the Web state machine;
- suppresses Web user/assistant message rendering with CSS while leaving the full-size Web layout/runtime present;
- records only structural counts/status/DOM metrics in diagnostics, never prompt/answer/reasoning text;
- does not integrate into `ConversationRepository` or production response ownership;
- has no retry/timer/watchdog/fallback machinery;
- is new-chat focused and does not yet virtualize existing conversation-detail history.

## Durable safety boundaries retained

b48 must not be generalized from this diagnostic without later explicit Runtime-backed decision. Still prohibited outside this exception:

- challenge/proof/Conduit/OAI value harvesting or replay;
- Native construction of protected `/f/conversation` Send;
- hidden file-input automation;
- production DOM answer/reasoning scraping;
- Sub2API/Codex OAuth Runtime on the user's primary account;
- speculative resume/header copying;
- claiming existing long-conversation performance is fixed before testing it.

## Runtime gate

Exact-device b48 must answer:

1. Native composer can submit without touching the Web composer.
2. Official Web protected Send still succeeds.
3. Native receives incremental assistant text while Web React does not receive the corresponding text patch.
4. Web assistant text/DOM footprint remains small during a long response.
5. After terminal `[DONE]`, a second Native-composer turn succeeds in the same Web session.
6. Native typing/Send interaction feels smooth.

Passing this gate only unlocks a later existing-conversation data-virtualization experiment; it does not itself approve hidden/shadow Web as production architecture.

## Non-atomic write-chain state

- **Batch A — checkpoint / Candidate allocation:** complete.
- **Batch B — non-CI assembly:** complete on `assembly/dev-send-stream-b48-20260830`.
- **Batch C — audit / publish:** complete. Assembly diff was exactly the four expected files; real branch Light Guard matched; non-force fast-forward to exact source `6ccba03cefaa32a1186f1f468c3e696ed9457699` succeeded.
- **Batch D — CI / Artifact:** pending/in progress. Accept only runs whose exact head is `6ccba03...` or a later docs-only head that packages the same exact product/config source; package identity must still embed source `6ccba03...` if build script uses checkout source marker. If a docs-only checkpoint commit causes a PR run, it does not redefine product source.
- **Batch E — durable docs / PR:** pending until CI/Artifact identity is known. Do not alter TD-024/TD-025 before Runtime.

## Next exact action

Inspect the b48 push and PR CI generated from the complete published Candidate, fix only deterministic compile/package defects if any, then obtain and independently inspect the legitimate Push Artifact. Roll this checkpoint with exact Run/Job/Artifact/IPA identities and hand the IPA to the user for the six-point real-device Runtime gate. Do not wait for an extra `继续` reply.