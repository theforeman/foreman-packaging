#!/bin/bash

set -e

if [ $# -lt 2 ]; then
  echo "Usage: $0 <yum.conf>"
  exit 1
fi

config=$1 ; shift

TEMPDIR=$(mktemp -d)
trap "rm -rf $TEMPDIR" EXIT

dnf repoclosure -c $config "$@"
