foreman-rpms
============
This git repo contains rpm and deb build files, patches, gem2rpm templates, and
other stuff that might be useful for building packages of Foreman and its
dependencies.

RPMs
====
Spec files and patches are stored under `rpms/` for EL and Fedora releases.

PRs should be made to `master`.

Debian
======
The Debian and Ubuntu packaging files are kept here too (despite the name).
They reside on the `deb/{nightly,rc,stable}` branches and changes are merged
between them.

PRs should be made to `deb/nightly`.

Installer
=========
The build script for the Foreman installer RPM and deb packages is stored under
`fpm/`.

Packaging PRs should be made to `master`.  Installer changes should be made to
the submodules via the foreman-installer repo.

SELinux
=======
An SELinux module for the targeted policy is stored under `rpms/selinux`.

PRs should be made to `master`.
