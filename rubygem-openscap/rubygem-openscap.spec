# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation/1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name openscap

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.2
Release: 2%{?dist}
Summary: A FFI wrapper around the OpenSCAP library
Group: Development/Languages
License: GPLv2+
URL: https://github.com/isimluk/ruby-openscap
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(ffi) >= 1.0.9
# require libopenscap.so.8 in an arch neutral way
Requires: openscap >= 1.2.1
Requires: openscap < 1.3.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby >= 1.9.3
# For tests we need:
BuildRequires: openscap >= 1.2.1
BuildRequires: openscap < 1.3.0
BuildRequires: bzip2
BuildRequires: %{?scl_prefix_ruby}rubygem(rake)
BuildRequires: %{?scl_prefix_ruby}rubygem(bundler)
BuildRequires: %{?scl_prefix}rubygem(ffi) >= 1.0.9
BuildRequires: openscap-devel
# End (for the tests we needed)

%if 0%{?fedora} > 18
Requires:      %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
# For the tests we need
BuildRequires: %{?scl_prefix}rubygem(test-unit)
%else
Requires:      %{?scl_prefix_ruby}ruby(abi)
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
# For the tests we need
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
%endif

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
A FFI wrapper around the OpenSCAP library. The %{name}
provides only a subset of openscap functionality.

%package devel
Summary: Development for %{name}
Requires: %{name} = %{version}-%{release}
Requires: rubygems
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-devel}
BuildArch: noarch

%description devel
Development files for %{name}

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
mkdir -p .%{gem_dir}

%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%check
%{?scl:scl enable %{scl} "}
rake test
%{?scl:"}

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
%{gem_instdir}/test/
%{gem_instdir}/Rakefile

%changelog
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
