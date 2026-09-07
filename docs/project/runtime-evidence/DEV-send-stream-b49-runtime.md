# DEV-send-stream b49 — Exact-device Runtime

## Exact identity

- Candidate: `DEV-send-stream-0.1.0-b49`
- Version/build: `0.1.0 (49)`
- Exact product/config source: `20fb8f3f400200965acb868aeb8a7504b9bfb91f`
- Push CI: Run `33268560803`, Job `99142837459` — success
- PR CI: Run `33268562114`, Job `99142840873` — success
- Runtime Artifact: `9719418761`
- Artifact ZIP digest: `sha256:1b59bd8c13da116b3221acd29a4ad52de9c3f841c09f262d625e60fa6fb3aaec`
- IPA SHA-256: `88bd8e46b054169cb1f4338d91bb06c216edbf204b9a440a5cdc678ea6e4cd95`
- Runtime: iPhone / iOS17.0 / Release
- Diagnostics source marker: `20fb8f3f4002`
- Exported at: `2026-08-29T18:50:54Z`

## User-visible result

The user sent two turns only through the Native composer. Both turns produced visible Native assistant text and the user observed that the text did not appear all at once, but both long replies were severely truncated: only short portions near the beginning/end were visible. Therefore the user correctly did not accept full streaming completeness.

## Exact protocol result

### Turn 1

- Native submit attempt 1 -> `submitted`.
- Official protected Send observed.
- Response: HTTP200 `text/event-stream`, `filtered=true`.
- Terminal metrics after 406 frames:
  - `removedTextPatchCount=2`
  - `removedTextCharacters=18`
  - `nativeDeltaCount=2`
  - `nativeCharacters=18`
  - `webAssistantTextCharacters=45`
  - `webMessageNodes=2`
  - `webElementCount=621`
  - `terminal=true`
- Web composer returned ready.

The first response remained active from roughly `18:44:24Z` to `18:45:58Z` (~94 s). During that same active response the app entered background three times for approximately 31 s, 10 s and 11 s (~52 s total overlap) and still reached terminal without a second Send. This is positive exact-b49 short-background survival evidence for the current Web-owned diagnostic stream only; it is not yet production background acceptance.

### Turn 2

- Native submit attempt 2 -> `submitted`.
- Official protected Send observed.
- Response: HTTP200 `text/event-stream`, `filtered=true`.
- Terminal metrics after 34 frames:
  - `removedTextPatchCount=2`
  - `removedTextCharacters=14`
  - `nativeDeltaCount=2`
  - `nativeCharacters=14`
  - `webAssistantTextCharacters=90`
  - `webMessageNodes=4`
  - `webElementCount=676`
  - `terminal=true`
- Web composer returned ready again.

## Accepted positive facts

1. b49 fixes b48's zero-hit defect: assistant text patches are now actually intercepted before Web React and forwarded to Native.
2. `nativeDeltaCount=2` on each turn plus the user's observation that visible text did not arrive all at once is direct evidence that the Native bridge can receive incremental assistant text during an active official-Web Send.
3. Two sequential Native-composer turns still succeed in one Web conversation/session and both official Sends return HTTP200 SSE.
4. The first long response survives several ordinary background/foreground intervals and still reaches terminal without resend.

## Rejected / incomplete facts

b49 **does not pass the complete-response interception gate**. A 406-frame long first response yielded only 18 Native characters and two intercepted patches; the user-visible answer was truncated. The second turn likewise yielded only 14 Native characters and two intercepted patches. Therefore b49 cannot be called a complete Native streaming implementation and existing-conversation history virtualization must not start from this parser yet.

`webAssistantTextCharacters` being only 45/90 is not sufficient evidence of successful full Web-render suppression because most assistant text was not captured by Native either. The missing text must be explained first.

## Source-backed missing grammar

Historical current-account b40 Runtime diagnostics already recorded a relevant v1 compact sequence:

1. explicit `o:"append"`, `p:"/message/content/parts/0"`, string `v`;
2. immediately following frame with event keys only `v` and string payload, classified by that probe as `value_string_patch`;
3. later structured/batch patch frame.

This is exact prior project Runtime evidence, not a speculative third-party grammar. b49 only recognizes the explicit `o/p/v` frame and therefore cannot consume the following compact value-only continuation frame(s).

The smallest next experiment may keep a text-continuation context only after an explicitly evidenced assistant text append and consume a bare object whose only key is string `v` while that context remains active. Any explicit new operation/path or non-value-only structural frame must terminate that context. Do not treat arbitrary bare `v` strings globally as assistant text.

## Classification

- Native composer -> official protected Send: Runtime Confirmed for this diagnostic scope.
- Native incremental assistant delivery: **Runtime Confirmed but partial/incomplete**.
- Full assistant response interception: **Runtime Rejected on b49**.
- Two-turn continuity: Runtime Confirmed for this diagnostic scope.
- Exact-b49 short-background stream survival: positive evidence only, not full product background acceptance.
- Production hidden/shadow-Web architecture: still not accepted; TD-024/TD-025 remain unchanged.
- Stable/Frozen Send: No.
