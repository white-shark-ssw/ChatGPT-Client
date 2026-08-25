# Project Profile

## Initialization

**Initialized — 2026-08-25**

Bootstrap inspection completed against the real repository state. Verified facts are recorded below; unsupported product details remain `Unknown / Unverified`.

## Identity

- **Project name**: ChatGPT-Client
- **Repository**: `white-shark-ssw/ChatGPT-Client`
- **Project purpose**: Develop an iOS native ChatGPT client.
- **Product type**: Native iOS third-party ChatGPT client application.
- **Primary users/runtime**: iOS users. The intended user-device environment does not exceed iOS 17.0; compatibility with lower iOS versions is preferred where practical.

## Technology stack

- **Primary language(s)**: Unknown / Unverified until product source is added.
- **Framework(s)**: Unknown / Unverified. UIKit vs SwiftUI and any supporting libraries have not yet been accepted from current source/requirements.
- **Package/dependency manager(s)**: None evidenced.
- **Important manifests/configs**: No product manifest or dependency configuration evidenced. Governance configuration lives in `AGENTS.md`, `.github/copilot-instructions.md`, and `docs/project/`.

## Repository structure

- **Main source roots**: No product source roots evidenced as of 2026-08-25.
- **Application/service entry points**: None evidenced.
- **Test roots**: None evidenced.
- **Key modules/state owners**: Governance state is owned by `docs/project/`; product modules/state owners remain Unknown / Unverified until implementation exists.

## Build and validation

- **Build command(s)**: Unknown / Unverified; no Xcode project/workspace or build configuration evidenced yet.
- **Test command(s)**: Unknown / Unverified; no test configuration evidenced.
- **Lint/static checks**: Unknown / Unverified; no lint/static configuration evidenced.
- **CI workflows**: None evidenced at bootstrap.
- **Artifact/package output**: User-required distributable form is an IPA suitable for installation through TrollStore. Exact signing/packaging/build pipeline is Unknown / Unverified until product build configuration exists.

## Versioning and candidate identity

- **Version source**: Unknown / Unverified
- **Build number source**: Unknown / Unverified
- **Release/tag scheme**: Unknown / Unverified
- **Parallel test-candidate scheme**: Unknown / Unverified
- **Artifact naming rule**: Unknown / Unverified

## Runtime / deployment

- **Supported runtime/OS/platform**: Native iOS application. The target user environment must not require an OS newer than iOS 17.0.
- **Minimum deployment target**: Unknown / Unverified. Choose the lowest practical target supported by the actual required APIs/dependencies and validated runtime behavior; do not infer `17.0` as the minimum merely because the user environment tops out at iOS 17.0.
- **Deployment / installation**: IPA installed through TrollStore.
- **Device family**: Exact iPhone/iPad support matrix is Unknown / Unverified.
- **Environment/configuration sources**: Unknown / Unverified.

## Historical reference material

The user supplied `ChatGPT_iOS_Native_Client_History_Pack_2026-08-25.zip` as experience/reference from a previous project. It is not the current source baseline and does not make historical endpoint names, WebView implementations, diagnoses, framework choices, or MVP suggestions current facts. Durable extracted lessons and evidence boundaries are summarized in `docs/project/HISTORICAL_REFERENCE.md`.

## Documentation evidence

- User explicit requirement on 2026-08-25: current project theme is development of an iOS native ChatGPT client.
- User explicit deployment/compatibility requirement on 2026-08-25: install the IPA through TrollStore; intended iOS systems do not exceed iOS 17.0; prefer compatibility with lower iOS versions.
- GitHub repository metadata: repository `white-shark-ssw/ChatGPT-Client`, default branch `main`, description `ChatGPT Third-party custom client`.
- Pre-bootstrap source baseline: `main@91f58c10cb44477b3130527f3037bb4365ea3cf5`.
- Governance baseline after initial rules merge: `main@f4ba767fde90c0258da19a92283e9f337532ca35`.
- Native-project context baseline: `main@bf71cb1152c2b114559af0ae1d74384566cc2a64`.
- No product source, manifest, tests, CI, version/build source, or concrete deployment-target config is present yet.

## Auto-refresh rule

Update this file proactively when project purpose, language/framework, build/test commands, version scheme, deployment/runtime, repository structure, or major state ownership changes.
