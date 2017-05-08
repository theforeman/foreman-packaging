%global npm_name uuid
%global enable_tests 1

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 3.0.1
Release: 1%{?dist}
Summary: RFC4122 (v1 and v4) generator
License: MIT
URL: https://github.com/kelektiv/node-uuid.git
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
cp -pfr .npmignore .travis.yml AUTHORS HISTORY.md LICENSE.md README.md bin index.js lib package.json test v1.js v4.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}/
install -p -D -m0755 bin/uuid %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/uuid
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/uuid %{buildroot}%{_bindir}/uuid

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/uuid
%license LICENSE.md
%doc HISTORY.md
%doc LICENSE.md
%doc README.md

%changelog
* Mon May 08 2017 Dominic Cleal <dominic@cleal.org> 3.0.1-1
- new package built with tito

