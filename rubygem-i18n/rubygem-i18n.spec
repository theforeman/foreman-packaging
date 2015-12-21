%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name i18n

Summary: New wave Internationalization support for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.7.0
Release: 2%{?dist}
Group: Development/Languages
License: MIT and (BSD or Ruby)
URL: http://github.com/svenfuchs/i18n
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fixes Ruby 2.2 test failures related to frozen objects.
# https://github.com/svenfuchs/i18n/pull/305
Patch0: rubygem-i18n-0.7.0-Ignore-metadata-for-frozen-classes.patch
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires: %{?scl_prefix_ror}rubygem(mocha)
BuildRequires: %{?scl_prefix_ror}rubygem(test_declarative)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Ruby Internationalization and localization solution.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}
%setup -q -D -T -n %{gem_name}-%{version}
%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%patch0 -p1

%build
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}

# Bundler just complicates everything in our case, remove it.
sed -i -e "/require 'bundler\/setup'/ s/^/#/" test/test_helper.rb

# Tests are failing without LANG environment is set.
# https://github.com/svenfuchs/i18n/issues/115
%{?scl:scl enable %{scl} - << \EOF}
LANG=en_US.utf8 ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/MIT-LICENSE
%{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/test
%{gem_instdir}/gemfiles
%doc %{gem_docdir}

%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 20 2015 Vít Ondruch <vondruch@redhat.com> - 0.7.0-1
- Update to i18n 0.7.0.

* Tue Jul 22 2014 Josef Stribny <jstribny@redhat.com> - 0.6.11-1
- Update to i18n 0.6.11

* Wed Jun 18 2014 Josef Stribny <jstribny@redhat.com> - 0.6.9-4
- Fix test suite compatibility with minitest 5

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 04 2014 Josef Stribny <jstribny@redhat.com> - 0.6.9-2
- Fix license: Ruby is now licensed under BSD or Ruby

* Mon Dec 09 2013 Vít Ondruch <vondruch@redhat.com> - 0.6.9-1
- Update to i18n 0.6.9.
  - Fix CVE-2013-4491.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Josef Stribny <jstribny@redhat.com> - 0.6.4-1
- Update to i18n 0.6.4.

* Tue Feb 26 2013 Vít Ondruch <vondruch@redhat.com> - 0.6.1-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 26 2012 Vít Ondruch <vondruch@redhat.com> - 0.6.1-1
- Update to I18n 0.6.1.

* Wed Jul 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.6.0-1
- Update to I18n 0.6.0.
- Removed unneeded %%defattr usage.

* Thu Jan 19 2012 Vít Ondruch <vondruch@redhat.com> - 0.5.0-3
- Rebuilt for Ruby 1.9.3.
- Enabled test suite.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 24 2011 Vít Ondruch <vondruch@redhat.com> - 0.5.0-1
- Update to i18n 0.5.0.
- Documentation moved into subpackage.
- Removed unnecessary cleanup.
- Preparetion for test suite execution during build.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 18 2010 Jozef Zigmund <jzigmund@redhat.com> - 0.4.2-2
- Add GPLv2 or Ruby License
- Files MIT-LICENSE, geminstdir/lib/i18n.rb are non executable now

* Thu Nov 11 2010 Jozef Zigmund <jzigmund@redhat.com> - 0.4.2-1
- Initial package
