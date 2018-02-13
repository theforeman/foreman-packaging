%global npm_name js-tokens
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 3.0.2
Release: 1%{?dist}
Summary: A regex that tokenizes JavaScript
License: MIT
URL: https://github.com/lydell/js-tokens
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%{?nodejs_find_provides_and_requires}

%description
%{summary}

%prep
%setup -q -n package

%build
$BUILD

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr CHANGELOG.md LICENSE README.md index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}


%nodejs_symlink_deps

%clean
rm -rf %{buildroot} npm_cache

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
#$CHECK
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Wed Oct 18 2017 Eric D. Helms <ericdhelms@gmail.com> 3.0.2-1
- new package built with tito

