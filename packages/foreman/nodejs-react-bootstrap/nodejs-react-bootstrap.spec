%global npm_name react-bootstrap

Name: nodejs-react-bootstrap
Version: 0.33.1
Release: 3%{?dist}
Summary: Bootstrap 3 components built with React
License: MIT
Group: Development/Libraries
URL: https://react-bootstrap.github.io/
Source0: https://registry.npmjs.org/@babel/runtime/-/runtime-7.29.7.tgz
Source1: https://registry.npmjs.org/@babel/runtime-corejs2/-/runtime-corejs2-7.29.7.tgz
Source2: https://registry.npmjs.org/@types/react/-/react-19.2.17.tgz
Source3: https://registry.npmjs.org/classnames/-/classnames-2.5.1.tgz
Source4: https://registry.npmjs.org/core-js/-/core-js-2.6.12.tgz
Source5: https://registry.npmjs.org/csstype/-/csstype-3.2.3.tgz
Source6: https://registry.npmjs.org/dom-helpers/-/dom-helpers-3.4.0.tgz
Source7: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source8: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source9: https://registry.npmjs.org/keycode/-/keycode-2.2.1.tgz
Source10: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source11: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source12: https://registry.npmjs.org/prop-types/-/prop-types-15.8.1.tgz
Source13: https://registry.npmjs.org/prop-types-extra/-/prop-types-extra-1.1.1.tgz
Source14: https://registry.npmjs.org/react-bootstrap/-/react-bootstrap-0.33.1.tgz
Source15: https://registry.npmjs.org/react-is/-/react-is-16.13.1.tgz
Source16: https://registry.npmjs.org/react-lifecycles-compat/-/react-lifecycles-compat-3.0.4.tgz
Source17: https://registry.npmjs.org/react-overlays/-/react-overlays-0.9.3.tgz
Source18: https://registry.npmjs.org/react-prop-types/-/react-prop-types-0.4.0.tgz
Source19: https://registry.npmjs.org/react-transition-group/-/react-transition-group-2.9.0.tgz
Source20: https://registry.npmjs.org/uncontrollable/-/uncontrollable-7.2.1.tgz
Source21: https://registry.npmjs.org/warning/-/warning-3.0.0.tgz
Source22: https://registry.npmjs.org/warning/-/warning-4.0.3.tgz
Source23: nodejs-react-bootstrap-%{version}-registry.npmjs.org.tgz
BuildRequires: npm >= 7
BuildRequires: nodejs-packaging
%if 0%{?rhel} == 10
# https://issues.redhat.com/browse/RHEL-137712
BuildRequires: /usr/bin/node
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/runtime)) = 7.29.7
Provides: bundled(npm(@babel/runtime-corejs2)) = 7.29.7
Provides: bundled(npm(@types/react)) = 19.2.17
Provides: bundled(npm(classnames)) = 2.5.1
Provides: bundled(npm(core-js)) = 2.6.12
Provides: bundled(npm(csstype)) = 3.2.3
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
Provides: bundled(npm(uncontrollable)) = 7.2.1
Provides: bundled(npm(warning)) = 3.0.0
Provides: bundled(npm(warning)) = 4.0.3
AutoReq: no
AutoProv: no

%define npm_cache_dir npm_cache_%{name}-%{version}-%{release}

%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done

%setup -T -q -a 23 -D -n %{npm_cache_dir}

%build
npm install --legacy-peer-deps --offline --cache %{_builddir}/%{npm_cache_dir} --package-lock false --omit optional --install-strategy shallow %{npm_name}@%{version}

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
* Sat Jun 06 2026 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.33.1-3
- Regenerate spec file

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
