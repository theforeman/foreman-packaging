foreman-packaging
=================
This git repo contains rpm and deb build files, patches, gem2rpm templates, and
other stuff that might be useful for building packages of Foreman and its
dependencies.

RPM packaging branches
======================
The rpm/\* branches contain the spec files for Foreman, related projects and its
dependencies.  Pull requests gladly accepted for these.  rpm/develop is the first
and best place to make changes, as it's branched for each release.

Koji's repos are built using the files under comps/, new packages and
dependencies must be added here.

Debian packaging branches
=========================

The deb/\* branches contain the Debian packaging files for Foreman and its
dependencies. The repo mirrors [Foreman Core](https://github.com/theforeman/foreman),
i.e. deb/develop is for packaging branch 'develop', deb/1.3 is for packaging release
1.3.x and so on

Contributing
============

It's generally best to contribute to `rpm/develop` or 'deb/develop' unless something
is specifically broken for an older release. Please fork and send a PR.
