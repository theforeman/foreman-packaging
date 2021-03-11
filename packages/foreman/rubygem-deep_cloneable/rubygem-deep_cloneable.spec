%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkgname %{name}}

%define gem_name deep_cloneable

Summary: This gem gives every ActiveRecord::Base object the possibility to do a deep clone
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.0.0
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/moiristo/deep_cloneable
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(activerecord) >= 3.1.0
Requires: %{?scl_prefix}rubygem(activerecord) < 7
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Extends the functionality of ActiveRecord::Base#dup to perform a deep clone
that includes user specified associations.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/*
%{gem_instdir}/lib
%exclude %{gem_cache}
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.document
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/readme.md
%doc %{gem_instdir}/CHANGELOG.md

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.0.0-4
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.0.0-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.0.0-2
- Update spec to remove the ror scl

* Tue Oct 01 2019 Michael Moll <mmoll@mmoll.at> 3.0.0-1
- Update to 3.0.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.3.2-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Mon Jun 04 2018 Michael Moll <mmoll@mmoll.at> 2.3.2-1
- Update to 2.3.2

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.2.2-2
- Rebuild packages for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Mon Oct 10 2016 Dominic Cleal <dominic@cleal.org> 2.2.2-1
- Update deep_cloneable to 2.2.2 (dominic@cleal.org)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 2.1.1-4
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 2.1.1-3
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 2.1.1-2
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Sep 30 2015 Dominic Cleal <dcleal@redhat.com> 2.1.1-1
- Update deep_cloneable to 2.1.1 (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 2.0.2-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Jan 07 2015 Dominic Cleal <dcleal@redhat.com> 2.0.2-1
- Update deep_cloneable to 2.0.2 (dcleal@redhat.com)

* Thu Jul 17 2014 Lukas Zapletal <lzap+git@redhat.com> 2.0.0-4
- Fixed dependency in the -doc subpackage (lzap+git@redhat.com)
- Fixed doc subpackages (lzap+git@redhat.com)

* Thu Jul 17 2014 Lukas Zapletal <lzap+rpm@redhat.com> 2.0.0-3
- Fixed dependency in the -doc subpackage

* Tue Jul 01 2014 Dominic Cleal <dcleal@redhat.com> 2.0.0-2
- Fix rubygem-activerecord dep to use epochs (dcleal@redhat.com)

* Tue Jul 01 2014 Dominic Cleal <dcleal@redhat.com> 2.0.0-1
- Update to deep_cloneable 2.0 (dcleal@redhat.com)

* Mon Mar 03 2014 Dominic Cleal <dcleal@redhat.com> 1.6.0-2
- Add rubygems-devel BR so SCL paths are used, tidy up (dcleal@redhat.com)

* Fri Feb 21 2014 Daniel Lobato <dlobatog@redhat.com> - 1.6.0-1
- new package rubygem-deep_cloneable built with tito
