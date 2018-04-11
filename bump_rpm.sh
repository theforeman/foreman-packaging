#!/bin/bash -e

if [[ -z $1 ]] ; then
	echo "Usage: $0 directory"
	exit 1
elif [[ ! -d $1 ]] ; then
	echo "$1 is not a directory. It must be the full path"
	exit 1
fi

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
	if [[ $PACKAGE_NAME == rubygem-* ]] ; then
		ensure_program curl
		ensure_program jq
		NEW_VERSION=$(curl -s https://rubygems.org/api/v1/gems/${GEM_NAME}.json | jq -r .version)
	else
		echo "Unknown package type for $1"
		exit 2
	fi
else
	NEW_VERSION=$2
fi

if [[ $CURRENT_VERSION != $NEW_VERSION ]] ; then
	ensure_program rpmspec rpm-build

	echo "${GEM_NAME}: $CURRENT_VERSION != $NEW_VERSION ; bumping"

	sed -i "s/^\(Version:\s\+\).\+$/\1${NEW_VERSION}/" $SPEC_FILE

	RELEASE=$(rpmspec --srpm -q --queryformat='%{release}' --undefine=dist $SPEC_FILE)
	if [[ ${RELEASE} != 1 ]] ; then
		echo "Resetting release ($RELEASE) in $SPEC_FILE"
		sed -i "s/^\(Release:\s\+\)${RELEASE}/\11/" $SPEC_FILE
	fi

	$ROOT/add_changelog.sh $SPEC_FILE ${NEW_VERSION}-1 <<-EOF
	- Update to $NEW_VERSION
	EOF

	git rm *.gem

	spectool --get-files $SPEC_FILE
	git annex add *.gem
	git add .

	echo "TODO:"
	if [[ $PACKAGE_NAME == rubygem-* ]] ; then
		echo "* Verify the ruby runtime dependencies"

		# TODO: hint at installing rubygem-gem-compare
		gem compare -b $GEM_NAME $CURRENT_VERSION $NEW_VERSION
	else
		echo "* Verify the dependencies"
	fi

	git commit -m "Update $PACKAGE_NAME to $NEW_VERSION"
else
	echo "${GEM_NAME}: $CURRENT_VERSION == $NEW_VERSION ; skipping"
fi
