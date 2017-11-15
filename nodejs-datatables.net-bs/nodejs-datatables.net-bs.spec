%global npm_name datatables.net-bs
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 1.10.16
Release: 1%{?dist}
Summary: DataTables for jQuery with styling for Bootstrap 3
License: MIT
Group: Development/Libraries
URL: https://datatables.net
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch
Obsoletes: %{name}-doc < %{version}

Requires: npm(datatables.net) = 1.10.16
Requires: npm(jquery) >= 1.7

%description
%{summary}

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr Readme.md css js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%doc Readme.md

%changelog
* Fri Sep 02 2016 Dominic Cleal <dominic@cleal.org> 1.10.12-1
- new package built with tito

