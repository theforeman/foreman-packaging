%global npm_name stats-webpack-plugin

Name: nodejs-%{npm_name}
Version: 0.4.0
Release: 1%{?dist}
Summary: Write the stats of a build to a file
License: MIT
Group: Development/Libraries
URL: https://github.com/unindented/stats-webpack-plugin
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
Write the stats of a build to a file.

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
cp -pfr LICENSE index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
%nodejs_symlink_deps

%check

%files
%{nodejs_sitelib}/%{npm_name}
%doc LICENSE

%files doc

%changelog
* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 0.4.0-1
- new package built with tito

