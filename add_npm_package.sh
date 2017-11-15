#!/bin/bash -e

NPM_MODULE_NAME=$1
VERSION=${2:-auto}
STRATEGY=$3

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
mkdir nodejs-$NPM_MODULE_NAME
echo "FINISHED"
echo -n "Creating specs and downloading sources..."
npm2rpm -n $NPM_MODULE_NAME -v $VERSION -s $STRATEGY
echo "FINISHED"
echo -n "Copying specs..."
cp npm2rpm/SPECS/* nodejs-$NPM_MODULE_NAME
echo "FINISHED"
echo -n "Copying sources..."
cp npm2rpm/SOURCES/* nodejs-$NPM_MODULE_NAME
echo "FINISHED"
rm -r npm2rpm
echo -n "Setting tito props..."
# Get tito.props whitelists and add node package
original_locale=$LC_COLLATE
export LC_COLLATE=en_GB
el7whitelist=$(crudini --get rel-eng/tito.props foreman-nightly-nonscl-rhel7 whitelist)
el7whitelist=$(echo "$el7whitelist nodejs-$NPM_MODULE_NAME" | tr " " "\n" | sort -u)
crudini --set rel-eng/tito.props foreman-nightly-nonscl-rhel7 whitelist "$el7whitelist"
export LC_COLLATE=$original_locale
git add rel-eng/tito.props
echo "FINISHED"
cd nodejs-$NPM_MODULE_NAME
if [ "$STRATEGY" = "bundle" ]; then
  echo -e "Adding npmjs cache binary... - "
  git add *-registry.npmjs.org.tgz
  echo "FINISHED"
fi
echo -e "Annexing sources... - "
git annex add *.tgz
echo "FINISHED"
echo -e "Adding spec to git... - "
git add *.spec
echo "FINISHED"
echo -e "Updating comps... - "
cd ..
./add_to_comps.rb comps/comps-foreman-rhel7.xml nodejs-$NPM_MODULE_NAME nonscl
./comps_doc.sh
git add comps/
echo "FINISHED"
echo "Done! Now commit and send your pull request."
