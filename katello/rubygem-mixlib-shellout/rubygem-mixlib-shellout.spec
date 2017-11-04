%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name mixlib-shellout

Summary: Run external commands on Unix or Windows
Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 2.2.1
Release: 3%{?dist}
Group:   Development/Languages
License: GPLv3
URL:     https://github.com/chef/mixlib-shellout
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby(release)

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby

%description
Provides a simplified interface to shelling out
yet still collecting both standard out and standard error
and providing full control over environment, working directory, uid, gid, etc.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
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
%license %{gem_instdir}/LICENSE
%{gem_instdir}/lib
%{gem_spec}

%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Apr 26 2016 Justin Sherrill <jsherril@redhat.com> 2.2.1-3
- rebuild for ror42 (jsherril@redhat.com)

* Wed Jan 06 2016 Eric D. Helms <ericdhelms@gmail.com> 2.2.1-2
- Build rubygem-mixlib-shellout for rh22 SCL (ericdhelms@gmail.com)

* Tue Dec 01 2015 Eric D. Helms <ericdhelms@gmail.com> 2.2.1-1
- new package built with tito

* Mon Nov 02 2015 Ondrej Prazak <oprazak@redhat.com> 2.2.1-1
- initial build
