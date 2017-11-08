%global npm_name patternfly-react
%global enable_tests 0

Name: nodejs-%{npm_name}
Version: 0.9.0
Release: 1%{?dist}
Summary: This library provides a set of common React components for use with the PatternFly reference implementation
License: Apache-2.0
URL: https://github.com/patternfly/patternfly-react#readme
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
cp -pfr CONTRIBUTING.md LICENSE README.md lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%license LICENSE
%doc CONTRIBUTING.md
%doc README.md

%changelog
