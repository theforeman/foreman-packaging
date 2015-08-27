%{?scl:%scl_package rubygem-%{gemname}}
%{!?scl:%global pkg_name %{name}}

%global	mainver		1.6.6.2
#%%global	prever			.beta.4

%global	mainrel		1
%global	prerpmver		%(echo "%{?prever}" | sed -e 's|\\.||g')

%global	gemdir			%(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global	gemname		nokogiri
%global	geminstdir		%{gemdir}/gems/%{gemname}-%{mainver}%{?prever}

%global	ruby19		1
%global	rubyabi		1.9.1
%global	gemdir		%{gem_dir}
%global	geminstdir	%{gem_instdir}
%if 0%{?fedora}
%global	gemsodir	%{gem_extdir_mri}/lib
%else
%global	gemsodir	%{gem_extdir}/lib
%endif
%global	gem_name	%{gemname}

# Note for packager:
# Nokogiri 1.4.3.1 gem says that Nokogiri upstream will
# no longer support ruby 1.8.6 after 2010-08-01, so
# it seems that 1.4.3.1 is the last version for F-13 and below.

Summary:	An HTML, XML, SAX, and Reader parser
Name:		%{?scl_prefix}rubygem-%{gemname}
Version:	%{mainver}
Release:  1%{?dist}
Group:		Development/Languages
License:	MIT
URL:		http://nokogiri.rubyforge.org/nokogiri/
Source0:	http://rubygems.org/gems/%{gemname}-%{mainver}.gem
# ./test/html/test_element_description.rb:62 fails, as usual......
# Patch0:		rubygem-nokogiri-1.5.0.beta3-test-failure.patch
#Patch0:		rubygem-nokogiri-1.5.0-allow-non-crosscompile.patch
%if 0%{?fedora} >= 19
Requires:	%{?scl_prefix_ruby}ruby(release)
BuildRequires:	%{?scl_prefix_ruby}ruby(release)
%else
Requires:	%{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
BuildRequires:	%{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
%endif
BuildRequires:	%{?scl_prefix_ruby}ruby(rubygems)
##
## For %%check
BuildRequires:	%{?scl_prefix_ruby}rubygem(minitest)
BuildRequires:	%{?scl_prefix_ruby}rubygems-devel
%if 0%{?ruby19} > 0
Obsoletes:		%{?scl_prefix}ruby-%{gemname} <= 1.5.2-2
%endif
#BuildRequires:	%{?scl_prefix}ruby(racc)
##
## Others
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	%{?scl_prefix_ruby}ruby-devel
Requires:	%{?scl_prefix_ruby}ruby(rubygems)
Provides:	%{?scl_prefix}rubygem(%{gemname}) = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gemname}}

%description
Nokogiri parses and searches XML/HTML very quickly, and also has
correctly implemented CSS3 selector support as well as XPath support.

Nokogiri also features an Hpricot compatibility layer to help ease the change
to using correct CSS and XPath.

%if 0
%package	jruby
Summary:	JRuby support for %{pkg_name}
Group:		Development/Languages
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description	jruby
This package contains JRuby support for %{pkg_name}.
%endif


%package	doc
Summary:	Documentation for %{pkg_name}
Group:		Documentation
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gemname}-doc}

%description	doc
This package contains documentation for %{pkg_name}.

%package	-n %{?scl_prefix}ruby-%{gemname}
Summary:	Non-Gem support package for %{gemname}
Group:		Development/Languages
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}
Provides:	%{?scl_prefix}ruby(%{gemname}) = %{version}-%{release}
%{?scl:Obsoletes: ruby193-ruby-%{gemname}}

%description	-n %{?scl_prefix}ruby-%{gemname}
This package provides non-Gem support for %{gemname}.

%prep
%setup -n %{pkg_name}-%{version} -q -T -c

# Gem repack
TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
cd %{gem_name}-%{version}

# patches
#%%patch0 -p1

%{?scl:scl enable %{scl} "}
gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec
%{?scl:"}

# remove bundled external libraries
sed -i \
   -e 's|, "ports/archives/[^"][^"]*"||g' \
   -e 's|, "ports/patches/[^"][^"]*"||g' \
   %{gem_name}.gemspec
# Actually not needed when using system libraries
sed -i -e '\@mini_portile@d' %{gem_name}.gemspec

# Ummm...
%{?scl:scl enable %{scl} "}
env LANG=ja_JP.UTF-8 gem build %{gem_name}.gemspec
%{?scl:"}
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
mkdir -p ./%{gemdir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
# 1.6.0 needs this
export NOKOGIRI_USE_SYSTEM_LIBRARIES=yes
%{?scl:scl enable %{scl} "}
gem install \
	--local \
	--install-dir ./%{gemdir} \
	-V --force \
	%{gem_name}-%{version}.gem
%{?scl:"}


# Permission
chmod 0644 .%{gemdir}/cache/%{gemname}-%{mainver}%{?prever}.gem

# Remove precompiled Java .jar file
rm -f .%{geminstdir}/lib/*.jar
# For now remove JRuby support
rm -rf .%{geminstdir}/ext/java


%install
mkdir -p %{buildroot}%{gemdir}
cp -a ./%{gemdir}/* %{buildroot}%{gemdir}

# Remove backup file
find %{buildroot} -name \*.orig_\* | xargs rm -vf

# move arch dependent files to %%gem_extdir
mkdir -p %{buildroot}%{gemsodir}/%{gemname}
mv %{buildroot}%{geminstdir}/lib/%{gemname}/*.so \
	%{buildroot}%{gemsodir}/%{gemname}/

# move bin/ files
mkdir -p %{buildroot}%{_prefix}
mv -f %{buildroot}%{gemdir}/bin %{buildroot}%{_prefix}

# remove all shebang
for f in $(find %{buildroot}%{geminstdir} -name \*.rb)
do
	sed -i -e '/^#!/d' $f
	chmod 0644 $f
done

# cleanups
rm -rf %{buildroot}%{geminstdir}/ext/%{gemname}/
rm -rf %{buildroot}%{geminstdir}/tmp/
rm -f %{buildroot}%{geminstdir}/{.autotest,.require_paths,.gemtest,.travis.yml}
rm -f %{buildroot}%{geminstdir}/.cross_rubies
rm -f %{buildroot}%{geminstdir}/{build_all,dependencies.yml,test_all}
rm -f %{buildroot}%{geminstdir}/.editorconfig
rm -rf %{buildroot}%{geminstdir}/suppressions/

%check
# Ah....
# test_exslt(TestXsltTransforms) [./test/test_xslt_transforms.rb:93]
# fails without TZ on sparc
export TZ="Asia/Tokyo"
#???
%if 0%{?ruby19} > 0
LANG=ja_JP.UTF-8
%endif

pushd ./%{geminstdir}
# Need investigation. For now anyway build
%{?scl:scl enable %{scl} - << \EOF}
ruby -I.:lib:test \
	-e \
	"require 'minitest/autorun' ; Dir.glob('test/**/test_*.rb'){|f| require f}" || \
	echo "Please investigate this"
%{?scl:EOF}

for f in $SKIPTEST
do
	mv $f.skip $f
done

popd

%files
%defattr(-,root, root,-)
%{_bindir}/%{gemname}
%if 0%{?ruby19} < 1
%{ruby_sitearch}/%{gemname}
%else
%{gemsodir}/
%endif
%dir	%{geminstdir}/
%doc	%{geminstdir}/[A-Z]*
#%%doc	%{geminstdir}/nokogiri_help_responses.md
%exclude %{geminstdir}/Rakefile
%exclude %{geminstdir}/Gemfile
%{geminstdir}/bin/
%{geminstdir}/lib/
%{gemdir}/cache/%{gemname}-%{mainver}%{?prever}.gem
%{gemdir}/specifications/%{gemname}-%{mainver}%{?prever}.gemspec

%if 0
%files	jruby
%defattr(-,root,root,-)
%{geminstdir}/ext/java/
%endif

%files	doc
%defattr(-,root,root,-)
%{geminstdir}/Rakefile
#%%{geminstdir}/deps.rip
#%%{geminstdir}/spec/
%{geminstdir}/tasks/
%{geminstdir}/test/
%{gemdir}/doc/%{gemname}-%{mainver}%{?prever}/

%if 0%{?ruby19} < 1
%files	-n %{?scl_prefix}ruby-%{gemname}
%defattr(-,root,root,-)
%{ruby_sitelib}/*%{gemname}.rb
%{ruby_sitelib}/%{gemname}/
%{ruby_sitelib}/xsd/
%endif

%changelog
* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 1.6.6.2-1
- Update nokogiri to 1.6.6.2 (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.5.11-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Mar 11 2014 Dominic Cleal <dcleal@redhat.com> 1.5.11-1
- Update to v1.5.11 (dcleal@redhat.com)

* Fri Feb 21 2014 Jason Montleon <jmontleo@redhat.com> 1.5.6-9
- additional work for moving gem build to %%build (jmontleo@redhat.com)
- gem build to %%build to adhere to packaging guidelines (jmontleo@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Fri Mar 08 2013 Lukas Zapletal <lzap+git@redhat.com> 1.5.6-7
- fixing ruby193 scl package (lzap+git@redhat.com)

* Fri Mar 08 2013 Lukas Zapletal <lzap+git@redhat.com> 1.5.6-6
- fixing ruby193 scl package (lzap+git@redhat.com)

* Fri Mar 08 2013 Lukas Zapletal <lzap+git@redhat.com> 1.5.6-5
- fixing ruby193 scl package (lzap+git@redhat.com)
- fixing ruby193 scl package (lzap+git@redhat.com)

* Thu Mar 07 2013 Lukas Zapletal <lzap+git@redhat.com> 1.5.6-1.2
- fixing ruby193 scl package (lzap+git@redhat.com)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan  1 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.5.6-1
- A Happy New Year
- 1.5.6

* Fri Aug 17 2012 Vít Ondruch <vondruch@redhat.com> - 1.5.5-2
- Rebuilt againts libxml2 2.9.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.5-1
- 1.5.5

* Mon May 28 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.2-3
- Fix Obsoletes (bug 822931)

* Mon Apr  9 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.2-1
- 1.5.2

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.5.0-3
- Fix conditionals for F17 to work for RHEL 7 as well.

* Tue Jan 24 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.0-2
- F-17: rebuild for ruby19
- For now aviod build failure by touching some files

* Thu Jan 18 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.0-1
- 1.5.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.5.beta4.1
- F-17: Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.0-0.5.beta4
- Remove unneeded patch

* Thu Mar 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.0-0.4.beta4
- Patch for newer rake to make testsuite run

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.3.beta4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0-0.3.beta4
- 1.5.0.beta.4

* Tue Dec  7 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0-0.2.beta3
- 1.5.0.beta.3

* Sun Oct 17 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0-0.1.beta2
- Try 1.5.0.beta.2

* Fri Jul 30 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.3.1-1
- 1.4.3.1

* Wed May 26 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.2-1
- 1.4.2

* Thu Apr 29 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.1-2
- Fix build failure with libxml2 >= 2.7.7

* Tue Dec 15 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.1-1
- 1.4.1

* Mon Nov  9 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.0-1
- 1.4.0

* Sat Aug 22 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.3-2
- Fix test failure on sparc

* Wed Jul 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.3-1
- 1.3.3

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.2-3
- F-12: Mass rebuild

* Thu Jul  2 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.2-2
- Enable test
- Recompile with -O2

* Thu Jun 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.2-1
- 1.3.2

* Thu Jun 11 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.1-1
- 1.3.1

* Thu Mar 26 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.3-1
- 1.2.3

* Thu Mar 19 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.2-1
- 1.2.2

* Thu Mar 12 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.1-1
- 1.2.1

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.1-2
- F-11: Mass rebuild

* Thu Jan 15 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.1-1
- 1.1.1

* Thu Dec 25 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.0-1
- Initial packaging
