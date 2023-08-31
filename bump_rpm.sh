#!/bin/bash -e

# Dependencies:
# curl (if no new version is specified)
# jq (if no new version is specified)
# python3-semver (for update-requirements)
# rpm-build (provides rpmspec)
# rpmdevtools (provides spectool)
# rubygem-gem2rpm

if [[ -z $1 ]] ; then
	echo "Usage: $0 directory [version]"
	exit 1
elif [[ ! -d $1 ]] ; then
	echo "$1 is not a directory. It must be the full path"
	exit 1
fi

program_exists() {
	which "$@" &> /dev/null
}

ensure_program() {
	package=${2:-$1}
	if ! (program_exists "$1"); then
		echo "$1 is not installed - you can install it with"
		echo "sudo yum install $package"
		exit 1
	fi
}

ensure_program rpmspec rpm-build

SCRIPT_DIR=$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")

ROOT=$(git rev-parse --show-toplevel)
PACKAGE_NAME=$(basename "$1")
SPEC_FILE=*.spec
CURRENT_VERSION=$(rpmspec --srpm -q --queryformat="%{version}" "$1"/$SPEC_FILE)

if [[ -z $2 ]] ; then
	if [[ $PACKAGE_NAME == *rubygem-* ]]; then
		ensure_program curl
		ensure_program jq
		GEM_NAME=$(awk '/^%global\s+gem_name/ { print $3 }' $SPEC_FILE)
		NEW_VERSION=$(curl -s "https://rubygems.org/api/v1/versions/${GEM_NAME}/latest.json" | jq -r .version)
	else
		echo "Unknown package type for $1; a version must be specified"
		echo "Usage: $0 $1 VERSION"
		exit 2
	fi
else
	NEW_VERSION=$2
fi

if [[ $CURRENT_VERSION != "$NEW_VERSION" ]] ; then
	ensure_program spectool rpmdevtools

	echo "${PACKAGE_NAME}: $CURRENT_VERSION != $NEW_VERSION ; bumping"

	if [[ $PACKAGE_NAME == *rubygem-* ]]; then
		cd "$1"
		GEM_NAME=$(awk '/^%global\s+gem_name/ { print $3 }' $SPEC_FILE)

		spectool --list-files $SPEC_FILE | cut -d' ' -f2 | grep http | xargs --no-run-if-empty -n 1 basename | xargs --no-run-if-empty git rm

		sed -i "s/^\(Version:\s\+\).\+$/\1${NEW_VERSION}/" $SPEC_FILE

		RELEASE=$(rpmspec --srpm -q --queryformat='%{release}' --undefine=dist $SPEC_FILE)
		if [[ ${RELEASE} != 1 ]] ; then
			echo "* Resetting release ($RELEASE) in $SPEC_FILE"
			sed -i "s/^\(Release:\s\+\)${RELEASE}/\11/" $SPEC_FILE
		fi

		"$SCRIPT_DIR"/add_changelog.sh $SPEC_FILE <<-EOF
		- Update to $NEW_VERSION
		EOF

		spectool --get-files $SPEC_FILE
		spectool --list-files $SPEC_FILE | cut -d' ' -f2 | grep http | xargs --no-run-if-empty -n 1 basename | xargs --no-run-if-empty git annex add
		git add $SPEC_FILE

		TEMPLATE="$(awk '/^# template: / { print $3 }' $SPEC_FILE)"
		if [[ $TEMPLATE == 'scl' ]] || [[ $TEMPLATE == 'nonscl' ]] || [[ -z $TEMPLATE ]]; then
			CHANGELOG=$(mktemp)
			trap "rm -f $CHANGELOG" EXIT
			sed -e '1,/%changelog/ d' $SPEC_FILE > "$CHANGELOG"
			gem2rpm -t "$ROOT/gem2rpm/default.spec.erb" -o $SPEC_FILE ./*.gem
			cat "$CHANGELOG" >> $SPEC_FILE
			git add $SPEC_FILE
		elif [[ -n $TEMPLATE ]] ; then
			echo "* Updating requirements"
			gem2rpm -t "$ROOT/gem2rpm/$TEMPLATE.spec.erb" ./*.gem | "$SCRIPT_DIR"/update-requirements specfile - $SPEC_FILE
			if [[ $TEMPLATE == foreman_plugin ]]; then
				UNPACKED_GEM_DIR=$(mktemp -d)
				gem unpack --target "$UNPACKED_GEM_DIR" ./*.gem
				PLUGIN_LIB="${UNPACKED_GEM_DIR}/${GEM_NAME}-${NEW_VERSION}/lib"
				REQUIRES_FOREMAN=$(grep --extended-regexp --recursive --no-filename 'requires_foreman\s' "$PLUGIN_LIB" | sed -E 's/[^0-9.]//g')
				if [[ -n $REQUIRES_FOREMAN ]]; then
					sed -i "/%global foreman_min_version/ s/foreman_min_version.*/foreman_min_version $REQUIRES_FOREMAN/" $SPEC_FILE
				fi
				rm -rf "$UNPACKED_GEM_DIR"
			fi
			git add $SPEC_FILE
		fi

		if grep -q "# start package.json" $SPEC_FILE ; then
			UNPACKED_GEM_DIR=$(mktemp -d)
			gem unpack --target "$UNPACKED_GEM_DIR" ./*.gem
			PACKAGE_JSON="${UNPACKED_GEM_DIR}/${GEM_NAME}-${NEW_VERSION}/package.json"
			if [[ -f $PACKAGE_JSON ]] ; then
				"$ROOT"/update-requirements npm "$PACKAGE_JSON" $SPEC_FILE
				git add $SPEC_FILE
			else
				echo "Unable to find package.json in gem"
			fi
			rm -rf "$UNPACKED_GEM_DIR"
		fi
	elif [[ $PACKAGE_NAME == *nodejs-* ]]; then
		NPM_NAME=$(awk '/^%global\s+npm_name/ { print $3 }' "$1"/$SPEC_FILE)

		echo "Bumping NPM package"
		SKIP_GIT_COMMIT=1
		SOURCES=$(spectool --list-files "$1"/$SPEC_FILE)

		if [[ $SOURCES == *registry.npmjs.org.tgz* ]]; then
			NPM_STRATEGY='bundle'
		else
			NPM_STRATEGY='single'
		fi

		"$SCRIPT_DIR"/add_npm_package.sh "$NPM_NAME" "$NEW_VERSION" "$NPM_STRATEGY"
	else
		echo "TODO:"
		echo "* Verify the dependencies"
	fi

	if [[ "$SKIP_GIT_COMMIT" != "1" ]] ; then
		git commit -m "Update $PACKAGE_NAME to $NEW_VERSION"
	fi
else
	echo "${PACKAGE_NAME}: $CURRENT_VERSION == $NEW_VERSION ; skipping"
fi
