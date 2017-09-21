%global npm_name diff
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 3.0.0
Release: 1%{?dist}
Summary: A javascript text diff implementation
License: BSD-3-Clause
URL: https://github.com/kpdecker/jsdiff/issues
Source0: http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

%{?nodejs_find_provides_and_requires}

%description
%{summary}

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
cp -pfr CONTRIBUTING.md LICENSE README.md dist examples images lib package.json release-notes.md runtime.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%doc LICENSE

%files doc
%doc CONTRIBUTING.md
%doc README.md
%doc release-notes.md

%changelog
* Thu Sep 08 2016 Dominic Cleal <dominic@cleal.org> 3.0.0-1
- new package built with tito

