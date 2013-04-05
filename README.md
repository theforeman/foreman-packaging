deb packaging branches
======================

The Debian/Ubuntu packaging files are kept here. They use a branch structure, one
branch per repo:

deb/[repo-type]

The files (within the branch) are in:

debian/[os]/[packagename]

Contributing
============

Changes are only merged down from `nightly` (i.e nightly -> rc -> stable), so please
send patches to the [nightly](https://github.com/theforeman/foreman-rpms/tree/deb/nightly) branch.
