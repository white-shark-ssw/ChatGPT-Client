#!/bin/bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE_DIR="$ROOT_DIR/scripts/assets"
ICON_DIR="$ROOT_DIR/ChatGPTClient/Assets.xcassets/AppIcon.appiconset"
ICON_PATH="$ICON_DIR/AppIcon-1024.png"
EXPECTED_SHA256="205ab2c7952781ffc05c68fdf8bbb621ac065093c3216c3f30b4a2c551f802a6"

mkdir -p "$ICON_DIR"
cat "$SOURCE_DIR"/AppIcon-1024.b64.part* | /usr/bin/base64 -D > "$ICON_PATH"
ACTUAL_SHA256="$(shasum -a 256 "$ICON_PATH" | awk '{print $1}')"

if [[ "$ACTUAL_SHA256" != "$EXPECTED_SHA256" ]]; then
  echo "App icon checksum mismatch: expected $EXPECTED_SHA256, got $ACTUAL_SHA256" >&2
  rm -f "$ICON_PATH"
  exit 1
fi

echo "App icon reconstructed: $ICON_PATH"
