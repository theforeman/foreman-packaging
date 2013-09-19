foreman-packaging
=================
This git repo contains rpm and deb build files, patches, gem2rpm templates, and
other stuff that might be useful for building packages of Foreman and its
dependencies.

RPMs
====
Foreman RPMs are built using the files in the foreman repo itself, same for
related subprojects.

Dependencies are built using the spec files found under rpms/ in this repo.
Pull requests gladly accepted for these to the `master` branch.

Koji's repos are built using the files under comps/, new packages and
dependencies must be added here.

Debian Packaging Branches
=========================

The deb/\* branches contain the Debian packaging files for Foreman and it's
dependencies. The repo mirrors [Foreman Core](https://github.com/theforeman/foreman),
i.e. deb/develop is for packaging branch 'develop', deb/1.3 is for packaging release
1.3.x and so on

Contributing to the debs
========================

It's generally best to contribute to 'deb/develop' unless something is specifically
broken for an older release. Please fork and send a PR.

SELinux
=======
The SELinux module has moved to [foreman-selinux](https://github.com/theforeman/foreman-selinux/).
