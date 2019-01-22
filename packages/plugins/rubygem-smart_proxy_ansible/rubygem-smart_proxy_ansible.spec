%global gem_name smart_proxy_ansible

%global foreman_proxy_dir /usr/share/foreman-proxy
%global foreman_proxy_statedir %{_localstatedir}/lib/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d
%global smart_proxy_dynflow_bundlerd_dir %{?rhel:/opt/theforeman/tfm/root/}%{_datadir}/smart_proxy_dynflow_core/bundler.d

Summary: Ansible support for Foreman smart proxy
Name: rubygem-%{gem_name}
Version: 2.1.1
Release: 1%{?foremandist}%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_ansible
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?rhel:tfm-}rubygem(smart_proxy_dynflow_core) >= 0.1.5
Requires: %{?rhel:tfm-}rubygem(foreman_ansible_core)
Requires: foreman-proxy >= 1.11.0
Requires: rubygem(smart_proxy_dynflow) >= 0.1
Requires: rubygem(smart_proxy_dynflow) < 1.0

Requires: ruby
Requires: ruby(rubygems)

Requires: ansible >= 2.2

Requires: ruby(release)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildArch: noarch

Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-ansible

%description
Ansible support for Foreman smart proxy

%package doc
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep

%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%pre
for i in ansible ansible_galaxy; do
  if [ -d %{foreman_proxy_dir}/.$i ]; then
    mv %{foreman_proxy_dir}/.$i %{foreman_proxy_statedir}/$i
  fi
done

if [ -f %{foreman_proxy_dir}/.ansible.cfg ] && [ ! -L %{foreman_proxy_dir}/.ansible.cfg ]; then
  mv %{foreman_proxy_dir}/.ansible.cfg %{_sysconfdir}/foreman-proxy/ansible.cfg
fi

%install
mkdir -p %{buildroot}%{gem_dir}

cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
cp -pa .%{gem_instdir}/bundler.plugins.d/smart_proxy_ansible.rb %{buildroot}%{foreman_proxy_bundlerd_dir}

mkdir -p  %{buildroot}%{foreman_proxy_settingsd_dir}
cp -pa .%{gem_instdir}/settings.d/ansible.yml.example %{buildroot}%{foreman_proxy_settingsd_dir}/ansible.yml

mkdir -p %{buildroot}%{smart_proxy_dynflow_bundlerd_dir}
cat <<EOF > %{buildroot}%{smart_proxy_dynflow_bundlerd_dir}/foreman_ansible_core.rb
gem 'foreman_ansible_core'
EOF

mkdir -p %{buildroot}%{foreman_proxy_dir}

# Ensure all the ansible state is in /var/lib
for i in ansible ansible_galaxy; do
  mkdir -p %{buildroot}%{foreman_proxy_statedir}/$i
  ln -sv %{foreman_proxy_statedir}/$i %{buildroot}%{foreman_proxy_dir}/.$i
done

ln -sv %{_sysconfdir}/foreman-proxy/ansible.cfg %{buildroot}%{foreman_proxy_dir}/.ansible.cfg
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_instdir}/lib
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/smart_proxy_ansible.rb
%config(noreplace) %{foreman_proxy_settingsd_dir}/ansible.yml
%{foreman_proxy_dir}/.ansible
%{foreman_proxy_dir}/.ansible_galaxy
%{foreman_proxy_dir}/.ansible.cfg
%attr(-,foreman-proxy,foreman-proxy) %{foreman_proxy_statedir}/ansible
%attr(-,foreman-proxy,foreman-proxy) %{foreman_proxy_statedir}/ansible_galaxy
%ghost %attr(0640,root,foreman-proxy) %config(noreplace) %{_sysconfdir}/foreman-proxy/ansible.cfg
%license %{gem_instdir}/LICENSE
%{smart_proxy_dynflow_bundlerd_dir}/foreman_ansible_core.rb

%exclude %{gem_instdir}/bundler.plugins.d
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}

%changelog
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

