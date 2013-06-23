%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from activerecord-1.15.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name activerecord
%global rubyabi 1.9.1

Summary: Implements the ActiveRecord pattern for ORM
Name: %{?scl_prefix}rubygem-%{gem_name}
Epoch: 1
Version: 3.2.8
Release: 12%{?dist}
Group: Development/Languages
License: MIT
URL: http://www.rubyonrails.org
Source0: http://rubygems.org/downloads/activerecord-%{version}.gem
# git clone http://github.com/rails/rails.git
# cd rails/activerecord/
# git checkout v3.2.8
# tar czvf activerecord-3.2.8-tests.tgz test/
Source1: activerecord-%{version}-tests.tgz

# CVE-2012-6496
# https://bugzilla.redhat.com/show_bug.cgi?id=891470
# https://bugzilla.redhat.com/show_bug.cgi?id=891471
Patch0: rubygem-activerecord-3.2.10-CVE-2012-6496-dynamic_finder_injection.patch
# CVE-2013-0155
# https://bugzilla.redhat.com/show_bug.cgi?id=892866
Patch1: rubygem-activerecord-3.2.11-CVE-2013-0155-null_array_param.patch
# Searching in the Templates page in Foreman raises a DB stack trace
# https://bugzilla.redhat.com/show_bug.cgi?id=963295
Patch2: rubygem-activerecord-3.2.9-rhbz963295-nulls-first-last.patch

Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(activesupport) = %{version}
Requires: %{?scl_prefix}rubygem(activemodel)   = %{version}
Requires: %{?scl_prefix}rubygem(arel) 
Requires: %{?scl_prefix}rubygem(tzinfo) >= 0.3.23
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(bcrypt-ruby)
BuildRequires: %{?scl_prefix}rubygem(activesupport) = %{version}
BuildRequires: %{?scl_prefix}rubygem(activemodel)   = %{version}
BuildRequires: %{?scl_prefix}rubygem(sqlite3)
BuildRequires: %{?scl_prefix}rubygem(erubis)
BuildRequires: %{?scl_prefix}rubygem(mocha)
BuildRequires: %{?scl_prefix}rubygem(arel)
BuildRequires: %{?scl_prefix}rubygem(tzinfo) >= 0.3.23
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Implements the ActiveRecord pattern (Fowler, PoEAA) for ORM. It ties database
tables and classes together for business objects, like Customer or
Subscription, that can find, save, and destroy themselves without resorting to
manual SQL.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

pushd .%{gem_instdir}
%patch0 -p2
%patch1 -p2
%patch2 -p2
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

%check
pushd .%{gem_instdir}

tar xzvf %{SOURCE1}

# load_path is not available, remove its require.
sed -i '1,2d' test/cases/helper.rb

%{?scl:scl enable %scl - << \FOE}
#ruby -I.:test:lib << EOF
#  test_files = Dir.glob( "test/cases/**/*_test.rb" )
#  test_files.reject! { |x| x =~ %r|/adapters/| }
#
#  # Only test sqlite3 backend
#  test_files += Dir.glob("test/cases/adapters/sqlite3/*_test.rb")
#
#  # To prevent a circular dependency w/ actionpack.
#  test_files.delete('test/cases/session_store/session_test.rb')
#
#  # Test dependes on mysql adapter
#  # https://github.com/rails/rails/issues/7103
#  test_files.delete('test/cases/connection_specification/resolver_test.rb')
#
#  test_files.each { |f| require f }
#EOF
%{?scl:FOE}

popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/MIT-LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/examples

%changelog
* Fri May 31 2013 Lukas Zapletal <lzap+git@redhat.com> 3.2.8-12
- removing test from #963295 backport

* Fri May 31 2013 Lukas Zapletal <lzap+git@redhat.com> 3.2.8-11
- adding missing tito.props

* Fri May 31 2013 Lukas Zapletal <lzap+git@redhat.com> 3.2.8-10
- RHBZ#963295 - backporting NULLS FIRST/LAST pgsql parsing

* Fri May 10 2013 Sam Kottler <shk@redhat.com> 3.2.8-9
- new package built with tito

* Wed May 08 2013 Bryan Kearney <bkearney@redhat.com> 3.2.8-8
- new package built with tito

* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 3.2.8-6
- disable tests (msuchy@redhat.com)

* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 3.2.8-5
- disable tests (msuchy@redhat.com)

* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 3.2.8-4
- new package built with tito

* Mon Jan 14 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.8-3
- Fix for CVE-2013-0155.

* Mon Jan 07 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.8-2
- Fix for CVE-2012-6496.

* Tue Sep 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.8-1
- Update to ActiveRecord 3.2.8.

* Fri Jul 27 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.6-4
- Fixed the Require in -doc subpackage.

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.6-3
- Imported from Fedora again.

* Tue Jul 24 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.6-2
- Fixed missing epoch in -doc subpackage.

* Thu Jul 19 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.6-1
- Update to ActiveRecord 3.2.6.

* Fri Jun 15 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.15-1
- Update to ActiveRecord 3.0.15.

* Fri Jun 01 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.13-1
- Update to ActiveRecord 3.0.13.

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-1
- Rebuilt for Ruby 1.9.3.
- Update to ActionRecord 3.0.11

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.10-1
- Update to ActiveRecord 3.0.10

* Mon Jul 04 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.9-1
- Update to ActiveRecord 3.0.9

* Fri Mar 25 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.5-1
- Updated to ActiveRecord 3.0.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-1
- Update to rails 3

* Wed Sep 08 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-4
- Updated postgres fix to resolve security issue

* Mon Aug 16 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-3
- Included postgres fix (patch also pushed upstream, see rails issue tracker)

* Thu Aug 12 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-2
- Updated patch0 to correctly parse sqlite3 version

* Wed Aug 04 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-1
- Update to 2.3.8

* Thu Jan 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.5-1
- Update to 2.3.5

* Wed Oct  7 2009 David Lutterkort <lutter@redhat.com> - 1:2.3.4-2
- Bump Epoch to ensure upgrade path from F-11

* Fri Sep 18 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.4-1
- Update to 2.3.4
- Enable check

* Sun Jul 26 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 2.3.3-1
- New upstream version

* Mon Mar 16 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 2.3.2-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 2.2.2-1
- New upstream version
- Fixed rpmlint errors zero-length files and script-without-shebang

* Thu Nov 20 2008 David Lutterkort <lutter@redhat.com> - 2.1.1-2
- Do not mark lib/ as doc

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 2.1.1-1
- New version (fixes CVE-2008-4094)

* Thu Jul 31 2008 Michael Stahnke <stahnma@fedoraproject.org> - 2.1.0-1
- New Upstream

* Tue Apr  8 2008 David Lutterkort <dlutter@redhat.com> - 2.0.2-2
- Fix dependency

* Mon Apr 07 2008 David Lutterkort <dlutter@redhat.com> - 2.0.2-1
- New version

* Mon Dec 10 2007 David Lutterkort <dlutter@redhat.com> - 2.0.1-1
- New version

* Thu Nov 29 2007 David Lutterkort <dlutter@redhat.com> - 1.15.6-1
- New version

* Tue Nov 14 2007 David Lutterkort <dlutter@redhat.com> - 1.15.5-2
- Fix buildroot
- Properly mark docs in geminstdir

* Tue Oct 30 2007 David Lutterkort <dlutter@redhat.com> - 1.15.5-1
- Initial package
