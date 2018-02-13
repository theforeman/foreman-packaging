%global npm_name react-onclickoutside
%global enable_tests 0

Name: nodejs-%{npm_name}
Version: 6.6.3
Release: 1%{?dist}
Summary: An onClickOutside wrapper for React components
License: MIT
URL: https://github.com/Pomax/react-onclickoutside
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%{?nodejs_find_provides_and_requires}

%description
%{summary}

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr README.md dist es lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
* Tue Nov 07 2017 Daniel Lobato Garcia <me@daniellobato.me> 6.6.3-1
- new package built with tito

