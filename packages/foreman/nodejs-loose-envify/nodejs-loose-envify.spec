%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name loose-envify

Name: %{?scl_prefix}nodejs-loose-envify
Version: 1.3.1
Release: 2%{?dist}
Summary: Fast (and loose) selective `process
License: MIT
Group: Development/Libraries
URL: https://github.com/zertosh/loose-envify
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
Requires: %{?scl_prefix}npm(js-tokens) >= 3.0.0
Requires: %{?scl_prefix}npm(js-tokens) < 4.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr cli.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr custom.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr loose-envify.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr replace.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/cli.js
ln -sf %{nodejs_sitelib}/%{npm_name}/cli.js %{buildroot}%{_bindir}/loose-envify

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/loose-envify
%license LICENSE
%doc README.md

%changelog
* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.3.1-2
- Update specs to handle SCL

* Wed Oct 18 2017 Eric D. Helms <ericdhelms@gmail.com> 1.3.1-1
- new package built with tito
