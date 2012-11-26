# Upstream git:
# https://github.com/rubygems/rubygems.git
#
%global	gem_dir	%(ruby -rrbconfig -e 'puts File::expand_path(File::join(Config::CONFIG["sitedir"],"..","gems"))')
%global	rb_ver		%(ruby -rrbconfig -e 'puts Config::CONFIG["ruby_version"]')
%global	gem_home	%{gem_dir}/%{rb_ver}
%global	ruby_sitelib	%(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')

%global	repoid		75309

# Executing testsuite (enabling %%check section) will cause dependency loop.
# To avoid dependency loop when necessary, please set the following value to 0
%global	enable_check  0

Summary:	The Ruby standard for packaging ruby libraries
Name:		rubygems
Version:	1.8.10
Release:	1%{?dist}
Group:		Development/Libraries
License:	Ruby or MIT

URL:		http://rubyforge.org/projects/rubygems/
Source0:	http://rubyforge.org/frs/download.php/%{repoid}/rubygems-%{version}.tgz
Patch0:		rubygems-1.8.5-noarch-gemdir.patch
# Will discuss upstream
# https://github.com/rubygems/rubygems/issues/120
# rubygems-Patches-28631
Patch1:		rubygems-1.8.6-show-extension-build-process-in-sync.patch
# rubygems-Patches-29049
# https://github.com/rubygems/rubygems/issues/118
Patch3:		rubygems-1.8.5-show-rdoc-process-verbosely.patch
# Fix Gem.all_load_paths (although it is deprecated and will be removed
# on 2011-10-01)
Patch6:		rubygems-1.8.5-all-load-paths.patch

Requires:	ruby(abi) = 1.8
Requires:	ruby >= 1.8.7
Requires:	ruby-rdoc
BuildRequires:	ruby
BuildRequires:	ruby-rdoc
%if %{enable_check}
# For mkmf.rb
BuildRequires:	ruby-devel
BuildRequires:	rubygem(hoe)
BuildRequires:	rubygem(minitest)
BuildRequires:	rubygem(rake)
%endif
BuildArch:	noarch
Provides:	ruby(rubygems) = %{version}-%{release}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
RubyGems is the Ruby standard for publishing and managing third party
libraries.

%prep
%setup -q
%patch0 -p1 -b .noarch
%patch1 -p1 -b .insync
%patch3 -p1 -b .rdoc_v
%patch6 -p1 -b .load_path

# Some of the library files start with #! which rpmlint doesn't like
# and doesn't make much sense
for f in `find lib -name \*.rb` ; do
  head -1 $f | grep -q '^#!/usr/bin/env ruby' && sed -i -e '1d' $f
done

%build
# Nothing

%install
rm -rf $RPM_BUILD_ROOT
GEM_HOME=%{buildroot}/%{gem_home} \
    ruby setup.rb --prefix=%{_prefix} \
        --no-rdoc --no-ri \
        --destdir=%{buildroot}/%{ruby_sitelib}


mkdir -p %{buildroot}/%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{gem_home}/{cache,gems,specifications,doc}
mv %{buildroot}/%{ruby_sitelib}/usr/bin/gem %{buildroot}/%{_bindir}/gem
rm -rf %{buildroot}/%{ruby_sitelib}/bin
mv %{buildroot}/%{ruby_sitelib}/usr/lib/* %{buildroot}/%{ruby_sitelib}/.

%clean
rm -rf $RPM_BUILD_ROOT

%if %{enable_check}
%check
# Don't use isolate
sed -i.tmp -e '\@isolate@d' Rakefile
rake test
mv Rakefile.tmp Rakefile
%endif

%files
%defattr(-, root, root, -)
%doc README* 
#%%doc ChangeLog
%doc History.txt
%doc MIT.txt LICENSE.txt
%dir %{gem_dir}
%dir %{gem_home}
%dir %{gem_home}/cache
%dir %{gem_home}/gems
%dir %{gem_home}/specifications
%doc %{gem_home}/doc
%{_bindir}/gem

%dir %{ruby_sitelib}/
%{ruby_sitelib}/gauntlet_rubygems.rb
#%{ruby_sitelib}/lib
%{ruby_sitelib}/rbconfig/
%{ruby_sitelib}/rubygems/
%{ruby_sitelib}/rubygems.rb
%{ruby_sitelib}/ubygems.rb

%changelog
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
