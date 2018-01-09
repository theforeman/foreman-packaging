%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from net-ssh-gateway-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name net-ssh-gateway

Summary: A simple library to assist in establishing tunneled Net::SSH connections
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.0
Release: 5%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/net-ssh/net-scp
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems) >= 1.2
Requires: %{?scl_prefix}rubygem(net-ssh) >= 2.6.5
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix}rubygem(net-ssh) >= 2.6.5
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
A simple library to assist in establishing tunneled Net::SSH connections

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

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
%doc %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Manifest
%{gem_instdir}/Rakefile
%{gem_instdir}/net-ssh-gateway.gemspec
%{gem_instdir}/gem-public_cert.pem
%{gem_instdir}/setup.rb
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGES.txt
%{gem_instdir}/test

%changelog
* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.2.0-4
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 1.2.0-3
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Fix build errors and modernise specs (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 1.2.0-2
- Converted to tfm SCL (dcleal@redhat.com)

* Thu May 09 2013 Vít Ondruch <vondruch@redhat.com> - 1.2.0-1
- Update to net-ssh-gateway 1.2.0.

* Fri Mar 08 2013 Vít Ondruch <vondruch@redhat.com> - 1.1.0-8
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 07 2012 Vít Ondruch <vondruch@redhat.com> - 1.1.0-5
- Fix broken dependency.

* Tue Jan 31 2012 Vít Ondruch <vondruch@redhat.com> - 1.1.0-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 06 2011 Vít Ondruch <vondruch@redhat.com> - 1.1.0-2
- Removed unnecessary setup.rb.

* Thu May 26 2011 Vít Ondruch <vondruch@redhat.com> - 1.1.0-1
- Initial package
