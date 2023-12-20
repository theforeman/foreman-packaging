#!/bin/bash -e

usage() {
	echo "Usage: $0 GEM_NAME [TEMPLATE [PACKAGE_SUBDIR [REPO]]]"
	echo "Valid templates: $(ls gem2rpm | sed 's/.spec.erb//' | tr '\n' ' ')"
	echo "Valid repos: foreman-el8 foreman-plugins-el8 katello-el8 foreman-client"
	exit 1
}

generate_gem_package() {
	if [[ $UPDATE == true ]] ; then
		CHANGELOG=$(mktemp)
		sed -n '/%changelog/,$p' $PACKAGE_DIR/$SPEC_FILE > $CHANGELOG
		git rm -r $PACKAGE_DIR
	fi
	mkdir $PACKAGE_DIR
	pushd $PACKAGE_DIR
	GEM_FILE_NAME=( $( gem fetch $GEM_NAME -q ${GEM_VERSION:+-v $GEM_VERSION} --platform=ruby ) ) # the output of gem fetch is "Downloaded foo-1.2.3" we need to extract only the second word
	gem2rpm -o $SPEC_FILE "${GEM_FILE_NAME[1]}.gem" -t $TEMPLATE
	sed -i 's/\s\+$//' $SPEC_FILE
	git annex add *.gem

	VERSION=$(rpmspec --srpm -q --queryformat="%{version}-%{release}" --undefine=dist $SPEC_FILE)

	if [[ $TEMPLATE_NAME == foreman_plugin ]]; then
		UNPACKED_GEM_DIR=$(mktemp -d)
		gem unpack --target "$UNPACKED_GEM_DIR" *.gem
		PLUGIN_LIB="${UNPACKED_GEM_DIR}"/${GEM_NAME}-*/lib
		REQUIRES_FOREMAN=$(grep --extended-regexp --recursive --no-filename 'requires_foreman\s' $PLUGIN_LIB | sed -E 's/[^0-9.]//g')
		if [[ -n $REQUIRES_FOREMAN ]]; then
			sed -i "/%global foreman_min_version/ s/foreman_min_version.*/foreman_min_version $REQUIRES_FOREMAN/" "$SPEC_FILE"
		fi
		rm -rf "$UNPACKED_GEM_DIR"
	fi

	if [[ $UPDATE == true ]]; then
		cat $CHANGELOG >> $SPEC_FILE
		sed -i '/^%changelog/,/^%changelog/{0,//!d}' $SPEC_FILE
		rm $CHANGELOG
		CHANGELOG="- Update to $VERSION"
	else
		CHANGELOG="- Add $PACKAGE_NAME generated by gem2rpm using the $TEMPLATE_NAME template"
	fi
	echo "$CHANGELOG" | $ROOT/add_changelog.sh $SPEC_FILE

	if grep -q "# start package.json" $SPEC_FILE ; then
		GEM_VERSION=$(rpmspec --srpm -q --queryformat="%{version}" --undefine=dist $SPEC_FILE)
		UNPACKED_GEM_DIR=$(mktemp -d)
		gem unpack --target "$UNPACKED_GEM_DIR" *.gem
		PACKAGE_JSON="${UNPACKED_GEM_DIR}/${GEM_NAME}-${GEM_VERSION}/package.json"
		if [[ -f $PACKAGE_JSON ]] ; then
			$ROOT/update-requirements npm $PACKAGE_JSON $SPEC_FILE
		else
			echo "Unable to find package.json in gem: $PACKAGE_JSON"
		fi
		rm -rf "$UNPACKED_GEM_DIR"
	fi

	git add $SPEC_FILE
	popd
}

add_gem_to_all_comps() {
	add_gem_to_comps $REPO
	if [[ $REPO == "foreman-el8" ]] ; then
		add_gem_to_comps foreman-el9
	fi
	if [[ $REPO == "foreman-client-*" ]] ; then
		add_gem_to_comps foreman-client-el9
		add_gem_to_comps foreman-client-rhel7
	fi
}

add_gem_to_comps() {
	local tag=$1
	local distro=${tag##*-}

	# TODO: figure this out for katello
	if [[ $tag == foreman-plugins-* ]]; then
		local comps_file="foreman-plugins"
	else
		local comps_file="foreman"
	fi

	./add_to_comps.rb comps/comps-${comps_file}-${distro}.xml $PACKAGE_NAME
	./comps_doc.sh
	git add comps/
}

add_to_manifest() {
	if [[ $REPO == "foreman-el8" ]] ; then
		local section="foreman_core_packages"
	elif [[ $REPO == "foreman-plugins-el8" ]] ; then
		local section="foreman_plugin_packages"
	elif [[ $REPO == "katello-el8" ]] ; then
		local section="katello_packages"
	elif [[ $REPO == "foreman-client-*" ]] ; then
		local section="foreman_client_packages"
	else
		# TODO: installer, smart_proxy plugins, rails
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

# Main script

GEM_FULL_NAME=$1
OLD_IFS=$IFS
IFS=':' read -ra GEM_NAME_ARR <<< "$GEM_FULL_NAME"
IFS=$OLD_IFS
GEM_NAME=${GEM_NAME_ARR[0]}
GEM_VERSION=${GEM_NAME_ARR[1]}
PACKAGE_NAME=rubygem-$GEM_NAME
TEMPLATE_NAME=$2
PACKAGE_SUBDIR=$3
REPO=$4
ROOT=$(git rev-parse --show-toplevel)

REWRITE_ON_SAME_VERSION=${REWRITE_ON_SAME_VERSION:-true}

if [[ -z $TEMPLATE_NAME ]] ; then
	if [[ $GEM_NAME == smart_proxy_* ]] ; then
		TEMPLATE_NAME="smart_proxy_plugin"
	elif [[ $GEM_NAME == foreman_* ]] ; then
		TEMPLATE_NAME="foreman_plugin"
	elif [[ $GEM_NAME == hammer_* ]] ; then
		TEMPLATE_NAME="hammer_plugin"
	fi
fi

if [[ -z $REPO ]] ; then
	if [[ $TEMPLATE_NAME == *_plugin ]] ; then
		REPO="foreman-plugins-el8"
	fi
fi

if [[ -z $PACKAGE_SUBDIR ]] ; then
	if [[ $REPO == foreman-plugins-* ]] ; then
		PACKAGE_SUBDIR="plugins"
	elif [[ $REPO == katello-* ]] ; then
		PACKAGE_SUBDIR="katello"
	else
		PACKAGE_SUBDIR="foreman"
	fi
fi

PACKAGE_DIR=packages/$PACKAGE_SUBDIR/$PACKAGE_NAME
SPEC_FILE="${PACKAGE_NAME}.spec"

if [[ -f "${PACKAGE_DIR}/${SPEC_FILE}" ]]; then
	echo "Detected update..."
	UPDATE=true
	if [[ -z $TEMPLATE_NAME ]] ; then
		TEMPLATE_NAME="$(awk '/^# template: / { print $3 }' "${PACKAGE_DIR}/${SPEC_FILE}")"
	fi
else
	UPDATE=false
fi

if [[ -z $GEM_NAME ]] || [[ -z $TEMPLATE_NAME ]] || [[ $UPDATE != true ]] && [[ -z $REPO ]]; then
	usage
fi

TEMPLATE=$(pwd)/gem2rpm/$TEMPLATE_NAME.spec.erb

if [[ ! -e $TEMPLATE ]] ; then
	echo "Template $TEMPLATE does not exist."
	usage
	exit 1
fi

if [[ $UPDATE == true ]] ; then
	EXISTING_VERSION=$(rpmspec --srpm -q --queryformat="%{version}" $PACKAGE_DIR/$SPEC_FILE)
	NEW_VERSION=$(curl -s https://rubygems.org/api/v1/gems/${GEM_NAME}.json | jq -r .version)
	if [[ $REWRITE_ON_SAME_VERSION == true ]] || [[ $NEW_VERSION != $EXISTING_VERSION ]]; then
		generate_gem_package
		VERSION=$(rpmspec --srpm -q --queryformat="%{version}-%{release}" --undefine=dist $PACKAGE_DIR/$SPEC_FILE)
		git commit -m "Bump $PACKAGE_NAME to $VERSION"
	else
		echo "$PACKAGE_NAME is already at version $VERSION"
	fi
else
	generate_gem_package
	add_to_manifest
	add_gem_to_all_comps
	git commit -m "Add $PACKAGE_NAME package"
fi
