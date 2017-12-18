%global npm_name symbol-observable
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 1.1.0
Release: 1%{?dist}
Summary: Symbol
License: MIT
Group: Development/Libraries
URL: https://github.com/blesh/symbol-observable#readme
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
cp -pfr es %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license license
%doc CHANGELOG.md
%doc readme.md

%changelog
