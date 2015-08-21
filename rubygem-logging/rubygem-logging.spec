%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name logging

Summary: A flexible and extendable logging library for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.8.2
Release: 1%{?dist}
Group: Development/Languages
License: Ruby or BSD
URL: http://rubygems.org/gems/logging
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?scl_prefix_ruby}ruby(rubygems)

%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && "%{?scl}" == "")
Requires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires: %{?scl_prefix_ruby}ruby(release)
%endif
Requires: %{?scl_prefix}rubygem(little-plugger) >= 1.1.3
Requires: %{?scl_prefix}rubygem(multi_json) >= 1.8.4

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
# BuildRequires: %{?scl_prefix}rubygem(little-plugger) >= 1.1.3
# BuildRequires: %{?scl_prefix}rubygem(flexmock) >= 0.9.0
# BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Logging is a flexible logging library for use in Ruby programs based on the
design of Java's log4j library. It features a hierarchical logging system,
custom level names, multiple output destinations per log event, custom
formatting, and more.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation

Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
This package contains documentation for %{pkg_name}.


%prep
%setup -n %{pkg_name}-%{version} -q -c -T

mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/data
# contains licensing information
%doc %{gem_instdir}/README.rdoc
# version.txt is needed for runtime
%{gem_instdir}/version.txt
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/script
%{gem_instdir}/lib
%{gem_spec}
%exclude %{gem_cache}

%files doc
%{gem_instdir}/examples
%{gem_instdir}/test
%{gem_instdir}/Rakefile
%doc %{gem_docdir}/ri
%doc %{gem_docdir}/rdoc
%doc %{gem_instdir}/History.txt

%changelog
* Thu Jan 15 2015 Dominic Cleal <dcleal@redhat.com> 1.8.2-1
- Update logging to 1.8.2 (dcleal@redhat.com)

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 1.8.1-26
- Modernise and update for EL7 (dcleal@redhat.com)

* Wed Aug 28 2013 Dominic Cleal <dcleal@redhat.com> 1.8.1-25
- Don't override gem macros when building under SCL (dcleal@redhat.com)

* Wed Aug 21 2013 Dominic Cleal <dcleal@redhat.com> 1.8.1-24
- Add multi_json dependency, update little-plugger version (dcleal@redhat.com)

* Tue Aug 20 2013 Dominic Cleal <dcleal@redhat.com> 1.8.1-23
- fix dependency on ruby(abi) for ruby193 SCL builds (dcleal@redhat.com)

* Fri Aug 16 2013 Sam Kottler <shk@redhat.com> 1.8.1-22
- Remove SCL conditional

* Fri Aug 16 2013 Sam Kottler <shk@redhat.com> 1.8.1-21
- Fix SCL logic (shk@redhat.com)

* Fri Aug 16 2013 Sam Kottler <shk@redhat.com> 1.8.1-20
- Fix dep issues with ruby-abi (again) (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-19
- Fix ruby-abi version on RHEL (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-18
- Fix ruby-abi version on RHEL (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-17
- gem_dir -> gem_instdir (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-16
- Remove superfluous excludes (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-15
- Add more rubygem-devel stuff (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-14
- Fix gem_instdir (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-13
- Remove test running (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-12
- Remove excessive conditional (shk@redhat.com)

* Wed Aug 14 2013 Sam Kottler <shk@redhat.com> 1.8.1-11
- Fixed a minor syntax error (shk@redhat.com)
- Ensure the correct ABI version or release is used (shk@redhat.com)

* Tue Aug 13 2013 Sam Kottler <shk@redhat.com> 1.8.1-10
- Final bump for release

* Tue Aug 13 2013 Sam Kottler <shk@redhat.com> 1.8.1-9
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Tue Aug 13 2013 Sam Kottler <shk@redhat.com>
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Tue Aug 13 2013 Sam Kottler <shk@redhat.com>
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Tue Mar 12 2013 Lukas Zapletal <lzap+git@redhat.com> 1.8.1-5
- fixing ruby193 scl package (lzap+git@redhat.com)

* Mon Mar 11 2013 Lukas Zapletal <lzap+git@redhat.com> 1.6.2-4
- fixing ruby193 scl package (lzap+git@redhat.com)

* Mon Mar 11 2013 Lukas Zapletal <lzap+git@redhat.com> 1.6.2-3
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 30 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.6.2-1
- Rebuilt for Ruby 1.9.3.
- Updated to version 1.6.2.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 02 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 1.6.1-1
- New version.
- Removed unnecessary defattr macro in files section.
- Removed unnecessary clean section.
- Replaced define macros with more appropriate global.
- Moved gem install to the prep section.
- Added check section to run tests.
- BuildRequires now contain rubygem(little-plugger) and rubygem(flexmock) due to running tests.
- Introduced doc subpackage.

* Wed Mar 16 2011 Chris Lalancette <clalance@redhat.com> - 1.4.3-1
- Initial package
