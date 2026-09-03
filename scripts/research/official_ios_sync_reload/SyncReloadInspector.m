#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>
#import <objc/runtime.h>

static NSString * const SRProbeVersion = @"0.1";
static NSString * const SRLogName = @"ChatGPTSyncReloadInspector.jsonl";
static dispatch_queue_t SRLogQueue;

NSString *SRLogPath(void) {
    NSString *documents = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES).firstObject ?: NSTemporaryDirectory();
    return [documents stringByAppendingPathComponent:SRLogName];
}

static NSString *SRNow(void) {
    static NSISO8601DateFormatter *formatter;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{ formatter = [NSISO8601DateFormatter new]; formatter.formatOptions = NSISO8601DateFormatWithInternetDateTime | NSISO8601DateFormatWithFractionalSeconds; });
    return [formatter stringFromDate:[NSDate date]];
}

static void SRAppendRecord(NSDictionary *record) {
    if (![NSJSONSerialization isValidJSONObject:record]) return;
    NSData *json = [NSJSONSerialization dataWithJSONObject:record options:0 error:nil];
    if (!json) return;
    NSMutableData *line = [json mutableCopy];
    [line appendData:[@"\n" dataUsingEncoding:NSUTF8StringEncoding]];
    NSString *path = SRLogPath();
    dispatch_async(SRLogQueue, ^{
        if (![NSFileManager.defaultManager fileExistsAtPath:path]) [NSFileManager.defaultManager createFileAtPath:path contents:nil attributes:nil];
        NSFileHandle *handle = [NSFileHandle fileHandleForWritingAtPath:path];
        if (!handle) return;
        @try { [handle seekToEndOfFile]; [handle writeData:line]; [handle synchronizeFile]; }
        @catch (__unused NSException *exception) {}
        @finally { [handle closeFile]; }
    });
}

void SRLog(NSString *event, NSDictionary *payload) {
    NSMutableDictionary *record = [@{ @"ts": SRNow(), @"probeVersion": SRProbeVersion, @"event": event ?: @"unknown" } mutableCopy];
    if (payload) [record addEntriesFromDictionary:payload];
    SRAppendRecord(record);
}

void SRClearLog(void) {
    dispatch_sync(SRLogQueue, ^{
        NSString *path = SRLogPath();
        [NSFileManager.defaultManager removeItemAtPath:path error:nil];
        [NSFileManager.defaultManager createFileAtPath:path contents:nil attributes:nil];
    });
    SRLog(@"inspector.log_cleared", nil);
}

static NSString *SRString(const char *value) {
    return value ? [NSString stringWithUTF8String:value] : @"";
}

static BOOL SRNameLooksRelevant(NSString *name) {
    NSString *lower = name.lowercaseString;
    NSArray<NSString *> *needles = @[ @"refresh", @"reload", @"fetch", @"conversation", @"current", @"poll", @"resume", @"sync", @"repository", @"coordinator", @"appear", @"load" ];
    for (NSString *needle in needles) if ([lower containsString:needle]) return YES;
    return NO;
}

static NSArray<NSDictionary *> *SRMethodList(Class cls, BOOL classMethods) {
    if (!cls) return @[];
    Class target = classMethods ? object_getClass(cls) : cls;
    unsigned int count = 0;
    Method *methods = class_copyMethodList(target, &count);
    NSMutableArray<NSDictionary *> *all = [NSMutableArray array];
    NSMutableArray<NSDictionary *> *relevant = [NSMutableArray array];
    for (unsigned int index = 0; index < count; index++) {
        NSString *selector = NSStringFromSelector(method_getName(methods[index])) ?: @"";
        NSDictionary *entry = @{ @"selector": selector, @"types": SRString(method_getTypeEncoding(methods[index])) };
        if (all.count < 200) [all addObject:entry];
        if (SRNameLooksRelevant(selector) && relevant.count < 200) [relevant addObject:entry];
    }
    free(methods);
    return @[ @{ @"declaredCount": @(count), @"declared": all, @"relevant": relevant } ];
}

static NSArray<NSDictionary *> *SRPropertyList(Class cls) {
    if (!cls) return @[];
    unsigned int count = 0;
    objc_property_t *properties = class_copyPropertyList(cls, &count);
    NSMutableArray<NSDictionary *> *items = [NSMutableArray array];
    for (unsigned int index = 0; index < count && items.count < 200; index++) {
        NSString *name = SRString(property_getName(properties[index]));
        [items addObject:@{ @"name": name, @"attributes": SRString(property_getAttributes(properties[index])), @"relevant": @(SRNameLooksRelevant(name)) }];
    }
    free(properties);
    return items;
}

static NSArray<NSDictionary *> *SRIvarList(Class cls) {
    if (!cls) return @[];
    unsigned int count = 0;
    Ivar *ivars = class_copyIvarList(cls, &count);
    NSMutableArray<NSDictionary *> *items = [NSMutableArray array];
    for (unsigned int index = 0; index < count && items.count < 200; index++) {
        NSString *name = SRString(ivar_getName(ivars[index]));
        [items addObject:@{ @"name": name, @"type": SRString(ivar_getTypeEncoding(ivars[index])), @"offset": @(ivar_getOffset(ivars[index])), @"relevant": @(SRNameLooksRelevant(name)) }];
    }
    free(ivars);
    return items;
}

static Class SRResolveClass(NSArray<NSString *> *names, NSString **resolvedName) {
    for (NSString *name in names) {
        Class cls = NSClassFromString(name);
        if (!cls) cls = objc_getClass(name.UTF8String);
        if (cls) { if (resolvedName) *resolvedName = NSStringFromClass(cls) ?: name; return cls; }
    }
    return Nil;
}

static NSDictionary *SRInspectCandidate(NSString *logicalName, NSArray<NSString *> *runtimeNames) {
    NSString *resolvedName = nil;
    Class cls = SRResolveClass(runtimeNames, &resolvedName);
    if (!cls) return @{ @"logical": logicalName, @"available": @NO, @"requestedNames": runtimeNames };
    NSArray *instanceMethods = SRMethodList(cls, NO);
    NSArray *classMethods = SRMethodList(cls, YES);
    return @{
        @"logical": logicalName,
        @"available": @YES,
        @"requestedNames": runtimeNames,
        @"resolvedName": resolvedName ?: @"",
        @"superclass": class_getSuperclass(cls) ? NSStringFromClass(class_getSuperclass(cls)) ?: @"" : @"",
        @"instanceSize": @(class_getInstanceSize(cls)),
        @"instanceMethods": instanceMethods.firstObject ?: @{},
        @"classMethods": classMethods.firstObject ?: @{},
        @"properties": SRPropertyList(cls),
        @"ivars": SRIvarList(cls)
    };
}

static NSArray<NSString *> *SRLoadedRelevantClasses(void) {
    int count = objc_getClassList(NULL, 0);
    if (count <= 0) return @[];
    Class *classes = (__unsafe_unretained Class *)calloc((size_t)count, sizeof(Class));
    count = objc_getClassList(classes, count);
    NSMutableArray<NSString *> *names = [NSMutableArray array];
    for (int index = 0; index < count && names.count < 300; index++) {
        NSString *name = NSStringFromClass(classes[index]) ?: @"";
        NSString *lower = name.lowercaseString;
        if ([lower containsString:@"conversation"] || [lower containsString:@"historyviewcontroller"] || [lower containsString:@"pollingmanager"]) [names addObject:name];
    }
    free(classes);
    [names sortUsingSelector:@selector(compare:)];
    return names;
}

static UIWindow *SRActiveWindow(void) {
    UIApplication *application = UIApplication.sharedApplication;
    for (UIScene *scene in application.connectedScenes) {
        if (![scene isKindOfClass:[UIWindowScene class]] || scene.activationState != UISceneActivationStateForegroundActive) continue;
        UIWindowScene *windowScene = (UIWindowScene *)scene;
        for (UIWindow *window in windowScene.windows) if (window.isKeyWindow) return window;
        for (UIWindow *window in windowScene.windows) if (!window.hidden && window.alpha > 0.0) return window;
    }
    return application.windows.firstObject;
}

static void SRCollectController(UIViewController *controller, NSMutableArray<NSString *> *classes, NSInteger depth) {
    if (!controller || depth > 10 || classes.count >= 120) return;
    [classes addObject:NSStringFromClass(controller.class) ?: @""];
    if (controller.presentedViewController && !controller.presentedViewController.isBeingDismissed) SRCollectController(controller.presentedViewController, classes, depth + 1);
    if ([controller isKindOfClass:[UINavigationController class]]) SRCollectController(((UINavigationController *)controller).visibleViewController, classes, depth + 1);
    if ([controller isKindOfClass:[UITabBarController class]]) SRCollectController(((UITabBarController *)controller).selectedViewController, classes, depth + 1);
    for (UIViewController *child in controller.childViewControllers) SRCollectController(child, classes, depth + 1);
}

static void SRCollectViewClasses(UIView *view, NSMutableArray<NSString *> *classes, NSUInteger *visited) {
    if (!view || *visited >= 800 || classes.count >= 200) return;
    (*visited)++;
    NSString *name = NSStringFromClass(view.class) ?: @"";
    NSString *lower = name.lowercaseString;
    if ([lower containsString:@"conversation"] || [lower containsString:@"history"] || [lower containsString:@"hosting"] || [lower containsString:@"navigation"] || [lower containsString:@"chatgpt"]) [classes addObject:name];
    for (UIView *child in view.subviews) SRCollectViewClasses(child, classes, visited);
}

NSDictionary *SRInspectRuntime(void) {
    NSArray<NSDictionary *> *specs = @[
        @{ @"logical": @"ConversationViewModel", @"names": @[ @"ChatGPTConversation.ConversationViewModel", @"_TtC19ChatGPTConversation21ConversationViewModel" ] },
        @{ @"logical": @"HistoryViewController", @"names": @[ @"ChatGPTHistory.HistoryViewController", @"_TtC14ChatGPTHistory21HistoryViewController" ] },
        @{ @"logical": @"DefaultConversationRepository", @"names": @[ @"Conversations.DefaultConversationRepository", @"_TtC13Conversations29DefaultConversationRepository" ] },
        @{ @"logical": @"DefaultConversationCoordinatorProvider", @"names": @[ @"Conversations.DefaultConversationCoordinatorProvider", @"_TtC13Conversations38DefaultConversationCoordinatorProvider" ] },
        @{ @"logical": @"ConversationPollingManager", @"names": @[ @"Conversations.ConversationPollingManager", @"_TtC13Conversations26ConversationPollingManager" ] }
    ];
    NSMutableArray<NSDictionary *> *candidates = [NSMutableArray array];
    NSInteger availableCount = 0;
    for (NSDictionary *spec in specs) {
        NSDictionary *result = SRInspectCandidate(spec[@"logical"], spec[@"names"]);
        [candidates addObject:result];
        if ([result[@"available"] boolValue]) availableCount++;
    }

    UIWindow *window = SRActiveWindow();
    NSMutableArray<NSString *> *controllerClasses = [NSMutableArray array];
    if (window.rootViewController) SRCollectController(window.rootViewController, controllerClasses, 0);
    NSMutableArray<NSString *> *viewClasses = [NSMutableArray array];
    NSUInteger visited = 0;
    if (window) SRCollectViewClasses(window, viewClasses, &visited);

    NSDictionary *summary = @{
        @"availableCandidateCount": @(availableCount),
        @"candidateCount": @(specs.count),
        @"keyWindowClass": window ? NSStringFromClass(window.class) ?: @"" : @"",
        @"controllerClasses": controllerClasses,
        @"matchingViewClasses": viewClasses,
        @"viewCountVisited": @(visited),
        @"loadedRelevantClasses": SRLoadedRelevantClasses()
    };
    SRLog(@"inspector.runtime_snapshot", @{ @"summary": summary, @"candidates": candidates });
    return summary;
}

__attribute__((constructor)) static void SRInspectorInitialize(void) {
    SRLogQueue = dispatch_queue_create("com.openai.research.sync-reload-inspector.log", DISPATCH_QUEUE_SERIAL);
    SRLog(@"inspector.loaded", @{ @"binary": @"ChatGPTSyncReloadInspector" });
}
