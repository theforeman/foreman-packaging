%global npm_name jquery-ui
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 1.12.1
Release: 1%{?dist}
Summary: A curated set of user interface interactions, effects, widgets, and themes built on top of the jQuery JavaScript Library
License: MIT
Group: Development/Libraries
URL: http://jqueryui.com
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
cp -pfr external %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr tests %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr themes %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr ui %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.txt
%doc AUTHORS.txt
%doc CONTRIBUTING.md
%doc README.md
%doc demos

%changelog
