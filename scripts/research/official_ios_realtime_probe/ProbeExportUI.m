#import <UIKit/UIKit.h>

static NSString * const RPTUIProbeLogName = @"ChatGPTRealtimeProbe.jsonl";
static NSString * const RPTUIBatchLogName = @"ChatGPTRealtimeProbeBatch.jsonl";
static const NSInteger RPTUIProbeButtonTag = 0x52505431;
static const NSInteger RPTUIClearButtonTag = 0x52505432;

extern void RPTClearLog(void);
extern void RPTBatchClearLog(void);

static NSString *RPTUILogPath(NSString *name) {
    NSString *documents = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES).firstObject ?: NSTemporaryDirectory();
    return [documents stringByAppendingPathComponent:name];
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
- (void)clearButtonTapped:(UIButton *)button;
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

        UIButton *clearButton = [UIButton buttonWithType:UIButtonTypeSystem];
        clearButton.tag = RPTUIClearButtonTag;
        clearButton.translatesAutoresizingMaskIntoConstraints = NO;
        clearButton.accessibilityIdentifier = @"ChatGPTRealtimeProbe.Clear";
        [clearButton setTitle:@"清空" forState:UIControlStateNormal];
        [clearButton setTitleColor:UIColor.whiteColor forState:UIControlStateNormal];
        clearButton.titleLabel.font = [UIFont systemFontOfSize:12.0 weight:UIFontWeightSemibold];
        clearButton.backgroundColor = UIColor.systemRedColor;
        clearButton.layer.cornerRadius = 8.0;
        [clearButton addTarget:self action:@selector(clearButtonTapped:) forControlEvents:UIControlEventTouchUpInside];

        [window addSubview:button];
        [window addSubview:clearButton];
        [NSLayoutConstraint activateConstraints:@[
            [button.trailingAnchor constraintEqualToAnchor:window.safeAreaLayoutGuide.trailingAnchor constant:-8.0],
            [button.topAnchor constraintEqualToAnchor:window.safeAreaLayoutGuide.topAnchor constant:8.0],
            [button.widthAnchor constraintEqualToConstant:58.0],
            [button.heightAnchor constraintEqualToConstant:34.0],
            [clearButton.trailingAnchor constraintEqualToAnchor:button.leadingAnchor constant:-6.0],
            [clearButton.centerYAnchor constraintEqualToAnchor:button.centerYAnchor],
            [clearButton.widthAnchor constraintEqualToConstant:58.0],
            [clearButton.heightAnchor constraintEqualToConstant:34.0]
        ]];
        [window bringSubviewToFront:clearButton];
        [window bringSubviewToFront:button];
        NSLog(@"[ChatGPTRealtimeProbe] export UI ready");
    });
}

- (void)probeButtonTapped:(UIButton *)button {
    UIViewController *presenter = RPTUITopViewController(RPTUIActiveWindow().rootViewController);
    if (!presenter) return;
    NSFileManager *manager = NSFileManager.defaultManager;
    NSMutableArray<NSURL *> *urls = [NSMutableArray array];
    NSString *basePath = RPTUILogPath(RPTUIProbeLogName);
    NSString *batchPath = RPTUILogPath(RPTUIBatchLogName);
    if ([manager fileExistsAtPath:basePath]) [urls addObject:[NSURL fileURLWithPath:basePath]];
    if ([manager fileExistsAtPath:batchPath]) [urls addObject:[NSURL fileURLWithPath:batchPath]];
    if (!urls.count) {
        UIAlertController *alert = [UIAlertController alertControllerWithTitle:@"Probe 日志尚未生成" message:@"请确认 Probe 已成功注入并完全重启 ChatGPT。" preferredStyle:UIAlertControllerStyleAlert];
        [alert addAction:[UIAlertAction actionWithTitle:@"好" style:UIAlertActionStyleDefault handler:nil]];
        [presenter presentViewController:alert animated:YES completion:nil];
        return;
    }
    UIActivityViewController *activity = [[UIActivityViewController alloc] initWithActivityItems:urls applicationActivities:nil];
    activity.popoverPresentationController.sourceView = button;
    activity.popoverPresentationController.sourceRect = button.bounds;
    [presenter presentViewController:activity animated:YES completion:nil];
}

- (void)clearButtonTapped:(UIButton *)button {
    UIViewController *presenter = RPTUITopViewController(RPTUIActiveWindow().rootViewController);
    if (!presenter) return;
    UIAlertController *alert = [UIAlertController alertControllerWithTitle:@"清空 Probe 日志？" message:@"会同时清空基础日志和综合诊断日志，只保留下一轮测试事件。" preferredStyle:UIAlertControllerStyleAlert];
    [alert addAction:[UIAlertAction actionWithTitle:@"取消" style:UIAlertActionStyleCancel handler:nil]];
    [alert addAction:[UIAlertAction actionWithTitle:@"清空" style:UIAlertActionStyleDestructive handler:^(__unused UIAlertAction *action) {
        RPTClearLog();
        RPTBatchClearLog();
        UIAlertController *done = [UIAlertController alertControllerWithTitle:@"已清空" message:@"下一轮两份 Probe 日志都已从新的起点开始。" preferredStyle:UIAlertControllerStyleAlert];
        [done addAction:[UIAlertAction actionWithTitle:@"好" style:UIAlertActionStyleDefault handler:nil]];
        [presenter presentViewController:done animated:YES completion:nil];
    }]];
    alert.popoverPresentationController.sourceView = button;
    alert.popoverPresentationController.sourceRect = button.bounds;
    [presenter presentViewController:alert animated:YES completion:nil];
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
