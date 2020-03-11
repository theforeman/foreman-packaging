%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rails-i18n

Summary: Common locale data and translations for Rails i18n
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 5.1.1
Release: 4%{?dist}
Group: Development/Ruby
License: MIT
URL: https://github.com/svenfuchs/rails-i18n
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(i18n) >= 0.7
Requires: %{?scl_prefix}rubygem(i18n) < 2
Requires: %{?scl_prefix}rubygem(railties) >= 5.0
Requires: %{?scl_prefix}rubygem(railties) < 6.0
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A set of common locale data and translations to internationalize and/or
localize your Rails applications.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -q -c -T
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
%{gem_instdir}/rails
%doc %{gem_instdir}/MIT-LICENSE.txt
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Mon Mar 02 2020 Eric D. Helms <ericdhelms@gmail.com> - 5.1.1-4
- Drop references to ruby193

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.1.1-3
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.1.1-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Aug 17 2018 Eric D. Helms <ericdhelms@gmail.com> 5.1.1-1
- Release 5.1.1

* Thu Jan 04 2018 Eric D. Helms <ericdhelms@gmail.com> 5.0.4-1
- Bump rails-i18n to 5.0.4 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Tue Jul 05 2016 Dominic Cleal <dominic@cleal.org> 4.0.9-1
- Update rails-i18n to 4.0.9 (dominic@cleal.org)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 4.0.8-3
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 4.0.8-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Mon Jan 04 2016 Dominic Cleal <dcleal@redhat.com> 4.0.8-1
- Update rails-i18n to 4.0.8 (dcleal@redhat.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 4.0.7-1
- Update rails-i18n to 4.0.7 (dcleal@redhat.com)
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 3.0.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Jul 29 2015 Dominic Cleal <dcleal@redhat.com> 3.0.1-1
- new package built with tito
