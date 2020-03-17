%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name extract-text-webpack-plugin

Name: %{?scl_prefix}nodejs-extract-text-webpack-plugin
Version: 3.0.2
Release: 4%{?dist}
Summary: Extract text from bundle into a file
License: MIT
Group: Development/Libraries
URL: http://github.com/webpack-contrib/extract-text-webpack-plugin
Source0: https://registry.npmjs.org/ajv/-/ajv-5.5.2.tgz
Source1: https://registry.npmjs.org/async/-/async-2.6.3.tgz
Source2: https://registry.npmjs.org/big.js/-/big.js-5.2.2.tgz
Source3: https://registry.npmjs.org/co/-/co-4.6.0.tgz
Source4: https://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz
Source5: https://registry.npmjs.org/extract-text-webpack-plugin/-/extract-text-webpack-plugin-3.0.2.tgz
Source6: https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-1.1.0.tgz
Source7: https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.0.0.tgz
Source8: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.3.1.tgz
Source9: https://registry.npmjs.org/json5/-/json5-1.0.1.tgz
Source10: https://registry.npmjs.org/loader-utils/-/loader-utils-1.2.3.tgz
Source11: https://registry.npmjs.org/lodash/-/lodash-4.17.15.tgz
Source12: https://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz
Source13: https://registry.npmjs.org/schema-utils/-/schema-utils-0.3.0.tgz
Source14: https://registry.npmjs.org/source-list-map/-/source-list-map-2.0.1.tgz
Source15: https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz
Source16: https://registry.npmjs.org/webpack-sources/-/webpack-sources-1.4.3.tgz
Source17: nodejs-extract-text-webpack-plugin-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(ajv)) = 5.5.2
Provides: bundled(npm(async)) = 2.6.3
Provides: bundled(npm(big.js)) = 5.2.2
Provides: bundled(npm(co)) = 4.6.0
Provides: bundled(npm(emojis-list)) = 2.1.0
Provides: bundled(npm(extract-text-webpack-plugin)) = 3.0.2
Provides: bundled(npm(fast-deep-equal)) = 1.1.0
Provides: bundled(npm(fast-json-stable-stringify)) = 2.0.0
Provides: bundled(npm(json-schema-traverse)) = 0.3.1
Provides: bundled(npm(json5)) = 1.0.1
Provides: bundled(npm(loader-utils)) = 1.2.3
Provides: bundled(npm(lodash)) = 4.17.15
Provides: bundled(npm(minimist)) = 1.2.0
Provides: bundled(npm(schema-utils)) = 0.3.0
Provides: bundled(npm(source-list-map)) = 2.0.1
Provides: bundled(npm(source-map)) = 0.6.1
Provides: bundled(npm(webpack-sources)) = 1.4.3
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

%setup -T -q -a 17 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/schema %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.0.2-4
- Bump packages to build for el8

* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.0.2-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.0.2-2
- Update specs to handle SCL

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 3.0.2-1
- Update to 3.0.2

* Wed Jul 26 2017 Eric D. Helms <ericdhelms@gmail.com> 3.0.0-1
- Update nodejs-extract-text-webpack to 3.0 (me@daniellobato.me)

* Sat Jul 15 2017 Eric D. Helms <ericdhelms@gmail.com> 2.1.2-2
- Add back missing Provides: npm (ericdhelms@gmail.com)

* Sat Jul 15 2017 Eric D. Helms <ericdhelms@gmail.com> 2.1.2-1
- update webpack to v3.0 (ohadlevy@gmail.com)

* Sat Jul 15 2017 Eric D. Helms <ericdhelms@gmail.com>
- update webpack to v3.0 (ohadlevy@gmail.com)

* Sat Jul 15 2017 Eric D. Helms <ericdhelms@gmail.com>
- update webpack to v3.0 (ohadlevy@gmail.com)
