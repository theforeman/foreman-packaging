%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from sass-3.1.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sass

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.4.19
Release: 2%{?dist}
Summary: A powerful but elegant CSS compiler that makes CSS fun again
Group: Development/Languages
License: MIT
URL: http://sass-lang.com/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Sass makes CSS fun again. Sass is an extension of CSS, adding
nested rules, variables, mixins, selector inheritance, and more.
It's translated to well-formatted, standard CSS using the
command line tool or a web-framework plugin.

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

%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

pushd .%{gem_instdir}
# Remove bundled rubygem-listener:
# https://github.com/nex3/sass/issues/458
rm -rf vendor
popd

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%{_bindir}/sass
%{_bindir}/sass-convert
%{_bindir}/scss
%exclude %{gem_instdir}/.*
%{gem_instdir}/CODE_OF_CONDUCT.md
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/REVISION
%{gem_instdir}/VERSION
%{gem_instdir}/VERSION_DATE
%{gem_instdir}/VERSION_NAME
%{gem_instdir}/bin
%dir %{gem_instdir}/extra
%{gem_instdir}/extra/update_watch.rb
%{gem_instdir}/init.rb
%{gem_libdir}
%dir %{gem_instdir}/rails
%{gem_instdir}/rails/init.rb
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Thu Dec 17 2015 Dominic Cleal <dcleal@redhat.com> 3.4.19-2
- Replace %%license for EL6 compatibility

* Mon Oct 12 2015 Vít Ondruch <vondruch@redhat.com> - 3.4.19-1
- Update to Sass 3.4.19.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 16 2014 Mo Morsi <mmorsi@redhat.com> - 3.4.4-1
- Update to 3.4.4
- Remove patch now included in upstream release

* Thu Jun 12 2014 Mo Morsi <mmorsi@redhat.com> - 3.3.8-1
- Update to latest upstream release
- Include patch updating test suite to minitest 5

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 13 2014 Vít Ondruch <vondruch@redhat.com> - 3.2.14-1
- Update to sass 3.2.14.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.6-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to sass 3.2.6.
- Own extra and rails directories (rhbz#911648).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Mo Morsi <mmorsi@redhat.com> - 3.2.3-2
- update to sass 3.2.3
- update changelog

* Thu Jul 26 2012 Vít Ondruch <vondruch@redhat.com> - 3.1.20-2
- Fix dependency rubygem(fssm) => rubygem(listen).

* Mon Jul 23 2012 Vít Ondruch <vondruch@redhat.com> - 3.1.20-1
- Update to sass 3.1.20.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.1.7-6
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Chris Lalancette <clalance@redhat.com> - 3.1.4-4
- Add patches to make sass work in Fedora

* Thu Jul 21 2011 Mo Morsi <mmorsi@redhat.com> - 3.1.4-3
- changed ruby(fssm) dep to rubygem(fssm)

* Thu Jul 14 2011 Mo Morsi <mmorsi@redhat.com> - 3.1.4-2
- corrected license, whitespace fixes

* Wed Jul 13 2011 Mo Morsi <mmorsi@redhat.com> - 3.1.4-1
- Initial package
