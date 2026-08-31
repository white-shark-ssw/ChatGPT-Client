from pathlib import Path
import re

ROOT = Path('docs/project')


def read(name):
    path = ROOT / name
    return path, path.read_text()


def write(path, text):
    path.write_text(text)


def replace_between(text, start, end, replacement, label):
    i = text.find(start)
    if i < 0:
        raise SystemExit(f'missing start: {label}')
    j = text.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f'missing end: {label}')
    return text[:i] + replacement.rstrip() + '\n\n' + text[j:]


def replace_line_prefix(text, prefix, new_line, label):
    lines = text.splitlines()
    hits = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(hits) != 1:
        raise SystemExit(f'{label}: expected one line, got {len(hits)}')
    lines[hits[0]] = new_line
    return '\n'.join(lines) + ('\n' if text.endswith('\n') else '')

# PROJECT_PROFILE
path, text = read('PROJECT_PROFILE.md')
text = re.sub(r'\*\*Initialized — 2026-08-25; refreshed .*?\*\*', '**Initialized — 2026-08-25; refreshed 2026-09-01 through accepted b67 production transport Runtime, positive b72 tested cross-conversation simultaneous-generation Runtime, exact b73 Runtime defect evidence, and exact b74 Code/scope/Simulator/Push+PR CI/Artifact/package verification.**', text, count=1)
text = replace_line_prefix(text, '- Native application shell / production covered-Send orchestration:', '- Native application shell / production covered-Send/continuation orchestration: `AppDelegate.swift`, `RootViewController.swift`.', 'profile shell owner')
text = replace_line_prefix(text, '- Production native conversation/list/read/recovery/**response lifecycle** authority:', '- Production native conversation/list/read/recovery/**response lifecycle** authority: one `ConversationRepository` in `Conversation/ConversationFeature.swift`; optimistic local-Send state and external page-resume adoption both feed the same per-conversation Repository response runtime. b74 adds only derived resident-geometry reuse and no second message/response authority.', 'profile repository owner')
text = replace_line_prefix(text, '- Covered official Web executor:', '- Covered official Web executor: `CoveredWebSendExecutor`; browser challenge/protected-Send plus page-owned matching continuation observation only, never conversation/message/response authority. b74 may clone/parse the official page\'s own matching `/backend-api/f/conversation/resume` SSE but never constructs that request or offset.', 'profile executor')
new = '''## Exact b74 current Candidate

Build74 is the exact Runtime candidate produced from concrete b73 real-device defects plus the current Web Rule Lab cross-device continuation evidence.

Identity: Candidate `DEV-send-stream-0.1.0-b74`, `0.1.0 (74)`, exact product/config source `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`; final clean-reassembly `33420128454 / 99580192017` success; Push `33420408779 / 99581104920`; PR `33420412792 / 99581117817`; canonical Artifact `9768668727`; ZIP `sha256:6ac4cc97954a0a26ed258a9775921cc4d12b17a1ff29c5e8d65cddf3c5595cb3`; IPA `sha256:07c999fd0e9aaa5685725e6a97f066221f1f986cc3e23a99693a91accda285da`; independently unpacked package source marker `50dd61b8b31c`, Release, iOS14 minimum, arm64, iPhone/iPad family. Evidence: Code/scope/Simulator/Push+PR CI/Artifact/package verified; **Runtime pending**; Stable-Frozen No.

b74 preserves b38 deterministic geometry semantics while reusing already-derived historical geometry only for unchanged resident presentation identity, increases main tool-row vertical rhythm, and adds external active-response adoption by observing only the official page's own matching `/backend-api/f/conversation/resume` SSE. Native does not create the resume request, offset, stream-status polling or a second response store.'''
text = replace_between(text, '## Exact b73 current Candidate', '## Current product interaction target', new, 'profile candidate')
new = '''## Current next Candidate boundary

Build74 is the current exact real-device Runtime candidate. b39-b74 are permanently reserved. Do not allocate b75 unless exact b74 Runtime supplies a concrete defect or new evidence-backed requirement. The Runtime gate must verify long resident re-entry performance, larger tool-row rhythm, external active-response adoption through page-owned matching `/resume`, local protected-Send regression, b72 simultaneous-generation ownership, hidden-thought exclusion and b38 quick-navigation/geometry semantics.'''
text = replace_between(text, '## Current next Candidate boundary', '## Remaining Unknown / Unverified', new, 'profile next boundary')
text = replace_line_prefix(text, 'Exact b73 presentation Runtime,', 'Exact b74 Runtime for resident-geometry reuse, external active-response adoption and tool spacing; new-chat authoritative identity timing, server Stop mechanism, broader cross-conversation/service concurrency beyond the exact b72 A/B test, connector detail beyond the evidenced GitHub mapping, Native-constructed first/exclusive resume, 5/15-minute background execution, WebContent termination, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.', 'profile unknown')
write(path, text)

# PROJECT_STATE
path, text = read('PROJECT_STATE.md')
text = re.sub(r'_Last updated:.*?_', '_Last updated: 2026-09-01 through accepted b67 production transport Runtime, positive b72 tested cross-conversation simultaneous-generation Runtime, exact b73 real-device defect evidence, and exact b74 Code/scope/Simulator/Push+PR CI/Artifact/package verification. Phase 9 `DEV-send-stream` remains Active at the b74 human Runtime gate. Stable/Frozen Send remains No._', text, count=1)
current = '''Latest exact product Candidate is **`DEV-send-stream-0.1.0-b74` / `0.1.0 (74)`**:

- exact product/config source `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`;
- final clean-reassembly `33420128454 / 99580192017` passed exact four-file replay/content equality, scope/invariant audit, `git diff --check` and Xcode 16.4 iOS Simulator compile;
- Push `33420408779 / 99581104920` and PR `33420412792 / 99581117817` — success on exact source;
- canonical Push Artifact `9768668727`; ZIP `sha256:6ac4cc97954a0a26ed258a9775921cc4d12b17a1ff29c5e8d65cddf3c5595cb3`;
- IPA `sha256:07c999fd0e9aaa5685725e6a97f066221f1f986cc3e23a99693a91accda285da`;
- independently unpacked package `0.1.0 (74)` / Candidate b74 / source `50dd61b8b31c` / Release / minimum iOS14 / arm64 / iPhone+iPad family.

b73 real-device evidence localized long resident re-entry delay to repeated historical geometry rebuild, retained the need for more main tool-row spacing, and exposed the missing external active-response lifecycle. A current Web Rule Lab capture proved official Web uses page-owned matching `POST /backend-api/f/conversation/resume` `{conversation_id, offset}` -> HTTP200 SSE after `stream_status` when entering an externally active conversation. b74 observes only that page-owned matching resume stream, never constructs the request/offset or polls, and feeds it into the existing Repository response runtime. b74 also reuses derived b38 geometry only for unchanged resident presentation identity and increases main tool rhythm. Evidence ladder: **Code / exact scope / Simulator compile / Push+PR CI / Artifact / package verified / Runtime pending / Stable-Frozen No.** b39-b74 are permanently reserved.'''
start = text.find('Latest exact product Candidate is **')
end = text.find('## b65 accepted probe predecessor', start)
if start < 0 or end < 0:
    raise SystemExit('state current candidate block missing')
text = text[:start] + current + '\n\n' + text[end:]
text = replace_between(text, '## Current exact Runtime gate', '## Remaining Unknown / Unverified', '''## Current exact Runtime gate

Install exact b74 Artifact `9768668727` / IPA SHA `07c999fd...285da` on the primary iPhone/iOS17 device. Confirm Candidate/source marker, then verify: repeated re-entry into the previously slow long resident materially removes the ~1.4s geometry rebuild stall without breaking geometry/quick navigation; meaningful main tool rows have larger vertical rhythm; an externally initiated still-active response is adopted when entering the conversation via the official page-owned matching `/resume` SSE without duplicate Send or synthetic user bubble; terminal history reconciles once; one normal local Native Send still follows the b67 protected-Send HTTP200 SSE route; b72 A/B simultaneous-generation ownership remains correct; hidden thoughts stay absent. Export diagnostics for the Runtime run.''', 'state runtime')
# Replace final unknown paragraph if present.
text = re.sub(r'Exact b73 presentation Runtime, new-chat authoritative identity timing,.*?CI/Artifact success is never Runtime proof\.', 'Exact b74 resident-geometry/tool-spacing/external-adoption Runtime, new-chat authoritative identity timing, exact server Stop mechanism, broader cross-conversation/service concurrency beyond the exact b72 A/B test, connector-detail schemas beyond the evidenced GitHub mapping, Native-constructed first/exclusive resume, 5/15-minute background behavior, WebContent termination recovery, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.', text, count=1, flags=re.S)
write(path, text)

# MODULE_STATUS
path, text = read('MODULE_STATUS.md')
updates = {
'| Build/runtime metadata |': '| Build/runtime metadata | **b74 exact identity; Runtime pending** | Xcode settings / built `Info.plist` | `0.1.0 (74)`, exact source `50dd61b8...`, Artifact `9768668727`; b39-b74 reserved. |',
'| IPA build / CI packaging |': '| IPA build / CI packaging | **Stable capability; b74 Artifact valid** | `scripts/build_ipa.sh`, workflow | Push `33420408779/99581104920`, PR `33420412792/99581117817`, Artifact `9768668727`, ZIP `6ac4cc97...95cb3`, IPA `07c999fd...285da`; package independently verified as b74/source `50dd61b8b31c`/Release/iOS14/arm64. |',
'| Official same-response resume |': '| Official same-response resume | **Runtime Confirmed official-page continuation; b74 external adoption candidate** | official Web `/backend-api/f/conversation/resume` | b45/b47 proved no-resend continuation; 2026-09-01 Web Rule Lab additionally proves page-owned matching `{conversation_id, offset}` -> HTTP200 SSE on cross-device active-conversation entry. Native construction remains Unverified/rejected for current product path. |',
'| Covered official-Web protected Send executor |': '| Covered official-Web protected Send executor | **b67 local Send Runtime accepted; b74 page-owned resume observation packaged** | `CoveredWebSendExecutor` + TD-029 + `WEB_SEND_ADAPTER.md` | b67 passed protected Send -> HTTP200 SSE -> terminal/reconcile. b74 retains that path and adds observation of only the official page\'s matching `/resume` SSE for external active-response adoption; Runtime pending. |',
'| Native conversation read/recovery |': '| Native conversation read/recovery | **Stable merged baseline + b74 response/adoption candidate** | `ConversationRepository` | Sole production conversation/list/detail/recovery/response lifecycle authority. b74 external continuation creates one response generation in the existing Repository runtime; no second response store. |',
'| Native message geometry / round navigation |': '| Native message geometry / round navigation | **Stable merged b38 semantics; b74 reuse optimization Runtime pending** | presentation projection + message cell | b38 deterministic bounded geometry/quick navigation remain authoritative. b74 caches only derived presentation geometry for unchanged resident identity to avoid repeated full rebuild; no message-body cache. |',
'| Streaming / Send |': '| Streaming / Send | **Active — b67 transport accepted; b72 A/B positive; b74 exact Runtime candidate** | `DEV-send-stream`; PR #29; TD-029 | b74 exact source/Push+PR CI/Artifact/package verified; external page-owned resume adoption + geometry reuse/tool spacing Runtime pending. |',
'| User-visible reasoning |': '| User-visible reasoning | **Production local stream passed b67; b74 external-adoption Runtime pending** | `ConversationRepository` + `DEV-send-stream` | Ordered reasoning/tool segments retained; external matching resume feeds the same Repository timeline; hidden thoughts prohibited. |',
'| Tool activity presentation |': '| Tool activity presentation | **b74 Code/CI/Artifact/package verified; Runtime pending** | `DEV-send-stream` | b73 semantic filtering retained; b74 increases main meaningful tool-row vertical rhythm only. Ordered tools-only/input-only sheet remains. |',
}
for prefix, line in updates.items():
    text = replace_line_prefix(text, prefix, line, prefix)
text = replace_between(text, '## Current acceptance boundary', '## Auto-refresh rule', '''## Current acceptance boundary

- Stable merged native baseline remains b38.
- b67 production existing-conversation transport Runtime is accepted.
- Exact b72 Runtime positively supports the tested A-generating + B-send/generate simultaneous-generation path.
- Exact b73 Runtime is the evidence predecessor that exposed long resident geometry rebuild cost, insufficient tool rhythm and the external-active-response lifecycle gap.
- Exact b74 source `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`, Push/PR CI, canonical Artifact `9768668727`, ZIP `6ac4cc97...95cb3` and IPA `07c999fd...285da` are verified; package identity independently unpacked.
- b74 observes only the official page-owned matching `/backend-api/f/conversation/resume` SSE for external adoption; it does not construct resume/offset/polling and does not change `ConversationRepository` authority.
- b39-b74 are reserved. Phase 9 Stable/Frozen: No. Runtime remains pending.''', 'module acceptance')
write(path, text)

# TECHNICAL_DECISIONS
path, text = read('TECHNICAL_DECISIONS.md')
# TD-014 status only inside section
start = text.find('### TD-014 —')
end = text.find('\n### ', start + 1)
if start < 0:
    raise SystemExit('TD-014 missing')
if end < 0:
    end = len(text)
section = text[start:end]
section = re.sub(r'- \*\*Status\*\*:.*', '- **Status**: Confirmed requirement; local production transport Runtime accepted b67; tested A/B simultaneous generation positive b72; exact b74 package verified with external-adoption/tool-rhythm/geometry-reuse Runtime pending', section, count=1)
text = text[:start] + section + text[end:]
# TD-029 append durable extension
start = text.find('### TD-029 —')
if start < 0:
    raise SystemExit('TD-029 missing')
end = text.find('\n### ', start + 1)
if end < 0:
    end = len(text)
section = text[start:end]
section = re.sub(r'- \*\*Status\*\*:.*', '- **Status**: Confirmed product architecture decision; existing-conversation local protected-Send transport Runtime accepted b67; external page-owned matching-resume adoption exact b74 Code/CI/Artifact/package verified, Runtime pending', section, count=1)
if '**b74 external continuation extension**' not in section:
    section = section.rstrip() + '''\n- **b74 external continuation extension**: 2026-09-01 Web Rule Lab Runtime evidence shows that when another platform already owns an active response and official Web enters that conversation, official Web may request `stream_status` and then issue its own `POST /backend-api/f/conversation/resume` with `{conversation_id, offset}` receiving HTTP200 SSE. Production Native may observe/clone/parse only that page-owned resume when its `conversation_id` exactly matches the executor target, then create/adopt one response generation in the existing `ConversationRepository` runtime. Native must not construct the resume request, select/derive `offset`, poll `stream_status`, replay browser headers, treat the user WebSocket as response-body authority, or issue a second Send. Exact b74 package implements this boundary; real-device adoption behavior remains pending.\n'''
text = text[:start] + section + text[end:]
write(path, text)

# BUILD_TEST_INDEX
path, text = read('BUILD_TEST_INDEX.md')
if 'DEV-send-stream-0.1.0-b74' not in text:
    lines = text.splitlines()
    indexes = [i for i, line in enumerate(lines) if line.startswith('| `DEV-send-stream-0.1.0-b73`')]
    if len(indexes) != 1:
        raise SystemExit(f'build index b73 row count {len(indexes)}')
    row = '| `DEV-send-stream-0.1.0-b74` | `DEV-send-stream` | `0.1.0 (74)` | exact source `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`; PR #29 open | clean reassembly `33420128454/99580192017`; Push `33420408779/99581104920`; PR `33420412792/99581117817`; Artifact `9768668727`; ZIP `sha256:6ac4cc97954a0a26ed258a9775921cc4d12b17a1ff29c5e8d65cddf3c5595cb3`; IPA `sha256:07c999fd0e9aaa5685725e6a97f066221f1f986cc3e23a99693a91accda285da`; package independently verified source `50dd61b8b31c`/Release/iOS14/arm64 | Runtime pending: resident geometry reuse, larger tool rhythm, external page-owned resume adoption + local/A-B regressions | **Exact Runtime candidate / package verified; permanently reserved** |'
    lines.insert(indexes[0] + 1, row)
    text = '\n'.join(lines) + ('\n' if text.endswith('\n') else '')
write(path, text)

# PROJECT_SPECIFIC_RULES
path, text = read('PROJECT_SPECIFIC_RULES.md')
needle = '- Current tested protected route is official page-owned `POST /backend-api/f/conversation` -> HTTP200 `text/event-stream`.'
if needle not in text:
    raise SystemExit('specific protected route missing')
extra = needle + '\n- Current cross-device continuation evidence additionally authorizes **observation only** of the official page\'s own matching `POST /backend-api/f/conversation/resume` `{conversation_id, offset}` -> HTTP200 SSE. Native must not construct resume/offset, poll `stream_status`, replay browser headers, use the user WebSocket as response-body authority, or issue a second Send.'
text = text.replace(needle, extra, 1)
if '## External active-response adoption' not in text:
    marker = '## New-chat identity handoff'
    i = text.find(marker)
    if i < 0:
        raise SystemExit('new chat marker missing')
    section = '''## External active-response adoption

- Entering a conversation may expose an active response started by another platform only when the covered official page itself issues a `/backend-api/f/conversation/resume` whose request `conversation_id` exactly matches the executor's authoritative target.
- The page remains continuation-transport authority; Native observes a cloned SSE response and feeds accepted events into one existing `ConversationRepository` response generation.
- External adoption does not invent an optimistic prompt/user bubble; authoritative user history remains Repository Detail data.
- Native never chooses/derives offset, constructs the resume request, polls `stream_status`, replays browser/session headers, resends the prompt, or treats WebSocket frames as message-body authority without separate evidence.
- b74 is the first packaged production candidate for this boundary; Runtime remains pending.

'''
    text = text[:i] + section + text[i:]
text = text.replace('- b24-b73 emitted identities are permanently reserved;', '- b24-b74 emitted identities are permanently reserved;', 1)
if '- exact b74 package authority is' not in text:
    marker = '- exact b73 package authority is `0.1.0 (73)`, source `4edda892a04a1a07f4a07e74b135b969ea82193e`, Artifact `9764247402`, IPA `8285ba9d5f63207feb2eaf722ec722a886f3ee88956236a89a716ad58b884113`; Runtime presentation pending;'
    if marker not in text:
        raise SystemExit('b73 package rule missing')
    text = text.replace(marker, marker + '\n- exact b74 package authority is `0.1.0 (74)`, source `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`, Artifact `9768668727`, ZIP `6ac4cc97954a0a26ed258a9775921cc4d12b17a1ff29c5e8d65cddf3c5595cb3`, IPA `07c999fd0e9aaa5685725e6a97f066221f1f986cc3e23a99693a91accda285da`; Code/CI/Artifact/package verified, Runtime pending;', 1)
text = text.replace('- do not allocate b74 before exact b73 Runtime supplies a concrete need.', '- do not allocate b75 unless exact b74 Runtime supplies a concrete defect or new evidence-backed requirement.', 1)
write(path, text)

# WEB_SEND_ADAPTER: refresh authority date + current integration boundary.
path, text = read('WEB_SEND_ADAPTER.md')
text = re.sub(r'_Last established:.*?_', '_Last established: 2026-09-01 through DEV-send-stream b67 accepted local transport, b72 tested concurrent ownership, and current cross-device page-owned `/resume` evidence used by exact b74._', text, count=1)
start = text.find('## Current next integration boundary')
if start < 0:
    raise SystemExit('web adapter next boundary missing')
text = text[:start] + '''## Current next integration boundary

Exact b74 is the first packaged product candidate for cross-device active-response adoption under this rule. Its human Runtime gate must prove:

1. another platform starts a still-active response in an existing conversation;
2. entering that conversation in b74 lets official Web perform its own continuation behavior;
3. only a matching page-owned `/backend-api/f/conversation/resume` is adopted;
4. `ConversationRepository` owns one Native live-response generation and chronological reasoning/tool/final state;
5. no duplicate Send, Native resume request, offset synthesis, stream-status polling, synthetic user bubble or WebSocket-body assumption occurs;
6. terminal authoritative history reconciles once;
7. the b67 local Send path and b72 tested A/B simultaneous-generation path remain intact;
8. diagnostics remain privacy-safe.

CI/Artifact/package verification does not prove this Runtime gate. Any code correction after the emitted b74 Artifact requires a new Candidate identity.'''
write(path, text)
