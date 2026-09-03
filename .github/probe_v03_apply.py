from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, got {count}")
    return text.replace(old, new, 1)


probe_path = Path("scripts/research/official_ios_realtime_probe/ChatGPTRealtimeProbe.m")
probe = probe_path.read_text()

probe = replace_once(
    probe,
    'static NSString * const RPTProbeVersion = @"0.2";',
    'static NSString * const RPTProbeVersion = @"0.3";',
    "probe version",
)

probe = replace_once(
    probe,
    'static NSMutableDictionary<NSString *, NSValue *> *RPTOriginalIMPs;\n',
    'static NSMutableDictionary<NSString *, NSValue *> *RPTOriginalIMPs;\nstatic char RPTWebSocketReceiveErrorLoggedKey;\n',
    "websocket error association key",
)

old_receive = '''static void RPTWebSocketReceive(id self, SEL _cmd, void (^completionHandler)(NSURLSessionWebSocketMessage *, NSError *)) API_AVAILABLE(ios(13.0)) {
    RPTRecordTaskURL(self, @"ws.receive.arm");
    IMP original = RPTOriginalIMP(self, _cmd);
    if (!original) return;
    void (*function)(id, SEL, void (^)(NSURLSessionWebSocketMessage *, NSError *)) = (void *)original;
    function(self, _cmd, ^(NSURLSessionWebSocketMessage *message, NSError *error) {
        if (message) RPTWriteEvent(@"ws.inbound.frames", @{ @"frames": RPTMessageSummaries(message) });
        if (error) RPTWriteEvent(@"ws.receive.error", @{ @"domain": error.domain ?: @"", @"code": @(error.code) });
        if (completionHandler) completionHandler(message, error);
    });
}
'''
new_receive = '''static void RPTWebSocketReceive(id self, SEL _cmd, void (^completionHandler)(NSURLSessionWebSocketMessage *, NSError *)) API_AVAILABLE(ios(13.0)) {
    IMP original = RPTOriginalIMP(self, _cmd);
    if (!original) return;
    void (*function)(id, SEL, void (^)(NSURLSessionWebSocketMessage *, NSError *)) = (void *)original;
    function(self, _cmd, ^(NSURLSessionWebSocketMessage *message, NSError *error) {
        if (message) {
            objc_setAssociatedObject(self, &RPTWebSocketReceiveErrorLoggedKey, nil, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
            RPTWriteEvent(@"ws.inbound.frames", @{ @"frames": RPTMessageSummaries(message) });
        }
        if (error && !objc_getAssociatedObject(self, &RPTWebSocketReceiveErrorLoggedKey)) {
            objc_setAssociatedObject(self, &RPTWebSocketReceiveErrorLoggedKey, @YES, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
            RPTWriteEvent(@"ws.receive.error", @{ @"domain": error.domain ?: @"", @"code": @(error.code) });
        }
        if (completionHandler) completionHandler(message, error);
    });
}
'''
probe = replace_once(probe, old_receive, new_receive, "dedupe websocket receive errors")

marker = '''static void RPTDelegateDidReceiveResponse(id self, SEL _cmd, NSURLSession *session, NSURLSessionDataTask *dataTask, NSURLResponse *response, void (^completionHandler)(NSURLSessionResponseDisposition)) {
'''
url_functions = '''static NSURLSessionDataTask *RPTSessionDataURL(id self, SEL _cmd, NSURL *url) {
    IMP original = RPTOriginalIMP(self, _cmd);
    if (!original) return nil;
    NSURLSessionDataTask *(*function)(id, SEL, NSURL *) = (void *)original;
    NSURLSessionDataTask *task = function(self, _cmd, url);
    if (RPTShouldObserveURL(url)) {
        NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:url];
        request.HTTPMethod = @"GET";
        RPTWriteEvent(@"http.observed.request", RPTRequestFields(request));
    }
    return task;
}

static NSURLSessionDataTask *RPTSessionDataURLCompletion(id self, SEL _cmd, NSURL *url, void (^completionHandler)(NSData *, NSURLResponse *, NSError *)) {
    IMP original = RPTOriginalIMP(self, _cmd);
    if (!original) return nil;
    NSURLSessionDataTask *(*function)(id, SEL, NSURL *, void (^)(NSData *, NSURLResponse *, NSError *)) = (void *)original;
    NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:url];
    request.HTTPMethod = @"GET";
    BOOL candidate = RPTShouldObserveURL(url);
    if (candidate) RPTWriteEvent(@"http.observed.request", RPTRequestFields(request));
    return function(self, _cmd, url, ^(NSData *data, NSURLResponse *response, NSError *error) {
        if (candidate) RPTWriteEvent(@"http.observed.response", RPTResponseFields(request, response, data, error));
        if (completionHandler) completionHandler(data, response, error);
    });
}

'''
probe = replace_once(probe, marker, url_functions + marker, "URLSession URL-form wrappers")

old_hooks = '''            if (RPTClassOwnsSelector(cls, @selector(dataTaskWithRequest:))) RPTInstallHookOnClass(cls, @selector(dataTaskWithRequest:), (IMP)RPTSessionDataRequest);
            if (RPTClassOwnsSelector(cls, @selector(dataTaskWithRequest:completionHandler:))) RPTInstallHookOnClass(cls, @selector(dataTaskWithRequest:completionHandler:), (IMP)RPTSessionDataRequestCompletion);
'''
new_hooks = '''            if (RPTClassOwnsSelector(cls, @selector(dataTaskWithURL:))) RPTInstallHookOnClass(cls, @selector(dataTaskWithURL:), (IMP)RPTSessionDataURL);
            if (RPTClassOwnsSelector(cls, @selector(dataTaskWithURL:completionHandler:))) RPTInstallHookOnClass(cls, @selector(dataTaskWithURL:completionHandler:), (IMP)RPTSessionDataURLCompletion);
            if (RPTClassOwnsSelector(cls, @selector(dataTaskWithRequest:))) RPTInstallHookOnClass(cls, @selector(dataTaskWithRequest:), (IMP)RPTSessionDataRequest);
            if (RPTClassOwnsSelector(cls, @selector(dataTaskWithRequest:completionHandler:))) RPTInstallHookOnClass(cls, @selector(dataTaskWithRequest:completionHandler:), (IMP)RPTSessionDataRequestCompletion);
'''
probe = replace_once(probe, old_hooks, new_hooks, "URLSession URL-form hook install")

if 'RPTRecordTaskURL(self, @"ws.receive.arm")' in probe:
    raise SystemExit("ws.receive.arm logging still present")
if probe.count('@selector(dataTaskWithURL:)') != 2:
    raise SystemExit("unexpected dataTaskWithURL selector count")
if probe.count('@selector(dataTaskWithURL:completionHandler:)') != 2:
    raise SystemExit("unexpected dataTaskWithURL completion selector count")

probe_path.write_text(probe)

readme_path = Path("scripts/research/official_ios_realtime_probe/README.md")
readme = readme_path.read_text()
readme = replace_once(readme, "Current research revision: **Probe v0.2**.", "Current research revision: **Probe v0.3**.", "README version")
readme = replace_once(
    readme,
    "- transport errors by domain/code.\n",
    "- transport errors by domain/code; repeated receive failures on the same failed WebSocket task are emitted once until a real message arrives;\n- URLSession conversation/realtime observations cover both request-based and URL-based data-task constructors.\n",
    "README observation scope",
)
readme = replace_once(
    readme,
    "The decisive question is whether a target conversation event (`conversation-update`, `add-messages`, async status, or a per-turn subscription) arrives before assistant completion.\n",
    "The decisive question is which target-correlated acquisition event appears first before assistant completion: conversation HTTP/stream-status/resume/SSE, a conversation/per-turn WebSocket subscription/update, or another official route. Probe v0.3 also verifies that a failed user socket no longer expands the research log into a per-receive error storm.\n",
    "README decisive test",
)
readme_path.write_text(readme)
