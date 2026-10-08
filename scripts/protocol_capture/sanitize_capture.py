#!/usr/bin/env python3
import argparse
import json
import re
import tempfile
from pathlib import Path

SECRET_PATTERN = re.compile(r"password|passwd|token|cookie|authorization|credential|secret|oauth|session|proof|turnstile|conduit", re.I)
SECRET_VALUE_PATTERN = re.compile(r"bearer\s+|set-cookie:|authorization:|password=|session(token)?=", re.I)
SAFE_ALIAS = re.compile(r"^id-\d{4}$")


def scrub(value, key=""):
    if SECRET_PATTERN.search(key):
        return "<redacted>"
    if isinstance(value, dict):
        return {str(k): scrub(v, str(k)) for k, v in sorted(value.items()) if not SECRET_PATTERN.search(str(k))}
    if isinstance(value, list):
        return [scrub(item, key) for item in value]
    if isinstance(value, str):
        if SECRET_VALUE_PATTERN.search(value):
            return "<redacted>"
        return value
    return value


def materialize_path(template, parameters):
    path = str(template or "")
    for key, value in (parameters or {}).items():
        if not isinstance(value, str) or not SAFE_ALIAS.fullmatch(value):
            raise ValueError(f"unsafe or missing path alias for {key}")
        path = path.replace("{" + key + "}", value)
    if "{" in path or not path.startswith("/backend-api/"):
        raise ValueError(f"unresolved or unsafe replay path: {path}")
    return path


def detail_projection_to_body(projection):
    if not isinstance(projection, dict):
        raise ValueError("detail projection must be an object")
    conversation_id = projection.get("conversationID")
    current_node = projection.get("currentNode")
    if not isinstance(conversation_id, str) or not SAFE_ALIAS.fullmatch(conversation_id):
        raise ValueError("detail projection is missing a safe conversation alias")
    if not isinstance(current_node, str) or not SAFE_ALIAS.fullmatch(current_node):
        raise ValueError("detail projection is missing a safe current-node alias")
    nodes = projection.get("nodes") or []
    included = {node.get("nodeID") for node in nodes if isinstance(node, dict) and isinstance(node.get("nodeID"), str)}
    mapping = {}
    child_by_parent = {}
    for node in nodes:
        node_id = node.get("nodeID")
        if not isinstance(node_id, str) or not SAFE_ALIAS.fullmatch(node_id):
            continue
        raw_parent = node.get("parentID")
        parent_id = raw_parent if isinstance(raw_parent, str) and raw_parent in included else None
        if parent_id:
            child_by_parent.setdefault(parent_id, []).append(node_id)
        message_projection = node.get("message")
        message = None
        if isinstance(message_projection, dict):
            message_id = message_projection.get("messageID")
            text_characters = int(message_projection.get("textCharacters") or 0)
            placeholder = f"[captured-text:{text_characters}]" if text_characters > 0 else ""
            message = {
                "id": message_id if isinstance(message_id, str) and SAFE_ALIAS.fullmatch(message_id) else f"{node_id}-message",
                "author": {"role": message_projection.get("role") or "unknown"},
                "content": {"content_type": message_projection.get("contentType") or "text", "parts": [placeholder] if placeholder else []},
                "status": message_projection.get("status") or "unknown",
                "end_turn": message_projection.get("endTurn"),
                "metadata": {"capture_original_text_characters": text_characters}
            }
            if message_projection.get("recipient"):
                message["recipient"] = message_projection["recipient"]
            if message_projection.get("finishType"):
                message["metadata"]["finish_details"] = {"type": message_projection["finishType"]}
        mapping[node_id] = {"id": node_id, "parent": parent_id, "children": [], "message": message}
    for parent, children in child_by_parent.items():
        if parent in mapping:
            mapping[parent]["children"] = children
    return {
        "conversation_id": conversation_id,
        "id": conversation_id,
        "current_node": current_node,
        "mapping": mapping,
        "conversation_async_status": projection.get("asyncStatus")
    }


def compile_fixture(capture):
    if capture.get("schema") != "authenticated-protocol-capture-v1":
        raise ValueError("unsupported capture schema")
    requests = {}
    responses = {}
    response_bodies = {}
    request_bodies = {}
    stream_events = {}
    for wrapper in capture.get("events") or []:
        event = wrapper.get("event") if isinstance(wrapper, dict) else None
        if not isinstance(event, dict):
            continue
        request_id = event.get("requestID")
        if not isinstance(request_id, str):
            continue
        kind = event.get("kind")
        if kind == "request": requests[request_id] = event
        elif kind == "request_body": request_bodies[request_id] = event
        elif kind == "response": responses[request_id] = event
        elif kind == "response_body": response_bodies[request_id] = event
        elif kind == "sse_event": stream_events.setdefault(request_id, []).append(event)

    interactions = []
    observations = []
    for request_id, request in requests.items():
        response = responses.get(request_id)
        body_event = response_bodies.get(request_id)
        if not response:
            continue
        route = request.get("route")
        fixture_request_body = request.get("fixtureBody")
        if fixture_request_body is None and request_id in request_bodies:
            fixture_request_body = request_bodies[request_id].get("fixtureBody")
        fixture_response_body = body_event.get("fixtureBody") if isinstance(body_event, dict) else None
        detail_projection = body_event.get("detailProjection") if isinstance(body_event, dict) else None
        replay_body = None
        if route == "stop_conversation" and isinstance(fixture_response_body, dict):
            replay_body = fixture_response_body
        elif route == "conversation_detail_web" and isinstance(detail_projection, dict):
            replay_body = detail_projection_to_body(detail_projection)
        if replay_body is not None:
            path = materialize_path(request.get("pathTemplate"), request.get("pathParameters") or {})
            interaction = {
                "request": {"method": request.get("method") or "GET", "path": path},
                "response": {"status": int(response.get("status") or 0), "contentType": response.get("contentType") or "application/json", "body": replay_body}
            }
            if isinstance(fixture_request_body, dict):
                interaction["request"]["body"] = fixture_request_body
            query = request.get("query")
            if isinstance(query, dict) and query:
                interaction["request"]["query"] = query
            interactions.append(interaction)
        if request_id in stream_events:
            observations.append({"route": route, "pathTemplate": request.get("pathTemplate"), "sseEvents": [event.get("payload") for event in stream_events[request_id]]})

    if not interactions and not observations:
        raise ValueError("capture contains no replayable protocol evidence")
    fixture = {"schema": "protocol-replay-fixture-v1", "sourceCaptureSchema": capture.get("schema"), "interactions": interactions}
    if observations:
        fixture["observations"] = observations
    fixture = scrub(fixture)
    encoded = json.dumps(fixture, ensure_ascii=False, sort_keys=True)
    if SECRET_VALUE_PATTERN.search(encoded) or re.search(r'"(?:authorization|cookie|accessToken|sessionToken|password)"', encoded, re.I):
        raise ValueError("secret-like value survived fixture compilation")
    return fixture


def self_test():
    capture = {
        "schema": "authenticated-protocol-capture-v1",
        "Authorization": "Bearer SHOULD-NOT-SURVIVE",
        "events": [
            {"event": {"kind": "request", "requestID": "doc:1", "route": "stop_conversation", "method": "POST", "pathTemplate": "/backend-api/stop_conversation", "pathParameters": {}, "query": {}, "fixtureBody": {"conversation_id": "id-0001", "exclude_async_types": []}, "cookie": "secret"}},
            {"event": {"kind": "response", "requestID": "doc:1", "route": "stop_conversation", "status": 200, "contentType": "application/json"}},
            {"event": {"kind": "response_body", "requestID": "doc:1", "route": "stop_conversation", "fixtureBody": {"last_message_id": None, "status": "ok", "sessionToken": "secret"}}}
        ]
    }
    fixture = compile_fixture(capture)
    text = json.dumps(fixture, sort_keys=True)
    assert "SHOULD-NOT-SURVIVE" not in text and "Bearer" not in text and "sessionToken" not in text and "cookie" not in text.lower()
    assert fixture["interactions"][0]["request"]["body"]["conversation_id"] == "id-0001"
    assert fixture["interactions"][0]["response"]["body"]["status"] == "ok"
    print("protocol capture sanitizer self-test: ok")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?")
    parser.add_argument("output", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if not args.input or not args.output:
        parser.error("input and output are required unless --self-test is used")
    capture = json.loads(Path(args.input).read_text())
    fixture = compile_fixture(capture)
    Path(args.output).write_text(json.dumps(fixture, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
