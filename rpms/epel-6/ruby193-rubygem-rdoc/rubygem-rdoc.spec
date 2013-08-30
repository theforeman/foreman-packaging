%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}
# Generated from rdoc-3.4.gem by gem2rpm -*- rpm-spec -*-
%define debug_package %{nil}

%if !("%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16)
%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global gem_libdir %{gem_instdir}/lib
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%global gem_cache %{gem_dir}/cache
%global gem_spec %{gem_dir}/specifications
%endif

%global gem_name rdoc

Summary: RDoc produces HTML and command-line documentation for Ruby projects
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.12
Release: 12%{?dist}
Group: Development/Languages
License: GPLv2 and Ruby and MIT
URL: http://docs.seattlerb.org/rdoc/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-rdoc-3.12-CVE-2013-0256-fix.patch
Requires: %{?scl_prefix}ruby(rubygems)
%if 0%{?fedora} && 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
%if "%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%else
Requires: %{?scl_prefix}ruby(abi) = 1.8
%endif
%endif
Requires: %{?scl_prefix}rubygem(json) => 1.4
Requires: %{?scl_prefix}rubygem(json) < 2
Requires: %{?scl_prefix}ruby-irb
BuildRequires: %{?scl_prefix}ruby-devel
%if "%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16
BuildRequires: %{?scl_prefix}rubygems-devel
%endif
BuildRequires: %{?scl_prefix}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(json) => 1.4
BuildRequires: %{?scl_prefix}rubygem(json) < 2
BuildRequires: %{?scl_prefix}rubygem(rake)
BuildRequires: %{?scl_prefix}ruby-irb
# RDoc files differ between architectures.
# https://github.com/rdoc/rdoc/issues/71
# BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
RDoc produces HTML and command-line documentation for Ruby projects.  RDoc
includes the +rdoc+ and +ri+ tools for generating and displaying online
documentation.
See RDoc for a description of RDoc's markup and basic use.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %scl "}
gem install --local --install-dir .%{gem_dir} \
%if "%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16
            --bindir .%{_bindir} \
%endif
            --force %{SOURCE0}
%{?scl:"}

pushd .%{gem_instdir}
%patch0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%if "%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
%endif

%if 0%{?ruby_libdir:1}
mkdir -p %{buildroot}%{ruby_libdir}
ln -s %{gem_libdir}/%{gem_name}.rb %{buildroot}%{ruby_libdir}/%{gem_name}.rb
ln -s %{gem_libdir}/%{gem_name} %{buildroot}%{ruby_libdir}/%{gem_name}
%endif

%check
# Tests won't run with old EL6 rubygems version
%if "%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16
pushd .%{gem_instdir}
# 73 test fails due to bug in packagin of the gem.
# https://github.com/rdoc/rdoc/issues/98
# Wrong assumptions about encoding. LANG has to be used.
# https://github.com/rdoc/rdoc/issues/99
%{?scl:scl enable %scl - << \EOF}
LANG=en_US.utf8 RUBYOPT="-Ilib" testrb test | \
	grep "1485 tests, 3339 assertions, 0 failures, 73 errors, 16 skips"
%{?scl:EOF}
popd
%endif

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE.rdoc
%doc %{gem_instdir}/LEGAL.rdoc
%exclude %{gem_instdir}/.*
%if "%{?scl}" == "ruby193" || 0%{?rhel} > 6 || 0%{?fedora} > 16
%{_bindir}/rdoc
%{_bindir}/ri
%else
%{gem_dir}/bin/rdoc
%{gem_dir}/bin/ri
%endif
%{gem_libdir}
%{gem_instdir}/bin
%exclude %{gem_cache}
%{gem_spec}
%if 0%{?ruby_libdir:1}
%{ruby_libdir}/%{gem_name}*
%endif

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/DEVELOPERS.rdoc
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CVE-2013-0256.rdoc
%doc %{gem_instdir}/RI.rdoc
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/TODO.rdoc
%{gem_instdir}/test


%changelog
* Fri Aug 30 2013 Dominic Cleal <dcleal@redhat.com> 3.12-12
- Support non-SCL EL6 builds, install alongside ruby-rdoc (dcleal@redhat.com)
- rubygem-rdoc: remove debuginfo package (cduryee@redhat.com)
- remove empty tito.props and definition which are duplicate with default from
  rel-eng/tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 3.12-10
- new package built with tito

* Thu Feb 07 2013 Josef Stribny <jstribny@redhat.com> - 3.12-9
- Patch cross site scripting vulnerability CVE-2013-0256 (rhbz#908358).

* Tue Jul 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.12-8
- Provide the symlink in %%{ruby_libdir}.

* Tue Jul 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.12-7
- Specfile cleanup.

* Mon Jun 04 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.12-6
- Removed BuildArch: noarch, as some files differ between arches.

* Wed Apr 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.12-5
- Add BR: rake to run all tests.

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.12-4
- Rebuilt for scl.

* Mon Apr 02 2012 Vít Ondruch <vondruch@redhat.com> - 3.12-3
- Add missing obsolete (rhbz#809007).

* Mon Feb 13 2012 Vít Ondruch <vondruch@redhat.com> - 3.12-2
- Add missing IRB dependency.

* Tue Feb 07 2012 Vít Ondruch <vondruch@redhat.com> - 3.12-1
- Rebuilt for Ruby 1.9.3.
- Updated to RDoc 3.12.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Mo Morsi <mmorsi@redhat.com> - 3.8-2
- Fixes for fedora compliance

* Mon Jan 10 2011 mo morsi <mmorsi@redhat.com> - 3.8-1
- Initial package
