# 0.2.0 Release #

This release adds a new 'tests' command that lists any pending or
waiting test runs against the PPA at autopackage.canonical.com.  This
functionality is integrated from Christian Ehrhardt's `lp-test-ppa`
tool[1], coupled with new test cases, code documentation, and
pylint/flake style improvements.  The new command is run like this:

    $ ppa tests ppa:my-name/my-ppa

The second major focus for this release was to refine and solidify the
packaging and installation process.  In addition to PyPI, this will be
packaged as a snap and as a debian package via PPA (of course!)

1: https://git.launchpad.net/~ubuntu-server/+git/ubuntu-helpers/tree/cpaelzer/lp-test-ppa



# 0.1.0 Release #

A core set of commands including create, destroy, wait, list, and show
are implemented, along with basic help and package docs.  The
intent of this release is to get registered with PyPI and scope out the
release process.

Here's an example set of commands one might use:

   $ ppa create my-ppa
   $ dput ppa:my-name/my-ppa some-package.changes
   $ ppa wait my-ppa
   $ cat some-package/README | ppa desc ppa:my-name/my-ppa
   $ ppa destroy my-ppa

This creates a PPA and uploads a package to it.  Then it waits for the
package to complete building and then updates the PPA's description with
some user-provided information.  At this point the PPA might be shared
with users or used for testing purposes.  Finally, when no longer needed
it is removed.
