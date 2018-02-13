%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from net-ssh-multi-1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name net-ssh-multi

%global enable_check 0

Summary: Control multiple Net::SSH connections via a single interface
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.0
Release: 7%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/net-ssh/net-ssh-multi
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-net-ssh-multi-1.2.0-minitest.patch
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(net-ssh) >= 2.6.5
Requires: %{?scl_prefix}rubygem(net-ssh-gateway) >= 1.2.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
%if 0%{?enable_check}
BuildRequires: %{?scl_prefix}rubygem(net-ssh)
BuildRequires: %{?scl_prefix}rubygem(net-ssh-gateway)
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires: %{?scl_prefix_ror}rubygem(mocha)
%endif
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Control multiple Net::SSH connections via a single interface.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
This package contains documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

pushd .%{gem_instdir}
%patch0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
%if 0%{?enable_check}
pushd %{buildroot}%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
ruby -Ilib:test test/test_all.rb
%{?scl:EOF}
popd
%endif

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/net-ssh-multi.gemspec

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGES.txt
%doc %{gem_instdir}/LICENSE.txt
%{gem_instdir}/gem-public_cert.pem
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 1.2.0-7
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.2.0-6
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 1.2.0-5
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 1.2.0-4
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jun 13 2014 Julian C. Dunn <jdunn@aquezada.com> - 1.2.0-3
- Convert to Minitest (bz#1107179)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 21 2013 Julian C. Dunn <jdunn@aquezada.com> - 1.2.0-1
- Update to 1.2.0 (bz#1015287)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 16 2013 Julian C. Dunn <jdunn@aquezada.com> - 1.1-4
- Unbreak build on >= F19

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 27 2012 Julian C. Dunn <jdunn@aquezada.com> - 1.1-2
- Unified EPEL and Fedora builds

* Sat Apr 14 2012  <rpms@courteau.org> - 1.1-1
- Initial package
