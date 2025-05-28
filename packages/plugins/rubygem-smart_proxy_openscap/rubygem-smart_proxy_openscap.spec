# template: smart_proxy_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_bindir:%global _root_bindir %{_bindir}}
%{!?_root_datadir:%global _root_datadir %{_datadir}}
%{!?_root_localstatedir:%global _root_localstatedir %{_localstatedir}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name smart_proxy_openscap
%global plugin_name openscap

%global foreman_proxy_min_version 1.25
%global foreman_proxy_dir %{_root_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_root_localstatedir}/lib/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_root_sysconfdir}/foreman-proxy/settings.d

%global spool_dir %{_var}/spool/foreman-proxy/openscap
%global content_dir %{foreman_proxy_statedir}/openscap
%global proxy_user foreman-proxy

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.12.1
Release: 1%{?foremandist}%{?dist}
Summary: OpenSCAP plug-in for Foreman's smart-proxy
Group: Applications/Internet
License: GPLv3+
URL: https://github.com/theforeman/smart_proxy_openscap
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: ruby >= 2.7
Requires: ruby < 4
BuildRequires: ruby >= 2.7
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# These are called at runtime
Requires: /usr/bin/bunzip2
Requires: /usr/bin/oscap

%{?scl:Obsoletes: rubygem-%{gem_name} < %{version}-%{release}}

%description
A plug-in to the Foreman's smart-proxy which receives
bzip2ed ARF files and forwards them to the Foreman.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%{?scl:Obsoletes: rubygem-%{gem_name}-doc < %{version}-%{release}}

%description doc
Documentation for %{name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
mkdir -p %{buildroot}%{_root_bindir}
mv  %{buildroot}%{gem_instdir}/bin/* \
        %{buildroot}%{_root_bindir}/

# bundler file
mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
mv %{buildroot}%{gem_instdir}/bundler.d/%{plugin_name}.rb \
   %{buildroot}%{foreman_proxy_bundlerd_dir}

# sample config
mkdir -p %{buildroot}%{foreman_proxy_settingsd_dir}
mv %{buildroot}%{gem_instdir}/settings.d/openscap.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/openscap.yml

#crontab
mkdir -p %{buildroot}%{_root_sysconfdir}/cron.d/
mv %{buildroot}%{gem_instdir}/extra/smart-proxy-openscap-send.cron \
   %{buildroot}%{_root_sysconfdir}/cron.d/%{name}

# create spool directory
mkdir -p %{buildroot}%{spool_dir}

# create content, reports and failed_reports directories and symlink it to foreman-proxy directory
mkdir -p %{buildroot}%{content_dir}/content
mkdir -p %{buildroot}%{content_dir}/reports
mkdir -p %{buildroot}%{content_dir}/failed
ln -sv %{content_dir} %{buildroot}%{foreman_proxy_dir}/openscap

%files
%dir %{gem_instdir}
%{_root_bindir}/smart-proxy-openscap-send
%{foreman_proxy_dir}/openscap
%attr(-,%{proxy_user},%{proxy_user}) %{spool_dir}
%attr(-,%{proxy_user},%{proxy_user}) %{content_dir}
%config(noreplace) %attr(0644, root, root) %{_root_sysconfdir}/cron.d/%{name}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/openscap.yml
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop_todo.yml
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/COPYING
%{gem_instdir}/bin
%{gem_libdir}
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%exclude %{gem_instdir}/extra
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/smart_proxy_openscap.gemspec
%{gem_instdir}/test

%changelog
* Mon Apr 14 2025 Adam Ruzicka <aruzicka@redhat.com> - 0.12.1-1
- Update to 0.12.1

* Wed Dec 04 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.12.0-1
- Update to 0.12.0

* Wed Jul 24 2024 Adam Ruzicka <aruzicka@redhat.com> - 0.11.1-1
- Update to 0.11.1

* Thu May 30 2024 Adam Ruzicka <aruzicka@redhat.com> - 0.11.0-1
- Update to 0.11.0

* Wed May 15 2024 Adam Ruzicka <aruzicka@redhat.com> - 0.10.0-1
- Release rubygem-smart_proxy_openscap 0.10.0

* Thu May 26 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.9.2-1
- Update to 0.9.2

* Mon May 09 2022 Eric D. Helms <ericdhelms@gmail.com> - 0.9.1-3
- Drop unused smart_proxy_dynflow_core_bundlerd_dir macro

* Mon Jan 10 2022 Evgeni Golov - 0.9.1-2
- use versioned obsoletes for proxy plugins

* Wed Jul 14 2021 Ondrej Prazak <oprazak@redhat.com> 0.9.1-1
- Update to 0.9.1

* Tue May 18 2021 Ondrej Prazak <oprazak@redhat.com> 0.9.0-1
- Update to 0.9.0

* Thu Apr 22 2021 Ondrej Prazak <oprazak@redhat.com> 0.8.1-1
- Update to 0.8.1

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.8.0-2
- Rebuild for Ruby 2.7

* Wed Mar 03 2021 Ondrej Prazak <oprazak@redhat.com> 0.8.0-1
- Update to 0.8.0

* Thu Aug 06 2020 Ondrej Prazak <oprazak@redhat.com> 0.7.4-1
- Update to 0.7.4

* Thu Jul 30 2020 Ondrej Prazak <oprazak@redhat.com> 0.7.3-1
- Update to 0.7.3

* Mon Jun 22 2020 Evgeni Golov - 0.7.2-6
- Fix bundler.d location on EL8

* Tue May 26 2020 Adam Ruzicka <aruzicka@redhat.com> 0.7.2-5
- Move local state to /var/lib

* Tue May 12 2020 Adam Ruzicka <aruzicka@redhat.com> - 0.7.2-4
- Change localstatedir to sharedstatedir

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.7.2-3
- Build for SCL

* Thu Sep 26 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.7.2-2
- Update to SCL based template

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
