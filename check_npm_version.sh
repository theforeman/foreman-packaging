#!/bin/bash -e

NPM_PACKAGE_NAME=$1

if [[ -z $NPM_PACKAGE_NAME ]] ; then
	echo "Usage: $0 PACKAGE"
	exit 1
fi

if [[ -d nodejs-$NPM_PACKAGE_NAME ]] ; then
	grep Version nodejs-$NPM_PACKAGE_NAME/*.spec
else
	./add_npm_package.sh $NPM_PACKAGE_NAME
fi
