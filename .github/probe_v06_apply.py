from pathlib import Path

SOURCE = Path('scripts/research/official_ios_realtime_probe/ChatGPTRealtimeProbe.m')
README = Path('scripts/research/official_ios_realtime_probe/README.md')
CHECKPOINT = Path('docs/project/current/dev/DEV-send-stream.md')
PROJECT_STATE = Path('docs/project/PROJECT_STATE.md')
EVIDENCE = Path('docs/project/runtime-evidence/DEV-send-stream-official-ios-probe-v05-runtime-v06-callback-surface-20260904.md')


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected exactly 1 match, got {count}')
    return text.replace(old, new, 1)


s = SOURCE.read_text()
s = replace_once(s, 'static NSString * const RPTProbeVersion = @"0.5";', 'static NSString * const RPTProbeVersion = @"0.6";', 'version')
s = replace_once(s, 'static BOOL RPTLateSessionRefreshDone = NO;\n', 'static BOOL RPTLateSessionRefreshDone = NO;\nstatic BOOL RPTDetailCallbackSurfaceLogged = NO;\n', 'callback surface global')

anchor = '''static void RPTInstallSessionHooks(void);\n\nstatic void RPTTaskResume(id self, SEL _cmd) {\n'''
insert = r'''static BOOL RPTCallbackSelectorRelevant(NSString *selectorName) {
    NSString *lower = selectorName.lowercaseString ?: @"";
    for (NSString *term in @[@"data", @"response", @"receive", @"complete", @"completion", @"finish", @"body", @"bytes"]) {
        if ([lower containsString:term]) return YES;
    }
    return NO;
}

static BOOL RPTCallbackIvarRelevant(NSString *ivarName) {
    NSString *lower = ivarName.lowercaseString ?: @"";
    for (NSString *term in @[@"session", @"delegate", @"handler", @"data", @"response", @"protocol", @"connection", @"completion", @"body"]) {
        if ([lower containsString:term]) return YES;
    }
    return NO;
}

static NSArray<NSDictionary *> *RPTDetailTaskMethodSurface(Class startClass) {
    NSMutableArray<NSDictionary *> *items = [NSMutableArray array];
    NSUInteger depth = 0;
    for (Class cls = startClass; cls && depth < 8 && items.count < 80; cls = class_getSuperclass(cls), depth += 1) {
        unsigned int count = 0;
        Method *methods = class_copyMethodList(cls, &count);
        for (unsigned int i = 0; i < count && items.count < 80; i++) {
            SEL selector = method_getName(methods[i]);
            NSString *name = NSStringFromSelector(selector) ?: @"";
            if (!RPTCallbackSelectorRelevant(name)) continue;
            const char *types = method_getTypeEncoding(methods[i]);
            [items addObject:@{
                @"class": NSStringFromClass(cls) ?: @"",
                @"selector": name,
                @"argumentCount": @(method_getNumberOfArguments(methods[i])),
                @"typeEncoding": types ? [NSString stringWithUTF8String:types] ?: @"" : @""
            }];
        }
        free(methods);
    }
    return items;
}

static NSArray<NSDictionary *> *RPTDetailTaskIvarSurface(Class startClass) {
    NSMutableArray<NSDictionary *> *items = [NSMutableArray array];
    NSUInteger depth = 0;
    for (Class cls = startClass; cls && depth < 8 && items.count < 40; cls = class_getSuperclass(cls), depth += 1) {
        unsigned int count = 0;
        Ivar *ivars = class_copyIvarList(cls, &count);
        for (unsigned int i = 0; i < count && items.count < 40; i++) {
            const char *rawName = ivar_getName(ivars[i]);
            NSString *name = rawName ? [NSString stringWithUTF8String:rawName] ?: @"" : @"";
            if (!RPTCallbackIvarRelevant(name)) continue;
            const char *types = ivar_getTypeEncoding(ivars[i]);
            [items addObject:@{
                @"class": NSStringFromClass(cls) ?: @"",
                @"ivar": name,
                @"typeEncoding": types ? [NSString stringWithUTF8String:types] ?: @"" : @""
            }];
        }
        free(ivars);
    }
    return items;
}

static void RPTRecordDetailTaskCallbackSurface(NSURLSessionTask *task) {
    if (!task) return;
    @synchronized (RPTHookedKeys) {
        if (RPTDetailCallbackSurfaceLogged) return;
        RPTDetailCallbackSurfaceLogged = YES;
    }
    Class taskClass = object_getClass(task);
    NSMutableDictionary *fields = [NSMutableDictionary dictionary];
    fields[@"taskClass"] = NSStringFromClass(taskClass) ?: @"";
    fields[@"methods"] = RPTDetailTaskMethodSurface(taskClass);
    fields[@"ivars"] = RPTDetailTaskIvarSurface(taskClass);
    RPTWriteEvent(@"probe.detail_task_callback_surface", fields);
}

static void RPTInstallSessionHooks(void);

static void RPTTaskResume(id self, SEL _cmd) {
'''
s = replace_once(s, anchor, insert, 'callback surface insertion')
old = '''    BOOL refreshLateHooks = NO;\n    if ([[RPTPathKind(request.URL.path ?: @"") lowercaseString] isEqualToString:@"conversation_detail"]) {\n        @synchronized (RPTHookedKeys) {\n            if (!RPTLateSessionRefreshDone) { RPTLateSessionRefreshDone = YES; refreshLateHooks = YES; }\n        }\n    }\n'''
new = '''    BOOL refreshLateHooks = NO;\n    BOOL isConversationDetail = [[RPTPathKind(request.URL.path ?: @"") lowercaseString] isEqualToString:@"conversation_detail"];\n    if (isConversationDetail) {\n        RPTRecordDetailTaskCallbackSurface(task);\n        @synchronized (RPTHookedKeys) {\n            if (!RPTLateSessionRefreshDone) { RPTLateSessionRefreshDone = YES; refreshLateHooks = YES; }\n        }\n    }\n'''
s = replace_once(s, old, new, 'task resume callback discovery')
SOURCE.write_text(s)

r = README.read_text()
r = replace_once(r, 'Current research revision: **Probe v0.5**.', 'Current research revision: **Probe v0.6**.', 'readme version')
r = replace_once(r, '- for authoritative Conversation Detail responses only, v0.5 observes `URLSession:dataTask:didReceiveData:` and emits only the safe enum value of the exact `conversation_async_status` field (for example `is_streaming` / `complete`); response content is never persisted or logged. A one-time late delegate-hook refresh occurs on the first Detail task so Swift-async delegate classes loaded after probe injection are covered.\n', '- v0.5 response-data observation remains present, but v0.6 additionally records one privacy-safe callback-surface snapshot for the first authoritative Conversation Detail `NSURLSessionTask`: only relevant Objective-C class/selector names, argument counts, method type encodings, and relevant ivar names/type encodings. It does not read ivar values, install private callback hooks, or log response content.\n', 'readme callback surface')
r = replace_once(r, 'The decisive v0.5 question is whether the same target Conversation Detail loop emits `conversation_async_status=is_streaming` while the remote answer is active and later `complete` when official polling stops. v0.5 keeps v0.4 task-resume observation and adds only privacy-safe status-field observation; it does not initiate requests or copy response content.\n', 'Probe v0.5 Runtime reconfirmed Native Conversation Detail polling but emitted no `http.conversation_detail.async_status`, proving the public delegate-data hook did not cover the Swift-async Detail response path. The decisive v0.6 output is one `probe.detail_task_callback_surface` event identifying the actual `__NSCFLocalDataTask` callback surface structurally. Do not infer field absence from the v0.5 observer miss.\n', 'readme decisive test')
README.write_text(r)

checkpoint_section = '''## Official iOS Probe v0.5 Runtime / v0.6 callback-surface gate — 2026-09-04\n\nExact user-exported Probe v0.5 JSONL `sha256:26e8646945831764bf6317c99213ff8a9621d09942e642a19b4f15aa24c892ba` is clean Human Runtime evidence: 47,648 bytes / 146 valid events / zero parse errors / all `probeVersion=0.5`, beginning from a clean-log test window. Native task-level observation is Runtime Positive again.\n\nFor target conversation hash `0df178903e95`, exact `__NSCFLocalDataTask` GET Detail requests occur at `20:57:28.958`, `20:57:56.962`, `20:58:07.117`, `20:58:16.235`, `20:58:25.668`, `20:58:35.051`, `20:58:44.323`, and `20:58:53.546Z`. After the first reacquisition gap, the repeated intervals are approximately `10.155 / 9.118 / 9.433 / 9.383 / 9.272 / 9.223s` (median `9.328s`). This independently reconfirms official Native authoritative Conversation Detail polling on the current account.\n\nThere are **zero** `http.conversation_detail.async_status` events despite the target Detail tasks. This is not evidence that `conversation_async_status` is absent. Probe v0.5's public `URLSession:dataTask:didReceiveData:` observer is therefore **Runtime Negative as coverage for this Swift-async Detail response path**; the field/value and official active/terminal contract remain Unverified.\n\nProbe v0.6 is research-only and changes no ChatGPTClient product file. It keeps v0.5 observation but, on the first target Detail task only, records a bounded structural snapshot of the actual task class hierarchy: callback-relevant Objective-C selector names, argument counts/type encodings, plus callback/session/delegate-related ivar names/type encodings. It reads no ivar values, installs no guessed private callback hook, initiates no request, and logs no auth/content. The purpose is to identify one evidenced Swift-async response-delivery callback before any deeper observer.\n\nGovernance recovery: an unrelated/accidental commit `a4d7f7337a4047e2f9525cc0cef131cd17a0a14d` replaced this checkpoint with `NO`. The exact pre-overwrite checkpoint blob `06d5ab77bfc2038153af5393bc0fb4789b6bd7c8` was uniquely recovered at commit `500a17baad18a2cf3713fe9edad2bcf41502cfe4`; a temporary recovery placeholder created during that correction was removed in the same final recovery tree. No ChatGPTClient product or Probe source changed in that recovery.\n\nEvidence ladder: **Probe v0.5 package verified / Native Detail polling Runtime Positive again / v0.5 async-status callback coverage Runtime Negative / async-status semantics Unverified / v0.6 research source next / product remains b95 / b96 unallocated / Stable-Frozen Send No.**\n\n**Next exact action:** build/package exact Probe v0.6 and run one clean long cross-platform response after `清空`. Decisive v0.6 evidence is `probe.detail_task_callback_surface`; use only an evidenced callback signature from that output for any later response-state observer. Do not allocate b96 yet, and do not add Native polling/resume/timer/retry/watchdog/duplicate Send or a second response store from the callback-coverage miss.\n\n'''
c = CHECKPOINT.read_text()
if not c.startswith('# DEV-send-stream\n\n'):
    raise SystemExit('checkpoint header mismatch')
if checkpoint_section.splitlines()[0] in c:
    raise SystemExit('checkpoint section already exists')
c = c.replace('# DEV-send-stream\n\n', '# DEV-send-stream\n\n' + checkpoint_section, 1)
CHECKPOINT.write_text(c)

state_section = '''## 2026-09-04 — Probe v0.5 Runtime reconfirms Native Detail polling / v0.6 callback-surface gate\n\n- Exact v0.5 JSONL `sha256:26e8646945831764bf6317c99213ff8a9621d09942e642a19b4f15aa24c892ba`: 47,648 bytes / 146 events / zero parse errors / all v0.5. Target `0df178903e95` again issued repeated `__NSCFLocalDataTask` authoritative Conversation Detail GETs at about 9.3s median after reacquisition.\n- Zero `http.conversation_detail.async_status` events means the v0.5 public `URLSession:dataTask:didReceiveData:` hook did not cover the Swift-async Detail response path; it does **not** prove the field is absent. Native Detail polling remains Runtime Positive; exact async-status semantics remain Unverified.\n- Probe v0.6 is research-only and records one bounded callback-surface snapshot from the first target Detail task (relevant selector/ivar names and type signatures only). It installs no guessed private callback hook and reads no content/auth. Product remains b95; b96 remains unallocated.\n\n'''
p = PROJECT_STATE.read_text()
if not p.startswith('# Project State\n\n'):
    raise SystemExit('project state header mismatch')
if state_section.splitlines()[0] in p:
    raise SystemExit('project state section already exists')
p = p.replace('# Project State\n\n', '# Project State\n\n' + state_section, 1)
PROJECT_STATE.write_text(p)

evidence = '''# DEV-send-stream — Official iOS Probe v0.5 Runtime / v0.6 callback-surface gate — 2026-09-04\n\n## Input identity\n\n- User-exported JSONL: `ChatGPTRealtimeProbe(4).jsonl`\n- SHA-256: `26e8646945831764bf6317c99213ff8a9621d09942e642a19b4f15aa24c892ba`\n- Size: 47,648 bytes\n- Parsed events: 146\n- Parse errors: 0\n- Probe version: all `0.5`\n\n## Runtime result\n\nProbe v0.5 is clean and does not reproduce the v0.2 receive-error logging storm. Task-level observation is Runtime Positive. The target conversation hash `0df178903e95` issued authoritative `__NSCFLocalDataTask` GET Detail requests at `20:57:28.958`, `20:57:56.962`, `20:58:07.117`, `20:58:16.235`, `20:58:25.668`, `20:58:35.051`, `20:58:44.323`, and `20:58:53.546Z`. Excluding the first 28.004s reacquisition gap, intervals are `10.155 / 9.118 / 9.433 / 9.383 / 9.272 / 9.223s`, median approximately `9.328s`.\n\nThis independently reconfirms the v0.4 finding: the official iOS app performs Native authoritative Conversation Detail polling for the cross-platform target.\n\nThere are zero `http.conversation_detail.async_status` events. Because the same target Detail tasks are visible at `NSURLSessionTask.resume`, this absence is classified as an instrumentation-coverage failure of the v0.5 public `URLSession:dataTask:didReceiveData:` observer for the Swift-async Detail response path. It is **not** a protocol negative and does not prove `conversation_async_status` is absent.\n\n## v0.6 research gate\n\nProbe v0.6 changes research instrumentation only. On the first target Conversation Detail task, it records one bounded `probe.detail_task_callback_surface` event containing only callback-relevant Objective-C class/selector names, method argument counts/type encodings, and callback/session/delegate-related ivar names/type encodings from the task class hierarchy. It does not read ivar values, hook guessed private callbacks, issue requests, poll, retry, or capture response/auth/content.\n\nThe next decision must come from the actual Runtime selector surface. Only after one exact response-delivery callback is evidenced may a later research revision attach the existing exact `conversation_async_status` scanner to that callback.\n\n## Product boundary\n\nChatGPTClient product remains exact b95. b96 is unallocated. `ConversationRepository` remains sole Native response/content authority. Do not implement Native polling cadence, `/resume`, retry/watchdog/timers, duplicate Send, WebSocket-body authority, or a second store from this observer miss.\n'''
if EVIDENCE.exists():
    raise SystemExit('evidence file already exists')
EVIDENCE.write_text(evidence)
