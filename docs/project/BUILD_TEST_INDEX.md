# Build / Test / Release Index

This file is the durable index for testable identities and evidence.

## Current identity scheme

**Unknown / Unverified for product version/build/test candidate numbering.**

No product version source, build-number source, CI artifact convention, release/tag convention, or test-candidate convention was present in the repository at bootstrap. Establish a minimal unambiguous scheme only when real product configuration or a testable artifact requirement exists.

Verified distribution requirement: runnable/distributable product artifacts are expected to be **IPA files suitable for installation through TrollStore**. Exact signing/packaging commands and artifact naming remain Unknown / Unverified until an Xcode project/build pipeline exists.

Compatibility evidence for future artifacts must record the actual deployment target and the iOS versions/devices on which runtime testing was performed. The intended user environment does not exceed iOS 17.0, and lower-version compatibility is preferred where practical.

## Candidate table

| Candidate | Work ID | Version / Build / Tag | Branch / PR | Commit | Validation | Artifact | Runtime result | Status |
|---|---|---|---|---|---|---|---|---|
| _None yet_ |  |  |  |  |  |  |  |  |

## Uniqueness rule

Different Active tasks must not reuse the same exact candidate identity, build number, version/build tuple, release tag, artifact name, or candidate ID.

Once allocated, an Active candidate identity is reserved until explicitly completed/released and documented.

## Evidence labels

- Code written
- Static/local checks passed
- CI passed
- Artifact produced
- Runtime/manual/real-device tested
- Stable / frozen
