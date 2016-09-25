%global npm_name jquery-flot

Name: nodejs-%{npm_name}
Version: 0.8.3
Release: 3%{?dist}
Summary: Flot is a Javascript plotting library for jQuery
License: MIT
Group: Development/Libraries
URL: https://www.npmjs.com/package/jquery-flot
Source0: http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildArch: noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif
Provides: npm(%{npm_name}) = %{version}
%{?nodejs_find_provides_and_requires}

%description
Flot is a Javascript plotting library for jQuery.

Read more at the website: http://www.flotcharts.org/

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
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr *.md LICENSE.txt component.json examples *.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check

%files
%{nodejs_sitelib}/%{npm_name}
%doc LICENSE.txt

%files doc
%doc API.md
%doc CONTRIBUTING.md
%doc FAQ.md
%doc LICENSE.txt
%doc NEWS.md
%doc PLUGINS.md
%doc README.md

%changelog
* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 0.8.3-3
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Mon Aug 15 2016 Dominic Cleal <dominic@cleal.org> 0.8.3-2
- Fix missing licence/summary information (dominic@cleal.org)

* Mon Aug 15 2016 Dominic Cleal <dominic@cleal.org> 0.8.3-1
- new package built with tito

