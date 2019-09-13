#!/bin/bash -e

if [[ -z $1 ]] ; then
	echo "Usage: $0 directory [version]"
	exit 1
elif [[ ! -d $1 ]] ; then
	echo "$1 is not a directory. It must be the full path"
	exit 1
fi

SCRIPT_DIR=$(dirname $(readlink -f $BASH_SOURCE))

cd $1

ROOT=$(git rev-parse --show-toplevel)
PACKAGE_NAME=$(basename $1)
SPEC_FILE=*.spec
GEM_NAME=$(awk '/^%global\s+gem_name/ { print $3 }' $SPEC_FILE)
CURRENT_VERSION=$(rpmspec --srpm -q --queryformat="%{version}" $SPEC_FILE)

program_exists() {
	which "$@" &> /dev/null
}

ensure_program() {
	package=${2:-$1}
	if !(program_exists $1); then
		echo "$1 is not installed - you can install it with"
		echo "sudo yum install $package"
		exit 1
	fi
}

if [[ -z $2 ]] ; then
	if [[ $PACKAGE_NAME == *rubygem-* ]]; then
		ensure_program curl
		ensure_program jq
		NEW_VERSION=$(curl -s https://rubygems.org/api/v1/gems/${GEM_NAME}.json | jq -r .version)
	else
		echo "Unknown package type for $1; a version must be specified"
		echo "Usage: $0 $1 VERSION"
		exit 2
	fi
else
	NEW_VERSION=$2
fi

if [[ $CURRENT_VERSION != $NEW_VERSION ]] ; then
	ensure_program rpmspec rpm-build

	echo "${PACKAGE_NAME}: $CURRENT_VERSION != $NEW_VERSION ; bumping"

	spectool --list-files $SPEC_FILE | cut -d' ' -f2 | grep http | xargs --no-run-if-empty -n 1 basename | xargs --no-run-if-empty git rm

	sed -i "s/^\(Version:\s\+\).\+$/\1${NEW_VERSION}/" $SPEC_FILE

	RELEASE=$(rpmspec --srpm -q --queryformat='%{release}' --undefine=dist $SPEC_FILE)
	if [[ ${RELEASE} != 1 ]] ; then
		echo "* Resetting release ($RELEASE) in $SPEC_FILE"
		sed -i "s/^\(Release:\s\+\)${RELEASE}/\11/" $SPEC_FILE
	fi

	EVR=$(rpmspec --srpm -q --queryformat='%{evr}' --undefine=dist $SPEC_FILE)
	$SCRIPT_DIR/add_changelog.sh $SPEC_FILE $EVR <<-EOF
	- Update to $NEW_VERSION
	EOF

	spectool --get-files $SPEC_FILE
	spectool --list-files $SPEC_FILE | cut -d' ' -f2 | grep http | xargs --no-run-if-empty -n 1 basename | xargs --no-run-if-empty git annex add
	git add $SPEC_FILE

	if [[ $PACKAGE_NAME == *rubygem-* ]]; then
		TEMPLATE="$(awk '/^# template: / { print $3 }' $SPEC_FILE)"
		if [[ -n $TEMPLATE ]] ; then
			echo "* Updating requirements"
			gem2rpm -t $ROOT/gem2rpm/$TEMPLATE.spec.erb *.gem | $SCRIPT_DIR/update-requirements specfile - $SPEC_FILE
			git add $SPEC_FILE
		fi

		# TODO: hint at installing rubygem-gem-compare
		echo "* Calling gem compare"
		gem compare -b $GEM_NAME $CURRENT_VERSION $NEW_VERSION
	else
		echo "TODO:"
		echo "* Verify the dependencies"
	fi

	if grep -q "# start package.json" $SPEC_FILE ; then
		UNPACKED_GEM_DIR=$(mktemp -d)
		gem unpack --target "$UNPACKED_GEM_DIR" *.gem
		PACKAGE_JSON="${UNPACKED_GEM_DIR}/${GEM_NAME}-${NEW_VERSION}/package.json"
		if [[ -f $PACKAGE_JSON ]] ; then
			$ROOT/update-requirements npm $PACKAGE_JSON $SPEC_FILE
			git add $SPEC_FILE
		else
			echo "Unable to find package.json in gem"
		fi
		rm -rf "$UNPACKED_GEM_DIR"
	fi

	git commit -m "Update $PACKAGE_NAME to $NEW_VERSION"
else
	echo "${PACKAGE_NAME}: $CURRENT_VERSION == $NEW_VERSION ; skipping"
fi
