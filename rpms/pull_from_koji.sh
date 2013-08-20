#!/bin/bash
#
# Our dependencies are built in koji, so use sfk to pull the spec files
# from the published SRPMs into git.
#
# https://github.com/skottler/spec-from-koji

koji=http://koji.katello.org
here=$(dirname $0)

sfk -h $koji \
  -t foreman-nightly-rhel6 \
  -t foreman-nightly-nonscl-rhel6 \
  -t foreman-plugins-1.2-rhel6 \
  -t foreman-plugins-nightly-rhel6 \
  -o $here/epel-6 -e ^foreman $*

sfk -h $koji \
  -t foreman-nightly-fedora18 \
  -t foreman-plugins-1.2-fedora18 \
  -t foreman-plugins-nightly-fedora18 \
  -o $here/fedora-18 -e ^foreman $*

sfk -h $koji \
  -t foreman-nightly-fedora19 \
  -t foreman-plugins-1.2-fedora19 \
  -t foreman-plugins-nightly-fedora19 \
  -o $here/fedora-19 -e ^foreman $*
