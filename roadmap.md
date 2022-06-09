In order to plan for new updates of the Anbox Cloud software stack, this page gives you insight into the general release cycle and planned features for the next versions of Anbox Cloud. However don't consider the roadmap to be complete or set in stone.

## Release Cycle

Anbox Cloud follows a defined release cycle with frequent minor and patch releases.

#### Minor releases

A new minor release of Anbox Cloud is released every three months. It includes new features and bug fixes.

#### Patch releases

A patch release for Anbox Cloud is released at the beginning of every month and includes Android and Chrome security updates alongside Anbox Cloud specific bug fixes.

## Roadmap

### 1.14.1 (June 2022)

Target date: June 15, 2022

* Android security updates for June 2022
* Bug fixes

### 1.14.2 (July 2022)

Target date: July 13, 2022

* Android security updates for July 2022
* Bug fixes

### 1.15.0 (August 2022)

Target date: August 24, 2022

* Minimum TLS version of 1.3 for AMS

   [note type="information" status="Important"]
   With the new requirement, LXD images from Anbox Cloud versions prior to 1.15 will stop functioning. To ease transition, it will be possible to temporarily force the minimum TLS version back to 1.2.
   [/note]
* Extended Android CTS coverage
* Bidirectional out-of-band data exchange for WebRTC

### 1.16.0 (November 2022)

Target date: November 16, 2022

* LXD images for Android 13