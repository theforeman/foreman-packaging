%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name babel-plugin-syntax-dynamic-import

Name: %{?scl_prefix}nodejs-babel-plugin-syntax-dynamic-import
Version: 6.18.0
Release: 2%{?dist}
Summary: Allow parsing of import()
License: MIT
Group: Development/Libraries
URL: https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-dynamic-import
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?!scl:1}
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
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
* Wed Oct 23 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.18.0-2
- Build for SCL

* Wed Jan 09 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.18.0-1
- Add nodejs-babel-plugin-syntax-dynamic-import generated by npm2rpm using the single strategy
