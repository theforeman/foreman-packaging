%global gem_name openscap

Name: rubygem-%{gem_name}
Version: 0.4.7
Release: 1%{?dist}
Summary: A FFI wrapper around the OpenSCAP library
Group: Development/Languages
License: GPLv2+
URL: https://github.com/OpenSCAP/ruby-openscap
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: ruby(rubygems)
Requires: rubygem(ffi) >= 1.0.9
# require libopenscap.so.8 in an arch neutral way
Requires: openscap >= 1.2.9
Requires: openscap < 1.3.0
BuildRequires: rubygems-devel

# For tests we need:
BuildRequires: openscap >= 1.2.9
BuildRequires: openscap < 1.3.0
BuildRequires: bzip2

BuildRequires: rubygem(rake)
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(ffi) >= 1.0.9
BuildRequires: openscap-devel
# End (for the tests we needed)

%if 0%{?rhel} == 6
Requires: ruby(abi)
BuildRequires: ruby(abi)
%else
Requires: ruby(release)
BuildRequires: ruby(release)
%endif

# For the tests we need
%if 0%{?fedora} > 18
BuildRequires: rubygem(test-unit)
%else
BuildRequires: rubygem(minitest)
%endif

BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Obsoletes: ruby193-rubygem-%{gem_name}
Obsoletes: tfm-rubygem-%{gem_name} < 0.4.3-1

%description
A FFI wrapper around the OpenSCAP library. The %{name}
provides only a subset of openscap functionality.

%package devel
Summary: Development for %{name}
Requires: %{name} = %{version}-%{release}
Requires: rubygems
Obsoletes: ruby193-rubygem-%{gem_name}-devel
Obsoletes: tfm-rubygem-%{gem_name}-devel < 0.4.3-1
BuildArch: noarch

%description devel
Development files for %{name}

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
mkdir -p .%{gem_dir}

gem build %{gem_name}.gemspec

%gem_install -n %{gem_name}-%{version}.gem

%check
rake test

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/README.md
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files devel
%{gem_docdir}
%{gem_instdir}/test/
%{gem_instdir}/Rakefile

%changelog
* Tue Feb 14 2017 Dominic Cleal <dominic@cleal.org> 0.4.7-1
- Update openscap to 0.4.7 (mhulan@redhat.com)

* Mon Jan 04 2016 Dominic Cleal <dcleal@redhat.com> 0.4.3-2
- Fix dep to install correct test framework for F21 (dcleal@redhat.com)

* Fri Nov 06 2015 Dominic Cleal <dcleal@redhat.com> 0.4.3-1
- openscap version bump to 0.4.3, changed to non-SCL (shlomi@ben-hanna.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 0.4.2-3
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jan 23 2015 Marek Hulan <mhulan@redhat.com> 0.4.2-2
- new package built based on upstream spec

* Mon Jan 12 2015 Šimon Lukašík <slukasik@redhat.com> - 0.4.2-1
- upgrade to the new upstream version

* Sat Jan 10 2015 Šimon Lukašík <slukasik@redhat.com> - 0.4.1-1
- upgrade to the new upstream version

* Tue Dec 02 2014 Šimon Lukašík <slukasik@redhat.com> - 0.4.0-1
- upgrade to the new upstream version

* Thu Oct 23 2014 Šimon Lukašík <slukasik@redhat.com> - 0.3.0-1
- upgrade to the new upstream version

* Sat Sep 27 2014 Šimon Lukašík <slukasik@redhat.com> - 0.2.0-2
- fix dependency issue

* Fri Jul 25 2014 Šimon Lukašík <slukasik@redhat.com> - 0.2.0-1
- upgrade to the new upstream version

* Wed Jul 16 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.1-1
- upgrade to the new upstream version

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-5
- Avoid requires on a specific soname

* Wed May 21 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-4
- Fallback to cp command

* Tue May 20 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-3
- Moved COPYING and readme to the main package
- Created -devel sub-package out of -doc sub-package
- Dropped the word 'currently' from the package description
- Make a use of install instead of cp

* Tue May 06 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-2
- corrected license tag
- avoided macro in comment

* Tue Apr 22 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-1
- Initial package
