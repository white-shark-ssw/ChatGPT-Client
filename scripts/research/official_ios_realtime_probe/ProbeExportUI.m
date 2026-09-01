#import <UIKit/UIKit.h>

static NSString * const RPTUIProbeLogName = @"ChatGPTRealtimeProbe.jsonl";
static const NSInteger RPTUIProbeButtonTag = 0x52505431;

static NSString *RPTUILogPath(void) {
    NSString *documents = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES).firstObject ?: NSTemporaryDirectory();
    return [documents stringByAppendingPathComponent:RPTUIProbeLogName];
}

static UIWindow *RPTUIActiveWindow(void) {
    UIApplication *application = UIApplication.sharedApplication;
    for (UIScene *scene in application.connectedScenes) {
        if (![scene isKindOfClass:[UIWindowScene class]] || scene.activationState != UISceneActivationStateForegroundActive) continue;
        UIWindowScene *windowScene = (UIWindowScene *)scene;
        for (UIWindow *window in windowScene.windows) if (window.isKeyWindow) return window;
        for (UIWindow *window in windowScene.windows) if (!window.hidden && window.alpha > 0.0) return window;
    }
    return application.windows.firstObject;
}

static UIViewController *RPTUITopViewController(UIViewController *controller) {
    if (!controller) return nil;
    if (controller.presentedViewController && !controller.presentedViewController.isBeingDismissed) return RPTUITopViewController(controller.presentedViewController);
    if ([controller isKindOfClass:[UINavigationController class]]) return RPTUITopViewController(((UINavigationController *)controller).visibleViewController);
    if ([controller isKindOfClass:[UITabBarController class]]) return RPTUITopViewController(((UITabBarController *)controller).selectedViewController);
    return controller;
}

@interface RPTProbeExportTarget : NSObject
+ (instancetype)shared;
- (void)attachIfPossible;
- (void)probeButtonTapped:(UIButton *)button;
@end

@implementation RPTProbeExportTarget

+ (instancetype)shared {
    static RPTProbeExportTarget *target;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{ target = [RPTProbeExportTarget new]; });
    return target;
}

- (void)attachIfPossible {
    dispatch_async(dispatch_get_main_queue(), ^{
        UIWindow *window = RPTUIActiveWindow();
        if (!window || [window viewWithTag:RPTUIProbeButtonTag]) return;

        UIButton *button = [UIButton buttonWithType:UIButtonTypeSystem];
        button.tag = RPTUIProbeButtonTag;
        button.translatesAutoresizingMaskIntoConstraints = NO;
        button.accessibilityIdentifier = @"ChatGPTRealtimeProbe.Export";
        [button setTitle:@"Probe" forState:UIControlStateNormal];
        [button setTitleColor:UIColor.whiteColor forState:UIControlStateNormal];
        button.titleLabel.font = [UIFont systemFontOfSize:12.0 weight:UIFontWeightSemibold];
        button.backgroundColor = UIColor.systemBlueColor;
        button.layer.cornerRadius = 8.0;
        button.layer.shadowColor = UIColor.blackColor.CGColor;
        button.layer.shadowOpacity = 0.18;
        button.layer.shadowRadius = 3.0;
        button.layer.shadowOffset = CGSizeMake(0.0, 1.0);
        [button addTarget:self action:@selector(probeButtonTapped:) forControlEvents:UIControlEventTouchUpInside];
        [window addSubview:button];
        [NSLayoutConstraint activateConstraints:@[
            [button.trailingAnchor constraintEqualToAnchor:window.safeAreaLayoutGuide.trailingAnchor constant:-8.0],
            [button.topAnchor constraintEqualToAnchor:window.safeAreaLayoutGuide.topAnchor constant:8.0],
            [button.widthAnchor constraintEqualToConstant:58.0],
            [button.heightAnchor constraintEqualToConstant:34.0]
        ]];
        [window bringSubviewToFront:button];
        NSLog(@"[ChatGPTRealtimeProbe] export UI ready");
    });
}

- (void)probeButtonTapped:(UIButton *)button {
    NSString *path = RPTUILogPath();
    UIViewController *presenter = RPTUITopViewController(RPTUIActiveWindow().rootViewController);
    if (!presenter) return;

    if (![NSFileManager.defaultManager fileExistsAtPath:path]) {
        UIAlertController *alert = [UIAlertController alertControllerWithTitle:@"Probe 日志尚未生成" message:@"请确认 Probe 已成功注入并完全重启 ChatGPT。" preferredStyle:UIAlertControllerStyleAlert];
        [alert addAction:[UIAlertAction actionWithTitle:@"好" style:UIAlertActionStyleDefault handler:nil]];
        [presenter presentViewController:alert animated:YES completion:nil];
        return;
    }

    NSURL *url = [NSURL fileURLWithPath:path];
    UIActivityViewController *activity = [[UIActivityViewController alloc] initWithActivityItems:@[url] applicationActivities:nil];
    activity.popoverPresentationController.sourceView = button;
    activity.popoverPresentationController.sourceRect = button.bounds;
    [presenter presentViewController:activity animated:YES completion:nil];
}

@end

__attribute__((constructor)) static void RPTUIInitialize(void) {
    dispatch_async(dispatch_get_main_queue(), ^{
        RPTProbeExportTarget *target = RPTProbeExportTarget.shared;
        NSNotificationCenter *center = NSNotificationCenter.defaultCenter;
        [center addObserver:target selector:@selector(attachIfPossible) name:UIApplicationDidBecomeActiveNotification object:nil];
        [center addObserver:target selector:@selector(attachIfPossible) name:UIWindowDidBecomeVisibleNotification object:nil];
        dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(1.0 * NSEC_PER_SEC)), dispatch_get_main_queue(), ^{ [target attachIfPossible]; });
    });
}
