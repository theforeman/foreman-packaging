%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @theforeman/vendor

Name: %{?scl_prefix}nodejs-theforeman-vendor
Version: 3.0.0
Release: 1%{?dist}
Summary: foreman supported 3rd-party node_modules
License: MIT
Group: Development/Libraries
URL: https://github.com/theforeman/foreman-js#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr scss %{buildroot}%{nodejs_sitelib}/%{npm_name}


%files
%{nodejs_sitelib}/%{npm_name}
%license license
%doc CHANGELOG.md
%doc docs
%doc readme.md

%changelog
* Tue Nov 12 2019 Avi Sharvit <sharvita@gmail.com> 3.0.0-1
- Update to 3.0.0

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.7.0-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.7.0-2
- Update specs to handle SCL

* Tue Sep 24 2019 Ondřej Ezr <oezr@redhat.com> 1.7.0-1
- Update to 1.7.0

* Tue Aug 20 2019 Avi Sharvit <sharvita@gmail.com> 1.4.0-1
- Update to 1.4.0

* Tue Jul 23 2019 Evgeni Golov 0.1.1-1
- Update to 0.1.1

* Tue Jul 16 2019 Evgeni Golov 0.1.0-0.1.alpha.11
- Add nodejs-theforeman-vendor generated by npm2rpm using the single strategy
