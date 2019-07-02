# template: smart_proxy_plugin
%global gem_name smart_proxy_openscap
%global plugin_name openscap

%global foreman_proxy_min_version 1.11.0
%global foreman_proxy_dir %{_datarootdir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d
%global spool_dir %{_var}/spool/foreman-proxy/openscap
%global content_dir %{_sharedstatedir}/foreman-proxy/openscap
%global proxy_user foreman-proxy

Name: rubygem-%{gem_name}
Version: 0.7.2
Release: 2%{?foremandist}%{?dist}
Summary: OpenSCAP plug-in for Foreman's smart-proxy
Group: Applications/Internet
License: GPLv3+
URL: https://github.com/theforeman/smart_proxy_openscap
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: ruby(release)
Requires: ruby
Requires: ruby(rubygems)
Requires: rubygem(openscap) >= 0.4.7
Requires: rubygem(openscap) < 0.5
BuildRequires: ruby(release)
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
A plug-in to the Foreman's smart-proxy which receives
bzip2ed ARF files and forwards them to the Foreman.


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
mv %{buildroot}%{gem_instdir}/settings.d/openscap.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/openscap.yml

# crontab
mkdir -p %{buildroot}%{_sysconfdir}/cron.d/
mv %{buildroot}%{gem_instdir}/extra/smart-proxy-openscap-send.cron \
   %{buildroot}%{_sysconfdir}/cron.d/%{name}

# create spool directory
mkdir -p %{buildroot}%{spool_dir}

# create content, reports and failed_reports directories and symlink it to foreman-proxy directory
mkdir -p %{buildroot}%{content_dir}/content
mkdir -p %{buildroot}%{content_dir}/reports
mkdir -p %{buildroot}%{content_dir}/failed
ln -sv %{content_dir} %{buildroot}%{_datadir}/foreman-proxy/openscap

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/openscap.yml
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop_todo.yml
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/COPYING
%exclude %{gem_instdir}/bin
%exclude %{gem_instdir}/bundler.d
%exclude %{gem_instdir}/extra
%{gem_libdir}
%exclude %{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}

%attr(-,%{proxy_user},%{proxy_user}) %{spool_dir}
%attr(-,%{proxy_user},%{proxy_user}) %{content_dir}
%{_datadir}/foreman-proxy/openscap
%{foreman_proxy_bundlerd_dir}/openscap.rb
%{_bindir}/smart-proxy-arf-html
%{_bindir}/smart-proxy-arf-json
%{_bindir}/smart-proxy-openscap-send
%{_bindir}/smart-proxy-policy-guide
%{_bindir}/smart-proxy-scap-profiles
%{_bindir}/smart-proxy-scap-validation
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/cron.d/%{name}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/smart_proxy_openscap.gemspec
%{gem_instdir}/test

%changelog
* Tue Jul 02 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.7.2-2
- Regenerate spec file based on smart_proxy_plugin

* Thu May 09 2019 Marek Hulan <mhulan@redhat.com> 0.7.2-1
- Update to 0.7.2

* Wed Nov 28 2018 Marek Hulan <mhulan@redhat.com> 0.7.1-1
- Update to 0.7.1

* Fri Oct 12 2018 Marek Hulan <mhulan@redhat.com> 0.7.0-1
- Update to 0.7.0

* Wed Sep 19 2018 Marek Hulan <mhulan@redhat.com> 0.6.11-1
- Update to 0.6.11

* Thu Apr 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.6.10-1
- Update to 0.6.10

* Wed Jan 17 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.6.9-1
- Update smart_proxy_openscap to 0.6.9 (mhulan@redhat.com)

* Wed Oct 25 2017 Eric D. Helms <ericdhelms@gmail.com> 0.6.8-1
- Update smart_proxy_openscap to 0.6.8 (mhulan@redhat.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Sep 14 2017 Eric D. Helms <ericdhelms@gmail.com> 0.6.7-1
- Update smart_proxy_openscap to 0.6.7 (mhulan@redhat.com)

* Wed Sep 13 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.6.6-1
- Update smart_proxy_openscap to 0.6.6 (ares@users.noreply.github.com)

* Thu Aug 10 2017 Eric D. Helms <ericdhelms@gmail.com> 0.6.5-1
- Update smart_proxy_openscap to v0.6.5 (oprazak@redhat.com)

* Wed Apr 12 2017 Dominic Cleal <dominic@cleal.org> 0.6.4-1
- Update smart_proxy_openscap to 0.6.4 (mhulan@redhat.com)

* Thu Mar 23 2017 Dominic Cleal <dominic@cleal.org> 0.6.3-1
- Update smart_proxy_openscap to 0.6.3 (oprazak@redhat.com)

* Wed Mar 15 2017 Dominic Cleal <dominic@cleal.org> 0.6.2-1
- Update smart_proxy_openscap to 0.6.2 (mhulan@redhat.com)

* Tue Feb 14 2017 Dominic Cleal <dominic@cleal.org> 0.6.1-1
- Update smart_proxy_openscap to 0.6.1 (mhulan@redhat.com)

* Fri Sep 02 2016 Dominic Cleal <dominic@cleal.org> 0.6.0-1
- Update smart_proxy_openscap to 0.6.0 (oprazak@redhat.com)

* Thu Jun 02 2016 Dominic Cleal <dominic@cleal.org> 0.5.4-1
- version bump smart_proxy_openscap 0.5.4 (shlomi@ben-hanna.com)

* Thu Jan 28 2016 Dominic Cleal <dcleal@redhat.com> 0.5.3-1
- smart_proxy_openscap 0.5.3 (shlomi@ben-hanna.com)

* Thu Dec 10 2015 Dominic Cleal <dcleal@redhat.com> 0.5.1-1
- smart_proxy_openscap version 0.5.1 (shlomi@ben-hanna.com)

* Fri Nov 06 2015 Dominic Cleal <dcleal@redhat.com> 0.5.0-1
- smart_proxy_openscap 0.5.0 (shlomi@ben-hanna.com)

* Tue May 19 2015 Dominic Cleal <dcleal@redhat.com> 0.4.1-1
- Version 0.4.1 + directory for SCAP content (shlomi@ben-hanna.com)

* Wed Mar 25 2015 Šimon Lukašík <slukasik@redhat.com> - 0.4.0-1
- new upstream release

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
