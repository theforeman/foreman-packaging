%global	rubyxver	1.8
%global	rubyver	1.8.7
%global	_patchlevel	357

%global	dotpatchlevel	%{?_patchlevel:.%{_patchlevel}}
%global	patchlevel	%{?_patchlevel:-p%{_patchlevel}}
%global	arcver		%{rubyver}%{?patchlevel}

%{!?vendorlibbase:	%global vendorlibbase	%{_prefix}/lib/ruby}
%{!?vendorarchbase:	%global vendorarchbase	%{_libdir}/ruby}
%{!?sitelibbase:	%global sitelibbase	%{vendorlibbase}/site_ruby}
%{!?sitearchbase:	%global sitearchbase	%{vendorarchbase}/site_ruby}

%global	_normalized_cpu	%(echo %{_target_cpu} | sed 's/^ppc/powerpc/;s/i.86/i386/;s/sparcv./sparc/')

Name:		ruby
Version:	%{rubyver}%{?dotpatchlevel}
Release:	1%{?dist}
# Please check if ruby upstream changes this to "Ruby or GPLv2+"
License:	Ruby or GPLv2
URL:		http://www.ruby-lang.org/

%if 0%{?fedora} >= 13
BuildRequires:	compat-readline5-devel
%else
BuildRequires: 	readline-devel
%endif

BuildRequires:	db4-devel
BuildRequires:	gdbm-devel
#BuildRequires:	libX11-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel

BuildRequires:	autoconf 

BuildRequires:	bison
BuildRequires:	byacc

# Official ruby source release tarball
Source0:	ftp://ftp.ruby-lang.org/pub/%{name}/%{rubyxver}/%{name}-%{arcver}.tar.bz2

# Patches 23, 29, and 33 brought over from ruby 1.8.6
#  (updated to apply against 1.8.7 source)
# If building against a 64bit arch, use 64bit libdir
Patch23:	ruby-1.8.7-p330-multilib.patch
# Mark all i.86 arch's (eg i586, i686, etc) as i386
Patch29:	ruby-1.8.7-always-use-i386.patch
# Use shared libs as opposed to static for mkmf
# See bug 428384
Patch33:	ruby-1.8.7-p249-mkmf-use-shared.patch

# Lower autoconf requirements (fixing RHEL5 builds)
Patch34:	autoconf-2.59.patch
# Change ruby load path to conform to Fedora/ruby
# library placement (various 1.8.6 patches consolidated into this)
Patch100:	ruby-1.8.7-lib-paths.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Summary:	An interpreter of object-oriented scripting language
Group:		Development/Languages
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

# emacs-23.2.x itself now provides the ruby mode
# And no Provides here
Obsoletes:	%{name}-mode < 1.8.7
# remove old documentation
# And no Provides here
Obsoletes:	%{name}-docs < 1.8.7

#
# Remove TCL/TK
Obsoletes: ruby-tcltk

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.


%package	libs
Summary:	Libraries necessary to run Ruby
Group:		Development/Libraries
# ext/bigdecimal/bigdecimal.{c,h} are under (GPL+ or Artistic) which
# are used for bigdecimal.so
License:	(Ruby or GPLv2) and (GPL+ or Artistic)
Provides:	ruby(abi) = %{rubyxver}
Provides:	libruby = %{version}-%{release}
Obsoletes:	libruby < %{version}-%{release}

%description libs
This package includes the libruby, necessary to run Ruby.


%package	devel
Summary:	A Ruby development environment
Group:		Development/Languages
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description	devel
Header files and libraries for building a extension library for the
Ruby or an application embedded Ruby.

%package	static
Summary:	Static libraries for Ruby development environment
Group:		Development/Languages
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description	static
Static libraries for for building a extension library for the
Ruby or an application embedded Ruby.

%package	irb
Summary:	The Interactive Ruby
Group:		Development/Languages
# No isa specific
Requires:	%{name} = %{version}-%{release}
Provides:	irb = %{version}-%{release}
Obsoletes:	irb < %{version}-%{release}
%if 0%{?fedora} >= 10 || 0%{?rhel} >= 6
BuildArch:	noarch
%endif

%description irb
The irb is acronym for Interactive Ruby.  It evaluates ruby expression
from the terminal.


%package	rdoc
Summary:	A tool to generate documentation from Ruby source files
Group:		Development/Languages
# generators/template/html/html.rb is under CC-BY
License:	(GPLv2 or Ruby) and CC-BY
# No isa specific
Requires:	%{name}-irb = %{version}-%{release}
Provides:	rdoc = %{version}-%{release}
Obsoletes:	rdoc < %{version}-%{release}
%if 0%{?fedora} >= 10 || 0%{?rhel} >= 6
BuildArch:	noarch
%endif

%description rdoc
The rdoc is a tool to generate the documentation from Ruby source files.
It supports some output formats, like HTML, Ruby interactive reference (ri),
XML and Windows Help file (chm).


%package	ri
Summary:	Ruby interactive reference
Group:		Documentation
## ruby-irb requires ruby, which ruby-rdoc requires
#Requires: %%{name} = %%{version}-%%{release}
# No isa specific
Requires:	%{name}-rdoc = %{version}-%{release}
Provides:	ri = %{version}-%{release}
Obsoletes:	ri < %{version}-%{release}
# FIXME: Make ruby-ri really arch independent
# BuildArch:	noarch # Currently commented out

%description ri
ri is a command line tool that displays descriptions of built-in
Ruby methods, classes and modules. For methods, it shows you the calling
sequence and a description. For classes and modules, it shows a synopsis
along with a list of the methods the class or module implements.

%prep
%setup -q -c 
pushd %{name}-%{arcver}
%patch23 -p1
%patch29 -p1
%patch33 -p1
%patch34 -p1
%patch100 -p1

popd

%build
pushd %{name}-%{arcver}
for i in config.sub config.guess; do
	test -f %{_datadir}/libtool/$i && cp -p %{_datadir}/libtool/$i .
done
autoconf

rb_cv_func_strtod=no
export rb_cv_func_strtod

# bug 489990
CFLAGS="-fno-strict-aliasing"
#CFLAGS="%{optflags} -D__LINUX__ -D_GNU_SOURCE -D_LARGEFILE64_SOURCE"
export CFLAGS

%configure \
	--disable-rpath \
	--enable-shared \
	--without-X11 \
	--disable-pthread \
%if 0%{?fedora} >= 13
	--with-readline-include=%{_includedir}/readline5 \
	--with-readline-lib=%{_libdir}/readline5 \
%endif
	--with-sitedir='%{sitelibbase}' \
	--with-sitearchdir='%{sitearchbase}' \
	--with-vendordir='%{vendorlibbase}' \
	--with-vendorarchdir='%{vendorarchbase}'

# For example ext/socket/extconf.rb uses try_run (for getaddrinfo test),
# which executes conftest and setting LD_LIBRARY_PATH for libruby.so is
# needed.
export LD_LIBRARY_PATH=$(pwd)

make RUBY_INSTALL_NAME=ruby \
	COPY="cp -p" \
	%{?_smp_mflags}
%ifarch ia64
# Miscompilation? Buggy code?
rm -f parse.o
make OPT=-O0 RUBY_INSTALL_NAME=ruby \
	%{?_smp_mflags}
%endif

# Avoid multilib conflict on -libs (bug 649174)
# Maybe dlconfig.rb is unneeded anyway, however for now moving
# dlconfig.rb and add wrapper (need checking)
CONFIGARCH=$(./miniruby -I. -rrbconfig -e "puts Config::CONFIG['arch']")
[ -z "$CONFIGARCH" ] && exit 1
pushd ext/dl
mkdir $CONFIGARCH
mv dlconfig.rb $CONFIGARCH/
cat > dlconfig.rb <<EOF
require 'rbconfig'
dlconfig_path=File.join(File.dirname(__FILE__), Config::CONFIG['arch'], 'dlconfig')
require dlconfig_path
EOF
popd


# Generate ri doc
rm -rf .ext/rdoc
rm -rf ./RI_TMPDIR
mkdir ./RI_TMPDIR
make \
	DESTDIR=$(pwd)/RI_TMPDIR \
	install-doc

popd

%check
pushd %{name}-%{arcver}
%ifarch ppc64
make test || true
%else
make test
%endif
popd

%install
# install documenation in tmp directory to be
# picked up by %%doc macros in %%files sections
rm -rf tmp-ruby-docs
mkdir tmp-ruby-docs
pushd tmp-ruby-docs

mkdir \
	ruby ruby-libs irb

# First gather all samples
cp -a  ../%{name}-%{arcver}/sample/ ruby
cp -a \
	../%{name}-%{arcver}/lib/README* ../%{name}-%{arcver}/doc/ \
	ruby-libs
# Use tar to keep directory hierarchy
cd ruby-libs
(
	cd ../../%{name}-%{arcver} ; \
	find ext \
	-mindepth 1 \
	\( -path '*/sample/*' -o -path '*/demo/*' \) -o \
	\( -name '*.rb' -not -path '*/lib/*' -not -name extconf.rb \) -o \
	\( -name 'README*' -o -name '*.txt*' -o -name 'MANUAL*' \) \
	\
	| xargs tar cf -
) \
	| tar xf -
cd ..

# make sure that all doc files are the world-readable 
find -type f | xargs chmod 0644

# Fix shebang
grep -rl '#![ \t]*%{_prefix}/local/bin' . | \
	xargs sed -i -e '1s|\(#![ \t]*\)%{_prefix}/local/bin|\1%{_bindir}|'
grep -rl '#![ \t]*\./ruby' . | \
	xargs sed -i -e '1s|\(#![ \t]*\)\./ruby|%{_bindir}/ruby|'

# Fix encoding
# Suppress message
set +x
find . -type f | while read f ; do
	file $f | grep -q 'text' || continue
	iconv -f UTF-8 -t UTF-8 $f &> /dev/null && continue
	for encoding in \
		EUC-JP ISO-8859-1
	do
		iconv -f $encoding -t UTF-8 $f -o $f.tmp 2>/dev/null && \
			{ touch -r $f $f.tmp ; mv $f.tmp $f ; \
				echo -e "$f\t: converted from $encoding -t UTF-8" ; continue 2; } || \
			rm -f $f.tmp
	done
done
# Enable message
set -x

# irb
mv ruby-libs/doc/irb/* irb
rm -rf ruby-libs/doc/irb

# done w/ docs
popd

# installing binaries ...
make \
	-C $RPM_BUILD_DIR/%{name}-%{version}/%{name}-%{arcver} \
	DESTDIR=$RPM_BUILD_ROOT \
	install

# install ri doc
cp -a ./%{name}-%{arcver}/RI_TMPDIR/* $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{sitelibbase}/%{rubyxver}
mkdir -p $RPM_BUILD_ROOT%{sitearchbase}/%{rubyxver}/%{_normalized_cpu}-%{_target_os}

# remove shebang
for i in \
	$RPM_BUILD_ROOT%{vendorlibbase}/%{rubyxver}/{abbrev,generator,irb/{cmd/subirb,ext/save-history},matrix,rdoc/{markup/sample/rdoc2latex,parsers/parse_rb},set,tsort}.rb; \
	do
	sed -i -e '/^#!.*/,1D' $i
done
# The following can be executable
chmod 0644 $RPM_BUILD_ROOT%{vendorarchbase}/%{rubyxver}/%{_normalized_cpu}-%{_target_os}/*.h

find $RPM_BUILD_ROOT/ -name "*.so" -exec chmod 755 {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-, root, root, -)
%doc	%{name}-%{arcver}/COPYING*
%doc	%{name}-%{arcver}/ChangeLog
%doc	%{name}-%{arcver}/GPL
%doc	%{name}-%{arcver}/LEGAL
%doc	%{name}-%{arcver}/LGPL
%doc	%{name}-%{arcver}/NEWS
%doc	%{name}-%{arcver}/README
%lang(ja)	%doc	%{name}-%{arcver}/README.ja
%doc	%{name}-%{arcver}/ToDo
%doc	tmp-ruby-docs/ruby/*
%{_bindir}/ruby
%{_bindir}/erb
%{_bindir}/testrb
%{_mandir}/man1/ruby.1*

%files	devel
%defattr(-, root, root, -)
%doc	%{name}-%{arcver}/COPYING*
%doc	%{name}-%{arcver}/ChangeLog
%doc	%{name}-%{arcver}/GPL
%doc	%{name}-%{arcver}/LEGAL
%doc	%{name}-%{arcver}/LGPL
%doc	%{name}-%{arcver}/README.EXT
%lang(ja)	%doc	%{name}-%{arcver}/README.EXT.ja
%{_libdir}/libruby.so
%{vendorarchbase}/%{rubyxver}/%{_normalized_cpu}-%{_target_os}/*.h

%files	static
%defattr(-, root, root, -)
%{_libdir}/libruby-static.a

%files	libs
%defattr(-, root, root, -)
%doc %{name}-%{arcver}/README
%lang(ja)	%doc	%{name}-%{arcver}/README.ja
%doc	%{name}-%{arcver}/COPYING*
%doc	%{name}-%{arcver}/ChangeLog
%doc	%{name}-%{arcver}/GPL
%doc	%{name}-%{arcver}/LEGAL
%doc	%{name}-%{arcver}/LGPL
%doc	tmp-ruby-docs/ruby-libs/*
%dir	%{vendorlibbase}
%dir	%{vendorlibbase}/%{rubyxver}
%{sitelibbase}
%ifarch ppc64 s390x sparc64 x86_64
%dir	%{vendorarchbase}
%dir	%{vendorarchbase}/%{rubyxver}
%{sitearchbase}
%endif
## the following files should goes into ruby-rdoc package.
%exclude	%{vendorlibbase}/%{rubyxver}/rdoc
## the following files should goes into ruby-irb package.
%exclude	%{vendorlibbase}/%{rubyxver}/irb.rb
%exclude	%{vendorlibbase}/%{rubyxver}/irb
## files in ruby-libs from here
%{vendorlibbase}/%{rubyxver}/*.rb
%{vendorlibbase}/%{rubyxver}/bigdecimal
%{vendorlibbase}/%{rubyxver}/cgi
%{vendorlibbase}/%{rubyxver}/date
%{vendorlibbase}/%{rubyxver}/digest
%{vendorlibbase}/%{rubyxver}/dl
%{vendorlibbase}/%{rubyxver}/drb
%{vendorlibbase}/%{rubyxver}/io
%{vendorlibbase}/%{rubyxver}/net
%{vendorlibbase}/%{rubyxver}/openssl
%{vendorlibbase}/%{rubyxver}/optparse
%{vendorlibbase}/%{rubyxver}/racc
%{vendorlibbase}/%{rubyxver}/rexml
%{vendorlibbase}/%{rubyxver}/rinda
%{vendorlibbase}/%{rubyxver}/rss
%{vendorlibbase}/%{rubyxver}/runit
%{vendorlibbase}/%{rubyxver}/shell
%{vendorlibbase}/%{rubyxver}/soap
%{vendorlibbase}/%{rubyxver}/test
%{vendorlibbase}/%{rubyxver}/uri
%{vendorlibbase}/%{rubyxver}/webrick
%{vendorlibbase}/%{rubyxver}/wsdl
%{vendorlibbase}/%{rubyxver}/xmlrpc
%{vendorlibbase}/%{rubyxver}/xsd
%{vendorlibbase}/%{rubyxver}/yaml
%{_libdir}/libruby.so.*
%{vendorarchbase}/%{rubyxver}/%{_normalized_cpu}-%{_target_os}/*.so
%{vendorarchbase}/%{rubyxver}/%{_normalized_cpu}-%{_target_os}/digest
%{vendorarchbase}/%{rubyxver}/%{_normalized_cpu}-%{_target_os}/io
%{vendorarchbase}/%{rubyxver}/%{_normalized_cpu}-%{_target_os}/racc
%{vendorarchbase}/%{rubyxver}/%{_normalized_cpu}-%{_target_os}/rbconfig.rb

%files	rdoc
%defattr(-, root, root, -)
%doc	%{name}-%{arcver}/COPYING*
%doc	%{name}-%{arcver}/ChangeLog
%doc	%{name}-%{arcver}/GPL
%doc	%{name}-%{arcver}/LEGAL
%doc	%{name}-%{arcver}/LGPL
%{_bindir}/rdoc
%{vendorlibbase}/%{rubyxver}/rdoc

%files irb
%defattr(-, root, root, -)
%doc	%{name}-%{arcver}/COPYING*
%doc	%{name}-%{arcver}/ChangeLog
%doc	%{name}-%{arcver}/GPL
%doc	%{name}-%{arcver}/LEGAL
%doc	%{name}-%{arcver}/LGPL
%doc	tmp-ruby-docs/irb/*
%{_bindir}/irb
%{vendorlibbase}/%{rubyxver}/irb.rb
%{vendorlibbase}/%{rubyxver}/irb

%files ri
%defattr(-, root, root, -)
%doc	%{name}-%{arcver}/COPYING*
%doc	%{name}-%{arcver}/ChangeLog
%doc	%{name}-%{arcver}/GPL
%doc	%{name}-%{arcver}/LEGAL
%doc	%{name}-%{arcver}/LGPL
%{_bindir}/ri
%{_datadir}/ri

%changelog
* Fri Aug 19 2011 Sergio Rubio <rubiojr@frameos.org> - 1.8.7.352-5
- remove TCL/TK
- --disable-pthreads --without-X11

* Mon Aug 08 2011 Sergio Rubio <rubiojr@frameos.org> - 1.8.7.352-3
- Test new build flags

* Wed Aug 03 2011 Sergio Rubio <rubiojr@frameos.org> - 1.8.7.352-2
- Test new build flags

* Tue Jul 12 2011 Sergio Rubio <rubiojr@frameos.org> - 1.8.7.352-1
- new upstream release

* Tue Apr 26 2011 Sergio Rubio <rubiojr@frameos.org> - 1.8.7.334-3
- Do not depend on AutoConf >= 2.60

* Thu Apr  7 2011 Erik Sabowski <airyk@sabowski.com> - 1.8.7.334-2
- Update to build on CentOS 5.5:
- 'compat-readline5-devel' only used for >=fc13, rhel5 just needs 'readline5-devel'
- add 'BuildRoot:' line since rpmbuild on CentOS 5.5 still requires it
- don't use "noarch" on subpackages for certain distros

* Sat Feb 19 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.7.334-1
- Update to 1.8.7 p334

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.7.330-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Dennis Gilmore <dennis@ausil.us> - 1.8.7.330-2
- nomalise the 32 bit sparc archs to sparc

* Sun Dec 26 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.7.330-1
- Update to 1.8.7 p330
- ext/tk updated to the newest header

* Thu Nov  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.7.302-2
- Avoid multilib conflict on -libs subpackage (bug 649174)

* Mon Aug 23 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.7.302-1
- Update to 1.8.7.302
- CVE-2010-0541 (bug 587731) is fixed in this version
- Update ext/tk to the latest head

* Mon Aug  2 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.7.299-5
- More cleanup of spec file, expecially for rpmlint issue
- build ri files in %%build

* Mon Jul 26 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.7.299-4
- Cleanup spec file
- Make -irb, -rdoc subpackage noarch
- Make dependencies between arch-dependent subpackages isa specific
- Improve sample documentation gathering

* Mon Jul 12 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.8.7.299-3
- updated packaged based on feedback (from mtasaka)
- added comments to all patches / sources
- obsoleted ruby-mode, as it's now provided by the emacs package itself
- readded missing documentation
- various small compatability/regression fixes

* Tue Jul 06 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.8.7.299-2
- readded bits to pull tk package from upstream source branch
- removed unecessary .tk.old dir
- renamed macros which may cause confusion, removed unused ones

* Thu Jun 24 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.8.7.299-1
- integrate more of jmeyering's and mtaska's feedback
- removed emacs bits that are now shipped with the emacs package
- various patch and spec cleanup
- rebased to ruby 1.8.7 patch 299, removed patches no longer needed:
   ruby-1.8.7-openssl-1.0.patch, ruby-1.8.7-rb_gc_guard_ptr-optimization.patch

* Wed Jun 23 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.8.7.249-5
- Various fixes

* Wed Jun 23 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.8.7.249-4
- Fixed incorrect paths in 1.8.7 rpm

* Tue Jun 22 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.8.7.249-3
- Integrated Jim Meyering's feedback and changes in to:
- remove trailing blanks
- placate rpmlint
- ruby_* definitions: do not use trailing slashes in directory names
- _normalized_cpu: simplify definition

* Mon Jun 21 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.8.7.249-2
- Integrate mtasaka's feedback and changes
- patch101 ruby_1_8_7-rb_gc_guard_ptr-optimization.patch

* Tue Jun 15 2010 Mohammed Morsi <mmorsi@redhat.com> - 1.8.7.249-1
- Initial Ruby 1.8.7 specfile

* Wed May 19 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.6.399-5
- Retry for bug 559158, Simplify the OpenSSL::Digest class
  pull more change commits from ruby_1_8 branch

* Mon May 17 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.6.399-4
- Patch36 (ruby-1.8.x-RHASH_SIZE-rb_hash_lookup-def.patch)
  also backport rb_hash_lookup definition (bug 592936)

* Thu May 13 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.6.399-3
- ruby-1.8.x-null-class-must-be-Qnil.patch (bug 530407)
- Recreate some patches using upstream svn when available, and
  add some comments for patches

* Tue May 11 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.6.399-2
- tcltk: Give up using potentially unmaintained ruby_1_8_6 branch
  and instead completely replace with ruby_1_8 branch head
  (at this time, using rev 27738)
  (seems to fix 560053, 590503)
- Fix Japanese encoding strings under ruby-tcltk/ext/tk/sample/

* Tue Apr 27 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.6.399-1
- Update to 1.8.6 p 399 (bug 579675)
- Patch to fix gc bug causing open4 crash (bug 580993)

* Fri Mar 12 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.6.388-9
- F-14: rebuild against new gdbm

* Thu Jan 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Once revert the previous change (patch34)

* Wed Jan 27 2010 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.8.6.388-8
- Backport openssl/digest functions providing digest and hexdigest functions
  directly in OpenSSL::Digest.methods
- Make sure that Red Hat people version their changelog entries
- This is actually release #1, but now needs to be release #7

* Mon Jan 18 2010 Akira TAGOH <tagoh@redhat.com> - 1.8.6.388-1
- Add conditional for RHEL.

* Wed Jan 13 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.6.383-6
- CVE-2009-4492 ruby WEBrick log escape sequence (bug 554485)

* Wed Dec  9 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.6.383-5
- Change mkmf.rb to use LIBRUBYARG_SHARED so that have_library() works
  without libruby-static.a (bug 428384)
- And move libruby-static.a to -static subpackage

* Thu Oct 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.6.383-4
- Use bison to regenerate parse.c to keep the original format of error
  messages (bug 530275 comment 4)

* Sun Oct 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.6.383-3
- Patch so that irb saves its history (bug 518584, ruby issue 1556)

* Sat Oct 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.6.383-2
- Update to 1.8.6 patchlevel 383 (bug 520063)

* Wed Oct 14 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.6.369-5
- Much better idea for Patch31 provided by Akira TAGOH <tagoh@redhat.com>

* Wed Oct 14 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.6.369-4
- Fix the search path of ri command for ri manuals installed with gem
  (bug 528787)

* Wed Aug 26 2009 Tomas Mraz <tmraz@redhat.com> - 1.8.6.369-3
- Rebuild against new openssl

* Thu Jul 23 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.6.369-2
- Make sure that readline.so is linked against readline 5 because
  Ruby is under GPLv2

* Sat Jun 20 2009  Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.8.6.369-1
- New patchlevel fixing CVE-2009-1904
- Fix directory on ARM (#506233, Kedar Sovani)

* Sun May 31 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.8.6.368-1
- New upstream release (p368)

* Sat Apr 11 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.6.287-8
- Merge Review fix (#226381)

* Wed Mar 18 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.8.6.287-7
- Fix regression in CVE-2008-3790 (#485383)

* Mon Mar 16 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.8.6.287-6
- Again use -O2 optimization level
- i586 should search i386-linux directory (on <= F-11)

* Thu Mar 05 2009 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.8.6.287-5
- Rebuild for gcc4.4

* Fri Feb 27 2009 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.8.6.287-3
- CVE-2008-5189: CGI header injection.

* Wed Oct  8 2008 Akira TAGOH <tagoh@redhat.com> - 1.8.6.287-2
- CVE-2008-3790: DoS vulnerability in the REXML module.

* Sat Aug 23 2008 Akira TAGOH <tagoh@redhat.com> - 1.8.6.287-1
- New upstream release.
- Security fixes.
  - CVE-2008-3655: Ruby does not properly restrict access to critical
                   variables and methods at various safe levels.
  - CVE-2008-3656: DoS vulnerability in WEBrick.
  - CVE-2008-3657: Lack of taintness check in dl.
  - CVE-2008-1447: DNS spoofing vulnerability in resolv.rb.
  - CVE-2008-3443: Memory allocation failure in Ruby regex engine.
- Remove the unnecessary backported patches.

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.8.6.230-5
- rebuild against db4-4.7

* Tue Jul  1 2008 Akira TAGOH <tagoh@redhat.com> - 1.8.6.230-4
- Backported from upstream SVN to fix a segfault issue with Array#fill.

* Mon Jun 30 2008 Akira TAGOH <tagoh@redhat.com> - 1.8.6.230-3
- Backported from upstream SVN to fix a segfault issue. (#452825)
- Backported from upstream SVN to fix an integer overflow in rb_ary_fill.

* Wed Jun 25 2008 Akira TAGOH <tagoh@redhat.com> - 1.8.6.230-2
- Fix a segfault issue. (#452810)

* Tue Jun 24 2008 Akira TAGOH <tagoh@redhat.com> - 1.8.6.230-1
- New upstream release.
- Security fixes. (#452295)
  - CVE-2008-1891: WEBrick CGI source disclosure.
  - CVE-2008-2662: Integer overflow in rb_str_buf_append().
  - CVE-2008-2663: Integer overflow in rb_ary_store().
  - CVE-2008-2664: Unsafe use of alloca in rb_str_format().
  - CVE-2008-2725: Integer overflow in rb_ary_splice().
  - CVE-2008-2726: Integer overflow in rb_ary_splice().
- ruby-1.8.6.111-CVE-2007-5162.patch: removed.
- Build ruby-mode package for all archtectures.

* Tue Mar  4 2008 Akira TAGOH <tagoh@redhat.com> - 1.8.6.114-1
- Security fix for CVE-2008-1145.
- Improve a spec file. (#226381)
  - Correct License tag.
  - Fix a timestamp issue.
  - Own a arch-specific directory.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.8.6.111-9
- Autorebuild for GCC 4.3

* Tue Feb 19 2008 Akira TAGOH <tagoh@redhat.com> - 1.8.6.111-8
- Rebuild for gcc-4.3.

* Tue Jan 15 2008 Akira TAGOH <tagoh@redhat.com> - 1.8.6.111-7
- Revert the change of libruby-static.a. (#428384)

* Fri Jan 11 2008 Akira TAGOH <tagoh@redhat.com> - 1.8.6.111-6
- Fix an unnecessary replacement for shebang. (#426835)

* Fri Jan  4 2008 Akira TAGOH <tagoh@redhat.com> - 1.8.6.111-5
- Rebuild.

* Fri Dec 28 2007 Akira TAGOH <tagoh@redhat.com> - 1.8.6.111-4
- Clean up again.

* Fri Dec 21 2007 Akira TAGOH <tagoh@redhat.com> - 1.8.6.111-3
- Clean up the spec file.
- Remove ruby-man-1.4.6 stuff. this is entirely the out-dated document.
  this could be replaced by ri.
- Disable the static library building.

* Tue Dec 04 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.8.6.111-2
 - Rebuild for openssl bump

* Wed Oct 31 2007 Akira TAGOH <tagoh@redhat.com>
- Fix the dead link.

* Mon Oct 29 2007 Akira TAGOH <tagoh@redhat.com> - 1.8.6.111-1
- New upstream release.
- ruby-1.8.6.111-CVE-2007-5162.patch: Update a bit with backporting the changes
   at trunk to enable the fix without any modifications on the users' scripts.
   Note that Net::HTTP#enable_post_connection_check isn't available anymore.
   If you want to disable this post-check, you should give OpenSSL::SSL::VERIFY_NONE
   to Net::HTTP#verify_mode= instead of.

* Mon Oct 15 2007 Akira TAGOH <tagoh@redhat.com> - 1.8.6.110-2
- Enable pthread support for ppc too. (#201452)
- Fix unexpected dependencies appears in ruby-libs. (#253325)

* Wed Oct 10 2007 Akira TAGOH <tagoh@redhat.com> - 1.8.6.110-1
- New upstream release.
  - ruby-r12567.patch: removed.
- ruby-1.8.6-CVE-2007-5162.patch: security fix for Net::HTTP that is
  insufficient verification of SSL certificate.

* Thu Aug 23 2007 Akira TAGOH <tagoh@redhat.com> - 1.8.6.36-4
- Rebuild

* Fri Aug 10 2007 Akira TAGOH <tagoh@redhat.com>
- Update License tag.

* Mon Jul 25 2007 Akira TAGOH <tagoh@redhat.com> - 1.8.6.36-3
- ruby-r12567.patch: backport patch from upstream svn to get rid of
  the unnecessary declarations. (#245446)

* Wed Jul 20 2007 Akira TAGOH <tagoh@redhat.com> - 1.8.6.36-2
- New upstream release.
  - Fix Etc::getgrgid to get the correct gid as requested. (#236647)

* Wed Mar 28 2007 Akira TAGOH <tagoh@redhat.com> - 1.8.6-2
- Fix search path breakage. (#234029)

* Thu Mar 15 2007 Akira TAGOH <tagoh@redhat.com> - 1.8.6-1
- New upstream release.
- clean up a spec file.

* Tue Feb 13 2007 Akira TAGOH <tagoh@redhat.com> - 1.8.5.12-2
- Rebuild

* Mon Feb  5 2007 Akira TAGOH <tagoh@redhat.com> - 1.8.5.12-1
- New upstream release.

* Mon Dec 11 2006 Akira TAGOH <tagoh@redhat.com> - 1.8.5.2-1
- security fix release.

* Fri Oct 27 2006 Akira TAGOH <tagoh@redhat.com> - 1.8.5-4
- security fix release.
- ruby-1.8.5-cgi-CVE-2006-5467.patch: fix a CGI multipart parsing bug that
  causes the denial of service. (#212396)

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 1.8.5-3
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Akira TAGOH <tagoh@redhat.com> - 1.8.5-2
- fixed rbconfig.rb to refer to DESTDIR for sitearchdir. (#207311)

* Mon Aug 28 2006 Akira TAGOH <tagoh@redhat.com> - 1.8.5-1
- New upstream release.
- removed the unnecessary patches:
  - ruby-1.8.4-no-eaccess.patch
  - ruby-1.8.4-64bit-pack.patch
  - ruby-1.8.4-fix-insecure-dir-operation.patch
  - ruby-1.8.4-fix-insecure-regexp-modification.patch
  - ruby-1.8.4-fix-alias-safe-level.patch
- build with --enable-pthread except on ppc.
- ruby-1.8.5-hash-memory-leak.patch: backported from CVS to fix a memory leak
  on Hash. [ruby-talk:211233]

* Mon Aug  7 2006 Akira TAGOH <tagoh@redhat.com> - 1.8.4-12
- owns sitearchdir. (#201208)

* Thu Jul 20 2006 Akira TAGOH <tagoh@redhat.com> - 1.8.4-11
- security fixes [CVE-2006-3694]
  - ruby-1.8.4-fix-insecure-dir-operation.patch:
  - ruby-1.8.4-fix-insecure-regexp-modification.patch: fixed the insecure
    operations in the certain safe-level restrictions. (#199538)
  - ruby-1.8.4-fix-alias-safe-level.patch: fixed to not bypass the certain
    safe-level restrictions. (#199543)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.8.4-10.fc6.1
- rebuild

* Mon Jun 19 2006 Akira TAGOH <tagoh@redhat.com> - 1.8.4-10
- fixed the wrong file list again. moved tcltk library into ruby-tcltk.
  (#195872)

* Thu Jun  8 2006 Akira TAGOH <tagoh@redhat.com> - 1.8.4-8
- ruby-deprecated-sitelib-search-path.patch: correct the order of search path.

* Wed Jun  7 2006 Akira TAGOH <tagoh@redhat.com> - 1.8.4-7
- exclude ppc64 to make ruby-mode package. right now emacs.ppc64 isn't provided
  and buildsys became much stricter.
- ruby-deprecated-sitelib-search-path.patch: applied to add more search path
  for backward compatiblity.
- added byacc to BuildReq. (#194161)

* Wed May 17 2006 Akira TAGOH <tagoh@redhat.com> - 1.8.4-6
- ruby-deprecated-search-path.patch: added the deprecated installation paths
  to the search path for the backward compatibility.
- added a Provides: ruby(abi) to ruby-libs.
- ruby-1.8.4-64bit-pack.patch: backport patch from upstream to fix unpack("l")
  not working on 64bit arch and integer overflow on template "w". (#189350)
- updated License tag to be more comfortable, and with a pointer to get more
  details, like Python package does. (#179933)
- clean up.

* Wed Apr 19 2006 Akira TAGOH <tagoh@redhat.com>
- ruby-rubyprefix.patch: moved all arch-independent modules under /usr/lib/ruby
  and keep arch-dependent modules under /usr/lib64/ruby for 64bit archs.
  so 'rubylibdir', 'sitelibdir' and 'sitedir' in Config::CONFIG points to
  the kind of /usr/lib/ruby now. (#184199)

* Mon Apr 17 2006 Akira TAGOH <tagoh@redhat.com> - 1.8.4-4
- correct sitelibdir. (#184198)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.8.4-3.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.8.4-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Feb  6 2006 Akira TAGOH <tagoh@redhat.com> - 1.8.4-3
- ruby-1.8.4-no-eaccess.patch: backported from ruby CVS to avoid conflict
  between newer glibc. (#179835)

* Wed Jan  4 2006 Akira TAGOH <tagoh@redhat.com> - 1.8.4-2
- ruby-tcltk-multilib.patch: fixed a typo.

* Tue Dec 27 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.4-1
- New upstream release.
  - fixed a missing return statement. (#140833)
  - fixed an use of uninitialized variable. (#144890)

* Fri Dec 16 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.4-0.4.preview2
- updates to 1.8.4-preview2.
- renamed the packages to ruby-* (#175765)
  - irb  -> ruby-irb
  - rdoc -> ruby-rdoc
  - ri   -> ruby-ri
- added tcl-devel and tk-devel into BuildRequires.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 10 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.4-0.3.preview1
- rebuilt against the latest openssl.

* Tue Nov  1 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.4-0.2.preview1
- build-deps libX11-devel instead of xorg-x11-devel.

* Mon Oct 31 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.4-0.1.preview1
- New upstream release.
- ruby-1.8.2-strscan-memset.patch: removed because it's no longer needed.

* Tue Oct  4 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.3-4
- moved the documents from ruby-libs to ruby-docs, which contains the arch
  specific thing and to be multilib support. (#168826)

* Mon Oct  3 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.3-3
- fixed the wrong file list. the external library for tcl/tk was included
  in ruby-libs unexpectedly.

* Mon Sep 26 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.3-2
- ruby-multilib.patch: added another chunk for multilib. (#169127)

* Wed Sep 21 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.3-1
- New upstream release.
- Build-Requires xorg-x11-devel instead of XFree86-devel.
- ruby-multilib.patch: applied for only 64-bit archs.
- ruby-1.8.2-xmlrpc-CAN-2005-1992.patch: removed. it has already been in upstream.

* Tue Jun 21 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.2-9
- ruby-1.8.2-xmlrpc-CAN-2005-1992.patch: fixed the arbitrary command execution
  on XMLRPC server. (#161096)

* Thu Jun 16 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.2-8
- ruby-1.8.2-tcltk-multilib.patch: applied to get tcltklib.so built. (#160194)

* Thu Apr  7 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.2-7
- ruby-1.8.2-deadcode.patch: removed the dead code from the source. (#146108)
- make sure that all documentation files in ruby-docs are the world-
  readable. (#147279)

* Tue Mar 22 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.2-6
- ruby-1.8.2-strscan-memset.patch: fixed an wrong usage of memset(3).

* Tue Mar 15 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.2-5
- rebuilt

* Tue Jan 25 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.2-4
- fixed the wrong generation of file manifest. (#146055)
- spec file clean up.

* Mon Jan 24 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.2-3
- separated out to rdoc package.
- make the dependency of irb for rdoc. (#144708)

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> - 1.8.2-2
- Rebuilt for new readline.

* Wed Jan  5 2005 Akira TAGOH <tagoh@redhat.com> - 1.8.2-1
- New upstream release.
- ruby-1.8.1-ia64-stack-limit.patch: removed - it's no longer needed.
- ruby-1.8.1-cgi_session_perms.patch: likewise.
- ruby-1.8.1-cgi-dos.patch: likewise.
- generated Ruby interactive documentation - senarated package.
  it's now provided as ri package. (#141806)

* Thu Nov 11 2004 Jeff Johnson <jbj@jbj.org> 1.8.1-10
- rebuild against db-4.3.21.

* Wed Nov 10 2004 Akira TAGOH <tagoh@redhat.com> - 1.8.1-9
- ruby-1.8.1-cgi-dos.patch: security fix [CAN-2004-0983]
- ruby-1.8.1-cgi_session_perms.patch: security fix [CAN-2004-0755]

* Fri Oct 29 2004 Akira TAGOH <tagoh@redhat.com> - 1.8.1-8
- added openssl-devel and db4-devel into BuildRequires (#137479)

* Wed Oct  6 2004 Akira TAGOH <tagoh@redhat.com> - 1.8.1-7
- require emacs-common instead of emacs.

* Wed Jun 23 2004 Akira TAGOH <tagoh@redhat.com> 1.8.1-4
- updated the documentation.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 04 2004 Akira TAGOH <tagoh@redhat.com> 1.8.1-1
- New upstream release.
- don't use any optimization for ia64 to avoid the build failure.
- ruby-1.8.1-ia64-stack-limit.patch: applied to fix SystemStackError when the optimization is disabled.

* Sat Dec 13 2003 Jeff Johnson <jbj@jbj.org> 1.8.0-3
- rebuild against db-4.2.52.

* Thu Sep 25 2003 Jeff Johnson <jbj@jbj.org> 1.8.0-2
- rebuild against db-4.2.42.

* Tue Aug  5 2003 Akira TAGOH <tagoh@redhat.com> 1.8.0-1
- New upstream release.

* Thu Jul 24 2003 Akira TAGOH <tagoh@redhat.com> 1.6.8-9.1
- rebuilt

* Thu Jul 24 2003 Akira TAGOH <tagoh@redhat.com> 1.6.8-9
- ruby-1.6.8-castnode.patch: handling the nodes with correct cast.
  use this patch now instead of ruby-1.6.8-fix-x86_64.patch.

* Fri Jul 04 2003 Akira TAGOH <tagoh@redhat.com> 1.6.8-8
- rebuilt

* Fri Jul 04 2003 Akira TAGOH <tagoh@redhat.com> 1.6.8-7
- fix the gcc warnings. (#82192)
- ruby-1.6.8-fix-x86_64.patch: correct a patch.
  NOTE: DON'T USE THIS PATCH FOR BIG ENDIAN ARCHITECTURE.
- ruby-1.6.7-long2int.patch: removed.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb  7 2003 Jens Petersen <petersen@redhat.com> - 1.6.8-5
- rebuild against ucs4 tcltk

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jan 22 2003 Akira TAGOH <tagoh@redhat.com> 1.6.8-3
- ruby-1.6.8-multilib.patch: applied to fix the search path issue on x86_64

* Tue Jan 21 2003 Akira TAGOH <tagoh@redhat.com> 1.6.8-2
- ruby-1.6.8-require.patch: applied to fix the search bug in require.
- don't apply long2int patch to s390 and s390x. it doesn't work.

* Wed Jan 15 2003 Akira TAGOH <tagoh@redhat.com> 1.6.8-1
- New upstream release.
- removed some patches. it's no longer needed.
  - ruby-1.6.7-100.patch
  - ruby-1.6.7-101.patch
  - ruby-1.6.7-102.patch
  - ruby-1.6.7-103.patch
  - 801_extmk.rb-shellwords.patch
  - 801_mkmf.rb-shellwords.patch
  - 804_parse.y-new-bison.patch
  - 805_uri-bugfix.patch
  - ruby-1.6.6-900_XXX_strtod.patch
  - ruby-1.6.7-sux0rs.patch
  - ruby-1.6.7-libobj.patch

* Wed Jan 15 2003 Jens Petersen <petersen@redhat.com> 1.6.7-14
- rebuild to update tcltk deps

* Mon Dec 16 2002 Elliot Lee <sopwith@redhat.com> 1.6.7-13
- Remove ExcludeArch: x86_64
- Fix x86_64 ruby with long2int.patch (ruby was assuming that sizeof(long)
  == sizeof(int). The patch does not fix the source of the problem, just
  makes it a non-issue.)
- _smp_mflags

* Tue Dec 10 2002 Tim Powers <timp@redhat.com> 1.6.7-12
- rebuild to fix broken tcltk deps

* Tue Oct 22 2002 Akira TAGOH <tagoh@redhat.com> 1.6.7-11
- use %%configure macro instead of configure script.
- use the latest config.{sub,guess}.
- get archname from rbconfig.rb for %%dir
- applied some patches from Debian:
  - 801_extmk.rb-shellwords.patch: use Shellwords
  - 801_mkmf.rb-shellwords.patch: mkmf.rb creates bad Makefile. the Makefile
    links libruby.a to the target.
  - 803_sample-fix-shbang.patch: all sample codes should be
    s|/usr/local/bin|/usr/bin|g
  - 804_parse.y-new-bison.patch: fix syntax warning.
  - 805_uri-bugfix.patch: uri.rb could not handle correctly broken mailto-uri.
- add ExcludeArch x86_64 temporarily to fix Bug#74581. Right now ruby can't be
  built on x86_64.

* Tue Aug 27 2002 Akira TAGOH <tagoh@redhat.com> 1.6.7-10
- moved sitedir to /usr/lib/ruby/site_ruby again according as our perl and
  python.
- ruby-1.6.7-resolv1.patch, ruby-1.6.7-resolv2.patch: applied to fix 'Too many
  open files - "/etc/resolv.conf"' issue. (Bug#64830)

* Thu Jul 18 2002 Akira TAGOH <tagoh@redhat.com> 1.6.7-9
- add the owned directory.

* Fri Jul 12 2002 Akira TAGOH <tagoh@redhat.com> 1.6.7-8
- fix typo.

* Thu Jul 04 2002 Akira TAGOH <tagoh@redhat.com> 1.6.7-7
- removed the ruby-mode-xemacs because it's merged to the xemacs sumo.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Akira TAGOH <tagoh@redhat.com> 1.6.7-5
- fix the stripped binary.
- use the appropriate macros.

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Akira TAGOH <tagoh@redhat.com> 1.6.7-3
- ruby-1.6.7-libobj.patch: applied to fix autoconf2.53 error.

* Mon Mar 18 2002 Akira TAGOH <tagoh@redhat.com> 1.6.7-2
- ruby-man-1.4.6-jp.tar.bz2: removed.
- ruby-refm-rdp-1.4.7-ja-html.tar.bz2: uses it instead of.
- ruby-1.6.7-500-marshal-proc.patch, ruby-1.6.7-501-class-var.patch:
  removed.
- ruby-1.6.7-100.patch: applied a bug fix patch.
  (ruby-dev#16274: patch for 'wm state')
  (PR#206ja: SEGV handle EXIT)
- ruby-1.6.7-101.patch: applied a bug fix patch.
  (ruby-list#34313: singleton should not be Marshal.dump'ed)
  (ruby-dev#16411: block local var)
- ruby-1.6.7-102.patch: applied a bug fix patch.
  (handling multibyte chars is partially broken)
- ruby-1.6.7-103.patch: applied a bug fix patch.
  (ruby-dev#16462: preserve reference for GC, but link should be cut)

* Fri Mar  8 2002 Akira TAGOH <tagoh@redhat.com> 1.6.7-1
- New upstream release.
- ruby-1.6.6-100.patch, ruby-1.6.6-501-ruby-mode.patch:
  removed. these patches no longer should be needed.
- ruby-1.6.7-500-marshal-proc.patch: applied a fix patch.
  (ruby-dev#16178: Marshal::dump should call Proc#call.)
- ruby-1.6.7-501-class-var.patch: applied a fix patch.
  (ruby-talk#35157: class vars broken in 1.6.7)

* Wed Feb 27 2002 Akira TAGOH <tagoh@redhat.com> 1.6.6-5
- Disable alpha because nothing is xemacs for alpha now.

* Tue Feb  5 2002 Akira TAGOH <tagoh@redhat.com> 1.6.6-3
- Fixed the duplicate files.

* Tue Feb  5 2002 Akira TAGOH <tagoh@redhat.com> 1.6.6-2
- Fixed the missing %%defattr

* Fri Feb  1 2002 Akira TAGOH <tagoh@redhat.com> 1.6.6-1
- New upstream release.
- Applied bug fix patches:
  - ruby-1.6.6-501-ruby-mode.patch: ruby-talk#30479: disables font-lock
    coloring.
  - ruby-1.6.6-100.patch: ruby-talk#30203: Ruby 1.6.6 bug and fix
                          ruby-list#33047: regex bug
                          PR#230: problem with -d in 1.6.6
- Added ruby-mode and ruby-mode-xemacs packages.
- Ruby works fine for ia64. so re-enable to build with ia64.
  (probably it should be worked for alpha)

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jul 19 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.6.4-2
- Remove Japanese description and summaries; they belong in specspo and
  break rpm
- Clean up specfile
- Mark language specific files (README.jp) as such
- bzip2 sources
- rename the libruby package to ruby-libs for consistency
- Exclude ia64 (doesn't build - the code doesn't seem to be 64-bit clean
  [has been excluded on alpha forever])

* Tue Jul 17 2001 Akira TAGOH <tagoh@redhat.com> 1.6.4-1
- rebuild for Red Hat 7.2

* Mon Jun 04 2001 akira yamada <akira@vinelinux.org>
- upgrade to nwe upstream version 1.6.4.

* Mon Apr 02 2001 akira yamada <akira@vinelinux.org>
- applied patch:
  - fixed method cache bug. etc. (Patch103, Patch104)

* Tue Mar 27 2001 akira yamada <akira@vinelinux.org>
- applied patch:
  - fixed marshal for bignum bug.
  - fixed scope of constant variables bug.

* Tue Mar 20 2001 akira yamada <akira@vinelinux.org>
- upgraded to new upstream version 1.6.3.

* Fri Feb 09 2001 akira yamada <akira@vinelinux.org>
- fixed bad group for libruby.
- Applied patch: upgraded to cvs version (2001-02-08):
  fixed minor bugs.

* Thu Jan 18 2001 akira yamada <akira@vinelinux.org>
- Applied patch: upgraded to cvs version (2001-01-15):
  fixed minor bugs(e.g. ruby makes extention librares too large...).

* Wed Jan 10 2001 akira yamada <akira@vinelinux.org>
- Applied patch: upgraded to cvs version (2001-01-09):
  fixed minor bugs.

* Sat Dec 30 2000 akira yamada <akira@vinelinux.org>
- Applied bug fix patch.

* Mon Dec 25 2000 akira yamada <akira@vinelinux.org>
- Updated to new upstream version 1.6.2.

* Fri Dec 22 2000 akira yamada <akira@vinelinux.org>
- Removed ruby_cvs.2000122019.patch, added ruby_cvs.2000122215.patch
  (upgraded ruby to latest cvs version, 1.6.2-preview4).

* Wed Dec 20 2000 akira yamada <akira@vinelinux.org>
- Removed ruby_cvs.2000121413.patch, added ruby_cvs.2000122019.patch
  (upgraded ruby to latest cvs version).
- new package: libruby

* Thu Dec 14 2000 akira yamada <akira@vinelinux.org>
- Removed ruby_cvs.2000101901.patch, added ruby_cvs.2000121413.patch
  (upgraded ruby to latest cvs version).
- Removed ruby-dev.11262.patch, ruby-dev.11265.patch,
  and ruby-dev.11268.patch (included into above patch).

* Sun Nov 12 2000 MACHINO, Satoshi <machino@vinelinux.org> 1.6.1-0vl9
- build on gcc-2.95.3

* Thu Oct 19 2000 akira yamada <akira@vinelinux.org>
- Added ruby-dev.11268.patch.

* Thu Oct 19 2000 akira yamada <akira@vinelinux.org>
- Removed ruby_cvs.2000101117.patch and added ruby_cvs.2000101901.patch
  (upgraded ruby to latest cvs version).
- Added ruby-dev.11262.patch.
- Added ruby-dev.11265.patch.

* Wed Oct 11 2000 akira yamada <akira@vinelinux.org>
- Removed ruby_cvs.2000100313.patch and added ruby_cvs.2000101117.patch
  (upgraded ruby to latest cvs version).

* Mon Oct 09 2000 akira yamada <akira@vinelinux.org>
- Removed ruby_cvs.2000100313.patch and added ruby_cvs.2000100313.patch
  (upgraded ruby to latest cvs version).

* Tue Oct 03 2000 akira yamada <akira@vinelinux.org>
- Removed ruby_cvs.2000100218.patch and added ruby_cvs.2000100313.patch
  (upgraded ruby to latest cvs version).

* Mon Oct 02 2000 akira yamada <akira@vinelinux.org>
- Removed ruby_cvs.2000092718.patch and added ruby_cvs.2000100218.patch
  (upgraded ruby to latest cvs version).

* Thu Sep 27 2000 akira yamada <akira@vinelinux.org>
- Updated to upstream version 1.6.1.
- Removed ruby_cvs.2000082901.patch and added ruby_cvs.2000092718.patch
  (upgraded ruby to latest cvs version).

* Tue Aug 29 2000 akira yamada <akira@redhat.com>
- Updated to version 1.4.6.
- removed ruby-dev.10123.patch(included into ruby-1.4.6).
- Added ruby_cvs.2000082901.patch(upgraded ruby to latest cvs version).

* Tue Jun 27 2000 akira yamada <akira@redhat.com>
- Updated manuals to version 1.4.5.

* Sun Jun 25 2000 akira yamada <akira@redhat.com>
- Added ruby-dev.10123.patch.

* Sat Jun 24 2000 akira yamada <akira@redhat.com>
- Updated to version 1.4.5.
- Removed ruby_cvs.2000062401.patch(included into ruby-1.4.5).

* Thu Jun 22 2000 akira yamada <akira@redhat.com>
- Updated to version 1.4.4(06/22/2000 CVS).
- Removed ruby-dev.10054.patch(included into ruby_cvs.patch).

* Thu Jun 22 2000 akira yamada <akira@redhat.com>
- Renamed to ruby_cvs20000620.patch from ruby_cvs.patch.

* Tue Jun 20 2000 akira yamada <akira@redhat.com>
- Updated to version 1.4.4(06/20/2000 CVS).
- Removed ruby-list.23190.patch(included into ruby_cvs.patch).
- Added ruby-dev.10054.patch.

* Tue Jun 15 2000 akira yamada <akira@redhat.com>
- Updated to version 1.4.4(06/12/2000 CVS).
- Added manuals and FAQs.
- Split into ruby, ruby-devel, ruby-tcltk, ruby-docs, irb.

* Tue Jun 13 2000 Mitsuo Hamada <mhamada@redhat.com>
- Updated to version 1.4.4

* Wed Dec 08 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.4.3

* Mon Sep 20 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.4.2 (Sep 18)

* Fri Sep 17 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.4.2

* Tue Aug 17 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.4.0

* Fri Jul 23 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- 2nd release
- Updated to version 1.2.6(15 Jul 1999)
- striped %%{prefix}/bin/ruby

* Mon Jun 28 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.2.6(21 Jun 1999)

* Wed Apr 14 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.2.5

* Fri Apr 09 1999 Atsushi Yamagata <yamagata@plathome.co.jp>
- Updated to version 1.2.4

* Fri Dec 25 1998 Toru Hoshina <hoshina@best.com>
- Version up to 1.2 stable.

* Fri Nov 27 1998 Toru Hoshina <hoshina@best.com>
- Version up to 1.1c9.

* Thu Nov 19 1998 Toru Hoshina <hoshina@best.com>
- Version up to 1.1c8, however it appear short life :-P

* Fri Nov 13 1998 Toru Hoshina <hoshina@best.com>
- Version up.

* Mon Sep 22 1998 Toru Hoshina <hoshina@best.com>
- To make a libruby.so.

* Mon Sep 21 1998 Toru Hoshina <hoshina@best.com>
- Modified SPEC in order to install libruby.a so that it should be used by
  another ruby entention.
- 2nd release.

* Mon Mar 9 1998 Shoichi OZAWA <shoch@jsdi.or.jp>
- Added a powerPC arch part. Thanks, MURATA Nobuhiro <nob@makioka.y-min.or.jp>

