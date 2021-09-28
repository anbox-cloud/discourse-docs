You might want to have addons that perform translation on platforms that are not
natively supported by your application (running x86_64 applications on ARM for example).

You can add the top-level key  `provides`  to your addon manifest and list the architecture
it supports:

```yaml
name: my-addon
description: provides support for x86_64 architecture
provides:
  abi-support:
    - arm64-v8a
    - armeabi-v7a
```

This will tell AMS that an application can be scheduled on `arm64-v8a` and `armeabi-v7a` systems
even if no native support is detected in the APK.
