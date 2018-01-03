%global npm_name datatables.net-select
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 1.2.4
Release: 1%{?dist}
Summary: Select for DataTables
License: MIT
Group: Development/Libraries
URL: https://datatables.net
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(datatables.net) >= 1.10.15
Requires: npm(datatables.net) < 2.0.0
Requires: npm(jquery) >= 1.7
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%doc Readme.md

%changelog
