from pathlib import Path

SOURCE = Path('scripts/research/official_ios_realtime_probe/ChatGPTRealtimeProbe.m')
README = Path('scripts/research/official_ios_realtime_probe/README.md')
CHECKPOINT = Path('docs/project/current/dev/DEV-send-stream.md')


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected exactly 1 match, got {count}')
    return text.replace(old, new, 1)

s = SOURCE.read_text()
s = replace_once(s, 'static NSString * const RPTProbeVersion = @"0.4";', 'static NSString * const RPTProbeVersion = @"0.5";', 'version')
s = replace_once(s, '''static char RPTWebSocketReceiveErrorLoggedKey;
static char RPTTaskResumeLoggedKey;
''', '''static char RPTWebSocketReceiveErrorLoggedKey;
static char RPTTaskResumeLoggedKey;
static char RPTDetailAsyncStatusLoggedKey;
static char RPTDetailScanTailKey;
static BOOL RPTLateSessionRefreshDone = NO;
''', 'globals')

anchor = '''static void RPTDelegateDidReceiveResponse(id self, SEL _cmd, NSURLSession *session, NSURLSessionDataTask *dataTask, NSURLResponse *response, void (^completionHandler)(NSURLSessionResponseDisposition)) {
'''
insert = r'''static NSString *RPTConversationAsyncStatusToken(NSData *data, NSRange keyRange) {
    if (!data.length || keyRange.location == NSNotFound || keyRange.location >= data.length) return @"";
    NSUInteger length = MIN((NSUInteger)256, data.length - keyRange.location);
    NSString *window = [[NSString alloc] initWithData:[data subdataWithRange:NSMakeRange(keyRange.location, length)] encoding:NSUTF8StringEncoding];
    if (!window.length) return @"";
    NSRange colon = [window rangeOfString:@":"];
    if (colon.location == NSNotFound) return @"";
    NSUInteger index = NSMaxRange(colon);
    while (index < window.length && [[NSCharacterSet whitespaceAndNewlineCharacterSet] characterIsMember:[window characterAtIndex:index]]) index += 1;
    if (index >= window.length) return @"";
    if ([window characterAtIndex:index] == '"') {
        NSUInteger start = index + 1;
        NSRange end = [window rangeOfString:@"\"" options:0 range:NSMakeRange(start, window.length - start)];
        if (end.location == NSNotFound) return @"";
        return RPTSafeToken([window substringWithRange:NSMakeRange(start, end.location - start)]);
    }
    NSString *tail = [[window substringFromIndex:index] lowercaseString];
    if ([tail hasPrefix:@"null"]) return @"null";
    return @"";
}

static void RPTObserveConversationDetailData(NSURLSessionDataTask *task, NSData *data) {
    if (!task || !data.length || objc_getAssociatedObject(task, &RPTDetailAsyncStatusLoggedKey)) return;
    NSURLRequest *request = task.currentRequest ?: task.originalRequest;
    if (![[RPTPathKind(request.URL.path ?: @"") lowercaseString] isEqualToString:@"conversation_detail"]) return;
    NSData *key = [@"\"conversation_async_status\"" dataUsingEncoding:NSUTF8StringEncoding];
    NSRange keyRange = [data rangeOfData:key options:0 range:NSMakeRange(0, data.length)];
    NSData *scan = data;
    if (keyRange.location == NSNotFound) {
        NSData *tail = objc_getAssociatedObject(task, &RPTDetailScanTailKey);
        if (tail.length) {
            NSUInteger prefixLength = MIN((NSUInteger)256, data.length);
            NSMutableData *boundary = [tail mutableCopy];
            [boundary appendData:[data subdataWithRange:NSMakeRange(0, prefixLength)]];
            NSRange boundaryRange = [boundary rangeOfData:key options:0 range:NSMakeRange(0, boundary.length)];
            if (boundaryRange.location != NSNotFound) { scan = boundary; keyRange = boundaryRange; }
        }
    }
    if (keyRange.location != NSNotFound) {
        NSString *status = RPTConversationAsyncStatusToken(scan, keyRange);
        if (status.length) {
            objc_setAssociatedObject(task, &RPTDetailAsyncStatusLoggedKey, @YES, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
            NSMutableDictionary *fields = RPTRequestFields(request);
            fields[@"asyncStatus"] = status;
            fields[@"taskClass"] = NSStringFromClass(object_getClass(task)) ?: @"";
            RPTWriteEvent(@"http.conversation_detail.async_status", fields);
        }
    }
    NSUInteger tailLength = MIN((NSUInteger)128, data.length);
    if (tailLength) objc_setAssociatedObject(task, &RPTDetailScanTailKey, [data subdataWithRange:NSMakeRange(data.length - tailLength, tailLength)], OBJC_ASSOCIATION_RETAIN_NONATOMIC);
}

static void RPTDelegateDidReceiveData(id self, SEL _cmd, NSURLSession *session, NSURLSessionDataTask *dataTask, NSData *data) {
    IMP original = RPTOriginalIMP(self, _cmd);
    if (!original) return;
    void (*function)(id, SEL, NSURLSession *, NSURLSessionDataTask *, NSData *) = (void *)original;
    function(self, _cmd, session, dataTask, data);
    RPTObserveConversationDetailData(dataTask, data);
}

'''
s = replace_once(s, anchor, insert + anchor, 'data observer insertion')

s = replace_once(s, '''static void RPTTaskResume(id self, SEL _cmd) {
    NSURLSessionTask *task = (NSURLSessionTask *)self;
    NSURLRequest *request = task.currentRequest ?: task.originalRequest;
''', '''static void RPTInstallSessionHooks(void);

static void RPTTaskResume(id self, SEL _cmd) {
    NSURLSessionTask *task = (NSURLSessionTask *)self;
    NSURLRequest *request = task.currentRequest ?: task.originalRequest;
    BOOL refreshLateHooks = NO;
    if ([[RPTPathKind(request.URL.path ?: @"") lowercaseString] isEqualToString:@"conversation_detail"]) {
        @synchronized (RPTHookedKeys) {
            if (!RPTLateSessionRefreshDone) { RPTLateSessionRefreshDone = YES; refreshLateHooks = YES; }
        }
    }
    if (refreshLateHooks) {
        RPTInstallSessionHooks();
        RPTWriteEvent(@"probe.late_hooks_refreshed", @{ @"hookCount": @(RPTHookedKeys.count) });
    }
''', 'late hook refresh')

s = replace_once(s, '''    SEL responseSelector = NSSelectorFromString(@"URLSession:dataTask:didReceiveResponse:completionHandler:");
    SEL completeSelector = NSSelectorFromString(@"URLSession:task:didCompleteWithError:");
''', '''    SEL dataSelector = NSSelectorFromString(@"URLSession:dataTask:didReceiveData:");
    SEL responseSelector = NSSelectorFromString(@"URLSession:dataTask:didReceiveResponse:completionHandler:");
    SEL completeSelector = NSSelectorFromString(@"URLSession:task:didCompleteWithError:");
''', 'selector declaration')
s = replace_once(s, '''        if (RPTClassOwnsSelector(cls, responseSelector)) RPTInstallHookOnClass(cls, responseSelector, (IMP)RPTDelegateDidReceiveResponse);
        if (RPTClassOwnsSelector(cls, completeSelector)) RPTInstallHookOnClass(cls, completeSelector, (IMP)RPTDelegateDidComplete);
''', '''        if (RPTClassOwnsSelector(cls, dataSelector)) RPTInstallHookOnClass(cls, dataSelector, (IMP)RPTDelegateDidReceiveData);
        if (RPTClassOwnsSelector(cls, responseSelector)) RPTInstallHookOnClass(cls, responseSelector, (IMP)RPTDelegateDidReceiveResponse);
        if (RPTClassOwnsSelector(cls, completeSelector)) RPTInstallHookOnClass(cls, completeSelector, (IMP)RPTDelegateDidComplete);
''', 'data selector hook')
SOURCE.write_text(s)

r = README.read_text()
r = replace_once(r, 'Current research revision: **Probe v0.4**.', 'Current research revision: **Probe v0.5**.', 'readme version')
r = replace_once(r, '- one privacy-safe `http.task.resume` event is emitted per observed NSURLSession task, including tasks created internally by Swift async `URLSession.data(for:)` / `bytes(for:)` paths; no task body or auth material is logged.\n', '- one privacy-safe `http.task.resume` event is emitted per observed NSURLSession task, including tasks created internally by Swift async `URLSession.data(for:)` / `bytes(for:)` paths; no task body or auth material is logged.\n- for authoritative Conversation Detail responses only, v0.5 observes `URLSession:dataTask:didReceiveData:` and emits only the safe enum value of the exact `conversation_async_status` field (for example `is_streaming` / `complete`); response content is never persisted or logged. A one-time late delegate-hook refresh occurs on the first Detail task so Swift-async delegate classes loaded after probe injection are covered.\n', 'readme observed status')
r = replace_once(r, 'The decisive question is which target-correlated acquisition event appears first before assistant completion: conversation HTTP/stream-status/resume/SSE, a conversation/per-turn WebSocket subscription/update, or another official route. Probe v0.4 keeps the v0.3 WebSocket error de-duplication and adds task-resume observation so Swift async URLSession acquisition cannot bypass the probe merely by avoiding public data-task constructors.\n', 'The decisive v0.5 question is whether the same target Conversation Detail loop emits `conversation_async_status=is_streaming` while the remote answer is active and later `complete` when official polling stops. v0.5 keeps v0.4 task-resume observation and adds only privacy-safe status-field observation; it does not initiate requests or copy response content.\n', 'readme decisive test')
README.write_text(r)

c = CHECKPOINT.read_text()
section = '''## Official iOS Probe v0.5 async-status response gate — 2026-09-04\n\nExact resume guard before this research delta: branch `dev/send-stream-20260829` at `1074cabfb6afa31e0db37896bf606f25f2f7d685`; PR #29 open/unmerged; `main` `94f0c5777dad262cd1fb22be49082dbd92c962f2`; exact product remains b95 (`ac5e621aa69f5f27ef3167b4a951812be8b8e2c2` / package `a10320e589acd551a8dc53f56aaf28a0a08f5b4a`); b96 remains unallocated.\n\nProbe v0.4 Human Runtime already observed the current-account target `GET /backend-api/conversation/<id>` loop at ~9.7s median while the ordinary user WebSocket failed. User separately recalls official iOS cross-platform continuation as batched/block refresh rather than SSE-like token flow; this is qualitative support only, not exact timestamp correlation. Exact official static evidence identifies `conversation_async_status`, `KnownConversationAsyncStatus`, `IS_STREAMING` / `COMPLETE`, `ConversationPollingManager`, and the stop-when-no-longer-streaming contract.\n\nProbe v0.5 is research-only and changes no ChatGPTClient product file. It retains v0.4 task-resume observation, hooks `URLSession:dataTask:didReceiveData:`, scans only the exact `conversation_async_status` field in authoritative Conversation Detail response chunks, and logs only its safe enum token plus existing privacy-safe request identity. It keeps only a 128-byte rolling boundary tail in memory to detect a field split across chunks and never persists/logs response content. On the first target Detail task it refreshes delegate hooks once so Swift-async delegate classes loaded after probe injection are included. No extra request, polling, timer, retry, resume, response store, or content authority is introduced.\n\nEvidence ladder after this source commit: **v0.5 research code written; dedicated research CI/Artifact/package pending; Human Runtime pending; product b95 unchanged; b96 unallocated; Stable/Frozen Send No.**\n\n**Next exact action:** run the existing dedicated research Probe CI for exact v0.5 source, package the verified dylib into the exact official source ZIP, independently verify IPA identity/diff/hash, then Human Runtime one long cross-platform response after `清空`. The decisive log is target-correlated `http.conversation_detail.async_status` transitioning from `is_streaming` to `complete` (or another explicitly observed safe enum). Do not allocate b96 before that result.\n\n'''
if section.splitlines()[0] in c:
    raise SystemExit('checkpoint section already exists')
if not c.startswith('# DEV-send-stream\n\n'):
    raise SystemExit('checkpoint header mismatch')
c = c.replace('# DEV-send-stream\n\n', '# DEV-send-stream\n\n' + section, 1)
CHECKPOINT.write_text(c)
