Ppa Dev Tools
=============

ppa is a command line client for managing PPAs in Launchpad.

This primarily focuses on functionality needed by owners of PPAs, to
assist in their creation, deletion, and configuration.  A key
functionality is to poll and wait until the package(s) in the PPA have
completed building; this permits blocking on the builds to delay other
actions such as requesting users on a bug report to test the PPA, or
submitting a merge proposal for the update to be considered for
inclusion in the distro.

You can view a team's registered PPAs using 'ppa list'.


Usage
-----

Register a new PPA

```
$ ppa create my-ppa
PPA 'my-ppa' created for the following architectures:

   i386, amd64, armel, armhf, ppc64el, s390x, arm64, powerpc

The PPA can be viewed at:

   https://launchpad.net/~my-name/+archive/ubuntu/my-ppa

You can upload packages to this PPA using:

   dput ppa:my-name/my-ppa <source.changes>
```

Upload a package to the PPA

```
$ dput ppa:my-name/my-ppa some-package.changes
```

Wait until all packages in the PPA have finished building

```
$ ppa wait my-ppa
```

Set the public description for a PPA from a file

```
$ cat some-package/README | ppa desc ppa:my-name/my-ppa
```

Delete the PPA

```
$ ppa destroy my-ppa
```
