%global npm_name redux-form-validators
%global enable_tests 0

Name: nodejs-%{npm_name}
Version: 2.1.2
Release: 1%{?dist}
Summary: Simple validations with redux-form
License: MIT
URL: https://github.com/gtournie/redux-form-validators#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}
%description
%{summary}

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr .bootstraprc README.md TODO.txt coverage dist lib package.json postcss.config.js registerBabel.js src translationRunner.js yarn.lock %{buildroot}%{nodejs_sitelib}/%{npm_name}
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
%doc TODO.txt

%changelog
* Tue Jan 02 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.1.2-1
- Update redux-form-validators to 2.1.2 (me@daniellobato.me)

* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.1.0-1
- new package built with tito
