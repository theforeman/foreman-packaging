# template: default
%global gem_name facter

Name: rubygem-%{gem_name}
Version: 4.4.0
Release: 1%{?dist}
Summary: Facter, a system inventory tool
License: ASL 2.0
URL: https://github.com/puppetlabs/facter
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5
Requires: ruby < 4.0
BuildRequires: ruby >= 2.5
BuildRequires: ruby < 4.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%ifarch %ix86 x86_64 ia64
Requires: dmidecode
Requires: pciutils
Requires: virt-what
%endif
Requires: net-tools

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
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/facter
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Thu May 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 4.4.0-1
- Update to 4.4.0

* Mon Apr 17 2023 Foreman Packaging Automation <packaging@theforeman.org> 4.3.1-1
- Update to 4.3.1

* Tue Feb 21 2023 Foreman Packaging Automation <packaging@theforeman.org> 4.3.0-1
- Update to 4.3.0

* Wed Jan 04 2023 Foreman Packaging Automation <packaging@theforeman.org> 4.2.14-1
- Update to 4.2.14

* Sun Oct 23 2022 Foreman Packaging Automation <packaging@theforeman.org> 4.2.13-1
- Update to 4.2.13

* Sun Sep 18 2022 Foreman Packaging Automation <packaging@theforeman.org> 4.2.12-1
- Update to 4.2.12

* Sun Aug 28 2022 Foreman Packaging Automation <packaging@theforeman.org> 4.2.11-1
- Update to 4.2.11

* Fri Jul 22 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.2.10-1
- Update to 4.2.10

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

