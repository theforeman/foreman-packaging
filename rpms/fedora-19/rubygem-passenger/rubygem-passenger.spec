%global gem_name passenger

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}


%global _missing_build_ids_terminate_build 0
%define debug_package %{nil}

%if 0%{?fedora} >= 19
%global gem_extdir %{gem_extdir_mri}
%endif

%if !("%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16)
%define gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%define gem_cache %{gem_dir}/cache/%{gem_name}-%{version}.gem
%define gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%define gem_spec %{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%define ruby_vendorarchdir %{_libdir}/ruby
%endif

Summary: Passenger Ruby web application server
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.0.5
Release: 4%{?dist}
Group: System Environment/Daemons
# Passenger code uses MIT license.
# Bundled(Boost) uses Boost Software License
# BCrypt and Blowfish files use BSD license.
# Documentation is CC-BY-SA
# See: https://bugzilla.redhat.com/show_bug.cgi?id=470696#c146
License: Boost and BSD and BSD with advertising and MIT and zlib

URL: http://www.modrails.com
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source: http://phusion-passenger.googlecode.com/files/passenger-%{version}.tar.gz
Source1: passenger.logrotate
Source2: rubygem-passenger.tmpfiles
Source10: apache-passenger.conf.in
#Source20: nginx-passenger4.conf.in

# Get passenger to recognize our path preferences
#Patch1:         rubygem-passenger-3.0.12-force-native.patch

# Include sys/types.h for GCC 4.7
Patch2:         passenger_include_sys_types.patch

# Remove signing gems with GPG, requires rubygem-openpgp >= 0.3.0
Patch3:        passenger_do_not_sign_gem.patch

# Make example config for tests ready for linux by default
Patch4:        passenger_tests_default_config_example.patch

#Patch10:        rubygem-passenger-3.0.12-spoof-nginx-install.patch

# Honor CXXFLAGS in the environment.
#Patch100:       passenger_apache_fix_autofoo.patch

# Test tries to spawn 1000 threads with 256kb stacks. Default Linux settings
# deny allocating so much, causing test to fail. Let's use 8kb stacks instead.
#Patch102:       passenger_dynamic_thread_group.patch

# Use rspec2 conventions
#Patch103:       passenger_rspec2_helper.patch

# Remove checking for fastthread on F17+
Patch104:       passenger_remove_fastthread_dep.patch

# removes -Werror in upstream build scripts.  -Werror conflicts with
# -D_FORTIFY_SOURCE=2 causing warnings to turn into errors.
##Patch200:       nginx-auto-cc-gcc.patch

Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem(daemon_controller) >= 1.1.0
Requires: %{?scl_prefix}rubygem(rack)
Requires: %{?scl_prefix}rubygem(rake)
%if 0%{?fedora} >= 19
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby
%endif

%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
BuildRequires:  libcurl-devel
%else
BuildRequires:  curl-devel
%endif

%if "%{?scl}" != "ruby193" && 0%{?rhel} <= 6 && 0%{?fedora} <= 16
Requires: %{?scl_prefix}rubygem(fastthread) >= 1.0.1
BuildRequires:  %{?scl_prefix}rubygem(fastthread) >= 1.0.1
%endif

BuildRequires: asciidoc
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: httpd-devel
BuildRequires: libev-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires: %{?scl_prefix}rubygems

%if "%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16
BuildRequires: %{?scl_prefix}rubygems-devel
%endif

BuildRequires: %{?scl_prefix}rubygem(rake) >= 0.8.1
BuildRequires: %{?scl_prefix}rubygem(rack)
BuildRequires: %{?scl_prefix}rubygem(rspec)
BuildRequires: %{?scl_prefix}rubygem(mime-types)
BuildRequires: source-highlight

# XXX
BuildRequires: zlib-devel

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}
Provides: %{?scl_prefix}bundled(boost) =  1.44

%description
Phusion Passenger™ — a.k.a. mod_rails or mod_rack — makes deployment
of Ruby web applications, such as those built on the revolutionary
Ruby on Rails web framework, a breeze. It follows the usual Ruby on
Rails conventions, such as “Don’t-Repeat-Yourself”.

%package -n %{?scl_prefix}mod_passenger
Summary: Apache Module for Phusion Passenger
Group: System Environment/Daemons
BuildRequires:  httpd-devel
Requires: httpd >= 2.2
Requires: %{?scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}
Requires: %{?scl_prefix}%{pkg_name}-native%{?_isa} = %{version}-%{release}
License: Boost and BSD and BSD with advertising and MIT and zlib

%description -n %{?scl_prefix}mod_passenger
This package contains the pluggable Apache server module for Phusion Passenger™.

%package devel
Summary: Apache Module for Phusion Passenger
Group: System Environment/Daemons
Requires: %{?scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}
Provides: %{?scl_prefix}bundled(boost-devel) =  1.44
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
Requires: %{?scl_prefix}%{pkg_name}-native-libs%{?_isa} = %{version}-%{release}
Requires: %{?scl_prefix}%{pkg_name}%{?_isa} = %{version}-%{release}
Requires: libev
License: Boost and BSD and BSD with advertising and MIT and zlib
%description native
This package contains the native code extensions for Apache & Nginx
Phusion Passenger™ bindings.

%package native-libs
Summary: Phusion Passenger native extensions
Group: System Environment/Daemons
Requires: %{?scl_prefix}%{pkg_name}%{?_isa} = %{version}-%{release}
Requires: %{?scl_prefix}ruby
License: Boost and BSD and BSD with advertising and MIT and zlib
%description native-libs
This package contains the native shared library for Apache & Nginx
Phusion Passenger™ bindings, built against ruby sources. It has been
separated so that installing a new ruby interpreter only necessitates
rebuilding this package.


%prep
%setup -q -n passenger-%{version}

#%patch1   -p1 -b .force-native
%patch2   -p1 -b .include-sys-types
%patch3   -p1 -b .nosign
%patch4   -p1 -b .lindefault

#%patch20  -p1 -b .spawnip
#%patch100 -p0 -b .autofoo
#%patch102 -p1 -b .threadtest
#%patch103 -p1 -b .rspec2

# remove fastthread checking
%if "%{?scl}" == "ruby193" || 0%{?fedora} >= 17
%patch104 -p1 -b .fastthread
%endif

# Don't use bundled libev
%{__rm} -rf ext/libev

# asciidoc 8.4.x doesn't have an html5 backend
%{__sed} -i 's/-b html5/-b html4/' build/documentation.rb

# fix up install paths
%{__sed} -i \
    -e 's|%%%%GEM_INSTALL_DIR%%%%|%{gem_instdir}|g' \
    -e 's|%%%%APACHE_INSTALLED_MOD%%%%|%{_libdir}/httpd/modules/|g' \
    -e 's|%%%%AGENTS_DIR%%%%|%{gem_instdir}/agents|g' \
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
%{?scl:scl enable %{scl} '}
export USE_VENDORED_LIBEV=false
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ;
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS ;
#CONFIGURE_ARGS='--with-cflags='%{optflags}'' ; export CONFIGURE_ARGS ;

rake package:gem
rake apache2
#rake nginx
%{?scl: '}

%install
export USE_VENDORED_LIBEV=false
export MANPATH=%{_mandir}:\$MANPATH

# Install the gem.
%{?scl:scl enable %{scl} "}
gem install -V \
            --local \
            --install-dir %{buildroot}%{gem_dir} \
            --bindir %{buildroot}%{gem_instdir}/bin \
            --force \
            --rdoc \
            pkg/%{gem_name}-%{version}.gem
%{?scl:"}

# Install Apache module.
%{__mkdir_p} %{buildroot}/%{_libdir}/httpd/modules
install -pm 0755 libout/apache2/mod_passenger.so %{buildroot}/%{_libdir}/httpd/modules

# Install Apache config.
%{__mkdir_p} %{buildroot}/%{_sysconfdir}/httpd/conf.d
install -pm 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/httpd/conf.d/passenger.conf
%{__sed} -i -e 's|@PASSENGERROOT@|%{gem_instdir}|g' %{buildroot}/%{_sysconfdir}/httpd/conf.d/passenger.conf

# Install man pages into the proper location.
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__mkdir_p} %{buildroot}%{_mandir}/man8
%{__mv} %{buildroot}%{gem_instdir}/man/*.1 %{buildroot}%{_mandir}/man1
%{__mv} %{buildroot}%{gem_instdir}/man/*.8 %{buildroot}%{_mandir}/man8
rmdir %{buildroot}%{gem_instdir}/man

# The agents aren't in the gem for some reason...
%{__chmod} -R 0755 agents/*
%{__mkdir_p} %{buildroot}%{gem_instdir}
%{__cp} -a agents %{buildroot}%{gem_instdir}

# Make our ghost log and run directories...
%{__mkdir_p} %{buildroot}%{_localstatedir}/log/passenger-analytics

# logrotate
%{__mkdir_p} %{buildroot}%{_sysconfdir}/logrotate.d
install -pm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/passenger

# tmpfiles.d
%if 0%{?fedora} > 15
%{__mkdir_p} %{buildroot}/run
%{__mkdir_p} %{buildroot}%{_prefix}/lib/tmpfiles.d
install -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/tmpfiles.d/%{pkg_name}.conf
install -d -m 0755 %{buildroot}/run/%{pkg_name}
%else
%{__mkdir_p} %{buildroot}%{_localstatedir}/run/%{pkg_name}
%endif

# Fix wrong EOF encoding on the RI files...
for file in `find %{buildroot}%{gem_docdir} -type f -name "*.ri"`; do
    sed -i 's/\r//' $file
done

# Bring over just the native binaries
%if "%{?scl}" != "ruby193" && 0%{?rhel} <= 6 && 0%{?fedora} < 17
%{__mkdir_p} %{buildroot}%{_libdir}/ruby/site_ruby/1.8
install -m 0755 libout/ruby/ruby*linux/passenger_native_support.so %{buildroot}%{_libdir}/ruby/site_ruby/1.8
%else
%{__mkdir_p} %{buildroot}%{ruby_vendorarchdir}
install -m 0755 libout/ruby/ruby*linux/passenger_native_support.so %{buildroot}%{ruby_vendorarchdir}
%endif

# Remove zero-length files
find %{buildroot}%{gem_instdir} -type f -size 0c -delete

%{__rm} -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/.yardoc

# Install binaries
mkdir -p %{buildroot}%{_bindir}
# Don't install the installation scripts. That's why we have packaging.
%{__rm} %{buildroot}%{gem_instdir}/bin/%{gem_name}-install-apache2-module
%{__rm} %{buildroot}%{gem_instdir}/bin/%{gem_name}-install-nginx-module
cp -a %{buildroot}%{gem_instdir}/bin/* %{buildroot}%{_bindir}
find %{buildroot}%{_bindir} -type f | xargs chmod a+x

%check
export USE_VENDORED_LIBEV=false
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

%{__mkdir_p} test/stub/wsgi/tmp

%{?scl:scl enable %{scl} "}
rake test --trace ||:
%{?scl:"}

%files
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/NEWS
%{gem_cache}
%{gem_spec}
%{gem_instdir}/passenger.gemspec
%{gem_instdir}/.travis.yml
%dir %{gem_instdir}
%{_bindir}/passenger
%{_bindir}/passenger-config
%{_bindir}/passenger-status
%{_bindir}/passenger-memory-stats
%{gem_instdir}/bin
%{gem_instdir}/helper-scripts
%{gem_instdir}/lib
%{gem_instdir}/resources
%{_mandir}/man1/%{gem_name}-*
%{_mandir}/man8/%{gem_name}-*
%if 0%{?fedora} > 15
%{_prefix}/lib/tmpfiles.d/%{pkg_name}.conf
%dir /run/rubygem-passenger
%else
%dir %{_localstatedir}/run/rubygem-passenger
%endif
%exclude %{gem_instdir}/configure
%exclude %{gem_instdir}/debian/
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/doc

%files devel
%doc %{gem_instdir}/INSTALL.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_instdir}/build
%{gem_instdir}/dev
%{gem_instdir}/ext

%files -n %{?scl_prefix}mod_passenger
%config(noreplace) %{_sysconfdir}/httpd/conf.d/passenger.conf
%doc doc/Users?guide?Apache.txt
%{_libdir}/httpd/modules/mod_passenger.so

%files native
%{gem_instdir}/agents
%dir %{_localstatedir}/log/passenger-analytics
%{_sysconfdir}/logrotate.d/passenger

%files native-libs
%if "%{?scl}" != "ruby193" && 0%{?rhel} <= 6 && 0%{?fedora} < 17
%dir %{_libdir}/ruby/site_ruby/1.8
%{_libdir}/ruby/site_ruby/1.8
%else
%dir %{ruby_vendorarchdir}
%{ruby_vendorarchdir}
%endif

%changelog
* Mon Jun 10 2013 Martin Bačovský <mbacovsk@redhat.com> 4.0.5-4
- Fixed native-libs paths on F18 (mbacovsk@redhat.com)

* Thu Jun 06 2013 Martin Bačovský <mbacovsk@redhat.com> 4.0.5-3
- Fixed binary utils path and manpath (mbacovsk@redhat.com)

* Wed Jun 05 2013 Martin Bačovský <mbacovsk@redhat.com> 4.0.5-2
- new package built with tito
- update to 4.0.5
- support for SCL

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
