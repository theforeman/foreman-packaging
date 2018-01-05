%global npm_name uuid
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 3.1.0
Release: 1%{?dist}
Summary: RFC4122 (v1, v4, and v5) UUIDs
License: MIT
Group: Development/Libraries
URL: https://github.com/kelektiv/node-uuid#readme
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
cp -pfr bin %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr v1.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr v4.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr v5.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/uuid
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
%doc AUTHORS
%doc HISTORY.md
%doc README.md

%changelog
* Mon May 08 2017 Dominic Cleal <dominic@cleal.org> 3.0.1-1
- new package built with tito

