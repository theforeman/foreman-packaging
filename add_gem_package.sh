#!/bin/bash -e

GEM_NAME=$1
PACKAGE_NAME=rubygem-$GEM_NAME
TEMPLATE_NAME=$2
TEMPLATE=gem2rpm/$TEMPLATE_NAME.spec.erb
TITO_TAG=$3
DISTRO=${TITO_TAG##*-}

usage() {
	echo "Usage: $0 GEM_NAME TEMPLATE TITO_TAG"
	echo "Valid templates: $(ls gem2rpm | sed 's/.spec.erb//' | tr '\n' ' ')"
	python -c "import ConfigParser ; c = ConfigParser.ConfigParser() ; c.read('rel-eng/tito.props') ; print 'Tito tags: ' + ' '.join(s for s in c.sections() if s not in ('requirements', 'buildconfig', 'builder'))"
	exit 1
}

generate_gem_package() {
	mkdir $PACKAGE_NAME
	pushd $PACKAGE_NAME
	gem2rpm -o $PACKAGE_NAME.spec --fetch $GEM_NAME -t ../$TEMPLATE
	git annex add *.gem
	git add $PACKAGE_NAME.spec
	popd
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

add_gem_to_comps() {
	if [[ $TEMPLATE_NAME == "nonscl" ]] || [[ $TEMPLATE_NAME == "smart_proxy_plugin" ]] ; then
		local comps_scl="nonscl"
		local comps_package="${PACKAGE_NAME}"
	else
		local comps_scl=""
		local comps_package="tfm-${PACKAGE_NAME}"
	fi

	# TODO: scl or non-scl could still only be needed for plugins
	if [[ $TEMPLATE_NAME == "*_plugin" ]] ; then
		local comps_file="foreman-plugins"
	else
		local comps_file="foreman"
	fi

	./add_to_comps.rb comps/comps-${comps_file}-${DISTRO}.xml $comps_package $comps_scl
	./comps_doc.sh
	git add comps/
}

commit() {
	git commit -m "Add $PACKAGE_NAME package"
}

# Main script

if [[ -z $GEM_NAME ]] || [[ -z $TEMPLATE_NAME ]] || [[ -z $TITO_TAG ]]; then
	usage
fi

if [[ ! -e $TEMPLATE ]] ; then
	echo "Template $TEMPLATE does not exist."
	usage
	exit 1
fi

generate_gem_package
add_to_tito_props
add_gem_to_comps
commit
