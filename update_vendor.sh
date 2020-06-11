#!/bin/bash -e

VERSION=${1:-auto}

./add_npm_package.sh @theforeman/vendor ${VERSION}
./add_npm_package.sh @theforeman/builder ${VERSION}
