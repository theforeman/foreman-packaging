#!/bin/bash

set -e

if [ $# -lt 2 ]; then
  echo "Usage: $0 <yum.conf> <url>"
  exit 1
fi

yumorig=$1
url=$2
shift; shift

TEMPDIR=$(mktemp -d)
trap "rm -rf $TEMPDIR" EXIT

# repo names must be unique, or yum will get confused between different OSes and URLs
reponame=undertest-$(basename $yumorig .conf)-$(echo $url | cksum | sed 's/ /-/g')

yumconf=$TEMPDIR/yum.conf
cat $yumorig > $yumconf
cat >> $yumconf << EOF

[$reponame]
name=$reponame
gpgcheck=0
baseurl=$url

EOF

repoclosure -c $yumconf -t -r $reponame $* 2>&1 | tee $TEMPDIR/repoclosure.log

if tail -n1 $TEMPDIR/repoclosure.log | grep -q "Num Packages"; then
  exit 0
else
  exit 1
fi
