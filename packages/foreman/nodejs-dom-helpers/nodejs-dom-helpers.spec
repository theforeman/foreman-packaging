%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name dom-helpers

Name: %{?scl_prefix}nodejs-dom-helpers
Version: 3.3.1
Release: 3%{?dist}
Summary: tiny modular DOM lib for ie8+
License: MIT
Group: Development/Libraries
URL: https://github.com/jquense/dom-helpers#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr activeElement.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr class %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr events %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr ownerDocument.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr ownerWindow.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr query %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr style %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr transition %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr util %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.3.1-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.3.1-2
- Update specs to handle SCL

* Wed Oct 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.3.1-1
- Add nodejs-dom-helpers generated by npm2rpm using the single strategy
