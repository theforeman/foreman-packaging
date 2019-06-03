%global npm_name is-buffer

Name: nodejs-is-buffer
Version: 2.0.3
Release: 1%{?dist}
Summary: Determine if an object is a Buffer
License: MIT
Group: Development/Libraries
URL: https://github.com/feross/is-buffer#readme
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
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
* Mon Jun 03 2019 Ohad Levy <ohadlevy@gmail.com> 2.0.3-1
- Update to 2.0.3

* Tue Jan 30 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.1.6-1
- new package built with tito

