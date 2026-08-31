# DEV-send-stream b70 Runtime evidence — 2026-08-31

## Exact identity

- Candidate: `DEV-send-stream-0.1.0-b70`
- Version / Build: `0.1.0 (70)`
- Product source: `fb83be9163838f78abfa47903e67f27b6f66ec52`
- Artifact: `9752289536`
- IPA SHA: `8084e2ace5926b7ee6a790f3eeb2445a2c4ce1fee67d8953300aca93a446a44a`
- Runtime device: primary iPhone / iOS17.0
- Supplied diagnostics: `ChatGPTClient-Diagnostics-20260831-094954.json`

## Accepted evidence retained

The supplied run retained one local Send -> one submitted -> one real protected Send -> HTTP200 `text/event-stream` -> Repository response events -> terminal -> authoritative reconciliation. Navigation away while generation remained active did not create another response owner. This keeps the accepted b67 transport result intact. The supplied run did not independently prove every b70 transient-auth/403 recovery gate.

## Presentation/performance rejection

The user supplied two b70 screenshots and two official ChatGPT iOS reference screenshots and explicitly required the official interaction/presentation as the target with pixel-level attention to spacing, row height, icon size and thinking-time placement.

Observed defects:

1. GitHub tool presentation used literal `GH`; an additional generic `</> 工具调用 · 已完成` row made the timeline noisy compared with the supplied official reference.
2. Reasoning and tool disclosure interactions were visibly slow. Exact diagnostics recorded `reasoningSummary.toggled` around 1.38–1.73s and `toolDetail.toggled` around 1.39–1.45s in the tested long conversation.
3. Source correlation identified the owner: each historical toggle called full `rebuildPresentationGeometry(...)` and recomputed all presentation metrics/offsets before table reload; the following table layout itself was only milliseconds to tens of milliseconds.
4. Expanded tool detail was capped at 260pt and used nested `UITextView` scrolling; the supplied official sheet instead grows detail and lets one outer surface scroll.
5. Assistant clear-bubble content applied an additional 12pt horizontal inset on top of the 16pt table margin, yielding roughly 28pt alignment rather than the supplied official ~16–18pt alignment.
6. b70 used inline `思考过程` expansion in the conversation. The official reference uses a compact `思考了 7s` summary + chevron/tool row and a rounded bottom sheet titled `正在思考`, with tool detail, progress/completion, `思考了 7s`, then `完成`.
7. The supplied official GitHub mark is approximately 16pt square; literal `GH` is not acceptable parity.

## Conclusion

b70 is **Runtime Partial/Rejected for daily-chat reasoning/tool presentation parity**. Its package identity remains valid and permanently reserved. The evidence authorizes b71 only as a presentation/performance correction; it does not authorize protected-Send route/selector/challenge/SSE changes, another response owner, retry/poll/timer/watchdog machinery, or unrelated Composer/Stop/background/attachment work.
