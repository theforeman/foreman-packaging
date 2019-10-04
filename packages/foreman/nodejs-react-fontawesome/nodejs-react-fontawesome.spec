%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name react-fontawesome

Name: %{?scl_prefix}nodejs-react-fontawesome
Version: 1.6.1
Release: 3%{?dist}
Summary: A React component for the font-awesome icon library
License: MIT
Group: Development/Libraries
URL: https://github.com/danawoodman/react-fontawesome#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
Requires: %{?scl_prefix}npm(prop-types) >= 15.5.6
Requires: %{?scl_prefix}npm(prop-types) < 16.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
AutoReq: no

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr examples %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license license
%doc changelog.md
%doc readme.md

%changelog
* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.6.1-3
- Update specs to handle SCL

* Tue Dec 19 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.6.1-2
- Fix the nodejs-react-fontawesome spec (ewoud@kohlvanwijngaarden.nl)

* Thu Dec 14 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.6.1-1
- new package built with tito
