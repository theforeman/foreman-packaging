%global npm_name react-dom

Name: nodejs-react-dom
Version: 16.8.1
Release: 1%{?dist}
Summary: React package for working with the DOM
License: MIT
Group: Development/Libraries
URL: https://reactjs.org/
Source0: https://registry.npmjs.org/react-dom/-/react-dom-16.8.1.tgz
Source1: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source2: https://registry.npmjs.org/prop-types/-/prop-types-15.7.1.tgz
Source3: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source4: https://registry.npmjs.org/scheduler/-/scheduler-0.13.1.tgz
Source5: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source6: https://registry.npmjs.org/react-is/-/react-is-16.8.1.tgz
Source7: %{name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(prop-types)) = 15.7.1
Provides: bundled(npm(react-dom)) = 16.8.1
Provides: bundled(npm(react-is)) = 16.8.1
Provides: bundled(npm(scheduler)) = 0.13.1
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
%setup -T -q -a 7 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/build-info.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/cjs %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/profiling.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/server.browser.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/server.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/server.node.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/test-utils.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/umd %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/unstable-fizz.browser.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/unstable-fizz.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/unstable-fizz.node.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/unstable-native-dependencies.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Mon Feb 11 2019 Ohad Levy <ohadlevy@gmail.com> 16.8.1-1
- Update to 16.8.1

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 16.4.0-1
- Update to 16.4.0

* Thu Jan 04 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 16.2.0-1
- Update nodejs-react-dom to 16.2 (me@daniellobato.me)

* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 16.0.0-1
- Update nodejs-react-dom to 16.0.0 (ewoud@kohlvanwijngaarden.nl)

* Thu Oct 05 2017 Eric D. Helms <ericdhelms@gmail.com> 15.6.2-1
- Update react-dom to 15.6.2 (me@daniellobato.me)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 15.3.2-1
- new package built with tito
