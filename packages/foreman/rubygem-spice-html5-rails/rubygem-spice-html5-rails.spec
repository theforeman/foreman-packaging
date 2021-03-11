%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from spice-html5-rails-0.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name spice-html5-rails

Summary: Spice client using HTML5 (WebSockets, Canvas)
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.5
Release: 10%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://www.spice-space.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(railties) >= 3.1.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Spice HTML5 client packed for Rails application


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
%exclude %{gem_cache}
%{gem_spec}
%{gem_instdir}/vendor
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/COPYING.LESSER
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.md

%files doc
%doc %{gem_docdir}

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.1.5-10
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.1.5-9
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.1.5-8
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.1.5-7
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.5-6
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.1.5-5
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.1.5-4
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.1.5-3
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.1.5-2
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Dec 18 2014 Dominic Cleal <dcleal@redhat.com> 0.1.5-1
- Update spice-html5-rails to 0.1.5 (dcleal@redhat.com)

* Tue Feb 11 2014 Dominic Cleal <dcleal@redhat.com> 0.1.4-1
- Update to v0.1.4 (dcleal@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 0.0.1-6
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 0.0.1-5
- new package built with tito

* Wed Apr 03 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.1-3
- new package built with tito

* Wed Apr 03 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.1-2
- new package built with tito

* Wed Apr 03 2013 msuchy@redhat.com - 0.0.1-1
- Initial package
