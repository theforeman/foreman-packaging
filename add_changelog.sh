#!/bin/bash

SPEC_FILE=$1
VERSION=$2

if [[ -z $SPEC_FILE ]] || [[ ! -e $SPEC_FILE ]] ; then
	echo "Usage: $0 SPEC_FILE"
	exit 1
fi

if [[ -z $VERSION ]] ; then
	VERSION=$(rpmspec --srpm -q --queryformat="%{version}-%{release}" --undefine=dist $SPEC_FILE)
fi

read MESSAGE

sed -i -e "/%changelog/a \
* $(LANG=en_US.UTF-8 date +"%a %b %d %Y") $(rpmdev-packager) $VERSION\n$MESSAGE\n" $SPEC_FILE
