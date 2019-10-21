%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name file-loader

Name: %{?scl_prefix}nodejs-file-loader
Version: 0.9.0
Release: 5%{?dist}
Summary: file loader module for webpack
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack/file-loader
Source0: https://registry.npmjs.org/big.js/-/big.js-3.2.0.tgz
Source1: https://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz
Source2: https://registry.npmjs.org/file-loader/-/file-loader-0.9.0.tgz
Source3: https://registry.npmjs.org/json5/-/json5-0.5.1.tgz
Source4: https://registry.npmjs.org/loader-utils/-/loader-utils-0.2.17.tgz
Source5: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source6: nodejs-file-loader-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(big.js)) = 3.2.0
Provides: bundled(npm(emojis-list)) = 2.1.0
Provides: bundled(npm(file-loader)) = 0.9.0
Provides: bundled(npm(json5)) = 0.5.1
Provides: bundled(npm(loader-utils)) = 0.2.17
Provides: bundled(npm(object-assign)) = 4.1.1
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
cp -pfr node_modules/%{npm_name}/index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%doc node_modules/%{npm_name}/README.md

%changelog
* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.9.0-5
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.9.0-4
- Update specs to handle SCL

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 0.9.0-2
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 0.9.0-1
- new package built with tito
