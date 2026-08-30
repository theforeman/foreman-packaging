# template: default
%global gem_name faraday

Name: rubygem-%{gem_name}2
Version: 2.12.2
Release: 1%{?dist}
Summary: HTTP/REST API client library
License: MIT
URL: https://lostisland.github.io/faraday
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 3.0
BuildRequires: ruby >= 3.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

# Co-installable with rubygem-faraday 1.x
Conflicts: rubygem-%{gem_name} > 2

%description
HTTP/REST API client library.
This package provides Faraday 2.x, installable alongside Faraday 1.x
for consumers that require the newer major version.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Wed May 27 2026 Pablo Mendez Hernandez <pablomh@redhat.com> 2.12.2-1
- Add Faraday 2.x as co-installable package alongside 1.x
- Needed by smart-proxy for persistent HTTP connections (theforeman/smart-proxy#944)
