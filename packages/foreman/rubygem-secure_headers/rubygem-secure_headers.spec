%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name secure_headers

Summary: Security related headers all in one gem
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 6.3.0
Release: 3%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/twitter/secureheaders
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Add easily configured security headers to responses including content security
policy, x-frame-options, strict-transport-security and more.

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
%exclude %{gem_instdir}/secure_headers.gemspec
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/docs
%{gem_instdir}/Gemfile
%{gem_instdir}/Guardfile
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 6.3.0-3
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 6.3.0-2
- Bump to release for EL8

* Tue Jan 28 2020 Michael Moll <mmoll@mmoll.at> 6.3.0-1
- Update secure_headers to 6.3.0

* Mon Sep 10 2018 Michael Moll <mmoll@mmoll.at> 6.0.0-1
- Update secure_headers to 6.0.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.0.5-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Mon Apr 30 2018 Michael Moll <mmoll@mmoll.at> 5.0.5-1
- Update secure_headers to 5.0.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.4.1-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Mon Sep 12 2016 Dominic Cleal <dominic@cleal.org> 3.4.1-1
- Update secure_headers to 3.4.1 (dominic@cleal.org)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 1.4.1-4
- Use gem_install macro (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.4.1-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.4.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Dec 15 2014 Dominic Cleal <dcleal@redhat.com> 1.4.1-1
- Update secure_headers to 1.4.1 (dcleal@redhat.com)

* Mon Oct 13 2014 Dominic Cleal <dcleal@redhat.com> 1.3.3-1
- new package built with tito
