%global npm_name jquery

Name: nodejs-%{npm_name}
Version: 1.11.3
Release: 1%{?dist}
Summary: JavaScript library for DOM operations
License: MIT
Group: Development/Libraries
URL: https://github.com/jquery/jquery.git
Source0: http://registry.npmjs.org/jquery/-/jquery-1.11.3.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: npm(%{npm_name}) = %{version}

%description
JavaScript library for DOM operations

%package doc
Summary: Documentation for nodejs-%{pkg_name}
Group: Documentation
Requires: nodejs-%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for nodejs-%{npm_name}.

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist src *.json *.md *.txt %{buildroot}%{nodejs_sitelib}/%{npm_name}

%build

%check
%nodejs_symlink_deps --check

%files
%{nodejs_sitelib}/%{npm_name}

%files doc
%doc %{nodejs_sitelib}/%{npm_name}/*.md
%doc %{nodejs_sitelib}/%{npm_name}/*.txt
%exclude %{nodejs_sitelib}/%{npm_name}/.*
%exclude %{nodejs_sitelib}/%{npm_name}/bower.json

%changelog
