%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name facter

# Disable debuginfo as no native code is packaged (only Reqs)
%global debug_package %{nil}

Summary: Command and ruby library for gathering system information
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.0.51
Release: 2%{?dist}
Group: System Environment/Base
License: ASL 2.0
URL: https://puppetlabs.com/%{gem_name}
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(hocon) >= 1.3
Requires: %{?scl_prefix}rubygem(hocon) < 2.0
Requires: %{?scl_prefix}rubygem(thor) >= 1.0.1
Requires: %{?scl_prefix}rubygem(thor) < 2.0


%ifarch %ix86 x86_64 ia64
Requires: dmidecode
Requires: pciutils
Requires: virt-what
%endif
Requires: net-tools
Requires: which

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

Obsoletes: ruby193-%{gem_name}

%description
Facter is a lightweight program that gathers basic node information about the
hardware and operating system. Facter is especially useful for retrieving
things like operating system names, hardware characteristics, IP addresses, MAC
addresses, and SSH keys.

Facter is extensible and allows gathering of node information that may be
custom or site specific. It is easy to extend by including your own custom
facts. Facter can also be used to create conditional expressions in Puppet that
key off the values returned by facts.

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
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

%files
%dir %{gem_instdir}
%{_bindir}/facter
%{gem_libdir}
%{gem_instdir}/bin
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.0.51-2
- Rebuild against rh-ruby27

* Tue Mar 02 2021 Lukas Zapletal <lzap+rpm@redhat.com> 4.0.51-1
- Update to 4.0.51

* Wed Nov 25 2020 Lukas Zapletal <lzap+rpm@redhat.com> 4.0.44-1
- Update to 4.0.44

* Thu Aug 20 2020 Lukas Zapletal <lzap+rpm@redhat.com> 4.0.35-1
- Update to 4.0.35

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.4.0-7
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.4.0-6
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.4.0-5
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Mon Apr 10 2017 Dominic Cleal <dominic@cleal.org> 2.4.0-4
- Disable debuginfo package (dominic@cleal.org)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 2.4.0-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 2.4.0-2
- new package built with tito

