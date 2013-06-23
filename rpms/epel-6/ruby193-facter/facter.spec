%{?scl:%scl_package facter}
%{!?scl:%global pkg_name %{name}}

# F-17 and above have ruby-1.9.x, and place libs in a different location
# The checks also fail on older releases, due to an older mocha gem, it appears
%if 0%{?fedora} >= 17
%global enable_check    1
%global facter_libdir   %(ruby -rrbconfig -e 'puts RbConfig::CONFIG["vendorlibdir"]')
%else
%global enable_check    0
%global facter_libdir   %(ruby -rrbconfig -e 'puts RbConfig::CONFIG["sitelibdir"]')
%endif
%global facter_libdir %{ruby_vendorlibdir}
#disable for Katello
%global enable_check 0

%global ruby_version    %(ruby -rrbconfig -e 'puts RbConfig::CONFIG["ruby_version"]')

# There is nothing useful in debuginfo, facter is only an arch package to
# allow arch-dependent requires.
%global debug_package %{nil}

Name:           %{?scl_prefix}facter
Version:        1.6.18
Release:        4%{?dist}
Summary:        Command and ruby library for gathering system information

Group:          System Environment/Base
License:        ASL 2.0
URL:            http://www.puppetlabs.com/puppet/related-projects/%{pkg_name}/
Source0:        http://downloads.puppetlabs.com/%{pkg_name}/%{pkg_name}-%{version}.tar.gz
Source1:        http://downloads.puppetlabs.com/%{pkg_name}/%{pkg_name}-%{version}.tar.gz.asc
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}ruby >= 1.8.1
BuildRequires:  %{?scl_prefix}ruby-devel
%if %{enable_check}
BuildRequires:  net-tools
BuildRequires:  %{?scl_prefix}rubygem(mocha)
BuildRequires:  %{?scl_prefix}rubygem(rspec-core)
BuildRequires:  %{?scl_prefix}rubygem(rspec)
%endif

# dmidecode and pciutils are not available on all arches
%ifarch %ix86 x86_64 ia64
Requires:       dmidecode
Requires:       pciutils
Requires:       virt-what
%endif
Requires:       net-tools
# Work around the lack of ruby in the default mock buildroot
%if "%{ruby_version}"
%if 0%{?fedora} >= 19
Requires:       %{?scl_prefix}ruby(release)
%else
Requires:       %{?scl_prefix}ruby(abi) = %{ruby_version}
%endif
%endif
Requires:       which

%description
Facter is a lightweight program that gathers basic node information about the
hardware and operating system. Facter is especially useful for retrieving
things like operating system names, hardware characteristics, IP addresses, MAC
addresses, and SSH keys.

Facter is extensible and allows gathering of node information that may be
custom or site specific. It is easy to extend by including your own custom
facts. Facter can also be used to create conditional expressions in Puppet that
key off the values returned by facts.

%prep
%setup -n %{pkg_name}-%{version} -q


%build
# Nothing to build


%install
rm -rf %{buildroot}
%{?scl:scl enable %{scl} "}
ruby install.rb --destdir=%{buildroot} --quick --no-rdoc --sitelibdir=%{facter_libdir}
%{?scl:"}

#%if ! (0%{?fedora} || 0%{?rhel} >= 7)
## Install man page, rubygem-rdoc is not available on older EL releases)
#install -D -pv -m 644 man/man8/%{pkg_name}.8 %{buildroot}/%{_mandir}/man8/%{pkg_name}.8
#%endif

%postun
# Work around issues where puppet fails to run after a facter update
# https://bugzilla.redhat.com/806370
# http://projects.puppetlabs.com/issues/12879
if [ "$1" -ge 1 ]; then
  /sbin/service puppet condrestart >/dev/null 2>&1 || :
fi


%clean
rm -rf %{buildroot}


%check
%if %{enable_check}
%{?scl:scl enable %{scl} "}
rspec spec
%{?scl:"}
%endif


%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_bindir}/%{pkg_name}
%{facter_libdir}/%{pkg_name}*
%{_mandir}/man8/%{pkg_name}*

%changelog
* Thu Mar 21 2013 Miroslav Suchý <msuchy@redhat.com> 1.6.18-4
- put ruby libs into ruby_vendorlibdir (msuchy@redhat.com)

* Thu Mar 21 2013 Miroslav Suchý <msuchy@redhat.com> 1.6.18-3
- remove scl deps on non-ruby packages (msuchy@redhat.com)

* Thu Mar 21 2013 Miroslav Suchý <msuchy@redhat.com> 1.6.18-2
- new package built with tito

* Mon Mar 18 2013 Todd Zullinger <tmz@pobox.com> - 1.6.18-1
- Update to 1.6.18
- Restart puppet in %%postun (#806370)
- Require virt-what for improved KVM detection (#905592)
- Ensure man page is installed on EL < 7

* Tue Mar 12 2013 Vít Ondruch <vondruch@redhat.com> - 1.6.17-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Mon Feb 25 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.6.17-1
- New upstream version, fixes rhbz #892734

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 04 2012 Michael Stahnke <stahnma@puppetlabs.com> - 1.6.16-1
- Update to 1.6.16

* Wed Nov 28 2012 Michael Stahnke <stahnma@puppetlabs.com> -  1.6.15-1
- Rebase to 1.6.15
- Put asc file back as Source1

* Fri Nov 09 2012 Michael Stahnke <stahnma@puppetlabs.com> - 1.6.13-2
- Add patch for ec2 fix
- Rebase to 1.6.14 via bz 871211

* Mon Oct 29 2012 Michael Stahnke <stahnma@puppetlabs.com> - 1.6.13-1
- Rebase to 1.6.13

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 05 2012 Todd Zullinger <tmz@pobox.com> - 1.6.6-1
- Update to 1.6.6

* Sun Feb 19 2012 Todd Zullinger <tmz@pobox.com> - 1.6.5-5
- Disable useless debuginfo generation (#795106, thanks to Ville Skyttä)
- Update summary and description
- Remove INSTALL from %%doc

* Wed Feb 15 2012 Todd Zullinger <tmz@pobox.com> - 1.6.5-4
- Only run rspec checks on Fedora >= 17

* Mon Feb 13 2012 Todd Zullinger <tmz@pobox.com> - 1.6.5-3
- Make spec file work for EPEL and Fedora
- Drop BuildArch: noarch and make dmidecode/pciutils deps arch-specific
- Make ec2 facts work on CentOS again (#790849, thanks to Jeremy Katz)
- Preserve timestamps when installing files

* Thu Feb 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.6.5-2
- Rebuilt for Ruby 1.9.3.

* Thu Jan 26 2012 Todd Zullinger <tmz@pobox.com> - 1.6.5-1
- Update to 1.6.5
- Require net-tools and pciutils, thanks to Dominic Cleal (#783749)

* Thu Jan 05 2012 Todd Zullinger <tmz@pobox.com> - 1.6.4-1
- Update to 1.6.4
- Require dmidecode (upstream #11041)

* Sat Oct 15 2011 Todd Zullinger <tmz@pobox.com> - 1.6.2-1
- Update to 1.6.2
- Update source URL

* Thu Sep 29 2011 Todd Zullinger <tmz@pobox.com> - 1.6.1-1
- Update to 1.6.1
- Minor spec file reformatting

* Wed Jul 27 2011 Todd Zullinger <tmz@pobox.com> - 1.6.0-2
- Update license tag, GPLv2+ -> ASL 2.0

* Thu Jul 14 2011 Todd Zullinger <tmz@pobox.com> - 1.6.0-1
- Update to 1.6.0

* Thu May 26 2011 Todd Zullinger <tmz@pobox.com> - 1.5.9-1
- Update to 1.5.9
- Improve Scientific Linux support, courtesy of Orion Poplawski (upstream #7682)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 28 2010 Todd Zullinger <tmz@pobox.com> - 1.5.8-1
- Update to 1.5.8

* Fri Sep 25 2009 Todd Zullinger <tmz@pobox.com> - 1.5.7-1
- Update to 1.5.7
- Update #508037 patch from upstream ticket

* Wed Aug 12 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.5.5-3
- Fix #508037 or upstream #2355

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Todd Zullinger <tmz@pobox.com> - 1.5.5-1
- Update to 1.5.5
- Drop upstreamed libperms patch

* Sat Feb 28 2009 Todd Zullinger <tmz@pobox.com> - 1.5.4-1
- New version
- Use upstream install script

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 09 2008 Todd Zullinger <tmz@pobox.com> - 1.5.2-1
- New version
- Simplify spec file checking for Fedora and RHEL versions

* Mon Sep  8 2008 David Lutterkort <dlutter@redhat.com> - 1.5.1-1
- New version

* Thu Jul 17 2008 David Lutterkort <dlutter@redhat.com> - 1.5.0-3
- Change 'mkdir' in install to 'mkdir -p'

* Thu Jul 17 2008 David Lutterkort <dlutter@redhat.com> - 1.5.0-2
- Remove files that were listed twice in files section

* Mon May 19 2008 James Turnbull <james@lovedthanlosty.net> - 1.5.0-1
- New version
- Added util and plist files

* Mon Sep 24 2007 David Lutterkort <dlutter@redhat.com> - 1.3.8-1
- Update license tag
- Copy all of lib/ into ruby_sitelibdir

* Thu Mar 29 2007 David Lutterkort <dlutter@redhat.com> - 1.3.7-1
- New version

* Fri Jan 19 2007 David Lutterkort <dlutter@redhat.com> - 1.3.6-1
- New version

* Thu Jan 18 2007 David Lutterkort <dlutter@redhat.com> - 1.3.5-3
- require which; facter is very unhappy without it

* Mon Nov 20 2006 David Lutterkort <dlutter@redhat.com> - 1.3.5-2
- Make require ruby(abi) and buildarch: noarch conditional for fedora 5 or
  later to allow building on older fedora releases

* Tue Oct 10 2006 David Lutterkort <dlutter@redhat.com> - 1.3.5-1
- New version

* Tue Sep 26 2006 David Lutterkort <dlutter@redhat.com> - 1.3.4-1
- New version

* Wed Sep 13 2006 David Lutterkort <dlutter@redhat.com> - 1.3.3-2
- Rebuilt for FC6

* Wed Jun 28 2006 David Lutterkort <dlutter@redhat.com> - 1.3.3-1
- Rebuilt

* Fri Jun 19 2006 Luke Kanies <luke@madstop.com> - 1.3.0-1
- Fixed spec file to work again with the extra memory and processor files.
- Require ruby(abi). Build as noarch

* Fri Jun 9 2006 Luke Kanies <luke@madstop.com> - 1.3.0-1
- Added memory.rb and processor.rb

* Mon Apr 17 2006 David Lutterkort <dlutter@redhat.com> - 1.1.4-4
- Rebuilt with changed upstream tarball

* Tue Mar 21 2006 David Lutterkort <dlutter@redhat.com> - 1.1.4-3
- Do not rely on install.rb, it will be deleted upstream

* Mon Mar 13 2006 David Lutterkort <dlutter@redhat.com> - 1.1.4-2
- Commented out noarch; requires fix for bz184199

* Mon Mar  6 2006 David Lutterkort <dlutter@redhat.com> - 1.1.4-1
- Removed unused macros

* Mon Feb  6 2006 David Lutterkort <dlutter@redhat.com> - 1.1.1-2
- Fix BuildRoot. Add dist to release tag

* Wed Jan 11 2006 David Lutterkort <dlutter@redhat.com> - 1.1.1-1
- Initial build.
