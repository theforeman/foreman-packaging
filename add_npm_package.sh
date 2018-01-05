#!/bin/bash -e

NPM_MODULE_NAME=$1
VERSION=${2:-auto}
STRATEGY=$3

PACKAGE_NAME=nodejs-$NPM_MODULE_NAME

if [[ -z $NPM_MODULE_NAME ]]; then
  echo "This script adds a new npm package based on the module found on npmjs.org"
  echo -e "\nUsage:\n$0 NPM_MODULE_NAME VERSION STRATEGY \n"
  exit 1
fi

program_exists() {
  which "$@" &> /dev/null;
}

if !(program_exists crudini); then
  echo "crudini is not installed - you can install it with"
  echo "sudo yum install crudini"
  exit 1
fi

if !(program_exists npm2rpm); then
  echo "npm2rpm is not installed - you can install it with:"
  echo "sudo npm install npm2rpm"
  exit 1
fi

if [[ $VERSION == "auto" ]] ; then
  if !(program_exists curl) ;  then
    echo "curl is not installed - you can install it with:"
    echo "sudo yum install curl"
    exit 1
  fi

  if !(program_exists jq) ;  then
    echo "jq is not installed - you can install it with:"
    echo "sudo yum install jq"
    exit 1
  fi

  VERSION=$(curl -s https://api.npms.io/v2/package/$NPM_MODULE_NAME | jq -r .collected.metadata.version)

  if [[ $VERSION == "null" ]] ; then
    echo "Could not determine the version for $NPM_MODULE_NAME"
    exit 1
  fi
fi

if [[ -z $STRATEGY ]] ; then
  if !(program_exists curl) ;  then
    echo "curl is not installed - you can install it with:"
    echo "sudo yum install curl"
    exit 1
  fi

  if !(program_exists jq) ;  then
    echo "jq is not installed - you can install it with:"
    echo "sudo yum install jq"
    exit 1
  fi

  DEPENDENCIES=$(curl -s https://api.npms.io/v2/package/$NPM_MODULE_NAME | jq -r '.collected.metadata.dependencies|length')
  if [[ $DEPENDENCIES -gt 2 ]] ; then
    STRATEGY="bundle"
  else
    STRATEGY="single"
  fi
  echo "Found $DEPENDENCIES dependencies - using $STRATEGY strategy"
fi

echo -n "Making directory..."
UPDATE=false
if [ -f "$PACKAGE_NAME"/*.spec ]; then
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
echo -n "Setting tito props..."
# Get tito.props whitelists and add node package
original_locale=$LC_COLLATE
export LC_COLLATE=en_GB
el7whitelist=$(crudini --get rel-eng/tito.props foreman-nightly-nonscl-rhel7 whitelist)
el7whitelist=$(echo "$el7whitelist $PACKAGE_NAME" | tr " " "\n" | sort -u)
crudini --set rel-eng/tito.props foreman-nightly-nonscl-rhel7 whitelist "$el7whitelist"
export LC_COLLATE=$original_locale
git add rel-eng/tito.props
echo "FINISHED"
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
echo -e "Updating comps... - "
./add_to_comps.rb comps/comps-foreman-rhel7.xml $PACKAGE_NAME nonscl
./comps_doc.sh
git add comps/
echo "FINISHED"
git commit -m "Add $PACKAGE_NAME package"
echo "Done! Now review the generated file and send a pull request"
