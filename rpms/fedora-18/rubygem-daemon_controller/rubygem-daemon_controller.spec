%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from daemon_controller-0.2.5.gem by gem2rpm -*- rpm-spec -*-
%define gem_name daemon_controller

%if !("%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16)
%define gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%define gem_cache %{gem_dir}/cache/%{gem_name}-%{version}.gem
%define gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%define gem_libdir %{gem_instdir}/lib
%define gem_spec %{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%endif

%if 0%{?fedora} >= 19
%global gem_extdir %{gem_extdir_mri}
%endif

Summary: A library for implementing daemon management capabilities
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.4
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/FooBarWidget/daemon_controller/tree/master
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

%if 0%{?fedora} >= 19
Requires:      %{?scl_prefix}ruby(release)
%else
Requires:      %{?scl_prefix}ruby(abi) >= %{rubyabi}
BuildRequires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
%endif

Requires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}ruby
%if "%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16
BuildRequires: %{?scl_prefix}rubygems-devel
%endif
BuildRequires: %{?scl_prefix}rubygem(rspec-core)
BuildRequires: %{?scl_prefix}rubygem(rspec-mocks)
BuildRequires: %{?scl_prefix}rubygem(rspec-expectations)
%if "%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16
BuildRequires: %{?scl_prefix}rubygems-devel
%endif
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A library for robust daemon management.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep

%build

%install
mkdir -p %{buildroot}%{gem_dir}
%{?scl:scl enable %scl "}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --bindir %{buildroot}%{_bindir} \
            -V --no-ri \
            --force %{SOURCE0}
%{?scl:"}

%__rm -rf %{buildroot}%{gem_instdir}/debian.template

%check
pushd %{buildroot}%{gem_instdir}
# be explicit so localhost doesn't resolve to an ipv6 address.
%{__sed} -i 's/localhost/127.0.0.1/g' spec/daemon_controller_spec.rb
%{?scl:scl enable %{scl} "}
rspec -I%{buildroot}%{gem_libdir} -Ispec spec/
%{?scl:"}
popd

%files
%defattr(-, root, root, -)
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.markdown
%{gem_cache}
%{gem_spec}

%files doc
%defattr(-, root, root, -)
%{gem_instdir}/*.gemspec
%{gem_docdir}
%{gem_instdir}/spec

%changelog
* Wed Jun 05 2013 Martin Bačovský <mbacovsk@redhat.com> 1.1.4-3
- Added support for nonscl build in rhel6 (mbacovsk@redhat.com)

* Mon Jun 03 2013 Martin Bačovský <mbacovsk@redhat.com> 1.1.4-2
- built with tito
- scl support

* Fri May 03 2013 Brett Lentz <blentz@redhat.com> - 1.1.4-1
- Update to 1.1.4

* Mon Mar 18 2013 Brett Lentz <blentz@redhat.com> - 1.1.2-2
- use %%gem_install macro

* Fri Mar 15 2013 Brett Lentz <blentz@redhat.com> - 1.1.2-1
- Update to 1.1.2

* Wed Mar 13 2013 Brett Lentz <blentz@redhat.com> - 1.1.1-2
- Update to new packaging guidelines.

* Fri Feb 22 2013 Brett Lentz <blentz@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 13 2012 Brett Lentz <blentz@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 06 2012 Vít Ondruch <vondruch@redhat.com> - 0.2.6-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Apr 25 2011  Peng Wu <pwu@redhat.com> - 0.2.6-1
- Update to version 0.2.6

* Thu Apr 21 2011  Peng Wu <pwu@redhat.com> - 0.2.5-3
- Run test suite

* Wed Apr 20 2011  Peng Wu <pwu@redhat.com> - 0.2.5-2
- Fixes the spec

* Wed Apr 20 2011 Peng Wu <pwu@redhat.com> - 0.2.5-1
- Initial package
