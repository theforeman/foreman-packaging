%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkgname %{name}}

%define gem_name gridster-rails

Summary: Provides jquery.gridster for your Rails 3+ application
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.5.6.1
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/vanetten/gridster-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ror}rubygem(railties) >= 3.1.0
Requires: %{?scl_prefix_ror}rubygem(railties) < 6.0.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Gridster is a jQuery plugin that makes building intuitive draggable layouts
from elements spanning multiple columns. You can even dynamically add and
remove elements from the grid.

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
%{gem_instdir}/lib
%{gem_instdir}/vendor
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%changelog
* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.5.6.1-2
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Tue Aug 09 2016 Dominic Cleal <dominic@cleal.org> 0.5.6.1-1
- Update gridster-rails to 0.5.6.1 (dominic@cleal.org)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.5.6-4
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.5.6-3
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.5.6-2
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Thu Nov 12 2015 Dominic Cleal <dcleal@redhat.com> 0.5.6-1
- Update gridster-rails to 0.5.6 (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.1.5-5
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Jul 17 2014 Lukas Zapletal <lzap+git@redhat.com> 0.1.5-4
- Fixed dependency in the -doc subpackage (lzap+git@redhat.com)
- Fixed doc subpackages (lzap+git@redhat.com)

* Thu Jul 17 2014 Lukas Zapletal <lzap+rpm@redhat.com> 0.1.5-3
- Fixed dependency in the -doc subpackage

* Wed May 21 2014 Dominic Cleal <dcleal@redhat.com> 0.1.5-2
- Remove RHEL 7 from ruby(release) conditional (dcleal@redhat.com)

* Tue May 20 2014 Dominic Cleal <dcleal@redhat.com> 0.1.5-1
- new package built with tito
