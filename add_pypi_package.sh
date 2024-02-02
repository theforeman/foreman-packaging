#!/bin/bash -e

PYPI_NAME=$1
VERSION=${2:-auto}
REPO=${3:-foreman-el8}
DISTRO=${REPO##*-}
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

SCRIPT_ROOT=$(dirname $(readlink -f $0))

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
  pyp2rpm --no-autonc --sclize --no-meta-runtime-dep --no-meta-buildtime-dep -s -t $TEMPLATE -o epel7 -b $BASE_PYTHON -d $PACKAGE_DIR -v $VERSION $RPM_NAME_ARG $PYPI_NAME
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
    echo "$CHANGELOG" | $SCRIPT_ROOT/add_changelog.sh $PACKAGE_DIR/*.spec
  fi
  echo "FINISHED"

  echo -e "Adding spec to git... - "
  git add $PACKAGE_DIR/*.spec
  echo "FINISHED"
  echo -e "Annexing sources... - "
  find "$PACKAGE_DIR" -name '*.tar.*' -exec git annex add {} +
  echo "FINISHED"
}

add_pypi_to_comps() {
  local comps_packages=$(rpmspec --query --builtrpms --queryformat '%{NAME}\n' $PACKAGE_DIR/*.spec)
  if [[ $REPO == katello-* ]]; then
    local comps_file="katello-server"
  else
    local comps_file="foreman"
  fi

  for comps_package in ${comps_packages}; do
    if [[ $comps_package != *-debuginfo ]] && [[ $comps_package != *-debugsource ]] ; then
      ${SCRIPT_ROOT}/add_to_comps.rb comps/comps-${comps_file}-${DISTRO}.xml $comps_package
    fi
  done
  ${SCRIPT_ROOT}/comps_doc.sh
  git add comps/
}

add_pypi_to_manifest() {
	if [[ $REPO == "foreman-el8" ]] ; then
		local section="foreman_core_packages"
	elif [[ $REPO == "foreman-plugins-el8" ]] ; then
		local section="foreman_plugin_packages"
	elif [[ $REPO == "katello-el8" ]] ; then
		local section="katello_packages"
	else
		# TODO: client packages
		local section=""
	fi

	if [[ -n $section ]] ; then
		${SCRIPT_ROOT}/add_host.py "$section" "$PACKAGE_NAME"
		git add package_manifest.yaml
	else
		echo "TODO: Add the package into the right section"
		echo "${SCRIPT_ROOT}/add_host.py SECTION '$PACKAGE_NAME'"
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
  echo -e "\nUsage:\n$0 PYPI_NAME [VERSION [REPO [PACKAGE_SUBDIR [TEMPLATE]]] \n"
  echo "VERSION is optional but can be an exact version number or auto to use the latest version"
  exit 1
fi

ensure_program pyp2rpm
ensure_program spec2scl

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
  echo -e "Updating comps... - "
  add_pypi_to_comps
  echo "FINISHED"
  echo -e "Updating manifest... - "
  add_pypi_to_manifest
  echo "FINISHED"
  git commit -m "Add $PACKAGE_NAME package"
fi
echo "Done! Now review the generated file and send a pull request"
