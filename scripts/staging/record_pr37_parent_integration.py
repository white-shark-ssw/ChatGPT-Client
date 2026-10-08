from pathlib import Path

CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream-round7-runtime-addendum.md")
INDEX = Path("docs/project/BUILD_TEST_INDEX.md")

if "## PR #37 Simulator baseline integration complete — DEV-send-stream owner" not in CHECKPOINT.read_text():
    raise SystemExit("missing durable DEV-send-stream PR37 integration record")
if "## Simulator baseline parent integration — 2026-10-09" not in INDEX.read_text():
    raise SystemExit("missing durable Simulator baseline integration index")

print("PR37 parent integration record already durable; no mutation required")
