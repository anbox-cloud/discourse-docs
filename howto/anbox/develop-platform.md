Anbox Cloud provides a platform SDK that allows the development of custom platform plugins for the Anbox runtime, if the [default platform](https://anbox-cloud.io/docs/ref/platforms) don't fit. For example when the integration with a custom streaming protocol is necessary a custom platform is required for integration with the Anbox runtime.

This guide assumes all steps are being run on a machine running Ubuntu 22.04 and hosting the [Anbox Cloud Appliance](https://discourse.ubuntu.com/t/install-appliance/22681).

## Preparation

A platform module must be built on the same version of Ubuntu as the Anbox runtime. This means if you're using one of the Anbox images based on Ubuntu 22.04 (for example, `jammy:android12:arm64`), you must build on Ubuntu 22.04.

In case that you're not running the [Anbox Cloud Appliance](https://discourse.ubuntu.com/t/install-appliance/22681) on an Ubuntu 22.04 system, you can build the platform on a separate system, e.g. in a LXD or docker container or another machine.

To get started you first need install the [Anbox Platform SDK](https://github.com/anbox-cloud/anbox-platform-sdk). Please follow the [instructions](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#anbox-platform-sdk) to complete this.

## Build example platform

The [Anbox Platform SDK](https://github.com/anbox-cloud/anbox-platform-sdk) comes with various examples that demonstrate different features. The following steps use the `minimal` example. Alternatively, choose the `nvidia` example if you're working with NVIDIA GPUs and want to see graphical output.

To build the `minimal` platform example, run the following commands:

    triplet=$(dpkg-architecture -qDEB_BUILD_MULTIARCH)
    cmake \
        -G Ninja \
        -B build \
        -DCMAKE_PREFIX_PATH=../../lib/anbox-platform-sdk/ \
        -DCMAKE_INSTALL_LIBDIR=lib/${triplet} \
        -DCMAKE_INSTALL_PREFIX=/usr examples/minimal/
    ninja -C build

As a result of the build process you will find a `platform_minimal.so` module in the `build` directory.

## Install example platform

[AMS](https://discourse.ubuntu.com/t/about-ams/24321) allows launching Anbox containers in a special [development mode](https://anbox-cloud.io/docs/exp/containers#dev-mode) which is meant for development tasks, specifically for addon or platform development. The Anbox runtime is instructed, when in [development mode](https://anbox-cloud.io/docs/exp/containers#dev-mode), not to terminate the container when it detects failures or other problems.

To try out the minimal platform, start a raw container with development mode turned on:

    amc launch --raw --devmode --instance-type=a4.3

If you choose the `nvidia` example, you must select an [instance type](https://discourse.ubuntu.com/t/instance-types/17764) that supports GPUs:

    amc launch --raw --devmode --instance-type=g4.3

The command will print out the ID of the container. Note down this ID; you will need it in the next step.

The start of the [raw container](https://discourse.ubuntu.com/t/managing-containers/17763#application-vs-raw) will take a moment as it will run through the full [bootstrap process](https://discourse.ubuntu.com/t/managing-applications/17760#bootstrap) before the container is ready to be used.

Once the container is fully up and running you can copy the `platform_minimal.so` module to it:

    id=<id of the container>
    triplet=$(dpkg-architecture -qDEB_BUILD_MULTIARCH)
    amc exec "${id}" mkdir "/usr/lib/${triplet}/anbox/platforms/minimal"
    lxc file push build/platform_minimal.so "ams-${id}/usr/lib/${triplet}/anbox/platforms/minimal/"

With the platform plugin present inside the container, you can now configure the Anbox runtime to make use of it. For that you have to change the `/var/lib/anbox/session.yaml` configuration file within the container:

    cat << EOF | amc exec "${id}" tee /var/lib/anbox/session.yaml
    log-level: debug
    platform: minimal
    EOF

This will rewrite the Anbox runtime configuration to use the new "minimal" platform instead of the default one.

As last step you have to restart Anbox inside the container

    amc exec "${id}" -- systemctl restart anbox

Once the Anbox runtime got restarted, you can verify from the container system log that it now uses the new "minimal" platform:

    amc logs "${id}"

Inside the log you will fine a line saying

    [ 2022-12-07 14:00:18] [anbox-session] [base_platform.cpp:34@create] Using platform 'minimal'

This shows that the platform was successfully loaded and is in use by Anbox.

When developing a new platform, you can also directly invoke the Anbox runtime rather than start it via `systemd`. For that, stop the `anbox.service` unit first:

    amc exec "${id}" -- systemctl stop anbox

Then start the Anbox runtime directly by running:

    amc exec "${id}" -- anbox-starter

When you want to stop Anbox, you can use CTRL+C to send it the signal to terminate.

## Package platform

In order to ship the platform to actual containers via AMS you have to create an [addon](https://discourse.ubuntu.com/t/managing-addons/17759) package which will install the platform into the container.

A very simple addon to install the created minimal platform looks as follows:

    mkdir hooks
    cat << EOF > hooks/pre-start
    #!/bin/sh -ex

    # Only run for base containers
    [ "$CONTAINER_TYPE" = "regular" ] && exit0

    # Install the platform plugin into the right location
    # NOTE: Please adjust the path for the right architecture you're targeting
    mkdir -p /usr/lib/aarch64-linux-gnu/anbox/platforms/minimal
    cp "$ADDON_DIR"/platform_minimal.so /usr/lib/aarch64-linux-gnu/anbox/platforms/minimal/
    EOF
    chmod +x hooks/pre-start
    tar cjf minimal-addon.tar.bz2 hooks platform_minimal.so

The addon can then be loaded into AMS and be used by applications and containers

    amc addon add minimal minimal-addon.tar.bz2

When launching a container you have to explicitly specifiy the platform the Anbox runtime inside the container should use with the `--platform` argument. If not specified Anbox will use its default. To launch a container with the minimal platform run

    amc launch --raw --addon minimal --platform minimal
