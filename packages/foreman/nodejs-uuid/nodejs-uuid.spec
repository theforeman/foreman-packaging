%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name uuid

Name: %{?scl_prefix}nodejs-uuid
Version: 13.0.0
Release: 1%{?dist}
Summary: RFC9562 UUIDs (v1, v3, v4, v5, v6, v7)
License: MIT
Group: Development/Libraries
URL: https://github.com/uuidjs/uuid#readme
Source0: https://registry.npmjs.org/uuid/-/uuid-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
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
cp -pfr dist-node %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.md
%doc README.md

%changelog
* Tue Apr 07 2026 Jakub Duchek <jakduch@seznam.cz> - 13.0.0-1
- Update to 13.0.0 (pure ESM, RFC 9562 support including v6 and v7)

* Tue Aug 19 2025 Odilon Sousa <osousa@redhat.com> - 3.4.0-2
- Exclude uuid bin to avoid upgrade issues with the binary from other packages

* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.4.0-1
- Update to 3.4.0

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.3.2-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.3.2-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.3.2-2
- Update specs to handle SCL

* Thu Jan 17 2019 Avi Sharvit <asharvit@redhat.com> 3.3.2-1
- Update to 3.3.2

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 3.2.1-1
- Update to 3.2.1

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.1.0-1
- Bump nodejs-uuid to 3.1.0 (ewoud@kohlvanwijngaarden.nl)

* Mon May 08 2017 Dominic Cleal <dominic@cleal.org> 3.0.1-1
- new package built with tito
