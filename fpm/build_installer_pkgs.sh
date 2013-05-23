#!/bin/bash

export VERSION=$1
export RELEASE=$2
export PLATFORM=$3
BRANCH=$4
[ -z "$BRANCH" ] && BRANCH=master

export CHECKOUTDIR="/usr/share/foreman-installer"

function clone_repo() {
  if [ -e $CHECKOUTDIR ]; then
    sudo rm -rf $CHECKOUTDIR
  fi
  sudo git clone --recursive -b $BRANCH https://github.com/theforeman/foreman-installer $CHECKOUTDIR
  sudo chown -R $USER:$USER $CHECKOUTDIR
  cd $CHECKOUTDIR
  git checkout $VERSION
}

function clean_repo() {
  rm -rf $CHECKOUTDIR/.git
  for submodule in $(ls $CHECKOUTDIR | grep -v README); do
    rm -rf $CHECKOUTDIR/$submodule/.git*
  done
}

function build_pkgs() {
  echo $VERSION > $CHECKOUTDIR/VERSION
  if [ $PLATFORM = "deb" ]; then
    fpm -d "facter >= 1.6.2" -d "puppet >= 2.6.5" -d "libhighline-ruby1.8" \
      -d "rubygems" -s dir -t $PLATFORM -n "foreman-installer" -a all \
      -v $VERSION --iteration $RELEASE $CHECKOUTDIR
  else
    fpm -d "facter >= 1.6.2" -d "puppet >= 2.6.5" -d "rubygem-highline" \
      -s dir -t $PLATFORM -n "foreman-installer" -a all \
      -v $VERSION --iteration $RELEASE $CHECKOUTDIR
  fi
}

function usage() {
  echo "USAGE: ./build_installer_pkgs.sh <version> <release> <platform> <branch>"
  exit 1
}

if [ $# != 4 ]; then
  usage
fi

clone_repo
clean_repo
build_pkgs
