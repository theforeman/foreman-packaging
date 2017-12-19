%global npm_name jquery-match-height
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 0.7.2
Release: 1%{?dist}
Summary: a responsive equal heights plugin for jQuery
License: MIT
Group: Development/Libraries
URL: http://brm.io/jquery-match-height/
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
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr jquery.matchHeight.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr matchHeight.jquery.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr test %{buildroot}%{nodejs_sitelib}/%{npm_name}

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
