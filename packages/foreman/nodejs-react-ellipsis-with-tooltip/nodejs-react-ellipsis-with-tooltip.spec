%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name react-ellipsis-with-tooltip

Name: %{?scl_prefix}nodejs-react-ellipsis-with-tooltip
Version: 1.1.1
Release: 1%{?dist}
Summary: truncates (with ellipsis) overflowing text elements and adds a tooltip https://amirfefer
License: MIT
Group: Development/Libraries
URL: https://github.com/amirfefer/react-ellipsis-with-tooltip#readme
Source0: https://registry.npmjs.org/react-ellipsis-with-tooltip/-/react-ellipsis-with-tooltip-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(uuid) >= 3.1.0
Requires: npm(uuid) < 4.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc readme.md

%changelog
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
