# DEV-send-stream

## Status

**Blocked — API product rejected; existing-account visible-Web Send must pass background-resilience feasibility before any next UI Candidate**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail / 官方 Web / hybrid / 后台 / 真后台`
- **Branch / PR**: `dev/send-stream-20260829`; PR #29 open/mergeable; do not merge as accepted Send UX.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; Stable native predecessor remains b38.
- **Exact b44 product/config source**: `f1503cf7121512a84e5c55a3642181c17324d791`.
- **Exact b44 Artifact**: `9712583513`; IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.
- **Current docs batch baseline**: branch was `10843c106659186e84d08a181c1e0901f2a54857` before the latest background-requirement updates.
- **Parallel guard**: only this Active development checkpoint exists under `docs/project/current/dev/`; no peer Active dev conflict found.
- **Candidate rule**: b39-b44 are permanently reserved. **No b45 or later Send/background Candidate has been allocated.**

## Security / transport boundary

Exact b42 proved successful tested ChatGPT-account Send requires browser anti-abuse challenge output (`proofOfWorkRequired=true`, `turnstileRequired=true`, `soRequired=true`, non-empty PoW + Turnstile finalize input). Pure-native/transient-auth account-session Send remains blocked.

Never implement PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay, captured proof/token replay, guessed fallback endpoints, hidden challenge-harvesting WebViews, DOM message/reasoning scraping, covered-Web Native composer injection, synthetic hidden Send clicks or challenge extraction/replay.

TD-024 permits only an **explicit user-visible** official ChatGPT Web Send surface. TD-025 records that b44's full-page Native -> Web -> Native form is product-rejected. TD-026 adds the background-resilience gate below.

## b43 / b44 accepted evidence

### b43 visible-Web feasibility

Exact b43 `DEV-send-stream-0.1.0-b43`, source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`, Artifact `9711364573`, IPA SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.

Primary iPhone/iOS17 Runtime:

- first/re-entry, keyboard/typing, visible Web Send, stream scrolling and rapid scrolling had no material problem reported;
- Web `+` -> attachment selection roughly **100–200 ms**, not rejected;
- Web Photos selection filtered video assets;
- standalone Settings Web-chat interaction was not accepted as final product UX.

Public `WKUIDelegate` file-open-panel replacement is iOS18.4+, not primary iOS17. Do not use private WebKit or DOM/file-input injection to fake an iOS17 photo+video picker fix.

### b44 full-page integrated trial

Exact b44 `DEV-send-stream-0.1.0-b44`, source `f1503cf7121512a84e5c55a3642181c17324d791`, Push Run/Job `33245105815` / `99081114295` success, PR Run `33245107290` success, Artifact `9712583513`, IPA SHA `70471f76c90974eae34bb99335ad4f4c5132ba9f5d143444c306f11e81542970`.

Runtime established:

1. Web Send worked.
2. Immediate `返回并同步` could expose the just-sent user message but not assistant output already visible in Web.
3. Repeated immediate Native Sync still could miss that assistant output.
4. A later Sync after waiting could expose it.
5. Tested Native A/B IDs mapped to corresponding Web `/c/<id>` conversations.
6. A/B switching caused Web to load/render the selected conversation again.

Conclusion: Native Detail is eventually consistent relative to Web generation in the tested sequence; no stable readiness delay/signal was established. Do not add timer/poll/retry/repeated automatic Sync. The full-page Native -> Web -> Native product form is rejected / superseded.

## Latest explicit product decision

The user explicitly stated that the **separately authenticated/billed supported API product path will not be accepted**. Do not keep it as an active product option unless the user later reverses that decision.

The only active non-deferred Send direction is now:

**Native list/history/read/navigation + explicitly visible official-Web composer/live-response for the existing ChatGPT account/history.**

This direction is conditional on the background gate below.

## TD-026 — background reasoning/stream resilience gate

The user identifies this behavior as unacceptable: during long reasoning / streamed reasoning-output / final-answer generation, backgrounding or locking the client for a while can lead to timeout/disconnect and require manual refresh on return.

Required product outcome:

- preferred: the same visible official-Web reasoning/stream survives the user's normal background/lock habit and resumes without forced reload;
- acceptable: a **known** background/WebKit lifecycle interruption triggers one deterministic same-conversation foreground recovery without prompt resend and without routine manual refresh;
- rejected: timer/poll/retry loops, manual refresh as normal use, hidden DOM recovery, fake keepalive timers, or permanently keeping the app alive while idle.

Public iOS background time is finite. `beginBackgroundTask` is only a short-duration baseline and cannot honestly guarantee a long reasoning/stream session.

Because this is a TrollStore product, the next feasibility question is whether narrowly scoped process preservation also preserves the relevant **WebKit WebContent/network execution and actual official ChatGPT response stream**. Main-app PID survival alone is not proof.

Durable owner: `docs/project/HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md`.

Key Unknown / Unverified facts until exact-device Runtime:

- WebContent survival;
- WebKit network-process survival;
- official ChatGPT stream continuity across background/lock;
- silent-stall behavior;
- Wi-Fi/cellular transition;
- battery/thermal cost;
- deterministic no-manual-refresh recovery after a known WebKit interruption.

Since Native has no supported Web terminal signal without prohibited DOM/stream observation, an initial experiment may conservatively preserve the process for the whole background interval when the visible Web Send surface was active at background entry, then release on foreground return. Do not create a fake `isWebStreaming` owner from UI text, timers or DOM scraping.

## Go / No-go before UI polish

Exact primary iPhone/iOS17 TrollStore matrix must include:

- long visible-Web reasoning/stream -> short background -> return;
- same with device lock;
- ~5-minute and ~15-minute intervals when workload permits;
- longer intervals only when a controlled active response can meaningfully support them;
- public background-task expiration;
- observed WebContent/process interruption + one-shot foreground recovery;
- no prompt resend / no duplicate message;
- stable Wi-Fi first, then network transition after baseline works;
- battery/thermal observation.

**Go**: normal user background use keeps the live response alive, or a known interruption recovers automatically on foreground without resend/manual refresh.

**No-go**: routine background still requires manual refresh, WebKit execution cannot be preserved reliably, recovery requires prohibited hidden DOM automation, or battery/thermal impact is unacceptable. With API rejected, No-go means defer ChatGPT-account Send.

## Requirement/docs batch — completed

Completed after exact b44 product source, with no intentional product/config/workflow mutation:

- created `HYBRID_WEB_BACKGROUND_RESILIENCE_PLAN.md`;
- updated `START_HERE.md` to route future hybrid background work;
- updated `PROJECT_STATE.md`;
- updated `MODULE_STATUS.md`;
- updated `PROJECT_PROFILE.md`;
- updated `DEVELOPMENT_PLAN.md`;
- updated `TECHNICAL_DECISIONS.md` with TD-026;
- updated `PROJECT_SPECIFIC_RULES.md`;
- updated PR #29 title/body to the background-resilience gate;
- no b45 allocated, no CI/Artifact produced.

## Next exact action

**Human gate:** decide whether to run the existing-account TrollStore/WebKit background-resilience feasibility experiment.

If authorized:

1. reread governance and both background plans;
2. create the appropriately isolated/stacked background experiment Work because it depends on this unmerged Send branch;
3. verify exact branch/PR/base/state-owner/Frozen/shared-infrastructure conflicts;
4. inspect real AppDelegate/WebKit lifecycle/entitlement/signing/package source before changing code;
5. allocate the next unique Candidate only after identity preflight;
6. implement the smallest measurement/preservation/recovery experiment first — **not** embedded-Web UI polish;
7. hand the exact Artifact to the user for the TD-026 matrix.

If not authorized, leave ChatGPT-account Send deferred. Do not reactivate the API product route unless the user explicitly reverses that decision.
