%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_maintain
%global directory_name foreman-maintain

%{!?_root_bindir:%global _root_bindir %{_bindir}}

Summary: The Foreman/Satellite maintenance tool
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.9
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

install -d -m0750 %{buildroot}%{_localstatedir}/lib/%{directory_name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{directory_name}
install -d -m0750 %{buildroot}%{_sysconfdir}/%{directory_name}
install -D -m0640 %{buildroot}%{gem_instdir}/config/foreman_maintain.yml.packaging %{buildroot}%{_sysconfdir}/%{directory_name}/foreman_maintain.yml

%files
%dir %{gem_instdir}
%{_root_bindir}/foreman-maintain
%{gem_instdir}/bin
%{gem_instdir}/definitions
%{gem_instdir}/lib
%{gem_instdir}/config
%config(noreplace) %{_sysconfdir}/%{directory_name}
%{_localstatedir}/log/%{directory_name}
%{_localstatedir}/lib/%{directory_name}
%license %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Sep 14 2017 Anurag Patel <apatel@redhat.com> 0.0.9-1
- Updated gem version to 0.0.9

* Tue Aug 29 2017 Anurag Patel <apatel@redhat.com> 0.0.8-1
- Updated gem version to 0.0.8, with upgrade scenario updates.

* Mon Aug 21 2017 Anurag Patel <apatel@redhat.com> 0.0.7-1
- Updated gem version to 0.0.7, that includes full upgrade path support.

* Tue Jul 25 2017 Anurag Patel <apatel@redhat.com> 0.0.6-1
- Updated gem version to 0.0.6, that fixes an issue with config file location.

* Thu Jul 06 2017 Anurag Patel <apatel@redhat.com> 0.0.5-4
- Updated spec to support config file, data and log dirs.

* Fri Jun 16 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.3-1
- new package built with tito

* Tue May 23 2017 Anurag Patel <apatel@redhat.com> 0.0.3-1
- Updated foreman_maintain with 0.0.3 tag.

* Mon Mar 20 2017 Anurag Patel <apatel@redhat.com> 0.0.2-1
- Updated foreman_maintain with 0.0.2 tag.

* Mon Feb 27 2017 Anurag Patel <apatel@redhat.com> 0.0.1-1
- Package foreman_maintain into RPM (#3, apatel@redhat.com)

