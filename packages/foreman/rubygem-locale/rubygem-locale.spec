%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from locale-2.0.0.gem by gem2rpm -*- rpm-spec -*-

%global	gem_name   locale

%global	repoid		67114

Summary:	Pure ruby library which provides basic APIs for localization
Name:		%{?scl_prefix}rubygem-%{gem_name}
Version:	2.0.9
Release:	15%{?dist}
Group:		Development/Languages
License:	GPLv2 or Ruby
URL:		http://locale.rubyforge.org/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch:	noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Ruby-Locale is the pure ruby library which provides basic and general purpose
APIs for localization.
It aims to support all environments which ruby works and all kind of programs
(GUI, WWW, library, etc), and becomes the hub of other i18n/l10n libs/apps to
handle major locale ID standards.

%package	doc
Summary:	Documentation for %{pkg_name}
Group:		Documentation
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description	doc
This package contains documentation for %{pkg_name}.

%package	-n %{?scl_prefix}ruby-%{gem_name}
Summary:	Non-Gem support package for %{gem_name}
Group:		Development/Languages
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}
Provides:	%{?scl_prefix}ruby(%{gem_name}) = %{version}-%{release}
%{?scl:Obsoletes: ruby193-ruby-%{gem_name}}

%description	-n %{?scl_prefix}ruby-%{gem_name}
This package provides non-Gem support for %{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

# rm -f .%{gem_instdir}/Rakefile
find . -name \*gem | xargs chmod 0644

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

# The following method is completely copied from rubygem-gettext
# spec file
#
# Create symlinks

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

%if 0%{?ruby19} < 1
#create_symlink_rec %{gem_instdir}/lib %{ruby_sitelib}
%endif

# Clean up unneeded files
rm -f %{buildroot}%{gem_instdir}/.yardopts

%check

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{gem_instdir}/
%doc %{gem_instdir}/[A-Z]*
%doc %{gem_instdir}/doc/
%exclude %{gem_instdir}/Rakefile
%{gem_instdir}/lib/
#%%{gem_instdir}/*.rb
%{gem_cache}
%{gem_spec}

%files doc
%defattr(-,root,root,-)
%{gem_docdir}/
%{gem_instdir}/samples/
%{gem_instdir}/test/
%{gem_instdir}/*.gemspec

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.0.9-15
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.9-14
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.9-13
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.9-12
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)
- Remove unused non-SCL awesome_print, locale gems (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 2.0.9-11
- Remove touch from prep to not touch root-owned files (dcleal@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 2.0.9-10
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 2.0.9-9
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)
- Add full rubygems.org source URL (dcleal@redhat.com)

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 2.0.9-8
- Modernise and update for EL7 (dcleal@redhat.com)

* Tue Mar 18 2014 Jason Montleon <jmontleo@redhat.com> 2.0.9-7
- new package built with tito

* Tue Mar 18 2014 Jason Montleon <jmontleo@redhat.com> 2.0.9-6
- further rpm spec file fixes (jmontleo@redhat.com)

* Tue Mar 18 2014 Jason Montleon <jmontleo@redhat.com> 2.0.9-5
- fix provides in rpm spec (jmontleo@redhat.com)

* Tue Mar 18 2014 Jason Montleon <jmontleo@redhat.com> 2.0.9-4
- more rpm spec file fixes (jmontleo@redhat.com)

* Tue Mar 18 2014 Jason Montleon <jmontleo@redhat.com> 2.0.9-3
- disable checks for now (jmontleo@redhat.com)

* Tue Mar 18 2014 Jason Montleon <jmontleo@redhat.com> 2.0.9-2
- fix (build)requires (jmontleo@redhat.com)

* Tue Mar 18 2014 Jason Montleon <jmontleo@redhat.com> 2.0.9-1
- make corrections to rpm spec file (jmontleo@redhat.com)

* Thu Sep 12 2013 Jason Montleon <jmontleo@redhat.com> 2.0.8-4
- new package built with tito

* Wed May 08 2013 Dominic Cleal <dcleal@redhat.com> 2.0.8-3
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Tue Mar 12 2013 Lukas Zapletal <lzap+git@redhat.com> 2.0.8-2
- new package built with tito

* Tue Sep 11 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.0.8-1
- 2.0.8

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.0.5-5
- Fix conditionals for F17 to work for RHEL 7 as well.

* Sun Jan 29 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.0.5-4
- F-17: rebuild against ruby 1.9

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 12 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- gems.rubyforge.org gem file seems old, changing Source0 URL for now

* Wed Nov 18 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.5-1
- 2.0.5
- Fix the license tag

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.4-2
- F-12: Mass rebuild

* Wed May 27 2009  Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.4-1
- 2.0.4

* Mon May 11 2009  Mamoru Tasaka <mtasaka@ios.s.u-tokyo.ac.jp> - 2.0.3-1
- 2.0.3

* Tue Apr 21 2009  Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.1-1
- 2.0.1

* Thu Mar 26 2009  Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.0-1
- Initial package
