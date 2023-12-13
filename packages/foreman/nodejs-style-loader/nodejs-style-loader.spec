%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name style-loader

Name: %{?scl_prefix}nodejs-style-loader
Version: 1.3.0
Release: 1%{?dist}
Summary: style loader module for webpack
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack-contrib/style-loader
Source0: https://registry.npmjs.org/@types/json-schema/-/json-schema-7.0.15.tgz
Source1: https://registry.npmjs.org/ajv/-/ajv-6.12.6.tgz
Source2: https://registry.npmjs.org/ajv-keywords/-/ajv-keywords-3.5.2.tgz
Source3: https://registry.npmjs.org/big.js/-/big.js-5.2.2.tgz
Source4: https://registry.npmjs.org/emojis-list/-/emojis-list-3.0.0.tgz
Source5: https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz
Source6: https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz
Source7: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz
Source8: https://registry.npmjs.org/json5/-/json5-2.2.3.tgz
Source9: https://registry.npmjs.org/loader-utils/-/loader-utils-2.0.4.tgz
Source10: https://registry.npmjs.org/punycode/-/punycode-2.3.1.tgz
Source11: https://registry.npmjs.org/schema-utils/-/schema-utils-2.7.1.tgz
Source12: https://registry.npmjs.org/style-loader/-/style-loader-1.3.0.tgz
Source13: https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz
Source14: nodejs-style-loader-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@types/json-schema)) = 7.0.15
Provides: bundled(npm(ajv)) = 6.12.6
Provides: bundled(npm(ajv-keywords)) = 3.5.2
Provides: bundled(npm(big.js)) = 5.2.2
Provides: bundled(npm(emojis-list)) = 3.0.0
Provides: bundled(npm(fast-deep-equal)) = 3.1.3
Provides: bundled(npm(fast-json-stable-stringify)) = 2.1.0
Provides: bundled(npm(json-schema-traverse)) = 0.4.1
Provides: bundled(npm(json5)) = 2.2.3
Provides: bundled(npm(loader-utils)) = 2.0.4
Provides: bundled(npm(punycode)) = 2.3.1
Provides: bundled(npm(schema-utils)) = 2.7.1
Provides: bundled(npm(style-loader)) = 1.3.0
Provides: bundled(npm(uri-js)) = 4.4.1
AutoReq: no
AutoProv: no

%if 0%{?scl:1}
%define npm_cache_dir npm_cache
%else
%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}
%endif

%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done
%{?scl:end_of_scl}

%setup -T -q -a 14 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Wed Dec 13 2023 Evgeni Golov 1.3.0-1
- Update to 1.3.0

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.13.2-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.13.2-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.13.2-2
- Update specs to handle SCL

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 0.13.2-1
- Update to 0.13.2

* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 0.13.1-1
- new package built with tito
