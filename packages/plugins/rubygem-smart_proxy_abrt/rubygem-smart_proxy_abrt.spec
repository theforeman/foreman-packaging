%global gem_name smart_proxy_abrt

%global foreman_proxy_dir %{_datarootdir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d
%global spool_dir %{_var}/spool/foreman-proxy-abrt

Name: rubygem-%{gem_name}
Version: 0.0.8
Release: 3%{?dist}
Summary: Automatic Bug Reporting Tool plugin for Foreman's smart proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_abrt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: ruby(rubygems)
Requires: foreman-proxy >= 1.8.0
Requires: crontabs
Requires: rubygem-satyr >= 0.1
Requires: rubygem-satyr < 1.0

Requires: ruby(release)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby(rubygems)
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(json)
BuildRequires: foreman-proxy >= 1.8.0

BuildArch: noarch

Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-abrt

%description
This smart proxy plugin, together with a Foreman plugin, add the capability to
send ABRT micro-reports from your managed hosts to Foreman.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires:%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep

%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
       %{buildroot}%{gem_dir}/

# executables
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
       %{buildroot}%{_bindir}

# bundler file
mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
mv %{buildroot}%{gem_instdir}/bundler.d/abrt.rb \
   %{buildroot}%{foreman_proxy_bundlerd_dir}

# sample config
mkdir -p %{buildroot}%{foreman_proxy_settingsd_dir}
mv %{buildroot}%{gem_instdir}/settings.d/abrt.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/abrt.yml

# crontab
mkdir -p %{buildroot}%{_sysconfdir}/cron.d/
mv %{buildroot}%{gem_instdir}/extra/foreman-proxy-abrt-send.cron \
   %{buildroot}%{_sysconfdir}/cron.d/%{name}

# create spool directory
mkdir -p %{buildroot}%{spool_dir}

%check
pushd .%{gem_instdir}
# Explicitly include smart-proxy path because it is not installed as a gem
ruby -Ilib:test:%{foreman_proxy_dir}/lib -e 'Dir.glob "./test/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%{gem_instdir}/bin
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/Rakefile

%dir %attr(0755, foreman-proxy, foreman-proxy) %{spool_dir}
%{foreman_proxy_bundlerd_dir}/abrt.rb
%{_bindir}/smart-proxy-abrt-send
%config(noreplace) %{foreman_proxy_settingsd_dir}/abrt.yml
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/cron.d/%{name}

%files doc
%{gem_docdir}
%{gem_instdir}/README

%changelog
* Thu May 04 2017 Dominic Cleal <dominic@cleal.org> 0.0.8-3
- Enable check on EL builds (dominic@cleal.org)

* Tue May 31 2016 Dominic Cleal <dominic@cleal.org> 0.0.8-2
- Replace testrb with call to ruby (dominic@cleal.org)

* Tue May 17 2016 Dominic Cleal <dominic@cleal.org> 0.0.8-1
- Updated smart_proxy_abrt to 0.0.8 (lzap+git@redhat.com)

* Tue Jan 05 2016 Dominic Cleal <dcleal@redhat.com> 0.0.7-2
- Fix dep to install correct test framework for F21 (dcleal@redhat.com)

* Wed Mar 25 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-1
- Update smart_proxy_abrt to 0.0.7 (dcleal@redhat.com)

* Fri Jan 09 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-3
- Missing config option for yaml file (lzap+git@redhat.com)

* Fri Nov 14 2014 Martin Milata <mmilata@redhat.com> - 0.0.6-2
- Require smart-proxy 1.7 due to API changes

* Fri Nov 14 2014 Martin Milata <mmilata@redhat.com> - 0.0.6-1
- New upstream version

* Wed Oct 08 2014 Martin Milata <mmilata@redhat.com> - 0.0.5-1
- New upstream version

* Mon Oct 06 2014 Martin Milata <mmilata@redhat.com> - 0.0.4-1
- New upstream version

* Tue Sep 30 2014 Martin Milata <mmilata@redhat.com> - 0.0.3-1
- New upstream version

* Fri Aug 22 2014 Martin Milata <mmilata@redhat.com> - 0.0.2-1
- Initial package
