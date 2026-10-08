# DEV-send-stream b50 Runtime Evidence

_Date: 2026-08-29_

## Exact identity

- Candidate: `DEV-send-stream-0.1.0-b50`
- Version/build: `0.1.0 (50)`
- Exact product/config source: `837d5feeff05d198785f884ccf9cc4c1f71412ec`
- Push Run / Job: `33270436935` / `99147835200` — success
- PR Run / Job: `33270439156` / `99147841433` — success
- Artifact: `9719942650`
- Artifact ZIP SHA-256: `dde656d41ea767714586a92a46740bb9bfe51531b74673e266a58aeec5dce99b`
- IPA SHA-256: `26431faabe0b2c836fd6c1d7aa84d31cf8811ea09d57a8ad692e127ecb42613c`
- Package identity: Release; source marker `837d5feeff05`; minimum iOS14.0; UIDeviceFamily `[1,2]`; arm64
- Runtime export identity: app `0.1.0`, build `50`, Candidate b50, source `837d5feeff05`, Release, iPhone / iOS17.0

## User-visible result

The user tested three sequential turns from the Native composer in one fresh/new-chat probe session.

Direct feedback:

- overall result was described as very good;
- only the first reply lost a middle section;
- turns 2 and 3 were complete;
- turns 2 and 3 visibly streamed incrementally, described as effectively one character at a time.

This direct Runtime observation outranks prior expectations.

## Turn 1 — fresh/new-chat first response: incomplete

Transport/lifecycle:

- Native submit succeeded.
- Official protected Send observed on `/backend-api/f/conversation`.
- Response: HTTP200 `text/event-stream`, `filtered=true`.
- `frameCount=34`.
- Terminal `[DONE]` path completed and composer returned ready.

Terminal metrics:

- `explicitTextPatchCount=2`
- `contextualValueStringCount=1`
- `contextualValueStringCharacters=16`
- `nativeDeltaCount=3`
- `nativeCharacters=35`
- `removedTextPatchCount=3`
- `removedTextCharacters=35`
- `webAssistantTextCharacters=45`
- `webMessageNodes=2`
- `webElementCount=621`
- `terminal=true`

The user states the actual assistant reply was materially longer and the Native display omitted a middle section. Therefore complete-response interception is **Runtime Rejected for this turn** even though Send/stream/terminal are healthy.

## Turn 2 — complete positive response

Transport/lifecycle:

- second sequential Native submit succeeded in the same Web session;
- official protected Send returned HTTP200 SSE, `filtered=true`;
- terminal completed and composer returned ready.

Terminal metrics:

- `frameCount=21`
- `explicitTextPatchCount=2`
- `contextualValueStringCount=8`
- `contextualValueStringCharacters=152`
- `nativeDeltaCount=10`
- `nativeCharacters=191`
- `removedTextPatchCount=10`
- `removedTextCharacters=191`
- `webAssistantTextCharacters=45`
- `webMessageNodes=4`
- `webElementCount=664`
- `terminal=true`

The user observed the answer as complete and incremental. This is accepted positive evidence for Native value-continuation streaming.

## Turn 3 — strongest positive response

Transport/lifecycle:

- third sequential Native submit succeeded;
- official protected Send returned HTTP200 SSE, `filtered=true`;
- terminal completed and composer returned ready.

Terminal metrics:

- `frameCount=42`
- `explicitTextPatchCount=2`
- `contextualValueStringCount=29`
- `contextualValueStringCharacters=652`
- `nativeDeltaCount=31`
- `nativeCharacters=671`
- `removedTextPatchCount=31`
- `removedTextCharacters=671`
- `webAssistantTextCharacters=45`
- `webMessageNodes=5`
- `webElementCount=678`
- `terminal=true`

The user observed the answer as complete and visibly incremental. This confirms that most assistant body text can arrive as contextual value-only string continuation frames and be intercepted before normal Web rendering.

## Accepted b50 conclusions

1. Native composer -> official browser-owned protected Send works through at least three sequential turns in this diagnostic scope.
2. Incremental Native assistant delivery is real; it is not a completion-time dump.
3. Contextual bare `{v:string}` frames carry substantial assistant text: 152 chars over 8 frames on turn 2 and 652 chars over 29 frames on turn 3.
4. The Web assistant DOM text metric remained 45 chars while Native captured 191 and 671 chars on turns 2/3, supporting the pre-React text-removal direction.
5. b50 remains only a **partial parser pass** because the first fresh/new-chat answer truncated.
6. No duplicate Send, stream error, nonterminal close or composer-continuity failure is evidenced in the three-turn capture.

## Evidence-backed first-turn hypothesis

Historical b40/b41 Runtime already established that a fresh new-chat first Send emits a `title_generation` structural event.

b50 currently clears `textContinuationActive` on every parsed non-value structural frame. The only established structural difference between the failed turn 1 and successful turns 2/3 is that turn 1 is the fresh new-chat first turn.

Therefore the smallest justified next hypothesis is:

> `title_generation` can occur after assistant text continuation has begun; because it is conversation-title metadata rather than a new assistant patch operation/path, clearing the assistant continuation context on that event may cause the observed missing middle.

This is not yet Runtime-confirmed for the failing capture because b50 did not count title-generation frames. The next Candidate must test only this specific hypothesis and record a structural counter.

## b51 gate derived from this evidence

b51 may preserve assistant-text continuation only across exact top-level `type == "title_generation"`, forward that event unchanged to Web, and count when it occurs while continuation is active. All other b50 reset behavior remains unchanged.

Passing evidence requires a fresh/new-chat long first answer with:

- complete visible Native body;
- `titleGenerationWhileContinuationCount > 0` if the hypothesis is correct;
- long-response-scale contextual/Native character totals;
- terminal true;
- Web composer ready and a second Native turn succeeds.

If title generation is absent or the first answer still truncates, do not broaden the parser by guess; collect the next smallest structural reset evidence.

## Evidence classification

- Code written: Yes
- CI passed: Yes
- Artifact produced: Yes
- Package identity verified: Yes
- Runtime/manual/real-device: **Yes — partial parser pass**
- Native incremental streaming: **Runtime Confirmed for turns 2/3**
- Complete fresh-new-chat first-turn interception: **Runtime Rejected on b50**
- Production hidden/shadow Web architecture: **Not accepted; TD-024/TD-025 unchanged**
- Stable/Frozen Send: No
