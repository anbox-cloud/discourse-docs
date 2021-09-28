Starting with 1.12, the following hooks are deprecated and should be replaced:

- `installed` should be replaced by `pre-start`
- `prepare` should be replaced by `post-start`
- `restore` should be replaced by `pre-start`
- `backup` should be replaced by `post-stop`

Be aware that the new hooks are **run no matter the container type**. To only execute a hook for regular or
base containers, a new `CONTAINER_TYPE` environment variable is made available. This variable can be set to either
`base` or `regular`.

If you want to execute a hook only when your application is bootstrapped, you can do the following
```bash
if [ "$CONTAINER_TYPE" = "regular" ]; then
  exit 0
fi

# Rest of the code for your addon
```

**Warning**: Copying your exising addons without modifications may have unintended side effects as your hooks
will run for every container.
