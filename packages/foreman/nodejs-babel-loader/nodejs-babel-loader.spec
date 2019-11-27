%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name babel-loader

Name: %{?scl_prefix}nodejs-babel-loader
Version: 8.0.6
Release: 1%{?dist}
Summary: babel module loader for webpack
License: MIT
Group: Development/Libraries
URL: https://github.com/babel/babel-loader
Source0: https://registry.npmjs.org/babel-loader/-/babel-loader-8.0.6.tgz
Source1: https://registry.npmjs.org/big.js/-/big.js-5.2.2.tgz
Source2: https://registry.npmjs.org/commondir/-/commondir-1.0.1.tgz
Source3: https://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz
Source4: https://registry.npmjs.org/find-cache-dir/-/find-cache-dir-2.1.0.tgz
Source5: https://registry.npmjs.org/find-up/-/find-up-3.0.0.tgz
Source6: https://registry.npmjs.org/json5/-/json5-1.0.1.tgz
Source7: https://registry.npmjs.org/loader-utils/-/loader-utils-1.2.3.tgz
Source8: https://registry.npmjs.org/locate-path/-/locate-path-3.0.0.tgz
Source9: https://registry.npmjs.org/make-dir/-/make-dir-2.1.0.tgz
Source10: https://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source11: https://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz
Source12: https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source13: https://registry.npmjs.org/p-limit/-/p-limit-2.2.1.tgz
Source14: https://registry.npmjs.org/p-locate/-/p-locate-3.0.0.tgz
Source15: https://registry.npmjs.org/p-try/-/p-try-2.2.0.tgz
Source16: https://registry.npmjs.org/path-exists/-/path-exists-3.0.0.tgz
Source17: https://registry.npmjs.org/pify/-/pify-4.0.1.tgz
Source18: https://registry.npmjs.org/pkg-dir/-/pkg-dir-3.0.0.tgz
Source19: https://registry.npmjs.org/semver/-/semver-5.7.1.tgz
Source20: nodejs-babel-loader-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(babel-loader)) = 8.0.6
Provides: bundled(npm(big.js)) = 5.2.2
Provides: bundled(npm(commondir)) = 1.0.1
Provides: bundled(npm(emojis-list)) = 2.1.0
Provides: bundled(npm(find-cache-dir)) = 2.1.0
Provides: bundled(npm(find-up)) = 3.0.0
Provides: bundled(npm(json5)) = 1.0.1
Provides: bundled(npm(loader-utils)) = 1.2.3
Provides: bundled(npm(locate-path)) = 3.0.0
Provides: bundled(npm(make-dir)) = 2.1.0
Provides: bundled(npm(minimist)) = 0.0.8
Provides: bundled(npm(minimist)) = 1.2.0
Provides: bundled(npm(mkdirp)) = 0.5.1
Provides: bundled(npm(p-limit)) = 2.2.1
Provides: bundled(npm(p-locate)) = 3.0.0
Provides: bundled(npm(p-try)) = 2.2.0
Provides: bundled(npm(path-exists)) = 3.0.0
Provides: bundled(npm(pify)) = 4.0.1
Provides: bundled(npm(pkg-dir)) = 3.0.0
Provides: bundled(npm(semver)) = 5.7.1
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
* Wed Nov 27 2019 Evgeni Golov 8.0.6-1
- Update to 8.0.6

* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 7.1.4-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 7.1.4-2
- Update specs to handle SCL

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 7.1.4-1
- Update to 7.1.4

* Tue Jul 25 2017 Michael Moll <kvedulv@kvedulv.de> 7.1.1-2
- Add missing provides to nodejs-babel-loader (eric.d.helms@gmail.com)

* Tue Jul 25 2017 Michael Moll <kvedulv@kvedulv.de> 7.1.1-1
- Bump babel-loader to 7.1.1 (eric.d.helms@gmail.com)

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 6.2.4-2
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 6.2.4-1
- new package built with tito
