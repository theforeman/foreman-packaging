%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name sass-loader

Name: %{?scl_prefix}nodejs-sass-loader
Version: 6.0.7
Release: 3%{?dist}
Summary: Sass loader for webpack
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack-contrib/sass-loader
Source0: https://registry.npmjs.org/big.js/-/big.js-5.2.2.tgz
Source1: https://registry.npmjs.org/clone-deep/-/clone-deep-2.0.2.tgz
Source2: https://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz
Source3: https://registry.npmjs.org/for-in/-/for-in-0.1.8.tgz
Source4: https://registry.npmjs.org/for-in/-/for-in-1.0.2.tgz
Source5: https://registry.npmjs.org/for-own/-/for-own-1.0.0.tgz
Source6: https://registry.npmjs.org/is-extendable/-/is-extendable-0.1.1.tgz
Source7: https://registry.npmjs.org/is-plain-object/-/is-plain-object-2.0.4.tgz
Source8: https://registry.npmjs.org/isobject/-/isobject-3.0.1.tgz
Source9: https://registry.npmjs.org/json5/-/json5-1.0.1.tgz
Source10: https://registry.npmjs.org/kind-of/-/kind-of-5.1.0.tgz
Source11: https://registry.npmjs.org/kind-of/-/kind-of-6.0.2.tgz
Source12: https://registry.npmjs.org/loader-utils/-/loader-utils-1.2.3.tgz
Source13: https://registry.npmjs.org/lodash.tail/-/lodash.tail-4.1.1.tgz
Source14: https://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz
Source15: https://registry.npmjs.org/mixin-object/-/mixin-object-2.0.1.tgz
Source16: https://registry.npmjs.org/neo-async/-/neo-async-2.6.1.tgz
Source17: https://registry.npmjs.org/pify/-/pify-3.0.0.tgz
Source18: https://registry.npmjs.org/sass-loader/-/sass-loader-6.0.7.tgz
Source19: https://registry.npmjs.org/shallow-clone/-/shallow-clone-1.0.0.tgz
Source20: nodejs-sass-loader-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(big.js)) = 5.2.2
Provides: bundled(npm(clone-deep)) = 2.0.2
Provides: bundled(npm(emojis-list)) = 2.1.0
Provides: bundled(npm(for-in)) = 0.1.8
Provides: bundled(npm(for-in)) = 1.0.2
Provides: bundled(npm(for-own)) = 1.0.0
Provides: bundled(npm(is-extendable)) = 0.1.1
Provides: bundled(npm(is-plain-object)) = 2.0.4
Provides: bundled(npm(isobject)) = 3.0.1
Provides: bundled(npm(json5)) = 1.0.1
Provides: bundled(npm(kind-of)) = 5.1.0
Provides: bundled(npm(kind-of)) = 6.0.2
Provides: bundled(npm(loader-utils)) = 1.2.3
Provides: bundled(npm(lodash.tail)) = 4.1.1
Provides: bundled(npm(minimist)) = 1.2.0
Provides: bundled(npm(mixin-object)) = 2.0.1
Provides: bundled(npm(neo-async)) = 2.6.1
Provides: bundled(npm(pify)) = 3.0.0
Provides: bundled(npm(sass-loader)) = 6.0.7
Provides: bundled(npm(shallow-clone)) = 1.0.0
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

%setup -T -q -a 20 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.0.7-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.0.7-2
- Update specs to handle SCL

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 6.0.7-1
- Update to 6.0.7

* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.0.6-1
- Update nodejs-sass-loader to 6.0.6 (ewoud@kohlvanwijngaarden.nl)

* Tue Feb 28 2017 Dominic Cleal <dominic@cleal.org> 4.1.1-1
- new package built with tito
