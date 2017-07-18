#!/bin/bash
display_usage() {
  echo "This script adds a new npm package based on the module found on npmjs.org"
  echo -e "\nUsage:\n$0 NPM_MODULE_NAME VERSION STRATEGY \n"
  exit 1
}

if [ $# -ne 3 ]; then
  display_usage
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

echo -n "Making directory..."
mkdir nodejs-$1
echo "FINISHED"
echo -n "Creating specs and downloading sources..."
npm2rpm -n $1 -v $2 -s $3
echo "FINISHED"
echo -n "Copying specs..."
cp npm2rpm/SPECS/* nodejs-$1
echo "FINISHED"
echo -n "Copying sources..."
cp npm2rpm/SOURCES/* nodejs-$1
echo "FINISHED"
rm -r npm2rpm
echo -n "Setting tito props..."
# Get tito.props whitelists and add node package
original_locale=$LC_COLLATE
export LC_COLLATE=en_GB
el7whitelist=$(crudini --get rel-eng/tito.props foreman-nightly-nonscl-rhel7 whitelist)
el7whitelist=$(echo "$el7whitelist nodejs-$1" | tr " " "\n" | sort)
crudini --set rel-eng/tito.props foreman-nightly-nonscl-rhel7 whitelist "$el7whitelist"
export LC_COLLATE=$original_locale
git add rel-eng/tito.props
echo "FINISHED"
cd nodejs-$1
if [ "$3" = "bundle" ]; then
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
./add_to_comps.rb comps/comps-foreman-rhel7.xml nodejs-$1 nonscl
./comps_doc.sh
git add comps/
echo "FINISHED"
echo "Done! Now commit and send your pull request."
