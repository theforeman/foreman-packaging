%global gem_name smart_proxy_openscap

%global foreman_proxy_bundlerd_dir %{_datadir}/foreman-proxy/bundler.d
%global foreman_proxy_pluginconf_dir %{_sysconfdir}/foreman-proxy/settings.d
%global spool_dir %{_var}/spool/foreman-proxy/openscap
%global proxy_user foreman-proxy

Name: rubygem-%{gem_name}
Version: 0.3.0
Release: 2%{?dist}
Summary: OpenSCAP plug-in for Foreman's smart-proxy.
Group: Applications/Internet
License: GPLv3+
URL: http://github.com/openscap/smart_proxy_openscap
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?rhel} == 6
Requires: ruby(abi)
BuildRequires: ruby(abi)
%else
Requires: ruby(release)
BuildRequires: ruby(release)
%endif
Requires: ruby(rubygems)
Requires: foreman-proxy >= 1.7.0-0.develop.201410221520
Requires: crontabs
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Obsoletes: rubygem-foreman-proxy_openscap <= 0.3.0-1

%description
A plug-in to the Foreman's smart-proxy which receives bzip2ed ARF files
and forwards them to the Foreman.

%package doc
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
       %{buildroot}%{gem_dir}/

# executables
mkdir -p %{buildroot}%{_bindir}
mv  %{buildroot}%{gem_instdir}/bin/* \
	%{buildroot}%{_bindir}

# bundler file
mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
mv %{buildroot}%{gem_instdir}/bundler.d/openscap.rb \
   %{buildroot}%{foreman_proxy_bundlerd_dir}

# sample config
mkdir -p %{buildroot}%{foreman_proxy_pluginconf_dir}
mv  %{buildroot}%{gem_instdir}/settings.d/openscap.yml.example \
    %{buildroot}%{foreman_proxy_pluginconf_dir}/openscap.yml

# crontab
mkdir -p %{buildroot}%{_sysconfdir}/cron.d/
mv %{buildroot}%{gem_instdir}/extra/smart-proxy-openscap-send.cron \
   %{buildroot}%{_sysconfdir}/cron.d/%{name}

# create spool directory
mkdir -p %{buildroot}%{spool_dir}

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%config(noreplace) %{foreman_proxy_pluginconf_dir}/openscap.yml

%attr(-,%{proxy_user},%{proxy_user}) %{spool_dir}
%{foreman_proxy_bundlerd_dir}/openscap.rb
%{_bindir}/smart-proxy-openscap-send
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/cron.d/%{name}
%doc %{gem_instdir}/COPYING

%exclude %{gem_instdir}/extra/rubygem-%{gem_name}.spec
%exclude %{gem_instdir}/%{gem_name}.gemspec

%files doc
%{gem_docdir}
%{gem_instdir}/README.md


%changelog
* Fri Jan 23 2015 Marek Hulan <mhulan@redhat.com> 0.3.0-2
- new package built based on upstream spec

* Tue Jan 20 2015 Šimon Lukašík <slukasik@redhat.com> - 0.3.0-1
- new upstream release

* Tue Jan 20 2015 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-2
- renamed to smart_proxy_openscap

* Fri Oct 24 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-1
- rebuilt

* Fri Jul 18 2014 Šimon Lukašík <slukasik@redhat.com> - 0.0.1-1
- Initial package
