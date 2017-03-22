%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_maintain
%global confdir foreman_maintain

%{!?_root_bindir:%global _root_bindir %{_bindir}}

Summary: The Foreman/Satellite maintenance tool
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.3
Release: 1%{?dist}
Group: Development/Languages
License: GPLv3
URL: https://github.com/theforeman/foreman_maintain
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(clamp) >= 0.6.2
Requires: %{?scl_prefix}rubygem(highline)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
foreman_maintain aims to provide various features that helps keeping
the Foreman/Satellite up and running. It supports multiple versions
and subparts of the Foreman infrastructure, including server or smart
proxy and is smart enough to provide the right tools for the specific
version.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
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
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
sed -i '1s@/.*@/usr/bin/%{?scl_prefix}ruby@' .%{_bindir}/*
mkdir -p %{buildroot}%{_root_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_root_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_root_bindir}/foreman-maintain
%{gem_instdir}/bin
%{gem_instdir}/definitions
%{gem_instdir}/lib
%license %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue May 23 2017 Anurag Patel <apatel@redhat.com> 0.0.3-1
- Updated foreman_maintain with 0.0.3 tag.

* Mon Mar 20 2017 Anurag Patel <apatel@redhat.com> 0.0.2-1
- Updated foreman_maintain with 0.0.2 tag.

* Mon Feb 27 2017 Anurag Patel <apatel@redhat.com> 0.0.1-1
- Package foreman_maintain into RPM (#3, apatel@redhat.com)

