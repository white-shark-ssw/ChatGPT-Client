# DEV-send-stream visible Web focus / cross-platform continuation A/B — 2026-09-02

## Evidence class

User-observed real-device Web Rule Lab Runtime evidence using the same `WKWebsiteDataStore.default()` browser login/session authority as production covered Web execution. This is a visible official-Web diagnostic sample, not b88 product Runtime.

## Known-good sample

The user started a new response on another official client, opened Web Rule Lab, visibly entered that active cross-platform conversation, and immediately observed the official Web UI continuing the in-progress response live. The composer control was already the active-response **Stop** control rather than Send, showing that the official page had acquired the active response lifecycle state.

The privacy-safe page probe returned `visibilityState=visible`, `hidden=false`, `readyState=complete`, `document.hasFocus=true`. The coarse probe returned `route=other`, but screenshot/user observation proves the page was visibly inside the target conversation, so the current `^/c/` classifier is diagnostic-only and is not conversation-state authority.

Exact b87 supplies the negative counterpart: covered production was visible/loaded/attached but stayed `document.hasFocus=false` and produced zero page-owned continuation for about 161 seconds foreground.

Focus remained correlation rather than causality because the known-good visible sample also included a genuine user-driven SPA/router conversation-entry transition. This evidence authorized b88 as a one-variable first-responder A/B only; it did not authorize Native request synthesis, offset guessing, polling, timers, retries/watchdogs, duplicate Send, WebSocket-body authority or a second response store.
