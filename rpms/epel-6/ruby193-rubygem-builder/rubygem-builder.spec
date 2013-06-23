%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name builder
%global rubyabi 1.9.1

Summary: Builders for MarkUp
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.0.0
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://onestepback.org
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/jimweirich/builder/pull/15
Patch0: builder-3.0.0-fix-tests-with-Ruby-1.9.3-where-UTF-16-is-a-supporte.patch
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
Requires: %{?scl_prefix}ruby(rubygems)
# Builder carries copy of Blankslate, which was in the meantime extracted into
# independent gem.
# https://github.com/jimweirich/builder/issues/24
#
# Moreover, rubygem-blankslate is not yet in Fedora.
# https://bugzilla.redhat.com/show_bug.cgi?id=771316
#
# Requires: %{?scl_prefix}rubygem(blankslate)
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Builder provides a number of builder objects that make creating structured
data simple to do. Currently the following builder objects are supported:
* XML Markup
* XML Events

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

pushd .%{gem_instdir}
%patch0 -p1
popd

%build

%install
# test_cssbuilder.rb is part of the package just by mistake it seems.
# https://github.com/jimweirich/builder/pull/25
rm .%{gem_instdir}/test/test_cssbuilder.rb

mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Fix anything executable that does not have a shebang.
for file in `find %{buildroot}/%{gem_instdir} -name "*.rb"`; do
    [ ! -z "`head -n 1 $file | grep \"^#!\"`" ] && chmod +x $file
done

chmod -x %{buildroot}%{gem_instdir}/doc/releases/builder-2.1.1.rdoc

# Convert README.rdoc to utf8
strings %{buildroot}/%{gem_instdir}/README.rdoc > %{buildroot}/%{gem_instdir}/README.rdoc.strings
mv -f %{buildroot}/%{gem_instdir}/README.rdoc.strings %{buildroot}/%{gem_instdir}/README.rdoc

# Convert README to utf8
strings %{buildroot}/%{gem_instdir}/README > %{buildroot}/%{gem_instdir}/README.strings
mv -f %{buildroot}/%{gem_instdir}/README.strings %{buildroot}/%{gem_instdir}/README


%check
pushd .%{gem_instdir}
# we would need Gem unit-test to get no failures => no more dependencies, please
%{?scl:scl enable %{scl} "}
testrb -I.:lib test | grep '100 tests, 173 assertions, 0 failures, 18 errors, 0 skips'
%{?scl:"}
popd

%files
%dir %{gem_instdir}
# Two inconsitent readmes?
# https://github.com/jimweirich/builder/issues/22
%doc %{gem_instdir}/README
%doc %{gem_instdir}/README.rdoc
# Seems to be in package just by accident.
# https://github.com/jimweirich/builder/issues/10
%exclude %{gem_instdir}/TAGS
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc/releases/builder-1.2.4.rdoc
%doc %{gem_instdir}/doc/releases/builder-2.0.0.rdoc
%doc %{gem_instdir}/doc/releases/builder-2.1.1.rdoc
%{gem_instdir}/test

%changelog
* Thu Feb 21 2013 Miroslav Suchý <msuchy@redhat.com> 3.0.0-3
- new package built with tito

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.0-2
- Converted to scl again from Fedora - much better packaged there.

* Wed Jul 18 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.0-1
- Update to Builder 3.0.0.

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 2.1.2-9
- Fixed license.

* Thu Jan 19 2012 Vít Ondruch <vondruch@redhat.com> - 2.1.2-8
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 Vít Ondruch <vondruch@redhat.com> - 2.1.2-6
- Fix FTBFS rhbz#712927.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 29 2008 Jeroen van Meeuwen <kanarip@kanarip.com> - 2.1.2-2
- Rebuild for review

* Sun Jul 13 2008 root <root@oss1-repo.usersys.redhat.com> - 2.1.2-1
- Initial package

