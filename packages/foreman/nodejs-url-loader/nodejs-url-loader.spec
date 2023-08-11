%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name url-loader

Name: %{?scl_prefix}nodejs-url-loader
Version: 1.1.2
Release: 1%{?dist}
Summary: A loader for webpack which transforms files into base64 URIs
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack-contrib/url-loader
Source0: https://registry.npmjs.org/ajv/-/ajv-6.12.6.tgz
Source1: https://registry.npmjs.org/ajv-errors/-/ajv-errors-1.0.1.tgz
Source2: https://registry.npmjs.org/ajv-keywords/-/ajv-keywords-3.5.2.tgz
Source3: https://registry.npmjs.org/big.js/-/big.js-5.2.2.tgz
Source4: https://registry.npmjs.org/emojis-list/-/emojis-list-3.0.0.tgz
Source5: https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz
Source6: https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz
Source7: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz
Source8: https://registry.npmjs.org/json5/-/json5-1.0.2.tgz
Source9: https://registry.npmjs.org/loader-utils/-/loader-utils-1.4.2.tgz
Source10: https://registry.npmjs.org/mime/-/mime-2.6.0.tgz
Source11: https://registry.npmjs.org/minimist/-/minimist-1.2.8.tgz
Source12: https://registry.npmjs.org/punycode/-/punycode-2.3.0.tgz
Source13: https://registry.npmjs.org/schema-utils/-/schema-utils-1.0.0.tgz
Source14: https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz
Source15: https://registry.npmjs.org/url-loader/-/url-loader-1.1.2.tgz
Source16: nodejs-url-loader-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(ajv)) = 6.12.6
Provides: bundled(npm(ajv-errors)) = 1.0.1
Provides: bundled(npm(ajv-keywords)) = 3.5.2
Provides: bundled(npm(big.js)) = 5.2.2
Provides: bundled(npm(emojis-list)) = 3.0.0
Provides: bundled(npm(fast-deep-equal)) = 3.1.3
Provides: bundled(npm(fast-json-stable-stringify)) = 2.1.0
Provides: bundled(npm(json-schema-traverse)) = 0.4.1
Provides: bundled(npm(json5)) = 1.0.2
Provides: bundled(npm(loader-utils)) = 1.4.2
Provides: bundled(npm(mime)) = 2.6.0
Provides: bundled(npm(minimist)) = 1.2.8
Provides: bundled(npm(punycode)) = 2.3.0
Provides: bundled(npm(schema-utils)) = 1.0.0
Provides: bundled(npm(uri-js)) = 4.4.1
Provides: bundled(npm(url-loader)) = 1.1.2
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

%setup -T -q -a 16 -D -n %{npm_cache_dir}

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
* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.1.2-1
- Update to 1.1.2

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.1-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.0.1-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.0.1-2
- Update specs to handle SCL

* Tue Jun 19 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.1-1
- Update to 1.0.1

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 0.5.9-1
- Update to 0.5.9

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 0.5.7-3
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 0.5.7-2
- Only symlink peer deps from sitelib (dominic@cleal.org)

* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 0.5.7-1
- new package built with tito
