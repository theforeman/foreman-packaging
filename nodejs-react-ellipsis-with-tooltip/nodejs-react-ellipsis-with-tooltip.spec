%global npm_name react-ellipsis-with-tooltip
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 1.0.6
Release: 1%{?dist}
Summary: truncates (with ellipsis) overflowing text elements and adds a tooltip
License: MIT
Group: Development/Libraries
URL: https://github.com/amirfefer/react-ellipsis-with-tooltip
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(uuid) >= 3.1.0
Requires: npm(uuid) < 4.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr stories %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.6-1
- new package built with tito

