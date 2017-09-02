%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rails-i18n

Summary: Common locale data and translations for Rails i18n
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 4.0.9
Release: 1%{?dist}
Group: Development/Ruby
License: MIT
URL: https://github.com/svenfuchs/rails-i18n
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix_ror}rubygem(i18n) >= 0.7
Requires: %{?scl_prefix_ror}rubygem(i18n) < 1
Requires: %{?scl_prefix_ror}rubygem(railties) >= 4.0
Requires: %{?scl_prefix_ror}rubygem(railties) < 5.0
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
A set of common locale data and translations to internationalize and/or
localize your Rails applications.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
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
