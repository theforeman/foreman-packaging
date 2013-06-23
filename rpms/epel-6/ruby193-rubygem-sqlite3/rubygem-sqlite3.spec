%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name sqlite3

Summary:        Allows Ruby scripts to interface with a SQLite3 database
Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        1.3.6
Release:        2%{?dist}
Group:          Development/Languages
License:        BSD
# It is not clear what is the official homepage. However, I have risen ticket
# on upstream: https://github.com/luislavena/sqlite3-ruby/issues/issue/26
URL:            http://sqlite-ruby.rubyforge.org/
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:       %{?scl_prefix}ruby(rubygems)
Requires:       %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires:  %{?scl_prefix}rubygems-devel
BuildRequires:  %{?scl_prefix}ruby-devel
BuildRequires:  sqlite-devel
BuildRequires:  %{?scl_prefix}rubygem(rake)
BuildRequires:	%{?scl_prefix}rubygem(minitest)
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}

%description
SQLite3/Ruby is a module to allow Ruby scripts to interface with a SQLite3
database.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -q -c -T
mkdir -p ./%{gem_dir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%{?scl:scl enable %scl "}
gem install \
        --local \
        --install-dir ./%{gem_dir} \
        -V --force \
        %{SOURCE0}
%{?scl:"}

# Permission
find . -name \*.rb -or -name \*.gem | xargs chmod 0644

%build

%install
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{gem_extdir}/lib/sqlite3
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mv %{buildroot}%{gem_libdir}/sqlite3/sqlite3_native.so %{buildroot}%{gem_extdir}/lib/sqlite3

%check
pushd .%{gem_instdir}
%{?scl:scl enable %scl "}
testrb -Ilib test/test_*.rb
%{?scl:"}
popd

%files
%{gem_extdir}
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gemtest
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/ext
%{gem_libdir}/
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/API_CHANGES.rdoc
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/ChangeLog.cvs
%doc %{gem_instdir}/Manifest.txt
%{gem_instdir}/Rakefile
%{gem_instdir}/setup.rb
%doc %{gem_docdir}
%doc %{gem_instdir}/faq/
%{gem_instdir}/tasks/
%{gem_instdir}/test/


%changelog
* Fri Feb 22 2013 Miroslav Suchý <msuchy@redhat.com> 1.3.6-2
- new package built with tito

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.6-1
- Update to Sqlite3 1.3.6.
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.5-1
- Rebuilt for scl.
- Updated to 1.3.5.

* Thu Jan 19 2012 Vít Ondruch <vondruch@redhat.com> - 1.3.4-3
- Rebuilt for Ruby 1.9.3.
- Drop ruby-sqlite3 subpackage.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 20 2011 Vít Ondruch <vondruch@redhat.com> - 1.3.4-1
- Updated to sqlite3 1.3.4.
- Use the upstream big endian fix.

* Wed Jun 22 2011 Dan Horák <dan[at]danny.cz> - 1.3.3-5
- fix build on big endian arches (patch by Vít Ondruch)

* Fri Jun 03 2011 Vít Ondruch <vondruch@redhat.com> - 1.3.3-4
- The subdirectory of ruby_sitearch has to be owned by package.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Vít Ondruch <vondruch@redhat.com> - 1.3.3-2
- Updated links.
- Removed obsolete BuildRoot.
- Removed unnecessary cleanup.

* Wed Feb 02 2011 Vít Ondruch <vondruch@redhat.com> - 1.3.3-1
- Package renamed from rubygem-sqlite3-ruby to rubygem-sqlite3.
- Test suite executed upon build.
- Documentation moved into separate package.
- Removed clean section which is not necessary.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.4-4
- F-12: Rebuild to create valid debuginfo rpm again (ref: #505774)

* Tue Jun 16 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.4-3
- Create ruby-sqlite3 as subpackage (ref: #472621, #472622)
- Use gem as source

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 13 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.2.4-1
- Fix items from review (#459881)
- New upstream version

* Sun Aug 31 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.2.2-2
- Fix items from review (#459881)

* Sun Jul 13 2008 Matt Hicks <mhicks@localhost.localdomain> - 1.2.2-1
- Initial package
