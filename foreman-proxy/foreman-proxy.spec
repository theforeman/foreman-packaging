%global homedir %{_datadir}/%{name}
%global confdir config

%if "%{?scl}" == "ruby193"
    %global scl_prefix %{scl}-
    %global scl_ruby /usr/bin/ruby193-ruby
    %global scl_rake /usr/bin/ruby193-rake
%else
    %global scl_ruby /usr/bin/ruby
    %global scl_rake /usr/bin/rake
%endif

# set and uncomment all three to set alpha tag
%global alphatag RC2
%global dotalphatag .%{alphatag}
%global dashalphatag -%{alphatag}

Name:           foreman-proxy
Version:        1.7.0
Release:        0.2%{?dotalphatag}%{?dist}
Summary:        Restful Proxy for DNS, DHCP, TFTP, PuppetCA and Puppet

Group:          Applications/System
License:        GPLv3+
URL:            http://theforeman.org/projects/smart-proxy
Source0:        http://downloads.theforeman.org/%{name}/%{name}-%{version}%{?dashalphatag}.tar.bz2
Source1:        %{name}.sysconfig
Source2:        %{name}.init
Source3:        logrotate
Source4:        %{name}.service
Source5:        %{name}.tmpfiles
Source6:        logrotate.systemd
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  /usr/bin/rename
BuildRequires:  asciidoc
BuildRequires:  %{?scl_prefix}rubygem(rake) >= 0.8.3

%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && "%{?scl}" == "")
BuildRequires: %{?scl_prefix}ruby(abi)
Requires:      %{?scl_prefix}ruby(abi)
%else
BuildRequires: %{?scl_prefix}ruby(release)
Requires:      %{?scl_prefix}ruby(release)
%endif

Requires:       %{?scl_prefix}rubygems
Requires:       %{?scl_prefix}rubygem(rake) >= 0.8.3
Requires:       %{?scl_prefix}rubygem(sinatra)
Requires:       %{?scl_prefix}rubygem(rack) >= 1.1.0
Requires:       %{?scl_prefix}rubygem(json)
Requires:       %{?scl_prefix}rubygem(rkerberos)
Requires:       %{?scl_prefix}rubygem(rubyipmi)
Requires:       %{?scl_prefix}rubygem(gssapi)
Requires:       %{?scl_prefix}rubygem(bundler_ext)
Requires:       sudo
Requires:       wget
Requires(pre):  shadow-utils
%if 0%{?rhel} == 6
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
Requires(postun): initscripts
%else
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
BuildRequires: systemd-units
%endif


%description
Manages DNS, DHCP, TFTP and puppet settings though HTTP Restful API
Mainly used by the foreman project (http://theforeman.org)

%prep
%setup -q -n %{name}-%{version}%{?dashalphatag}

%build
#build man pages
%{scl_rake} -f Rakefile.dist build \
PREFIX=%{_prefix} \
SBINDIR=%{_sbindir} \
SYSCONFDIR=%{_sysconfdir} \
--trace

#replace shebangs for SCL
%if %{?scl:1}%{!?scl:0}
  for f in bin/smart-proxy extra/query.rb extra/changelog extra/migrate_settings.rb; do
    sed -ri '1sX(/usr/bin/ruby|/usr/bin/env ruby)X%{scl_ruby}X' $f
  done
  sed -ri '1,$sX/usr/bin/rubyX%{scl_ruby}X' extra/spec/foreman-proxy.init
%endif

#replace default location of 'settings.d'
sed -i '/^---/ a #replace default location of "settings.d"\n:settings_directory: %{_sysconfdir}/%{name}/settings.d\n' \
  %{confdir}/settings.yml.example

# switches to bundler_ext instead of bundler
mv Gemfile Gemfile.in

%install
rm -rf %{buildroot}
#install man pages
%{scl_rake} -f Rakefile.dist install \
PREFIX=%{buildroot}%{_prefix} \
SBINDIR=%{buildroot}%{_sbindir} \
SYSCONFDIR=%{buildroot}%{_sysconfdir} \
--trace
%{scl_rake} -f Rakefile.dist clean

install -d -m0755 %{buildroot}%{_datadir}/%{name}
install -d -m0755 %{buildroot}%{_datadir}/%{name}/config
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}/settings.d
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m0750 %{buildroot}%{_localstatedir}/lib/rpm-state/%{name}
install -d -m0750 %{buildroot}%{_var}/run/%{name}

%if 0%{?rhel} == 6
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -Dp -m0755 %{SOURCE2} %{buildroot}%{_initrddir}/%{name}
install -Dp -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%else
install -Dp -m0644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}.service
install -Dp -m0644 %{SOURCE5} %{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf
install -Dp -m0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%endif

mkdir -p %{buildroot}%{_sbindir}
install -m 0755 sbin/foreman-prepare-realm %{buildroot}%{_sbindir}/foreman-prepare-realm
cp -p -r bin extra lib modules Rakefile Gemfile.in bundler.d config.ru VERSION %{buildroot}%{_datadir}/%{name}
chmod a+x %{buildroot}%{_datadir}/%{name}/bin/smart-proxy
rm -rf %{buildroot}%{_datadir}/%{name}/*.rb

# remove all test units from productive release
find %{buildroot}%{_datadir}/%{name} -type d -name "test" |xargs rm -rf

# Move config files to %{_sysconfdir}
install -Dp -m0644 %{confdir}/settings.yml.example %{buildroot}%{_sysconfdir}/%{name}/settings.yml
ln -sv %{_sysconfdir}/%{name}/settings.yml %{buildroot}%{_datadir}/%{name}/config/settings.yml
install -Dp -m0644 %{confdir}/settings.d/*.example %{buildroot}%{_sysconfdir}/%{name}/settings.d/
rename .example '' %{buildroot}%{_sysconfdir}/%{name}/settings.d/*

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
%doc README LICENSE VERSION
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(-,%{name},%{name}) %{_localstatedir}/lib/%{name}
%dir %attr(-,%{name},%{name}) %{_localstatedir}/lib/rpm-state/%{name}
%attr(-,%{name},%{name}) %{_localstatedir}/log/%{name}
%attr(-,%{name},%{name}) %{_var}/run/%{name}
%attr(-,%{name},root) %{_datadir}/%{name}/config.ru
%{_sbindir}/foreman-prepare-realm
%{_mandir}/man8
%if 0%{?rhel} == 6
%{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%else
%{_unitdir}/%{name}.service
%{_prefix}/lib/tmpfiles.d/%{name}.conf
%endif

%pre
# Add the "foreman-proxy" user and group
getent group foreman-proxy >/dev/null || \
  groupadd -r foreman-proxy
getent passwd foreman-proxy >/dev/null || \
  useradd -r -g foreman-proxy -d %{homedir} -s /sbin/nologin -c "Foreman Proxy deamon user" foreman-proxy

# Keep monolithic config in case it's replaced with the new default
if [ $1 == 2 -a ! -e %{_sysconfdir}/%{name}/settings.d ]; then
  test -e %{_localstatedir}/lib/rpm-state/%{name} || mkdir -p %{_localstatedir}/lib/rpm-state/%{name}
  cp %{_sysconfdir}/%{name}/settings.yml %{_localstatedir}/lib/rpm-state/%{name}/settings.yml.orig
fi

exit 0

%post
# Migrate legacy monolithic proxy config
if [ $1 == 2 -a -e %{_localstatedir}/lib/rpm-state/%{name}/settings.yml.orig ]; then
  pushd %{_localstatedir}/lib/rpm-state/%{name} >/dev/null
  if %{homedir}/extra/migrate_settings.rb settings.yml.orig; then
    mv settings.yml %{_sysconfdir}/%{name}
    sed -i '/^---/ a #replace default location of "settings.d"\n:settings_directory: %{_sysconfdir}/%{name}/settings.d\n' \
      %{_sysconfdir}/%{name}/settings.yml
    rm -f settings.yml.orig
    ls *.yml >/dev/null 2>&1 && mv *.yml %{_sysconfdir}/%{name}/settings.d/
  else
    rm -f settings.yml.orig
  fi
  popd >/dev/null
fi

%if 0%{?rhel} == 6
  /sbin/chkconfig --add %{name}
  exit 0
%else
  if [ $1 -eq 1 ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
  fi
%endif

%preun
if [ $1 -eq 0 ] ; then
  # Package removal, not upgrade
  %if 0%{?rhel} == 6
    /sbin/service %{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
  %else
    /bin/systemctl --no-reload disable foreman-proxy.service >/dev/null 2>&1 || :
    /bin/systemctl stop foreman-proxy.service >/dev/null 2>&1 || :
  %endif
fi

%postun
%if 0%{?rhel} == 6
  if [ $1 -ge 1 ] ; then
    /sbin/service %{name} restart >/dev/null 2>&1
  fi
%else
  /bin/systemctl daemon-reload >/dev/null 2>&1 || :
  if [ $1 -ge 1 ] ; then
    /bin/systemctl try-restart foreman-proxy.service >/dev/null 2>&1 || :
  fi
%endif


%changelog
* Tue Nov 25 2014 Dominic Cleal <dcleal@redhat.com> 1.7.0-0.2.RC2
- Release 1.7.0-RC2
- refs #7197 - add foreman-prepare-realm man page (stbenjam@redhat.com)

* Tue Nov 11 2014 Dominic Cleal <dcleal@redhat.com> 1.7.0-0.1.RC1
- Release 1.7.0-RC1

* Mon Aug 11 2014 Dominic Cleal <dcleal@redhat.com> - 1.7.0-0.develop
- Bump version to 1.7-develop

* Wed Apr 16 2014 Dominic Cleal <dcleal@redhat.com> - 1.6.0-0.develop
- Bump to version 1.6-develop

* Thu Jan 16 2014 Dominic Cleal <dcleal@redhat.com> - 1.5.0-0.develop
- Bump to version 1.5-develop

* Thu Nov 21 2013 Dominic Cleal <dcleal@redhat.com> - 1.4.0-0.develop
- Bump and change versioning scheme (#3712)
- Ship config.ru for running under Passenger

* Thu Sep 05 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.3.9999-1
- bump to version 1.3-develop

* Wed Jul 03 2013 Dominic Cleal <dcleal@redhat.com> - 1.2.9999-3
- add rubyipmi dependency for BMC support

* Tue Jun 11 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.2.9999-2
- fixed service file for systemd
- /etc/sysconfig configuration is no longer in use for systemd

* Thu May 16 2013 Martin Bačovský <mbacovsk@redhat.com> 1.2.9999-1
- added support for building with tito

* Mon Feb 4 2013 shk@redhat.com 1.1-1
- 1.1 final.

* Fri Jan 25 2013 shk@redhat.com 1.1RC3-1
- Updated to RC3

* Wed Jan 09 2013 shk@redhat.com 1.1RC2-1
- Updated to RC2
- Removed net-ping dependency

* Tue Jan 1 2013 shk@redhat.com 1.1RC1-1
- Update to 1.1RC1

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

* Tue Nov 08 2011 Ohad Levy <ohadlevy@gmail.com> - 0.3
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
