%global gem_name passenger

%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%if 0%{?fedora} >= 19
%global gem_extdir %{gem_extdir_mri}
%endif

%if 0%{?rhel} <= 6
%{!?gem_extdir:%global gem_extdir %{_libdir}/gems/exts/%{gem_name}-%{version}}
%endif

%{!?_root_includedir:%global _root_includedir %{_includedir}}
%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs       %%{_sbindir}/apxs}}
%{!?_httpd_mmn:        %{expand: %%global _httpd_mmn        %%(cat %{_root_includedir}/httpd/.mmn 2>/dev/null || echo missing-httpd-devel)}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:    %{expand: %%global _httpd_moddir    %%{_libdir}/httpd/modules}}

Summary: Passenger Ruby web application server
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.0.18
Release: 9.2%{?dist}
Group: System Environment/Daemons
# Passenger code uses MIT license.
# Bundled(Boost) uses Boost Software License
# BCrypt and Blowfish files use BSD license.
# Documentation is CC-BY-SA
# See: https://bugzilla.redhat.com/show_bug.cgi?id=470696#c146
License: Boost and BSD and BSD with advertising and MIT and zlib

URL: http://www.modrails.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source: https://github.com/FooBarWidget/passenger/archive/release-%{version}.tar.gz
Source1: passenger.logrotate
Source2: rubygem-passenger.tmpfiles
Source10: apache-passenger.conf.in
Source11: locations.ini

# Include sys/types.h for GCC 4.7
Patch2:         rubygem-passenger-4.0.18-gcc47-include-sys_types.patch

# Make example config for tests ready for linux by default
Patch4:        passenger_tests_default_config_example.patch

# Honor CXXFLAGS in the environment.
Patch100:       rubygem-passenger-4.0.18_apache_fix_autofoo.patch

# Test tries to spawn 1000 threads with 256kb stacks. Default Linux settings
# deny allocating so much, causing test to fail. Let's use 8kb stacks instead.
Patch102:       passenger_dynamic_thread_group.patch

# Remove checking for fastthread on F17+
Patch104:       rubygem-passenger-4.0.18_remove_fastthread_dep.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=985634
Patch107:       rubygem-passenger-4.0.18-GLIBC_HAVE_LONG_LONG.patch

# bz1059084 - https://github.com/phusion/passenger/commit/34b1087870c2.patch
Patch108:       rubygem-passenger-4.0.18-tmpsymlink.patch

# bz1059084 - https://github.com/phusion/passenger/commit/94428057c602.patch
Patch109:       rubygem-passenger-4.0.18-CVE-2014-1832.patch

# Until rubygem-bluecloth is in Fedora, don't use it
Patch201:       rubygem-passenger-4.0.18-correct_docs.patch

# Load native library from proper directory
Patch202:       rubygem-passenger-4.0.18_native_dir.patch
Patch203:       rubygem-passenger-4.0.18-daemon-controller.patch

Requires: %{?scl_prefix}rubygems
# XXX: Needed to run passenger standalone
#Requires: %{?scl_prefix}rubygem(daemon_controller) >= 1.0.0
Requires: %{?scl_prefix}rubygem(rack)
Requires: %{?scl_prefix}rubygem(rake)
Requires: %{?scl_prefix}ruby(abi)

%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
BuildRequires:  libcurl-devel
%else
BuildRequires:  curl-devel
%endif

# %if 0%{?rhel} <= 6 && 0%{?fedora} <= 16
# Requires: rubygem(fastthread) >= 1.0.1
# BuildRequires:  rubygem(fastthread) >= 1.0.1
# %endif

BuildRequires: asciidoc
BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: httpd-devel
# BuildRequires: libev-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(rake) >= 0.8.1
BuildRequires: %{?scl_prefix}rubygem(rack)
BuildRequires: %{?scl_prefix}rubygem(rspec)
BuildRequires: %{?scl_prefix}rubygem(mime-types)
# BuildRequires: source-highlight

# XXX
BuildRequires: zlib-devel

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}
Provides: bundled(boost) =  1.44

%description
Phusion Passenger™ — a.k.a. mod_rails or mod_rack — makes deployment
of Ruby web applications, such as those built on the revolutionary
Ruby on Rails web framework, a breeze. It follows the usual Ruby on
Rails conventions, such as “Don’t-Repeat-Yourself”.

%package -n %{?scl_prefix}mod_passenger
Summary: Apache Module for Phusion Passenger
Group: System Environment/Daemons
BuildRequires: httpd-devel
Requires: httpd-mmn = %{_httpd_mmn}
Requires: %{?scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}
Requires: %{name}-native%{?_isa} = %{version}-%{release}
License: Boost and BSD and BSD with advertising and MIT and zlib

%description -n %{?scl_prefix}mod_passenger
This package contains the pluggable Apache server module for Phusion Passenger™.

%package devel
Summary: Apache Module for Phusion Passenger
Group: System Environment/Daemons
Requires: %{?scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}
Provides: bundled(boost-devel) =  1.44
License: Boost and BSD and BSD with advertising and GPL+ and MIT and zlib

%description devel
This package contains development files for Phusion Passenger™.

%package doc
Summary: Apache Module for Phusion Passenger
Group: System Environment/Daemons
Requires: %{?scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}
BuildArch: noarch
License: CC-BY-SA and MIT and (MIT or GPL+)

%description doc
This package contains documentation files for Phusion Passenger™.

%package native
Summary: Phusion Passenger native extensions
Group: System Environment/Daemons
Requires: %{?scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}
Requires: %{name}-native-libs%{?_isa} = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
License: Boost and BSD and BSD with advertising and MIT and zlib
%description native
This package contains the native code extensions for Apache & Nginx
Phusion Passenger™ bindings.

%package native-libs
Summary: Phusion Passenger native extensions
Group: System Environment/Daemons
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{?scl_prefix}ruby
License: Boost and BSD and BSD with advertising and MIT and zlib
%description native-libs
This package contains the native shared library for Apache & Nginx
Phusion Passenger™ bindings, built against ruby sources. It has been
separated so that installing a new ruby interpreter only necessitates
rebuilding this package.


%prep
%setup -q -n %{gem_name}-release-%{version}

%patch2   -p1 -b .include-sys-types
%patch4   -p1 -b .lindefault
%patch100 -p1 -b .autofoo
%patch102 -p1 -b .threadtest

# remove fastthread checking
# %if 0%{?fedora} >= 17
%patch104 -p1 -b .fastthread
# %endif

# fix passenger boost for glibc >= 2.18
%if 0%{?fedora} >= 20
%patch107 -p1 -b .glibc-long
%endif

%patch108 -p1 -b .tmpsymlink
%patch109 -p1 -b .1832

# Until bluecloth is in Fedora, don't use it
%patch201 -p1 -b .docs
%patch202 -p1 -b .nativedir
%patch203 -p1 -b .daemoncontroller

# Don't use bundled libev
# %{__rm} -rf ext/libev

# asciidoc 8.4.x doesn't have an html5 backend
%{__sed} -i 's/-b html5/-b html4/' build/documentation.rb

# fix up install paths
%{__sed} -i \
    -e 's|%%%%GEM_INSTALL_DIR%%%%|%{gem_instdir}|g' \
    -e 's|%%%%APACHE_INSTALLED_MOD%%%%|%{_httpd_moddir}|g' \
    -e 's|%%%%AGENTS_DIR%%%%|%{gem_extdir}/agents|g' \
    -e 's|%%%%NATIVE_SUPPORT_DIR%%%%|%{gem_extdir}/lib|g' \
    lib/phusion_passenger.rb \
    lib/phusion_passenger/native_support.rb \
    ext/common/ResourceLocator.h

# Fix anything executable that does not have a hash-bang
# Why are there executable header files? WTF.
for script in `find . -type f -perm /a+x -name "*.rb" -o -perm /a+x -name "*.h"`; do
    [ -z "`head -n 1 $script | grep \"^#!/\"`" ] && chmod -v 644 $script
done

# Find files with a hash-bang that do not have executable permissions
for script in `find . -type f ! -perm /a+x -name "*.rb"`; do
    [ ! -z "`head -n 1 $script | grep \"^#!/\"`" ] && chmod -v 755 $script
done

%build
# export USE_VENDORED_LIBEV=false
CFLAGS="${CFLAGS:-%optflags} -fno-strict-aliasing" ; export CFLAGS ;
CXXFLAGS="${CXXFLAGS:-%optflags} -fno-strict-aliasing" ; export CXXFLAGS ;
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS ;

%if 0%{?scl:1}
. /opt/rh/%scl/enable
%endif

rake package:gem SKIP_SIGNING=1
rake apache2
#rake nginx

%install
# export USE_VENDORED_LIBEV=false

%if 0%{?scl:1}
. /opt/rh/%scl/enable
%endif

# Install the gem.
gem install -V \
            --local \
            --install-dir %{buildroot}%{gem_dir} \
            --bindir %{buildroot}%{_bindir} \
            --force \
            --rdoc \
            pkg/%{gem_name}-%{version}.gem

# Install locations.ini
install -pm 0644 %{SOURCE11} %{buildroot}%{gem_instdir}/lib/phusion_passenger/
%{__sed} -i 's|@BINDIR@|%{_bindir}|' %{buildroot}%{gem_instdir}/lib/phusion_passenger/locations.ini
%{__sed} -i 's|@GEM_EXTDIR@|%{gem_extdir}|' %{buildroot}%{gem_instdir}/lib/phusion_passenger/locations.ini
%{__sed} -i 's|@GEM_INSTDIR@|%{gem_instdir}|' %{buildroot}%{gem_instdir}/lib/phusion_passenger/locations.ini
%{__sed} -i 's|@GEM_DOCDIR@|%{gem_docdir}|' %{buildroot}%{gem_instdir}/lib/phusion_passenger/locations.ini
%{__sed} -i 's|@HTTPD_MODDIR@|%{_httpd_moddir}|' %{buildroot}%{gem_instdir}/lib/phusion_passenger/locations.ini

# Install Apache module.
%{__mkdir_p} %{buildroot}/%{_httpd_moddir}
install -pm 0755 buildout/apache2/mod_passenger.so %{buildroot}/%{_httpd_moddir}

# Install Apache config.
%{__mkdir_p} %{buildroot}%{_httpd_confdir} %{buildroot}%{_httpd_modconfdir}
%{__sed} -e 's|@PASSENGERROOT@|%{gem_instdir}/lib/phusion_passenger/locations.ini|g' %{SOURCE10} > passenger.conf
%{__sed} -i 's|@BINDIR@|%{_bindir}|' passenger.conf

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
%{__sed} -n /^LoadModule/p passenger.conf > 10-passenger.conf
%{__sed} -i /^LoadModule/d passenger.conf
touch -r %{SOURCE10} 10-passenger.conf
install -pm 0644 10-passenger.conf %{buildroot}%{_httpd_modconfdir}/passenger.conf
%endif
touch -r %{SOURCE10} passenger.conf
install -pm 0644 passenger.conf %{buildroot}%{_httpd_confdir}/passenger.conf


# Install man pages into the proper location.
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__mkdir_p} %{buildroot}%{_mandir}/man8
%{__mv} %{buildroot}%{gem_instdir}/man/*.1 %{buildroot}%{_mandir}/man1
%{__mv} %{buildroot}%{gem_instdir}/man/*.8 %{buildroot}%{_mandir}/man8
rmdir %{buildroot}%{gem_instdir}/man

# The agents aren't in the gem for some reason...
%{__chmod} -R 0755 buildout/agents/*
%{__mkdir_p} %{buildroot}%{gem_extdir}
%{__cp} -a buildout/agents %{buildroot}%{gem_extdir}
%{__rm} -f %{buildroot}%{gem_extdir}/agents/*.o

# Make our ghost log and run directories...
%{__mkdir_p} %{buildroot}%{_localstatedir}/log/passenger-analytics

# logrotate
%{__mkdir_p} %{buildroot}/etc/logrotate.d
install -pm 0644 %{SOURCE1} %{buildroot}/etc/logrotate.d/%{?scl_prefix}passenger
sed -i 's|\$localstatedir|%{_localstatedir}|' \
    %{buildroot}/etc/logrotate.d/%{?scl_prefix}passenger

# # tmpfiles.d
# %if 0%{?fedora} > 15
# %{__mkdir_p} %{buildroot}/run
# %{__mkdir_p} %{buildroot}%{_prefix}/lib/tmpfiles.d
# install -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf
# install -d -m 0755 %{buildroot}/run/%{name}
# %else
%{__mkdir_p} %{buildroot}%{_localstatedir}/run/rubygem-passenger
# %endif

# Bring over just the native binaries
%{__mkdir_p} %{buildroot}%{gem_extdir}/lib/native
install -m 0755 buildout/ruby/ruby*linux/passenger_native_support.so %{buildroot}%{gem_extdir}/lib/native

# Remove zero-length and non-needed files
find %{buildroot}%{gem_instdir} -type f -size 0c -delete
%{__rm} -rf %{buildroot}%{gem_instdir}/.gitignore
%{__rm} -rf %{buildroot}%{gem_instdir}/.yardoc
%{__rm} -rf %{buildroot}%{gem_instdir}/rpm/


# Don't install the installation scripts and Rakefile. That's why we have packaging.
%{__rm} %{buildroot}%{gem_instdir}/bin/%{gem_name}-install-apache2-module
%{__rm} %{buildroot}%{gem_instdir}/bin/%{gem_name}-install-nginx-module
%{__rm} %{buildroot}%{_bindir}/%{gem_name}-install-apache2-module
%{__rm} %{buildroot}%{_bindir}/%{gem_name}-install-nginx-module
%{__rm} %{buildroot}%{gem_instdir}/Rakefile

%check
%if 0%{?scl:1}
. /opt/rh/%scl/enable
%endif

# export USE_VENDORED_LIBEV=false
# Run the tests, capture the output, but don't fail the build if the tests fail
#
# This will make the test failure non-critical, but it should be examined
# anyway.
sed -i 's|sh "cd test && \./cxx/CxxTestMain"|& rescue true|' \
    build/cxx_tests.rb

# Fedora has RSpec 2 while the test suite seems to require RSpec 1.
sed -i \
    "s|return locate_ruby_tool('spec')|return locate_ruby_tool('rspec')|" \
    lib/phusion_passenger/platform_info/ruby.rb

%{__cp} test/config.json.example test/config.json

rake test --trace ||:

%files
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/NEWS
%{gem_cache}
%{gem_spec}
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_instdir}/helper-scripts
%{gem_instdir}/lib
%{gem_instdir}/passenger.gemspec
%{gem_instdir}/resources
%{gem_instdir}/.travis.yml
%{_bindir}/%{gem_name}*
%{_mandir}/man1/%{gem_name}-*
%{_mandir}/man8/%{gem_name}-*
%dir %{_localstatedir}/run/rubygem-passenger
%exclude %{gem_instdir}/configure
%exclude %{gem_instdir}/debian.template/
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/doc

%files devel
%doc %{gem_instdir}/INSTALL.md
%{gem_instdir}/test
%{gem_instdir}/build
%{gem_instdir}/dev
%{gem_instdir}/ext

%files -n %{?scl_prefix}mod_passenger
%config(noreplace) %{_httpd_modconfdir}/*.conf
%{_httpd_moddir}/mod_passenger.so
%doc doc/Users?guide?Apache.txt

%files native
%{gem_extdir}/agents
%dir %{_localstatedir}/log/passenger-analytics
/etc/logrotate.d/%{?scl_prefix}passenger

%files native-libs
%dir %{gem_extdir}
%{gem_extdir}/lib

%changelog
* Tue Apr 22 2014 Dominic Cleal <dcleal@redhat.com> 4.0.18-9.2
- Fix expansion of _root_includedir in non-SCL build (dcleal@redhat.com)

* Tue Apr 22 2014 Dominic Cleal <dcleal@redhat.com> 4.0.18-9.1
- Fix expansion of httpd_mmn in SCL build (dcleal@redhat.com)

* Wed Mar 05 2014 Jan Kaluza <jkaluza@redhat.com> - 4.0.18-9
- fix the dependency on daemon-controller (#1072927)

* Fri Feb 14 2014 Jan Kaluza <jkaluza@redhat.com> - 4.0.18-8
- fix corrupted RI documentation (#1064824)

* Mon Feb 03 2014 Jan Kaluza <jkaluza@redhat.com> - 4.0.18-7
- fix also CVE-2014-1832 (#1059084)

* Wed Jan 29 2014 Jan Kaluza <jkaluza@redhat.com> - 4.0.18-6
- fix a symlink-related security vulnerability (#1059084)

* Tue Nov 26 2013 Joe Orton <jorton@redhat.com> - 4.0.18-5
- build with no-strict-aliasing

* Mon Nov 11 2013 Jan Kaluza <jkaluza@redhat.com> - 4.0.18-4
- load native library from proper path

* Mon Nov 11 2013 Jan Kaluza <jkaluza@redhat.com> - 4.0.18-3
- support for software collections

* Wed Sep 25 2013 Troy Dawson <tdawson@redhat.com> - 4.0.18-2
- Cleanup spec file
- Fix for bz#987879

* Tue Sep 24 2013 Troy Dawson <tdawson@redhat.com> - 4.0.18-1
- Update to 4.0.18
- Remove patches no longer needed
- Update patches that need updating

* Mon Sep 23 2013 Brett Lentz <blentz@redhat.com> - 3.0.21-9
- finish fixing bz#999384

* Fri Sep 20 2013 Joe Orton <jorton@redhat.com> - 3.0.21-8
- update packaging for httpd 2.4.x

* Thu Sep 19 2013 Troy Dawson <tdawson@redhat.com> - 3.0.21-7
- Fix for F20 FTBFS (#993310)

* Thu Aug 22 2013 Brett Lentz <blentz@redhat.com> - 3.0.21-6
- bz#999384

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Troy Dawson <tdawson@redhat.com> - 3.0.21-4
- Fix for CVE-2013-4136 (#985634)

* Fri Jun 21 2013 Troy Dawson <tdawson@redhat.com> - 3.0.21-3
- Putting the agents back to where they originally were

* Fri Jun 21 2013 Troy Dawson <tdawson@redhat.com> - 3.0.21-2
- Remove Rakefile (only used for building) (#976843)

* Thu May 30 2013 Troy Dawson <tdawson@redhat.com> - 3.0.21-1
- Update to version 3.0.21
- Fix for CVE-2013-2119

* Thu May 16 2013 Troy Dawson <tdawson@redhat.com> - 3.0.19-4
- Fix to make agents work on F19+

* Wed Mar 13 2013 Troy Dawson <tdawson@redhat.com> - 3.0.19-3
- Fix to make it build/install on F19+
- Added patch105

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 20 2013 Orion Poplawski <orion@cora.nwra.com> - 3.0.19-1
- Update to 3.0.19

* Wed Sep 19 2012 Orion Poplawski <orion@cora.nwra.com> - 3.0.17-3
- Drop dependency on rubygem(file-tail), no longer needed

* Fri Sep 7 2012 Brett Lentz <blentz@redhat.com> - 3.0.17-2
- Fix License

* Thu Sep 6 2012 Brett Lentz <blentz@redhat.com> - 3.0.17-1
- update to 3.0.17

* Wed Sep 5 2012 Brett Lentz <blentz@redhat.com> - 3.0.14-15
- add support for tmpfiles.d

* Tue Sep 4 2012 Brett Lentz <blentz@redhat.com> - 3.0.14-14
- Fix License tag
- Fix gem_extdir ownership issue

* Wed Aug 29 2012 Brett Lentz <blentz@redhat.com> - 3.0.14-13
- fix pathing issues
- fix ruby abi requires

* Wed Aug 29 2012 Brett Lentz <blentz@redhat.com> - 3.0.14-12
- remove capability for running passenger standalone until daemon_controller is updated

* Tue Aug 28 2012 Brett Lentz <blentz@redhat.com> - 3.0.14-11
- fix issues with fastthread

* Mon Aug 27 2012 Brett Lentz <blentz@redhat.com> - 3.0.14-10
- get test suite sort of working
- move agents to gem_extdir

* Fri Aug 24 2012 Brett Lentz <blentz@redhat.com> - 3.0.14-9
- stop using _bindir
- fix native libs path
- fix ownership on extdir
- improve test output

* Wed Aug 22 2012 Brett Lentz <blentz@redhat.com> - 3.0.14-8
- removed policycoreutils requirement
- moved native libs to gem_extdir

* Wed Aug 22 2012 Brett Lentz <blentz@redhat.com> - 3.0.14-7
- remove selinux policy module. it's in the base policy now.

* Fri Aug 17 2012 Brett Lentz <blentz@redhat.com> - 3.0.14-6
- put native-libs into ruby_vendorarchdir.

* Thu Aug 16 2012 Brett Lentz <blentz@redhat.com> - 3.0.14-5
- clean up packaging and file placement.
- add logrotate file for /var/log/passenger-analytics

* Wed Aug 15 2012 Brett Lentz <blentz@redhat.com> - 3.0.14-4
- backported fix only needed on f18+

* Wed Aug 15 2012 Brett Lentz <blentz@redhat.com> - 3.0.14-3
- backport fix from https://svn.boost.org/trac/boost/ticket/6940

* Mon Aug 13 2012 Brett Lentz <blentz@redhat.com> - 3.0.14-2
- remove F15 conditional. F15 is EOL.

* Fri Jul 27 2012 Troy Dawson <tdawson@redhat.com> - 3.0.14-1
- Updated to version 3.0.14

* Fri Jul 27 2012 Troy Dawson <tdawson@redhat.com> - 3.0.12-6
- Added patch20, spawn-ip
- Changed selinux files to be more dynamic

* Tue Jun 05 2012 Troy Dawson <tdawson@redhat.com> - 3.0.12-5
- Add all the selinux files

* Tue Jun 05 2012 Troy Dawson <tdawson@redhat.com> - 3.0.12-4
- Added selinux configurations

* Tue Jun 05 2012 Troy Dawson <tdawson@redhat.com> - 3.0.12-3
- Added native and native-libs rpms.

* Mon Apr 16 2012 Brett Lentz <blentz@redhat.com> - 3.0.12-2
- Add dist to release.
- Shuffle around deprecated buildrequires and requires.

* Mon Apr 16 2012 Brett Lentz <blentz@redhat.com> - 3.0.12-1
- Update to 3.0.12
- Incorporate specfile changes from kanarip's version

* Wed Apr 11 2012 Brett Lentz <blentz@redhat.com> - 3.0.11-1
- Initial spec file
