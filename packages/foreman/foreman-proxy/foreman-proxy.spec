%global homedir %{_datadir}/%{name}
%global confdir config

%global release 1
%global prereleasesource develop
%global prerelease %{?prereleasesource}

Name:           foreman-proxy
Version:        3.17.0
Release:        %{?prerelease:0.}%{release}%{?prerelease:.}%{?prerelease}%{?nightly}%{?dist}
Summary:        Restful Proxy for DNS, DHCP, TFTP, PuppetCA and Puppet

Group:          Applications/System
License:        GPLv3+
URL:            https://theforeman.org/projects/smart-proxy
Source0:        https://downloads.theforeman.org/%{name}/%{name}-%{version}%{?prerelease:-}%{?prerelease}.tar.bz2
Source1:        %{name}.tmpfiles
Source2:        logrotate.conf

BuildArch:      noarch
BuildRequires:  /usr/bin/rename
BuildRequires:  asciidoc
BuildRequires:  rubygem(rake) >= 0.8.3
Requires:       rubygem(rake) >= 0.8.3

BuildRequires:  ruby(release) >= 2.5
Requires:       ruby(release) >= 2.5
Requires:       rubygems
Requires:       rubygem(bundler_ext)

# Require fapolicyd package if fapolicyd is present
Requires: (%{name}-fapolicyd if fapolicyd)

# These come from smart_proxy.gemspec - get-gemfile-deps can't handle that yet
Requires:       (rubygem(base64) or ruby-default-gems < 3.4)
Requires:       rubygem(json)
Requires:       rubygem(rack) >= 1.3.0
Requires:       (rubygem(sd_notify) >= 0.1 with rubygem(sd_notify) < 0.2)
Requires:       (rubygem(logging) >= 1.8.0 with rubygem(logging) < 3.0.0)
Requires:       (rubygem(rexml) >= 3.2.0 with rubygem(rexml) < 4.0.0)
Requires:       rubygem(sinatra)

# start specfile default Requires
Requires: (rubygem(concurrent-ruby) >= 1.0 with rubygem(concurrent-ruby) < 2.0)
# end specfile default Requires

# start specfile bmc Requires
Requires: rubygem(rubyipmi) >= 0.10.0
Requires: rubygem(redfish_client) >= 0.5.1
# end specfile bmc Requires

# This is a group within bundler.d/dhcp_isc.rb
# start specfile dhcp_isc_inotify Requires
Requires: rubygem(rsec) < 1
Requires: rubygem(rb-inotify)
# end specfile dhcp_isc_inotify Requires

# start specfile krb5 Requires
Requires: rubygem(rkerberos) >= 0.1.1
Requires: rubygem(gssapi)
# end specfile krb5 Requires

# start specfile libvirt Requires
Requires: rubygem(ruby-libvirt) >= 0.6.0
# end specfile libvirt Requires

# start specfile puppetca_token_whitelisting Requires
Requires: rubygem(jwt)
# end specfile puppetca_token_whitelisting Requires

# start specfile realm_freeipa Requires
Requires: (rubygem(xmlrpc) >= 0.2 with rubygem(xmlrpc) < 1.0)
# end specfile realm_freeipa Requires

Requires:       sudo
Requires:       curl
Requires(pre):  shadow-utils
%{?systemd_requires}
BuildRequires: systemd

%description
Manages DNS, DHCP, TFTP and puppet settings though HTTP Restful API
Mainly used by the foreman project (https://theforeman.org)

%prep
%setup -q -n %{name}-%{version}%{?prerelease:-}%{?prerelease}

%build
#build man pages
/usr/bin/rake -f Rakefile.dist build \
PREFIX=%{_prefix} \
SBINDIR=%{_sbindir} \
SYSCONFDIR=%{_sysconfdir} \
--trace

#replace default location of 'settings.d'
sed -i '/^---/ a #replace default location of "settings.d"\n:settings_directory: %{_sysconfdir}/%{name}/settings.d\n' \
  %{confdir}/settings.yml.example

# switches to bundler_ext instead of bundler
mv Gemfile Gemfile.in

%install
rm -rf %{buildroot}
#install man pages
/usr/bin/rake -f Rakefile.dist install \
PREFIX=%{buildroot}%{_prefix} \
SBINDIR=%{buildroot}%{_sbindir} \
SYSCONFDIR=%{buildroot}%{_sysconfdir} \
--trace
/usr/bin/rake -f Rakefile.dist clean

# install foreman-devel script
install -Dp -m0755 extra/foreman-debug-proxy %{buildroot}%{_datadir}/foreman/script/foreman-debug.d/75-foreman-proxy

install -d -m0755 %{buildroot}%{_datadir}/%{name}
install -d -m0755 %{buildroot}%{_datadir}/%{name}/config
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}/settings.d
install -d -m0755 %{buildroot}%{_sharedstatedir}/%{name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m0750 %{buildroot}%{_localstatedir}/spool/%{name}
install -d -m0750 %{buildroot}%{_rundir}/%{name}

install -Dp -m0644 extra/systemd/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
# Compatibility with old init script, prefer systemd overrides now
sed -i '/^ExecStart/a EnvironmentFile=-%{_sysconfdir}/sysconfig/%{name}' %{buildroot}%{_unitdir}/%{name}.service

install -Dp -m0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

mkdir -p %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
install -m 0755 extra/puppet_sign.rb %{buildroot}%{_libexecdir}/%{name}/puppet_sign.rb

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
%doc README.md VERSION
%license LICENSE
%{_datadir}/%{name}
%{_libexecdir}/%{name}/puppet_sign.rb
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/migration_state
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/settings.yml
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/settings.d/*yml
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(-,%{name},%{name}) %{_localstatedir}/log/%{name}
%attr(-,%{name},%{name}) %{_localstatedir}/spool/%{name}
%attr(-,%{name},%{name}) %{_sharedstatedir}/%{name}
%attr(-,%{name},%{name}) %{_rundir}/%{name}
%attr(-,%{name},root) %{_datadir}/%{name}/config.ru
%exclude %{_datadir}/%{name}/bundler.d/development.rb
%exclude %{_datadir}/%{name}/bundler.d/test.rb
%exclude %{_datadir}/%{name}/bundler.d/windows.rb
%exclude %{_datadir}/%{name}/bundler.d/journald.rb
%{_sbindir}/foreman-prepare-realm
%{_mandir}/man8
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{_datadir}/foreman/script/foreman-debug.d/75-foreman-proxy

%package journald
Summary:  Foreman Proxy journald logging dependencies
Group:    Applications/System
# start specfile journald Requires
Requires: (rubygem(logging-journald) >= 2.0 with rubygem(logging-journald) < 3.0)
# end specfile journald Requires
Requires: %{name} = %{version}-%{release}

%description journald
Additional dependencies required to configure journald logging.

%files journald
%{_datadir}/%{name}/bundler.d/journald.rb

%pre
# Add the "foreman-proxy" user and group
getent group foreman-proxy >/dev/null || \
  groupadd -r foreman-proxy
getent passwd foreman-proxy >/dev/null || \
  useradd -r -g foreman-proxy -d %{homedir} -s /sbin/nologin -c "Foreman Proxy daemon user" foreman-proxy
exit 0

%post
# Migrate proxy config files
if [ $1 == 2 ]; then
  TEMP=$(mktemp -d)
  trap "rm -rf $TEMP" EXIT
  pushd $TEMP >/dev/null

  if /usr/bin/ruby %{homedir}/extra/migrate_settings.rb -t . > %{_localstatedir}/log/%{name}/migrate_settings.log 2>&1; then
    (
      cd result && for f in migration_state settings.yml settings.d/*.yml; do
        [ -e "$f" ] && cat $f > %{_sysconfdir}/%{name}/$f
      done
    )

    # from monolithic to split config files
    grep -q -E '^:settings_directory' %{_sysconfdir}/%{name}/settings.yml || \
      sed -i '/^---/ a #replace default location of "settings.d"\n:settings_directory: %{_sysconfdir}/%{name}/settings.d\n' \
        %{_sysconfdir}/%{name}/settings.yml
  fi
  popd >/dev/null
fi

%systemd_post %{name}.service

# Enforce tmpfiles run
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
exit 0

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%changelog
* Wed Aug 13 2025 Ondřej Gajdušek <ogajduse@redhat.com> - 3.17.0-0.1.develop
- Bump version to 3.17-develop

* Mon May 19 2025 Ondřej Gajdušek <ogajduse@redhat.com> - 3.16.0-0.1.develop
- Bump version to 3.16-develop

* Thu Apr 10 2025 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.15.0-0.2.develop
- Add dependency on base64 gem

* Tue Feb 18 2025 Patrick Creech <pcreech@redhat.com> - 3.15.0-0.1.develop
- Bump version to 3.15-develop

* Fri Jan 24 2025 Adam Ruzicka <aruzicka@redhat.com> - 3.14.0-0.2.develop
- Declare rexml as dependency

* Wed Nov 06 2024 Patrick Creech <pcreech@redhat.com> - 3.14.0-0.1.develop
- Bump version to 3.14-develop

* Tue Aug 20 2024 Patrick Creech <pcreech@redhat.com> - 3.13.0-0.1.develop
- Bump version to 3.13-develop

* Wed May 22 2024 Zach Huntington-Meath <zhunting@redhat.com> - 3.12.0-0.1.develop
- Bump version to 3.12-develop

* Tue Feb 20 2024 Patrick Creech <pcreech@redhat.com> - 3.11.0-0.1.develop
- Bump version to 3.11-develop

* Wed Jan 03 2024 Evgeni Golov - 3.10.0-0.2.develop
- Drop requirement on foreman-debug

* Wed Nov 29 2023 Zach Huntington-Meath <zhunting@redhat.com> - 3.10.0-0.1.develop
- Bump version to 3.10-develop

* Fri Nov 24 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.9.0-0.3.develop
- Update Gem dependencies

* Fri Oct 13 2023 Eric D. Helms <ericdhelms@gmail.com> - 3.9.0-0.2.develop
- Require fapolicyd rules package if fapolicyd is present

* Wed Aug 23 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.9.0-0.1.develop
- Bump version to 3.9-develop

* Tue May 23 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.8.0-0.1.develop
- Bump version to 3.8-develop

* Thu May 11 2023 Evgeni Golov - 3.7.0-0.3.develop
- drop SCL bits from spec file

* Thu May 04 2023 Evgeni Golov - 3.7.0-0.2.develop
- use grep -E instead of egrep in post script

* Wed Feb 22 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.7.0-0.1.develop
- Bump version to 3.7-develop

* Tue Dec 13 2022 Adam Ruzicka <aruzicka@redhat.com> - 3.6.0-0.2.develop
- Notify only the main process on logrotate

* Tue Nov 08 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.6.0-0.1.develop
- Bump version to 3.6-develop

* Wed Aug 10 2022 Patrick Creech <pcreech@redhat.com> - 3.5.0-0.1.develop
- Bump version to 3.5-develop

* Tue May 10 2022 Odilon Sousa <osousa@redhat.com> - 3.4.0-0.1.develop
- Bump version to 3.4-develop

* Thu Feb 10 2022 Zach Huntington-Meath <zhunting@redhat.com> - 3.3.0-0.1.develop
- Bump version to 3.3-develop

* Fri Nov 12 2021 Odilon Sousa <osousa@redhat.com> - 3.2.0-0.1.develop
- Bump version to 3.2-develop

* Tue Nov 09 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.1.0-0.2.develop
- Swap wget for curl dependency

* Thu Aug 05 2021 Patrick Creech <pcreech@redhat.com> - 3.1.0-0.1.develop
- Bump version to 3.1-develop

* Thu Jul 22 2021 Tomer Brisker <tbrisker@gmail.com> - 3.0.0-0.1.develop
- Bump version to 3.0-develop

* Tue May 04 2021 Zach Huntington-Meath <zhunting@redhat.com> - 2.6.0-0.1.develop
- Bump version to 2.6-develop

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.5.0-0.2.develop
- Rebuild against rh-ruby27

* Tue Feb 02 2021 Evgeni Golov - 2.5.0-0.1.develop
- Bump version to 2.5-develop

* Mon Nov 02 2020 Patrick Creech <pcreech@redhat.com> - 2.4.0-0.1.develop
- Bump version to 2.4-develop

* Mon Oct 26 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.0-0.4.develop
- Update Gem dependencies

* Fri Sep 04 2020 Lukas Zapletal <lzap+rpm@redhat.com> - 2.3.0-0.3.develop
- Enforce tmpfiles

* Wed Sep 02 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.0-0.2.develop
- Add sd_notify gem dependency (#30731)

* Tue Aug 11 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.3.0-0.1.develop
- Bump version to 2.3-develop

* Thu Jun 25 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.2.0-0.4.develop
- Update Gem dependencies

* Sun Jun 21 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.2.0-0.3.develop
- Set config file modes to 0640 and ownership to foreman-proxy

* Wed May 13 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.2.0-0.2.develop
- Bump version to 2.2-develop

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.1.0-0.2.develop
- Bump to release for EL8

* Thu Feb 13 2020 Tomer Brisker <tbrisker@gmail.com> - 2.1.0-0.1.develop
- Bump version to 2.1-develop

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.0-0.3.develop
- Update spec to remove the ror scl

* Wed Jan 08 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.0.0-0.2.develop
- Update and rebuild into SCL

* Mon Jan 06 2020 Tomer Brisker <tbrisker@gmail.com> - 2.0.0-0.1.develop
- Bump version to 2.0-develop

* Mon Nov 18 2019 Evgeni Golov - 1.25.0-0.2.develop
- Unify prerelease macro handling

* Wed Oct 30 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.25.0-0.1.develop
- Bump version to 1.25-develop

* Wed Sep 18 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.24.0-0.2.develop
- Updates to build for SCL

* Tue Jul 30 2019 Evgeni Golov - 1.24.0-0.1.develop
- Bump version to 1.24-develop

* Tue Apr 23 2019 Evgeni Golov <evgeni@golov.de> - 1.23.0-0.1.develop
- Bump version to 1.23-develop

* Wed Jan 16 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.22.0-0.1.develop
- Bump to 1.22

* Fri Nov 16 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.21.0-0.4.develop
- Handle a missing prerelease macro

* Wed Oct 24 2018 Adam Price <komidore64@gmail.com> - 1.21.0-0.3.develop
- add nightly macro

* Wed Oct 24 2018 Lukas Zapletal <lzap+rpm@redhat.com> - 1.21.0-0.2.develop
- Added logging and logging-journald dependencies

* Wed Oct 17 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.21.0-0.1.develop
- Bump version to 1.21 and reset release

* Thu Sep 13 2018 Timo Goebel <mail@timogoebel.name> - 1.20.0-0.2.develop
- add puppetca_token_whitelisting provider helper script

* Wed Jul 25 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.20.0-0.1.develop
- Add prerelease macro

* Tue Jul 17 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.20.0-0.develop
- Bump version to 1.20-develop

* Thu May 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.19.0-0.develop
- Bump version to 1.19-develop

* Mon Aug 28 2017 Daniel Lobato Garcia <me@daniellobato.me> - 1.17.0-0.develop
- Bump version to 1.17-develop

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
