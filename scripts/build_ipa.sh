#!/bin/bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BUILD_DIR="$ROOT_DIR/build"
DERIVED_DATA="$BUILD_DIR/DerivedData"
ARTIFACT_DIR="$BUILD_DIR/artifacts"
STAGING_DIR="$BUILD_DIR/ipa-staging"
PROJECT="$ROOT_DIR/ChatGPTClient.xcodeproj"
SCHEME="ChatGPTClient"
SOURCE_COMMIT="$(git -C "$ROOT_DIR" rev-parse --short=12 HEAD 2>/dev/null || echo unknown)"
CANDIDATE="${DIAGNOSTICS_CANDIDATE:-DEV-multi-conversation-state-0.1.0-b19}"

rm -rf "$BUILD_DIR"
mkdir -p "$ARTIFACT_DIR" "$STAGING_DIR/Payload"

bash "$ROOT_DIR/scripts/reconstruct_app_icon.sh"

xcodebuild \
  -project "$PROJECT" \
  -scheme "$SCHEME" \
  -configuration Release \
  -sdk iphoneos \
  -derivedDataPath "$DERIVED_DATA" \
  CODE_SIGNING_ALLOWED=NO \
  CODE_SIGNING_REQUIRED=NO \
  SOURCE_COMMIT="$SOURCE_COMMIT" \
  DIAGNOSTICS_CANDIDATE="$CANDIDATE" \
  build

APP_PATH="$DERIVED_DATA/Build/Products/Release-iphoneos/ChatGPTClient.app"
if [[ ! -d "$APP_PATH" ]]; then
  echo "Expected app bundle not found: $APP_PATH" >&2
  exit 1
fi

cp -R "$APP_PATH" "$STAGING_DIR/Payload/"
PLIST="$APP_PATH/Info.plist"
VERSION="$(/usr/libexec/PlistBuddy -c 'Print :CFBundleShortVersionString' "$PLIST")"
BUILD_NUMBER="$(/usr/libexec/PlistBuddy -c 'Print :CFBundleVersion' "$PLIST")"
IPA_NAME="ChatGPTClient-${VERSION}-b${BUILD_NUMBER}-dev-multi-conversation-state.ipa"
IPA_PATH="$ARTIFACT_DIR/$IPA_NAME"

(
  cd "$STAGING_DIR"
  /usr/bin/zip -qry "$IPA_PATH" Payload
)

shasum -a 256 "$IPA_PATH" | tee "$IPA_PATH.sha256"
echo "IPA: $IPA_PATH"
echo "Candidate: $CANDIDATE"
echo "Source commit: $SOURCE_COMMIT"
