# DEV-send-stream b48 Runtime evidence

- Candidate: `DEV-send-stream-0.1.0-b48`
- Version / Build: `0.1.0 (48)`
- Exact product/config source: `6ccba03cefaa32a1186f1f468c3e696ed9457699`
- Runtime Artifact: `9718885751`
- IPA SHA-256: `c1f2f6a4e750af8abc7438e289f709cdf23c564f06ce2118b1c9b74f2d8ed850`
- Runtime device: iPhone / iOS 17.0
- Evidence time: 2026-08-30 local session; diagnostics exported `2026-08-29T18:12:14Z`
- Scope: isolated diagnostic exception only; not production architecture acceptance and not a TD-024/TD-025 change.

## User-observed result

- The user interacted with the Native composer rather than the Web composer.
- First Native message visibly submitted, but assistant text did not appear incrementally in the Native output area.
- The user then submitted a second Native message in the same probe session.
- In the ordinary Native conversation list, the newly created server conversation appeared. Opening it showed that the assistant had answered both submitted user messages.
- Screenshot during the second active response showed `Send 2`, Web composer not-ready / response active, both Native user messages visible in the diagnostic Native surface, and no Native assistant body rendered.

## Exact diagnostics facts

Metadata exactly matched b48 / Release / iPhone / iOS17.0 / source marker `6ccba03cefaa`.

### First turn

- Native submit attempt 1 recorded `promptCharacters=21`.
- Web composer strategy was `prompt_textarea`.
- Native submit result: `submitted`.
- Official protected Send was observed on an `existing_conversation` page after new-chat creation.
- Send response: HTTP200 `text/event-stream`, `filtered=true`.
- Terminal metrics after 268 SSE frames:
  - `removedTextPatchCount=0`
  - `removedTextCharacters=0`
  - `nativeDeltaCount=0`
  - `nativeCharacters=0`
  - `webAssistantTextCharacters=5864`
  - `webMessageNodes=2`
  - `webElementCount=951`
  - `terminal=true`
- Web composer returned ready after terminal.

### Second turn

- Native submit attempt 2 recorded `promptCharacters=25`.
- Native submit result: `submitted`.
- Official protected Send again observed on the same existing conversation.
- Send response again HTTP200 `text/event-stream`, `filtered=true`.
- Export occurred about 16 seconds into the second active response, before its terminal metrics were emitted.
- User later verified in the ordinary Native conversation detail that the assistant had answered both turns.

## Accepted Runtime conclusions

1. **Native composer -> Web composer state -> official protected Send works on this exact b48 new-chat/two-turn path.** The user did not need to touch the Web composer.
2. **Sequential conversation state survived at least two Native-composer Sends.** The second Send succeeded in the same newly created conversation; there was no evidence of parent/branch state break before the second request.
3. **The b48 SSE interception hook did capture the official response transport**, because each Send returned HTTP200 SSE with `filtered=true` through the wrapper.
4. **Native assistant streaming failed completely in b48.** Zero text patches were removed and zero Native text deltas were delivered.
5. **Web rendering was therefore not reduced in b48.** The first assistant response still accumulated 5864 Web assistant-text characters.
6. The new conversation was authoritative and visible through the existing Native read/list path, with both assistant answers later readable there.

## Deterministic implementation defect found after Runtime

The b48 filter's `scrubTextPatches` looks for verbose patch fields:

- `node.op === "append"`
- `node.path === "/message/content/parts/0"`
- `node.value`

Current repository evidence from exact b40's real Send probe uses compact patch fields instead:

- operation: `o`
- path: `p`
- value: `v`
- batch patch envelope: `o === "patch"` with `v` array items carrying compact `o/p` fields.

Therefore b48's zero-match result is explained by a source-backed parser-field mismatch, not by absence of assistant text patches or failure of the fetch hook.

## Classification

- Native composer bridge: **Runtime positive for tested new-chat + second-turn scope**.
- Official protected Send via Web runtime: **Runtime positive**.
- Second sequential Native-composer Send: **Runtime positive**.
- Native incremental assistant text: **Runtime failed due deterministic b48 parser defect**.
- Web assistant DOM/text suppression by filtered SSE: **Not achieved in b48**.
- Existing long-conversation performance: **Not tested / still Unknown**.
- Production hidden/shadow-Web architecture: **Not accepted; durable boundary unchanged**.

## Next exact evidence action

Because b48 Artifact identity is emitted and permanently reserved, any product correction requires b49+. Make the smallest b49 correction to parse the already-evidenced compact `o/p/v` patch form while preserving the b48 Native composer, official Send path, no-clone stream transform, privacy boundary and two-turn Runtime gate. Do not expand into existing-conversation history virtualization until corrected Native streaming/filtered-Web behavior is proven.