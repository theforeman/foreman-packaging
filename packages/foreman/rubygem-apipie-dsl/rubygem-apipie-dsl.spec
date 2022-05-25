# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name apipie-dsl

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.5.0
Release: 1%{?dist}
Summary: Ruby DSL documentation tool
Group: Development/Languages
License: MIT
URL: https://github.com/ofedoren/apipie-dsl
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.5.0
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.5.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Ruby DSL documentation tool.


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
%license %{gem_instdir}/APACHE-LICENSE-2.0
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/app
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/test

%changelog
* Wed May 25 2022 Evgeni Golov 2.5.0-1
- Update to 2.5.0

* Thu Apr 15 2021 Oleh Fedorenko <ofedoren@redhat.com> 2.4.0-1
- Update to 2.4.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.3.0-2
- Rebuild against rh-ruby27

* Tue Oct 13 2020 Oleh Fedorenko <ofedoren@redhat.com> 2.3.0-1
- Update to 2.3.0

* Mon Jul 27 2020 Oleh Fedorenko <ofedoren@redhat.com> 2.2.9-1
- Update to 2.2.9

* Mon Jul 20 2020 Oleh Fedorenko <ofedoren@redhat.com> 2.2.8-1
- Update to 2.2.8

* Fri Jun 26 2020 Oleh Fedorenko <ofedoren@redhat.com> 2.2.7-1
- Update to 2.2.7

* Fri May 29 2020 Oleh Fedorenko <ofedoren@redhat.com> 2.2.5-1
- Update to 2.2.5

* Tue Apr 28 2020 Tomer Brisker <tbrisker@gmail.com> - 2.2.2-2
- rebuild for el8

* Mon Apr 06 2020 Oleh Fedorenko <ofedoren@redhat.com> 2.2.2-1
- Add rubygem-apipie-dsl generated by gem2rpm using the scl template

