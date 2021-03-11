%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name friendly_id

Summary: Swiss Army bulldozer of slugging and permalinks for Active Record
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 5.3.0
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/norman/friendly_id
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby

Requires: %{?scl_prefix}rubygem(activerecord) >= 4.0.0

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for
Ruby on Rails. It allows you to create pretty URLs and work with
human-friendly strings as if they were numeric ids for Active Record models.


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
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/friendly_id.gemspec
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Changelog.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/UPGRADING.md
%{gem_instdir}/bench.rb
%{gem_instdir}/Gemfile
%{gem_instdir}/gemfiles
%{gem_instdir}/guide.rb
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 5.3.0-2
- Rebuild against rh-ruby27

* Fri May 01 2020 Michael Moll <mmoll@mmoll.at> - 5.3.0-1
- Update friendly_id to 5.3.0

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2.4-4
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2.4-3
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.2.4-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Mon Jun 04 2018 Michael Moll <mmoll@mmoll.at> 5.2.4-1
- Update to 5.2.4

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.1.0-4
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 5.1.0-3
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 5.1.0-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 5.1.0-1
- Update friendly_id to 5.1.0 (dcleal@redhat.com)
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 4.0.10.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Sep 29 2014 Dominic Cleal <dcleal@redhat.com> 4.0.10.1-1
- new package built with tito
