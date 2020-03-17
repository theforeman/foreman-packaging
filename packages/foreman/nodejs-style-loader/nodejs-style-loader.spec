%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name style-loader

Name: %{?scl_prefix}nodejs-style-loader
Version: 0.13.2
Release: 4%{?dist}
Summary: style loader module for webpack
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack/style-loader#readme
Source0: https://registry.npmjs.org/big.js/-/big.js-5.2.2.tgz
Source1: https://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz
Source2: https://registry.npmjs.org/json5/-/json5-1.0.1.tgz
Source3: https://registry.npmjs.org/loader-utils/-/loader-utils-1.2.3.tgz
Source4: https://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz
Source5: https://registry.npmjs.org/style-loader/-/style-loader-0.13.2.tgz
Source6: nodejs-style-loader-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(big.js)) = 5.2.2
Provides: bundled(npm(emojis-list)) = 2.1.0
Provides: bundled(npm(json5)) = 1.0.1
Provides: bundled(npm(loader-utils)) = 1.2.3
Provides: bundled(npm(minimist)) = 1.2.0
Provides: bundled(npm(style-loader)) = 0.13.2
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

%setup -T -q -a 6 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/addStyleUrl.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/addStyles.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/url.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/useable.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
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
