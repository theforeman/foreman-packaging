%global npm_name react-dom
%global enable_tests 1

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 15.6.2
Release: 1%{?dist}
Summary: React package for working with the DOM
License: MIT
URL: https://facebook.github.io/react/
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
cp -pfr LICENSE README.md dist index.js lib package.json server.js test-utils.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%doc LICENSE
%doc README.md

%changelog
* Thu Oct 05 2017 Eric D. Helms <ericdhelms@gmail.com> 15.6.2-1
- Update react-dom to 15.6.2 (me@daniellobato.me)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 15.3.2-1
- new package built with tito

