%global npm_name file-loader

Name: nodejs-%{npm_name}
Version: 0.9.0
Release: 3%{?dist}
Summary: file loader module for webpack
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack/file-loader
Source0: http://registry.npmjs.org/file-loader/-/file-loader-0.9.0.tgz
Source1: http://registry.npmjs.org/loader-utils/-/loader-utils-0.2.15.tgz
Source2: http://registry.npmjs.org/emojis-list/-/emojis-list-2.0.1.tgz
Source3: http://registry.npmjs.org/big.js/-/big.js-3.1.3.tgz
Source4: http://registry.npmjs.org/object-assign/-/object-assign-4.1.0.tgz
Source5: http://registry.npmjs.org/json5/-/json5-0.5.0.tgz
Source6: file-loader-0.9.0-registry.npmjs.org.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildArch: noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif
Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(file-loader) = 0.9.0
Provides: bundled-npm(loader-utils) = 0.2.15
Provides: bundled-npm(emojis-list) = 2.0.1
Provides: bundled-npm(big.js) = 3.1.3
Provides: bundled-npm(object-assign) = 4.1.0
Provides: bundled-npm(json5) = 0.5.0
AutoReq: no
AutoProv: no


%description
file loader module for webpack

%package doc
Summary: Documentation for nodejs-%{npm_name}
Group: Documentation
Requires: nodejs-%{npm_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for nodejs-%{npm_name}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 6 -D -n npm_cache

%build
npm install --cache-min Infinity --cache . --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/file-loader
cp -pfr README.md index.js package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf README.md ../../

%check

%files
%{nodejs_sitelib}/%{npm_name}

%doc

%files doc
%doc README.md

%changelog
* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 0.9.0-2
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 0.9.0-1
- new package built with tito

