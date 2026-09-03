#import <Foundation/Foundation.h>
#import <objc/runtime.h>
#import <CommonCrypto/CommonDigest.h>

static NSString * const RPTProbeVersion = @"0.5";
static NSString * const RPTLogName = @"ChatGPTRealtimeProbe.jsonl";
static const NSUInteger RPTMaxInspectableJSONBytes = 64 * 1024;

static dispatch_queue_t RPTLogQueue;
static NSMutableSet<NSString *> *RPTHookedKeys;
static NSMutableDictionary<NSString *, NSValue *> *RPTOriginalIMPs;
static char RPTWebSocketReceiveErrorLoggedKey;
static char RPTTaskResumeLoggedKey;
static char RPTDetailAsyncStatusLoggedKey;
static char RPTDetailScanTailKey;
static BOOL RPTLateSessionRefreshDone = NO;

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

void RPTClearLog(void) {
    if (!RPTLogQueue) return;
    dispatch_sync(RPTLogQueue, ^{
        [[NSFileManager defaultManager] removeItemAtPath:RPTLogPath() error:nil];
    });
    RPTWriteEvent(@"probe.log_cleared", @{});
}

static NSArray<NSString *> *RPTPathParts(NSString *path) {
    NSMutableArray<NSString *> *parts = [NSMutableArray array];
    for (NSString *part in [path componentsSeparatedByString:@"/"]) if (part.length) [parts addObject:part];
    return parts;
}

static BOOL RPTLooksOpaquePathPart(NSString *part) {
    if (!part.length) return NO;
    if (part.length > 32) return YES;
    NSString *lower = part.lowercaseString;
    if ([lower hasPrefix:@"user-"] && part.length > 12) return YES;
    NSRegularExpression *uuidLike = [NSRegularExpression regularExpressionWithPattern:@"^[0-9a-f]{8}-[0-9a-f-]{20,}$" options:NSRegularExpressionCaseInsensitive error:nil];
    if ([uuidLike firstMatchInString:part options:0 range:NSMakeRange(0, part.length)]) return YES;
    return RPTSafeToken(part).length == 0;
}

static NSString *RPTSafePathShape(NSString *path) {
    NSArray<NSString *> *parts = RPTPathParts(path ?: @"");
    NSMutableArray<NSString *> *safe = [NSMutableArray arrayWithCapacity:parts.count];
    for (NSString *part in parts) [safe addObject:RPTLooksOpaquePathPart(part) ? @"<opaque>" : part.lowercaseString];
    return safe.count ? [@"/" stringByAppendingString:[safe componentsJoinedByString:@"/"]] : @"/";
}

static NSString *RPTPathKind(NSString *path) {
    NSArray<NSString *> *parts = RPTPathParts(path ?: @"");
    NSString *lower = path.lowercaseString;
    if ([lower containsString:@"/ws/user/"] || [lower hasSuffix:@"/ws/user"]) return @"user_websocket";
    if (parts.count >= 2 && [parts[0] isEqualToString:@"backend-api"]) {
        if ([parts[1] isEqualToString:@"conversation"] && parts.count >= 3) {
            if (parts.count >= 4 && [parts[3] isEqualToString:@"stream_status"]) return @"conversation_stream_status";
            return @"conversation_detail";
        }
        if ([parts[1] isEqualToString:@"conversations"]) return @"conversations";
        if ([parts[1] isEqualToString:@"f"] && parts.count >= 3 && [parts[2] isEqualToString:@"conversation"]) {
            if (parts.count >= 4 && [parts[3] isEqualToString:@"resume"]) return @"conversation_resume";
            return @"conversation_send";
        }
    }
    if ([lower containsString:@"celsius"] || [lower containsString:@"websocket"] || [lower containsString:@"/ws/"]) return @"realtime_registration";
    if ([lower containsString:@"conversation"]) return @"conversation_other";
    if ([lower containsString:@"stream"] || [lower containsString:@"resume"]) return @"stream_other";
    return @"other";
}

static NSDictionary *RPTURLShape(NSURL *url) {
    if (!url) return @{};
    NSURLComponents *components = [NSURLComponents componentsWithURL:url resolvingAgainstBaseURL:NO];
    return @{
        @"scheme": url.scheme ?: @"",
        @"host": url.host ?: @"",
        @"pathShape": RPTSafePathShape(url.path ?: @""),
        @"pathKind": RPTPathKind(url.path ?: @""),
        @"queryPresent": (components.percentEncodedQuery.length > 0) ? @YES : @NO,
        @"queryItemCount": @(components.queryItems.count)
    };
}

static BOOL RPTShouldObserveURL(NSURL *url) { return ![RPTPathKind(url.path ?: @"") isEqualToString:@"other"]; }

static NSString *RPTConversationHashFromURL(NSURL *url) {
    NSArray<NSString *> *parts = RPTPathParts(url.path ?: @"");
    if (parts.count >= 3 && [parts[0] isEqualToString:@"backend-api"] && ([parts[1] isEqualToString:@"conversation"] || [parts[1] isEqualToString:@"conversations"])) return RPTHashString(parts[2]);
    return @"";
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

static NSMutableDictionary *RPTRequestFields(NSURLRequest *request) {
    NSMutableDictionary *fields = [NSMutableDictionary dictionaryWithDictionary:RPTURLShape(request.URL)];
    fields[@"method"] = request.HTTPMethod ?: @"GET";
    NSString *conversationHash = RPTConversationHashFromURL(request.URL);
    if (conversationHash.length) fields[@"conversationHash"] = conversationHash;
    id json = RPTJSONObjectFromData(request.HTTPBody);
    if ([json isKindOfClass:[NSDictionary class]]) {
        NSDictionary *dictionary = json;
        fields[@"requestKeys"] = RPTSortedKeys(dictionary);
        id conversation = dictionary[@"conversation_id"] ?: dictionary[@"conversationId"];
        if ([conversation isKindOfClass:[NSString class]] && [(NSString *)conversation length]) fields[@"conversationHash"] = RPTHashString(conversation);
        id offset = dictionary[@"offset"] ?: dictionary[@"last_offset"] ?: dictionary[@"lastOffset"];
        if (offset) fields[@"offsetClass"] = RPTValueClass(offset);
    }
    return fields;
}

static NSMutableDictionary *RPTResponseFields(NSURLRequest *request, NSURLResponse *response, NSData *data, NSError *error) {
    NSURL *url = response.URL ?: request.URL;
    NSMutableDictionary *fields = [NSMutableDictionary dictionaryWithDictionary:RPTURLShape(url)];
    fields[@"method"] = request.HTTPMethod ?: @"GET";
    NSString *conversationHash = RPTConversationHashFromURL(url);
    if (conversationHash.length) fields[@"conversationHash"] = conversationHash;
    NSHTTPURLResponse *http = [response isKindOfClass:[NSHTTPURLResponse class]] ? (id)response : nil;
    if (http) fields[@"status"] = @(http.statusCode);
    if (response.MIMEType.length) fields[@"mimeType"] = response.MIMEType.lowercaseString;
    if (response.expectedContentLength >= 0) fields[@"expectedContentLength"] = @(response.expectedContentLength);
    if (data) fields[@"bodyBytes"] = @(data.length);
    id json = RPTJSONObjectFromData(data);
    if ([json isKindOfClass:[NSDictionary class]]) fields[@"responseKeys"] = RPTSortedKeys(json);
    fields[@"responseClass"] = RPTValueClass(json);
    if (error) { fields[@"errorDomain"] = error.domain ?: @""; fields[@"errorCode"] = @(error.code); }
    return fields;
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
        NSString *commandState = RPTSafeToken(command[@"state"]);
        if (commandState.length) summary[@"commandState"] = commandState;
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
    if (RPTShouldObserveURL(request.URL)) RPTWriteEvent(@"http.observed.request", RPTRequestFields(request));
    return task;
}

static NSURLSessionDataTask *RPTSessionDataRequestCompletion(id self, SEL _cmd, NSURLRequest *request, void (^completionHandler)(NSData *, NSURLResponse *, NSError *)) {
    IMP original = RPTOriginalIMP(self, _cmd);
    if (!original) return nil;
    NSURLSessionDataTask *(*function)(id, SEL, NSURLRequest *, void (^)(NSData *, NSURLResponse *, NSError *)) = (void *)original;
    BOOL candidate = RPTShouldObserveURL(request.URL);
    if (candidate) RPTWriteEvent(@"http.observed.request", RPTRequestFields(request));
    return function(self, _cmd, request, ^(NSData *data, NSURLResponse *response, NSError *error) {
        id json = RPTJSONObjectFromData(data);
        NSArray *keys = [json isKindOfClass:[NSDictionary class]] ? RPTSortedKeys(json) : @[];
        BOOL websocketResponse = NO;
        for (NSString *key in keys) {
            NSString *lower = key.lowercaseString;
            if ([lower containsString:@"websocket"] || [lower isEqualToString:@"ws_url"] || [lower isEqualToString:@"wsurl"]) { websocketResponse = YES; break; }
        }
        if (candidate || websocketResponse) RPTWriteEvent(@"http.observed.response", RPTResponseFields(request, response, data, error));
        if (completionHandler) completionHandler(data, response, error);
    });
}

static NSURLSessionDataTask *RPTSessionDataURL(id self, SEL _cmd, NSURL *url) {
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

static NSString *RPTConversationAsyncStatusToken(NSData *data, NSRange keyRange) {
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

static void RPTDelegateDidReceiveResponse(id self, SEL _cmd, NSURLSession *session, NSURLSessionDataTask *dataTask, NSURLResponse *response, void (^completionHandler)(NSURLSessionResponseDisposition)) {
    NSURLRequest *request = dataTask.currentRequest ?: dataTask.originalRequest;
    if (RPTShouldObserveURL(request.URL ?: response.URL)) RPTWriteEvent(@"http.observed.response", RPTResponseFields(request, response, nil, nil));
    IMP original = RPTOriginalIMP(self, _cmd);
    if (!original) return;
    void (*function)(id, SEL, NSURLSession *, NSURLSessionDataTask *, NSURLResponse *, void (^)(NSURLSessionResponseDisposition)) = (void *)original;
    function(self, _cmd, session, dataTask, response, completionHandler);
}

static void RPTDelegateDidComplete(id self, SEL _cmd, NSURLSession *session, NSURLSessionTask *task, NSError *error) {
    NSURLRequest *request = task.currentRequest ?: task.originalRequest;
    if (RPTShouldObserveURL(request.URL)) RPTWriteEvent(@"http.observed.complete", RPTResponseFields(request, task.response, nil, error));
    IMP original = RPTOriginalIMP(self, _cmd);
    if (!original) return;
    void (*function)(id, SEL, NSURLSession *, NSURLSessionTask *, NSError *) = (void *)original;
    function(self, _cmd, session, task, error);
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

static BOOL RPTShouldObserveTaskURL(NSURL *url) {
    if (!url) return NO;
    NSString *host = url.host.lowercaseString ?: @"";
    if ([host isEqualToString:@"chatgpt.com"] || [host isEqualToString:@"chat.openai.com"] || [host isEqualToString:@"ios.chat.openai.com"] || [host isEqualToString:@"api.openai.com"]) return YES;
    if ([host hasSuffix:@".chatgpt.com"] || [host hasSuffix:@".openai.com"]) return YES;
    return RPTShouldObserveURL(url);
}

static void RPTInstallSessionHooks(void);

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
    if (request.URL && RPTShouldObserveTaskURL(request.URL) && !objc_getAssociatedObject(self, &RPTTaskResumeLoggedKey)) {
        objc_setAssociatedObject(self, &RPTTaskResumeLoggedKey, @YES, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
        NSMutableDictionary *fields = RPTRequestFields(request);
        fields[@"taskClass"] = NSStringFromClass(object_getClass(self)) ?: @"";
        RPTWriteEvent(@"http.task.resume", fields);
    }
    IMP original = RPTOriginalIMP(self, _cmd);
    if (!original) return;
    void (*function)(id, SEL) = (void *)original;
    function(self, _cmd);
}

static void RPTInstallSessionHooks(void) {
    int count = objc_getClassList(NULL, 0);
    if (count <= 0) return;
    Class *classes = (__unsafe_unretained Class *)calloc((size_t)count, sizeof(Class));
    count = objc_getClassList(classes, count);
    Class sessionClass = NSURLSession.class;
    Class taskClass = NSURLSessionTask.class;
    SEL dataSelector = NSSelectorFromString(@"URLSession:dataTask:didReceiveData:");
    SEL responseSelector = NSSelectorFromString(@"URLSession:dataTask:didReceiveResponse:completionHandler:");
    SEL completeSelector = NSSelectorFromString(@"URLSession:task:didCompleteWithError:");
    for (int i = 0; i < count; i++) {
        Class cls = classes[i];
        if (RPTIsSubclassOfClass(cls, taskClass) && RPTClassOwnsSelector(cls, @selector(resume))) RPTInstallHookOnClass(cls, @selector(resume), (IMP)RPTTaskResume);
        if (RPTIsSubclassOfClass(cls, sessionClass)) {
            if (@available(iOS 13.0, *)) {
                if (RPTClassOwnsSelector(cls, @selector(webSocketTaskWithRequest:))) RPTInstallHookOnClass(cls, @selector(webSocketTaskWithRequest:), (IMP)RPTSessionWebSocketRequest);
                if (RPTClassOwnsSelector(cls, @selector(webSocketTaskWithURL:))) RPTInstallHookOnClass(cls, @selector(webSocketTaskWithURL:), (IMP)RPTSessionWebSocketURL);
            }
            if (RPTClassOwnsSelector(cls, @selector(dataTaskWithURL:))) RPTInstallHookOnClass(cls, @selector(dataTaskWithURL:), (IMP)RPTSessionDataURL);
            if (RPTClassOwnsSelector(cls, @selector(dataTaskWithURL:completionHandler:))) RPTInstallHookOnClass(cls, @selector(dataTaskWithURL:completionHandler:), (IMP)RPTSessionDataURLCompletion);
            if (RPTClassOwnsSelector(cls, @selector(dataTaskWithRequest:))) RPTInstallHookOnClass(cls, @selector(dataTaskWithRequest:), (IMP)RPTSessionDataRequest);
            if (RPTClassOwnsSelector(cls, @selector(dataTaskWithRequest:completionHandler:))) RPTInstallHookOnClass(cls, @selector(dataTaskWithRequest:completionHandler:), (IMP)RPTSessionDataRequestCompletion);
        }
        if (RPTClassOwnsSelector(cls, dataSelector)) RPTInstallHookOnClass(cls, dataSelector, (IMP)RPTDelegateDidReceiveData);
        if (RPTClassOwnsSelector(cls, responseSelector)) RPTInstallHookOnClass(cls, responseSelector, (IMP)RPTDelegateDidReceiveResponse);
        if (RPTClassOwnsSelector(cls, completeSelector)) RPTInstallHookOnClass(cls, completeSelector, (IMP)RPTDelegateDidComplete);
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
