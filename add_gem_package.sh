#!/bin/bash -e

usage() {
	echo "Usage: $0 GEM_NAME [TEMPLATE [TITO_TAG [PACKAGE_SUBDIR]]]"
	echo "Valid templates: $(ls gem2rpm | sed 's/.spec.erb//' | tr '\n' ' ')"
	python3 -c "import configparser ; c = configparser.ConfigParser() ; c.read('rel-eng/tito.props') ; print('Tito tags: ' + ' '.join(s for s in c.sections() if s not in ('requirements', 'buildconfig', 'builder')))"
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

add_to_all_tito_props() {
	add_to_tito_props $TITO_TAG
	if [[ $TITO_TAG == "foreman-nightly-rhel7" ]] || [[ $TITO_TAG == "foreman-nightly-nonscl-rhel7" ]] ; then
		add_to_tito_props foreman-nightly-el8
	elif [[ $TITO_TAG == "foreman-plugins-nightly-rhel7" ]] || [[ $TITO_TAG == "foreman-plugins-nightly-nonscl-rhel7" ]] ; then
		add_to_tito_props foreman-plugins-nightly-el8
	elif [[ $TITO_TAG == "foreman-client-nightly-rhel7" ]] ; then
		add_to_tito_props foreman-client-nightly-el8
		add_to_tito_props foreman-client-nightly-el9
	elif [[ $TITO_TAG == "katello-nightly-rhel7" ]] ; then
		add_to_tito_props katello-nightly-el8
	fi
}

add_to_tito_props() {
	local tag=$1

	# Get tito.props whitelists and add node package
	original_locale=$LC_COLLATE
	export LC_COLLATE=en_GB
	local current_whitelist=$(crudini --get rel-eng/tito.props $tag whitelist)
	local whitelist=$(echo "$current_whitelist $PACKAGE_NAME" | tr " " "\n" | sort -u)
	crudini --set rel-eng/tito.props $tag whitelist "$whitelist"
	export LC_COLLATE=$original_locale
	git add rel-eng/tito.props
}

add_gem_to_all_comps() {
	add_gem_to_comps $TITO_TAG
	if [[ $TITO_TAG == "foreman-client-nightly-el8" ]] ; then
		add_gem_to_comps foreman-client-nightly-el9
		add_gem_to_comps foreman-client-nightly-rhel7
	fi
}

add_gem_to_comps() {
	local tag=$1
	local distro=${tag##*-}

	if [[ $distro == rhel7 ]] ; then
		if [[ $TEMPLATE_NAME == "nonscl" ]] || [[ $TEMPLATE_NAME == "smart_proxy_plugin" ]] ; then
			local comps_scl="nonscl"
			local comps_package="${PACKAGE_NAME}"
		else
			local comps_scl=""
			local comps_package="tfm-${PACKAGE_NAME}"
		fi
	else
			local comps_scl=""
			local comps_package="${PACKAGE_NAME}"
	fi

	# TODO: figure this out for katello
	if [[ $tag == foreman-plugins-* ]]; then
		local comps_file="foreman-plugins"
	else
		local comps_file="foreman"
	fi

	./add_to_comps.rb comps/comps-${comps_file}-${distro}.xml $comps_package $comps_scl
	./comps_doc.sh
	git add comps/
}

add_to_manifest() {
	if [[ $TITO_TAG == "foreman-nightly-el8" ]] ; then
		local section="foreman_core_packages"
	elif [[ $TITO_TAG == "foreman-plugins-nightly-el8" ]] ; then
		local section="foreman_plugin_packages"
	elif [[ $TITO_TAG == "katello-nightly-el8" ]] ; then
		local section="katello_packages"
	elif [[ $TITO_TAG == "foreman-client-*" ]] ; then
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
TITO_TAG=$3
PACKAGE_SUBDIR=$4
ROOT=$(git rev-parse --show-toplevel)

REWRITE_ON_SAME_VERSION=${REWRITE_ON_SAME_VERSION:-true}

if [[ -z $TEMPLATE_NAME ]] ; then
	if [[ $GEM_NAME == smart_proxy_*_core ]] ; then
		TEMPLATE_NAME="scl"
	elif [[ $GEM_NAME == smart_proxy_* ]] ; then
		TEMPLATE_NAME="smart_proxy_plugin"
	elif [[ $GEM_NAME == foreman_* ]] ; then
		TEMPLATE_NAME="foreman_plugin"
	elif [[ $GEM_NAME == hammer_* ]] ; then
		TEMPLATE_NAME="hammer_plugin"
	fi
fi

if [[ -z $TITO_TAG ]] ; then
	if [[ $TEMPLATE_NAME == smart_proxy_plugin ]] ; then
		TITO_TAG="foreman-plugins-nightly-nonscl-rhel7"
	elif [[ $TEMPLATE_NAME == *_plugin ]] ; then
		TITO_TAG="foreman-plugins-nightly-rhel7"
	elif [[ $GEM_NAME == smart_proxy_*_core ]] ; then
		TITO_TAG="foreman-plugins-nightly-rhel7"
	fi
fi

if [[ -z $PACKAGE_SUBDIR ]] ; then
	if [[ $TITO_TAG == foreman-plugins-* ]] ; then
		PACKAGE_SUBDIR="plugins"
	elif [[ $TITO_TAG == katello-* ]] ; then
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

if [[ -z $GEM_NAME ]] || [[ -z $TEMPLATE_NAME ]] || [[ $UPDATE != true ]] && [[ -z $TITO_TAG ]]; then
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
	add_to_all_tito_props
	add_gem_to_all_comps
	git commit -m "Add $PACKAGE_NAME package"
fi
