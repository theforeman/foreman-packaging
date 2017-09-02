%global gem_name smart_proxy_dynflow

%global foreman_proxy_dir /usr/share/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Summary: Dynflow runtime for Foreman smart proxy
Name: rubygem-%{gem_name}
Version: 0.1.7
Release: 1%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_dynflow
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: ruby(release)
Requires: ruby(rubygems)
Requires: foreman-proxy >= 1.11.0

%if 0%{?fedora}
Requires: rubygem(smart_proxy_dynflow_core) = %{version}
%else
Requires: tfm-rubygem(smart_proxy_dynflow_core) = %{version}
%endif

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildArch: noarch

Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-dynflow

%description
Dynflow runtime for Foreman smart proxy

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

mkdir -p %{buildroot}%{_localstatedir}/lib/foreman-proxy/dynflow

cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
cp -pa .%{gem_instdir}/bundler.plugins.d/dynflow.rb %{buildroot}%{foreman_proxy_bundlerd_dir}
mkdir -p  %{buildroot}%{foreman_proxy_settingsd_dir}
cp -pa .%{gem_instdir}/settings.d/dynflow.yml.example %{buildroot}%{foreman_proxy_settingsd_dir}/dynflow.yml

%files
%dir %{gem_instdir}
%dir %attr(750, foreman-proxy, foreman-proxy) %{_localstatedir}/lib/foreman-proxy/dynflow
%{gem_instdir}/lib
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/dynflow.rb
%config %{foreman_proxy_settingsd_dir}/dynflow.yml
%doc %{gem_instdir}/LICENSE

%exclude %{gem_instdir}/bundler.plugins.d
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Tue Aug 15 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.7-1
- Update smart_proxy_dynflow to 0.1.7 (inecas@redhat.com)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed May 10 2017 Dominic Cleal <dominic@cleal.org> 0.1.6-1
- upgrade smart_proxy_dynflow to 0.1.6 (a.ruzicka@outlook.com)
- Remove EL version conditionals (dominic@cleal.org)

* Tue Sep 20 2016 Dominic Cleal <dominic@cleal.org> 0.1.5-1
- Update smart_proxy_dynflow to 0.1.5 (inecas@redhat.com)

* Fri Jun 24 2016 Dominic Cleal <dominic@cleal.org> 0.1.3-1
- Release smart_proxy_dynflow 0.1.3 (stephen@redhat.com)

* Wed Feb 17 2016 Dominic Cleal <dominic@cleal.org> 0.0.7-1
- Release smart_proxy_dynflow 0.0.7 (stbenjam@redhat.com)

* Thu Feb 04 2016 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- Release smart_proxy_dynflow 0.0.6 (stbenjam@redhat.com)

* Mon Jan 25 2016 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- Release smart_proxy_dynflow 0.0.5 (stbenjam@redhat.com)

* Tue Oct 06 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-1
- Release smart_proxy_dynflow 0.0.4 (RPM) (stbenjam@redhat.com)

* Mon Aug 10 2015 Stephen Benjamin <stephen@redhat.com> 0.0.3-1
- Initial release of 0.0.3
