#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
SRC="$ROOT/research/official-sync-reload/OfficialSyncReloadProbe.mm"
OUT_DIR="$ROOT/build/research/official-sync-reload"
OUT="$OUT_DIR/OfficialSyncReloadProbe-v01.dylib"
SDK="$(xcrun --sdk iphoneos --show-sdk-path)"

mkdir -p "$OUT_DIR"
rm -f "$OUT" "$OUT.sha256"

xcrun --sdk iphoneos clang++ \
  -arch arm64 \
  -std=c++17 \
  -fobjc-arc \
  -fblocks \
  -miphoneos-version-min=17.0 \
  -isysroot "$SDK" \
  -dynamiclib \
  -Wl,-install_name,@rpath/OfficialSyncReloadProbe-v01.dylib \
  -framework Foundation \
  -framework UIKit \
  -framework QuartzCore \
  "$SRC" \
  -o "$OUT"

codesign --force --sign - "$OUT"
shasum -a 256 "$OUT" | awk '{print $1}' > "$OUT.sha256"

file "$OUT"
otool -L "$OUT"
codesign -dvv "$OUT" 2>&1 | sed -n '1,20p'
echo "sha256=$(cat "$OUT.sha256")"
