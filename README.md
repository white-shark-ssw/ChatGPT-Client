# ChatGPT-Client

Native iOS third-party ChatGPT client project.

## Current baseline

The first application foundation is implemented as Swift 5 + UIKit with no third-party dependencies and an iOS 14.0 deployment target.

Accepted foundation candidate: `DEV-app-foundation-0.1.0-b1` (`0.1.0 (1)`). It has reached Code written + CI passed + Artifact produced + Runtime/manual/real-device tested on iPhone / iOS 17.0 through TrollStore. The foundation is Stable, not Frozen; lower iOS versions and iPad runtime remain unverified.

The next serial implementation phase is `DEV-auth-bootstrap`, which must establish current real-device Google-based ChatGPT login/session evidence before private conversation protocol implementation begins.

## Diagnostics

The accepted foundation includes structured local diagnostics from the first executable build:

- OSLog events;
- bounded persistent JSONL history;
- trace/span correlation and timing;
- secret-field filtering;
- build/candidate/runtime metadata;
- user-triggered redacted diagnostic JSON export.

Do not log passwords, OAuth codes, tokens, Cookie/Authorization values, complete chat bodies or attachment contents by default.

## Build

On macOS with Xcode:

```bash
bash scripts/build_ipa.sh
```

The foundation CI workflow is `.github/workflows/ios-foundation.yml`.

## AI governance

AI-assisted project work is governed by root `AGENTS.md` and `docs/project/START_HERE.md`. Current project state, roadmap, module status, technical decisions, build/test identities, project-specific rules and active checkpoints are maintained under `docs/project/`.
