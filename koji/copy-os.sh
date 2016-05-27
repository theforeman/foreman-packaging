#!/bin/bash

if [ $# -ne 4 ]; then
  echo "$0 PRODUCT OLD_SYSTEM NEW_SYSTEM EXT_REPO_VERSION"
  echo "  echoes commands to copy a PRODUCT (e.g. 'foreman-nightly') from one SYSTEM"
  echo "  ('fedora21') to a new SYSTEM ('fedora24', 'nonscl-rhel7')."
  echo
  echo "  EXT_REPO_VERSION should be the version number in the Koji external repos,"
  echo "  e.g. 7.3 or 24"
  echo
  echo "  makes no changes to the server, execute its output to action"
  exit 1
fi

PRODUCT=$1
OLD_SYSTEM=$2
SYSTEM=$3
EXT_REPO_VERSION=$4

echo kkoji add-tag $PRODUCT-$SYSTEM
echo kkoji add-tag --parent=$PRODUCT-$SYSTEM $PRODUCT-$SYSTEM-override
echo kkoji add-tag --parent=$PRODUCT-$SYSTEM-override $PRODUCT-$SYSTEM-build

echo kkoji lock-tag $PRODUCT-$SYSTEM-build

ARCHES=`kkoji taginfo $PRODUCT-$OLD_SYSTEM-build | grep Arches | sed -e 's|^Arches: ||' -e 's| |,|g'`

echo kkoji edit-tag --arches=$ARCHES $PRODUCT-$SYSTEM-build

kkoji list-external-repos --quiet --tag=$PRODUCT-$OLD_SYSTEM-build | awk '{print $1 " " $2}' | while read PRIORITY REPO; do
    echo kkoji add-external-repo -p $PRIORITY -t $PRODUCT-$SYSTEM-build $(echo $REPO | sed "s/[0-9\.]\+/${EXT_REPO_VERSION}/")
done

kkoji list-groups $PRODUCT-$OLD_SYSTEM-build | awk '{print $1}' | while read LINE; do
    echo $LINE | grep -q ":$" && {
        # LINE is a package
        PKG=`echo $LINE | tr -d ':'`
        echo kkoji add-group-pkg $PRODUCT-$SYSTEM-build $GROUP $PKG
        continue
    }
    # LINE is a group
    GROUP=$LINE
    echo kkoji add-group $PRODUCT-$SYSTEM-build $GROUP
done

echo kkoji add-target $PRODUCT-$SYSTEM $PRODUCT-$SYSTEM-build $PRODUCT-$SYSTEM
