%global homedir %{_datadir}/%{name}
%global confdir config

%global scl_ruby_bin /usr/bin/%{?scl:%{scl_prefix}}ruby
%global scl_rake /usr/bin/%{?scl:%{scl_prefix}}rake

# set and uncomment all three to set alpha tag
%global alphatag RC1
%global dotalphatag .%{alphatag}
%global dashalphatag -%{alphatag}

Name:           foreman-proxy
Version:        1.16.0
Release: 0.1%{?dotalphatag}%{?dist}
Summary:        Restful Proxy for DNS, DHCP, TFTP, PuppetCA and Puppet

Group:          Applications/System
License:        GPLv3+
URL:            http://theforeman.org/projects/smart-proxy
Source0:        http://downloads.theforeman.org/%{name}/%{name}-%{version}%{?dashalphatag}.tar.bz2
Source1:        %{name}.tmpfiles
Source2:        logrotate.conf

BuildArch:      noarch
BuildRequires:  /usr/bin/rename
BuildRequires:  asciidoc
BuildRequires:  %{?scl_prefix_ruby}rubygem(rake) >= 0.8.3

BuildRequires: %{?scl_prefix_ruby}ruby(release)
Requires:      %{?scl_prefix_ruby}ruby(release)

Requires:       foreman-debug
Requires:       %{?scl_prefix_ruby}rubygems
Requires:       %{?scl_prefix_ruby}rubygem(rake) >= 0.8.3
Requires:       %{?scl_prefix_ruby}rubygem(sinatra)
Requires:       %{?scl_prefix_ruby}rubygem(rack) >= 1.1.0
Requires:       %{?scl_prefix_ruby}rubygem(json)
Requires:       %{?scl_prefix}rubygem(rkerberos)
Requires:       %{?scl_prefix}rubygem(rubyipmi) >= 0.9.2
Requires:       %{?scl_prefix}rubygem(gssapi)
Requires:       %{?scl_prefix}rubygem(bundler_ext)
Requires:       %{?scl_prefix}rubygem(rb-inotify)
Requires:       %{?scl_prefix}rubygem(rsec)
Requires:       %{?scl_prefix}rubygem(concurrent-ruby) >= 1.0
Requires:       %{?scl_prefix}rubygem(concurrent-ruby) < 2.0
Requires:       sudo
Requires:       wget
Requires(pre):  shadow-utils
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
BuildRequires: systemd-units


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
%if 0%{?scl:1}
  for f in bin/smart-proxy extra/query.rb extra/changelog extra/migrate_settings.rb; do
    sed -ri '1sX(/usr/bin/ruby|/usr/bin/env ruby)X%{scl_ruby_bin}X' $f
  done
  sed -ri '1,$sX/usr/bin/rubyX%{scl_ruby_bin}X' extra/spec/foreman-proxy.init
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

# install foreman-devel script
install -Dp -m0755 extra/foreman-debug-proxy %{buildroot}%{_datadir}/foreman/script/foreman-debug.d/75-foreman-proxy

install -d -m0755 %{buildroot}%{_datadir}/%{name}
install -d -m0755 %{buildroot}%{_datadir}/%{name}/config
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}/settings.d
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m0750 %{buildroot}%{_var}/run/%{name}

install -Dp -m0644 extra/systemd/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
# Compatibility with old init script, prefer systemd overrides now
sed -i '/^ExecStart/a EnvironmentFile=-%{_sysconfdir}/sysconfig/%{name}' %{buildroot}%{_unitdir}/%{name}.service

install -Dp -m0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

mkdir -p %{buildroot}%{_sbindir}
install -m 0755 sbin/foreman-prepare-realm %{buildroot}%{_sbindir}/foreman-prepare-realm
cp -p -r bin extra lib modules Rakefile Gemfile.in smart_proxy.gemspec bundler.d config.ru VERSION %{buildroot}%{_datadir}/%{name}
chmod a+x %{buildroot}%{_datadir}/%{name}/bin/smart-proxy
rm -rf %{buildroot}%{_datadir}/%{name}/*.rb

# remove all test units from productive release
find %{buildroot}%{_datadir}/%{name} -type d -name "test" |xargs rm -rf

# Move config files to %{_sysconfdir}
install -Dp -m0644 %{confdir}/settings.yml.example %{buildroot}%{_sysconfdir}/%{name}/settings.yml
ln -sv %{_sysconfdir}/%{name}/settings.yml %{buildroot}%{_datadir}/%{name}/config/settings.yml
install -Dp -m0644 %{confdir}/settings.d/*.example %{buildroot}%{_sysconfdir}/%{name}/settings.d/
rename .example '' %{buildroot}%{_sysconfdir}/%{name}/settings.d/*
touch %{buildroot}%{_sysconfdir}/%{name}/migration_state
ln -sv %{_sysconfdir}/%{name}/migration_state %{buildroot}%{_datadir}/%{name}/config/migration_state

# Put logs in %{_localstatedir}/log/%{name}
ln -sv %{_localstatedir}/log/%{name} %{buildroot}%{_datadir}/%{name}/logs

# Link temp directory to system wide temp
ln -sv %{_tmppath} %{buildroot}%{_datadir}/%{name}/tmp

%files
%doc README.md LICENSE VERSION
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(-,%{name},%{name}) %{_localstatedir}/log/%{name}
%attr(-,%{name},%{name}) %{_var}/run/%{name}
%attr(-,%{name},root) %{_datadir}/%{name}/config.ru
%exclude %{_datadir}/%{name}/bundler.d/development.rb
%exclude %{_datadir}/%{name}/bundler.d/test.rb
%exclude %{_datadir}/%{name}/bundler.d/windows.rb
%{_sbindir}/foreman-prepare-realm
%{_mandir}/man8
%{_unitdir}/%{name}.service
%{_prefix}/lib/tmpfiles.d/%{name}.conf
%{_datadir}/foreman/script/foreman-debug.d/75-foreman-proxy

%pre
# Add the "foreman-proxy" user and group
getent group foreman-proxy >/dev/null || \
  groupadd -r foreman-proxy
getent passwd foreman-proxy >/dev/null || \
  useradd -r -g foreman-proxy -d %{homedir} -s /sbin/nologin -c "Foreman Proxy deamon user" foreman-proxy

exit 0

%post
# Migrate proxy config files
if [ $1 == 2 ]; then
  TEMP=$(mktemp -d)
  trap "rm -rf $TEMP" EXIT
  pushd $TEMP >/dev/null

  if %{scl_ruby_bin} %{homedir}/extra/migrate_settings.rb -t . > %{_localstatedir}/log/%{name}/migrate_settings.log 2>&1; then
    (
      cd result && for f in migration_state settings.yml settings.d/*.yml; do
        [ -e "$f" ] && cat $f > %{_sysconfdir}/%{name}/$f
      done
    )

    # from monolithic to split config files
    egrep -q '^:settings_directory' %{_sysconfdir}/%{name}/settings.yml || \
      sed -i '/^---/ a #replace default location of "settings.d"\n:settings_directory: %{_sysconfdir}/%{name}/settings.d\n' \
        %{_sysconfdir}/%{name}/settings.yml
  fi
  popd >/dev/null
fi

if [ $1 -eq 1 ]; then
  /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
  # Package removal, not upgrade
  /bin/systemctl --no-reload disable foreman-proxy.service >/dev/null 2>&1 || :
  /bin/systemctl stop foreman-proxy.service >/dev/null 2>&1 || :
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
  /bin/systemctl try-restart foreman-proxy.service >/dev/null 2>&1 || :
fi


%changelog
* Thu Sep 21 2017 Daniel Lobato Garcia <me@daniellobato.me> 1.16.0-0.1.RC1
- new package built with tito

* Wed Mar 29 2017 Eric D Helms <ericdhelms@gmail.com> - 1.16.0-0.develop
- Bump version to 1.16-develop

* Tue Dec 06 2016 Dominic Cleal <dominic@cleal.org> - 1.15.0-0.develop
- Bump version to 1.15-develop

* Wed Sep 07 2016 Dominic Cleal <dominic@cleal.org> - 1.14.0-0.develop
- Bump version to 1.14-develop

* Tue May 31 2016 Dominic Cleal <dominic@cleal.org> - 1.13.0-0.develop
- Bump version to 1.13-develop

* Fri Feb 19 2016 Dominic Cleal <dominic@cleal.org> - 1.12.0-0.develop
- Bump version to 1.12-develop

* Wed Oct 07 2015 Dominic Cleal <dcleal@redhat.com> - 1.11.0-0.develop
- Bump version to 1.11-develop

* Fri Jun 26 2015 Dominic Cleal <dcleal@redhat.com> - 1.10.0-0.develop
- Bump version to 1.10-develop

* Tue Mar 03 2015 Dominic Cleal <dcleal@redhat.com> - 1.9.0-0.develop
- Bump version to 1.9-develop

* Tue Oct 28 2014 Dominic Cleal <dcleal@redhat.com> - 1.8.0-0.develop
- Bump version to 1.8-develop

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
