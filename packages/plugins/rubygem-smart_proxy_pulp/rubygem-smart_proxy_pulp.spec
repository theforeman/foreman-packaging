# template: smart_proxy_plugin
%global gem_name smart_proxy_pulp
%global plugin_name pulp

%global foreman_proxy_min_version 1.22.0
%global foreman_proxy_dir %{_datarootdir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Name: rubygem-%{gem_name}
Version: 1.4.1
Release: 2%{?foremandist}%{?dist}
Summary: Basic Pulp support for Foreman Smart-Proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart-proxy-pulp-plugin
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: ruby(release)
Requires: ruby
Requires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Basic Pulp support for Foreman Smart-Proxy.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# bundler file
mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
mv %{buildroot}%{gem_instdir}/bundler.d/%{plugin_name}.rb \
   %{buildroot}%{foreman_proxy_bundlerd_dir}

# sample config
mkdir -p %{buildroot}%{foreman_proxy_settingsd_dir}
mv %{buildroot}%{gem_instdir}/settings.d/pulp.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/pulp.yml
mv %{buildroot}%{gem_instdir}/settings.d/pulp3.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/pulp3.yml
mv %{buildroot}%{gem_instdir}/settings.d/pulpnode.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/pulpnode.yml

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/pulp.yml
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/pulp3.yml
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/pulpnode.yml
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/bundler.d
%{gem_libdir}
%exclude %{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile

%changelog
* Tue Jul 02 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.4.1-2
- Regenerate spec file based on smart_proxy_plugin

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

