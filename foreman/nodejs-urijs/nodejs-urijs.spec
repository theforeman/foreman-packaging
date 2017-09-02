# FIXME
# Remove nodejs_symlink_deps if installing bundled module with NPM

%global npm_name urijs
%global enable_tests 1

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 1.18.10
Release: 1%{?dist}
Summary: URI.js is a Javascript library for working with URLs.
License: MIT
URL: http://medialize.github.io/URI.js/
Source0: http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%{?nodejs_find_provides_and_requires}

%description
%{summary}

%prep
%setup -q -n package

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr CHANGELOG.md LICENSE.txt README.md package.json src %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
#$CHECK
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE.txt
%doc CHANGELOG.md
%doc README.md

%changelog
* Fri Jun 23 2017 Eric D. Helms <ericdhelms@gmail.com> 1.18.10-1
- new package built with tito

