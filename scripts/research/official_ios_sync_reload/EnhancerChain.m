#import <Foundation/Foundation.h>
#import <dlfcn.h>

static NSString * const SROriginalEnhancerBackupName = @"ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.original.dylib";

__attribute__((constructor(101))) static void SRLoadOriginalEnhancerIfPresent(void) {
    @autoreleasepool {
        NSString *frameworks = NSBundle.mainBundle.privateFrameworksPath;
        if (!frameworks.length) return;
        NSString *path = [frameworks stringByAppendingPathComponent:SROriginalEnhancerBackupName];
        if (![NSFileManager.defaultManager fileExistsAtPath:path]) return;
        void *handle = dlopen(path.fileSystemRepresentation, RTLD_NOW | RTLD_LOCAL);
        if (handle) NSLog(@"[ChatGPTSyncReloadInspector] original enhancer chained");
        else NSLog(@"[ChatGPTSyncReloadInspector] original enhancer chain failed");
    }
}
