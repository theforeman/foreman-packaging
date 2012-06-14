%global homedir %{_datadir}/%{name}
%global confdir extras/spec

Name:   foreman
Version:0.5.1
Release:8%{dist}
Summary:Systems Management web application

Group:  Applications/System
License:GPLv3+
URL:http://theforeman.org
Source0:http://github.com/ohadlevy/%{name}/tarball/%{name}-%{version}.tar.bz2

Patch0: 0001-foreman-initfix.patch
Patch2: 0003-foreman-add-prepbundle.patch
Patch3: 0004-foreman-mv-settings-into-place.patch

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:  noarch

Requires: ruby(abi) = 1.8
Requires: rubygems
Requires: facter
Requires: puppet >= 0.24.4
Requires(pre):  shadow-utils
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
Requires(postun): initscripts
Requires: rubygem(json)
Requires: rubygem(rails) = 3.0.14
Requires: rubygem(jquery-rails)
Requires: rubygem(rest-client)
Requires: rubygem(acts_as_audited) = 2.0.0
Requires: rubygem-has_many_polymorphs >= 3.0.0.beta1-2
Requires: rubygem(will_paginate) >= 3.0.2
Requires: rubygem(ancestry) >= 1.2.4
Requires: rubygem(scoped_search) >= 2.3.6
Requires: rubygem(net-ldap)
Requires: rubygem(safemode) >= 1.0.1
Requires: rubygem(uuidtools)
Requires: rubygem(rake) >= 0.9.2.2

Provides: %{name}-%{version}-%{release}
#Packager:   Ohad Levy <ohadlevy@gmail.com>

%package virt
Summary: Foreman virt support
Group:  Applications/System
Requires: rubygem(virt) >= 0.2.1
Requires: rubygem(rbovirt) >= 0.0.9
Requires: %{name}-%{version}-%{release}
Requires: foreman-fog-%{version}-%{release}

%description virt
Meta Package to install requirements for virt support

%files virt

%post virt
if ! grep -qx foreman-virt /usr/share/foreman/extras/bundle.list
then
echo foreman-virt >> /usr/share/foreman/extras/bundle.list
fi
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1

%preun virt
if [ $1 = 0 ]; then
sed -i "/^foreman-virt$/d" /usr/share/foreman/extras/bundle.list
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1
fi

%package fog
Summary: Foreman fog support
Group:  Applications/System
Requires: rubygem-fog >= 1.3.1-3
Requires: %{name}-%{version}-%{release}
Provides: foreman-fog-%{version}-%{release}

%description fog
Meta Package to install requirements for fog support

%files fog

%post fog
if ! grep -qx foreman-fog /usr/share/foreman/extras/bundle.list
then
echo foreman-fog >> /usr/share/foreman/extras/bundle.list
fi
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1

%preun fog
if [ $1 = 0 ]; then
sed -i "/^foreman-fog$/d" /usr/share/foreman/extras/bundle.list
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1
fi

%package vmware
Summary: Foreman vmware support
Group:  Applications/System
Requires: rubygem(rbvmomi)
Requires: %{name}-%{version}-%{release}
Requires: foreman-fog-%{version}-%{release}

%description vmware
Meta Package to install requirements for vmware support

%files vmware

%post vmware
if ! grep -qx foreman-vmware /usr/share/foreman/extras/bundle.list
then
echo foreman-vmware >> /usr/share/foreman/extras/bundle.list
fi
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1

%preun vmware
if [ $1 = 0 ]; then
sed -i "/^foreman-vmware$/d" /usr/share/foreman/extras/bundle.list
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1
fi

%package console
Summary: Foreman console support
Group:  Applications/System
Requires: rubygem(awesome_print)
Requires: rubygem(hirb-unicode)
Requires: rubygem(wirb)
Requires: %{name}-%{version}-%{release}

%description console
Meta Package to install requirements for console support

%files console

%post console
if ! grep -qx foreman-console /usr/share/foreman/extras/bundle.list
then
echo foreman-console >> /usr/share/foreman/extras/bundle.list
fi
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1

%postun console
if [ $1 = 0 ]; then
sed -i "/^foreman-console$/d" /usr/share/foreman/extras/bundle.list
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1
fi

%package mysql
Summary: Foreman mysql support
Group:  Applications/System
Requires: rubygem(mysql)
Requires: %{name}-%{version}-%{release}

%description mysql
Meta Package to install requirements for mysql support

%files mysql

%post mysql
if ! grep -qx foreman-mysql /usr/share/foreman/extras/bundle.list
then
echo foreman-mysql >> /usr/share/foreman/extras/bundle.list
fi
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1

%postun mysql
if [ $1 = 0 ]; then
sed -i "/^foreman-mysql$/d" /usr/share/foreman/extras/bundle.list
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1
fi

%package mysql2
Summary: Foreman mysql2 support
Group:  Applications/System
Requires: rubygem(mysql2)
Requires: %{name}-%{version}-%{release}

%description mysql2
Meta Package to install requirements for mysql2 support

%files mysql2

%post mysql2
if ! grep -qx foreman-mysql2 /usr/share/foreman/extras/bundle.list
then
echo foreman-mysql2 >> /usr/share/foreman/extras/bundle.list
fi
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1

%postun mysql2
if [ $1 = 0 ]; then
sed -i "/^foreman-mysql2$/d" /usr/share/foreman/extras/bundle.list
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1
fi

%package postgresql
Summary: Foreman Postgresql support
Group:  Applications/System
Requires: rubygem(pg)
Requires: %{name}-%{version}-%{release}

%description postgresql 
Meta Package to install requirements for postgresql support

%files postgresql

%post postgresql
if ! grep -qx foreman-postgresql /usr/share/foreman/extras/bundle.list
then
echo foreman-postgresql >> /usr/share/foreman/extras/bundle.list
fi
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1

%postun postgresql
if [ $1 = 0 ]; then
sed -i "/^foreman-postgresql$/d" /usr/share/foreman/extras/bundle.list
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1
fi

%package sqlite
Summary: Foreman sqlite support
Group:  Applications/System
Requires: rubygem(sqlite3)
Requires: %{name}-%{version}-%{release}

%description sqlite
Meta Package to install requirements for sqlite support

%files sqlite

%post sqlite
if ! grep -qx foreman-sqlite /usr/share/foreman/extras/bundle.list
then
echo foreman-sqlite >> /usr/share/foreman/extras/bundle.list
fi
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1

%postun sqlite
if [ $1 = 0 ]; then
sed -i "/^foreman-sqlite$/d" /usr/share/foreman/extras/bundle.list
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1
fi

%package devel
Summary: Foreman devel support
Group:  Applications/System
Requires: rubygem(debug)
Requires: %{name}-%{version}-%{release}

%description devel
Meta Package to install requirements for devel support

%files devel

%post devel
if ! grep -qx foreman-devel /usr/share/foreman/extras/bundle.list
then
echo foreman-devel >> /usr/share/foreman/extras/bundle.list
fi
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1

%postun devel
if [ $1 = 0 ]; then
sed -i "/^foreman-devel$/d" /usr/share/foreman/extras/bundle.list
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1
fi

%package test
Summary: Foreman test support
Group:  Applications/System
Requires: rubygem(mocha)
Requires: rubygem(shoulda)
Requires: rubygem(rr)
Requires: rubygem(rake)
Requires: %{name}-%{version}-%{release}

%description test
Meta Package to install requirements for test

%files test

%post test
if ! grep -qx foreman-test /usr/share/foreman/extras/bundle.list
then
echo foreman-test >> /usr/share/foreman/extras/bundle.list
fi
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1

%postun test
if [ $1 = 0 ]; then
sed -i "/^foreman-test$/d" /usr/share/foreman/extras/bundle.list
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1
fi

%description
Foreman is aimed to be a Single Address For All Machines Life Cycle Management.
Foreman is based on Ruby on Rails, and this package bundles Rails and all
plugins required for Foreman to work.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .fixinit
%patch2 -p1 
%patch3 -p1

%build

%install
rm -rf %{buildroot}
install -d -m0755 %{buildroot}%{_datadir}/%{name}
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m0755 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m0755 %{buildroot}%{_localstatedir}/run/%{name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{name}

install -Dp -m0644 %{confdir}/%{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -Dp -m0755 %{confdir}/%{name}.init %{buildroot}%{_initrddir}/%{name}
install -Dp -m0644 %{confdir}/logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
cp -p -r app config config.ru extras lib Rakefile script %{buildroot}%{_datadir}/%{name}
chmod 755 %{buildroot}%{_datadir}/%{name}/extras/prepbundle.sh
#chmod a+x %{buildroot}%{_datadir}/%{name}/script/{console,dbconsole,runner}
rm -rf %{buildroot}%{_datadir}/%{name}/extras/{jumpstart,spec}
# remove all test units from productive release
find %{buildroot}%{_datadir}/%{name} -type d -name "test" |xargs rm -rf

# Move config files to %{_sysconfdir}
mv %{buildroot}%{_datadir}/%{name}/config/database.yml.example %{buildroot}%{_datadir}/%{name}/config/database.yml
mv %{buildroot}%{_datadir}/%{name}/config/email.yaml.example %{buildroot}%{_datadir}/%{name}/config/email.yaml
for i in database.yml email.yaml settings.yaml; do
mv %{buildroot}%{_datadir}/%{name}/config/$i %{buildroot}%{_sysconfdir}/%{name}
ln -sv %{_sysconfdir}/%{name}/$i %{buildroot}%{_datadir}/%{name}/config/$i
done

# Put db in %{_localstatedir}/lib/%{name}/db
cp -pr db/migrate db/seeds.rb %{buildroot}%{_datadir}/%{name}
mkdir %{buildroot}%{_localstatedir}/lib/%{name}/db

ln -sv %{_localstatedir}/lib/%{name}/db %{buildroot}%{_datadir}/%{name}/db
ln -sv %{_datadir}/%{name}/migrate %{buildroot}%{_localstatedir}/lib/%{name}/db/migrate

# Put HTML %{_localstatedir}/lib/%{name}/public
cp -pr public %{buildroot}%{_localstatedir}/lib/%{name}/
ln -sv %{_localstatedir}/lib/%{name}/public %{buildroot}%{_datadir}/%{name}/public

# Put logs in %{_localstatedir}/log/%{name}
ln -sv %{_localstatedir}/log/%{name} %{buildroot}%{_datadir}/%{name}/log

# Put tmp files in %{_localstatedir}/run/%{name}
ln -sv %{_localstatedir}/run/%{name} %{buildroot}%{_datadir}/%{name}/tmp

# Create a script for migrating the database
cat << \EOF > %{buildroot}%{_datadir}/%{name}/extras/dbmigrate
#!/bin/sh
cd .. && /usr/bin/rake db:migrate RAILS_ENV=production
EOF
chmod a+x %{buildroot}%{_datadir}/%{name}/extras/dbmigrate

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc README
%doc VERSION
%{_datadir}/%{name}
%{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(-,%{name},%{name}) %{_localstatedir}/lib/%{name}
%attr(-,%{name},%{name}) %{_localstatedir}/log/%{name}
%attr(-,%{name},%{name}) %{_localstatedir}/run/%{name}
%attr(-,%{name},root) %{_datadir}/%{name}/config.ru
%attr(-,%{name},root) %{_datadir}/%{name}/config/environment.rb
%pre
# Add the "foreman" user and group
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
useradd -r -g %{name} -G puppet -d %{homedir} -s /sbin/nologin -c "Foreman" %{name}
exit 0

%pretrans
# Try to handle upgrades from earlier packages. Replacing a directory with a
# symlink is hampered in rpm by cpio limitations.
datadir=%{_datadir}/%{name}
varlibdir=%{_localstatedir}/lib/%{name}
# remove all active_scaffold left overs
find $datadir -type d -name "active_scaffold*" 2>/dev/null | xargs rm -rf
rm -f $datadir/public/javascripts/all.js 2>/dev/null

if [ ! -d $varlibdir/db -a -d $datadir/db -a ! -L $datadir/db ]; then
  [ -d $varlibdir ] || mkdir -p $varlibdir
  mv $datadir/db $varlibdir/db && ln -s $varlibdir/db $datadir/db
  if [ -d $varlibdir/db/migrate -a ! -L $varlibdir/db/migrate -a ! -d $datadir/migrate ]; then
mv $varlibdir/db/migrate $datadir/migrate && ln -s $datadir/migrate $varlibdir/db/migrate
  fi
fi

if [ ! -d $varlibdir/public -a -d $datadir/public -a ! -L $datadir/public ]; then
  [ -d $varlibdir ] || mkdir -p $varlibdir
  mv $datadir/public $varlibdir/public && ln -s $varlibdir/public $datadir/public
fi

varlibdir=%{_localstatedir}/log # /var/log
if [ ! -d $varlibdir/%{name} -a -d $datadir/log -a ! -L $datadir/log ]; then
  [ -d $varlibdir ] || mkdir -p $varlibdir
  mv $datadir/log $varlibdir/%{name} && ln -s $varlib/%{name} $datadir/log
fi

varlibdir=%{_localstatedir}/run # /var/run
if [ ! -d $varlibdir/%{name} -a -d $datadir/tmp -a ! -L $datadir/tmp ]; then
  [ -d $varlibdir ] || mkdir -p $varlibdir
  mv $datadir/tmp $varlibdir/%{name} && ln -s $varlib/%{name} $datadir/tmp
fi

%post
touch /usr/share/foreman/extras/bundle.list
cd /usr/share/foreman; ./extras/prepbundle.sh >/dev/null 2>&1

/sbin/chkconfig --add %{name} || ::

# initialize/migrate the database (defaults to SQLITE3)
su - foreman -s /bin/bash -c %{_datadir}/%{name}/extras/dbmigrate >/dev/null 2>&1 || :
(/sbin/service foreman status && /sbin/service foreman restart) >/dev/null 2>&1
exit 0

%preun
if [ $1 -eq 0 ] ; then
/sbin/service %{name} stop >/dev/null 2>&1
/sbin/chkconfig --del %{name} || :
fi

%postun
if [ $1 -ge 1 ] ; then
# Restart the service
/sbin/service %{name} restart >/dev/null 2>&1 || :
fi

%changelog
* Thu Jun 14 2012 jmontleo@redhat.com 0.5.1-8
- Rebuild with todays develop branch.
* Wed Jun 13 2012 jmontleo@redhat.com 0.5.1-7
- Rebuild with todays develop branch. Add require for at least rubygem-rake 0.9.2.2. Run rake:db migrate on upgrade.
* Wed May 30 2012 jmontleo@redhat.com 0.5.1-5
- Rebuild with todays merge of compute resource RBAC patch
* Tue May 29 2012 jmontleo@redhat.com 0.5.1-4
- Fix rpm dependencies for foreman-virt and foreman-vmware to include foreman-fog
* Tue May 29 2012 jmontleo@redhat.com 0.5.1-3
- tidy up postinstall prepbundle.sh, rebuild with EC2 support, and split out foreman-fog and foreman-vmware support
* Tue May 08 2012 jmontleo@redhat.com 0.5.1-1
- adding prepbundle.sh to run post install of any foreman packages, other small fixes
* Fri May 04 2012 jmontleo@redhat.com 0.5.1-0.2
- updated foreman to develop branch from May 04 which included many fixes including no longer requiring foreman-virt
* Mon Jan 11 2012 ohadlevy@gmail.com - 0.4.2
- rebuilt
* Mon Dec 6 2011 ohadlevy@gmail.com - 0.4.1
- rebuilt
* Thu Nov 08 2011 ohadlevy@gmail.com - 0.4
- rebuilt
* Thu Nov 07 2011 ohadlevy@gmail.com - 0.4rc5
- rebuilt
* Thu Oct 25 2011 ohadlevy@gmail.com - 0.4rc4
- rebuilt
* Thu Oct 18 2011 ohadlevy@gmail.com - 0.4rc3
- rebuilt
* Sat Sep 28 2011 ohadlevy@gmail.com - 0.4rc2
- rebuilt
* Sat Sep 10 2011 ohadlevy@gmail.com - 0.4rc1
- rebuilt

* Tue Jun 07 2011 ohadlevy@gmail.com - 0.3
- rebuilt

* Tue May 24 2011 ohadlevy@gmail.com - 0.3rc1-2
- rebuilt

* Thu May 05 2011 ohadlevy@gmail.com - 0.3rc1
- rebuilt

* Tue Mar 29 2011 ohadlevy@gmail.com - 0.2
- Version bump to 0.2

* Tue Mar 22 2011 ohadlevy@gmail.com - 0.2-rc1
- rebuilt

* Thu Feb 24 2011 ohadlevy@gmail.com - 0.1.7-rc5
- rebuilt

* Sat Feb 12 2011 ohadlevy@gmail.com - 0.1.7-rc4.1
- rebuilt
* Mon Jan 31 2011 ohadlevy@gmail.com - 0.1.7-rc3.1
- rebuilt
* Tue Jan 18 2011 ohadlevy@gmail.com - 0.1.7-rc2.1
- rebuilt

* Sat Jan 15 2011 ohadlevy@gmail.com - 0.1.7-rc2
- rebuilt

* Fri Dec 17 2010 ohadlevy@gmail.com - 0.1.7rc1
- rebuilt

* Mon Nov 29 2010 ohadlevy@gmail.com - 0.1.6-3
- rebuilt
* Thu Nov 12 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.6-1
- Included fix for #461, as without it newly installed instances are not usable
* Thu Nov 11 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.6
- New upstream version
* Sun Oct 30 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.6rc2
- New release candidate
- Updated configuration file permssion not to break passenger
* Sun Sep 19 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.6rc1
- Removed the depenecy upon rack 1.0.1 as its now bundled within Foreman
* Mon May 31 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.5-1
- New upstream version
- Added migration support between old directory layout to FHS compliancy, upgrades from 0.1-4.x should now work
- Added support for logrotate
- Cleanup old activescaffold plugin leftovers files
* Fri Apr 30 2010 Todd Zullinger <tmz@pobox.com> - 0.1.4-4
- Rework %%install for better FHS compliance
- Misc. adjustments to match Fedora/EPEL packaging guidelines
- Update License field to GPLv3+ to match README
- Use foreman as the primary group for the foreman user instead of puppet
- This breaks compatibility with previous RPM, as directories can't be replaced with links easily.

* Thu Apr 19 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1-4-3
- added status to startup script
- removed puppet module from the RPM

* Thu Apr 12 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.4-2
- Added startup script for built in webrick server
- Changed foreman user default shell to /sbin/nologin and is now part of the puppet group
- defaults to sqlite database

* Thu Apr 6 2010 Ohad Levy <ohadlevy@gmail.com> - 0.1.4-1
- Initial release.
