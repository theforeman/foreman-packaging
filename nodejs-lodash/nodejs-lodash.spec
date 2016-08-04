%global npm_name lodash

Name: nodejs-%{npm_name}
Version: 2.4.2
Release: 1%{?dist}
Summary: A utility library delivering consistency, customization, performance, & extras.
License: MIT
Group: Development/Libraries
URL: https://github.com/lodash/lodash
Source0: http://registry.npmjs.org/lodash/-/lodash-2.4.2.tgz

BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: npm(%{npm_name}) = %{version}

%description
A utility library delivering consistency, customization, performance, & extras.

%package doc
Summary: Documentation for nodejs-%{npm_name}
Group: Documentation
Requires: nodejs-%{npm_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for nodejs-%{npm_name}

%prep
%setup -q -n package

rm -rf node_modules

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist  *.json *.md *.js *.txt %{buildroot}%{nodejs_sitelib}/%{npm_name}
%nodejs_symlink_deps

%check

%files
%{nodejs_sitelib}/%{npm_name}
%doc LICENSE.txt

%files doc
%doc README.md

%changelog
