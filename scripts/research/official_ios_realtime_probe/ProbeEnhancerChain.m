#import <Foundation/Foundation.h>
#import <dlfcn.h>

static NSString * const RPTOriginalEnhancerBackupName = @"ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.original.dylib";

// Load the package's pre-existing enhancer before the Probe installs its own NSURLSession hooks.
// This keeps the existing behavior and lets the Probe wrap the final method implementations.
__attribute__((constructor(101))) static void RPTLoadOriginalEnhancerIfPresent(void) {
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
