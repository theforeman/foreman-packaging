%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name babel-preset-react

Name: %{?scl_prefix}nodejs-babel-preset-react
Version: 6.24.1
Release: 5%{?dist}
Summary: Babel preset for all React plugins
License: MIT
Group: Development/Libraries
URL: https://babeljs.io/
Source0: https://registry.npmjs.org/babel-helper-builder-react-jsx/-/babel-helper-builder-react-jsx-6.26.0.tgz
Source1: https://registry.npmjs.org/babel-plugin-syntax-flow/-/babel-plugin-syntax-flow-6.18.0.tgz
Source2: https://registry.npmjs.org/babel-plugin-syntax-jsx/-/babel-plugin-syntax-jsx-6.18.0.tgz
Source3: https://registry.npmjs.org/babel-plugin-transform-flow-strip-types/-/babel-plugin-transform-flow-strip-types-6.22.0.tgz
Source4: https://registry.npmjs.org/babel-plugin-transform-react-display-name/-/babel-plugin-transform-react-display-name-6.25.0.tgz
Source5: https://registry.npmjs.org/babel-plugin-transform-react-jsx/-/babel-plugin-transform-react-jsx-6.24.1.tgz
Source6: https://registry.npmjs.org/babel-plugin-transform-react-jsx-self/-/babel-plugin-transform-react-jsx-self-6.22.0.tgz
Source7: https://registry.npmjs.org/babel-plugin-transform-react-jsx-source/-/babel-plugin-transform-react-jsx-source-6.22.0.tgz
Source8: https://registry.npmjs.org/babel-preset-flow/-/babel-preset-flow-6.23.0.tgz
Source9: https://registry.npmjs.org/babel-preset-react/-/babel-preset-react-6.24.1.tgz
Source10: https://registry.npmjs.org/babel-runtime/-/babel-runtime-6.26.0.tgz
Source11: https://registry.npmjs.org/babel-types/-/babel-types-6.26.0.tgz
Source12: https://registry.npmjs.org/core-js/-/core-js-2.6.9.tgz
Source13: https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz
Source14: https://registry.npmjs.org/lodash/-/lodash-4.17.15.tgz
Source15: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.11.1.tgz
Source16: https://registry.npmjs.org/to-fast-properties/-/to-fast-properties-1.0.3.tgz
Source17: nodejs-babel-preset-react-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(babel-helper-builder-react-jsx)) = 6.26.0
Provides: bundled(npm(babel-plugin-syntax-flow)) = 6.18.0
Provides: bundled(npm(babel-plugin-syntax-jsx)) = 6.18.0
Provides: bundled(npm(babel-plugin-transform-flow-strip-types)) = 6.22.0
Provides: bundled(npm(babel-plugin-transform-react-display-name)) = 6.25.0
Provides: bundled(npm(babel-plugin-transform-react-jsx)) = 6.24.1
Provides: bundled(npm(babel-plugin-transform-react-jsx-self)) = 6.22.0
Provides: bundled(npm(babel-plugin-transform-react-jsx-source)) = 6.22.0
Provides: bundled(npm(babel-preset-flow)) = 6.23.0
Provides: bundled(npm(babel-preset-react)) = 6.24.1
Provides: bundled(npm(babel-runtime)) = 6.26.0
Provides: bundled(npm(babel-types)) = 6.26.0
Provides: bundled(npm(core-js)) = 2.6.9
Provides: bundled(npm(esutils)) = 2.0.3
Provides: bundled(npm(lodash)) = 4.17.15
Provides: bundled(npm(regenerator-runtime)) = 0.11.1
Provides: bundled(npm(to-fast-properties)) = 1.0.3
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

%setup -T -q -a 17 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --legacy-peer-deps --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
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
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Feb 01 2024 Eric D. Helms <ericdhelms@gmail.com> - 6.24.1-5
- Use --legacy-peer-deps during npm install

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 6.24.1-4
- Bump packages to build for el8

* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.24.1-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.24.1-2
- Update specs to handle SCL

* Thu Apr 26 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.24.1-1
- Update to 6.24.1

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 6.16.0-1
- new package built with tito
