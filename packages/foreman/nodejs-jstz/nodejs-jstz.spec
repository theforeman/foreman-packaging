%global npm_name jstz
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 1.0.11
Release: 1%{?dist}
Summary: Timezone detection for JavaScript
License: 
Group: Development/Libraries
URL: https://github.com/iansinnott/jstz#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr LICENCE %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr jstz.main.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr jstz.rules.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr test.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr utilities %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
* Thu Jun 07 2018 Tomas Strachota <tstrachota@redhat.com> 1.0.11-1
- Update to 1.0.11

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 1.0.7-2
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 1.0.7-1
- new package built with tito

