%{?scl:%scl_package puppet}
%{!?scl:%global pkg_name %{name}}

%global ruby_archdir   %{ruby_vendorarchdir}
%global ruby_version    1.9.1

Name:           %{?scl_prefix}ruby-shadow
Version:        1.4.1
Release:        22%{?dist}
Summary:        Ruby bindings for shadow password access
Group:          System Environment/Libraries
License:        Public Domain
URL:            http://ttsky.net/
Source0:        http://ttsky.net/src/ruby-shadow-%{version}.tar.gz
Patch0:         0001-Add-ruby-1.9-support.patch
Patch1:         ruby-shadow-1.4.1-cflags.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  %{?scl_prefix}ruby-devel
# Work around the lack of ruby in the default mock buildroot
%if "%{ruby_version}"
Requires:       %{?scl_prefix}ruby(abi) = %{ruby_version}
%endif
Provides:       %{?scl_prefix}ruby(shadow) = %{version}-%{release}

%description
Ruby bindings for shadow password access

%prep
%setup -q -n shadow-%{version}
%patch0 -p1
%patch1 -p1
%{_root_bindir}/iconv -f EUCJP -t utf8 -o README.ja README.euc

%build
%{?scl:scl enable %{scl} - << \EOF}
ruby extconf.rb --with-cflags="$RPM_OPT_FLAGS"
%{?scl:EOF}
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} sitearchdir=%{buildroot}%{ruby_archdir} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc HISTORY README README.ja
%{ruby_archdir}/shadow.so

%changelog
* Fri Mar 22 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.1-22
- fix scl macro (msuchy@redhat.com)

* Fri Mar 22 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.1-21
- run iconv from _root_bindir (msuchy@redhat.com)

* Fri Mar 22 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.1-20
- new package built with tito

* Fri Mar 22 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.1-19
- initial package

* Fri Mar 22 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.1-18
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 20 2012 Todd Zullinger <tmz@pobox.com> - 1.4.1-16
- Add ruby-1.9 support

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 10 2008 Kostas Georgiou <k.georgiou@imperial.ac.uk> - 1.4.1-11
- Rebuild for GCC 4.3

* Wed Aug 29 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> - 1.4.1-10
- Increase version to fix wrong tag

* Wed Aug 29 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> - 1.4.1-9
- Clean up of the "sh: ruby: command not found" added by the automated rebuild
  in the spec file

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.4.1-8
- Rebuild for selinux ppc32 issue.

* Wed Jul 18 2007 David Lutterkort <dlutter@redhat.com> - 1.4.1-7
- Remove dependency on ruby{,io}.h from depend - makes builds on RHEL4 fail, 
  and doesn't provide anything for proper rpm builds

* Fri May 25 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-6
Removed _smp_mflags from install since it was causing problems

* Fri May 18 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-5
Removed the ruby abi macro since it doesn't work in mock

* Tue May 15 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-4
Cleaner ruby abi macro

* Tue May 15 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-3
Fixed struct defines (0 != NULL in C) 
Calculate ruby abi at runtime instead of a hard coded version

* Tue May 15 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-2
Converted README.euc to utf8 README.ja
Patched extconf.rb to use provided CFLAGS

* Mon May 14 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-1
Initial rpm release
