# DEV-send-stream untrusted project SPA entry — no continuation activation

_Date: 2026-09-03_

## Evidence class

User-supplied Web Rule Lab Runtime trace and screenshots from visible official ChatGPT Web using the same persistent WebKit session authority as production. The probe recorded only coarse route shape, user-activation/trust state, history navigation, matching request families, HTTP status and content type. It did not record message bodies, cookies, tokens or raw IDs.

## Purpose

Control A separates trusted target-entry activation from scoped route + SPA/router transition for a project/GPT-scoped conversation.

Known positive controls previously used a trusted official anchor click from `/` to `/g/{x}/c/{x}` and then started official continuation (`stream_status`, page-owned `/resume`, and 404-resume status/snapshot fallback in the current samples).

This control used the same official target anchor, but clicked it programmatically only after transient browser user activation expired.

## Preconditions

- Web Rule Lab root route: `/`.
- Target project conversation route was saved from the real official page as masked `/g/{x}/c/{x}`.
- Returned to `/` in the same document.
- Sidebar/project list was expanded.
- Anchor-presence probe returned `matchCount=1`, `visibleMatchCount=1`.
- Network/router probe was installed before target entry.

## Exact corrected Control A result

Launcher result:

- `phase=clicked_programmatically`
- `delayMs=8000`
- `activationAtClick=false`
- `matchCount=1`

Captured sequence:

1. `t=370334ms`: synthetic target-anchor click on route `/`; `isTrusted=false`, `userActivationIsActive=false`, target `/g/{x}/c/{x}`.
2. `t=370394ms`: `history.pushState.before` to `/g/{x}/c/{x}`.
3. `t=370397ms`: `history.pushState.after`; current route `/g/{x}/c/{x}`.
4. `t=370722ms`: page-owned plural snapshot GET.
5. `t=370724ms`: page-owned conversation bootstrap/detail POST.
6. `t=371695ms`: bootstrap/detail HTTP200 `application/json`.
7. `t=372718ms`: plural snapshot HTTP200 `application/json`.
8. `t=373194ms`: another plural snapshot GET.
9. `t=374971ms`: plural snapshot HTTP200 `application/json`.
10. Final probe dump at `t=423408ms` remained on `/g/{x}/c/{x}`.

From the synthetic target click to final dump was about 53 seconds. During that window the probe recorded:

- zero matching `stream_status` requests;
- zero matching `/backend-api/f/conversation/resume` requests;
- no page-owned continuation request chain.

The page visibly entered the project conversation and showed active-response UI/Stop. Therefore SPA routing and initial authoritative bootstrap were successful, but the trusted-positive continuation lifecycle was not activated.

A later unrelated trusted click inside the already-entered page was captured, but no `stream_status` followed. This does not establish that arbitrary later trusted interaction is sufficient; the strongest remaining differential is trusted **target-entry** activation/lifecycle.

## Classification

- official programmatic anchor click: Runtime Positive;
- `isTrusted=false` with `userActivationIsActive=false`: Runtime Positive;
- same-document official `history.pushState`: Runtime Positive;
- exact scoped `/g/{x}/c/{x}` route: Runtime Positive;
- conversation bootstrap/plural initial acquisition: Runtime Positive;
- page-owned continuation activation under this untrusted target entry: Runtime Negative;
- trusted target-entry activation as a necessary condition: strongest remaining hypothesis, not yet fully proven.

## Causal matrix after Control A

| Entry | Route | Result |
|---|---|---|
| Full load | `/c/{id}` | Negative in b88 project samples |
| Full load | exact official `/g/{scope}/c/{id}` | Unknown — Control B |
| SPA programmatic click | exact official `/g/{scope}/c/{id}` | Router/bootstrap Positive; continuation Negative |
| SPA trusted click | exact official `/g/{scope}/c/{id}` | Positive — two visible-Web samples |

## Next evidence gate

Control B: while the same kind of project response is deliberately active on another official client, perform a fresh full document navigation to the exact official scoped `/g/{scope}/c/{conversation}` URL and observe whether the page itself starts `stream_status -> /resume/fallback`.

- Positive would show exact scoped full-load can activate continuation and would support a route-identity-focused product change.
- Negative would leave trusted official target-entry activation/lifecycle as the strongest remaining requirement.

No product source, Candidate, Artifact or IPA identity changed in this experiment.
