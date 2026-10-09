# Authenticated Protocol Capture fixtures

`sanitize_capture.py` converts a user-controlled real-device `authenticated-protocol-capture-v1` export into deterministic `protocol-replay-fixture-v1` input for the integrated Simulator fixture transport.

Security boundary:

- raw capture exports are local sensitive evidence and are never an automatic repository/CI input;
- the compiler drops secret-like keys and values and fails closed if reusable auth-shaped material survives output validation;
- repository fixtures may contain only endpoint/method/query structure, capture-local aliases, safe protocol enums/scalars, reduced authoritative state projections and placeholder message text lengths;
- Cookie, Authorization, access/session tokens, passwords, challenge/proof values and raw user/assistant text must never enter committed fixtures;
- aliases such as `id-0001` are capture-local correlation identities, not reversible service identifiers;
- generic unclassified `/backend-api/...` path segments preserve only structural alphabetic endpoint names (plus `_` / `-`); digit-bearing, high-entropy or otherwise identifier-like segments are exported as `{opaque}`. Explicitly classified Conversation Detail IDs use the capture-local alias mapping instead of the raw service identifier.

Replay validation remains strict: when a fixture declares a JSON request body, `SimulatorFixtureTransport` compares canonical JSON equality against the request body. The Debug-only seam accepts Foundation's equivalent `URLRequest.httpBody` or `httpBodyStream` representation; it does not loosen fixture matching or add production fallback behavior.

Typical developer flow:

1. On a logged-in user-controlled iPhone, open Settings -> Authenticated Protocol Capture.
2. Tap `开始采集`, perform the target operation normally in the embedded official Web surface, then tap `停止采集` and `导出采集包`.
3. Keep that export local/private. Run `python3 scripts/protocol_capture/sanitize_capture.py <capture.json> <fixture.json>` on the development side.
4. Review the generated fixture, then commit only the sanitized fixture if it is needed for regression coverage.
5. Simulator tests replay committed fixtures through the existing Debug-only `SimulatorFixtureTransport`; production `ConversationRepository`, `AuthSessionStore` and Web execution ownership remain unchanged.

Run `python3 scripts/protocol_capture/sanitize_capture.py --self-test` to verify the sanitizer's secret rejection/redaction path.
