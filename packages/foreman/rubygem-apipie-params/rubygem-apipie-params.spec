%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name apipie-params

Summary: DSL for describing data structures
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.5
Release: 5%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/iNecas/apipie-params
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby

%if 0%{?el6} && 0%{!?scl:1}
Requires: %{?scl_prefix_ruby}ruby(abi)
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%endif

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Allows defining structure of data and perform validation against
it using json-schema

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/test

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/%{gem_name}.gemspec

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.0.5-5
- Rebuild against rh-ruby27

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.0.5-4
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.0.5-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.0.5-2
- Rebuild for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Jul 21 2016 Dominic Cleal <dominic@cleal.org> 0.0.5-1
- Update apipie-params to 0.0.5 (inecas@redhat.com)

* Thu Jun 09 2016 Dominic Cleal <dominic@cleal.org> 0.0.4-5
- Make apipie-params depend on rake (#15342, aruzicka@redhat.com)
- Modernise spec file, correct license/URL (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-4
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-3
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 20 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-2
- Package apipie-params for non-SCL el7 (stbenjam@redhat.com)

* Mon Aug 17 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-1
- Release apipie-params 0.0.4 (stbenjam@redhat.com)

* Mon Jan 20 2014 Ivan Nečas <inecas@redhat.com> 0.0.3-1
- Bump version (inecas@redhat.com)

* Wed May 29 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.2-2
- change ruby(abi) to ruby(release) for F19+ (msuchy@redhat.com)

* Tue May 07 2013 Ivan Necas <inecas@redhat.com> 0.0.2-1
- new package built with tito
