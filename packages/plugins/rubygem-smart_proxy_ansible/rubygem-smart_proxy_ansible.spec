# template: smart_proxy_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name smart_proxy_ansible
%global plugin_name ansible

%{!?_root_datadir:%global _root_datadir %{_datadir}}
%{!?_root_localstatedir:%global _root_localstatedir %{_localstatedir}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global foreman_proxy_min_version 1.25
%global foreman_proxy_dir %{_root_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_root_localstatedir}/lib/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_root_sysconfdir}/foreman-proxy/settings.d

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.2.1
Release: 2%{?foremandist}%{?dist}
Summary: Smart-Proxy Ansible plugin
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_ansible
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: ansible >= 2.2

Requires: ansible-collection-theforeman-foreman

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.5
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(net-ssh)
Requires: %{?scl_prefix}rubygem(smart_proxy_dynflow) >= 0.5
Requires: %{?scl_prefix}rubygem(smart_proxy_dynflow) < 1
Requires: %{?scl_prefix}rubygem(smart_proxy_remote_execution_ssh) >= 0.4
Requires: %{?scl_prefix}rubygem(smart_proxy_remote_execution_ssh) < 1
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.5
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%{?scl:Obsoletes: rubygem-%{gem_name}}

%description
Smart-Proxy ansible plugin.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%{?scl:Obsoletes: rubygem-%{gem_name}-doc}

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

%pre
for i in ansible ansible_galaxy; do
  if [ -d %{foreman_proxy_dir}/.$i ]; then
    mv %{foreman_proxy_dir}/.$i %{foreman_proxy_statedir}/$i
  fi
done

if [ -f %{foreman_proxy_dir}/.ansible.cfg ] && [ ! -L %{foreman_proxy_dir}/.ansible.cfg ]; then
  mv %{foreman_proxy_dir}/.ansible.cfg %{_root_sysconfdir}/foreman-proxy/ansible.cfg
fi

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
mv %{buildroot}%{gem_instdir}/settings.d/ansible.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/ansible.yml

mkdir -p %{buildroot}%{foreman_proxy_dir}
# Ensure all the ansible state is in /var/lib
for i in ansible ansible_galaxy; do
  mkdir -p %{buildroot}%{foreman_proxy_statedir}/$i
  ln -sv %{foreman_proxy_statedir}/$i %{buildroot}%{foreman_proxy_dir}/.$i
done

ln -sv %{_root_sysconfdir}/foreman-proxy/ansible.cfg %{buildroot}%{foreman_proxy_dir}/.ansible.cfg

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/ansible.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}
%{foreman_proxy_dir}/.ansible
%{foreman_proxy_dir}/.ansible_galaxy
%{foreman_proxy_dir}/.ansible.cfg
%attr(-,foreman-proxy,foreman-proxy) %{foreman_proxy_statedir}/ansible
%attr(-,foreman-proxy,foreman-proxy) %{foreman_proxy_statedir}/ansible_galaxy
%ghost %attr(0640,root,foreman-proxy) %config(noreplace) %{_root_sysconfdir}/foreman-proxy/ansible.cfg

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Mon Jul 12 2021 Evgeni Golov - 3.2.1-2
- Do not obsolete ansible_core from smart_proxy_ansible

* Wed Jun 23 2021 Adam Ruzicka <aruzicka@redhat.com> 3.2.1-1
- Update to 3.2.1

* Wed Jun 23 2021 Adam Ruzicka <aruzicka@redhat.com> 3.2.0-1
- Update to 3.2.0

* Mon May 17 2021 Ondrej Prazak <oprazak@redhat.com> 3.1.0-1
- Update to 3.1.0

* Fri Apr 16 2021 Evgeni Golov - 3.0.1-9
- Unify *_core dependencies, now that the proxy is SCL'ed on EL7
- Require ansible-collection-theforeman-foreman for the callback plugin
- Don't require requests, the collection already does

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.0.1-8
- Rebuild for Ruby 2.7

* Wed Mar 17 2021 Adam Ruzicka <aruzicka@redhat.com> 3.0.1-7
- Deploy bundlerd file for foreman proxy

* Mon Jun 22 2020 Evgeni Golov - 3.0.1-6
- Fix bundler.d location on EL8

* Tue May 26 2020 Adam Ruzicka <aruzicka@redhat.com> 3.0.1-5
- Move local state to /var/lib

* Tue May 12 2020 Adam Ruzicka <aruzicka@redhat.com> 3.0.1-4
- Move local state to /var/lib

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.0.1-3
- Build for SCL

* Wed Sep 25 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.0.1-2
- Add SCL support to spec

* Fri Jun 28 2019 Ondrej Prazak <oprazak@redhat.com> 3.0.1-1
- Update to 3.0.1

* Wed May 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.1.2-3
- Require python-requests

* Thu May 16 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.1.2-2
- Require SCL prefix only on EL7

* Thu Mar 07 2019 Marek Hulan <mhulan@redhat.com> 2.1.2-1
- Update to 2.1.2

* Tue Jan 22 2019 Marek Hulan <mhulan@redhat.com> 2.1.1-1
- Update to 2.1.1

* Thu Sep 13 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.0.3-2
- Require foreman_ansible_core to be installed (#24857)

* Wed May 23 2018 Daniel Lobato Garcia <me@daniellobato.me> 2.0.3-1
- Update to 2.0.3

* Tue Apr 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.2-3
- Handle .ansible.cfg symlinks

* Wed Apr 04 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.2-2
- Manage ansible config/state files and migrate them if needed
- Mark ansible.yml as noreplace

* Mon Mar 05 2018 Daniel Lobato Garcia <me@daniellobato.me> - 2.0.2-1
- Update smart-proxy-ansible to 2.0.2

* Wed Feb 21 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.1-1
- Update smart_proxy_ansible to 2.0.1 (me@daniellobato.me)
- Restructure plugin packages to prepare for obal (pcreech@redhat.com)

* Fri Feb 02 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.0-1
- Update smart_proxy_ansible to 2.0.0 (me@daniellobato.me)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon Feb 13 2017 Dominic Cleal <dominic@cleal.org> 1.1.1-1
- Update smart_proxy_ansible to 1.1.1 (me@daniellobato.me)

* Fri Jan 20 2017 Dominic Cleal <dominic@cleal.org> 1.0.1-1
- Release 1.0.1 smart_proxy_ansible (me@daniellobato.me)
- Add Ansible dependency for Ansible proxy plugin (tbrisker@gmail.com)

* Wed Oct 05 2016 Dominic Cleal <dominic@cleal.org> 1.0.0-1
- new package built with tito

