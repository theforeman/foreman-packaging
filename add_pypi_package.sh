#!/bin/bash -e

PYPI_NAME=$1
VERSION=${2:-auto}
TITO_TAG=${3:-foreman-nightly-nonscl-rhel7}
DISTRO=${TITO_TAG##*-}
BASE_DIR=${4:-foreman}
TEMPLATE=${5:-fedora}
BASE_PYTHON=3

REWRITE_ON_SAME_VERSION=${REWRITE_ON_SAME_VERSION:-true}

if [[ ${PYPI_NAME} == python-* ]]; then
  PACKAGE_PREFIX=""
else
  PACKAGE_PREFIX="python-"
fi
# the package name will contain the downcased PYPI_NAME, with dots replaced by hyphens
PACKAGE_NAME=${PACKAGE_PREFIX}$(echo ${PYPI_NAME} |tr '[A-Z].' '[a-z]-')
PACKAGE_DIR=packages/$BASE_DIR/$PACKAGE_NAME

ROOT=$(git rev-parse --show-toplevel)

program_exists() {
  which "$@" &> /dev/null
}

ensure_program() {
  if !(program_exists $1); then
    echo "$1 is not installed - you can install it with"
    echo "sudo yum install $1"
    exit 1
  fi
}

generate_pypi_package() {
  echo -n "Making directory..."
  if [[ $UPDATE == true ]] ; then
    sed -n '/%changelog/,$p' $PACKAGE_DIR/*.spec > OLD_CHANGELOG
    git rm -r $PACKAGE_DIR
  fi
  mkdir $PACKAGE_DIR
  echo "FINISHED"
  echo -n "Creating specs and downloading sources..."
  # pass -r $PACKAGE_NAME to pyp2rpm if we had to downcase the name
  if [[ $PACKAGE_NAME != "${PACKAGE_PREFIX}${PYPI_NAME}" ]]; then
    RPM_NAME_ARG="-r ${PACKAGE_NAME}"
  else
    RPM_NAME_ARG=""
  fi
  pyp2rpm --no-autonc -s -t $TEMPLATE -b $BASE_PYTHON -d $PACKAGE_DIR -v $VERSION $RPM_NAME_ARG $PYPI_NAME
  # pyp2rpm does not create a newline at the end of the file, which breaks our changelog append script
  echo >> $PACKAGE_DIR/*.spec
  sed -i '/BuildRequires:.*sphinx/d' $PACKAGE_DIR/*.spec
  echo "FINISHED"
  if [[ $UPDATE == true ]]; then
    echo "Restoring changelogs..."
    cat OLD_CHANGELOG >> $PACKAGE_DIR/*.spec
    sed -i '/^%changelog/,/^%changelog/{0,//!d}' $PACKAGE_DIR/*.spec
    rm OLD_CHANGELOG
    CHANGELOG="- Update to $VERSION"
    echo "$CHANGELOG" | $ROOT/add_changelog.sh $PACKAGE_DIR/*.spec
  fi
  echo "FINISHED"

  echo -e "Adding spec to git... - "
  git add $PACKAGE_DIR/*.spec
  echo "FINISHED"
  echo -e "Annexing sources... - "
  find "$PACKAGE_DIR" -name '*.tar.gz' -exec git annex add {} +
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

add_pypi_to_comps() {
  local comps_packages=$(rpmspec --query --builtrpms --queryformat '%{NAME}\n' $PACKAGE_DIR/*.spec)
  if [[ $TITO_TAG == katello-*-pulpcore-* ]]; then
    local comps_file="katello-pulpcore"
    local comps_scl=""
  elif [[ $TITO_TAG == katello-* ]]; then
    local comps_file="katello-server"
    local comps_scl="nonscl"
  else
    local comps_file="foreman"
    local comps_scl="nonscl"
  fi

  for comps_package in ${comps_packages}; do
    ./add_to_comps.rb comps/comps-${comps_file}-${DISTRO}.xml $comps_package $comps_scl
  done
  ./comps_doc.sh
  git add comps/
}

add_pypi_to_manifest() {
	if [[ $TITO_TAG == "foreman-nightly-nonscl-rhel7" ]] ; then
		local section="foreman_nonscl_packages"
	elif [[ $TITO_TAG == "foreman-plugins-nightly-nonscl-rhel7" ]] ; then
		local section="plugin_nonscl_packages"
	elif [[ $TITO_TAG == "katello-nightly-rhel7" ]] ; then
		local section="katello_packages"
	elif [[ $TITO_TAG == "katello-nightly-pulpcore-el7" ]] ; then
		local section="pulpcore_packages"
	else
		# TODO: client packages
		local section=""
	fi

	if [[ -n $section ]] ; then
		./add_host.py "$section" "$PACKAGE_NAME"
		git add package_manifest.yaml
	else
		echo "TODO: Add the package into the right section"
		echo "./add_host.py SECTION '$PACKAGE_NAME'"
		echo "git add package_manifest.yaml"
		echo "git commit --amend --no-edit"
	fi
}

pypi_info() {
  curl -s https://pypi.org/pypi/${PYPI_NAME}/json
}

# Main script

if [[ -z $PYPI_NAME ]]; then
  echo "This script adds a new python package based on the module found on pypi.org"
  echo -e "\nUsage:\n$0 PYPI_NAME [VERSION [TITO_TAG [PACKAGE_SUBDIR [TEMPLATE]]] \n"
  echo "VERSION is optional but can be an exact version number or auto to use the latest version"
  exit 1
fi

ensure_program crudini
ensure_program pyp2rpm

if [[ $VERSION == "auto" ]] ; then
  ensure_program curl
  ensure_program jq

  VERSION=$(pypi_info | jq -r .info.version)

  if [[ $VERSION == "null" ]] ; then
    echo "Could not determine the version for $NPM_MODULE_NAME"
    exit 1
  fi
fi

if [ -f "$PACKAGE_DIR"/*.spec ]; then
  echo -n "Detected update..."
  UPDATE=true
else
  UPDATE=false
fi

if [[ $UPDATE == true ]] ; then
  EXISTING_VERSION=$(rpmspec --query --srpm --queryformat '%{VERSION}' $PACKAGE_DIR/*.spec)
  if [[ $REWRITE_ON_SAME_VERSION == true ]] || [[ $VERSION != $EXISTING_VERSION ]]; then
    generate_pypi_package
    git commit -m "Bump $PACKAGE_NAME to $VERSION"
  else
    echo "$PACKAGE_NAME is already at version $VERSION"
  fi
else
  generate_pypi_package
  echo -n "Setting tito props..."
  add_to_tito_props
  echo "FINISHED"
  echo -e "Updating comps... - "
  add_pypi_to_comps
  echo "FINISHED"
  echo -e "Updating manifest... - "
  add_pypi_to_manifest
  echo "FINISHED"
  git commit -m "Add $PACKAGE_NAME package"
fi
echo "Done! Now review the generated file and send a pull request"
