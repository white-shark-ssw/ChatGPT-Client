#import <UIKit/UIKit.h>

extern NSString *SRLogPath(void);
extern void SRClearLog(void);
extern NSDictionary *SRInspectRuntime(void);

static const NSInteger SRButtonTag = 0x53523031;

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

static UIViewController *SRTopViewController(UIViewController *controller) {
    if (!controller) return nil;
    if (controller.presentedViewController && !controller.presentedViewController.isBeingDismissed) return SRTopViewController(controller.presentedViewController);
    if ([controller isKindOfClass:[UINavigationController class]]) return SRTopViewController(((UINavigationController *)controller).visibleViewController);
    if ([controller isKindOfClass:[UITabBarController class]]) return SRTopViewController(((UITabBarController *)controller).selectedViewController);
    return controller;
}

@interface SRInspectorTarget : NSObject
+ (instancetype)shared;
- (void)attachIfPossible;
- (void)buttonTapped:(UIButton *)button;
@end

@implementation SRInspectorTarget

+ (instancetype)shared {
    static SRInspectorTarget *target;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{ target = [SRInspectorTarget new]; });
    return target;
}

- (void)attachIfPossible {
    dispatch_async(dispatch_get_main_queue(), ^{
        UIWindow *window = SRActiveWindow();
        if (!window || [window viewWithTag:SRButtonTag]) return;

        UIButton *button = [UIButton buttonWithType:UIButtonTypeSystem];
        button.tag = SRButtonTag;
        button.translatesAutoresizingMaskIntoConstraints = NO;
        button.accessibilityIdentifier = @"ChatGPTSyncReloadInspector.Button";
        [button setTitle:@"SR" forState:UIControlStateNormal];
        [button setTitleColor:UIColor.whiteColor forState:UIControlStateNormal];
        button.titleLabel.font = [UIFont systemFontOfSize:12.0 weight:UIFontWeightBold];
        button.backgroundColor = UIColor.systemIndigoColor;
        button.layer.cornerRadius = 9.0;
        button.layer.shadowColor = UIColor.blackColor.CGColor;
        button.layer.shadowOpacity = 0.18;
        button.layer.shadowRadius = 3.0;
        button.layer.shadowOffset = CGSizeMake(0.0, 1.0);
        [button addTarget:self action:@selector(buttonTapped:) forControlEvents:UIControlEventTouchUpInside];

        [window addSubview:button];
        [NSLayoutConstraint activateConstraints:@[
            [button.trailingAnchor constraintEqualToAnchor:window.safeAreaLayoutGuide.trailingAnchor constant:-8.0],
            [button.topAnchor constraintEqualToAnchor:window.safeAreaLayoutGuide.topAnchor constant:8.0],
            [button.widthAnchor constraintEqualToConstant:42.0],
            [button.heightAnchor constraintEqualToConstant:34.0]
        ]];
        [window bringSubviewToFront:button];
    });
}

- (void)buttonTapped:(UIButton *)button {
    UIViewController *presenter = SRTopViewController(SRActiveWindow().rootViewController);
    if (!presenter) return;

    UIAlertController *menu = [UIAlertController alertControllerWithTitle:@"Sync / Reload Inspector" message:@"v0.1 只检查官方运行时结构，不会触发同步、重载或网络请求。" preferredStyle:UIAlertControllerStyleActionSheet];
    [menu addAction:[UIAlertAction actionWithTitle:@"检查运行时" style:UIAlertActionStyleDefault handler:^(__unused UIAlertAction *action) {
        NSDictionary *summary = SRInspectRuntime();
        NSString *message = [NSString stringWithFormat:@"候选类 %@/%@ 可见；遍历视图 %@ 个。请导出日志供分析。", summary[@"availableCandidateCount"] ?: @0, summary[@"candidateCount"] ?: @0, summary[@"viewCountVisited"] ?: @0];
        UIAlertController *done = [UIAlertController alertControllerWithTitle:@"检查完成" message:message preferredStyle:UIAlertControllerStyleAlert];
        [done addAction:[UIAlertAction actionWithTitle:@"好" style:UIAlertActionStyleDefault handler:nil]];
        [presenter presentViewController:done animated:YES completion:nil];
    }]];
    [menu addAction:[UIAlertAction actionWithTitle:@"导出日志" style:UIAlertActionStyleDefault handler:^(__unused UIAlertAction *action) {
        NSString *path = SRLogPath();
        if (![NSFileManager.defaultManager fileExistsAtPath:path]) {
            UIAlertController *alert = [UIAlertController alertControllerWithTitle:@"暂无日志" message:@"请先运行一次“检查运行时”。" preferredStyle:UIAlertControllerStyleAlert];
            [alert addAction:[UIAlertAction actionWithTitle:@"好" style:UIAlertActionStyleDefault handler:nil]];
            [presenter presentViewController:alert animated:YES completion:nil];
            return;
        }
        UIActivityViewController *activity = [[UIActivityViewController alloc] initWithActivityItems:@[[NSURL fileURLWithPath:path]] applicationActivities:nil];
        activity.popoverPresentationController.sourceView = button;
        activity.popoverPresentationController.sourceRect = button.bounds;
        [presenter presentViewController:activity animated:YES completion:nil];
    }]];
    [menu addAction:[UIAlertAction actionWithTitle:@"清空日志" style:UIAlertActionStyleDestructive handler:^(__unused UIAlertAction *action) {
        SRClearLog();
        UIAlertController *done = [UIAlertController alertControllerWithTitle:@"已清空" message:@"下一次检查将从新的日志起点开始。" preferredStyle:UIAlertControllerStyleAlert];
        [done addAction:[UIAlertAction actionWithTitle:@"好" style:UIAlertActionStyleDefault handler:nil]];
        [presenter presentViewController:done animated:YES completion:nil];
    }]];
    [menu addAction:[UIAlertAction actionWithTitle:@"取消" style:UIAlertActionStyleCancel handler:nil]];
    menu.popoverPresentationController.sourceView = button;
    menu.popoverPresentationController.sourceRect = button.bounds;
    [presenter presentViewController:menu animated:YES completion:nil];
}

@end

__attribute__((constructor)) static void SRUIInitialize(void) {
    dispatch_async(dispatch_get_main_queue(), ^{
        SRInspectorTarget *target = SRInspectorTarget.shared;
        NSNotificationCenter *center = NSNotificationCenter.defaultCenter;
        [center addObserver:target selector:@selector(attachIfPossible) name:UIApplicationDidBecomeActiveNotification object:nil];
        [center addObserver:target selector:@selector(attachIfPossible) name:UIWindowDidBecomeVisibleNotification object:nil];
        dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(1.0 * NSEC_PER_SEC)), dispatch_get_main_queue(), ^{ [target attachIfPossible]; });
    });
}
