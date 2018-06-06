%global npm_name react-onclickoutside
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 6.7.1
Release: 1%{?dist}
Summary: An onClickOutside wrapper for React components
License: MIT
Group: Development/Libraries
URL: https://github.com/Pomax/react-onclickoutside
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
* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 6.7.1-1
- Update to 6.7.1

* Tue Nov 07 2017 Daniel Lobato Garcia <me@daniellobato.me> 6.6.3-1
- new package built with tito

