#!/bin/bash

set -e

if [ $# -lt 2 ]; then
  echo "Usage: $0 <yum.conf>"
  exit 1
fi

config=$1 ; shift

TEMPDIR=$(mktemp -d)
trap "rm -rf $TEMPDIR" EXIT

repoclosure -c $config -t $* 2>&1 | tee $TEMPDIR/repoclosure.log

if tail -n1 $TEMPDIR/repoclosure.log | grep -q "Num Packages"; then
  exit 0
else
  exit 1
fi
