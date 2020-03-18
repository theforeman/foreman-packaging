%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name fbjs

Name: %{?scl_prefix}nodejs-fbjs
Version: 0.8.16
Release: 4%{?dist}
Summary: A collection of utility libraries used by other Facebook JS projects
License: MIT
Group: Development/Libraries
URL: https://github.com/facebook/fbjs#readme
Source0: https://registry.npmjs.org/asap/-/asap-2.0.6.tgz
Source1: https://registry.npmjs.org/core-js/-/core-js-1.2.7.tgz
Source2: https://registry.npmjs.org/encoding/-/encoding-0.1.12.tgz
Source3: https://registry.npmjs.org/fbjs/-/fbjs-0.8.16.tgz
Source4: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.24.tgz
Source5: https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source6: https://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source7: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source8: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source9: https://registry.npmjs.org/node-fetch/-/node-fetch-1.7.3.tgz
Source10: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source11: https://registry.npmjs.org/promise/-/promise-7.3.1.tgz
Source12: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source13: https://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz
Source14: https://registry.npmjs.org/ua-parser-js/-/ua-parser-js-0.7.20.tgz
Source15: https://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-3.0.0.tgz
Source16: nodejs-fbjs-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(asap)) = 2.0.6
Provides: bundled(npm(core-js)) = 1.2.7
Provides: bundled(npm(encoding)) = 0.1.12
Provides: bundled(npm(fbjs)) = 0.8.16
Provides: bundled(npm(iconv-lite)) = 0.4.24
Provides: bundled(npm(is-stream)) = 1.1.0
Provides: bundled(npm(isomorphic-fetch)) = 2.2.1
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(node-fetch)) = 1.7.3
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(promise)) = 7.3.1
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(setimmediate)) = 1.0.5
Provides: bundled(npm(ua-parser-js)) = 0.7.20
Provides: bundled(npm(whatwg-fetch)) = 3.0.0
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
cp -pfr node_modules/%{npm_name}/flow %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/module-map.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.8.16-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.8.16-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.8.16-2
- Update specs to handle SCL

* Fri Nov 24 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.8.16-1
- Bump nodejs-fbjs to 0.8.16 (github@kohlvanwijngaarden.nl)

* Sat Jul 15 2017 Eric D. Helms <ericdhelms@gmail.com> 0.8.12-2
- Add back missing Provides: npm (ericdhelms@gmail.com)

* Sat Jul 15 2017 Eric D. Helms <ericdhelms@gmail.com> 0.8.12-1
- new package built with tito
