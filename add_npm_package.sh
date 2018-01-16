#!/bin/bash -e

NPM_MODULE_NAME=$1
VERSION=${2:-auto}
STRATEGY=$3
TITO_TAG=foreman-nightly-nonscl-rhel7
DISTRO=${TITO_TAG##*-}

PACKAGE_NAME=nodejs-$NPM_MODULE_NAME

program_exists() {
  which "$@" &> /dev/null
}

ensure_program() {
  if !(program_exists $1); then
    echo "$1 is not installed - you can install it with"
    if [[ $1 == "npm2pm" ]] ; then
      echo "sudo npm install npm2rpm"
    else
      echo "sudo yum install $1"
    fi
    exit 1
  fi
}

generate_npm_package() {
  echo -n "Making directory..."
  UPDATE=false
  if [ -f "$PACKAGE_NAME"/*.spec ]; then
    echo -n "Detected update..."
    UPDATE=true
    sed -n '/%changelog/,$p' $PACKAGE_NAME/*.spec > OLD_CHANGELOG
    git rm -r $PACKAGE_NAME
  fi
  mkdir $PACKAGE_NAME
  echo "FINISHED"
  echo -n "Creating specs and downloading sources..."
  npm2rpm -n $NPM_MODULE_NAME -v $VERSION -s $STRATEGY
  echo "FINISHED"
  echo -n "Copying specs..."
  cp npm2rpm/SPECS/* $PACKAGE_NAME
  if [ "$UPDATE" = true ]; then
    echo "Restoring changelogs..."
    cat OLD_CHANGELOG >> $PACKAGE_NAME/*.spec
    sed -i '/^%changelog/,/^%changelog/{0,//!d}' $PACKAGE_NAME/*.spec
    rm OLD_CHANGELOG
  fi
  echo "FINISHED"
  echo -n "Copying sources..."
  cp npm2rpm/SOURCES/* $PACKAGE_NAME
  echo "FINISHED"
  rm -r npm2rpm

  if [ "$STRATEGY" = "bundle" ]; then
    echo -e "Adding npmjs cache binary... - "
    git add $PACKAGE_NAME/*-registry.npmjs.org.tgz
    echo "FINISHED"
  fi
  echo -e "Adding spec to git... - "
  git add $PACKAGE_NAME/*.spec
  echo "FINISHED"
  echo -e "Annexing sources... - "
  git annex add $PACKAGE_NAME/*.tgz
  echo "FINISHED"
}

add_to_tito_props() {
  # Get tito.props whitelists and add node package
  original_locale=$LC_COLLATE
  export LC_COLLATE=en_GB
  local current_whitelist=$(crudini --get rel-eng/tito.props $TITO_TAG whitelist)
  local whitelist=$(echo "$current_whitelist $PACKAGE_NAME" | tr " " "\n" | sort -u)
  crudini --set rel-eng/tito.props $TITO_TAG whitelist "$whitelist"
  export LC_COLLATE=$original_locale
  git add rel-eng/tito.props
}

add_npm_to_comps() {
  local comps_scl="nonscl"
  local comps_package="${PACKAGE_NAME}"
  local comps_file="foreman"

  ./add_to_comps.rb comps/comps-${comps_file}-${DISTRO}.xml $comps_package $comps_scl
  ./comps_doc.sh
  git add comps/
}

commit() {
  git commit -m "Add $PACKAGE_NAME package"
}

# Main script

if [[ -z $NPM_MODULE_NAME ]]; then
  echo "This script adds a new npm package based on the module found on npmjs.org"
  echo -e "\nUsage:\n$0 NPM_MODULE_NAME VERSION STRATEGY \n"
  exit 1
fi

ensure_program crudini
ensure_program npm2rpm

if [[ $VERSION == "auto" ]] ; then
  ensure_program curl
  ensure_program jq

  VERSION=$(curl -s https://api.npms.io/v2/package/$NPM_MODULE_NAME | jq -r .collected.metadata.version)

  if [[ $VERSION == "null" ]] ; then
    echo "Could not determine the version for $NPM_MODULE_NAME"
    exit 1
  fi
fi

if [[ -z $STRATEGY ]] ; then
  ensure_program curl
  ensure_program jq

  DEPENDENCIES=$(curl -s https://api.npms.io/v2/package/$NPM_MODULE_NAME | jq -r '.collected.metadata.dependencies|length')
  if [[ $DEPENDENCIES -gt 2 ]] ; then
    STRATEGY="bundle"
  else
    STRATEGY="single"
  fi
  echo "Found $DEPENDENCIES dependencies - using $STRATEGY strategy"
fi

generate_npm_package
echo -n "Setting tito props..."
add_to_tito_props
echo "FINISHED"
echo -e "Updating comps... - "
add_npm_to_comps
echo "FINISHED"
commit
echo "Done! Now review the generated file and send a pull request"
