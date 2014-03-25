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
  -t foreman-plugins-1.3-rhel6 \
  -t foreman-plugins-1.4-rhel6 \
  -t foreman-plugins-nightly-rhel6 \
  -o $here/epel-6 \
  -e ^foreman \
  -e ^rubygem-hammer_cli \
  $*

sfk -h $koji \
  -t foreman-nightly-fedora19 \
  -t foreman-plugins-1.2-fedora19 \
  -t foreman-plugins-1.3-fedora19 \
  -t foreman-plugins-1.4-fedora19 \
  -t foreman-plugins-nightly-fedora19 \
  -o $here/fedora-19 \
  -e ^foreman \
  -e ^rubygem-hammer_cli \
  $*
