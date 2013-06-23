%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name i18n

Summary: New wave Internationalization support for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.6.0
Release: 4%{?dist}
Group: Development/Languages
License: MIT and (GPLv2 or Ruby)
URL: http://github.com/svenfuchs/i18n
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(mocha)
BuildRequires: %{?scl_prefix}rubygem(test_declarative)
BuildRequires: %{?scl_prefix}rubygem(sqlite3)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Ruby Internationalization and localization solution.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %scl "}
gem install --local --install-dir .%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
chmod -x %{buildroot}%{gem_instdir}/MIT-LICENSE
chmod -x %{buildroot}%{gem_libdir}/i18n.rb

%check
pushd .%{gem_instdir}

# Bundler just complicates everything in our case, remove it.
sed -i -e "s|require 'bundler/setup'||" test/test_helper.rb

# Tests are failing without LANG environment is set.
# https://github.com/svenfuchs/i18n/issues/115
# The test failure is due to change of default YAML engine in Ruby 1.9.3.
# https://github.com/svenfuchs/i18n/issues/114
%{?scl:scl enable %scl - << \EOF}
LANG=en_US.utf8 testrb -Ilib test/all.rb | \
	grep "1026 tests, 1505 assertions, 1 failures, 0 errors, 0 skips"
%{?scl:EOF}

popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/README.textile
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/CHANGELOG.textile
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/ci
%{gem_instdir}/test
%doc %{gem_docdir}


%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.6.0-4
- new package built with tito

* Tue Jul 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.6.0-3
- Exclude the cached gem.

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.6.0-2
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.6.0-1
- Rebuilt for scl.
- Updated to 0.6.0.

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
