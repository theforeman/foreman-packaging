%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rbvmomi

Summary: Ruby interface to the VMware vSphere API
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.10.0
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/vmware/rbvmomi
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/vmware/rbvmomi.git && cd rbvmomi/
# git checkout v1.10.0
# tar czvf rbvmomi-1.10.0-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby >= 1.8.7
Requires: %{?scl_prefix_ruby}rubygem(json) >= 1.8
Requires: %{?scl_prefix_ror}rubygem(nokogiri) >= 1.5
Requires: %{?scl_prefix_ror}rubygem(nokogiri) < 2.0
Requires: %{?scl_prefix_ror}rubygem(builder) >= 3.0
Requires: %{?scl_prefix_ror}rubygem(builder) < 4.0
Requires: %{?scl_prefix}rubygem(trollop) >= 2.1
Requires: %{?scl_prefix}rubygem(trollop) < 3.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygem(json) >= 1.8
BuildRequires: %{?scl_prefix_ror}rubygem(nokogiri) >= 1.5
BuildRequires: %{?scl_prefix_ror}rubygem(nokogiri) < 2.0
BuildRequires: %{?scl_prefix_ror}rubygem(builder) >= 3.0
BuildRequires: %{?scl_prefix_ror}rubygem(builder) < 4.0
BuildRequires: %{?scl_prefix_ruby}rubygem(test-unit)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby >= 1.8.7
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Ruby interface to the VMware vSphere API


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
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

find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x

%check
pushd %{buildroot}%{gem_instdir}
tar xzvf %{SOURCE1}
sed -i '/simplecov/I s/^\( *\)/\1#/' test/test_helper.rb

%{?scl:scl enable %{scl} - <<EOF}
ruby -Ilib:test -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{_bindir}/rbvmomish
%{gem_instdir}/exe
%{gem_libdir}
%{gem_instdir}/vmodl.db
%exclude %{gem_instdir}/.*
%{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/devel
%{gem_instdir}/test
%doc %{gem_instdir}/examples
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/*.gemspec

%changelog
* Tue Mar 14 2017 Dominic Cleal <dominic@cleal.org> 1.10.0-1
- Update rbvmomi to 1.10.0 (dominic@cleal.org)

* Wed Oct 19 2016 Dominic Cleal <dominic@cleal.org> 1.9.4-1
- Update rbvmomi to 1.9.4 (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.8.2-4
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.8.2-3
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Fix build errors and modernise specs (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 1.8.2-2
- Converted to tfm SCL (dcleal@redhat.com)

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
