%global npm_name select2

Name: nodejs-%{npm_name}
Version: 3.5.2
Release: 1%{?dist}
Summary: Browserify-ed version of Select2.
License: ASL 2.0 or GPLv2
Group: Development/Libraries
URL: https://github.com/chrisjbaik/select2
Source0: http://registry.npmjs.org/select2/-/select2-3.5.2-browserify.tgz

BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: npm(%{npm_name}) = %{version}

%description
Browserify-ed version of Select2.

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
cp -pfr *.png *.css *.json *.md *.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check

%files
%{nodejs_sitelib}/%{npm_name}
%doc LICENSE

%files doc
%doc README.md
%doc CONTRIBUTING.md

%changelog
