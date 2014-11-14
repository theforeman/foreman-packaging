%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rbvmomi

Summary: Ruby interface to the VMware vSphere API
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.8.2
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/vmware/rbvmomi
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} && 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi)
%endif
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby >= 1.8.7
Requires: %{?scl_prefix}rubygem(nokogiri) >= 1.4.1
Requires: %{?scl_prefix}rubygem(builder)
Requires: %{?scl_prefix}rubygem(trollop)
%if 0%{?fedora} && 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi)
%endif
BuildRequires: %{?scl_prefix}rubygem(nokogiri) >= 1.4.1
BuildRequires: %{?scl_prefix}rubygem(builder)
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby >= 1.8.7
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Ruby interface to the VMware vSphere API


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd %{buildroot}%{gem_instdir}
%{?scl:scl enable %{scl} "}
testrb -I lib test/test_*.rb
%{?scl:"}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{_bindir}/rbvmomish
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/vmodl.db
%exclude %{gem_instdir}/.yardopts
%{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/VERSION
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/devel
%{gem_instdir}/test
%doc %{gem_instdir}/examples
%{gem_instdir}/Rakefile

%changelog
* Fri Nov 14 2014 Dominic Cleal <dcleal@redhat.com> 1.8.2-1
- Rebase to rbvmomi 1.8.0 (dcleal@redhat.com)

* Thu Jan 23 2014 Dominic Cleal <dcleal@redhat.com> 1.6.0-2
- Update spec for Fedora 19 with ruby(release) (dcleal@redhat.com)

* Tue Jun 11 2013 Dominic Cleal <dcleal@redhat.com> 1.6.0-1
- Rebase to rbvmomi 1.6.0 (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 1.2.3-7
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.3-5
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 21 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.3-3
- Added vmodl.db back, since it's required dependency

* Mon Jul 11 2011 Francesco Vollero <fvollero@redhat.com> - 1.2.3-2
- Fix License to MIT
- Removed the >= 0 versions from rubygems Requires
- Add Requires and BuildRequires: ruby(abi) = 1.8
- Executed the test suite.

* Tue Jun 14 2011 Francesco Vollero <fvollero@redhat.com> - 1.2.3-1
- Initial package
