from pathlib import Path


def write(path, text):
    Path(path).write_text(text)


def prepend_after(path, marker, block):
    p = Path(path)
    text = p.read_text()
    if block.strip() in text:
        return
    if marker not in text:
        raise SystemExit(f"missing marker in {path}: {marker!r}")
    write(path, text.replace(marker, marker + block, 1))


# BUILD_TEST_INDEX.md
p = Path("docs/project/BUILD_TEST_INDEX.md")
text = p.read_text()
lines = text.splitlines()
b79 = "| `DEV-send-stream-0.1.0-b79` | `DEV-send-stream` | `0.1.0 (79)` | exact product/config source `a3d307b05d70e95568672bc29b0c939b7f3b8141`; PR #29 | Guarded staging validation `33488975445/99795672696`; formal Push `33489654106/99797864816`; PR `33489658656/99797878467`; canonical Push Artifact `9793240789`; ZIP `sha256:2016508002ae7ff43d803c90fcbb92ba01c45906c885be6f6e50a1e43e1e87fc`; IPA `sha256:39f64dd9146c3a8dc28cb9b733d1c56d4fbf3ff090a442c8ecbd27c672234fb4`; package Release/source `a3d307b05d70`/iOS14/arm64 | Runtime pending: symmetric reasoning/tool transition spacing; manual Sync re-arm of a newly-started remote turn; external stopped-thinking preserved as reasoning; progressive external final remains unavailable from the authorized source | **Code/static/Simulator/Push+PR CI/Artifact/package verified; Runtime Unverified; permanently reserved** |"
b78 = "| `DEV-send-stream-0.1.0-b78` | `DEV-send-stream` | `0.1.0 (78)` | exact product/config source `031b1a1f2c1d01900c2ab79ff14b1f2fb6c7e809`; clean product `180065e0faf947292a9f21b56c4ea366a5c322fe`; PR #29 | Final assembly/Xcode `33482721335/99775722851`; Push `33482983693/99776545604`; PR `33482987997/99776557269`; canonical Push Artifact `9790836559`; ZIP `sha256:7b5900a960ef680cce34642ca6cef232f201a260b182d6b640266e81982b081f`; IPA `sha256:726e3c09bcac4eb8a40a8ecb79b8abb0f145d89e41481083bc51941a7978620e`; package Release/source `031b1a1f2c1d`/iOS14/arm64 | Runtime partial/rejected: tool prominence active but transition spacing asymmetric; long user clipping case positive; external reasoning/tools only page-snapshot granular; progressive final rejected; already-open new remote turn misses live adoption; external manual stop promoted reasoning into final | **Runtime partial/rejected; permanently reserved** |"
found_header = False
found_b78 = False
out = []
for line in lines:
    if line.startswith("| `DEV-send-stream-0.1.0-b79`"):
        continue
    if line.startswith("| `DEV-send-stream-0.1.0-b78`"):
        out.append(b78)
        found_b78 = True
        continue
    out.append(line)
    if line == "|---|---|---|---|---|---|---|":
        out.append(b79)
        found_header = True
if not found_header or not found_b78:
    raise SystemExit(f"BUILD_TEST_INDEX patch guard failed header={found_header} b78={found_b78}")
write(p, "\n".join(out) + "\n")

# PROJECT_STATE.md
project_block = """## DEV-send-stream b79 candidate override — 2026-09-01\n\nExact b79 `DEV-send-stream-0.1.0-b79` / `0.1.0 (79)` is now the latest test candidate. Formal exact product/config source is `a3d307b05d70e95568672bc29b0c939b7f3b8141`. The guarded staging path `33488975445 / 99795672696` passed exact scope, `git diff --check` and Xcode 16.4 Simulator build before the validated product blobs were transplanted. Formal Push `33489654106 / 99797864816` and PR `33489658656 / 99797878467` both passed. Canonical Push Artifact `9793240789` has ZIP `sha256:2016508002ae7ff43d803c90fcbb92ba01c45906c885be6f6e50a1e43e1e87fc` and IPA `sha256:39f64dd9146c3a8dc28cb9b733d1c56d4fbf3ff090a442c8ecbd27c672234fb4`; independent unpacking confirms Release 0.1.0 (79), Candidate b79, source marker `a3d307b05d70`, MinimumOSVersion 14.0 and Mach-O arm64.\n\n- b79 gives reasoning/tool transitions one neutral 12-point separator instead of inheriting the preceding item paragraph style.\n- After explicit manual Sync, a changed latest user turn may force one same-conversation covered-page reload/re-arm when no live response is active; there is still no timer/poll/watchdog or automatic Sync implementation.\n- An external page-owned terminal without a real final body no longer promotes reasoning into final; the local protected-Send compatibility fallback remains limited to local responses. Stopped external reasoning is presented as `已停止思考`.\n- b78 remains the Runtime evidence predecessor: external reasoning/tool observation is only page-snapshot granular and external progressive final still has no authorized source. b79 does not fake final streaming.\n- Runtime/manual/real-device b79: **Pending / Unverified**. Stable/Frozen Send: **No**. b39-b79 are permanently reserved.\n\n"""
prepend_after("docs/project/PROJECT_STATE.md", "# Project State\n\n", project_block)

# MODULE_STATUS.md
module_block = """## DEV-send-stream b79 candidate override — 2026-09-01\n\n- Build/runtime metadata: exact b79 source `a3d307b05d70e95568672bc29b0c939b7f3b8141`; guarded staging `33488975445 / 99795672696` passed exact scope + `git diff --check` + Xcode 16.4 Simulator; formal Push `33489654106 / 99797864816` and PR `33489658656 / 99797878467` passed; canonical Artifact `9793240789`; ZIP `20165080...e87fc`; IPA `39f64dd9...34fb4`; package independently verified as Release 0.1.0 (79), Candidate b79, source `a3d307b05d70`, iOS14 minimum, arm64. Runtime pending.\n- Tool activity presentation: inter-item spacing now has one neutral separator owner instead of preceding reasoning/tool paragraph ownership; real-device symmetry remains the acceptance gate.\n- Covered external continuation: explicit Sync detecting a changed latest user may reload/re-arm the already-current covered official page once, preserving the page-owned observation model and adding no polling/automatic Sync.\n- External stop semantics: external terminal-without-final preserves reasoning/tools and uses stopped-thinking presentation; local protected-Send terminal fallback remains unchanged.\n- External progressive final remains unavailable from the currently authorized source; b79 adds no fake stream, DOM body, WebSocket body, retry, timer, watchdog or second state owner.\n- Stable/Frozen Send remains No; b39-b79 are permanently reserved.\n\n"""
prepend_after("docs/project/MODULE_STATUS.md", "# Module Status\n\n", module_block)

# DEVELOPMENT_PLAN.md
p = Path("docs/project/DEVELOPMENT_PLAN.md")
text = p.read_text()
old_update = "_Last updated: 2026-09-01 through exact DEV-send-stream b76 Code/static/Simulator/Push+PR CI/Artifact/package verification; the next gate is b76 real-device Runtime._"
new_update = "_Last updated: 2026-09-01 through exact DEV-send-stream b79 Code/static/Simulator/Push+PR CI/Artifact/package verification; the next gate is b79 real-device Runtime._"
if old_update in text:
    text = text.replace(old_update, new_update, 1)
elif new_update not in text:
    raise SystemExit("DEVELOPMENT_PLAN last-updated guard failed")
block = """\n## Current DEV-send-stream b79 gate — 2026-09-01\n\n- Exact candidate `DEV-send-stream-0.1.0-b79` / `0.1.0 (79)`; source `a3d307b05d70e95568672bc29b0c939b7f3b8141`; Push `33489654106 / 99797864816`; PR `33489658656 / 99797878467`; canonical Artifact `9793240789`; IPA SHA `39f64dd9146c3a8dc28cb9b733d1c56d4fbf3ff090a442c8ecbd27c672234fb4`.\n- b79 implements only the b78 Runtime-backed corrections: neutral reasoning/tool transition spacing, explicit-manual-Sync same-page re-arm after a changed latest user turn, and preservation of external stopped-thinking reasoning instead of synthesizing final body text.\n- External reasoning/tool continuation remains page-snapshot granular. External progressive final still has no authorized progressive source; do not fake it. Automatic Sync remains future evidence work and must not be implemented as fixed polling.\n- **Next gate is Human Runtime:** verify symmetric tool spacing, manual Sync adopts an already-open conversation's newly-started external response, stopped external reasoning displays as stopped reasoning rather than body text, and retained b67/b72 behavior where practical. Stable/Frozen remains No.\n"""
marker = "\n## Purpose / delivery principles\n"
if "## Current DEV-send-stream b79 gate — 2026-09-01" not in text:
    if marker not in text:
        raise SystemExit("DEVELOPMENT_PLAN insertion marker missing")
    text = text.replace(marker, block + marker, 1)
write(p, text)
