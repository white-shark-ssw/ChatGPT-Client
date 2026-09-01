#import <Foundation/Foundation.h>
#import <dlfcn.h>

static NSString * const RPTOriginalEnhancerBackupName = @"ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.original.dylib";

__attribute__((constructor)) static void RPTLoadOriginalEnhancerIfPresent(void) {
    @autoreleasepool {
        NSString *frameworks = NSBundle.mainBundle.privateFrameworksPath;
        if (!frameworks.length) return;
        NSString *path = [frameworks stringByAppendingPathComponent:RPTOriginalEnhancerBackupName];
        if (![NSFileManager.defaultManager fileExistsAtPath:path]) return;
        void *handle = dlopen(path.fileSystemRepresentation, RTLD_NOW | RTLD_LOCAL);
        if (handle) NSLog(@"[ChatGPTRealtimeProbe] original enhancer chained");
        else NSLog(@"[ChatGPTRealtimeProbe] original enhancer chain failed");
    }
}
