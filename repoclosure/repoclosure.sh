#!/bin/bash

set -e

if [ $# -lt 2 ]; then
  echo "Usage: $0 <yum.conf> <url>"
  exit 1
fi

yumorig=$1
url=$2
shift; shift

TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT

# repo names must be unique, or yum will get confused between different OSes and URLs
reponame=undertest-$(basename $yumorig .conf)-$(echo $url | cksum | sed 's/ /-/g')

yumconf=$TMPDIR/yum.conf
cat $yumorig > $yumconf
cat >> $yumconf << EOF

[$reponame]
name=$reponame
gpgcheck=0
baseurl=$url

EOF

repoclosure -c $yumconf -t -r $reponame $* 2>&1 | tee $TMPDIR/repoclosure.log

if tail -n1 $TMPDIR/repoclosure.log | grep -q "Num Packages"; then
  exit 0
else
  exit 1
fi
