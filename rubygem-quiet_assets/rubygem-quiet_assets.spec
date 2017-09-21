%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from quiet_assets-1.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name quiet_assets

Summary: Turn off rails assets log
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.2
Release: 10%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: https://github.com/evrone/quiet_assets
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ror}rubygem(railties) >= 3.1
Requires: %{?scl_prefix_ror}rubygem(railties) < 5.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Quiet assets turn off rails assets log.


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
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/%{gem_name}.gemspec

%files doc
%doc %{gem_docdir}
%{gem_instdir}/test

%changelog
* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 1.0.2-10
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.0.2-9
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-8
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-7
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 1.0.2-6
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 1.0.2-5
- new package built with tito

* Wed Apr 03 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.2-3
- new package built with tito

* Wed Apr 03 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.2-2
- new package built with tito

* Wed Apr 03 2013 msuchy@redhat.com - 1.0.2-1
- Initial package
