# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name gettext

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.1.4
Release: 11%{?dist}
Summary: Gettext is a pure Ruby libary and tools to localize messages
Group: Development/Languages
License: Ruby or LGPLv3+
URL: http://ruby-gettext.github.com/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby 
Requires: %{?scl_prefix_ruby}ruby(rubygems) 
Requires: %{?scl_prefix}rubygem(locale) >= 2.0.5
Requires: %{?scl_prefix}rubygem(text) 
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby 
BuildRequires: %{?scl_prefix_ruby}rubygems-devel 
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Gettext is a GNU gettext-like program for Ruby.
The catalog file(po-file) is same format with GNU gettext.
So you can use GNU gettext tools for maintaining.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/rmsgcat
%{_bindir}/rmsgmerge
%{_bindir}/rxgettext
%{_bindir}/rmsgfmt
%{_bindir}/rmsginit
%exclude %{gem_instdir}/.yardopts
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/locale
%{gem_instdir}/src
%exclude %{gem_instdir}/po
%exclude %{gem_instdir}/samples
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%{gem_instdir}/gettext.gemspec
%{gem_instdir}/test

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.1.4-11
- Rebuild against rh-ruby27

* Tue Apr 14 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.1.4-10
- Remove the po and samples folder from the RPM.

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.1.4-9
- Change the spec to be more inline with the gem2rpm template.

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.1.4-8
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.1.4-7
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 3.1.4-6
- Replace shebangs to remove deps on non-SCL Ruby (dcleal@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 3.1.4-5
- Remove touch from prep to not touch root-owned files (dcleal@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 3.1.4-4
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 3.1.4-3
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Nov 24 2014 Dominic Cleal <dcleal@redhat.com> 3.1.4-2
- Disable tests, fix find-lang.sh and _bindir on EL6, fix SCL redirection
  (dcleal@redhat.com)

* Sun Aug 31 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.4-1
- 3.1.4

* Fri Aug  1 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.3-1
- 3.1.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May  4 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.2-1
- 3.1.2

* Thu Feb 27 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.1-1
- 3.1.1

* Mon Feb 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-1
- 3.1.0

* Mon Feb  3 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.6-1
- 3.0.6

* Tue Dec 24 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.3-1
- 3.0.3

* Tue Oct 15 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.2-6
- Patch from upstream git to remove memoization with
  coordination with rubygem-locale side change
- Patch from upstream git to fix test failure on arm

* Fri Oct 11 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.2-4
- Make test failure conditional

* Thu Oct 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.2-2
- F-21: rescue test failure for now

* Thu Oct 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.2-1
- 3.0.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.8-1
- 2.3.8

* Wed Feb 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.7-4
- Kill unneeded iconv call

* Wed Feb 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.7-3
- F-19: Rebuild for ruby 2.0.0
- F-19: Use GLib's iconv instead of iconv removed from ruby core

* Sun Feb 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.7-2
- Require levenshtein for fuzzy merging

* Thu Jan 24 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.7-1
- 2.3.7

* Wed Jan  2 2013 Mamoru TASAKA <mtasaka@fedoraproject.org>  - 2.3.6-1
- 2.3.6

* Wed Jan  2 2013 Mamoru TASAKA <mtasaka@fedoraproject.org>  - 2.2.1-3
- Clean up old stuff

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 30 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.2.1-1
- 2.2.1

* Sat Apr  7 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.2.0-2
- Fix test case

* Sat Apr  7 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.2.0-1
- 2.2.0

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.1.0-7
- Fix conditionals for F17 to work for RHEL 7 as well.

* Sun Jan 29 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.1.0-6
- F-17: rebuild against ruby 1.9

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jun 25 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.1.0-4
- Rescue Gem.all_load_paths when it is removed from rubygems

* Mon Feb 14 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.0-3
- F-15 mass rebuild

* Tue Jan 12 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- gems.rubyforge.org gem file seems old, changing Source0 URL for now

* Wed Nov 18 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.0-1
- 2.1.0

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.4-2
- F-12: Mass rebuild

* Thu May 28 2009 Mamoru Tasaka <mtasaka@ios.s.u-tokyo.ac.jp> - 2.0.4-1
- 2.0.4

* Mon May 11 2009 Mamoru Tasaka <mtasaka@ios.s.u-tokyo.ac.jp> - 2.0.3-2
- 2.0.3
- Add "BR: gettext" (not to Requires) for rake test

* Fri May  1 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.1-3
- Mark LICENSE etc as %%doc

* Wed Apr 22 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.1-2
- Bump ruby-locale Requires version

* Tue Apr 21 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.1-1
- 2.0.1, drop patches already in upstream (all)

* Sun Mar 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.0-1
- Update to 2.0.0
- Now require rubygem(locale)
- Rescue NoMethodError on gem call on gettext.rb
- Reintroduce 4 args bindtextdomain() compatibility

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.93.0-8
- %%global-ize "nested" macro

* Thu Oct 23 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.93.0-7
- Handle gettext .mo files under %%{gem_instdir}/data/locale by
  modifying find-lang.sh

* Tue Oct  7 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.93.0-6
- Move sed edit section for lib/ files from %%install to %%build
  stage for cached gem file

* Tue Oct  7 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.93.0-5
- Recreate gettext .mo files (by using this itself)

* Mon Oct  6 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.93.0-3
- Some modification for spec file by Scott

* Tue Sep 23 2008 Scott Seago <sseago@redhat.com> - 1.93.0-2
- Initial package (of rubygem-gettext)
  Set at release 2 to supercede ruby-gettext-package-1.93.0-1

* Thu Sep 18 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.93.0-1
- 1.93.0

* Sat Aug  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.92.0-1
- 1.92.0

* Thu May 22 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.91.0-1
- 1.91.0

* Sun Feb  3 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.90.0-1
- 1.90.0
- Arch changed to noarch

* Wed Aug 29 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.10.0-1
- 1.10.0

* Wed Aug 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.0-2.dist.2
- Mass rebuild (buildID or binutils issue)

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.0-2.dist.1
- License update

* Mon May  7 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.0-2
- Create -doc subpackage

* Sat Apr 21 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.9.0-1
- Initial packaging
