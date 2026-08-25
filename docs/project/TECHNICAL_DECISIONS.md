# Technical Decisions

This file records durable, evidence-backed technical decisions and rejected routes.

## Decision template

### TD-XXX — <title>

- **Status**: Proposed / Confirmed / Rejected / Frozen / Superseded
- **Date**:
- **Scope**:
- **Decision**:
- **Evidence**:
- **Alternatives considered**:
- **Rejected / do-not-repeat**:
- **Affected modules**:
- **Validation level**:
- **Supersedes**:
- **Notes**:

## Current decisions

### TD-001 — Product direction is an iOS native ChatGPT client

- **Status**: Confirmed
- **Date**: 2026-08-25
- **Scope**: Product direction / architecture baseline
- **Decision**: The current repository will be developed as an iOS native ChatGPT client. Product code should start from a new native-client baseline rather than treating the previous WebView client as the source to convert.
- **Evidence**: User explicit requirement in the current conversation; repository purpose already identifies a ChatGPT third-party custom client.
- **Alternatives considered**: Continue the previous WebView client as the primary chat runtime.
- **Rejected / do-not-repeat**: Do not inherit the old WebView chat implementation as the new source baseline by default.
- **Affected modules**: Future application architecture; concrete modules not yet created.
- **Validation level**: User-confirmed product requirement; no product code exists yet.
- **Supersedes**: None.
- **Notes**: This decision does not yet select UIKit vs SwiftUI, language/package stack, minimum iOS version, or login implementation.

### TD-002 — Previous-project history is reference-only evidence

- **Status**: Confirmed
- **Date**: 2026-08-25
- **Scope**: Historical evidence / protocol research / architecture reuse
- **Decision**: `ChatGPT_iOS_Native_Client_History_Pack_2026-08-25.zip` is retained conceptually as prior-project experience. Historical endpoint names, request/response shapes, WebView workarounds, diagnoses, and architecture suggestions must be revalidated before becoming current implementation facts or contracts.
- **Evidence**: User explicitly described the attachment as experience from the previous project and allowed it to be used as reference; the pack itself repeatedly marks old ChatGPT private API details as historical clues only.
- **Alternatives considered**: Treat the old pack as current API/specification or import old WebView implementation as the new baseline.
- **Rejected / do-not-repeat**: Do not implement private ChatGPT protocol behavior from old names or memory alone; do not confuse historical CI/artifact success with current runtime validation.
- **Affected modules**: Future protocol/network layer, authentication, conversation state, attachments, export, performance work.
- **Validation level**: User-confirmed evidence classification; no current protocol implementation exists yet.
- **Supersedes**: None.
- **Notes**: Distilled reference lessons are stored in `HISTORICAL_REFERENCE.md`.

## Rule

Do not write speculation here as fact. A historical plan is not proof of implementation.
