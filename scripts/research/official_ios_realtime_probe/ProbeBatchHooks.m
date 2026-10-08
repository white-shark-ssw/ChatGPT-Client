#import <Foundation/Foundation.h>
#import <dispatch/dispatch.h>
#import <objc/runtime.h>
#import <CommonCrypto/CommonDigest.h>

static NSString * const RPTBatchVersion = @"0.8";
static NSString * const RPTBatchLogName = @"ChatGPTRealtimeProbeBatch.jsonl";
static const NSUInteger RPTBatchTailBytes = 512;
static const NSUInteger RPTBatchCallbackLogCap = 40;

static dispatch_queue_t RPTBatchLogQueue;
static NSMutableSet<NSString *> *RPTBatchHookedKeys;
static NSMutableDictionary<NSString *, NSValue *> *RPTBatchOriginalIMPs;
static NSMutableSet<NSString *> *RPTBatchSkippedSurfaces;
static char RPTBatchCallbackSequenceKey;
static char RPTBatchCallbackCountsKey;

static NSString *RPTBatchTimestamp(void) {
    static NSISO8601DateFormatter *formatter;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{ formatter = [NSISO8601DateFormatter new]; formatter.formatOptions = NSISO8601DateFormatWithInternetDateTime | NSISO8601DateFormatWithFractionalSeconds; });
    return [formatter stringFromDate:[NSDate date]];
}

static NSString *RPTBatchLogPath(void) {
    NSString *documents = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES).firstObject ?: NSTemporaryDirectory();
    return [documents stringByAppendingPathComponent:RPTBatchLogName];
}

static void RPTBatchWriteEvent(NSString *name, NSDictionary *fields) {
    if (!name.length) return;
    NSMutableDictionary *event = [NSMutableDictionary dictionaryWithDictionary:fields ?: @{}];
    event[@"ts"] = RPTBatchTimestamp();
    event[@"event"] = name;
    event[@"probeVersion"] = RPTBatchVersion;
    dispatch_async(RPTBatchLogQueue, ^{
        if (![NSJSONSerialization isValidJSONObject:event]) return;
        NSData *json = [NSJSONSerialization dataWithJSONObject:event options:0 error:nil];
        if (!json) return;
        NSMutableData *line = [json mutableCopy];
        [line appendData:[@"\n" dataUsingEncoding:NSUTF8StringEncoding]];
        NSString *path = RPTBatchLogPath();
        NSFileManager *manager = NSFileManager.defaultManager;
        if (![manager fileExistsAtPath:path]) [manager createFileAtPath:path contents:nil attributes:nil];
        NSFileHandle *handle = [NSFileHandle fileHandleForWritingAtPath:path];
        if (!handle) return;
        @try { [handle seekToEndOfFile]; [handle writeData:line]; } @catch (__unused NSException *exception) {}
        [handle closeFile];
        NSLog(@"[ChatGPTRealtimeProbeBatch] %@", name);
    });
}

void RPTBatchClearLog(void) {
    if (!RPTBatchLogQueue) return;
    dispatch_sync(RPTBatchLogQueue, ^{ [[NSFileManager defaultManager] removeItemAtPath:RPTBatchLogPath() error:nil]; });
    RPTBatchWriteEvent(@"batch.log_cleared", @{});
}

static NSArray<NSString *> *RPTBatchPathParts(NSString *path) {
    NSMutableArray<NSString *> *parts = [NSMutableArray array];
    for (NSString *part in [path componentsSeparatedByString:@"/"]) if (part.length) [parts addObject:part];
    return parts;
}

static BOOL RPTBatchIsConversationDetailURL(NSURL *url) {
    NSArray<NSString *> *parts = RPTBatchPathParts(url.path ?: @"");
    return parts.count >= 3 && [parts[0] isEqualToString:@"backend-api"] && [parts[1] isEqualToString:@"conversation"] && !([parts count] >= 4 && [parts[3] isEqualToString:@"stream_status"]);
}

static NSString *RPTBatchHashString(NSString *value) {
    NSData *data = [value dataUsingEncoding:NSUTF8StringEncoding] ?: [NSData data];
    unsigned char digest[CC_SHA256_DIGEST_LENGTH];
    CC_SHA256(data.bytes, (CC_LONG)data.length, digest);
    NSMutableString *result = [NSMutableString stringWithCapacity:12];
    for (NSUInteger i = 0; i < 6; i++) [result appendFormat:@"%02x", digest[i]];
    return result;
}

static NSString *RPTBatchConversationHash(NSURL *url) {
    NSArray<NSString *> *parts = RPTBatchPathParts(url.path ?: @"");
    return parts.count >= 3 ? RPTBatchHashString(parts[2]) : @"";
}

static NSMutableDictionary *RPTBatchTaskFields(NSURLSessionTask *task) {
    NSURLRequest *request = task.currentRequest ?: task.originalRequest;
    NSMutableDictionary *fields = [NSMutableDictionary dictionary];
    fields[@"taskClass"] = NSStringFromClass(object_getClass(task)) ?: @"";
    fields[@"method"] = request.HTTPMethod ?: @"GET";
    fields[@"host"] = request.URL.host ?: @"";
    fields[@"pathKind"] = @"conversation_detail";
    NSString *conversationHash = RPTBatchConversationHash(request.URL);
    if (conversationHash.length) fields[@"conversationHash"] = conversationHash;
    NSHTTPURLResponse *response = [task.response isKindOfClass:[NSHTTPURLResponse class]] ? (id)task.response : nil;
    if (response) fields[@"status"] = @(response.statusCode);
    if (task.response.MIMEType.length) fields[@"mimeType"] = task.response.MIMEType.lowercaseString;
    if (task.response.expectedContentLength >= 0) fields[@"expectedContentLength"] = @(task.response.expectedContentLength);
    return fields;
}

static BOOL RPTBatchIsTargetTask(NSURLSessionTask *task) {
    NSURLRequest *request = task.currentRequest ?: task.originalRequest;
    return task && RPTBatchIsConversationDetailURL(request.URL);
}

static NSString *RPTBatchSafeToken(NSString *value) {
    if (![value isKindOfClass:[NSString class]]) return @"";
    NSString *token = value.lowercaseString;
    if (token.length == 0 || token.length > 64) return @"";
    NSCharacterSet *allowed = [NSCharacterSet characterSetWithCharactersInString:@"abcdefghijklmnopqrstuvwxyz0123456789._:-"];
    return [token rangeOfCharacterFromSet:allowed.invertedSet].location == NSNotFound ? token : @"";
}

static NSString *RPTBatchAsyncStatusToken(NSData *data, NSRange keyRange) {
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
        return RPTBatchSafeToken([window substringWithRange:NSMakeRange(start, end.location - start)]);
    }
    NSString *tail = [[window substringFromIndex:index] lowercaseString];
    if ([tail hasPrefix:@"null"]) return @"null";
    return @"";
}

static void RPTBatchScanData(NSData *data, NSMutableData *tail, BOOL *keyPresent, NSString **status) {
    if (!data.length) return;
    NSData *key = [@"\"conversation_async_status\"" dataUsingEncoding:NSUTF8StringEncoding];
    NSRange range = [data rangeOfData:key options:0 range:NSMakeRange(0, data.length)];
    if (range.location != NSNotFound) {
        *keyPresent = YES;
        NSString *candidate = RPTBatchAsyncStatusToken(data, range);
        if (candidate.length) *status = candidate;
    }
    if (tail.length) {
        NSUInteger prefixLength = MIN(RPTBatchTailBytes, data.length);
        NSMutableData *boundary = [tail mutableCopy];
        [boundary appendData:[data subdataWithRange:NSMakeRange(0, prefixLength)]];
        NSRange boundaryRange = [boundary rangeOfData:key options:0 range:NSMakeRange(0, boundary.length)];
        if (boundaryRange.location != NSNotFound) {
            *keyPresent = YES;
            NSString *candidate = RPTBatchAsyncStatusToken(boundary, boundaryRange);
            if (candidate.length) *status = candidate;
        }
    }
    if (data.length >= RPTBatchTailBytes) {
        [tail setData:[data subdataWithRange:NSMakeRange(data.length - RPTBatchTailBytes, RPTBatchTailBytes)]];
    } else {
        [tail appendData:data];
        if (tail.length > RPTBatchTailBytes) [tail replaceBytesInRange:NSMakeRange(0, tail.length - RPTBatchTailBytes) withBytes:NULL length:0];
    }
}

static NSDictionary *RPTBatchDispatchSummary(dispatch_data_t dispatchData) {
    if (!dispatchData) return @{ @"present": @NO };
    __block NSUInteger regionCount = 0;
    __block NSString *leadingClass = @"empty";
    __block BOOL leadingFound = NO;
    __block BOOL keyPresent = NO;
    __block NSString *status = @"";
    NSMutableData *tail = [NSMutableData data];
    dispatch_data_apply(dispatchData, ^bool(__unused dispatch_data_t region, __unused size_t offset, const void *buffer, size_t size) {
        regionCount += 1;
        if (!buffer || size == 0) return true;
        const unsigned char *bytes = buffer;
        if (!leadingFound) {
            for (size_t i = 0; i < size; i++) {
                unsigned char c = bytes[i];
                if (c == ' ' || c == '\n' || c == '\r' || c == '\t') continue;
                leadingFound = YES;
                leadingClass = c == '{' ? @"object" : (c == '[' ? @"array" : @"other");
                break;
            }
        }
        NSData *chunk = [NSData dataWithBytesNoCopy:(void *)buffer length:size freeWhenDone:NO];
        RPTBatchScanData(chunk, tail, &keyPresent, &status);
        return true;
    });
    NSMutableDictionary *summary = [NSMutableDictionary dictionary];
    summary[@"present"] = @YES;
    summary[@"bytes"] = @(dispatch_data_get_size(dispatchData));
    summary[@"regionCount"] = @(regionCount);
    summary[@"leadingClass"] = leadingClass;
    summary[@"asyncStatusKeyPresent"] = @(keyPresent);
    if (status.length) summary[@"asyncStatus"] = status;
    return summary;
}

static BOOL RPTBatchLooksLikeDispatchData(id object) {
    if (!object) return NO;
    NSString *name = NSStringFromClass(object_getClass(object)).lowercaseString ?: @"";
    return [name containsString:@"dispatch_data"];
}

static Ivar RPTBatchFindIvar(Class cls, const char *name) {
    for (Class current = cls; current; current = class_getSuperclass(current)) {
        Ivar ivar = class_getInstanceVariable(current, name);
        if (ivar) return ivar;
    }
    return NULL;
}

static NSDictionary *RPTBatchInspectDispatchIvar(id object, const char *name) {
    Ivar ivar = RPTBatchFindIvar(object_getClass(object), name);
    if (!ivar) return @{ @"available": @NO };
    const char *rawType = ivar_getTypeEncoding(ivar);
    NSString *type = rawType ? [NSString stringWithUTF8String:rawType] ?: @"" : @"";
    NSMutableDictionary *result = [NSMutableDictionary dictionaryWithDictionary:@{ @"available": @YES, @"typeEncoding": type }];
    if (![type containsString:@"OS_dispatch_data"]) { result[@"typeMatched"] = @NO; return result; }
    result[@"typeMatched"] = @YES;
    id value = object_getIvar(object, ivar);
    if (!value) { result[@"present"] = @NO; return result; }
    result[@"objectClass"] = NSStringFromClass(object_getClass(value)) ?: @"";
    if (!RPTBatchLooksLikeDispatchData(value)) { result[@"present"] = @YES; result[@"dispatchClassMatched"] = @NO; return result; }
    [result addEntriesFromDictionary:RPTBatchDispatchSummary((dispatch_data_t)value)];
    result[@"dispatchClassMatched"] = @YES;
    return result;
}

static NSString *RPTBatchHookKey(Class cls, SEL selector) { return [NSString stringWithFormat:@"%p:%@", cls, NSStringFromSelector(selector)]; }

static IMP RPTBatchOriginalIMP(id object, SEL selector) {
    for (Class cls = object_getClass(object); cls; cls = class_getSuperclass(cls)) {
        NSValue *value = RPTBatchOriginalIMPs[RPTBatchHookKey(cls, selector)];
        if (value) return value.pointerValue;
    }
    return NULL;
}

static NSDictionary *RPTBatchRecordCallback(NSURLSessionTask *task, SEL selector, NSDictionary *extra) {
    if (!RPTBatchIsTargetTask(task)) return nil;
    NSMutableDictionary *fields = RPTBatchTaskFields(task);
    @synchronized (task) {
        NSNumber *sequenceValue = objc_getAssociatedObject(task, &RPTBatchCallbackSequenceKey);
        NSUInteger sequence = sequenceValue.unsignedIntegerValue + 1;
        objc_setAssociatedObject(task, &RPTBatchCallbackSequenceKey, @(sequence), OBJC_ASSOCIATION_RETAIN_NONATOMIC);
        NSMutableDictionary *counts = objc_getAssociatedObject(task, &RPTBatchCallbackCountsKey);
        if (!counts) { counts = [NSMutableDictionary dictionary]; objc_setAssociatedObject(task, &RPTBatchCallbackCountsKey, counts, OBJC_ASSOCIATION_RETAIN_NONATOMIC); }
        NSString *selectorName = NSStringFromSelector(selector) ?: @"";
        NSUInteger selectorCount = [counts[selectorName] unsignedIntegerValue] + 1;
        counts[selectorName] = @(selectorCount);
        fields[@"selector"] = selectorName;
        fields[@"callbackSequence"] = @(sequence);
        fields[@"selectorInvocationCount"] = @(selectorCount);
        fields[@"eventLogged"] = @(sequence <= RPTBatchCallbackLogCap);
        if (extra) [fields addEntriesFromDictionary:extra];
        if (sequence <= RPTBatchCallbackLogCap) RPTBatchWriteEvent(@"batch.conversation_detail.private_callback", fields);
    }
    return fields;
}

static void RPTBatchMaybeLogAsyncStatus(NSURLSessionTask *task, NSString *source, NSDictionary *summary) {
    if (![summary[@"asyncStatusKeyPresent"] boolValue]) return;
    NSMutableDictionary *fields = RPTBatchTaskFields(task);
    fields[@"source"] = source ?: @"";
    fields[@"asyncStatusKeyPresent"] = @YES;
    NSString *status = summary[@"asyncStatus"];
    if (status.length) fields[@"asyncStatus"] = status;
    RPTBatchWriteEvent(@"batch.conversation_detail.async_status", fields);
}

static void RPTBatchTaskDispatchData(id self, SEL _cmd, dispatch_data_t dispatchData, id completionHandler) {
    NSURLSessionTask *task = (NSURLSessionTask *)self;
    NSDictionary *summary = RPTBatchDispatchSummary(dispatchData);
    RPTBatchRecordCallback(task, _cmd, @{ @"dispatch": summary });
    RPTBatchMaybeLogAsyncStatus(task, NSStringFromSelector(_cmd), summary);
    IMP original = RPTBatchOriginalIMP(self, _cmd);
    if (!original) return;
    void (*function)(id, SEL, dispatch_data_t, id) = (void *)original;
    function(self, _cmd, dispatchData, completionHandler);
}

static void RPTBatchConnectionDidReceiveData(id self, SEL _cmd, id connection, id data, id completionHandler) {
    NSURLSessionTask *task = (NSURLSessionTask *)self;
    NSMutableDictionary *extra = [NSMutableDictionary dictionary];
    extra[@"connectionClass"] = connection ? NSStringFromClass(object_getClass(connection)) ?: @"" : @"null";
    extra[@"dataClass"] = data ? NSStringFromClass(object_getClass(data)) ?: @"" : @"null";
    if (RPTBatchLooksLikeDispatchData(data)) {
        NSDictionary *summary = RPTBatchDispatchSummary((dispatch_data_t)data);
        extra[@"dispatch"] = summary;
        RPTBatchMaybeLogAsyncStatus(task, NSStringFromSelector(_cmd), summary);
    }
    RPTBatchRecordCallback(task, _cmd, extra);
    IMP original = RPTBatchOriginalIMP(self, _cmd);
    if (!original) return;
    void (*function)(id, SEL, id, id, id) = (void *)original;
    function(self, _cmd, connection, data, completionHandler);
}

static void RPTBatchTaskFinish(id self, SEL _cmd, NSError *error) {
    NSURLSessionTask *task = (NSURLSessionTask *)self;
    if (RPTBatchIsTargetTask(task)) {
        NSDictionary *dataTaskData = RPTBatchInspectDispatchIvar(self, "_dataTaskData");
        NSDictionary *pending = RPTBatchInspectDispatchIvar(self, "_pendingResponseBytes");
        NSMutableDictionary *extra = [NSMutableDictionary dictionary];
        extra[@"dataTaskData"] = dataTaskData;
        extra[@"pendingResponseBytes"] = pending;
        NSMutableDictionary *counts = objc_getAssociatedObject(task, &RPTBatchCallbackCountsKey);
        if (counts) extra[@"callbackCounts"] = [counts copy];
        if (error) { extra[@"errorDomain"] = error.domain ?: @""; extra[@"errorCode"] = @(error.code); }
        RPTBatchRecordCallback(task, _cmd, extra);
        RPTBatchMaybeLogAsyncStatus(task, @"_dataTaskData", dataTaskData);
        RPTBatchMaybeLogAsyncStatus(task, @"_pendingResponseBytes", pending);
    }
    IMP original = RPTBatchOriginalIMP(self, _cmd);
    if (!original) return;
    void (*function)(id, SEL, NSError *) = (void *)original;
    function(self, _cmd, error);
}

static void RPTBatchLogSkippedSurface(Class cls, SEL selector, NSString *expected, NSString *actual) {
    NSString *key = [NSString stringWithFormat:@"%@:%@:%@", NSStringFromClass(cls) ?: @"", NSStringFromSelector(selector) ?: @"", actual ?: @""];
    @synchronized (RPTBatchSkippedSurfaces) {
        if ([RPTBatchSkippedSurfaces containsObject:key]) return;
        [RPTBatchSkippedSurfaces addObject:key];
    }
    RPTBatchWriteEvent(@"batch.private_surface_skipped", @{ @"class": NSStringFromClass(cls) ?: @"", @"selector": NSStringFromSelector(selector) ?: @"", @"expectedEncoding": expected ?: @"", @"actualEncoding": actual ?: @"" });
}

static BOOL RPTBatchInstallExactHook(Class cls, SEL selector, IMP replacement, NSString *expectedEncoding) {
    if (!cls || !selector || !replacement) return NO;
    NSString *key = RPTBatchHookKey(cls, selector);
    @synchronized (RPTBatchHookedKeys) { if ([RPTBatchHookedKeys containsObject:key]) return YES; }
    Method inherited = class_getInstanceMethod(cls, selector);
    if (!inherited) { RPTBatchLogSkippedSurface(cls, selector, expectedEncoding, @"missing"); return NO; }
    const char *rawTypes = method_getTypeEncoding(inherited);
    NSString *types = rawTypes ? [NSString stringWithUTF8String:rawTypes] ?: @"" : @"";
    if (![types isEqualToString:expectedEncoding]) { RPTBatchLogSkippedSurface(cls, selector, expectedEncoding, types); return NO; }
    IMP original = class_getMethodImplementation(cls, selector);
    if (class_addMethod(cls, selector, replacement, rawTypes)) RPTBatchOriginalIMPs[key] = [NSValue valueWithPointer:original];
    else {
        Method own = class_getInstanceMethod(cls, selector);
        IMP old = method_setImplementation(own, replacement);
        RPTBatchOriginalIMPs[key] = [NSValue valueWithPointer:old];
    }
    @synchronized (RPTBatchHookedKeys) { [RPTBatchHookedKeys addObject:key]; }
    return YES;
}

static void RPTBatchInstallPrivateHooksForTask(NSURLSessionTask *task) {
    if (!task) return;
    Class cls = object_getClass(task);
    NSMutableArray<NSString *> *installed = [NSMutableArray array];
    if (RPTBatchInstallExactHook(cls, NSSelectorFromString(@"_task_onqueue_didReceiveDispatchData:completionHandler:"), (IMP)RPTBatchTaskDispatchData, @"v32@0:8@16@?24")) [installed addObject:@"_task_onqueue_didReceiveDispatchData:completionHandler:"];
    if (RPTBatchInstallExactHook(cls, NSSelectorFromString(@"_onqueue_didReceiveDispatchData:completion:"), (IMP)RPTBatchTaskDispatchData, @"v32@0:8@16@?24")) [installed addObject:@"_onqueue_didReceiveDispatchData:completion:"];
    if (RPTBatchInstallExactHook(cls, NSSelectorFromString(@"_onqueue_didFinishWithError:"), (IMP)RPTBatchTaskFinish, @"v24@0:8@16")) [installed addObject:@"_onqueue_didFinishWithError:"];
    if (RPTBatchInstallExactHook(cls, NSSelectorFromString(@"connection:didReceiveData:completion:"), (IMP)RPTBatchConnectionDidReceiveData, @"v40@0:8@16@24@?32")) [installed addObject:@"connection:didReceiveData:completion:"];
    NSMutableDictionary *fields = RPTBatchTaskFields(task);
    fields[@"installedSelectors"] = installed;
    RPTBatchWriteEvent(@"batch.detail_task.instrumented", fields);
}

static void RPTBatchTaskResume(id self, SEL _cmd) {
    NSURLSessionTask *task = (NSURLSessionTask *)self;
    if (RPTBatchIsTargetTask(task)) RPTBatchInstallPrivateHooksForTask(task);
    IMP original = RPTBatchOriginalIMP(self, _cmd);
    if (!original) return;
    void (*function)(id, SEL) = (void *)original;
    function(self, _cmd);
}

static BOOL RPTBatchClassOwnsSelector(Class cls, SEL selector) {
    unsigned int count = 0;
    Method *methods = class_copyMethodList(cls, &count);
    BOOL owns = NO;
    for (unsigned int i = 0; i < count; i++) if (method_getName(methods[i]) == selector) { owns = YES; break; }
    free(methods);
    return owns;
}

static BOOL RPTBatchIsTaskSubclass(Class cls) {
    for (Class current = cls; current; current = class_getSuperclass(current)) if (current == NSURLSessionTask.class) return YES;
    return NO;
}

static void RPTBatchInstallResumeHooks(void) {
    int count = objc_getClassList(NULL, 0);
    if (count <= 0) return;
    Class *classes = (__unsafe_unretained Class *)calloc((size_t)count, sizeof(Class));
    count = objc_getClassList(classes, count);
    NSUInteger installed = 0;
    for (int i = 0; i < count; i++) {
        Class cls = classes[i];
        if (!RPTBatchIsTaskSubclass(cls) || !RPTBatchClassOwnsSelector(cls, @selector(resume))) continue;
        if (RPTBatchInstallExactHook(cls, @selector(resume), (IMP)RPTBatchTaskResume, @"v16@0:8")) installed += 1;
    }
    free(classes);
    RPTBatchWriteEvent(@"batch.hooks_installed", @{ @"resumeHookCount": @(installed) });
}

__attribute__((constructor(200))) static void RPTBatchInitialize(void) {
    @autoreleasepool {
        RPTBatchLogQueue = dispatch_queue_create("dev.chatgptclient.realtime-probe.batch-log", DISPATCH_QUEUE_SERIAL);
        RPTBatchHookedKeys = [NSMutableSet set];
        RPTBatchOriginalIMPs = [NSMutableDictionary dictionary];
        RPTBatchSkippedSurfaces = [NSMutableSet set];
        RPTBatchWriteEvent(@"batch.loaded", @{ @"bundleID": NSBundle.mainBundle.bundleIdentifier ?: @"", @"logFile": RPTBatchLogName });
        RPTBatchInstallResumeHooks();
    }
}
