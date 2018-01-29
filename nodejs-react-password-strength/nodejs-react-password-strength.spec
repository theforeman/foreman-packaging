%global npm_name react-password-strength
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 2.3.1
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

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md
%doc changelog.md

%changelog
