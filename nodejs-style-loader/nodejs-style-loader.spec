%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name style-loader

%{?nodejs_find_provides_and_requires}

Name: %{?scl_prefix}nodejs-%{npm_name}
Version: 0.13.1
Release: 1%{?dist}
Summary: style loader module for webpack
License: MIT
URL: https://www.npmjs.com/package/style-loader
Source0: http://registry.npmjs.org/style-loader/-/style-loader-0.13.1.tgz
Source1: http://registry.npmjs.org/loader-utils/-/loader-utils-0.2.15.tgz
Source2: http://registry.npmjs.org/emojis-list/-/emojis-list-2.0.1.tgz
Source3: http://registry.npmjs.org/big.js/-/big.js-3.1.3.tgz
Source4: http://registry.npmjs.org/json5/-/json5-0.5.0.tgz
Source5: http://registry.npmjs.org/object-assign/-/object-assign-4.1.0.tgz
Source6: style-loader-0.13.1-registry.npmjs.org.tgz
Requires: %{?scl_prefix_nodejs}nodejs(engine)
BuildRequires: %{?scl_prefix_nodejs}npm
BuildArch: noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled-npm(style-loader) = 0.13.1
Provides: bundled-npm(loader-utils) = 0.2.15
Provides: bundled-npm(emojis-list) = 2.0.1
Provides: bundled-npm(big.js) = 3.1.3
Provides: bundled-npm(json5) = 0.5.0
Provides: bundled-npm(object-assign) = 4.1.0
AutoReq: no
AutoProv: no


%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  if [ $(echo $tgz | grep -q registry.npmjs.org) ];then
%{?scl:scl enable %{scl} - <<EOF}
npm cache add --cache ./npm_cache $tgz
%{?scl:EOF}
  fi
done

%setup -T -q -a 6 -D -n npm_cache

%build
%{?scl:scl enable %{scl} - <<EOF}
npm install --cache-min Infinity --cache . %{npm_name}@%{version}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/style-loader
cp -pfr .npmignore README.md addStyleUrl.js addStyles.js index.js package.json url.js useable.js node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr README.md ../../

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 0.13.1-1
- new package built with tito

