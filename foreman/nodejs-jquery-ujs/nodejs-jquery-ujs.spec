%global npm_name jquery-ujs

Name: nodejs-%{npm_name}
Version: 1.2.1
Release: 3%{?dist}
Summary: Ruby on Rails unobtrusive scripting adapter for jQuery, for npm
License: MIT
Group: Development/Libraries
URL: https://github.com/shakacode/jquery-ujs.git
Source0: http://registry.npmjs.org/jquery-ujs/-/jquery-ujs-1.2.1.tgz

BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
Requires: npm(jquery) >= 1.8.0
BuildArch: noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif
Provides: npm(%{npm_name}) = %{version}

%description
Ruby on Rails unobtrusive scripting adapter for jQuery, for npm

%package doc
Summary: Documentation for nodejs-%{npm_name}
Group: Documentation
Requires: nodejs-%{npm_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for nodejs-%{npm_name}

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr script src test MIT-LICENSE *.json *.md %{buildroot}%{nodejs_sitelib}/%{npm_name}

%files
%{nodejs_sitelib}/%{npm_name}
%doc %{nodejs_sitelib}/%{npm_name}/MIT-LICENSE

%files doc
%doc %{nodejs_sitelib}/%{npm_name}/README.md
%doc %{nodejs_sitelib}/%{npm_name}/CONTRIBUTING.md

%changelog
* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 1.2.1-3
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Fri Aug 12 2016 Dominic Cleal <dominic@cleal.org> 1.2.1-2
- Fix pkg/npm_name macro reference (dominic@cleal.org)

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 1.2.1-1
- new package built with tito

