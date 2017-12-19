%global npm_name jquery
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 3.2.1
Release: 1%{?dist}
Summary: JavaScript library for DOM operations
License: MIT
Group: Development/Libraries
URL: https://jquery.com
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Obsoletes: nodejs-%{npm_name}-doc < 3.2.1

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr external %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.txt
%doc AUTHORS.txt
%doc README.md

%changelog
* Thu Jan 26 2017 Dominic Cleal <dominic@cleal.org> 2.2.4-1
- Update nodejs-jquery to 2.2.4 (dominic@cleal.org)

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 1.11.3-3
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Fri Aug 12 2016 Dominic Cleal <dominic@cleal.org> 1.11.3-2
- Fix pkg/npm_name macro reference (dominic@cleal.org)

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 1.11.3-1
- new package built with tito

