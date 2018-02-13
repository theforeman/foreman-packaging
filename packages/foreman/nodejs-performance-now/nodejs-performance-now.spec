%global npm_name performance-now
%global enable_tests 0

Name: nodejs-%{npm_name}
Version: 2.1.0
Release: 1%{?dist}
Summary: Implements performance
License: MIT
URL: https://github.com/braveg1rl/performance-now
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%{?nodejs_find_provides_and_requires}

%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}
%description
%{summary}

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr .tm_properties README.md lib license.txt package.json src test %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%license license.txt
%doc README.md
%doc license.txt

%changelog
* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.1.0-1
- new package built with tito

