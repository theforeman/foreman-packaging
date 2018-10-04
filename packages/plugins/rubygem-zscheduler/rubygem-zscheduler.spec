%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name zscheduler

Summary: Minimalistic scheduler on top of eventmachine
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.6
Release: 5%{?dist}
Group: Development/Languages
License: LGPLv3
URL: https://github.com/eranb/zscheduler
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(eventmachine)

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Minimalistic scheduler on top of eventmachine.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
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
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}

%changelog
* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.0.6-5
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.0.6-4
- Use gem_install macro (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Jan 14 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- new package built with tito
