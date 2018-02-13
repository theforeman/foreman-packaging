%global npm_name loose-envify
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 1.3.1
Release: 1%{?dist}
Summary: Fast (and loose) selective `process
License: MIT
URL: https://github.com/zertosh/loose-envify
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch
Requires: npm(js-tokens) >= 3.0.0
Requires: npm(js-tokens) < 4.0.0

%{?nodejs_find_provides_and_requires}

%description
%{summary}

%prep
%setup -q -n package

%build
$BUILD

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr .npmignore LICENSE README.md cli.js custom.js index.js loose-envify.js package.json replace.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

# Handle binaries
mkdir -p %{buildroot}%{_bindir}
install -p -D -m0755 cli.js %{buildroot}%{nodejs_sitelib}/%{npm_name}/cli.js
ln -sf %{nodejs_sitelib}/%{npm_name}/cli.js %{buildroot}%{_bindir}/%{npm_name}.js


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
%{_bindir}/%{npm_name}.js

%license LICENSE
%doc README.md

%changelog
* Wed Oct 18 2017 Eric D. Helms <ericdhelms@gmail.com> 1.3.1-1
- new package built with tito

