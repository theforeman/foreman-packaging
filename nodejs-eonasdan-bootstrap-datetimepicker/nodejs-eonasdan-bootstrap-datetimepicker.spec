%global npm_name eonasdan-bootstrap-datetimepicker
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 4.17.47
Release: 1%{?dist}
Summary: A date/time picker component designed to work with Bootstrap 3 and Momentjs
License: MIT
Group: Development/Libraries
URL: http://eonasdan.github.io/bootstrap-datetimepicker/
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(bootstrap) >= 3.3
Requires: npm(jquery) >= 1.8.3
Requires: npm(jquery) < 4.0.0
Requires: npm(moment) >= 2.10
Requires: npm(moment-timezone) >= 0.4.0
Requires: npm(moment-timezone) < 1.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr build %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr component.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr tasks %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CONTRIBUTING.md
%doc README.md
%doc docs
%doc mkdocs.yml

%changelog
