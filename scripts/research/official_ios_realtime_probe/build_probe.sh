#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
OUT="${1:-$ROOT/build}"
mkdir -p "$OUT"
SDK="$(xcrun --sdk iphoneos --show-sdk-path)"
TARGET="$OUT/ChatGPTRealtimeProbe.dylib"

xcrun --sdk iphoneos clang \
  -arch arm64 \
  -isysroot "$SDK" \
  -miphoneos-version-min=17.0 \
  -fobjc-arc -fblocks \
  -dynamiclib \
  -framework Foundation \
  -framework UIKit \
  -o "$TARGET" \
  "$ROOT/ChatGPTRealtimeProbe.m" \
  "$ROOT/ProbeBatchHooks.m" \
  "$ROOT/ProbeExportUI.m" \
  "$ROOT/ProbeEnhancerChain.m" \
  -Wl,-install_name,@rpath/ChatGPTRealtimeProbe.dylib \
  -Wl,-dead_strip

codesign --force --sign - "$TARGET"
shasum -a 256 "$TARGET" > "$TARGET.sha256"

echo "Built: $TARGET"
file "$TARGET"
otool -L "$TARGET"
cat "$TARGET.sha256"
