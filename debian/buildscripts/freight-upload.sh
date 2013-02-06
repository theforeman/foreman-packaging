#!/bin/bash

set -x

# Script to sign and upload finished debs using Freight
# Assumes jenkins can read the Foreman GPG key and rsync to the webserver

COMPONENT="$1"
DISTRO="$2"
DEB_PATH="$3"

FREIGHT_CACHE="/var/lib/workspace/freight/web"
export GNUPGHOME="/var/lib/workspace/freight/.gnupg"

# Stage the debs
/usr/bin/freight-add $DEB_PATH/*deb apt/$DISTRO/$COMPONENT

# Sign the debs and push to the web cache
/usr/bin/freight-cache -v

# Push to shell.theforeman.org, preserving links
# Relies on ssh keys being set up
/usr/bin/rsync -aqHl --delete-after $FREIGHT_CACHE/ greg@shell.theforeman.org:deb.theforeman.org/html/
