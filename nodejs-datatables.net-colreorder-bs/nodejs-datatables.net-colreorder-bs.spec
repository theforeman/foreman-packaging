%global npm_name datatables.net-colreorder-bs
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 1.3.3
Release: 1%{?dist}
Summary: ColReorder for DataTables with styling for Bootstrap
License: MIT
Group: Development/Libraries
URL: https://datatables.net
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(datatables.net-bs) >= 1.10.9
Requires: npm(datatables.net-colreorder) >= 1.2.0
Requires: npm(jquery) >= 1.7
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr css %{buildroot}%{nodejs_sitelib}/%{npm_name}
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
