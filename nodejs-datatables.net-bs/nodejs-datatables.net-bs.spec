%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name datatables.net-bs

Name: %{?scl_prefix}nodejs-%{npm_name}
Version: 1.10.12
Release: 1%{?dist}
Summary: DataTables for jQuery with styling for Bootstrap
License: MIT
URL: https://datatables.net
Source0: http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz

Requires: %{?scl_prefix}npm(jquery) >= 1.7
BuildArch:  noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%package doc
Summary: Documentation for nodejs-%{npm_name}
Group: Documentation
Requires: nodejs-%{npm_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for nodejs-%{npm_name}

%prep
%setup -q -n package

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr Readme.md css js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
%nodejs_symlink_deps

%files
%{nodejs_sitelib}/%{npm_name}

%files doc
%doc Readme.md

%changelog
* Fri Sep 02 2016 Dominic Cleal <dominic@cleal.org> 1.10.12-1
- new package built with tito

