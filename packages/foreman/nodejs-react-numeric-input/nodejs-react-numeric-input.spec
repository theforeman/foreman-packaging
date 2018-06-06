%global npm_name react-numeric-input
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 2.2.3
Release: 1%{?dist}
Summary: Number input component that can replace the native number input which is not yet very well supported and where it is, it does not have the same appearance across the browsers
License: MIT
Group: Development/Libraries
URL: https://github.com/vlad-ignatov/react-numeric-input#readme
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
cp -pfr __tests__ %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr build_config %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr nightwatch.conf.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr nightwatch.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr selenium-download.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr tests_e2e %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%doc docs

%changelog
* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 2.2.3-1
- Update to 2.2.3

* Fri Nov 17 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.2.0-1
- Bump nodejs-react-numeric-input to 2.2.0 (ewoud@kohlvanwijngaarden.nl)

* Mon Aug 07 2017 Eric D. Helms <ericdhelms@gmail.com> 2.0.7-1
- new package built with tito

