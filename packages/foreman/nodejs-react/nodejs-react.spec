%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name react

Name: %{?scl_prefix}nodejs-react
Version: 16.8.1
Release: 4%{?dist}
Summary: React is a JavaScript library for building user interfaces
License: MIT
Group: Development/Libraries
URL: https://reactjs.org/
Source0: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source1: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source2: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source3: https://registry.npmjs.org/prop-types/-/prop-types-15.7.2.tgz
Source4: https://registry.npmjs.org/react/-/react-16.8.1.tgz
Source5: https://registry.npmjs.org/react-is/-/react-is-16.10.2.tgz
Source6: https://registry.npmjs.org/scheduler/-/scheduler-0.13.6.tgz
Source7: nodejs-react-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(prop-types)) = 15.7.2
Provides: bundled(npm(react)) = 16.8.1
Provides: bundled(npm(react-is)) = 16.10.2
Provides: bundled(npm(scheduler)) = 0.13.6
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

%setup -T -q -a 7 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/build-info.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/cjs %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/umd %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 16.8.1-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 16.8.1-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 16.8.1-2
- Update specs to handle SCL

* Mon Feb 11 2019 Ohad Levy <ohadlevy@gmail.com> 16.8.1-1
- Update to 16.8.1

* Wed Jun 13 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 16.4.0-1
- Update to 16.4.0

* Thu Jan 04 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 16.2.0-1
- Update nodejs-react to 16.2.0 (me@daniellobato.me)

* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 16.0.0-1
- Update nodejs-react to 16.0.0 (ewoud@kohlvanwijngaarden.nl)

* Thu Oct 05 2017 Eric D. Helms <ericdhelms@gmail.com> 15.6.2-1
- Update React to 15.6.2 (me@daniellobato.me)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 15.3.2-1
- new package built with tito
