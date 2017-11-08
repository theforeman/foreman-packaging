%global npm_name classnames
%global enable_tests 0

Name: nodejs-%{npm_name}
Version: 2.2.5
Release: 1%{?dist}
Summary: A simple utility for conditionally joining classNames together
License: MIT
URL: https://github.com/JedWatson/classnames.git
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
cp -pfr CONTRIBUTING.md HISTORY.md LICENSE README.md bind.js bower.json dedupe.js index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

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
%doc HISTORY.md
%doc README.md

%changelog
