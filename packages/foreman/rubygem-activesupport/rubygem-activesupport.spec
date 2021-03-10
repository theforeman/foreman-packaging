# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name activesupport
%global gem_require_name %{gem_name}

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 6.0.3.5
Release: 2%{?dist}
Summary: A toolkit of support libraries and Ruby core extensions extracted from the Rails framework
Group: Development/Languages
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.5.0
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(i18n) >= 0.7
Requires: %{?scl_prefix}rubygem(i18n) < 2
Requires: %{?scl_prefix}rubygem(tzinfo) >= 1.1
Requires: %{?scl_prefix}rubygem(tzinfo) < 2
Requires: %{?scl_prefix_ruby}rubygem(minitest) >= 5.1
Requires: %{?scl_prefix_ruby}rubygem(minitest) < 6
Requires: %{?scl_prefix}rubygem(concurrent-ruby) >= 1.0
Requires: %{?scl_prefix}rubygem(concurrent-ruby) < 2
Requires: %{?scl_prefix}rubygem(concurrent-ruby) >= 1.0.2
Requires: %{?scl_prefix}rubygem(zeitwerk) >= 2.2
Requires: %{?scl_prefix}rubygem(zeitwerk) < 3
Requires: %{?scl_prefix}rubygem(zeitwerk) >= 2.2.2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.5.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

Obsoletes: tfm-ror52-rubygem-%{gem_name} <= 5.2.1

%description
A toolkit of support libraries and Ruby core extensions extracted from the
Rails framework. Rich support for multibyte strings, internationalization,
time zones, and testing.


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

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc

%changelog
* Wed Mar 10 2021 Eric D. Helms <ericdhelms@gmail.com> - 6.0.3.5-2
- Rebuild against rh-ruby27

* Tue Feb 23 2021 Evgeni Golov - 6.0.3.5-1
- Release rubygem-activesupport 6.0.3.5

* Mon Oct 26 2020 Evgeni Golov - 6.0.3.4-1
- Release rubygem-activesupport 6.0.3.4

* Mon Jun 15 2020 Eric D. Helms <ericdhelms@gmail.com> - 6.0.3.1-1
- Release rubygem-activesupport 6.0.3.1

* Tue Apr 28 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.0.2.2-1
- Update to 6.0.2.2

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 6.0.2.1-1
- Release rubygem-activesupport 6.0.2.1

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2.1-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2.1-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 5.2.1-2
- Bump for moving over to foreman-packaging

* Wed Aug 22 2018 Eric D. Helms <ericdhelms@gmail.com> 5.2.1-1
- Release tfm-ror52-rubygem-activesupport 5.2.1

* Fri Aug 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.0-4
- rebuilt

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.0-3
- Fix minitest requires

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.0-2
- Add missing gem_docdir

* Wed Aug 08 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.0-1
- Initial package
