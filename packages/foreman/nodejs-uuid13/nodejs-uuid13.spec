%global npm_name uuid

Name: nodejs-uuid13
Version: 13.0.0
Release: 1%{?dist}
Summary: RFC9562 UUIDs (v1, v3, v4, v5, v6, v7)
License: MIT
URL: https://github.com/uuidjs/uuid#readme
Source0: https://registry.npmjs.org/uuid/-/uuid-%{version}.tgz
BuildRequires: nodejs-packaging
%if 0%{?rhel} == 10
# https://issues.redhat.com/browse/RHEL-137712 is fixed in RHEL 10.3
BuildRequires: /usr/bin/node
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: nodejs-uuid = %{version}-%{release}
Provides: npm(%{npm_name}) = %{version}
Obsoletes: nodejs-uuid < %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist-node %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.md
%doc README.md

%changelog
* Wed Sep 23 2026 Jakub Duchek <jakduch@seznam.cz> - 13.0.0-1
- Add a parallel UUID 13 package for the Foreman 5.1 transition
