%global gem_name smart_proxy_abrt

%global foreman_proxy_dir %{_datarootdir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d
%global spool_dir %{_var}/spool/foreman-proxy-abrt

Name: rubygem-%{gem_name}
Version: 0.0.6
Release: 2%{?dist}
Summary: Automatic Bug Reporting Tool plugin for Foreman's smart proxy
Group: Applications/Internet
License: GPLv3
URL: http://github.com/theforeman/smart_proxy_abrt
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: ruby(rubygems)
Requires: foreman-proxy >= 1.7.0
Requires: crontabs
Requires: rubygem-satyr >= 0.1
Requires: rubygem-satyr < 1.0

%if 0%{?rhel} == 6
Requires: ruby(abi)
BuildRequires: ruby(abi)
%else
Requires: ruby(release)
BuildRequires: ruby(release)
%endif
BuildRequires: rubygems-devel
BuildRequires: ruby(rubygems)

%if 0%{?rhel}
%else
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(json)
BuildRequires: foreman-proxy >= 1.7.0
%endif

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
%if 0%{?rhel}
# rhel6 has incompatible version of rubygem-mocha
# rhel7 is missing rubygem-rack-test: https://bugzilla.redhat.com/show_bug.cgi?id=1096201
%else
pushd .%{gem_instdir}
# Explicitly include smart-proxy path because it is not installed as a gem
testrb -Ilib -I%{foreman_proxy_dir}/lib test/*_test.rb
popd
%endif

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
%{foreman_proxy_settingsd_dir}/abrt.yml
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/cron.d/%{name}

%files doc
%{gem_docdir}
%{gem_instdir}/README

%changelog
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
