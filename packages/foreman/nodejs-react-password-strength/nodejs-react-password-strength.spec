%global npm_name react-password-strength

Name: nodejs-react-password-strength
Version: 2.4.0
Release: 1%{?dist}
Summary: A password strength indicator field for use in React projects
License: MIT
Group: Development/Libraries
URL: https://github.com/mmw/react-password-strength#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(prop-types) >= 15.6.0
Requires: npm(prop-types) < 16.0.0
Requires: npm(zxcvbn) >= 4.3.0
Requires: npm(zxcvbn) < 5.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr test %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr webpack.build.config.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr webpack.config.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr webpack.universal.config.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
* Sun Mar 31 2019 Ohad Levy <ohadlevy@gmail.com> 2.4.0-1
- Update to 2.4.0

* Tue Jan 30 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.3.1-1
- new package built with tito

