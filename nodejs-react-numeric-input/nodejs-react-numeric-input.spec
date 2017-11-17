%global npm_name react-numeric-input

Name: nodejs-%{npm_name}
Version: 2.2.0
Release: 1%{?dist}
Summary: A React component to replace number inputs with a cross-browser consistent appearance
License: MIT
Group: Development/Libraries
URL: https://github.com/vlad-ignatov/react-numeric-input#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Number input component that can replace the native number input which is not
yet very well supported and where it is, it does not have the same appearance
across the browsers. Additionally this component offers more flexible options
and can be used for any values (differently formatted representations of the
internal numeric value).

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js package.json src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%doc docs

%changelog
* Fri Nov 17 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.2.0-1
- Bump nodejs-react-numeric-input to 2.2.0 (ewoud@kohlvanwijngaarden.nl)

* Mon Aug 07 2017 Eric D. Helms <ericdhelms@gmail.com> 2.0.7-1
- new package built with tito

