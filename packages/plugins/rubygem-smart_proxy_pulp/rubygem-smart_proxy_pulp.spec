%global gem_name smart_proxy_pulp

%global foreman_proxy_dir /usr/share/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Summary: Basic Pulp support for Foreman Smart-Proxy
Name: rubygem-%{gem_name}
Version: 1.5.0
Release: 1%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_pulp
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: ruby(rubygems)
Requires: foreman-proxy >= 1.22.0

Requires: ruby(release)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel

BuildRequires: ruby(rubygems)
BuildArch: noarch

Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-pulp

%description
Basic Pulp support for Foreman Smart-Proxy.

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
cp -pa .%{gem_instdir}/bundler.d/pulp.rb %{buildroot}%{foreman_proxy_bundlerd_dir}
mkdir -p  %{buildroot}%{_sysconfdir}/foreman-proxy/settings.d/
cp -pa .%{gem_instdir}/settings.d/pulp3.yml.example %{buildroot}%{foreman_proxy_settingsd_dir}/pulp3.yml
cp -pa .%{gem_instdir}/settings.d/pulp.yml.example %{buildroot}%{foreman_proxy_settingsd_dir}/pulp.yml
cp -pa .%{gem_instdir}/settings.d/pulpnode.yml.example %{buildroot}%{foreman_proxy_settingsd_dir}/pulpnode.yml

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/bundler.d
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/pulp.rb
%config(noreplace) %{_sysconfdir}/foreman-proxy/settings.d/pulp3.yml
%config(noreplace) %{_sysconfdir}/foreman-proxy/settings.d/pulp.yml
%config(noreplace) %{_sysconfdir}/foreman-proxy/settings.d/pulpnode.yml
%license %{gem_instdir}/LICENSE

%exclude %{gem_cache}
%exclude %{gem_instdir}/Gemfile
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Wed Sep 18 2019 Justin Sherrill <jsherril@redhat.com> 1.5.0-1
- Update to 1.5.0

* Fri Mar 08 2019 Justin Sherrill <jsherril@redhat.com> 1.4.1-1
- Updated samrt_proxy_pulp to version 1.4.1
 
* Tue Sep 06 2016 Dominic Cleal <dominic@cleal.org> 1.3.0-1
- Updated smart_proxy_pulp to version 1.3.0 (dmitri@appliedlogic.ca)

* Fri Jul 15 2016 Dominic Cleal <dominic@cleal.org> 1.2.2-1
- Update rubygem-smart_proxy_pulp to 1.2.2 (dmitri@appliedlogic.ca)

* Thu Jun 09 2016 Dominic Cleal <dominic@cleal.org> 1.2.1-1
- Updated rubygem-smart_proxy_pulp to version 1.2.1 (dmitri@appliedlogic.ca)

* Wed Jan 27 2016 Dmitri Dolguikh <dmitri@appliedlogic.ca> 1.2.0-1
- Updated smart_proxy_pulp gem to version 1.2.0

* Wed Mar 18 2015 Marek Hulan <mhulan@redhat.com> 1.0.1-2
- Fixes the overriding of config file (mhulan@redhat.com)

* Thu Aug 07 2014 Dominic Cleal <dcleal@redhat.com> 1.0.1-1
- Add pulpnode.yml config file (dcleal@redhat.com)
- Updated smart_proxy_pulp gem to version 1.0.1 (dmitri@appliedlogic.ca)
- bumping smart_proxy_pulp version to 1.0.1 (jsherril@redhat.com)

* Wed Jul 23 2014 Dominic Cleal <dcleal@redhat.com> 1.0.0-2
- Fix -doc requirement on main package (dcleal@redhat.com)

* Wed Jul 23 2014 Dmitri Dolguikh <dmitri@appliedlogic.ca>
- new package built with tito

