# template: default
%global gem_name pg
%global gem_require_name %{gem_name}

Name: rubygem-%{gem_name}
Version: 1.6.1
Release: 1%{?dist}
Summary: Pg is the Ruby interface to the PostgreSQL RDBMS
# Upstream license clarification (https://bitbucket.org/ged/ruby-pg/issue/72/)
#
# The portions of the code that are BSD-licensed are licensed under
# the BSD 3-Clause license; the contents of the BSD file are incorrect.
#
License: (GPLv2 or Ruby) and PostgreSQL
URL: https://github.com/ged/ruby-pg
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.7
BuildRequires: ruby-devel >= 2.7
BuildRequires: rubygems-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
# end specfile generated dependencies

BuildRequires: postgresql-devel
BuildRequires: rubygem(bigdecimal)

%description
Pg is the Ruby interface to the PostgreSQL RDBMS. It works with PostgreSQL 9.3
and later.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
# Ideally, this would be something like this:
# GEM_PATH="%{buildroot}%{gem_dir}:$GEM_PATH" ruby -e "require '%{gem_require_name}'"
# But that fails to find native extensions on EL8, so we fake the structure that ruby expects
mkdir gem_ext_test
cp -a %{buildroot}%{gem_dir} gem_ext_test/
mkdir -p gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
cp -a %{buildroot}%{gem_extdir_mri} gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
GEM_PATH="./gem_ext_test/gems:$GEM_PATH" ruby -e "require '%{gem_require_name}'"
rm -rf gem_ext_test

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/BSDL
%license %{gem_instdir}/LICENSE
%license %{gem_instdir}/POSTGRES
%exclude %{gem_instdir}/certs
%{gem_libdir}
%exclude %{gem_instdir}/misc
%exclude %{gem_instdir}/ports
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Contributors.rdoc
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README-OS_X.rdoc
%doc %{gem_instdir}/README-Windows.rdoc
%doc %{gem_instdir}/README.ja.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/rakelib
%{gem_instdir}/sample
%exclude %{gem_instdir}/pg.gemspec

%changelog
* Wed Aug 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 1.6.1-1
- Update to 1.6.1

* Sun Oct 27 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.5.9-1
- Update to 1.5.9

* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.5.8-1
- Update to 1.5.8

* Sun Aug 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.5.7-1
- Update to 1.5.7

* Sun Mar 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.5.6-1
- Update to 1.5.6

* Sun Sep 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.5.4-1
- Update to 1.5.4

* Fri May 05 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.5.3-1
- Update to 1.5.3

* Sun Apr 30 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.5.2-1
- Update to 1.5.2

* Mon Mar 06 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.4.6-1
- Update to 1.4.6

* Tue Nov 22 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.4.5-1
- Update to 1.4.5

* Sun Oct 16 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.4.4-1
- Update to 1.4.4

* Tue Aug 16 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.4.3-1
- Update to 1.4.3

* Sun Jul 31 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.4.2-1
- Update to 1.4.2

* Tue Jul 26 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.4.1-1
- Update to 1.4.1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.1.4-4
- Rebuild against rh-ruby27

* Thu Apr 16 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.1.4-3
- Add check section to test native library

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.1.4-2
- Bump to release for EL8

* Mon Dec 02 2019 Evgeni Golov 1.1.4-1
- Update to 1.1.4-1

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.21.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 0.21.0-2
- Remove tests and rspec from pg (ericdhelms@gmail.com)

* Thu Jan 04 2018 Daniel Lobato Garcia <me@daniellobato.me> 0.21.0-1
- Update pg to 0.21 (eric.d.helms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.15.1-3
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 0.15.1-2
- Replace shebangs to remove deps on non-SCL Ruby (dcleal@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.15.1-1
- Update pg to 0.15.1 (dcleal@redhat.com)
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Fix build errors and modernise spec (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.12.2-9
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Mar 06 2013 Lukas Zapletal <lzap+git@redhat.com> 0.12.2-8
- disabling tests for ruby193-rubygem-pg

* Wed Mar 06 2013 Lukas Zapletal <lzap+git@redhat.com> 0.12.2-7
- importing rspec for pg

* Wed Mar 06 2013 Lukas Zapletal <lzap+git@redhat.com> 0.12.2-6
- new package built with tito

* Wed Mar 06 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.12.2-5
- rebuilt with prefix

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 07 2012 Vít Ondruch <vondruch@redhat.com> - 0.12.2-2
- Obsolete ruby-postgress, which was retired.

* Tue Jan 24 2012 Vít Ondruch <vondruch@redhat.com> - 0.12.2-1
- Rebuilt for Ruby 1.9.3.
- Upgrade to pg 0.12.2.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 03 2011 Vít Ondruch <vondruch@redhat.com> - 0.11.0-5
- Pass CFLAGS to extconf.rb.

* Fri Jun 03 2011 Vít Ondruch <vondruch@redhat.com> - 0.11.0-4
- Binary extension moved into ruby_sitearch dir.
- -doc subpackage made architecture independent.

* Wed Jun 01 2011 Vít Ondruch <vondruch@redhat.com> - 0.11.0-3
- Quoted upstream license clarification.

* Mon May 30 2011 Vít Ondruch <vondruch@redhat.com> - 0.11.0-2
- Removed/fixed shebang in non-executables.
- Removed sources.

* Thu May 26 2011 Vít Ondruch <vondruch@redhat.com> - 0.11.0-1
- Initial package
