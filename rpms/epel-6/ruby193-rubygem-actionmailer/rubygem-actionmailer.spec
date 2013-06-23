%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from actionmailer-1.3.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name actionmailer

%global rubyabi 1.9.1

Summary: Service layer for easy email delivery and testing
Name: %{?scl_prefix}rubygem-%{gem_name}
Epoch: 1
Version: 3.2.8
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: http://www.rubyonrails.org

Source0: http://rubygems.org/downloads/actionmailer-%{version}.gem

# Also the actionmailer gem doesn't ship with the test suite.
# You may check it out like so
# git clone http://github.com/rails/rails.git
# cd rails/actionmailer/
# git checkout v3.2.8
# tar czvf actionmailer-3.2.8-tests.tgz test/
Source2: actionmailer-%{version}-tests.tgz

# Let's keep Requires and BuildRequires sorted alphabeticaly
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(actionpack) = %{version}
Requires: %{?scl_prefix}rubygem(mail) >= 2.4.4
Requires: %{?scl_prefix}rubygem(mail) < 2.5
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(actionpack) = %{version}
BuildRequires: %{?scl_prefix}rubygem(mail) >= 2.4.4
BuildRequires: %{?scl_prefix}rubygem(mail) < 2.5
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(mocha)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Makes it trivial to test and deliver emails sent from a single service layer.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{epoch}:%{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            -V \
            --force --rdoc %{SOURCE0}
%{?scl:"}

# move the tests into place
tar xzvf %{SOURCE2} -C .%{gem_instdir}

# Remove backup files
find ./%{gem_instdir} -type f -name "*~" -delete

# Fix anything executable that does not have a shebang
for file in `find ./%{gem_instdir} -type f -perm /a+x`; do
    [ -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 644 $file
done

# Find files with a shebang that do not have executable permissions
for file in `find ./%{gem_instdir} -type f ! -perm /a+x -name "*.rb"`; do
    [ ! -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 755 $file
done


%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
export GEM_PATH="$(pwd)/%{gem_dir}:%{gem_dir}"
pushd .%{gem_instdir}

# load_path is not available, remove its require.
sed -i '8,+1d' test/abstract_unit.rb
%{?scl:scl enable %scl - << \EOF}
ruby -Itest -I. -e "Dir.glob('test/**/*_test.rb').each {|t| require t}"
%{?scl:EOF}
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
%{gem_instdir}/test

%changelog
* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 3.2.8-2
- new package built with tito

* Wed Sep 19 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.8-1
- Update to ActionMailer 3.2.8.

* Fri Jul 27 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.6-4
- Fixed the require in -doc subpackage.

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.6-3
- Imported from Fedora again.
- Specfile cleanup

* Tue Jul 24 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.6-2
- Fixed missing epoch in -doc subpackage.

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.6-1
- Update to ActionMailer 3.2.6.
- Don't run tests using Rakefile.
- Introduced -doc subpackage.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.15-1
- Update to ActionMailer 3.0.15.

* Fri Jun 01 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.13-1
- Update to ActionMailer 3.0.13.

* Wed May 09 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.11-2
- Fix Mailer dependencies.

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-1
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.10-1
- Update to ActionMailer 3.0.10

* Mon Jul 04 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.9-1
- Update to ActionMailer 3.0.9

* Thu Jun 02 2011 Mo Morsi <mmorsi@redhat.com> - 1:3.0.3-2
- bump rubygem-mail dependency version to that in Fedora

* Fri Mar 25 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.5-1
- Updated to ActionMailer 3.0.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-2
- Changed BuildRequires(check) to BuildRequires

* Mon Jan 10 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-1
- Update to rails 3

* Mon Aug 09 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-1
- Update to 2.3.8

* Thu Jan 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.5-1
- Update to 2.3.5

* Wed Oct  7 2009 David Lutterkort <lutter@redhat.com> - 1:2.3.4-2
- Bump Epoch to ensure upgrade path from F-11

* Mon Sep 7 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.4-1
- Update to 2.3.4

* Thu Aug 02 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 2.3.3-2
- Disable test

* Sun Aug  2 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.3-1
- 2.3.3
- Enable test

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 2.3.2-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 23 2008 David Lutterkort <lutter@redhat.com> - 2.2.2-1
- New version

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

* Thu Nov 29 2007 David Lutterkort <dlutter@redhat.com> - 1.3.6-1
- New version

* Tue Nov 14 2007 David Lutterkort <dlutter@redhat.com> - 1.3.5-2
- Fix buildroot
- Mark various things in geminstdir as doc

* Tue Oct 30 2007 David Lutterkort <dlutter@redhat.com> - 1.3.5-1
- Initial package
