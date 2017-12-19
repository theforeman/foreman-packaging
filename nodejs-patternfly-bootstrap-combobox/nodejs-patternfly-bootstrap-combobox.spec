%global npm_name patternfly-bootstrap-combobox
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 1.1.7
Release: 1%{?dist}
Summary: This is a fork of danielfarrell/bootstrap-combobox v1
License: Apache-2.0
Group: Development/Libraries
URL: https://github.com/patternfly/patternfly-bootstrap-combobox
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
cp -pfr css %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr less %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
