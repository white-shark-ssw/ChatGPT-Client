# DEV-send-stream b81 allocation — 2026-09-01

- User scope: defer account-wide notification discovery; keep client-owned Send/stream correct and prioritize reliable externally initiated cross-platform streaming.
- Candidate: `DEV-send-stream-0.1.0-b81` / `0.1.0 (81)` — permanently reserved.
- Allocation guard: formal branch head before allocation docs `2198fa2059e4104259ce49647ec057177bb9e932`; PR #29 open/mergeable/unmerged; actual main `94f0c5777dad262cd1fb22be49082dbd92c962f2`; exact b81 search unused; only one Active development checkpoint.
- Main drift from the PR's older recorded base is confined to `docs/project/COMPOSER_PARITY_PLAN.md`; no Send product/state-owner overlap found.
- b81 is a focused **at-document-start WebSocket structural probe**, not a response transport change. Historical Web evidence already proves a user-level `wss://ws.chatgpt.com/...` exists during cross-device continuation, but frame bodies remain non-authoritative.
- Product scope: `RootViewController.swift` privacy-safe socket structure diagnostics + Xcode Build/Candidate identity + workflow Artifact identity. No polling/timer/retry/watchdog, Native `stream_status`, duplicate Sync/Send, DOM/WebSocket body authority, fake progressive final, or account-wide notification implementation.
- Runtime purpose: while the same conversation is already open in the client, start a remote turn elsewhere without pressing Sync and determine whether a stable socket event/shape precedes or explains page-owned `stream_status`/plural adoption.
- b80 Frozen boundaries remain untouched: final tool/timeline->divider spacing; stopped external reasoning remains reasoning/tools rather than final.
