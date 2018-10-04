%global npm_name react-router-bootstrap
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 0.24.4
Release: 2%{?dist}
Summary: Integration between React Router and React-Bootstrap
License: ASL 2.0
Group: Development/Libraries
URL: https://github.com/react-bootstrap/react-router-bootstrap
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(prop-types) >= 15.5.10
Requires: npm(prop-types) < 16.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

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

%changelog
* Wed Sep 12 2018 Bryan Kearney <bryan.kearney@gmail.com> - 0.24.4-2
- Use ASL 2.0 instead of Apache 2.0 or Apache-2.0

* Thu Apr 19 2018 Eric D. Helms <ericdhelms@gmail.com> 0.24.4-1
- Add nodejs-react-router-bootstrap generated by npm2rpm using the single strategy

