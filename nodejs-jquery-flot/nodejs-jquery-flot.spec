%global npm_name jquery-flot

Name: nodejs-%{npm_name}
Version: 0.8.3
Release: 1%{?dist}
Summary: undefined
License: undefined
Group: Development/Libraries
URL: undefined
Source0: http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: npm(%{npm_name}) = %{version}
%{?nodejs_find_provides_and_requires}

%description
undefined

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
* Mon Aug 15 2016 Dominic Cleal <dominic@cleal.org> 0.8.3-1
- new package built with tito

