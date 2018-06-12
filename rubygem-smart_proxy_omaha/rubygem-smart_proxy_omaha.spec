%global gem_name smart_proxy_omaha
%global plugin_name omaha

%global foreman_proxy_dir %{_datarootdir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d
%global content_dir %{_var}/lib/foreman-proxy/omaha/content
%global proxy_user foreman-proxy

Name: rubygem-%{gem_name}
Version: 0.0.4
Release: 1%{?foremandist}%{?dist}
Summary: Omaha protocol support for smart-proxy
Group: Applications/Internet
License: GPLv3
URL: http://github.com/theforeman/smart_proxy_omaha
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: foreman-proxy >= 1.12
Requires: crontabs
Requires: ruby
Requires: ruby(rubygems)
Requires: rubygem(nokogiri) >= 1.8.1
Requires: rubygem(json)
%if 0%{?rhel} == 6
BuildRequires: ruby(abi)
%else
BuildRequires: ruby(release)
%endif
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name}

%description
This plug-in adds support for the Omaha Procotol to Foreman's Smart Proxy.


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

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# bundler file
mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
mv %{buildroot}%{gem_instdir}/bundler.d/%{plugin_name}.rb \
   %{buildroot}%{foreman_proxy_bundlerd_dir}

# sample config
mkdir -p %{buildroot}%{foreman_proxy_settingsd_dir}
mv %{buildroot}%{gem_instdir}/settings.d/omaha.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/omaha.yml

# crontab
mkdir -p %{buildroot}%{_sysconfdir}/cron.d/
mv %{buildroot}%{gem_instdir}/extra/foreman-proxy-omaha-sync.cron \
   %{buildroot}%{_sysconfdir}/cron.d/%{name}

# content directory
mkdir -p %{buildroot}%{content_dir}

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, %{proxy_user}) %{foreman_proxy_settingsd_dir}/omaha.yml
%attr(-,%{proxy_user},%{proxy_user}) %{content_dir}
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_instdir}/bundler.d
%{gem_libdir}
%{gem_instdir}/settings.d
%{_bindir}/smart-proxy-omaha-sync
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/cron.d/%{name}
%exclude %{gem_cache}
%exclude %{gem_instdir}/extra
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/test
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Jun 12 2018 Timo Goebel <mail@timogoebel.name> - 0.0.4-1
- Update smart_proxy_omaha to 0.0.4

* Tue Oct 24 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.0.3-1
- Update smart_proxy_omaha to 0.0.3 (mail@timogoebel.name)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon Aug 14 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.2-1
- Update smart_proxy_omaha to 0.0.2 (mail@timogoebel.name)

* Mon Oct 17 2016 Dominic Cleal <dominic@cleal.org> 0.0.1-1
- new package built with tito
