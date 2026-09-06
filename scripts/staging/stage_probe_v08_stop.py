from pathlib import Path

SOURCE = Path("scripts/research/official_ios_realtime_probe/ChatGPTRealtimeProbe.m")
README = Path("scripts/research/official_ios_realtime_probe/README.md")

text = SOURCE.read_text()

old = 'static NSString * const RPTProbeVersion = @"0.7";'
new = 'static NSString * const RPTProbeVersion = @"0.8";'
assert text.count(old) == 1
text = text.replace(old, new)

old = '''        if ([parts[1] isEqualToString:@"conversation"] && parts.count >= 3) {
            if (parts.count >= 4 && [parts[3] isEqualToString:@"stream_status"]) return @"conversation_stream_status";
            return @"conversation_detail";
        }'''
new = '''        if ([parts[1] isEqualToString:@"conversation"] && parts.count >= 3) {
            if (parts.count >= 4 && [parts[3] isEqualToString:@"stream_status"]) return @"conversation_stream_status";
            if (parts.count >= 4 && [parts[3] isEqualToString:@"stop_conversation"]) return @"conversation_stop";
            return @"conversation_detail";
        }'''
assert text.count(old) == 1
text = text.replace(old, new)

anchor = '''static void RPTWriteEvent(NSString *name, NSDictionary *fields) {'''
insert = '''static NSDictionary<NSString *, NSString *> *RPTValueClassesForDictionary(NSDictionary *dictionary) {
    NSMutableDictionary<NSString *, NSString *> *classes = [NSMutableDictionary dictionary];
    for (NSString *key in RPTSortedKeys(dictionary)) classes[key] = RPTValueClass(dictionary[key]);
    return classes;
}

static NSDictionary<NSString *, NSString *> *RPTIdentifierHashesForDictionary(NSDictionary *dictionary) {
    NSMutableDictionary<NSString *, NSString *> *hashes = [NSMutableDictionary dictionary];
    for (NSString *key in RPTSortedKeys(dictionary)) {
        NSString *lower = key.lowercaseString;
        BOOL identifierKey = [lower hasSuffix:@"id"] || [lower containsString:@"_id"] || [lower containsString:@"node"];
        id value = dictionary[key];
        if (identifierKey && [value isKindOfClass:[NSString class]] && [(NSString *)value length]) hashes[key] = RPTHashString(value);
    }
    return hashes;
}

'''
assert text.count(anchor) == 1
text = text.replace(anchor, insert + anchor)

anchor = '''static id RPTJSONObjectFromMessage(NSURLSessionWebSocketMessage *message) API_AVAILABLE(ios(13.0)) {'''
insert = '''static BOOL RPTIsConversationStopRequest(NSURLRequest *request) {
    return [[RPTPathKind(request.URL.path ?: @"") lowercaseString] isEqualToString:@"conversation_stop"];
}

static NSMutableDictionary *RPTConversationStopRequestFields(NSURLRequest *request) {
    NSMutableDictionary *fields = RPTRequestFields(request);
    if (request.HTTPBody) fields[@"requestBodyBytes"] = @(request.HTTPBody.length);
    id json = RPTJSONObjectFromData(request.HTTPBody);
    if ([json isKindOfClass:[NSDictionary class]]) {
        NSDictionary *dictionary = json;
        fields[@"requestValueClasses"] = RPTValueClassesForDictionary(dictionary);
        NSDictionary *hashes = RPTIdentifierHashesForDictionary(dictionary);
        if (hashes.count) fields[@"requestIdentifierHashes"] = hashes;
    }
    return fields;
}

static NSMutableDictionary *RPTConversationStopResponseFields(NSURLRequest *request, NSURLResponse *response, NSData *data, NSError *error) {
    NSMutableDictionary *fields = RPTResponseFields(request, response, data, error);
    id json = RPTJSONObjectFromData(data);
    if ([json isKindOfClass:[NSDictionary class]]) {
        NSDictionary *dictionary = json;
        fields[@"responseValueClasses"] = RPTValueClassesForDictionary(dictionary);
        NSDictionary *hashes = RPTIdentifierHashesForDictionary(dictionary);
        if (hashes.count) fields[@"responseIdentifierHashes"] = hashes;
    }
    return fields;
}

'''
assert text.count(anchor) == 1
text = text.replace(anchor, insert + anchor)

old = '''    BOOL candidate = RPTShouldObserveURL(request.URL);
    if (candidate) RPTWriteEvent(@"http.observed.request", RPTRequestFields(request));
    return function(self, _cmd, request, ^(NSData *data, NSURLResponse *response, NSError *error) {'''
new = '''    BOOL candidate = RPTShouldObserveURL(request.URL);
    BOOL stopCandidate = RPTIsConversationStopRequest(request);
    if (candidate) RPTWriteEvent(@"http.observed.request", RPTRequestFields(request));
    if (stopCandidate) RPTWriteEvent(@"http.conversation_stop.request", RPTConversationStopRequestFields(request));
    return function(self, _cmd, request, ^(NSData *data, NSURLResponse *response, NSError *error) {'''
assert text.count(old) == 1
text = text.replace(old, new)

old = '''        if (candidate || websocketResponse) RPTWriteEvent(@"http.observed.response", RPTResponseFields(request, response, data, error));
        if (completionHandler) completionHandler(data, response, error);'''
new = '''        if (candidate || websocketResponse) RPTWriteEvent(@"http.observed.response", RPTResponseFields(request, response, data, error));
        if (stopCandidate) RPTWriteEvent(@"http.conversation_stop.response", RPTConversationStopResponseFields(request, response, data, error));
        if (completionHandler) completionHandler(data, response, error);'''
assert text.count(old) == 1
text = text.replace(old, new)

anchor = '''static void RPTTaskDidReceiveDispatchData(id self, SEL _cmd, dispatch_data_t dispatchData, id completionHandler) {'''
insert = '''static void RPTObserveConversationStopDispatchData(NSURLSessionDataTask *task, dispatch_data_t dispatchData) {
    if (!task || !dispatchData) return;
    NSURLRequest *request = task.currentRequest ?: task.originalRequest;
    if (!RPTIsConversationStopRequest(request)) return;
    __block BOOL emittedStructured = NO;
    dispatch_data_apply(dispatchData, ^bool(__unused dispatch_data_t region, __unused size_t offset, const void *buffer, size_t size) {
        if (!buffer || size == 0) return true;
        NSData *chunk = [NSData dataWithBytesNoCopy:(void *)buffer length:size freeWhenDone:NO];
        id json = RPTJSONObjectFromData(chunk);
        if ([json isKindOfClass:[NSDictionary class]]) {
            NSMutableDictionary *fields = RPTConversationStopResponseFields(request, task.response, chunk, nil);
            fields[@"taskClass"] = NSStringFromClass(object_getClass(task)) ?: @"";
            RPTWriteEvent(@"http.conversation_stop.response_data", fields);
            emittedStructured = YES;
            return false;
        }
        return true;
    });
    if (!emittedStructured) {
        NSMutableDictionary *fields = RPTConversationStopResponseFields(request, task.response, nil, nil);
        fields[@"taskClass"] = NSStringFromClass(object_getClass(task)) ?: @"";
        fields[@"dispatchDataPresent"] = @YES;
        RPTWriteEvent(@"http.conversation_stop.response_data", fields);
    }
}

'''
assert text.count(anchor) == 1
text = text.replace(anchor, insert + anchor)

old = '''static void RPTTaskDidReceiveDispatchData(id self, SEL _cmd, dispatch_data_t dispatchData, id completionHandler) {
    RPTObserveConversationDetailDispatchData((NSURLSessionDataTask *)self, dispatchData);'''
new = '''static void RPTTaskDidReceiveDispatchData(id self, SEL _cmd, dispatch_data_t dispatchData, id completionHandler) {
    RPTObserveConversationDetailDispatchData((NSURLSessionDataTask *)self, dispatchData);
    RPTObserveConversationStopDispatchData((NSURLSessionDataTask *)self, dispatchData);'''
assert text.count(old) == 1
text = text.replace(old, new)

old = '''static void RPTDelegateDidReceiveResponse(id self, SEL _cmd, NSURLSession *session, NSURLSessionDataTask *dataTask, NSURLResponse *response, void (^completionHandler)(NSURLSessionResponseDisposition)) {
    NSURLRequest *request = dataTask.currentRequest ?: dataTask.originalRequest;
    if (RPTShouldObserveURL(request.URL ?: response.URL)) RPTWriteEvent(@"http.observed.response", RPTResponseFields(request, response, nil, nil));'''
new = '''static void RPTDelegateDidReceiveResponse(id self, SEL _cmd, NSURLSession *session, NSURLSessionDataTask *dataTask, NSURLResponse *response, void (^completionHandler)(NSURLSessionResponseDisposition)) {
    NSURLRequest *request = dataTask.currentRequest ?: dataTask.originalRequest;
    if (RPTShouldObserveURL(request.URL ?: response.URL)) RPTWriteEvent(@"http.observed.response", RPTResponseFields(request, response, nil, nil));
    if (RPTIsConversationStopRequest(request)) RPTWriteEvent(@"http.conversation_stop.response", RPTConversationStopResponseFields(request, response, nil, nil));'''
assert text.count(old) == 1
text = text.replace(old, new)

old = '''static void RPTDelegateDidComplete(id self, SEL _cmd, NSURLSession *session, NSURLSessionTask *task, NSError *error) {
    NSURLRequest *request = task.currentRequest ?: task.originalRequest;
    if (RPTShouldObserveURL(request.URL)) RPTWriteEvent(@"http.observed.complete", RPTResponseFields(request, task.response, nil, error));'''
new = '''static void RPTDelegateDidComplete(id self, SEL _cmd, NSURLSession *session, NSURLSessionTask *task, NSError *error) {
    NSURLRequest *request = task.currentRequest ?: task.originalRequest;
    if (RPTShouldObserveURL(request.URL)) RPTWriteEvent(@"http.observed.complete", RPTResponseFields(request, task.response, nil, error));
    if (RPTIsConversationStopRequest(request)) RPTWriteEvent(@"http.conversation_stop.complete", RPTConversationStopResponseFields(request, task.response, nil, error));'''
assert text.count(old) == 1
text = text.replace(old, new)

old = '''    if (request.URL && RPTShouldObserveTaskURL(request.URL) && !objc_getAssociatedObject(self, &RPTTaskResumeLoggedKey)) {
        objc_setAssociatedObject(self, &RPTTaskResumeLoggedKey, @YES, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
        NSMutableDictionary *fields = RPTRequestFields(request);
        fields[@"taskClass"] = NSStringFromClass(object_getClass(self)) ?: @"";
        RPTWriteEvent(@"http.task.resume", fields);
    }'''
new = '''    if (request.URL && RPTShouldObserveTaskURL(request.URL) && !objc_getAssociatedObject(self, &RPTTaskResumeLoggedKey)) {
        objc_setAssociatedObject(self, &RPTTaskResumeLoggedKey, @YES, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
        NSMutableDictionary *fields = RPTRequestFields(request);
        fields[@"taskClass"] = NSStringFromClass(object_getClass(self)) ?: @"";
        RPTWriteEvent(@"http.task.resume", fields);
        if (RPTIsConversationStopRequest(request)) {
            NSMutableDictionary *stopFields = RPTConversationStopRequestFields(request);
            stopFields[@"taskClass"] = NSStringFromClass(object_getClass(self)) ?: @"";
            RPTWriteEvent(@"http.conversation_stop.request", stopFields);
        }
    }'''
assert text.count(old) == 1
text = text.replace(old, new)

SOURCE.write_text(text)

readme = README.read_text()
assert readme.count('Current research revision: **Probe v0.7**.') == 1
readme = readme.replace('Current research revision: **Probe v0.7**.', 'Current research revision: **Probe v0.8**.')
anchor = 'Research-only observer for the user-supplied TrollStore ChatGPT package. It is not linked into ChatGPTClient and is not a product Candidate.\n'
assert readme.count(anchor) == 1
section = '''\nProbe v0.8 adds one exact **official Stop structural gate** on top of the already-evidenced v0.7 transport observers. It recognizes only `/backend-api/conversation/<opaque>/stop_conversation`. For that route it records the request method/path shape, top-level JSON keys and value classes, irreversible short hashes for top-level identifier-like string fields, response status/MIME and response JSON key/value structure where available. It never records raw IDs or request/response content, and it never initiates Stop or any other request.\n'''
readme = readme.replace(anchor, anchor + section)
old = '''## Decisive test\n\n1. Launch the injected official app and open/keep conversation A available.\n2. Confirm `probe.loaded` and WebSocket setup events exist in `ChatGPTRealtimeProbe.jsonl`.\n3. From another platform, send one deliberately long text turn to A.\n4. Let the response complete without manually refreshing A on the official iOS app.\n5. Export/copy only `ChatGPTRealtimeProbe.jsonl` for analysis.\n'''
new = '''## Decisive Stop test\n\n1. Install only the exact v0.8 research package, fully terminate/relaunch the official app, press `清空`, and open one normal existing conversation.\n2. Start one deliberately long response from the official iOS app itself.\n3. While the response is visibly active, invoke the official Stop control exactly once.\n4. Wait for the official UI to settle and for any official post-Stop Detail/async-status traffic to occur naturally. Do not manually refresh or issue a second Stop.\n5. Export/copy only `ChatGPTRealtimeProbe.jsonl` for analysis. Required evidence is `http.conversation_stop.*` request/response structure plus the app's naturally observed post-Stop terminal/Detail behavior.\n'''
assert readme.count(old) == 1
readme = readme.replace(old, new)
README.write_text(readme)
