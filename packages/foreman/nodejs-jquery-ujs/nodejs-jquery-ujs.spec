%global npm_name jquery-ujs
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 1.2.2
Release: 1%{?dist}
Summary: Unobtrusive scripting adapter for jQuery
License: MIT
Group: Development/Libraries
URL: https://github.com/rails/jquery-ujs#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(jquery) >= 1.8.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license MIT-LICENSE
%doc CONTRIBUTING.md
%doc README.md
%doc RELEASE.md

%changelog
* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 1.2.2-1
- Update to 1.2.2

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 1.2.1-3
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Fri Aug 12 2016 Dominic Cleal <dominic@cleal.org> 1.2.1-2
- Fix pkg/npm_name macro reference (dominic@cleal.org)

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 1.2.1-1
- new package built with tito

