%global npm_name react-fontawesome
%global enable_tests 1 

Name: nodejs-%{npm_name}
Version: 1.6.1
Release: 1%{?dist}
Summary: A React component for the font-awesome icon library
License: MIT
URL: https://github.com/danawoodman/react-fontawesome#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Requires: npm(proptypes) >= 15.5.6
Requires: npm(proptypes) < 16.0.0

%description
%{summary}

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr changelog.md examples lib license package.json readme.md %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%license license
%doc changelog.md
%doc readme.md
%doc examples

%changelog
* Thu Dec 14 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.6.1-1
- new package built with tito

