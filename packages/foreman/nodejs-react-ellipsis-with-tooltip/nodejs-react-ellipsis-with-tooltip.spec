%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name react-ellipsis-with-tooltip

Name: %{?scl_prefix}nodejs-react-ellipsis-with-tooltip
Version: 1.0.8
Release: 1%{?dist}
Summary: truncates (with ellipsis) overflowing text elements and adds a tooltip
License: MIT
Group: Development/Libraries
URL: https://github.com/amirfefer/react-ellipsis-with-tooltip
Source0: https://registry.npmjs.org/react-ellipsis-with-tooltip/-/react-ellipsis-with-tooltip-1.0.8.tgz
Source1: https://registry.npmjs.org/uuid/-/uuid-3.4.0.tgz
Source2: nodejs-react-ellipsis-with-tooltip-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(react-ellipsis-with-tooltip)) = 1.0.8
Provides: bundled(npm(uuid)) = 3.4.0
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

%setup -T -q -a 2 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --legacy-peer-deps --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/src %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/stories %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Jun 19 2025 MariaAga <mariaaga@redhat.com> 1.0.8-1
- Update to 1.0.8

* Sun Sep 10 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.1.1-1
- Update to 1.1.1

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.8-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.0.8-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.0.8-2
- Update specs to handle SCL

* Mon May 14 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.8-1
- Update to 1.0.8

* Tue Jan 30 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.7-1
- Bump nodejs-react-ellipsis-with-tooltip to 1.0.7
  (ewoud@kohlvanwijngaarden.nl)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.6-1
- new package built with tito
