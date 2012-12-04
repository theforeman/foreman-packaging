%global homedir %{_datadir}/%{name}
%global confdir config

Name:           foreman-proxy
Version:        1.0.0
Release:        4%{dist}
Summary:        Restful Proxy for DNS, DHCP, TFTP, PuppetCA and Puppet

Group:          Applications/System
License:        GPLv3+
URL:            http://theforeman.org/projects/smart-proxy
Source0:        https://github.com/theforeman/smart-proxy/archive/%{version}.tar.gz
Source1:        foreman-proxy.service
Source2:        foreman-proxy.tmpfiles
Source3:        foreman-proxy.logrotate
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  systemd-units
Requires:       ruby(abi) = 1.9.1
Requires:       rubygems
Requires:       rubygem(rake) >= 0.8.3
Requires:       rubygem(sinatra)
Requires:       rubygem(json)
Requires:       rubygem(net-ping)
Requires(pre):  shadow-utils
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

Packager:       Lukas Zapletal <lzap+git@redhat.com>

%description
Manages DNS, DHCP, TFTP and puppet settinsg though HTTP Restful API
Mainly used by the foreman project (http://theforeman.org)

%prep
%setup -q -n smart-proxy-%{version}
%build

%install
rm -rf %{buildroot}
install -d -m0755 %{buildroot}%{_datadir}/%{name}
install -d -m0755 %{buildroot}%{_datadir}/%{name}/config
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m0750 %{buildroot}%{_var}/run/%{name}

install -Dp -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf
install -Dp -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
cp -p -r bin lib Rakefile %{buildroot}%{_datadir}/%{name}
chmod a+x %{buildroot}%{_datadir}/%{name}/bin/smart-proxy
rm -rf %{buildroot}%{_datadir}/%{name}/*.rb

# remove all test units from productive release
find %{buildroot}%{_datadir}/%{name} -type d -name "test" |xargs rm -rf

# Move config files to %{_sysconfdir}
install -Dp -m0644 %{confdir}/settings.yml.example %{buildroot}%{_sysconfdir}/%{name}/settings.yml
ln -sv %{_sysconfdir}/%{name}/settings.yml %{buildroot}%{_datadir}/%{name}/config/settings.yml

# Put HTML %{_localstatedir}/lib/%{name}/public
for x in public views; do
  cp -pr $x %{buildroot}%{_localstatedir}/lib/%{name}/
  ln -sv %{_localstatedir}/lib/%{name}/$x %{buildroot}%{_datadir}/%{name}/$x
done

# Put logs in %{_localstatedir}/log/%{name}
ln -sv %{_localstatedir}/log/%{name} %{buildroot}%{_datadir}/%{name}/logs

# Link temp directory to system wide temp
ln -sv %{_tmppath} %{buildroot}%{_datadir}/%{name}/tmp

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc README
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_unitdir}/%{name}.service
%{_prefix}/lib/tmpfiles.d/%{name}.conf
%attr(-,%{name},%{name}) %{_localstatedir}/lib/%{name}
%attr(-,%{name},%{name}) %{_localstatedir}/log/%{name}
%attr(-,%{name},%{name}) %{_var}/run/%{name}


%pre
# Add the "foreman-proxy" user and group
getent group foreman-proxy >/dev/null || \
  groupadd -r foreman-proxy
getent passwd foreman-proxy >/dev/null || \
  useradd -r -g foreman-proxy -d %{homedir} -s /sbin/nologin -c "Foreman Proxy deamon user" foreman-proxy
exit 0

%post
if [ $1 -eq 1 ]; then
  /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ]; then
  # Package removal, not upgrade
  /bin/systemctl --no-reload disable foreman-proxy.service >/dev/null 2>&1 || :
  /bin/systemctl stop foreman-proxy.service >/dev/null 2>&1 || :
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
  # Package upgrade, not uninstall
  /bin/systemctl try-restart foreman-proxy.service >/dev/null 2>&1 || :
fi

%triggerun -- foreman-proxy < 1.0.0-4
/usr/bin/systemd-sysv-convert --save foreman-proxy >/dev/null 2>&1 ||:
/sbin/chkconfig --del foreman-proxy >/dev/null 2>&1 || :
/bin/systemctl try-restart foreman-proxy.service >/dev/null 2>&1 || :

%changelog
* Wed Nov 28 2012 Dominic Cleal <dcleal@redhat.com> 1.0.0-4
- Convert to systemd
- Fix missing /var/run/foreman-proxy with tmpfiles.d
* Thu Aug 30 2012 jmontleo@redhat.com 1.0.0-3
- Update to include up to 330dbef353
* Sun Aug 05 2012 jmontleo@redhat.com 1.0.0-2
- Update to pull in fixes
* Mon Jul 23 2012 jmontleo@redhat.com 1.0.0-1
- Update packages for Foreman 1.0 Release.
* Wed Jul 18 2012 jmontleo@redhat.com 1.0.0-0.7
- Updated pacakages for Foreman 1.0 RC5 and Proxy RC2
* Thu Jul 05 2012 jmontleo@redhat.com 1.0.0-0.6
- Fix foreman-release to account for different archs. Pull todays source.
* Wed Jul 04 2012 jmontleo@redhat.com 1.0.0-0.5
- Bump version number for foreman RC3 and build with todays develop branch
* Sun Jul 01 2012 jmontleo@redhat.com 1.0.0-0.4
- Pull todays develop branch
* Fri Jun 29 2012 jmontleo@redhat.com 1.0.0-0.2
- Rebuild with develop branch from today. Hopefully we're really 1.0.0 RC2 this time
* Tue Jun 19 2012 jmontleo@redhat.com 0.5.1-9
- Rebuild with todays develop branch.
* Thu Jun 14 2012 jmontleo@redhat.com 0.5.1-8
- Rebuild with todays develop branch.
* Tue May 08 2012 Jason Montleon <jmontleo@redhat.com> - 0.5.1-1
- update version to match foreman package version
* Wed Dec 28 2011 Ohad Levy <ohadlevy@gmail.com> - 0.3.1
- rebuilt
* Wed Nov 08 2011 Ohad Levy <ohadlevy@gmail.com> - 0.3
- rebuilt
* Wed Sep 28 2011 Ohad Levy <ohadlevy@gmail.com> - 0.3rc2
- rebuilt
* Sat Sep 10 2011 Ohad Levy <ohadlevy@gmail.com> - 0.3rc1
- rebuilt
* Mon Jun 6 2011 Ohad Levy <ohadlevy@gmail.com> - 0.2
- rebuilt
* Thu May 26 2011 ohadlevy@gmail.com - 0.2rc2-2
- rebuilt
* Thu Feb 24 2011 Ohad Levy <ohadlevy@gmail.com> - 0.1.0rc
- new package built with tito
* Wed Jan 26 2011 Lukas Zapletal <lzap+git@redhat.com> - 0.1.0
- new package built with tito
