#!/bin/bash

set -e

if [ $# -lt 2 ]; then
	echo "Usage: $0 <dnf.conf> <releasever>"
	exit 1
fi

config=$1 ; shift
releasever=$1 ; shift

TEMPDIR=$(mktemp -d -t repoclosure-XXXXXX)
trap "rm -rf $TEMPDIR" EXIT

if [[ $releasever == 8 ]] ; then
	# Enable modularity on EL8
	MODULESDIR=$TEMPDIR/etc/dnf/modules.d
	mkdir -p $MODULESDIR
	cat > $MODULESDIR/ruby.module <<-EOF
	[ruby]
	name=ruby
	stream=2.7
	profiles=
	state=enabled
	EOF

	cat > $MODULESDIR/postgresql.module <<-EOF
	[postgresql]
	name=postgresql
	stream=12
	profiles=
	state=enabled
	EOF

	cat > $MODULESDIR/foreman.module <<-EOF
	[foreman]
	name=foreman
	stream=el$releasever
	profiles=
	state=enabled
	EOF
fi

dnf --installroot $TEMPDIR --releasever $releasever repoclosure --config $config "$@"
