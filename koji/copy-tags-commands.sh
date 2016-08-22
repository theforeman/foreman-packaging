#!/bin/bash

if [ $# -ne 2 ]; then
  echo "$0 OLD_VERSION NEW_VERSION"
  echo "  echoes commands to clone old Koji tags (usually 'nightly') to a new release"
  echo "  makes no changes to the server, execute its output to action"
  exit 1
fi

OLD=$1
VERSION=$2

NONSCL_SYSTEMS="fedora24"
SCL_SYSTEMS="rhel6 rhel7"

clone() {
  echo kkoji clone-tag $PRODUCT-$OLD-$SYSTEM $PRODUCT-$VERSION-$SYSTEM

  echo kkoji add-tag --parent=$PRODUCT-$VERSION-$SYSTEM $PRODUCT-$VERSION-$SYSTEM-override
  echo kkoji add-tag --parent=$PRODUCT-$VERSION-$SYSTEM-override $PRODUCT-$VERSION-$SYSTEM-build

  echo kkoji lock-tag $PRODUCT-$VERSION-$SYSTEM-build

  ARCHES=`kkoji taginfo $PRODUCT-$OLD-$SYSTEM-build | grep Arches | sed -e 's|^Arches: ||' -e 's| |,|g'`

  echo kkoji edit-tag --arches=$ARCHES $PRODUCT-$VERSION-$SYSTEM-build

  kkoji list-external-repos --quiet --tag=$PRODUCT-$OLD-$SYSTEM-build | awk '{print $1 " " $2}' | while read PRIORITY REPO; do
      echo kkoji add-external-repo -p $PRIORITY -t $PRODUCT-$VERSION-$SYSTEM-build $REPO
  done

  kkoji list-groups $PRODUCT-$OLD-$SYSTEM-build | awk '{print $1}' | while read LINE; do
      echo $LINE | grep -q ":$" && {
          # LINE is a package
          PKG=`echo $LINE | tr -d ':'`
          echo kkoji add-group-pkg $PRODUCT-$VERSION-$SYSTEM-build $GROUP $PKG
          continue
      }
      # LINE is a group
      GROUP=$LINE
      echo kkoji add-group $PRODUCT-$VERSION-$SYSTEM-build $GROUP
  done

  echo kkoji add-target $PRODUCT-$VERSION-$SYSTEM $PRODUCT-$VERSION-$SYSTEM-build $PRODUCT-$VERSION-$SYSTEM
}

### Foreman
PRODUCT=foreman
# clone non-SCL OSes, nonscl tags for SCL OSes
for SYSTEM in $NONSCL_SYSTEMS $(echo $SCL_SYSTEMS | sed 's/\(^\| \)/\1nonscl-/g'); do
  clone $PRODUCT-$OLD-$SYSTEM $PRODUCT-$VERSION-$SYSTEM
done

# clone SCL tags, inherit nonscl into build tags
for SYSTEM in $SCL_SYSTEMS; do
  clone $PRODUCT-$OLD-$SYSTEM $PRODUCT-$VERSION-$SYSTEM
  echo kkoji add-tag-inheritance --priority=10 $PRODUCT-$VERSION-$SYSTEM-build $PRODUCT-$VERSION-nonscl-$SYSTEM
done

# create -dist tag for mash, built from SCL+nonscl tags (like a SQL view)
for SYSTEM in $NONSCL_SYSTEMS $SCL_SYSTEMS; do
  echo kkoji add-tag $PRODUCT-$VERSION-$SYSTEM-dist
  echo kkoji add-tag-inheritance --priority=20 $PRODUCT-$VERSION-$SYSTEM-dist $PRODUCT-$VERSION-$SYSTEM
done
for SYSTEM in $SCL_SYSTEMS; do
  echo kkoji add-tag-inheritance --priority=10 $PRODUCT-$VERSION-$SYSTEM-dist $PRODUCT-$VERSION-nonscl-$SYSTEM
done

### Plugins
PRODUCT=foreman-plugins
# clone plugin tags for non-SCL OSes, nonscl tags for SCL OSes
for SYSTEM in $NONSCL_SYSTEMS $(echo $SCL_SYSTEMS | sed 's/\(^\| \)/\1nonscl-/g'); do
  clone $PRODUCT-$OLD-$SYSTEM $PRODUCT-$VERSION-$SYSTEM
  echo kkoji add-tag-inheritance --priority=10 $PRODUCT-$VERSION-$SYSTEM-build foreman-$VERSION-$SYSTEM
done

# clone SCL tags
#   plugin SCL and nonscl tags: inherit core SCL
#   plugin SCL tags: inherit core + plugin nonscl
for SYSTEM in $SCL_SYSTEMS; do
  clone $PRODUCT-$OLD-$SYSTEM $PRODUCT-$VERSION-$SYSTEM
  echo kkoji add-tag-inheritance --priority=15 $PRODUCT-$VERSION-$SYSTEM-build foreman-$VERSION-$SYSTEM
  echo kkoji add-tag-inheritance --priority=15 $PRODUCT-$VERSION-nonscl-$SYSTEM-build foreman-$VERSION-$SYSTEM

  echo kkoji add-tag-inheritance --priority=5 $PRODUCT-$VERSION-$SYSTEM-build $PRODUCT-$VERSION-nonscl-$SYSTEM
  echo kkoji add-tag-inheritance --priority=20 $PRODUCT-$VERSION-$SYSTEM-build foreman-$VERSION-nonscl-$SYSTEM
done

# create -dist tag for mash, built from SCL+nonscl tags (like a SQL view)
for SYSTEM in $NONSCL_SYSTEMS $SCL_SYSTEMS; do
  echo kkoji add-tag $PRODUCT-$VERSION-$SYSTEM-dist
  echo kkoji add-tag-inheritance --priority=20 $PRODUCT-$VERSION-$SYSTEM-dist $PRODUCT-$VERSION-$SYSTEM
done
for SYSTEM in $SCL_SYSTEMS; do
  echo kkoji add-tag-inheritance --priority=10 $PRODUCT-$VERSION-$SYSTEM-dist $PRODUCT-$VERSION-nonscl-$SYSTEM
done
