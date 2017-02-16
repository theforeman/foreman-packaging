%global npm_name seamless-immutable
%global enable_tests 1

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 7.0.1
Release: 1%{?dist}
Summary: Immutable backwards-compatible data structures for JavaScript
License: BSD
URL: https://github.com/rtfeldman/seamless-immutable
Source0: http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

%{?nodejs_find_provides_and_requires}

%description
Immutable data structures for JavaScript which are backwards-compatible with
normal JS Arrays and Objects.

%prep
%setup -q -n package

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr .npmignore LICENSE README.md package.json seamless-immutable.development.js seamless-immutable.development.min.js seamless-immutable.production.min.js src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
* Thu Feb 16 2017 Dominic Cleal <dominic@cleal.org> 7.0.1-1
- new package built with tito

