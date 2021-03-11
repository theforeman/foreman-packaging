%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name algebrick

Summary: Algebraic types and pattern matching
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.7.3
Release: 8%{?dist}
Group: Development/Languages
License: GPLv3
URL: https://github.com/pitr-ch/algebrick
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
It's a gem providing algebraic types and pattern matching seamlessly
integrates with standard features Ruby.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE.txt
%{gem_instdir}/VERSION
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/README_FULL.md
%doc %{gem_instdir}/doc

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.7.3-8
- Rebuild against rh-ruby27

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.7.3-7
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.7.3-6
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.7.3-5
- Rebuild for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.7.3-4
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.7.3-3
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 20 2015 Dominic Cleal <dcleal@redhat.com> 0.7.3-2
- Package algebrick for non-SCL el7 (stbenjam@redhat.com)

* Tue Jul 07 2015 Dominic Cleal <dcleal@redhat.com> 0.7.3-1
- Update algebrick to 0.7.3 (dcleal@redhat.com)

* Thu Jul 02 2015 Dominic Cleal <dcleal@redhat.com> 0.7.0-1
- Update algebrick to 0.7.0 (inecas@redhat.com)
- Add full rubygems.org source URL (dcleal@redhat.com)

* Mon Jan 20 2014 Ivan Nečas <inecas@redhat.com> 0.4.0-2
- Fix scl build (inecas@redhat.com)

* Mon Jan 20 2014 Ivan Nečas <inecas@redhat.com> 0.4.0-1
- new package built with tito
