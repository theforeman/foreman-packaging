%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name react-redux

Name: %{?scl_prefix}nodejs-react-redux
Version: 5.1.1
Release: 4%{?dist}
Summary: Official React bindings for Redux
License: MIT
Group: Development/Libraries
URL: https://github.com/reduxjs/react-redux
Source0: https://registry.npmjs.org/@babel/runtime/-/runtime-7.6.2.tgz
Source1: https://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-3.3.0.tgz
Source2: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source3: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source4: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source5: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source6: https://registry.npmjs.org/prop-types/-/prop-types-15.7.2.tgz
Source7: https://registry.npmjs.org/react-is/-/react-is-16.10.2.tgz
Source8: https://registry.npmjs.org/react-lifecycles-compat/-/react-lifecycles-compat-3.0.4.tgz
Source9: https://registry.npmjs.org/react-redux/-/react-redux-5.1.1.tgz
Source10: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.13.3.tgz
Source11: nodejs-react-redux-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/runtime)) = 7.6.2
Provides: bundled(npm(hoist-non-react-statics)) = 3.3.0
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(prop-types)) = 15.7.2
Provides: bundled(npm(react-is)) = 16.10.2
Provides: bundled(npm(react-lifecycles-compat)) = 3.0.4
Provides: bundled(npm(react-redux)) = 5.1.1
Provides: bundled(npm(regenerator-runtime)) = 0.13.3
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

%setup -T -q -a 11 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/es %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE.md
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.1.1-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 5.1.1-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 5.1.1-2
- Update specs to handle SCL

* Mon May 20 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.1.1-1
- Update to 5.1.1

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 5.0.7-1
- Update to 5.0.7

* Fri Nov 17 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.0.6-1
- Bump nodejs-react-redux to 5.0.6 (ewoud@kohlvanwijngaarden.nl)

* Thu Feb 16 2017 Dominic Cleal <dominic@cleal.org> 5.0.2-2
- Use existing react, redux peer dependencies (dominic@cleal.org)

* Thu Feb 16 2017 Dominic Cleal <dominic@cleal.org> 5.0.2-1
- new package built with tito
