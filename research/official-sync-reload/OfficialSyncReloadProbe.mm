#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>
#import <QuartzCore/QuartzCore.h>
#import <objc/runtime.h>
#import <dlfcn.h>

static NSString * const OSRProbeVersion = @"0.1";
static NSString * const OSRExpectedBundleID = @"com.openai.chat";
static NSString * const OSRExpectedVersion = @"1.2026.202";
static NSString * const OSRExpectedBuild = @"30140022279";
static const char *OSRRootClassName = "_TtC23ChatGPTConversationRoot25ConversationRootViewModel";
static const char *OSRConversationClassName = "_TtC19ChatGPTConversation21ConversationViewModel";

static __weak id OSRRootViewModel;
static __weak id OSRConversationViewModel;
static UIButton *OSRButton;

static void OSRRunInspection(void);
static void OSRPresentResult(void);
static void OSRInstallButton(void);

@interface OSRProbeBootstrap : NSObject
+ (void)handleButtonTap:(id)sender;
@end

static NSString *OSRLogPath(void) {
    NSString *directory = NSSearchPathForDirectoriesInDomains(NSCachesDirectory, NSUserDomainMask, YES).firstObject ?: NSTemporaryDirectory();
    return [directory stringByAppendingPathComponent:@"DEV-official-sync-reload-v01.txt"];
}

static void OSRWriteLog(NSString *format, ...) NS_FORMAT_FUNCTION(1,2);
static void OSRWriteLog(NSString *format, ...) {
    va_list args;
    va_start(args, format);
    NSString *message = [[NSString alloc] initWithFormat:format arguments:args];
    va_end(args);
    NSString *line = [NSString stringWithFormat:@"%@ %@\n", [NSDate date], message];
    NSString *path = OSRLogPath();
    NSFileManager *manager = NSFileManager.defaultManager;
    if (![manager fileExistsAtPath:path]) [manager createFileAtPath:path contents:nil attributes:nil];
    NSFileHandle *handle = [NSFileHandle fileHandleForWritingAtPath:path];
    if (handle) {
        [handle seekToEndOfFile];
        [handle writeData:[line dataUsingEncoding:NSUTF8StringEncoding]];
        [handle closeFile];
    }
    NSLog(@"[OfficialSyncReload] %@", message);
}

static BOOL OSRExactBuildGate(void) {
    NSBundle *bundle = NSBundle.mainBundle;
    NSString *bundleID = bundle.bundleIdentifier ?: @"";
    NSString *version = [bundle objectForInfoDictionaryKey:@"CFBundleShortVersionString"] ?: @"";
    NSString *build = [bundle objectForInfoDictionaryKey:@"CFBundleVersion"] ?: @"";
    BOOL exact = [bundleID isEqualToString:OSRExpectedBundleID] && [version isEqualToString:OSRExpectedVersion] && [build isEqualToString:OSRExpectedBuild];
    OSRWriteLog(@"probe=%@ bundle=%@ version=%@ build=%@ exactBuild=%@", OSRProbeVersion, bundleID, version, build, exact ? @"YES" : @"NO");
    return exact;
}

static NSString *OSRImageDescriptionForIMP(IMP imp) {
    if (!imp) return @"imp=nil";
    Dl_info info = {0};
    if (!dladdr((const void *)imp, &info) || !info.dli_fbase) return [NSString stringWithFormat:@"imp=%p image=unknown", imp];
    uintptr_t offset = (uintptr_t)imp - (uintptr_t)info.dli_fbase;
    NSString *path = info.dli_fname ? [NSString stringWithUTF8String:info.dli_fname] : @"unknown";
    return [NSString stringWithFormat:@"imp=%p image=%@ offset=0x%llx", imp, path.lastPathComponent, (unsigned long long)offset];
}

static void OSRDumpMethods(Class cls, BOOL classMethods) {
    if (!cls) return;
    Class owner = classMethods ? object_getClass(cls) : cls;
    unsigned int count = 0;
    Method *methods = class_copyMethodList(owner, &count);
    OSRWriteLog(@"%@ %@ methods=%u", NSStringFromClass(cls), classMethods ? @"class" : @"instance", count);
    for (unsigned int i = 0; i < count; i++) {
        SEL selector = method_getName(methods[i]);
        const char *types = method_getTypeEncoding(methods[i]);
        IMP imp = method_getImplementation(methods[i]);
        OSRWriteLog(@"method %@ %s types=%s %@", classMethods ? @"+" : @"-", sel_getName(selector), types ?: "", OSRImageDescriptionForIMP(imp));
    }
    free(methods);
}

static void OSRDumpIvars(Class cls) {
    if (!cls) return;
    for (Class current = cls; current && current != NSObject.class; current = class_getSuperclass(current)) {
        unsigned int count = 0;
        Ivar *ivars = class_copyIvarList(current, &count);
        OSRWriteLog(@"%@ ivars=%u", NSStringFromClass(current), count);
        for (unsigned int i = 0; i < count; i++) {
            const char *name = ivar_getName(ivars[i]);
            const char *type = ivar_getTypeEncoding(ivars[i]);
            ptrdiff_t offset = ivar_getOffset(ivars[i]);
            OSRWriteLog(@"ivar %s type=%s offset=0x%tx", name ?: "", type ?: "", offset);
        }
        free(ivars);
    }
}

static BOOL OSRShouldSkipObject(id object) {
    if (!object) return YES;
    return [object isKindOfClass:UIView.class] || [object isKindOfClass:CALayer.class] || [object isKindOfClass:UIImage.class] || [object isKindOfClass:UIColor.class] || [object isKindOfClass:NSString.class] || [object isKindOfClass:NSNumber.class] || [object isKindOfClass:NSData.class];
}

static void OSRScanObject(id object, NSUInteger depth, NSMutableSet<NSValue *> *visited, NSUInteger *visitedCount, Class rootClass, Class conversationClass) {
    if (!object || depth > 8 || *visitedCount >= 6000) return;
    NSValue *identity = [NSValue valueWithPointer:(__bridge const void *)object];
    if ([visited containsObject:identity]) return;
    [visited addObject:identity];
    (*visitedCount)++;

    if (rootClass && [object isKindOfClass:rootClass]) {
        OSRRootViewModel = object;
        OSRWriteLog(@"LIVE rootVM=%p class=%@", object, NSStringFromClass(object_getClass(object)));
        Ivar conversationIvar = class_getInstanceVariable(rootClass, "$__lazy_storage_$_conversationViewModel");
        if (conversationIvar) {
            @try {
                id conversation = object_getIvar(object, conversationIvar);
                if (conversation) {
                    OSRConversationViewModel = conversation;
                    OSRWriteLog(@"LIVE rootVM.conversationViewModel=%p class=%@", conversation, NSStringFromClass(object_getClass(conversation)));
                } else {
                    OSRWriteLog(@"LIVE rootVM.conversationViewModel=nil");
                }
            } @catch (NSException *exception) {
                OSRWriteLog(@"root conversation ivar exception=%@", exception.name);
            }
        }
    }
    if (conversationClass && [object isKindOfClass:conversationClass]) {
        OSRConversationViewModel = object;
        OSRWriteLog(@"LIVE conversationVM=%p class=%@", object, NSStringFromClass(object_getClass(object)));
    }

    if ([object isKindOfClass:UIViewController.class]) {
        UIViewController *controller = object;
        OSRScanObject(controller.presentedViewController, depth + 1, visited, visitedCount, rootClass, conversationClass);
        for (UIViewController *child in controller.childViewControllers) OSRScanObject(child, depth + 1, visited, visitedCount, rootClass, conversationClass);
        if ([controller isKindOfClass:UINavigationController.class]) {
            for (UIViewController *child in ((UINavigationController *)controller).viewControllers) OSRScanObject(child, depth + 1, visited, visitedCount, rootClass, conversationClass);
        } else if ([controller isKindOfClass:UITabBarController.class]) {
            for (UIViewController *child in ((UITabBarController *)controller).viewControllers) OSRScanObject(child, depth + 1, visited, visitedCount, rootClass, conversationClass);
        } else if ([controller isKindOfClass:UISplitViewController.class]) {
            for (UIViewController *child in ((UISplitViewController *)controller).viewControllers) OSRScanObject(child, depth + 1, visited, visitedCount, rootClass, conversationClass);
        }
    }

    if ([object isKindOfClass:NSArray.class]) {
        NSUInteger limit = MIN(((NSArray *)object).count, (NSUInteger)100);
        for (NSUInteger i = 0; i < limit; i++) OSRScanObject(((NSArray *)object)[i], depth + 1, visited, visitedCount, rootClass, conversationClass);
        return;
    }
    if ([object isKindOfClass:NSDictionary.class]) {
        NSUInteger count = 0;
        for (id value in ((NSDictionary *)object).allValues) {
            if (count++ >= 100) break;
            OSRScanObject(value, depth + 1, visited, visitedCount, rootClass, conversationClass);
        }
        return;
    }
    if (OSRShouldSkipObject(object)) return;

    for (Class current = object_getClass(object); current && current != NSObject.class; current = class_getSuperclass(current)) {
        unsigned int count = 0;
        Ivar *ivars = class_copyIvarList(current, &count);
        for (unsigned int i = 0; i < count; i++) {
            const char *type = ivar_getTypeEncoding(ivars[i]);
            if (!type || type[0] != '@') continue;
            @try {
                id child = object_getIvar(object, ivars[i]);
                OSRScanObject(child, depth + 1, visited, visitedCount, rootClass, conversationClass);
            } @catch (__unused NSException *exception) {
            }
        }
        free(ivars);
    }
}

static NSArray<UIWindow *> *OSRApplicationWindows(void) {
    NSMutableArray<UIWindow *> *windows = [NSMutableArray array];
    UIApplication *application = UIApplication.sharedApplication;
    if (@available(iOS 13.0, *)) {
        for (UIScene *scene in application.connectedScenes) {
            if (![scene isKindOfClass:UIWindowScene.class]) continue;
            [windows addObjectsFromArray:((UIWindowScene *)scene).windows];
        }
    } else {
        [windows addObjectsFromArray:application.windows];
    }
    return windows;
}

static void OSRRunInspection(void) {
    Class rootClass = objc_getClass(OSRRootClassName);
    Class conversationClass = objc_getClass(OSRConversationClassName);
    OSRWriteLog(@"inspection begin rootClass=%p conversationClass=%p", rootClass, conversationClass);
    OSRDumpMethods(rootClass, NO);
    OSRDumpMethods(rootClass, YES);
    OSRDumpIvars(rootClass);
    OSRDumpMethods(conversationClass, NO);
    OSRDumpMethods(conversationClass, YES);
    OSRDumpIvars(conversationClass);

    OSRRootViewModel = nil;
    OSRConversationViewModel = nil;
    NSMutableSet<NSValue *> *visited = [NSMutableSet set];
    NSUInteger visitedCount = 0;
    OSRScanObject(UIApplication.sharedApplication.delegate, 0, visited, &visitedCount, rootClass, conversationClass);
    for (UIWindow *window in OSRApplicationWindows()) OSRScanObject(window.rootViewController, 0, visited, &visitedCount, rootClass, conversationClass);
    OSRWriteLog(@"inspection end visited=%lu rootFound=%@ conversationFound=%@", (unsigned long)visitedCount, OSRRootViewModel ? @"YES" : @"NO", OSRConversationViewModel ? @"YES" : @"NO");
}

static UIViewController *OSRTopViewController(UIViewController *controller) {
    if (!controller) return nil;
    if (controller.presentedViewController) return OSRTopViewController(controller.presentedViewController);
    if ([controller isKindOfClass:UINavigationController.class]) return OSRTopViewController(((UINavigationController *)controller).visibleViewController);
    if ([controller isKindOfClass:UITabBarController.class]) return OSRTopViewController(((UITabBarController *)controller).selectedViewController);
    return controller;
}

static UIViewController *OSRPresenter(void) {
    UIWindow *best = nil;
    for (UIWindow *window in OSRApplicationWindows()) {
        if (window.isHidden || window.alpha <= 0.0) continue;
        if (window.isKeyWindow) { best = window; break; }
        if (!best && window.windowLevel == UIWindowLevelNormal) best = window;
    }
    return OSRTopViewController(best.rootViewController);
}

static void OSRPresentResult(void) {
    UIViewController *presenter = OSRPresenter();
    if (!presenter) return;
    NSString *status = [NSString stringWithFormat:@"Root VM: %@\nConversation VM: %@\n\n本版本只做元数据/对象探测，不会触发同步或重载。", OSRRootViewModel ? @"已找到" : @"未找到", OSRConversationViewModel ? @"已找到" : @"未找到"];
    UIAlertController *alert = [UIAlertController alertControllerWithTitle:@"Sync / Reload Research v0.1" message:status preferredStyle:UIAlertControllerStyleAlert];
    [alert addAction:[UIAlertAction actionWithTitle:@"重新扫描" style:UIAlertActionStyleDefault handler:^(__unused UIAlertAction *action) { OSRRunInspection(); OSRPresentResult(); }]];
    [alert addAction:[UIAlertAction actionWithTitle:@"分享日志" style:UIAlertActionStyleDefault handler:^(__unused UIAlertAction *action) {
        NSURL *url = [NSURL fileURLWithPath:OSRLogPath()];
        UIActivityViewController *share = [[UIActivityViewController alloc] initWithActivityItems:@[url] applicationActivities:nil];
        [OSRPresenter() presentViewController:share animated:YES completion:nil];
    }]];
    [alert addAction:[UIAlertAction actionWithTitle:@"关闭" style:UIAlertActionStyleCancel handler:nil]];
    [presenter presentViewController:alert animated:YES completion:nil];
}

static void OSRInstallButton(void) {
    if (!OSRExactBuildGate()) return;
    UIWindow *targetWindow = nil;
    for (UIWindow *window in OSRApplicationWindows()) {
        if (window.isKeyWindow) { targetWindow = window; break; }
    }
    if (!targetWindow) return;
    if (OSRButton.superview == targetWindow) { [targetWindow bringSubviewToFront:OSRButton]; return; }
    [OSRButton removeFromSuperview];
    if (!OSRButton) {
        OSRButton = [UIButton buttonWithType:UIButtonTypeSystem];
        OSRButton.frame = CGRectMake(MAX(8.0, targetWindow.bounds.size.width - 54.0), MAX(8.0, targetWindow.safeAreaInsets.top + 4.0), 44.0, 32.0);
        OSRButton.autoresizingMask = UIViewAutoresizingFlexibleLeftMargin | UIViewAutoresizingFlexibleBottomMargin;
        OSRButton.backgroundColor = [UIColor colorWithWhite:0.12 alpha:0.82];
        OSRButton.layer.cornerRadius = 8.0;
        [OSRButton setTitle:@"SR" forState:UIControlStateNormal];
        [OSRButton setTitleColor:UIColor.whiteColor forState:UIControlStateNormal];
        OSRButton.titleLabel.font = [UIFont boldSystemFontOfSize:13.0];
        OSRButton.accessibilityIdentifier = @"DEV-official-sync-reload-v01";
        [OSRButton addTarget:OSRProbeBootstrap.class action:@selector(handleButtonTap:) forControlEvents:UIControlEventTouchUpInside];
    }
    [targetWindow addSubview:OSRButton];
    [targetWindow bringSubviewToFront:OSRButton];
    OSRWriteLog(@"SR button installed window=%p", targetWindow);
}

@implementation OSRProbeBootstrap
+ (void)load {
    dispatch_async(dispatch_get_main_queue(), ^{
        [[NSNotificationCenter defaultCenter] addObserverForName:UIApplicationDidBecomeActiveNotification object:nil queue:NSOperationQueue.mainQueue usingBlock:^(__unused NSNotification *note) { OSRInstallButton(); }];
        [[NSNotificationCenter defaultCenter] addObserverForName:UIWindowDidBecomeKeyNotification object:nil queue:NSOperationQueue.mainQueue usingBlock:^(__unused NSNotification *note) { OSRInstallButton(); }];
        OSRInstallButton();
    });
}

+ (void)handleButtonTap:(__unused id)sender {
    OSRRunInspection();
    OSRPresentResult();
}
@end
