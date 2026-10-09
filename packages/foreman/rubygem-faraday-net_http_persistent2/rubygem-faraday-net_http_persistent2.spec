# template: default
%global gem_name faraday-net_http_persistent

Name: rubygem-%{gem_name}2
Version: 2.3.0
Release: 1%{?dist}
Summary: Faraday adapter for NetHttpPersistent
License: MIT
URL: https://github.com/lostisland/faraday-net_http_persistent
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 3.0
Requires: rubygem(faraday) >= 2.0
Requires: rubygem(net-http-persistent) >= 4.0
BuildRequires: ruby >= 3.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

Conflicts: rubygem-%{gem_name} > 2

%description
Faraday adapter for NetHttpPersistent.
This package provides the 2.x adapter, compatible with Faraday 2.x
and net-http-persistent 4.x.


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
%doc %{gem_instdir}/README.md

%changelog
* Wed May 27 2026 Pablo Mendez Hernandez <pablomh@redhat.com> 2.3.0-1
- Add faraday-net_http_persistent 2.x as co-installable package alongside 1.x
- Needed by smart-proxy for persistent HTTP connections (theforeman/smart-proxy#944)
