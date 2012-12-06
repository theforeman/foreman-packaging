#!/bin/bash

# Script to be cloned from git to build foreman-proxy (stable)
# Assumes this repo/dir has been checked out already. Operates
# from ./ and copies to $source/debian

# Expected input
# $1 - pbuilder base image, eg squeeze64
# $2 - precreated temp dir to use

# Stop on errors
set -e

PACKAGE_NAME='foreman-proxy'

# Name of the pbuilder env to use
PBUILDER="$1"

# We use readlink to get an absolute path to the Jenkins
# checkout, but readlink expects the path to exist
mkdir -p "../$1"
BUILD_DIR=`readlink -f ../$1`
TARGET="${BUILD_DIR}/${PACKAGE_NAME}"

REPO='git://github.com/theforeman/smart-proxy.git'
BRANCH='9ea6076283d744ba55163ad45e3bacd96a1add72'

GIT='/usr/bin/git'

# Copy in packaging to the build dir
mkdir -p  "${BUILD_DIR}/debian"
cp -r ./* "${BUILD_DIR}/debian/"

# Clone source code
cd "${BUILD_DIR}"
$GIT clone "${REPO}" "${TARGET}"
cd "${TARGET}"
$GIT checkout "${BRANCH}"
$GIT submodule init
$GIT submodule update
# Move packaging into source clone
mv "${BUILD_DIR}/debian" "${TARGET}/"

# Cleanup source
rm -rf $(/usr/bin/find "${TARGET}" -name '.git*')

# Execute build using the pbuilder image in $1
sudo pdebuild-$PBUILDER
sudo chown -R jenkins:jenkins "${BUILD_DIR}"
