# template: smart_proxy_plugin
%global gem_name smart_proxy_chef
%global plugin_name chef

%global foreman_proxy_min_version 1.6.0
%global foreman_proxy_dir %{_datarootdir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Name: rubygem-%{gem_name}
Version: 0.2.0
Release: 2%{?foremandist}%{?dist}
Summary: Chef support for Foreman Smart-Proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_chef
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: ruby(release)
Requires: ruby
Requires: ruby(rubygems)
Requires: rubygem(chef-api)
BuildRequires: ruby(release)
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Chef support for Foreman Smart-Proxy.


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
mv %{buildroot}%{gem_instdir}/settings.d/chef.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/chef.yml

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/chef.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bundler.d
%{gem_libdir}
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile

%changelog
* Tue Jul 02 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.2.0-2
- Regenerate spec file

* Mon Jan 30 2017 Dominic Cleal <dominic@cleal.org> 0.2.0-1
- Update smart_proxy_chef to 0.2.0 (mhulan@redhat.com)

* Wed Jun 22 2016 Dominic Cleal <dominic@cleal.org> 0.1.8-1
- Update smart_proxy_chef to 0.1.8 (mhulan@redhat.com)

* Fri Apr 08 2016 Dominic Cleal <dominic@cleal.org> 0.1.7-1
- Update smart_proxy_chef to 0.1.7 (mhulan@redhat.com)

* Fri Dec 18 2015 Dominic Cleal <dcleal@redhat.com> 0.1.6-1
- Update smart_proxy_chef to 0.1.6 (mhulan@redhat.com)

* Tue Oct 06 2015 Dominic Cleal <dcleal@redhat.com> 0.1.5-1
- Update smart_proxy_chef to 0.1.5 (mhulan@redhat.com)

* Mon Jun 22 2015 Marek Hulan <mhulan@redhat.com> 0.1.4-1
- Update smart_proxy_chef to 0.1.4 (mhulan@redhat.com)

* Wed Mar 18 2015 Marek Hulan <mhulan@redhat.com> 0.1.3-2
- Fixes the overriding of config file (mhulan@redhat.com)

* Tue Mar 17 2015 Marek Hulan <mhulan@redhat.com> 0.1.3-1
- Update smart_proxy_chef to 0.1.3 (mhulan@redhat.com)

* Wed Jan 14 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- Update smart_proxy_chef to 0.1.2 (dcleal@redhat.com)

* Tue Nov 11 2014 Dominic Cleal <dcleal@redhat.com> 0.1.1-1
- new package built with tito (mhulan@redhat.com)

