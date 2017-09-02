%global npm_name multiselect
%global enable_tests 1

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 0.9.12
Release: 1%{?dist}
Summary: A replacement for the standard select with multiple attributes
License: MIT
URL: http://loudev.com
Source0: http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

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

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr .npmignore LICENSE.txt README.markdown css img js multi-select.jquery.json package.json test %{buildroot}%{nodejs_sitelib}/%{npm_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%doc LICENSE.txt

%files doc
%doc README.markdown

%changelog
* Fri Sep 23 2016 Dominic Cleal <dominic@cleal.org> 0.9.12-1
- new package built with tito

