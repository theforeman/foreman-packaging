%global npm_name diff

Name: nodejs-diff
Version: 4.0.1
Release: 1%{?dist}
Summary: A javascript text diff implementation
License: BSD-3-Clause
Group: Development/Libraries
URL: https://github.com/kpdecker/jsdiff#readme
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
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr rollup.config.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr runtime.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr yarn-error.log %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CONTRIBUTING.md
%doc README.md
%doc release-notes.md

%changelog
* Sun Jun 23 2019 Ohad Levy <ohadlevy@gmail.com> 4.0.1-1
- Update to 4.0.1

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 3.0.1-1
- Update to 3.0.1

* Thu Sep 08 2016 Dominic Cleal <dominic@cleal.org> 3.0.0-1
- new package built with tito

