#!/bin/bash -e

NPM_PACKAGE_NAME=$1
RPM_PACKAGE_DIR=packages/foreman/nodejs-$NPM_PACKAGE_NAME

if [[ -z $NPM_PACKAGE_NAME ]] ; then
	echo "Usage: $0 PACKAGE"
	exit 1
fi

if [[ -d $RPM_PACKAGE_DIR ]] ; then
	grep Version $RPM_PACKAGE_DIR/*.spec
else
	./add_npm_package.sh $NPM_PACKAGE_NAME
fi
