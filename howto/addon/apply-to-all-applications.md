To enable an addon for an application, you must add it to the [application manifest](https://discourse.ubuntu.com/t/application-manifest/24197).

However, if you want to use the same addon or addons for all your applications, you can enable them globally. To do so, run the following command after creating your addons:

```bash
amc config set application.addons foo,bar
```

This command adds the `foo` and `bar` addons to all your new and existing applications. AMS will automatically update existing applications.

If you define both global addons and application-specific addons, applications will use both.

[note type="caution" status="Warning"]Addons can delay the start of your applications. Therefore, keep them light.[/note]
