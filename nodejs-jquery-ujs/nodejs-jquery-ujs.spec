%global npm_name jquery-ujs

Name: nodejs-%{npm_name}
Version: 1.2.1
Release: 1%{?dist}
Summary: Ruby on Rails unobtrusive scripting adapter for jQuery, for npm
License: MIT
Group: Development/Libraries
URL: https://github.com/shakacode/jquery-ujs.git
Source0: http://registry.npmjs.org/jquery-ujs/-/jquery-ujs-1.2.1.tgz

BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
Requires: npm(jquery) >= 1.8.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: npm(%{npm_name}) = %{version}

%description
Ruby on Rails unobtrusive scripting adapter for jQuery, for npm

%package doc
Summary: Documentation for nodejs-%{npm_name}
Group: Documentation
Requires: nodejs-%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for nodejs-%{pkg_name}

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
* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 1.2.1-1
- new package built with tito

