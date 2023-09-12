Starting with Anbox Cloud 1.12, use the following new hooks instead of the deprecated ones:

* Use `pre-start` instead of `install` and `restore`
* Use `post-start` instead of `prepare`
* Use `post-stop` instead of `backup`

Be aware that the new hooks run for **all** container types. To execute a hook for only regular or only base containers, use the new `CONTAINER_TYPE` environment variable. This variable is set to either `base` or `regular`.

For example, if you want to execute a hook only when your application is bootstrapped, you can do the following:
```bash
if [ "$CONTAINER_TYPE" = "regular" ]; then
  exit 0
fi

# Rest of the code for your addon
```

[note type="caution" type="Warning"]Copying your existing addons without modifications might have unintended side effects, because your hooks will run for every container.[/note]
