%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name react-bootstrap

Name: %{?scl_prefix}nodejs-react-bootstrap
Version: 0.33.1
Release: 2%{?dist}
Summary: Bootstrap 3 components built with React
License: MIT
Group: Development/Libraries
URL: https://react-bootstrap.github.io/
Source0: https://registry.npmjs.org/@babel/runtime/-/runtime-7.21.5.tgz
Source1: https://registry.npmjs.org/@babel/runtime-corejs2/-/runtime-corejs2-7.21.5.tgz
Source2: https://registry.npmjs.org/@types/prop-types/-/prop-types-15.7.5.tgz
Source3: https://registry.npmjs.org/@types/react/-/react-18.2.5.tgz
Source4: https://registry.npmjs.org/@types/scheduler/-/scheduler-0.16.3.tgz
Source5: https://registry.npmjs.org/classnames/-/classnames-2.3.2.tgz
Source6: https://registry.npmjs.org/core-js/-/core-js-2.6.12.tgz
Source7: https://registry.npmjs.org/csstype/-/csstype-3.1.2.tgz
Source8: https://registry.npmjs.org/dom-helpers/-/dom-helpers-3.4.0.tgz
Source9: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source10: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source11: https://registry.npmjs.org/keycode/-/keycode-2.2.1.tgz
Source12: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source13: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source14: https://registry.npmjs.org/prop-types/-/prop-types-15.8.1.tgz
Source15: https://registry.npmjs.org/prop-types-extra/-/prop-types-extra-1.1.1.tgz
Source16: https://registry.npmjs.org/react-bootstrap/-/react-bootstrap-0.33.1.tgz
Source17: https://registry.npmjs.org/react-is/-/react-is-16.13.1.tgz
Source18: https://registry.npmjs.org/react-lifecycles-compat/-/react-lifecycles-compat-3.0.4.tgz
Source19: https://registry.npmjs.org/react-overlays/-/react-overlays-0.9.3.tgz
Source20: https://registry.npmjs.org/react-prop-types/-/react-prop-types-0.4.0.tgz
Source21: https://registry.npmjs.org/react-transition-group/-/react-transition-group-2.9.0.tgz
Source22: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.13.11.tgz
Source23: https://registry.npmjs.org/uncontrollable/-/uncontrollable-7.2.1.tgz
Source24: https://registry.npmjs.org/warning/-/warning-3.0.0.tgz
Source25: https://registry.npmjs.org/warning/-/warning-4.0.3.tgz
Source26: nodejs-react-bootstrap-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/runtime)) = 7.21.5
Provides: bundled(npm(@babel/runtime-corejs2)) = 7.21.5
Provides: bundled(npm(@types/prop-types)) = 15.7.5
Provides: bundled(npm(@types/react)) = 18.2.5
Provides: bundled(npm(@types/scheduler)) = 0.16.3
Provides: bundled(npm(classnames)) = 2.3.2
Provides: bundled(npm(core-js)) = 2.6.12
Provides: bundled(npm(csstype)) = 3.1.2
Provides: bundled(npm(dom-helpers)) = 3.4.0
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(keycode)) = 2.2.1
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(prop-types-extra)) = 1.1.1
Provides: bundled(npm(react-bootstrap)) = 0.33.1
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(react-lifecycles-compat)) = 3.0.4
Provides: bundled(npm(react-overlays)) = 0.9.3
Provides: bundled(npm(react-prop-types)) = 0.4.0
Provides: bundled(npm(react-transition-group)) = 2.9.0
Provides: bundled(npm(regenerator-runtime)) = 0.13.11
Provides: bundled(npm(uncontrollable)) = 7.2.1
Provides: bundled(npm(warning)) = 3.0.0
Provides: bundled(npm(warning)) = 4.0.3
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

%setup -T -q -a 26 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --legacy-peer-deps --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/es %{buildroot}%{nodejs_sitelib}/%{npm_name}
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
* Thu Feb 01 2024 Eric D. Helms <ericdhelms@gmail.com> - 0.33.1-2
- Use --legacy-peer-deps during npm install

* Thu May 04 2023 Eric D. Helms <ericdhelms@gmail.com> 0.33.1-1
- Update to 0.33.1

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.32.1-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.32.1-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.32.1-2
- Update specs to handle SCL

* Tue May 01 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.32.1-1
- Update to 0.32.1

* Wed Nov 08 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.31.5-1
- Bump nodejs-react-bootstrap to 0.31.5 (#1936) (github@kohlvanwijngaarden.nl)

* Thu May 11 2017 Dominic Cleal <dominic@cleal.org> 0.31.0-1
- Update react-bootstrap to 0.31.0 (dominic@cleal.org)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 0.30.5-2
- Use existing react, react-dom peer dependencies (dominic@cleal.org)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 0.30.5-1
- new package built with tito
