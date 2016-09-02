%global npm_name datatables.net-bs

Name: nodejs-%{npm_name}
Version: 1.10.12
Release: 1%{?dist}
Summary: DataTables for jQuery with styling for Bootstrap
License: MIT
URL: https://datatables.net
Source0: http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
%{?nodejs_find_provides_and_requires}

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
