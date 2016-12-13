%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name multiselect
%global enable_tests 1

Name: %{?scl_prefix}nodejs-%{npm_name}
Version: 0.9.12
Release: 1%{?dist}
Summary: A replacement for the standard select with multiple attributes
License: MIT
URL: http://loudev.com
Source0: http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz

Requires: %{?scl_prefix}npm(jquery) >= 1.7.1
BuildArch:  noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

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

