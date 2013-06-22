foreman-rpms
============
This git repo contains rpm and deb build files, patches, gem2rpm templates, and
other stuff that might be useful for building packages of Foreman and its
dependencies.

RPMs
====
RPMs are built using the files in the foreman repo itself.

Debian
======
The Debian and Ubuntu packaging files are kept here too (despite the name).
They reside on the `deb/{nightly,rc,stable}` branches and changes are merged
between them.

PRs should be made to `deb/nightly`.

Installer
=========
The build script for the Foreman installer deb packages is stored under `fpm/`.

RPMs are built using the files in the foreman-installer repo itself.

Packaging PRs should be made to `master`.  Installer changes should be made to
the submodules via the foreman-installer repo.

SELinux
=======
The SELinux module has moved to [foreman-selinux](https://github.com/theforeman/foreman-selinux/).
