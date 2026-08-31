from pathlib import Path

checkpoint = Path('docs/project/current/dev/DEV-send-stream.md')
text = checkpoint.read_text()
marker = '# DEV-send-stream\n\n'
assert text.startswith(marker)
assert '## Exact b75 Artifact milestone — 2026-09-01' not in text
section = '''## Exact b75 Artifact milestone — 2026-09-01

- Exact product/config source: `b77303b8870dc25851dbffbf38ffc153a47bbcb2`.
- Candidate / Version-Build: `DEV-send-stream-0.1.0-b75` / `0.1.0 (75)`.
- Clean product-code commit: `33bdb59d91ee3556899fb2c10e10014b2eea7fde`, direct parent `d43661ef4dd9a01480b11b4d70af5a79e6792bff`.
- Assembly validation `33429163152`: exact scope + `git diff --check` + Xcode 16.4 iOS Simulator build passed. Earlier b75 assembly failures were tooling-only patch-target/audit/push-permission corrections and produced no Artifact.
- Push CI `33429597213 / 99611443839` — success.
- PR CI `33429599704 / 99611451360` — success.
- Canonical Push Artifact `9772079468`.
- Artifact ZIP `sha256:6c4c4ec9de54264846376bdf7df4679daaaf33168481831698c884093b6209ad`.
- IPA `ChatGPTClient-0.1.0-b75-dev-send-stream.ipa`; SHA `a912547a1845cae182d83d551eb51955b5060062f66ec3fbdf14be45954dab9d`.
- Independent package check: `0.1.0 (75)`, Candidate b75, source marker `b77303b8870d`, Release, MinimumOSVersion 14.0, Mach-O arm64.
- b39-b75 are now permanently reserved. Runtime/manual/real-device = **Pending**. Stable/Frozen Send = **No**.

### b75 exact product behavior to test

1. External page-owned `/resume` is structural-only until exact HTTP200 `text/event-stream` response acceptance; a pre-accept 404/non-SSE must not create Native `回答失败`.
2. Successful explicit authoritative Sync/Reload clears only a terminal external response snapshot; local failed Sends are not broadly cleared.
3. Cache-miss historical geometry uses the same final b38-derived metrics but yields cooperatively on the main queue with conversation/presentation/build-generation freshness guards; resident cache reuse stays immediate.
4. Typography contract: tool line height 26; reasoning 18.2; final assistant 18.2; final measurement/rendering share one paragraph style; user bubbles unchanged.
5. Retain b67 local Send, b72 simultaneous A/B ownership, b38 Copy/round/quick-navigation, hidden-thought exclusion, and no retry/polling/timer/watchdog/second store.

### Next exact action

Install exact Build75 on iPhone/iOS17 and execute the b75 Runtime matrix: external active response adoption and pre-accept non-SSE behavior; successful Sync/Reload stale-external cleanup; 26/18.2/18.2 typography; first/changed long-history load with immediate left-edge Back; resident re-entry; local b67 Send; b72 simultaneous A/B generation. Export diagnostics. Do not allocate b76 without concrete b75 Runtime evidence.

'''
checkpoint.write_text(marker + section + text[len(marker):])

index = Path('docs/project/BUILD_TEST_INDEX.md')
text = index.read_text()
assert 'DEV-send-stream-0.1.0-b75' not in text
b74 = '| `DEV-send-stream-0.1.0-b74` | `DEV-send-stream` | `0.1.0 (74)` | exact source `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`; PR #29 open | clean reassembly `33420128454/99580192017`; Push `33420408779/99581104920`; PR `33420412792/99581117817`; Artifact `9768668727`; ZIP `sha256:6ac4cc97954a0a26ed258a9775921cc4d12b17a1ff29c5e8d65cddf3c5595cb3`; IPA `sha256:07c999fd0e9aaa5685725e6a97f066221f1f986cc3e23a99693a91accda285da`; package independently verified source `50dd61b8b31c`/Release/iOS14/arm64 | Runtime pending: resident geometry reuse, larger tool rhythm, external page-owned resume adoption + local/A-B regressions | **Exact Runtime candidate / package verified; permanently reserved** |'
assert text.count(b74) == 1
b75 = '| `DEV-send-stream-0.1.0-b75` | `DEV-send-stream` | `0.1.0 (75)` | exact source `b77303b8870dc25851dbffbf38ffc153a47bbcb2`; PR #29 open | Assembly `33429163152`; Push `33429597213/99611443839`; PR `33429599704/99611451360`; Artifact `9772079468`; ZIP `sha256:6c4c4ec9de54264846376bdf7df4679daaaf33168481831698c884093b6209ad`; IPA `sha256:a912547a1845cae182d83d551eb51955b5060062f66ec3fbdf14be45954dab9d`; package independently verified source `b77303b8870d`/Release/iOS14/arm64 | External resume validation + authoritative stale-external cleanup + cooperative geometry + exact 26/18.2/18.2 typography; Runtime pending | **Code/CI/Artifact/package verified; Runtime pending; permanently reserved** |'
index.write_text(text.replace(b74, b74 + '\n' + b75, 1))

entries = [
    ('docs/project/PROJECT_STATE.md', '## DEV-send-stream b75 current evidence — 2026-09-01', '- Exact Build75 product source `b77303b8870dc25851dbffbf38ffc153a47bbcb2`; Push/PR CI passed; Artifact `9772079468`; package independently verified. Runtime remains pending; Stable/Frozen Send remains No.\n- b75 validates external page-owned resume before Native adoption, clears only terminal external snapshots after successful explicit authoritative refresh, cooperatively schedules cache-miss history geometry, and applies tool/reasoning/final line heights 26/18.2/18.2.\n'),
    ('docs/project/MODULE_STATUS.md', '## DEV-send-stream b75 evidence — 2026-09-01', '- Conversation/Send presentation: Build75 package verified; Runtime pending. b67 local transport and b72 tested simultaneous A/B ownership remain retained.\n- External continuation: page-owned resume request alone is not response authority; Native adoption starts only after validated HTTP200 SSE.\n- Historical geometry: same deterministic metrics, cooperative cache-miss scheduling; Runtime responsiveness still requires iPhone validation.\n'),
    ('docs/project/WEB_SEND_ADAPTER.md', '## Validated external-resume adoption gate — b75', '- A matching official-page-owned `/backend-api/f/conversation/resume` request is structural observation only. Native response ownership must not begin until the matching response is validated as HTTP200 `text/event-stream`.\n- Pre-accept 404/non-SSE is non-presentational; do not create a Native failed response from it. Native still must not construct resume, derive/select offset, poll `stream_status`, replay browser/session headers, or use WebSocket frames as response-body authority.\n')
]
for filename, heading, body in entries:
    path = Path(filename)
    text = path.read_text()
    if heading not in text:
        path.write_text(text.rstrip() + '\n\n' + heading + '\n\n' + body.rstrip() + '\n')
