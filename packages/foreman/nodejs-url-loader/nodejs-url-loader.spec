%global npm_name url-loader

Name: nodejs-%{npm_name}
Version: 0.5.9
Release: 1%{?dist}
Summary: url loader module for webpack
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack/url-loader#readme
Source0: https://registry.npmjs.org/url-loader/-/url-loader-0.5.9.tgz
Source1: https://registry.npmjs.org/loader-utils/-/loader-utils-1.1.0.tgz
Source2: https://registry.npmjs.org/mime/-/mime-1.3.6.tgz
Source3: https://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz
Source4: https://registry.npmjs.org/big.js/-/big.js-3.2.0.tgz
Source5: https://registry.npmjs.org/json5/-/json5-0.5.1.tgz
Source6: %{npm_name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(big.js)) = 3.2.0
Provides: bundled(npm(emojis-list)) = 2.1.0
Provides: bundled(npm(json5)) = 0.5.1
Provides: bundled(npm(loader-utils)) = 1.1.0
Provides: bundled(npm(mime)) = 1.3.6
Provides: bundled(npm(url-loader)) = 0.5.9
AutoReq: no
AutoProv: no

%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}

%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done
%setup -T -q -a 6 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 0.5.9-1
- Update to 0.5.9

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 0.5.7-3
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 0.5.7-2
- Only symlink peer deps from sitelib (dominic@cleal.org)

* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 0.5.7-1
- new package built with tito

