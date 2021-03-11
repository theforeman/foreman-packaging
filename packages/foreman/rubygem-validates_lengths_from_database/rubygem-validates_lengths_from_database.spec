%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name validates_lengths_from_database

Summary: Introspects your database string field maximum lengths and validates
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.5.0
Release: 8%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/rubiety/validates_lengths_from_database
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(activerecord) >= 2.3.2

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Few people add length validations to fields in their database, and when saving
such fields that have exhausted their length, an SQL error occurs. This gem
introspects your table schema for maximum lengths on string and text fields and
automatically adds length validations to the model.

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
%{gem_libdir}
%{gem_instdir}/init.rb
%{gem_instdir}/rails
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%exclude %{gem_instdir}/Appraisals
%exclude %{gem_instdir}/Gemfile*
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/*.gem
%exclude %{gem_instdir}/*.gemspec

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.5.0-8
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.5.0-7
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.5.0-6
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.5.0-5
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.5.0-4
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.5.0-3
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.5.0-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Feb 16 2016 Dominic Cleal <dominic@cleal.org> 0.5.0-1
- Update validates_lengths_from_database to 0.5.0 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.4.0-3
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.4.0-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Jan 07 2015 Dominic Cleal <dcleal@redhat.com> 0.4.0-1
- Update validates_lengths_from_database to 0.4.0 (dcleal@redhat.com)

* Thu Jul 31 2014 Dominic Cleal <dcleal@redhat.com> 0.2.0-1
- new package built with tito
