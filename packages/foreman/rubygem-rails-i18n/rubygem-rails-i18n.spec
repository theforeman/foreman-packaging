# template: default
%global gem_name rails-i18n

Name: rubygem-%{gem_name}
Version: 7.0.9
Release: 1%{?dist}
Summary: Common locale data and translations for Rails i18n
License: MIT
URL: https://github.com/svenfuchs/rails-i18n
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel >= 1.8.11
BuildArch: noarch
# end specfile generated dependencies

%description
A set of common locale data and translations to internationalize and/or
localize your Rails applications.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE.txt
%{gem_libdir}
%{gem_instdir}/rails
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Mon Mar 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 7.0.9-1
- Update to 7.0.9

* Wed Aug 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 7.0.8-1
- Update to 7.0.8

* Tue May 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 7.0.7-1
- Update to 7.0.7

* Thu Nov 10 2022 Foreman Packaging Automation <packaging@theforeman.org> 7.0.6-1
- Update to 7.0.6

* Fri Aug 26 2022 Foreman Packaging Automation <packaging@theforeman.org> 7.0.5-1
- Update to 7.0.5

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 6.0.0-3
- Rebuild against rh-ruby27

* Thu Apr 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.0.0-2
- Update requirements on railties

* Thu Apr 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.0.0-1
- Update to 6.0.0

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.1.1-4
- Bump to release for EL8

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
