%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygems}
# Upstream git:
# https://github.com/rubygems/rubygems.git
#

# The RubyGems library has to stay out of Ruby directory three, since the
# RubyGems should be share by all Ruby implementations.
%global rubygems_dir %{_datadir}/rubygems

# Specify custom RubyGems root and other related macros.
%global gem_dir %{_datadir}/gems
# TODO: Should we create arch specific rubygems-filesystem?
%global gem_extdir %{_exec_prefix}/lib{,64}/gems

# Executing testsuite (enabling %%check section) will cause dependency loop.
# To avoid dependency loop when necessary, please set the following value to 0
%global	enable_check	1

Summary:	The Ruby standard for packaging ruby libraries
Name:		%{?scl_prefix}rubygems
Version:	1.8.24
Release:	3%{?dist}
Group:		Development/Libraries
License:	Ruby or MIT

URL:		https://rubygems.org/
Source0:	http://production.cf.rubygems.org/rubygems/%{pkg_name}-%{version}.tgz

# Sources from the works by Vít Ondruch <vondruch@redhat.com>
# Please keep Source100 and Patch{105,109} in sync with ruby.spec

Source100:	operating_system.rb

# Kill patch0 for ruby 1.9.x
##Patch0:		rubygems-1.8.5-noarch-gemdir.patch
# Will discuss upstream
# https://github.com/rubygems/rubygems/issues/120
# rubygems-Patches-28631
Patch1:		rubygems-1.8.6-show-extension-build-process-in-sync.patch
# rubygems-Patches-29049
# https://github.com/rubygems/rubygems/issues/118
Patch3:		rubygems-1.8.5-show-rdoc-process-verbosely.patch
# Fix Gem.all_load_paths (although it is deprecated and will be removed
# on 2011-10-01)
# Fixed in 1.8.22
#Patch6:		rubygems-1.8.5-all-load-paths.patch

# Patches from the works by Vít Ondruch <vondruch@redhat.com>
# Fix the uninstaller, so that it doesn't say that gem doesn't exist
# when it exists outside of the GEM_HOME (already fixed in the upstream)
Patch105:	ruby-1.9.3-rubygems-1.8.11-uninstaller.patch
# Add support for installing binary extensions according to FHS.
# https://github.com/rubygems/rubygems/issues/210
Patch109:	rubygems-1.8.11-binary-extensions.patch
# Make tests work with newest minitest.
Patch110:       rubygems-1.8.24-fix-changes-to-minitest.patch

Requires:	%{?scl_prefix}ruby(abi) = 1.9.1
Requires:	%{?scl_prefix}rubygem(rdoc) >= 3.9.4
Requires:	%{?scl_prefix}rubygem(io-console) >= 0.3
Requires:	ca-certificates

BuildRequires:	%{?scl_prefix}ruby(abi) = 1.9.1
%if %{enable_check}
# For mkmf.rb
BuildRequires:	%{?scl_prefix}ruby-devel
BuildRequires:	%{?scl_prefix}rubygem(minitest)
BuildRequires:	%{?scl_prefix}rubygem(rake)
BuildRequires:	%{?scl_prefix}rubygem(rdoc) >= 3.9.4
BuildRequires:	%{?scl_prefix}rubygem(io-console) >= 0.3
%endif
# Unbundle cert.pem
BuildRequires:	ca-certificates
BuildArch:	noarch
Provides:	%{?scl_prefix}ruby(rubygems) = %{version}-%{release}
Provides:       %{?scl_prefix}gem = %{version}-%{release}

%description
RubyGems is the Ruby standard for publishing and managing third party
libraries.

%package 	devel
Summary:	Macros and development tools for packagin RubyGems
Group:		Development/Libraries
License:	Ruby or MIT
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch:	noarch

%description	devel
Macros and development tools for packagin RubyGems.

%prep
%setup -q -n %{pkg_name}-%{version}
#%%patch0 -p1 -b .noarch
%if 1
%patch1 -p1 -b .insync
%patch3 -p1 -b .rdoc_v
#%%patch6 -p1 -b .load_path
%endif
%patch105 -p1 -b .uninst
%patch109 -p1 -b .bindir
%patch110 -p1

# Some of the library files start with #! which rpmlint doesn't like
# and doesn't make much sense
for f in `find lib -name \*.rb` ; do
  head -1 $f | grep -q '^#!/usr/bin/env ruby' && sed -i -e '1d' $f
done

%build
# Nothing

%install
%{?scl:scl enable %scl - << \EOF}
GEM_HOME=%{buildroot}/%{gem_dir} \
    ruby setup.rb --rdoc --prefix=/ \
        --destdir=%{buildroot}/%{rubygems_dir}/
%{?scl:EOF}

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}/%{rubygems_dir}/bin/gem %{buildroot}/%{_bindir}/gem
rm -rf %{buildroot}/%{rubygems_dir}/bin

mv %{buildroot}/%{rubygems_dir}/lib/* %{buildroot}/%{rubygems_dir}/.
# No longer needed
rmdir %{buildroot}%{rubygems_dir}/lib

# Install custom operating_system.rb.
mkdir -p %{buildroot}%{rubygems_dir}/rubygems/defaults
install -cpm 0644 %{SOURCE100} %{buildroot}%{rubygems_dir}/rubygems/defaults/

# Kill bundled cert.pem
mkdir -p %{buildroot}%{rubygems_dir}/rubygems/ssl_certs/
ln -sf %{?scl:%_root_sysconfdir}%{!?scl:%_sysconfdir}/pki/tls/cert.pem \
        %{buildroot}%{rubygems_dir}/rubygems/ssl_certs/ca-bundle.pem

# Create gem folders.
mkdir -p %{buildroot}%{gem_dir}/{cache,gems,specifications,doc}
mkdir -p %{buildroot}%{gem_extdir}/exts

# Create macros.rubygems file for rubygems-devel
mkdir -p %{buildroot}%{_root_sysconfdir}/rpm

cat >> %{buildroot}%{_root_sysconfdir}/rpm/macros.rubygems%{?scl:.%{scl}} << \EOF
# The RubyGems root folder.
%%gem_dir %{gem_dir}

# Common gem locations and files.
%%gem_instdir %%{gem_dir}/gems/%%{gem_name}-%%{version}
%%gem_extdir %%{_libdir}/gems/exts/%%{gem_name}-%%{version}
%%gem_libdir %%{gem_instdir}/lib
%%gem_cache %%{gem_dir}/cache/%%{gem_name}-%%{version}.gem
%%gem_spec %%{gem_dir}/specifications/%%{gem_name}-%%{version}.gemspec
%%gem_docdir %%{gem_dir}/doc/%%{gem_name}-%%{version}
EOF

%if %{enable_check}
%check
# Create an empty operating_system.rb, so that the system's one doesn't get used,
# otherwise the test suite fails.
mkdir -p lib/rubygems/defaults
touch lib/rubygems/defaults/operating_system.rb

# It is necessary to specify the paths using RUBYOPT to let the test suite pass."
%{?scl:scl enable %scl - << \EOF}
export GEM_PATH=%{gem_dir}
RUBYOPT="-Itest -Ilib" 
RUBYOPT="$RUBYOPT -I%{_libdir}/gems/exts/io-console-0.3/lib/"
# In case that rubygem-json is installed
RUBYOPT="$RUBYOPT -I%{gem_dir}/gems/json-1.6.5/lib -I%{_libdir}/gems/exts/json-1.6.6/ext/json/ext"
export RUBYOPT

sed -i 's|assert_match @installer.dir, %r!/installer/gems/a-2$!|assert_match %r!/installer/gems/a-2$!, @installer.dir|' test/rubygems/test_gem_installer.rb
testrb test
%{?scl:EOF}
%endif

%files
%doc README* 
%doc History.txt
%doc MIT.txt LICENSE.txt
%dir %{gem_dir}
%dir %{gem_dir}/cache
%dir %{gem_dir}/gems
%dir %{gem_dir}/specifications
%doc %{gem_dir}/doc
%{_bindir}/gem

%dir %{rubygems_dir}/
%{rubygems_dir}/rbconfig/
%{rubygems_dir}/rubygems/
%{rubygems_dir}/rubygems.rb
%{rubygems_dir}/ubygems.rb
%{rubygems_dir}/gauntlet_rubygems.rb

%dir %{_exec_prefix}/lib/gems
%dir %{_exec_prefix}/lib64/gems
%dir %{_exec_prefix}/lib/gems/exts
%dir %{_exec_prefix}/lib64/gems/exts

%files	devel
%config(noreplace)  %{_root_sysconfdir}/rpm/macros.rubygems%{?scl:.%{scl}}

%changelog
* Wed Feb 20 2013 Miroslav Suchý <msuchy@redhat.com> 1.8.24-3
- new package built with tito

* Tue Jul 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.8.24-2
- Specfile cleanup.
- Patch tests to work with new Minitest.

* Mon Jun 04 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.8.24-1
- Version 1.8.24

* Tue May 29 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.8.23-10
- Bump the release up not to conflict with rubygems generated from ruby.srpm.

* Tue May 29 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.8.23-7
- Fix the simlink to ca-bundle.pem to point to the core system, not SCL.

* Mon Apr 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.8.23-6
- Rebuilt for scl.

* Sat Apr 21 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.23-5
- 1.8.23
- Use system-wide cert.pem

* Thu Apr 18 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.22-1
- 1.8.22

* Thu Jan 26 2012 Vít Ondruch <vondruch@redhat.com> - 1.8.15-2
- Make test suite green.

* Thu Jan 26 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.15-1
- 1.8.15

* Thu Jan 26 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.11-10
- Incorpolate works by Vít Ondruch <vondruch@redhat.com>
  made for ruby 1.9.x

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 11 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.11-1
- 1.8.11

* Sun Aug 28 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.10-1
- 1.8.10

* Thu Aug 25 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.9-1
- 1.8.9

* Sun Aug 21 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.8-1
- 1.8.8

* Sat Aug  6 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.7-1
- 1.8.7

* Wed Jul 27 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.6-1
- 1.8.6

* Sat Jun 25 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.5-2
- Fix Gem.latest_load_paths (for rubygem-gettext FTBFS)
- Fix Gem.all_load_paths (for rubygem-gettext FTBFS, although it is already
  deprecated from 1.7.0)

* Wed Jun  1 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.5-1
- Try 1.8.5

* Tue May 24 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.7.2-2
- Handle gemspec file with containing "invalid" date format
  generated with psych (ref: bug 706914)

* Sat Apr 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.7.2-1
- Update to 1.7.2

* Sat Mar 12 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2

* Fri Mar  4 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1
- Patch2, 4 upstreamed

* Thu Mar  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Sun Feb 27 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.3-1
- Update to 1.5.3

* Sun Feb 20 2011 Mamoru Tasaka <mtasaka@fedorapeople.org> - 1.5.2-1
- Update to 1.5.2
- Show rdoc process verbosely in verbose mode

* Fri Feb 11 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0-2
- Modify in-sync patch to keep the original behavior (for testsuite)
- Patch to make testsuite succeed, enabling testsuite

* Thu Feb 10 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0-1
- Update to 1.5.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct  8 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.7-2
- Show build process of extension library in sync

* Mon May 17 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.7-1
- Update to 1.3.7, dropping upstreamed patch

* Wed Apr 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.6-1
- Update to 1.3.6
- Show prefix with gem contents by default as shown in --help

* Mon Sep 21 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.5-1
- Update to 1.3.5

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 09 2008 Jeroen van Meeuwen <kanarip@kanarip.com> - 1.3.1-1
- New upstream version

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 1.2.0-2
- Bump release because I forgot to check in newer patch

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 1.2.0-1
- Updated for new setup.rb
- Simplified by removing conditionals that were needed for EL-4;
  there's just no way we can support that with newer rubygems

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.4-2
- fix license tag

* Fri Jul 27 2007 David Lutterkort <dlutter@redhat.com> - 0.9.4-1
- Conditionalize so it builds on RHEL4

* Tue Feb 27 2007 David Lutterkort <dlutter@redhat.com> - 0.9.2-1
- New version
- Add patch0 to fix multilib sensitivity of Gem::dir (bz 227400)

* Thu Jan 18 2007 David Lutterkort <dlutter@redhat.com> - 0.9.1-1
- New version; include LICENSE.txt and GPL.txt
- avoid '..' in gem_dir to work around a bug in gem installer
- add ruby-rdoc to requirements

* Tue Jan  2 2007 David Lutterkort <dlutter@redhat.com> - 0.9.0-2
- Fix gem_dir to be arch independent
- Mention dual licensing in License field

* Fri Dec 22 2006 David Lutterkort <dlutter@redhat.com> - 0.9.0-1
- Updated to 0.9.0
- Changed to agree with Fedora Extras guidelines

* Mon Jan  9 2006 David Lutterkort <dlutter@redhat.com> - 0.8.11-1
- Updated for 0.8.11

* Sun Oct 10 2004 Omar Kilani <omar@tinysofa.org> 0.8.1-1ts
- First version of the package
