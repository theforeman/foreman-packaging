%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Initially generated from hpricot-0.6.164.gem by gem2rpm -*- rpm-spec -*-
%define	rubyabi		1.9.1

%define	gem_name		hpricot

Summary:	A Fast, Enjoyable HTML Parser for Ruby
Name:		%{?scl_prefix}rubygem-%{gem_name}
Version:	0.8.6
Release:	7%{?dist}
Group:		Development/Languages
# ext/fast_xs/FastXsService.java is licensed under ASL 2.0
License:	MIT and ASL 2.0
URL:		http://github.com/hpricot/hpricot
# Non-free file removed, see Source10
# Source0:	http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Source0:	%{gem_name}-%{version}-modified.gem
Source10:	rubygem-hpricot-create-free-gem.sh

BuildRequires:	%{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires:	%{?scl_prefix}rubygems-devel
# Recompile
BuildRequires:	%{?scl_prefix}rubygem(rake)
# Others
BuildRequires:	%{?scl_prefix}rubygem(rake-compiler)
%if 0%{?fedora} >= 16
BuildRequires:	%{?scl_prefix}rubygem(rdoc)
%endif
BuildRequires:	%{?scl_prefix}ruby-devel
BuildRequires:	ragel
BuildRequires:  %{?scl_prefix}rubygem(minitest)
BuildRequires:  %{?scl_prefix}rubygem(rake)
Requires:	%{?scl_prefix}ruby(abi) = %{rubyabi}
Requires:	%{?scl_prefix}ruby(rubygems)
Provides:	%{?scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}

%description
Hpricot is a very flexible HTML parser, based on Tanaka Akira's 
HTree and John Resig's JQuery, but with the scanner recoded in C 
(using Ragel for scanning.)

%package	doc
Summary:	Documentation for %{pkg_name}
Group:		Documentation
# Directory ownership issue
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}
Requires:	%{?scl_prefix}ruby(rubygems)

%description	doc
This package contains documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -T -c
mkdir -p ./%{gem_dir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%{?scl:scl enable %{scl} "}
gem install \
	--local \
	--install-dir ./%{gem_dir} \
	-V --force \
	%{SOURCE0}
%{?scl:"}

pushd .%{gem_instdir}/test
# Kill tests related to BOINGBOING, licensed under CC-BY-NC
grep -rl BOING . | \
	xargs sed -i '/BOING/s|^\([ \t][ \t]*\)\(.*\)$|\1# This test is intentionally killed\n\1return true\n\1\2|'
popd

# ??
find . -type f | xargs chmod ugo+r

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}

mkdir -p %{buildroot}%{gem_extdir}/lib
mv %{buildroot}%{gem_libdir}/*.so %{buildroot}%{gem_extdir}/lib

# Shebang
for f in $(find %{buildroot}%{gem_instdir} -name \*.rb)
do
	sed -i -e '/^#!/d' $f
	chmod 0644 $f
done

# clean
rm -rf %{buildroot}%{gem_instdir}/tmp/

# Kill unneeded files
find %{buildroot}%{gem_instdir}/ext \
	-type f \
	-not -name \*.java \
	-print0 | \
	xargs -0 rm -f
rm -f %{buildroot}%{gem_instdir}/.require_paths
DIR=%{buildroot}%{gem_libdir}/universal-java*
[ -d $DIR ] && rmdir $DIR

# The following method is completely copied from rubygem-gettext
# spec file
#
# Create symlinks
##
## Note that before switching to gem %%{ruby_sitelib}/%%{gem_name}
## already existed as a directory, so this cannot be replaced
## by symlink (cpio fails)
## Similarly, all directories under %%{ruby_sitelib} cannot be
## replaced by symlink
#

create_symlink_rec(){

ORIGBASEDIR=$1
TARGETBASEDIR=$2

## First calculate relative path of ORIGBASEDIR 
## from TARGETBASEDIR
TMPDIR=$TARGETBASEDIR
BACKDIR=
DOWNDIR=
num=0
nnum=0
while true
do
	num=$((num+1))
	TMPDIR=$(echo $TMPDIR | sed -e 's|/[^/][^/]*$||')
	DOWNDIR=$(echo $ORIGBASEDIR | sed -e "s|^$TMPDIR||")
	if [ x$DOWNDIR != x$ORIGBASEDIR ]
	then
		nnum=0
		while [ $nnum -lt $num ]
		do
			BACKDIR="../$BACKDIR"
			nnum=$((nnum+1))
		done
		break
	fi
done

RELBASEDIR=$( echo $BACKDIR/$DOWNDIR | sed -e 's|//*|/|g' )

## Next actually create symlink
pushd %{buildroot}/$ORIGBASEDIR
find . -type f | while read f
do
	DIRNAME=$(dirname $f)
	BACK2DIR=$(echo $DIRNAME | sed -e 's|/[^/][^/]*|/..|g')
	mkdir -p %{buildroot}${TARGETBASEDIR}/$DIRNAME
	LNNAME=$(echo $BACK2DIR/$RELBASEDIR/$f | \
		sed -e 's|^\./||' | sed -e 's|//|/|g' | \
		sed -e 's|/\./|/|' )
	ln -s -f $LNNAME %{buildroot}${TARGETBASEDIR}/$f
done
popd

}

#%if 0%{?fedora} < 17
#create_symlink_rec %{gem_libdir} %{ruby_sitelib}
#%endif

# Fix permission (bug 487654)
pushd %{buildroot}
find . -type f '(' -name '[A-Z]*' -or -name '*.java' -or -name '*.rb' -or -name '*gem*' ')' \
	-print0 | xargs -0 chmod 0644
popd

%check
export GEM_PATH=$(pwd)%{gem_dir}:%{gem_dir}
pushd .%{gem_instdir}

# problem reported here: https://github.com/hpricot/hpricot/issues/52
LANG=en_US.utf8
%{?scl:scl enable %{scl} "}
testrb -Ilib test
%{?scl:"}
popd

%files
%defattr(-,root, root,-)
%{gem_extdir}
%dir	%{gem_instdir}/
%doc	%{gem_instdir}/[A-Z]*
%exclude %{gem_instdir}/Rakefile
%{gem_instdir}/[a-l]*/
%{gem_cache}
%{gem_spec}

%files	doc
%defattr(-,root,root,-)
%{gem_instdir}/Rakefile
%{gem_instdir}/extras/
%{gem_instdir}/test/
%{gem_docdir}/

%changelog
* Fri Mar 08 2013 Lukas Zapletal <lzap+git@redhat.com> 0.8.6-7
- fixing ruby193 scl package (lzap+git@redhat.com)

* Fri Mar 08 2013 Lukas Zapletal <lzap+git@redhat.com> 0.8.6-6
- fixing ruby193 scl package (lzap+git@redhat.com)

* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 0.8.6-5
- fixing ruby193 scl package (lzap+git@redhat.com)

* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 0.8.6-4
- fixing ruby193 scl package (lzap+git@redhat.com)

* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 0.8.6-3
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 11 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.8.6-1
- 0.8.6

* Sun Feb  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.8.5-4
- F-17: kill compat ruby-%%{gem_name} package

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.5-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec  5 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.8.5-1
- 0.8.5

* Wed Mar  2 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.8.4-1
- 0.8.4

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.3-2
- Fix segfault on GC (bug 672169, patch suggested by TAGOH Akira)

* Sat Nov  6 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.3-1
- 0.8.3

* Mon Nov  9 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.2-1
- 0.8.2
- Kill BOINGBOING test properly

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.1-3
- F-12: Mass rebuild

* Sat Jun 27 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.1-2
- Readd Rakefile
- Enable check

* Wed Apr  8 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.1-1
- 0.8.1

* Thu Mar 26 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7-1
- 0.7

* Sat Feb 28 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.164-5
- Fix permission (bug 487654)

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.164-4
- F-11: Mass rebuild

* Thu Jan 15 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.164-3
- Fix license tag, removing non-free file (thanks to
  Michael Stahnke)

* Fri Dec 26 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.164-2
- Kill unneeded files more

* Sun Dec 21 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.164-1
- Switch to Gem

* Sat Dec 20 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6-3
- Fix build error related to Windows constant, detected
  by Matt's mass build
  (possibly due to rubygems 1.3.1 change)

* Wed Feb 13 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6-2
- Rebuild against gcc43
- Patch for Rakefile to skip unneeded commands call for ragel 6.0+
  (bug 432186, Thanks Jeremy Hinegardner !!)

* Tue Nov  6 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6-1
- 0.6

* Sat Nov  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.150-2
- Use rubygem(rake) for rebuild

* Fri Jun  8 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.150-1
- Initial packaging
