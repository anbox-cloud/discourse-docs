You may want to use the same addon for all your applications.

When your addon is created, run the following command

```bash
amc config set application.addons foo,bar
```
This will add the `foo` and `bar` addons to all your new and existing applications
(ams will automatically update existing applications).

Global addons will be added to application specific addons.

> **Warning**: addons can delay the start of your applications, keep them light.
