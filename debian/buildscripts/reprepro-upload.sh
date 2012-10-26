#!/bin/bash

# Script to sign and upload finished debs to reprepro
# Assumes root perms (use sudo) and that the deb/changes files are in .

COMPONENT="$1"
DISTRO="$2"
DEB_PATH="$3"

cd $3

export GNUPGHOME=/root/foreman-reprepro/.gnupg
dpkg-sig -k E775FF07 --sign builder *changes

# TODO: fix this - can't rebuild packages at the moment (without manual intervention)
# reprepro -b /root/foreman-reprepro -C stable remove squeeze foreman-proxy
reprepro -b /root/foreman-reprepro -C $COMPONENT includedeb $DISTRO *deb

# Push to shell.theforeman.org
# Relies on ssh keys being set up
rsync -av /root/foreman-reprepro/ greg@shell.theforeman.org:deb.theforeman.org/html/
