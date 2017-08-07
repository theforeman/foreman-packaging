%global npm_name react-numeric-input
%global enable_tests 1

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 2.0.7
Release: 1%{?dist}
Summary: Number input component that can replace the native number input which is not yet very well supported and where it is, it does not have the same appearance across the browsers
License: MIT
URL: https://github.com/vlad-ignatov/react-numeric-input#readme
Source0: http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
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
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr .eslintignore .eslintrc .flowconfig .npmignore .travis.yml CHANGELOG.md LICENSE README.md __tests__ build_config dist examples index.js karma.conf.js package.json src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
#$CHECK
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Mon Aug 07 2017 Eric D. Helms <ericdhelms@gmail.com> 2.0.7-1
- new package built with tito

