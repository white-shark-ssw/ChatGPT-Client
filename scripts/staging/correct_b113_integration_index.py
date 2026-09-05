from pathlib import Path

path = Path("docs/project/BUILD_TEST_INDEX.md")
text = path.read_text()
old = "**Human Runtime Positive for the tested b113 native message-presentation scope / stacked integration pending / Stable-Frozen No; permanently reserved**"
new = "**Human Runtime Positive for the tested b113 native message-presentation scope / stacked integration complete at `4a22086f7ccab39427c46a163854e8f68530c65f` / Stable-Frozen No; permanently reserved**"

if new in text:
    raise SystemExit(0)
if text.count(old) != 1:
    raise SystemExit(f"expected exactly one stale b113 candidate status, found {text.count(old)}")
path.write_text(text.replace(old, new, 1))
