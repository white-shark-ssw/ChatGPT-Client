#import <Foundation/Foundation.h>
#import <objc/runtime.h>
#import <CommonCrypto/CommonDigest.h>

static NSString * const RPTProbeVersion = @"0.1";
static NSString * const RPTLogName = @"ChatGPTRealtimeProbe.jsonl";
static const NSUInteger RPTMaxInspectableJSONBytes = 64 * 1024;

static dispatch_queue_t RPTLogQueue;
static NSMutableSet<NSString *> *RPTHookedKeys;
static NSMutableDictionary<NSString *, NSValue *> *RPTOriginalIMPs;

static NSString *RPTTimestamp(void) {
    static NSISO8601DateFormatter *formatter;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{ formatter = [NSISO8601DateFormatter new]; formatter.formatOptions = NSISO8601DateFormatWithInternetDateTime | NSISO8601DateFormatWithFractionalSeconds; });
    return [formatter stringFromDate:[NSDate date]];
}

static NSString *RPTLogPath(void) {
    NSString *documents = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES).firstObject ?: NSTemporaryDirectory();
    return [documents stringByAppendingPathComponent:RPTLogName];
}

static NSString *RPTHashString(NSString *value) {
    NSData *data = [value dataUsingEncoding:NSUTF8StringEncoding] ?: [NSData data];
    unsigned char digest[CC_SHA256_DIGEST_LENGTH];
    CC_SHA256(data.bytes, (CC_LONG)data.length, digest);
    NSMutableString *result = [NSMutableString stringWithCapacity:12];
    for (NSUInteger i = 0; i < 6; i++) [result appendFormat:@"%02x", digest[i]];
    return result;
}

static NSString *RPTValueClass(id value) {
    if (!value || value == [NSNull null]) return @"null";
    if ([value isKindOfClass:[NSString class]]) return @"string";
    if ([value isKindOfClass:[NSNumber class]]) return @"number";
    if ([value isKindOfClass:[NSArray class]]) return @"array";
    if ([value isKindOfClass:[NSDictionary class]]) return @"object";
    return NSStringFromClass([value class]) ?: @"other";
}

static NSString *RPTSafeToken(id value) {
    if (![value isKindOfClass:[NSString class]]) return @"";
    NSString *string = [(NSString *)value lowercaseString];
    if (string.length == 0 || string.length > 64) return @"";
    NSCharacterSet *allowed = [NSCharacterSet characterSetWithCharactersInString:@"abcdefghijklmnopqrstuvwxyz0123456789._:-"];
    if ([string rangeOfCharacterFromSet:allowed.invertedSet].location != NSNotFound) return @"";
    return string;
}

static NSString *RPTSafeTopic(id value) {
    if (![value isKindOfClass:[NSString class]]) return @"";
    NSString *string = (NSString *)value;
    if (string.length == 0) return @"";
    NSString *token = RPTSafeToken(string);
    NSRegularExpression *uuidLike = [NSRegularExpression regularExpressionWithPattern:@"[0-9a-f]{8}-[0-9a-f-]{20,}" options:NSRegularExpressionCaseInsensitive error:nil];
    BOOL opaque = token.length == 0 || string.length > 64 || [uuidLike firstMatchInString:string options:0 range:NSMakeRange(0, string.length)] != nil;
    return opaque ? [NSString stringWithFormat:@"opaque:%@", RPTHashString(string)] : string;
}

static NSArray<NSString *> *RPTSortedKeys(NSDictionary *dictionary) {
    NSMutableArray<NSString *> *keys = [NSMutableArray array];
    for (id key in dictionary.allKeys) if ([key isKindOfClass:[NSString class]]) [keys addObject:key];
    [keys sortUsingSelector:@selector(compare:)];
    if (keys.count > 48) [keys removeObjectsInRange:NSMakeRange(48, keys.count - 48)];
    return keys;
}

static void RPTWriteEvent(NSString *name, NSDictionary *fields) {
    if (!name.length) return;
    NSMutableDictionary *event = [NSMutableDictionary dictionaryWithDictionary:fields ?: @{}];
    event[@"ts"] = RPTTimestamp();
    event[@"event"] = name;
    event[@"probeVersion"] = RPTProbeVersion;
    dispatch_async(RPTLogQueue, ^{
        if (![NSJSONSerialization isValidJSONObject:event]) return;
        NSData *json = [NSJSONSerialization dataWithJSONObject:event options:0 error:nil];
        if (!json) return;
        NSMutableData *line = [json mutableCopy];
        [line appendData:[@"\n" dataUsingEncoding:NSUTF8StringEncoding]];
        NSString *path = RPTLogPath();
        NSFileManager *manager = NSFileManager.defaultManager;
        if (![manager fileExistsAtPath:path]) [manager createFileAtPath:path contents:nil attributes:nil];
        NSFileHandle *handle = [NSFileHandle fileHandleForWritingAtPath:path];
        if (!handle) return;
        @try { [handle seekToEndOfFile]; [handle writeData:line]; } @catch (__unused NSException *exception) {}
        [handle closeFile];
        NSLog(@"[ChatGPTRealtimeProbe] %@", name);
    });
}

static NSDictionary *RPTURLShape(NSURL *url) {
    if (!url) return @{};
    NSURLComponents *components = [NSURLComponents componentsWithURL:url resolvingAgainstBaseURL:NO];
    return @{
        @"scheme": url.scheme ?: @"",
        @"host": url.host ?: @"",
        @"path": url.path ?: @"",
        @"queryPresent": (components.percentEncodedQuery.length > 0) ? @YES : @NO,
        @"queryItemCount": @(components.queryItems.count)
    };
}

static BOOL RPTLikelyRealtimePath(NSString *path) {
    NSString *lower = path.lowercaseString;
    return [lower containsString:@"celsius"] || [lower containsString:@"websocket"] || [lower containsString:@"/ws/"] || [lower hasSuffix:@"/ws/user"];
}

static void RPTCollectNestedKeys(id object, NSUInteger depth, NSMutableSet<NSString *> *keys) {
    if (depth > 4 || keys.count >= 80) return;
    if ([object isKindOfClass:[NSDictionary class]]) {
        for (id key in [(NSDictionary *)object allKeys]) {
            if ([key isKindOfClass:[NSString class]]) [keys addObject:key];
            RPTCollectNestedKeys([(NSDictionary *)object objectForKey:key], depth + 1, keys);
            if (keys.count >= 80) break;
        }
    } else if ([object isKindOfClass:[NSArray class]]) {
        NSUInteger count = MIN([(NSArray *)object count], 8);
        for (NSUInteger i = 0; i < count; i++) RPTCollectNestedKeys([(NSArray *)object objectAtIndex:i], depth + 1, keys);
    }
}

static id RPTJSONObjectFromData(NSData *data) {
    if (!data.length || data.length > RPTMaxInspectableJSONBytes) return nil;
    return [NSJSONSerialization JSONObjectWithData:data options:0 error:nil];
}

static id RPTJSONObjectFromMessage(NSURLSessionWebSocketMessage *message) API_AVAILABLE(ios(13.0)) {
    NSData *data = nil;
    if (message.type == NSURLSessionWebSocketMessageTypeString) data = [message.string dataUsingEncoding:NSUTF8StringEncoding];
    else if (message.type == NSURLSessionWebSocketMessageTypeData) data = message.data;
    return RPTJSONObjectFromData(data);
}

static id RPTDecodedJSONObject(id value) {
    if ([value isKindOfClass:[NSDictionary class]] || [value isKindOfClass:[NSArray class]]) return value;
    if (![value isKindOfClass:[NSString class]]) return nil;
    NSString *string = (NSString *)value;
    if (string.length == 0 || string.length > RPTMaxInspectableJSONBytes) return nil;
    unichar first = [string characterAtIndex:0];
    if (first != '{' && first != '[') return nil;
    return RPTJSONObjectFromData([string dataUsingEncoding:NSUTF8StringEncoding]);
}

static id RPTFindValueForKeys(id object, NSArray<NSString *> *wanted, NSUInteger depth) {
    if (depth > 5) return nil;
    if ([object isKindOfClass:[NSDictionary class]]) {
        NSDictionary *dictionary = object;
        for (NSString *key in wanted) {
            id value = dictionary[key];
            if (value) return value;
        }
        for (id value in dictionary.allValues) {
            id found = RPTFindValueForKeys(RPTDecodedJSONObject(value) ?: value, wanted, depth + 1);
            if (found) return found;
        }
    } else if ([object isKindOfClass:[NSArray class]]) {
        NSUInteger count = MIN([(NSArray *)object count], 12);
        for (NSUInteger i = 0; i < count; i++) {
            id item = [(NSArray *)object objectAtIndex:i];
            id found = RPTFindValueForKeys(RPTDecodedJSONObject(item) ?: item, wanted, depth + 1);
            if (found) return found;
        }
    }
    return nil;
}

static NSDictionary *RPTFrameSummary(id frame) {
    id decoded = RPTDecodedJSONObject(frame) ?: frame;
    if (![decoded isKindOfClass:[NSDictionary class]]) return @{ @"frameClass": RPTValueClass(decoded) };
    NSDictionary *dictionary = decoded;
    NSMutableDictionary *summary = [NSMutableDictionary dictionary];
    summary[@"topKeys"] = RPTSortedKeys(dictionary);
    NSString *frameType = RPTSafeToken(dictionary[@"type"]);
    if (frameType.length) summary[@"frameType"] = frameType;
    id topic = dictionary[@"topic_id"] ?: dictionary[@"topicId"] ?: dictionary[@"topic"];
    if (topic) summary[@"topic"] = RPTSafeTopic(topic);
    id offset = dictionary[@"offset"] ?: dictionary[@"last_offset"] ?: dictionary[@"lastOffset"];
    if (offset) summary[@"offsetClass"] = RPTValueClass(offset);

    id commandValue = RPTDecodedJSONObject(dictionary[@"command"]) ?: dictionary[@"command"];
    if ([commandValue isKindOfClass:[NSDictionary class]]) {
        NSDictionary *command = commandValue;
        summary[@"commandKeys"] = RPTSortedKeys(command);
        NSString *commandType = RPTSafeToken(command[@"type"]);
        if (commandType.length) summary[@"commandType"] = commandType;
        id commandTopic = command[@"topic_id"] ?: command[@"topicId"] ?: command[@"topic"];
        if (commandTopic) summary[@"commandTopic"] = RPTSafeTopic(commandTopic);
        id commandOffset = command[@"offset"] ?: command[@"last_offset"] ?: command[@"lastOffset"];
        if (commandOffset) summary[@"commandOffsetClass"] = RPTValueClass(commandOffset);
        id presence = command[@"presence"];
        if ([presence isKindOfClass:[NSDictionary class]]) {
            NSString *state = RPTSafeToken(presence[@"state"]);
            if (state.length) summary[@"presenceState"] = state;
        }
    }

    id payloadValue = RPTDecodedJSONObject(dictionary[@"payload"]) ?: dictionary[@"payload"];
    if ([payloadValue isKindOfClass:[NSDictionary class]] || [payloadValue isKindOfClass:[NSArray class]]) {
        NSMutableSet<NSString *> *nested = [NSMutableSet set];
        RPTCollectNestedKeys(payloadValue, 0, nested);
        NSArray *nestedKeys = [[nested allObjects] sortedArrayUsingSelector:@selector(compare:)];
        if (nestedKeys.count > 80) nestedKeys = [nestedKeys subarrayWithRange:NSMakeRange(0, 80)];
        summary[@"payloadNestedKeys"] = nestedKeys;
    }

    id eventTypeValue = RPTFindValueForKeys(decoded, @[@"event", @"event_type", @"eventType"], 0);
    NSString *eventType = RPTSafeToken(eventTypeValue);
    if (eventType.length) summary[@"eventType"] = eventType;
    id updateTypeValue = RPTFindValueForKeys(decoded, @[@"update_type", @"updateType"], 0);
    NSString *updateType = RPTSafeToken(updateTypeValue);
    if (updateType.length) summary[@"updateType"] = updateType;
    id conversationValue = RPTFindValueForKeys(decoded, @[@"conversation_id", @"conversationId", @"conversation"], 0);
    if ([conversationValue isKindOfClass:[NSString class]] && [(NSString *)conversationValue length]) summary[@"conversationHash"] = RPTHashString(conversationValue);
    id messagesValue = RPTFindValueForKeys(decoded, @[@"messages"], 0);
    if ([messagesValue isKindOfClass:[NSArray class]]) summary[@"messagesCount"] = @([(NSArray *)messagesValue count]);
    return summary;
}

static NSArray<NSDictionary *> *RPTMessageSummaries(NSURLSessionWebSocketMessage *message) API_AVAILABLE(ios(13.0)) {
    id root = RPTJSONObjectFromMessage(message);
    if (!root) return @[@{ @"messageType": message.type == NSURLSessionWebSocketMessageTypeString ? @"string_non_json" : @"data_non_json" }];
    NSMutableArray<NSDictionary *> *summaries = [NSMutableArray array];
    if ([root isKindOfClass:[NSArray class]]) {
        NSUInteger count = MIN([(NSArray *)root count], 16);
        for (NSUInteger i = 0; i < count; i++) [summaries addObject:RPTFrameSummary([(NSArray *)root objectAtIndex:i])];
    } else {
        [summaries addObject:RPTFrameSummary(root)];
    }
    return summaries;
}

static NSString *RPTKeyForClassSelector(Class cls, SEL selector) { return [NSString stringWithFormat:@"%p:%@", cls, NSStringFromSelector(selector)]; }

static IMP RPTOriginalIMP(id object, SEL selector) {
    Class cls = object_getClass(object);
    while (cls) {
        NSValue *value = RPTOriginalIMPs[RPTKeyForClassSelector(cls, selector)];
        if (value) return value.pointerValue;
        cls = class_getSuperclass(cls);
    }
    return NULL;
}

static void RPTRecordTaskURL(NSURLSessionWebSocketTask *task, NSString *event) API_AVAILABLE(ios(13.0)) {
    NSURL *url = task.currentRequest.URL ?: task.originalRequest.URL;
    NSMutableDictionary *fields = [NSMutableDictionary dictionaryWithDictionary:RPTURLShape(url)];
    fields[@"taskClass"] = NSStringFromClass(object_getClass(task)) ?: @"";
    RPTWriteEvent(event, fields);
}

static void RPTWebSocketSend(id self, SEL _cmd, NSURLSessionWebSocketMessage *message, void (^completionHandler)(NSError *)) API_AVAILABLE(ios(13.0)) {
    RPTRecordTaskURL(self, @"ws.send");
    RPTWriteEvent(@"ws.outbound.frames", @{ @"frames": RPTMessageSummaries(message) });
    IMP original = RPTOriginalIMP(self, _cmd);
    if (!original) return;
    void (*function)(id, SEL, NSURLSessionWebSocketMessage *, void (^)(NSError *)) = (void *)original;
    function(self, _cmd, message, ^(NSError *error) {
        if (error) RPTWriteEvent(@"ws.send.error", @{ @"domain": error.domain ?: @"", @"code": @(error.code) });
        if (completionHandler) completionHandler(error);
    });
}

static void RPTWebSocketReceive(id self, SEL _cmd, void (^completionHandler)(NSURLSessionWebSocketMessage *, NSError *)) API_AVAILABLE(ios(13.0)) {
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

static void RPTInstallWebSocketTaskHooks(NSURLSessionWebSocketTask *task) API_AVAILABLE(ios(13.0)) {
    if (!task) return;
    Class cls = object_getClass(task);
    @synchronized (RPTHookedKeys) {
        SEL sendSelector = @selector(sendMessage:completionHandler:);
        NSString *sendKey = RPTKeyForClassSelector(cls, sendSelector);
        if (![RPTHookedKeys containsObject:sendKey]) {
            Method inherited = class_getInstanceMethod(cls, sendSelector);
            if (inherited) {
                IMP original = class_getMethodImplementation(cls, sendSelector);
                const char *types = method_getTypeEncoding(inherited);
                if (class_addMethod(cls, sendSelector, (IMP)RPTWebSocketSend, types)) RPTOriginalIMPs[sendKey] = [NSValue valueWithPointer:original];
                else {
                    Method own = class_getInstanceMethod(cls, sendSelector);
                    IMP old = method_setImplementation(own, (IMP)RPTWebSocketSend);
                    RPTOriginalIMPs[sendKey] = [NSValue valueWithPointer:old];
                }
                [RPTHookedKeys addObject:sendKey];
            }
        }

        SEL receiveSelector = @selector(receiveMessageWithCompletionHandler:);
        NSString *receiveKey = RPTKeyForClassSelector(cls, receiveSelector);
        if (![RPTHookedKeys containsObject:receiveKey]) {
            Method inherited = class_getInstanceMethod(cls, receiveSelector);
            if (inherited) {
                IMP original = class_getMethodImplementation(cls, receiveSelector);
                const char *types = method_getTypeEncoding(inherited);
                if (class_addMethod(cls, receiveSelector, (IMP)RPTWebSocketReceive, types)) RPTOriginalIMPs[receiveKey] = [NSValue valueWithPointer:original];
                else {
                    Method own = class_getInstanceMethod(cls, receiveSelector);
                    IMP old = method_setImplementation(own, (IMP)RPTWebSocketReceive);
                    RPTOriginalIMPs[receiveKey] = [NSValue valueWithPointer:old];
                }
                [RPTHookedKeys addObject:receiveKey];
            }
        }
    }
}

static NSURLSessionWebSocketTask *RPTSessionWebSocketRequest(id self, SEL _cmd, NSURLRequest *request) API_AVAILABLE(ios(13.0)) {
    IMP original = RPTOriginalIMP(self, _cmd);
    if (!original) return nil;
    NSURLSessionWebSocketTask *(*function)(id, SEL, NSURLRequest *) = (void *)original;
    NSURLSessionWebSocketTask *task = function(self, _cmd, request);
    NSMutableDictionary *fields = [NSMutableDictionary dictionaryWithDictionary:RPTURLShape(request.URL)];
    fields[@"method"] = request.HTTPMethod ?: @"GET";
    fields[@"sessionClass"] = NSStringFromClass(object_getClass(self)) ?: @"";
    RPTWriteEvent(@"ws.task.created", fields);
    RPTInstallWebSocketTaskHooks(task);
    return task;
}

static NSURLSessionWebSocketTask *RPTSessionWebSocketURL(id self, SEL _cmd, NSURL *url) API_AVAILABLE(ios(13.0)) {
    IMP original = RPTOriginalIMP(self, _cmd);
    if (!original) return nil;
    NSURLSessionWebSocketTask *(*function)(id, SEL, NSURL *) = (void *)original;
    NSURLSessionWebSocketTask *task = function(self, _cmd, url);
    NSMutableDictionary *fields = [NSMutableDictionary dictionaryWithDictionary:RPTURLShape(url)];
    fields[@"sessionClass"] = NSStringFromClass(object_getClass(self)) ?: @"";
    RPTWriteEvent(@"ws.task.created", fields);
    RPTInstallWebSocketTaskHooks(task);
    return task;
}

static NSURLSessionDataTask *RPTSessionDataRequest(id self, SEL _cmd, NSURLRequest *request) {
    IMP original = RPTOriginalIMP(self, _cmd);
    if (!original) return nil;
    NSURLSessionDataTask *(*function)(id, SEL, NSURLRequest *) = (void *)original;
    NSURLSessionDataTask *task = function(self, _cmd, request);
    if (RPTLikelyRealtimePath(request.URL.path ?: @"")) {
        NSMutableDictionary *fields = [NSMutableDictionary dictionaryWithDictionary:RPTURLShape(request.URL)];
        fields[@"method"] = request.HTTPMethod ?: @"GET";
        RPTWriteEvent(@"http.realtime.request", fields);
    }
    return task;
}

static NSURLSessionDataTask *RPTSessionDataRequestCompletion(id self, SEL _cmd, NSURLRequest *request, void (^completionHandler)(NSData *, NSURLResponse *, NSError *)) {
    IMP original = RPTOriginalIMP(self, _cmd);
    if (!original) return nil;
    NSURLSessionDataTask *(*function)(id, SEL, NSURLRequest *, void (^)(NSData *, NSURLResponse *, NSError *)) = (void *)original;
    BOOL candidate = RPTLikelyRealtimePath(request.URL.path ?: @"");
    if (candidate) {
        NSMutableDictionary *fields = [NSMutableDictionary dictionaryWithDictionary:RPTURLShape(request.URL)];
        fields[@"method"] = request.HTTPMethod ?: @"GET";
        RPTWriteEvent(@"http.realtime.request", fields);
    }
    return function(self, _cmd, request, ^(NSData *data, NSURLResponse *response, NSError *error) {
        NSHTTPURLResponse *http = [response isKindOfClass:[NSHTTPURLResponse class]] ? (id)response : nil;
        id json = RPTJSONObjectFromData(data);
        NSArray *keys = [json isKindOfClass:[NSDictionary class]] ? RPTSortedKeys(json) : @[];
        BOOL websocketResponse = NO;
        for (NSString *key in keys) {
            NSString *lower = key.lowercaseString;
            if ([lower containsString:@"websocket"] || [lower isEqualToString:@"ws_url"] || [lower isEqualToString:@"wsurl"]) { websocketResponse = YES; break; }
        }
        if (candidate || websocketResponse) {
            NSMutableDictionary *fields = [NSMutableDictionary dictionaryWithDictionary:RPTURLShape(response.URL ?: request.URL)];
            fields[@"method"] = request.HTTPMethod ?: @"GET";
            fields[@"status"] = @(http.statusCode);
            fields[@"responseKeys"] = keys;
            fields[@"responseClass"] = RPTValueClass(json);
            if (error) { fields[@"errorDomain"] = error.domain ?: @""; fields[@"errorCode"] = @(error.code); }
            RPTWriteEvent(@"http.realtime.response", fields);
        }
        if (completionHandler) completionHandler(data, response, error);
    });
}

static BOOL RPTIsSubclassOfClass(Class cls, Class parent) {
    for (Class current = cls; current; current = class_getSuperclass(current)) if (current == parent) return YES;
    return NO;
}

static BOOL RPTClassOwnsSelector(Class cls, SEL selector) {
    unsigned int count = 0;
    Method *methods = class_copyMethodList(cls, &count);
    BOOL owns = NO;
    for (unsigned int i = 0; i < count; i++) {
        if (method_getName(methods[i]) == selector) { owns = YES; break; }
    }
    free(methods);
    return owns;
}

static void RPTInstallHookOnClass(Class cls, SEL selector, IMP replacement) {
    if (!cls || !selector || !replacement) return;
    NSString *key = RPTKeyForClassSelector(cls, selector);
    @synchronized (RPTHookedKeys) {
        if ([RPTHookedKeys containsObject:key]) return;
        Method inherited = class_getInstanceMethod(cls, selector);
        if (!inherited) return;
        IMP original = class_getMethodImplementation(cls, selector);
        const char *types = method_getTypeEncoding(inherited);
        if (class_addMethod(cls, selector, replacement, types)) RPTOriginalIMPs[key] = [NSValue valueWithPointer:original];
        else {
            Method own = class_getInstanceMethod(cls, selector);
            IMP old = method_setImplementation(own, replacement);
            RPTOriginalIMPs[key] = [NSValue valueWithPointer:old];
        }
        [RPTHookedKeys addObject:key];
    }
}

static void RPTInstallSessionHooks(void) {
    int count = objc_getClassList(NULL, 0);
    if (count <= 0) return;
    Class *classes = (__unsafe_unretained Class *)calloc((size_t)count, sizeof(Class));
    count = objc_getClassList(classes, count);
    Class sessionClass = NSURLSession.class;
    for (int i = 0; i < count; i++) {
        Class cls = classes[i];
        if (!RPTIsSubclassOfClass(cls, sessionClass)) continue;
        if (@available(iOS 13.0, *)) {
            if (RPTClassOwnsSelector(cls, @selector(webSocketTaskWithRequest:))) RPTInstallHookOnClass(cls, @selector(webSocketTaskWithRequest:), (IMP)RPTSessionWebSocketRequest);
            if (RPTClassOwnsSelector(cls, @selector(webSocketTaskWithURL:))) RPTInstallHookOnClass(cls, @selector(webSocketTaskWithURL:), (IMP)RPTSessionWebSocketURL);
        }
        if (RPTClassOwnsSelector(cls, @selector(dataTaskWithRequest:))) RPTInstallHookOnClass(cls, @selector(dataTaskWithRequest:), (IMP)RPTSessionDataRequest);
        if (RPTClassOwnsSelector(cls, @selector(dataTaskWithRequest:completionHandler:))) RPTInstallHookOnClass(cls, @selector(dataTaskWithRequest:completionHandler:), (IMP)RPTSessionDataRequestCompletion);
    }
    free(classes);
}

__attribute__((constructor)) static void RPTInitialize(void) {
    @autoreleasepool {
        RPTLogQueue = dispatch_queue_create("dev.chatgptclient.realtime-probe.log", DISPATCH_QUEUE_SERIAL);
        RPTHookedKeys = [NSMutableSet set];
        RPTOriginalIMPs = [NSMutableDictionary dictionary];
        RPTWriteEvent(@"probe.loaded", @{ @"bundleID": NSBundle.mainBundle.bundleIdentifier ?: @"", @"logFile": RPTLogName });
        RPTInstallSessionHooks();
        RPTWriteEvent(@"probe.hooks_installed", @{ @"hookCount": @(RPTHookedKeys.count) });
    }
}
