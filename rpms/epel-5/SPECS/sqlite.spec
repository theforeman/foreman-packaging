# bcond default logic is nicely backwards...
%bcond_without tcl
%bcond_with static
%bcond_without check

# upstream doesn't provide separate -docs sources for all minor releases
%define basever 3.6.20
%define docver %(echo %{basever}|sed -e "s/\\./_/g")

Summary: Library that implements an embeddable SQL database engine
Name: sqlite
Version: %{basever}
Release: 1%{?dist}
License: Public Domain
Group: Applications/Databases
URL: http://www.sqlite.org/
Source0: http://www.sqlite.org/sqlite-%{version}.tar.gz
Source1: http://www.sqlite.org/sqlite_docs_%{docver}.zip
# Fix build with --enable-load-extension, upstream ticket #3137
Patch1: sqlite-3.6.12-libdl.patch
# Avoid insecure sprintf(), use a system path for lempar.c, patch from Debian
Patch2: sqlite-3.6.6.2-lemon-snprintf.patch
BuildRequires: ncurses-devel readline-devel glibc-devel
# libdl patch needs
BuildRequires: autoconf
%if %{with tcl}
BuildRequires: /usr/bin/tclsh
BuildRequires: tcl-devel
%{!?tcl_version: %global tcl_version 8.5}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%endif
BuildRoot: %{_tmppath}/%{name}-root

%description
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host

%package devel
Summary: Development tools for the sqlite3 embeddable SQL database engine
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files and development documentation 
for %{name}. If you like to develop programs using %{name}, you will need 
to install %{name}-devel.

%package doc
Summary: Documentation for sqlite
Group: Documentation

%description doc
This package contains most of the static HTML files that comprise the
www.sqlite.org website, including all of the SQL Syntax and the 
C/C++ interface specs and other miscellaneous documentation.

%package -n lemon
Summary: A parser generator
Group: Development/Tools

%description -n lemon
Lemon is an LALR(1) parser generator for C or C++. It does the same
job as bison and yacc. But lemon is not another bison or yacc
clone. It uses a different grammar syntax which is designed to reduce
the number of coding errors. Lemon also uses a more sophisticated
parsing engine that is faster than yacc and bison and which is both
reentrant and thread-safe. Furthermore, Lemon implements features
that can be used to eliminate resource leaks, making is suitable for
use in long-running programs such as graphical user interfaces or
embedded controllers.

%if %{with tcl}
%package tcl
Summary: Tcl module for the sqlite3 embeddable SQL database engine
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: tcl(abi) = %{tcl_version}

%description tcl
This package contains the tcl modules for %{name}.
%endif

%prep
%setup -q -a1
%patch1 -p1 -b .libdl
%patch2 -p1 -b .lemon-sprintf

%build
autoconf
export CFLAGS="$RPM_OPT_FLAGS -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_DISABLE_DIRSYNC=1 -DSQLITE_ENABLE_FTS3=3 -DSQLITE_ENABLE_RTREE=1 -Wall -fno-strict-aliasing"
%configure %{!?with_tcl:--disable-tcl} \
           --enable-threadsafe \
           --enable-threads-override-locks \
           --enable-load-extension \
           %{?with_tcl:TCLLIBDIR=%{tcl_sitearch}/sqlite3}

# rpath removal
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=${RPM_BUILD_ROOT} install

install -D -m0644 sqlite3.1 $RPM_BUILD_ROOT/%{_mandir}/man1/sqlite3.1
install -D -m0755 lemon $RPM_BUILD_ROOT/%{_bindir}/lemon
install -D -m0644 tool/lempar.c $RPM_BUILD_ROOT/%{_datadir}/lemon/lempar.c

%if %{with tcl}
# fix up permissions to enable dep extraction
chmod 0755 ${RPM_BUILD_ROOT}/%{tcl_sitearch}/sqlite3/*.so
%endif

%if ! %{with static}
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.{la,a}
%endif

%if %{with check}
%check
# let this fail for now:
# - five nan-test broken on PPC (upstream ticket #3404)
# - bunch of rtree-tests failing on PPC atm
make test ||:
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc README
%{_bindir}/sqlite3
%{_libdir}/*.so.*
%{_mandir}/man?/*

%files devel
%defattr(-, root, root)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%if %{with static}
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%endif

%files doc
%defattr(-, root, root)
%doc %{name}-%{docver}-docs/*

%files -n lemon
%defattr(-, root, root)
%{_bindir}/lemon
%{_datadir}/lemon

%if %{with tcl}
%files tcl
%defattr(-, root, root)
%{tcl_sitearch}/sqlite3
%endif

%changelog
* Tue Nov 17 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.20-1
- update to 3.6.20 (http://www.sqlite.org/releaselog/3_6_20.html)

* Tue Oct 06 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.18-1
- update to 3.6.18 (http://www.sqlite.org/releaselog/3_6_18.html)
- drop no longer needed test-disabler patches

* Fri Aug 21 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.17-1
- update to 3.6.17 (http://www.sqlite.org/releaselog/3_6_17.html)
- disable to failing tests until upstream fixes

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.14.2-1
- update to 3.6.14.2 (#505229)

* Mon May 18 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.14-2
- disable rpath
- add -doc subpackage instead of patching out reference to it

* Thu May 14 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.14-1
- update to 3.6.14 (http://www.sqlite.org/releaselog/3_6_14.html)
- merge-review cosmetics (#226429)
  - drop ancient sqlite3 obsoletes
  - fix tab vs space whitespace issues
  - remove commas from summaries
- fixup io-test fsync expectations wrt SQLITE_DISABLE_DIRSYNC

* Wed Apr 15 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.13-1
- update to 3.6.13

* Thu Apr 09 2009 Dennis Gilmore <dennis@ausil.us> - 3.6.12-3
- apply upstream patch for memory alignment issue (#494906)

* Tue Apr 07 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.12-2
- disable strict aliasing to work around brokenness on 3.6.12 (#494266)
- run test-suite on build but let it fail for now

* Fri Apr 03 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.12-1
- update to 3.6.12 (#492662)
- remove reference to non-existent sqlite-doc from manual (#488883)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.10-3
- enable RTREE and FTS3 extensions (#481417)

* Thu Jan 22 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.10-2
- upstream fix yum breakage caused by new keywords (#481189)

* Thu Jan 22 2009 Panu Matilainen <pmatilai@redhat.com> - 3.6.10-1
- update to 3.6.10

* Wed Dec 31 2008 Panu Matilainen <pmatilai@redhat.com> - 3.6.7-1
- update to 3.6.7
- avoid lemon ending up in main sqlite package too

* Fri Dec 05 2008 Panu Matilainen <pmatilai@redhat.com> - 3.6.6.2-4
- add lemon subpackage

* Thu Dec  4 2008 Matthias Clasen <mclasen@redhat.com> - 3.6.6.2-3
- Rebuild for pkg-config provides 

* Tue Dec 02 2008 Panu Matilainen <pmatilai@redhat.com> - 3.6.6.2-2
- require tcl(abi) in sqlite-tcl subpackage (#474034)
- move tcl extensions to arch-specific location
- enable dependency extraction on the tcl dso
- require pkgconfig in sqlite-devel

* Sat Nov 29 2008 Panu Matilainen <pmatilai@redhat.com> - 3.6.6.2-1
- update to 3.6.6.2

* Sat Nov 08 2008 Panu Matilainen <pmatilai@redhat.com> - 3.6.4-1
- update to 3.6.4
- drop patches already upstream

* Mon Sep 22 2008 Panu Matilainen <pmatilai@redhat.com> - 3.5.9-2
- Remove references to temporary registers from cache on release (#463061)
- Enable loading of external extensions (#457433)

* Tue Jun 17 2008 Stepan Kasal <skasal@redhat.com> - 3.5.9-1
- update to 3.5.9

* Wed Apr 23 2008 Panu Matilainen <pmatilai@redhat.com> - 3.5.8-1
- update to 3.5.8
- provide full version in pkg-config (#443692)

* Mon Mar 31 2008 Panu Matilainen <pmatilai@redhat.com> - 3.5.6-2
- remove reference to static libs from -devel description (#439376)

* Tue Feb 12 2008 Panu Matilainen <pmatilai@redhat.com> - 3.5.6-1
- update to 3.5.6
- also fixes #432447

* Fri Jan 25 2008 Panu Matilainen <pmatilai@redhat.com> - 3.5.4-3
- enable column metadata API (#430258)

* Tue Jan 08 2008 Panu Matilainen <pmatilai@redhat.com> - 3.5.4-2
- avoid packaging CVS directory as documentation (#427755)

* Fri Dec 21 2007 Panu Matilainen <pmatilai@redhat.com> - 3.5.4-1
- Update to 3.5.4 (#413801)

* Fri Sep 28 2007 Panu Matilainen <pmatilai@redhat.com> - 3.4.2-3
- Add another build conditional for enabling %%check

* Fri Sep 28 2007 Panu Matilainen <pmatilai@redhat.com> - 3.4.2-2
- Use bconds for the spec build conditionals
- Enable -tcl subpackage again (#309041)

* Wed Aug 15 2007 Paul Nasrat <pnasrat@redhat.com> - 3.4.2-1
- Update to 3.4.2

* Sat Jul 21 2007 Paul Nasrat <pnasrat@redhat.com> - 3.4.1-1
- Update to 3.4.1

* Sun Jun 24 2007 Paul Nasrat <pnsarat@redhat.com> - 3.4.0-2
- Disable load for now (#245486)

* Tue Jun 19 2007 Paul Nasrat <pnasrat@redhat.com> - 3.4.0-1
- Update to 3.4.0

* Fri Jun 01 2007 Paul Nasrat <pnasrat@redhat.com> - 3.3.17-2
- Enable load 
- Build fts1 and fts2
- Don't sync on dirs (#237427)

* Tue May 29 2007 Paul Nasrat <pnasrat@redhat.com> - 3.3.17-1
- Update to 3.3.17

* Mon Mar 19 2007 Paul Nasrat <pnasrat@redhat.com> - 3.3.13-1
- Update to 3.3.13

* Fri Aug 11 2006 Paul Nasrat <pnasrat@redhat.com> - 3.3.6-2
- Fix conditional typo (patch from Gareth Armstrong)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.3.6-1.1
- rebuild

* Mon Jun 26 2006 Paul Nasrat <pnasrat@redhat.com> - 3.3.6-1
- Update to 3.3.6
- Fix typo  (#189647)
- Enable threading fixes (#181298)
- Conditionalize static library

* Mon Apr 17 2006 Paul Nasrat <pnasrat@redhat.com> - 3.3.5-1
- Update to 3.3.5

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.3.3-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.3.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Christopher Aillon <caillon@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Tue Jan 31 2006 Christopher Aillon <caillon@redhat.com> - 3.3.2-1
- Update to 3.3.2

* Tue Jan 24 2006 Paul Nasrat <pnasrat@redhat.com> - 3.2.8-1
- Add --enable-threadsafe (Nicholas Miell)
- Update to 3.2.8

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Oct  4 2005 Jeremy Katz <katzj@redhat.com> - 3.2.7-2
- no more static file or libtool archive (#169874) 

* Wed Sep 28 2005 Florian La Roche <laroche@redhat.com>
- Upgrade to 3.2.7 release.

* Thu Sep 22 2005 Florian La Roche <laroche@redhat.com>
- Upgrade to 3.2.6 release.

* Sun Sep 11 2005 Florian La Roche <laroche@redhat.com>
- Upgrade to 3.2.5 release.

* Fri Jul  8 2005 Roland McGrath <roland@redhat.com> - 3.2.2-1
- Upgrade to 3.2.2 release.

* Sat Apr  9 2005 Warren Togami <wtogami@redhat.com> - 3.1.2-3
- fix buildreqs (#154298)

* Mon Apr  4 2005 Jeremy Katz <katzj@redhat.com> - 3.1.2-2
- disable tcl subpackage

* Wed Mar  9 2005 Jeff Johnson <jbj@redhat.com> 3.1.2-1
- rename to "sqlite" from "sqlite3" (#149719, #150012).

* Wed Feb 16 2005 Jeff Johnson <jbj@jbj.org> 3.1.2-1
- upgrade to 3.1.2.
- add sqlite3-tcl sub-package.

* Sat Feb  5 2005 Jeff Johnson <jbj@jbj.org> 3.0.8-3
- repackage for fc4.

* Mon Jan 17 2005 R P Herrold <info@owlriver.com> 3.0.8-2orc
- fix a man page nameing conflict when co-installed with sqlite-2, as
  is permissible
