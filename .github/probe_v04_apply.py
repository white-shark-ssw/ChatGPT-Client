from pathlib import Path

SOURCE = Path('scripts/research/official_ios_realtime_probe/ChatGPTRealtimeProbe.m')
README = Path('scripts/research/official_ios_realtime_probe/README.md')


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 match, got {count}')
    return text.replace(old, new, 1)

s = SOURCE.read_text()
s = replace_once(s, 'static NSString * const RPTProbeVersion = @"0.3";', 'static NSString * const RPTProbeVersion = @"0.4";', 'version')
s = replace_once(s, 'static char RPTWebSocketReceiveErrorLoggedKey;\n', 'static char RPTWebSocketReceiveErrorLoggedKey;\nstatic char RPTTaskResumeLoggedKey;\n', 'resume-associated-key')

insert_anchor = '''static void RPTInstallSessionHooks(void) {\n    int count = objc_getClassList(NULL, 0);\n'''
insert_block = '''static BOOL RPTShouldObserveTaskURL(NSURL *url) {\n    if (!url) return NO;\n    NSString *host = url.host.lowercaseString ?: @"";\n    if ([host isEqualToString:@"chatgpt.com"] || [host isEqualToString:@"chat.openai.com"] || [host isEqualToString:@"ios.chat.openai.com"] || [host isEqualToString:@"api.openai.com"]) return YES;\n    if ([host hasSuffix:@".chatgpt.com"] || [host hasSuffix:@".openai.com"]) return YES;\n    return RPTShouldObserveURL(url);\n}\n\nstatic void RPTTaskResume(id self, SEL _cmd) {\n    NSURLSessionTask *task = (NSURLSessionTask *)self;\n    NSURLRequest *request = task.currentRequest ?: task.originalRequest;\n    if (request.URL && RPTShouldObserveTaskURL(request.URL) && !objc_getAssociatedObject(self, &RPTTaskResumeLoggedKey)) {\n        objc_setAssociatedObject(self, &RPTTaskResumeLoggedKey, @YES, OBJC_ASSOCIATION_RETAIN_NONATOMIC);\n        NSMutableDictionary *fields = RPTRequestFields(request);\n        fields[@"taskClass"] = NSStringFromClass(object_getClass(self)) ?: @"";\n        RPTWriteEvent(@"http.task.resume", fields);\n    }\n    IMP original = RPTOriginalIMP(self, _cmd);\n    if (!original) return;\n    void (*function)(id, SEL) = (void *)original;\n    function(self, _cmd);\n}\n\nstatic void RPTInstallSessionHooks(void) {\n    int count = objc_getClassList(NULL, 0);\n'''
s = replace_once(s, insert_anchor, insert_block, 'resume-function-insert')

old_classes = '''    Class sessionClass = NSURLSession.class;\n    SEL responseSelector = NSSelectorFromString(@"URLSession:dataTask:didReceiveResponse:completionHandler:");\n'''
new_classes = '''    Class sessionClass = NSURLSession.class;\n    Class taskClass = NSURLSessionTask.class;\n    SEL responseSelector = NSSelectorFromString(@"URLSession:dataTask:didReceiveResponse:completionHandler:");\n'''
s = replace_once(s, old_classes, new_classes, 'task-class')

old_loop = '''    for (int i = 0; i < count; i++) {\n        Class cls = classes[i];\n        if (RPTIsSubclassOfClass(cls, sessionClass)) {\n'''
new_loop = '''    for (int i = 0; i < count; i++) {\n        Class cls = classes[i];\n        if (RPTIsSubclassOfClass(cls, taskClass) && RPTClassOwnsSelector(cls, @selector(resume))) RPTInstallHookOnClass(cls, @selector(resume), (IMP)RPTTaskResume);\n        if (RPTIsSubclassOfClass(cls, sessionClass)) {\n'''
s = replace_once(s, old_loop, new_loop, 'resume-hook-install')
SOURCE.write_text(s)

r = README.read_text()
r = replace_once(r, 'Current research revision: **Probe v0.3**.', 'Current research revision: **Probe v0.4**.', 'readme-version')
r = replace_once(r, '- URLSession conversation/realtime observations cover both request-based and URL-based data-task constructors.\n', '- URLSession conversation/realtime observations cover both request-based and URL-based data-task constructors.\n- one privacy-safe `http.task.resume` event is emitted per observed NSURLSession task, including tasks created internally by Swift async `URLSession.data(for:)` / `bytes(for:)` paths; no task body or auth material is logged.\n', 'readme-resume-bullet')
r = replace_once(r, 'Probe v0.3 also verifies that a failed user socket no longer expands the research log into a per-receive error storm.', 'Probe v0.4 keeps the v0.3 WebSocket error de-duplication and adds task-resume observation so Swift async URLSession acquisition cannot bypass the probe merely by avoiding public data-task constructors.', 'readme-decisive')
README.write_text(r)
