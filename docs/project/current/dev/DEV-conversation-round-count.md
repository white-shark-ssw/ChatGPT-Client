# DEV-conversation-round-count

## Status

**Active — b32 Runtime partial/failing; b33 clean product/config commit prepared on latest checkpoint head**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Implement and real-device tune the Phase 8 conversation metadata/settings bundle: compact official-style header, active-branch round count, historical message time, visible-text Copy, adaptive round navigation, centralized persisted Preferences, first-entry latest placement, and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open.
- **Verified branch head before this checkpoint write**: `7712a44df56eae68bc4731cabc548ca368bc46cb`.
- **Current main**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- **Batch A**: governance synchronization complete; no product/state-owner overlap evidenced.

## Runtime / candidate history

- b24 identity rejected/reserved.
- b25-b30 partial/failing iterations.
- b31 accepted precise user-row landing but rejected hitch/raw internal rows/Copy glyph.
- b32 exact identity valid. Runtime accepted recipient filtering, compact Copy direction and precise semantic landing; still rejects jump smoothness and bottom-rubber-band direction.

### Exact b32

- Candidate `DEV-conversation-round-count-0.1.0-b32`; version/build `0.1.0 (32)`.
- Product/config source `ea2b7bf4ee89acbb748f2b3aec5fcfc61555b2bc`.
- Push Run/Job `33177491033` / `98869786437`, success.
- Runtime Artifact `9688235425`; ZIP `sha256:17c6639b5ec2b106cab936c5de357b65671c116701127ed88dfbe92bb8378445`.
- IPA `ChatGPTClient-0.1.0-b32-dev-conversation-round-count.ipa`; SHA `f1eb4e6fb8cda58db0216df080ea90098ce681e1ed47962eebda57f803f9be80`.
- b32 Runtime long/tool-heavy sample: `filteredRecipientMessageCount=748`, ordinary visible messages `84`; raw tool rows no longer ordinary chat rows. Landing remained precise. Bottom direction + jump smoothness rejected.

## b33 scoped correction

1. Keep `ConversationRoundProjection`, user-message semantic targets, transient cursor, real-drag ownership and native animated `scrollToRow`.
2. Physical top/bottom boundaries outrank drag delta, including rubber-band overscroll.
3. On animation completion, measure native landing; only apply a nonanimated re-anchor when absolute error exceeds `1pt`.
4. Log privacy-safe `nativeLandingErrorPoints` and `landingCorrectionApplied`.
5. Do not change recipient filter, round derivation, Copy presentation, list reconciliation, network behavior, or state ownership.

## Clean b33 audit / recovery point

- Candidate identity: `DEV-conversation-round-count-0.1.0-b33` / `0.1.0 (33)`.
- Clean source blob `027c8b3df05b0bd7a15957fe3db78c551008f744`.
- Xcode identity blob `96a8b2124a2a6dd84ec6f682aaa9c60b205db37e`.
- Workflow identity blob `2d3fb98fd7c1c6b129c4d1dc57558e924a14f9d0`.
- Clean product/config commit prepared on latest verified pre-write head: `856a578e1ae6064864ee1c52a169a86f100812f6`, parent `7712a44d...`, tree `173c06903b19f203f75569d66971f234e00aa04c`.
- Parent→product diff is exactly 3 files: workflow identity 2+/2-, Xcode build/Candidate identity 4+/4-, source 28+/15-.
- Audit confirms the earlier dirty staged blob is not used. No duplicate request-start `.resume()` changes remain; `AuthTransientSession.dataTask` remains request-start authority.
- Source delta is only physical-boundary direction + conditional landing correction/diagnostics. No retry/timer/watchdog/cache/network/list/filter/Copy/state-owner changes.

Because this checkpoint write itself advances branch history, **do not force the branch backward to `856a578e...`**. Recovery must read the new checkpoint-created branch head, rebuild the exact same deterministic 3-file b33 tree on that head, compare the parent→new commit diff for exact equivalence, then fast-forward the branch. Do not write another checkpoint before that ref update.

## Remaining batches

- **Batch B**: read branch head after this checkpoint; rebuild exact 3-file b33 commit on it; verify diff; `update_ref` fast-forward; verify branch + PR.
- **Batch C**: exact b33 push CI/Runtime Artifact + current-main PR merge-view; verify package identity, IPA SHA, Candidate/source markers.
- **Batch D**: update checkpoint and durable project docs with exact b32 Runtime + b33 Code/CI/Artifact truth. Docs-only commits must not redefine product/config source.

## Validation state

- Code written: b33 clean source/config constructed and audited; final branch commit pending only because checkpoint ancestry must be retained.
- Static/source audit: passed for the exact 3-file b33 delta.
- CI/Artifact: b33 pending.
- Runtime/manual/real-device: b32 partial/failing; b33 pending.
- Stable/Frozen: No.

## Do not repeat

Do not reuse b24-b32 identities; do not use dirty source blob `a09eb28b...`; do not force branch backward to staged commits; do not add retry/timer/watchdog/row-height cache/alternate navigation owner/network route/duplicate request start/second conversation authority; do not modify another task checkpoint.

## Next exact action

Read the branch head created by this checkpoint write, build the exact same clean 3-file b33 product commit on that latest head, verify the diff, fast-forward the branch without another pre-ref checkpoint write, then immediately verify PR/base and continue into CI/Artifact.
