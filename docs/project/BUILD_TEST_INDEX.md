# Build / Test / Release Index

This file is the durable index for testable identities and evidence.

## Current identity scheme

**Unknown / Unverified for product builds and test candidates.**

No product version source, build-number source, CI artifact convention, release/tag convention, or test-candidate convention was present in the repository at bootstrap. Establish a minimal unambiguous scheme only when real product configuration or a testable artifact requirement exists.

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
