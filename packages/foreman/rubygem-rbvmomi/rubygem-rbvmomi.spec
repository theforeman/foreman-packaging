# template: default
%global gem_name rbvmomi

Name: rubygem-%{gem_name}
Version: 2.4.1
Release: 1%{?dist}
Summary: Ruby interface to the VMware vSphere API
License: MIT
URL: https://github.com/vmware/rbvmomi
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 1.8.7
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Ruby interface to the VMware vSphere API.


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

find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/rbvmomish
%license %{gem_instdir}/LICENSE
%{gem_instdir}/exe
%{gem_libdir}
%{gem_instdir}/vmodl.db
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.4.1-1
- Update to 2.4.1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.2.0-4
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.0-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.0-2
- Update spec to remove the ror scl

* Wed Aug 21 2019 Evgeni Golov 2.2.0-1
- Update to 2.2.0-1

* Thu Mar 21 2019 Marek Hulan <mhulan@redhat.com> 2.0.1-1
- Update to 2.0.1

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.10.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.10.0-2
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

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

* Thu Jul 21 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.3-3
- Added vmodl.db back, since it's required dependency

* Mon Jul 11 2011 Francesco Vollero <fvollero@redhat.com> - 1.2.3-2
- Fix License to MIT
- Removed the >= 0 versions from rubygems Requires
- Add Requires and BuildRequires: ruby(abi) = 1.8
- Executed the test suite.

* Tue Jun 14 2011 Francesco Vollero <fvollero@redhat.com> - 1.2.3-1
- Initial package
