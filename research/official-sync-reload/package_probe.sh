#!/bin/bash
set -euo pipefail

if [[ $# -ne 3 ]]; then
  echo "usage: $0 <ChatGPT_Decrypted.zip> <OfficialSyncReloadProbe-v01.dylib> <output.ipa>" >&2
  exit 2
fi

INPUT_ZIP="$1"
PROBE_DYLIB="$2"
OUTPUT_IPA="$3"
EXPECTED_ZIP_SHA="bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80"
INSTALL_NAME="@rpath/OfficialSyncReloadProbe-v01.dylib"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
PATCHER="$ROOT/research/official-sync-reload/patch_assets_load.py"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

actual_sha="$(shasum -a 256 "$INPUT_ZIP" | awk '{print $1}')"
if [[ "$actual_sha" != "$EXPECTED_ZIP_SHA" ]]; then
  echo "official source ZIP mismatch: expected $EXPECTED_ZIP_SHA got $actual_sha" >&2
  exit 1
fi

unzip -q "$INPUT_ZIP" -d "$WORK"
APP="$WORK/Payload/ChatGPT.app"
ASSETS_DIR="$APP/Frameworks/Assets.framework"
ASSETS="$ASSETS_DIR/Assets"
BACKUP="$ASSETS_DIR/Assets.troll-fools.bak"
FRAMEWORKS="$APP/Frameworks"

python3 - "$APP/Info.plist" <<'PY'
import plistlib, sys
p = plistlib.load(open(sys.argv[1], 'rb'))
expected = {
    'CFBundleIdentifier': 'com.openai.chat',
    'CFBundleShortVersionString': '1.2026.202',
    'CFBundleVersion': '30140022279',
    'MinimumOSVersion': '17.0',
}
for key, value in expected.items():
    actual = str(p.get(key, ''))
    if actual != value:
        raise SystemExit(f'{key} mismatch: expected {value} got {actual}')
print('bundle identity verified')
PY

if [[ ! -f "$BACKUP" ]]; then
  echo "missing pre-injection Assets backup: $BACKUP" >&2
  exit 1
fi

cp -f "$BACKUP" "$ASSETS"
python3 "$PATCHER" "$ASSETS" "$INSTALL_NAME"
cp -f "$PROBE_DYLIB" "$FRAMEWORKS/OfficialSyncReloadProbe-v01.dylib"
rm -f "$FRAMEWORKS/ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib"
cat > "$APP/DEV-official-sync-reload.txt" <<'EOF'
Work-ID: DEV-official-sync-reload
Research-Identity: OfficialSyncReloadProbe-v01
Official-Bundle: com.openai.chat
Official-Version: 1.2026.202
Official-Build: 30140022279
Scope: runtime metadata/live-object acquisition only; no Sync/Reload trigger
EOF

python3 - "$ASSETS" <<'PY'
import struct, sys
from pathlib import Path
d = Path(sys.argv[1]).read_bytes()
ncmds = struct.unpack_from('<I', d, 16)[0]
off = 32
names = []
for _ in range(ncmds):
    cmd, size = struct.unpack_from('<II', d, off)
    if cmd in {0xC,0xD,0x80000018,0x8000001F,0x80000023}:
        noff = struct.unpack_from('<I', d, off + 8)[0]
        end = d.find(b'\0', off + noff, off + size)
        names.append(d[off + noff:end].decode('utf-8','replace'))
    off += size
wanted = '@rpath/OfficialSyncReloadProbe-v01.dylib'
if wanted not in names:
    raise SystemExit('probe load command missing')
if any('ChatGPTEnhancer' in name for name in names):
    raise SystemExit('unrelated enhancer load command still present')
print('isolated Assets load command verified')
PY

mkdir -p "$(dirname "$OUTPUT_IPA")"
rm -f "$OUTPUT_IPA" "$OUTPUT_IPA.sha256"
(
  cd "$WORK"
  zip -qry "$OUTPUT_IPA" Payload
)
shasum -a 256 "$OUTPUT_IPA" | awk '{print $1}' > "$OUTPUT_IPA.sha256"
unzip -t "$OUTPUT_IPA" >/dev/null

echo "research IPA: $OUTPUT_IPA"
echo "sha256=$(cat "$OUTPUT_IPA.sha256")"
echo "Note: the local package intentionally does not claim Runtime validity. TrollStore must perform its normal install-time signing path."
