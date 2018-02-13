%global gem_name smart_proxy_dns_powerdns

%global foreman_proxy_dir /usr/share/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Summary: PowerDNS support for Foreman Smart-Proxy
Name: rubygem-%{gem_name}
Version: 0.3.0
Release: 1%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_dns_powerdns
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?rhel} == 6
Requires: ruby(abi)
BuildRequires: ruby(abi)
%else
Requires: ruby(release)
BuildRequires: ruby(release)
%endif
Requires: foreman-proxy >= 1.13.0
Requires: ruby(rubygems)
Requires: rubygem(mysql2)
Requires: rubygem(pg)
BuildRequires: ruby(rubygems)
BuildRequires: rubygems-devel

BuildArch: noarch

Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-dns_powerdns

%description
PowerDNS support for Foreman Smart-Proxy.

%package doc
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep

%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
cp -pa .%{gem_instdir}/bundler.d/dns_powerdns.rb %{buildroot}%{foreman_proxy_bundlerd_dir}
mkdir -p  %{buildroot}%{foreman_proxy_settingsd_dir}
cp -pa .%{gem_instdir}/config/dns_powerdns.yml %{buildroot}%{foreman_proxy_settingsd_dir}/dns_powerdns.yml

%files
%dir %{gem_instdir}
%{gem_instdir}/bundler.d
%{gem_libdir}
%{gem_instdir}/config
%{foreman_proxy_bundlerd_dir}/dns_powerdns.rb
%config(noreplace) %{foreman_proxy_settingsd_dir}/dns_powerdns.yml
%attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/dns_powerdns.yml
%doc %{gem_instdir}/LICENSE

%exclude %{gem_cache}
%exclude %{gem_instdir}/test
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Jan 03 2017 Dominic Cleal <dominic@cleal.org> 0.3.0-1
- Bump rubygem-smart_proxy_dns_powerdns to 0.3.0 (ewoud@kohlvanwijngaarden.nl)

* Wed Aug 10 2016 Dominic Cleal <dominic@cleal.org> 0.2.1-1
- Bump smart_proxy_dns_powerdns to 0.2.1 (ekohlvanwijngaarden@antagonist.nl)

* Tue Nov 10 2015 Dominic Cleal <dcleal@redhat.com> 0.1.0-1
- new package built with tito

* Thu Oct 08 2015 Ewoud Kohl van Wijngaarden 0.1.0-1
- Initial packaging
