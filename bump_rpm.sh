#!/bin/bash -e

if [[ -z $1 ]] ; then
	echo "Usage: $0 directory"
	exit 1
fi

cd $1

SPEC_FILE=*.spec
GEM_NAME=$(awk '/^%global\s+gem_name/ { print $3 }' $SPEC_FILE)
CURRENT_VERSION=$(rpmspec -P $SPEC_FILE | awk '/^Version:/ { print $2 }')

TYPE=${1%%-*}

if [[ -z $2 ]] ; then
	if [[ $TYPE == "rubygem" ]] ; then
		NEW_VERSION=$(curl -s https://rubygems.org/api/v1/gems/${GEM_NAME}.json | jq -r .version)
	else
		echo "Unknown package type for $1"
		exit 2
	fi
else
	NEW_VERSION=$2
fi

if [[ $CURRENT_VERSION != $NEW_VERSION ]] ; then
	echo "${GEM_NAME}: $CURRENT_VERSION != $NEW_VERSION ; bumping"

	sed -i "s/^\(Version:\s\+\).\+$/\1${NEW_VERSION}/" $SPEC_FILE

	git rm *.gem

	spectool --get-files $SPEC_FILE
	git annex add *.gem
	git add .

	echo "TODO:"
	if [[ $TYPE == "rubygem" ]] ; then
		echo "* Verify the ruby runtime dependencies"

		gem compare -b $GEM_NAME $CURRENT_VERSION $NEW_VERSION
	else
		echo "* Verify the dependencies"
	fi

	RELEASE=$(rpmspec -P $SPEC_FILE | awk '/^Release:/ { print $2 }')
	if [[ ${RELEASE%%.*} != "1" ]] ; then
		echo "* Check release ($RELEASE) in $SPEC_FILE"
	fi
else
	echo "${GEM_NAME}: $CURRENT_VERSION == $NEW_VERSION ; skipping"
fi
