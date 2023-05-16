# template: foreman_plugin
%global gem_name puppetdb_foreman
%global plugin_name puppetdb_foreman
%global foreman_min_version 3.1

Name: rubygem-%{gem_name}
Version: 6.0.2
Release: 1%{?foremandist}%{?dist}
Summary: This is a Foreman plugin to interact with PuppetDB
License: GPLv3
URL: https://www.github.com/theforeman/puppetdb_foreman
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: ruby
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Disable hosts on PuppetDB after they are deleted or built in Foreman. Follow
https://github.com/theforeman/puppetdb_foreman and raise an issue/submit a
pull request if you need extra functionality. You can also find some help via
the Foreman support pages (https://theforeman.org/support.html).


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%foreman_bundlerd_file

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_plugin_log}

%changelog
* Tue May 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 6.0.2-1
- Update to 6.0.2

* Thu Nov 03 2022 Foreman Packaging Automation <packaging@theforeman.org> 6.0.1-1
- Update to 6.0.1

* Fri Oct 14 2022 Dirk Goetz <dirk.goetz@netways.de> 6.0.0-1
- Update to 6.0.0

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 5.0.0-4
- Stop generaing apipie cache

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 5.0.0-3
- Rebuild for Ruby 2.7

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 5.0.0-2
- Drop migrate, seed and restart posttans

* Mon Apr 08 2019 Timo Goebel <mail@timogoebel.name> - 5.0.0-1
- Update puppetdb_foreman to 5.0.0

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 4.0.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Mon Jan 15 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.0.0-1
- Update puppetdb_foreman to 4.0.0 (mail@timogoebel.name)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed Sep 06 2017 Daniel Lobato Garcia <me@daniellobato.me> 3.1.2-1
- Update puppetdb_foreman to 3.1.2 (mail@timogoebel.name)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Fri Apr 28 2017 Dominic Cleal <dominic@cleal.org> 3.0.2-1
- Update puppetdb_foreman to 3.0.2 (mail@timogoebel.name)

* Wed Apr 26 2017 Dominic Cleal <dominic@cleal.org> 3.0.1-1
- Update puppetdb_foreman to 3.0.1 (mail@timogoebel.name)

* Fri Jan 13 2017 Dominic Cleal <dominic@cleal.org> 2.0.0-1
- Release puppetdb_foreman 2.0 (me@daniellobato.me)
- Use gem_install to build rubygem (dominic@cleal.org)

* Fri Sep 30 2016 Dominic Cleal <dominic@cleal.org> 1.0.4-1
- Update puppetdb_foreman 1.0.4 (me@daniellobato.me)

* Tue Apr 19 2016 Dominic Cleal <dominic@cleal.org> 1.0.3-1
- plugins:puppetdb_foreman - Release 1.0.3 (elobatocs@gmail.com)

* Thu Mar 03 2016 Dominic Cleal <dominic@cleal.org> 1.0.2-1
- plugins:puppetdb_foreman - Release 1.0.2 (elobatocs@gmail.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Fri Nov 13 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-1
- plugins:puppetdb_foreman - Release 0.2.0 (elobatocs@gmail.com)

* Mon Oct 26 2015 Dominic Cleal <dcleal@redhat.com> 0.1.3-1
- plugins:puppetdb_foreman - Release 0.1.3 (elobatocs@gmail.com)
- Add foremandist macro (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Nov 11 2014 Daniel Lobato <dlobatog@redhat.com> 0.1.2-1
- Update to v0.1.2 (dlobatog@redhat.com)
- Better error handling for dashboard

* Sat Oct 11 2014 Daniel Lobato <dlobatog@redhat.com> 0.1.1-1
- Update to v0.1.1 (dlobatog@redhat.com)
- Proxy PuppetDB dashboard

* Fri Oct 03 2014 Daniel Lobato <dlobatog@redhat.com> 0.0.9-1
- Update to v0.0.9 (dlobatog@redhat.com)
- Deactivate host after build

* Fri Sep 19 2014 Daniel Lobato <dlobatog@redhat.com> 0.0.8-1
- Update to v0.0.8 (dlobatog@redhat.com)
- Setting puppetdb_enabled is now a boolean

* Mon Jul 21 2014 Dominic Cleal <dcleal@redhat.com> 0.0.7-1
- Update to v0.0.7 (dcleal@redhat.com)

* Mon Jul 21 2014 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- Update to v0.0.6
- Config file removed and replaced with in-app settings

* Thu Jan 30 2014 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- Update to v0.0.5 (dcleal@redhat.com)

* Tue Nov 05 2013 Dominic Cleal <dcleal@redhat.com> 0.0.4-2
- Install disabled config file by default (dcleal@redhat.com)

* Tue Sep 10 2013 Dominic Cleal <dcleal@redhat.com> 0.0.4-1
- new package built with tito
