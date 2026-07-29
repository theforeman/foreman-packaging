%global __brp_mangle_shebangs_exclude_from ^%{_datadir}/%{name}/collections/.*$

Name:      foremanctl
Version:   2.3.0
Release:   4%{?dist}
Summary:   Install Foreman using containers

License:   GPL-2-only
URL:       https://github.com/theforeman/foremanctl
Source:    https://github.com/theforeman/foremanctl/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch
Requires:  python3.12-obsah >= 1.8.1

# These are needed on the target host, which is usually localhost
Recommends:  podman
Recommends:  skopeo
Recommends:  python3-libsemanage
Recommends:  python3-psycopg2
Recommends:  python3-requests
Recommends:  python3-requests-oauthlib

# Tab completion is nice to have
Suggests:  bash-completion
Suggests:  python3-argcomplete

%description
Install Foreman using containers. They are deployed as podman quadlets.

%prep
%setup -q -n %{name}-%{version}

%build
cat > inventories/inventory <<INVENTORY
[quadlet]
localhost ansible_connection=local

[proxy]
localhost ansible_connection=local
INVENTORY

sed -i '/^OBSAH_BASE=/ s|=.\+|=%{_datadir}/%{name}|' %{name}
sed -i '/^OBSAH_INVENTORY=/ s|=.\+|=%{_sysconfdir}/%{name}/inventory|' %{name}
sed -i '/^OBSAH_STATE=/ s|=.\+|=%{_sharedstatedir}/%{name}|' %{name}
sed -i '/^ANSIBLE_COLLECTIONS_PATH=/ s|=.\+|=%{_datadir}/%{name}/collections|' %{name}
sed -i '/^ANSIBLE_LOG_PATH=/ s|=.\+|=%{_localstatedir}/log/%{name}/%{name}.log|' %{name}

%install
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m0755 %{buildroot}%{_datadir}/%{name}
install -d -m0755 %{buildroot}%{_bindir}
install -d -m0750 %{buildroot}%{_sharedstatedir}/%{name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{name}

cp inventories/inventory %{buildroot}%{_sysconfdir}/%{name}/inventory
cp -r src %{buildroot}%{_datadir}/%{name}
cp -r %{name} %{buildroot}%{_bindir}/%{name}
cp -r build/collections/%{name} %{buildroot}%{_datadir}/%{name}/collections


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}
%{_sharedstatedir}/%{name}
%{_localstatedir}/log/%{name}


%changelog
* Wed Jul 29 2026 Zach Huntington-Meath <zhunting@redhat.com> - 2.3.0-4
- Rebuild for EL10

* Wed Jul 22 2026 Arvind Jangir <ajangir@redhat.com> 2.3.0-3
- Add proxy inventory group

* Thu Jun 25 2026 Stejskal Leos - 2.3.0-2
- Add skopeo to the Recommends list

* Mon Jun 08 2026 Evgeni Golov - 2.3.0-1
- Release foremanctl 2.3.0

* Thu May 21 2026 Evgeni Golov - 2.2.0-1
- Release foremanctl 2.2.0

* Tue May 05 2026 Evgeni Golov - 2.1.0-1
- Release foremanctl 2.1.0

* Wed Apr 15 2026 Evgeni Golov - 2.0.0-1
- Release foremanctl 2.0.0

* Mon Mar 16 2026 Evgeni Golov - 1.2.0-1
- Release foremanctl 1.2.0

* Fri Mar 13 2026 Evgeni Golov - 1.1.0-2
- Use Obsah built with Python 3.12

* Fri Jan 09 2026 Evgeni Golov - 1.1.0-1
- Release foremanctl 1.1.0

* Mon Dec 01 2025 Evgeni Golov - 1.0.0-2
- spec with a folder for logging

* Tue Oct 07 2025 akumari <akumari@redhat.com> 1.0.0-1
Initial packaging of foremanctl

