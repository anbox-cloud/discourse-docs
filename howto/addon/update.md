Updating an existing addon with a new version is possible with the following command:

```bash
amc addon update foo ./foo-addon
```
> **Note:**  Due to Snap strict confinement, the addon must be located in your home directory.

**AMS will update and create a new version for all applications that use this addon in the background.**
If the addon you are updating is used by many applications, you may experience increased load on your cluster
as AMS updates many applications simultaneously.