%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name opennebula

Summary: OpenNebula Client API
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.8.0
Release: 6%{?dist}
Group: Development/Languages
License: MIT
URL: http://opennebula.org/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby

Requires: %{?scl_prefix_ruby}rubygem(json)
Requires: %{?scl_prefix_ror}rubygem(nokogiri)

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Libraries needed to talk to OpenNebula

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
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/NOTICE

%changelog
* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 4.8.0-6
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 4.8.0-5
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 4.8.0-4
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 4.8.0-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 4.8.0-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Aug 13 2014 Dominic Cleal <dcleal@redhat.com> 4.8.0-1
- new package built with tito
