%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name responders

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.0.0
Release: 4%{?dist}
Summary: A set of Rails responders to dry up your application
Group: Development/Languages
License: MIT
URL: https://github.com/plataformatec/responders
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(actionpack) >= 5.0
Requires: %{?scl_prefix}rubygem(railties) >= 5.0
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A set of Rails responders to dry up your application

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.0.0-4
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.0.0-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.0.0-2
- Update spec to remove the ror scl

* Thu Oct 03 2019 Michael Moll <mmoll@mmoll.at> - 3.0.0-1
- Update responders to 3.0.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.4.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Thu Jan 04 2018 Eric D. Helms <ericdhelms@gmail.com> 2.4.0-1
- Bump rubygem-responders to 2.4.0 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed Aug 17 2016 Dominic Cleal <dominic@cleal.org> 2.3.0-1
- Update responders to 2.3.0 (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 2.1.1-1
- new package built with tito

