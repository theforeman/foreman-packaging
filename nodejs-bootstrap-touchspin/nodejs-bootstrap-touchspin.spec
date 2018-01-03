%global npm_name bootstrap-touchspin
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 3.1.1
Release: 1%{?dist}
Summary: A mobile and touch friendly input spinner component for Bootstrap 3
License: Apache-2.0
Group: Development/Libraries
URL: http://www.virtuosoft.eu/code/bootstrap-touchspin/
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
Requires: npm(jquery) >= 1.7
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr bootstrap-touchspin.jquery.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.md
%doc CONTRIBUTING.md
%doc README.md
%doc demo

%changelog
