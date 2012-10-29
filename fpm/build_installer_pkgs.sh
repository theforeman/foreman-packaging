#!/bin/bash

export VERSION=$1
export CHECKOUTDIR="/usr/share/foreman-installer"

function clone_repo() {
  if [ -e $CHECKOUTDIR ]; then
    sudo rm -rf $CHECKOUTDIR
  fi
  sudo git clone --recursive https://github.com/theforeman/foreman-installer $CHECKOUTDIR
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
  for platform in "rpm" "deb"; do
    fpm -s dir -t $platform -n "foreman-installer" -a all \
      -v $VERSION $CHECKOUTDIR
  done
}

function usage() {
  echo "USAGE: ./build_installer_pkgs.sh <version>"
  exit 1
}

if [ $# != 1 ]; then
  usage
fi

clone_repo
clean_repo
build_pkgs
