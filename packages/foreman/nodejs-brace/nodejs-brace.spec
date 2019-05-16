%global npm_name brace

Name: nodejs-brace
Version: 0.11.1
Release: 1%{?dist}
Summary: browserify compatible version of the ace editor
License: MIT
Group: Development/Libraries
URL: https://github.com/thlorenz/brace
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
cp -pfr assets %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr ext %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr keybinding %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr mode %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr snippets %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr test %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr theme %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr worker %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md
%doc example

%changelog
* Thu May 16 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.11.1-1
- Update to 0.11.1

* Fri Mar 24 2017 Dominic Cleal <dominic@cleal.org> 0.10.0-1
- new package built with tito

