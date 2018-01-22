%global npm_name url-loader

Name: nodejs-%{npm_name}
Version: 0.5.7
Release: 4%{?dist}
Summary: url loader module for webpack
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack/url-loader
Source0: http://registry.npmjs.org/url-loader/-/url-loader-0.5.7.tgz
Source1: http://registry.npmjs.org/mime/-/mime-1.2.11.tgz
Source2: http://registry.npmjs.org/loader-utils/-/loader-utils-0.2.15.tgz
Source3: http://registry.npmjs.org/emojis-list/-/emojis-list-2.0.1.tgz
Source4: http://registry.npmjs.org/big.js/-/big.js-3.1.3.tgz
Source5: http://registry.npmjs.org/json5/-/json5-0.5.0.tgz
Source6: http://registry.npmjs.org/object-assign/-/object-assign-4.1.0.tgz
Source7: url-loader-0.5.7-registry.npmjs.org.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildRequires: npm(file-loader)
BuildArch: noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif
Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(url-loader)) = 0.5.7
Provides: bundled(npm(mime)) = 1.2.11
Provides: bundled(npm(loader-utils)) = 0.2.15
Provides: bundled(npm(emojis-list)) = 2.0.1
Provides: bundled(npm(big.js)) = 3.1.3
Provides: bundled(npm(json5)) = 0.5.0
Provides: bundled(npm(object-assign)) = 4.1.0
AutoReq: no
AutoProv: no


%description
url loader module for webpack

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

%setup -T -q -a 7 -D -n npm_cache

%build
mkdir node_modules
ln -s %{nodejs_sitelib}/file-loader node_modules/
npm install --cache-min Infinity --cache . --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/url-loader
cp -pfr .npmignore README.md index.js package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf README.md ../../

%check

%files
%{nodejs_sitelib}/%{npm_name}

%files doc
%doc README.md

%changelog
* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 0.5.7-3
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 0.5.7-2
- Only symlink peer deps from sitelib (dominic@cleal.org)

* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 0.5.7-1
- new package built with tito

