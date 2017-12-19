%global npm_name bootstrap-sass
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 3.3.7
Release: 1%{?dist}
Summary: bootstrap-sass is a Sass-powered version of Bootstrap 3, ready to drop right into your Sass powered applications
License: MIT
Group: Development/Libraries
URL: https://github.com/twbs/bootstrap-sass#readme
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
cp -pfr eyeglass-exports.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
