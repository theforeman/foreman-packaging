%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rack-mount

%global testdir %{_tmppath}/%{gem_name}-%{version}

Summary: Stackable dynamic tree based Rack router
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.7.1
Release: 10%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/josh/%{gem_name}
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/josh/rack-mount.git && cd rack-mount && git checkout v0.7.1
# tar czvf rack-mount-tests.tgz test/
Source1: %{gem_name}-tests.tgz
# Add dependency on unbundeld regin.
Patch1: rack-mount-add-regin-deps.patch
Patch2: rack-mount-Fix-hash-order-dependent-test-failure.patch
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem(rack) >= 1.1.0
Requires: %{?scl_prefix}rubygem(regin)
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(rack) >= 1.1.0
BuildRequires: %{?scl_prefix}rubygem(regin)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Stackable dynamic tree based Rack router. Supports Rack’s X-Cascade convention
to continue trying routes if the response returns pass. This allows multiple
routes to be nested or stacked on top of each other. Since the application
endpoint can trigger the router to continue matching, middle-ware can be used
to add arbitrary conditions to any route. This allows you to route based
on other request attributes, session information, or even data dynamically
pulled from a database.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

pushd .%{gem_dir}
%patch1 -p0
rm -f specifications/rack-mount-0.7.1.gemspec.orig
popd

rm -rf %{testdir}
mkdir %{testdir}
tar xzvf %{SOURCE1} -C %{testdir}
pushd %{testdir}
%patch2 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

rm -rf %{buildroot}%{gem_instdir}/lib/rack/mount/vendor

%check
pushd %{testdir}
%{?scl:scl enable %{scl} - << \EOF}
#RUBYOPT="$RUBYOPT rubygems I%{buildroot}%{gem_instdir}/lib I./test" testrb test/test_*
%{?scl:EOF}
popd
rm -rf %{testdir}


%files
%defattr(-, root, root, -)
%dir %{gem_instdir}
%{gem_instdir}/lib
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%defattr(-, root, root, -)
%doc %{gem_dir}/doc/%{gem_name}-%{version}

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.7.1-10
- switch off tests (msuchy@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.7.1-9
- new package built with tito

* Tue Jul 17 2012 Miroslav Suchý <msuchy@redhat.com> 0.7.1-8
- adding first bunch of rails deps (lzap+git@redhat.com)

* Mon Mar 19 2012 John Eckersberg <jeckersb@redhat.com> - 0.7.1-7
- Add patch to fix hash-order dependent test failure

* Tue Sep 23 2011 Shannon Hughes <shughes@redhat.com> - 0.7.1-6
- Adjust patch to math correct lines in rhel6.

* Tue Jun 28 2011 Vít Ondruch <vondruch@redhat.com> - 0.7.1-3
- Relaxed Rack dependency.

* Fri Jun 03 2011 Vít Ondruch <vondruch@redhat.com> - 0.7.1-2
- Fixed missing dependencies after unbundling regin.

* Thu Apr 07 2011 Vít Ondruch <vondruch@redhat.com> - 0.7.1-1
- Updated to rack-mount 0.7.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 28 2011 Vít Ondruch <vondruch@redhat.com> - 0.6.13-4
- Fixed test execution

* Wed Jan 26 2011 Vít Ondruch <vondruch@redhat.com> - 0.6.13-3
- Fixed vendor subdirectory removal
- Added test dir cleanup on the beginning of %check section

* Wed Jan 19 2011 Vít Ondruch <vondruch@redhat.com> - 0.6.13-2
- Added missing prep, build and clean sections
- Added missing dependency on rubygem-rack
- Removed unnecessary cleanup
- Removed vendored Regin and Multimap gems
- Added exection of test suite

* Fri Jan 07 2011 Vít Ondruch <vondruch@redhat.com> - 0.6.13-1
- Initial package
