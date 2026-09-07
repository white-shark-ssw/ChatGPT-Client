from pathlib import Path

index_path = Path("docs/project/BUILD_TEST_INDEX.md")
checkpoint_path = Path("docs/project/current/dev/DEV-message-rendering.md")

index = index_path.read_text()
checkpoint = checkpoint_path.read_text()

candidate = "DEV-message-rendering-0.1.0-b113"
if candidate in index:
    raise SystemExit("b113 already exists in BUILD_TEST_INDEX")

marker = "|---|---|---|---|---|---|---|\n"
row = "| `DEV-message-rendering-0.1.0-b113` | `DEV-message-rendering` | `0.1.0 (113)` | stacked on Runtime-positive b112 head `50432b8743f3391a8174a3b7aae745298082d433`; product/PR pending | Candidate allocated; exact product scope `ChatGPTClient.xcodeproj/project.pbxproj` + `ChatGPTClient/Conversation/ConversationFeature.swift`; CI/Artifact pending | Human Runtime pending: user bare URL only blue while adjacent ordinary text stays label; assistant headings/emphasis/code/table/filecite render natively/readably; preserve b112 role-isolated color behavior and full-message Copy | **Allocated / Code pending / CI pending / Artifact pending / Human Runtime pending / Stable-Frozen No; permanently reserved** |\n"
if marker not in index:
    raise SystemExit("BUILD_TEST_INDEX table marker missing")
index = index.replace(marker, marker + row, 1)

old_validation = "- **Validation state**: Design/source evidence only; no product code written yet."
new_validation = "- **Validation state**: Candidate b113 durably allocated; product code not yet written."
old_pending = "- **Pending**: Record b113 in durable Build/Test index, implement minimum native renderer, preserve long-message chunk correctness, compile/CI/package, then Human Runtime on the exact screenshot scenario."
new_pending = "- **Pending**: Implement minimum native renderer, preserve long-message chunk correctness, compile/CI/package, then Human Runtime on the exact screenshot scenario."
old_batch = "- **Batch A — pending**: prepend one `DEV-message-rendering-0.1.0-b113` row to `docs/project/BUILD_TEST_INDEX.md` as allocated / Code pending / Artifact pending; update this checkpoint to confirm durable allocation."
new_batch = "- **Batch A — completed**: `DEV-message-rendering-0.1.0-b113` / Build113 is durably recorded in `BUILD_TEST_INDEX.md` as this task's unique reserved candidate before product changes."
for old in (old_validation, old_pending, old_batch):
    if old not in checkpoint:
        raise SystemExit(f"checkpoint marker missing: {old}")
checkpoint = checkpoint.replace(old_validation, new_validation, 1).replace(old_pending, new_pending, 1).replace(old_batch, new_batch, 1)

index_path.write_text(index)
checkpoint_path.write_text(checkpoint)
