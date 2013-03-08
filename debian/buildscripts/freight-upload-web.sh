#!/bin/bash

set -x

# Script to copy the newly-built debs to the web node for signing and promoting

# Dependencies
# * the freight::client class in foreman-infra
# * the web node (server2) must have the freight class applied

COMPONENT="$1"
DISTRO="$2"
DEB_PATH="$3"

# The path is important, as freight_rsync (which is run on the web node for incoming
# transfers) will parse the path to figure out the repo to send debs to.
TARGET_PATH="freight@server2.theforeman.org:rsync_cache/$DISTRO/$COMPONENT/"

# Export this to avoid quoting issues
export RSYNC_RSH="ssh -i /var/lib/workspace/workspace/ssh_key_freight"

/usr/bin/rsync -avPx $DEB_PATH/*deb $TARGET_PATH
