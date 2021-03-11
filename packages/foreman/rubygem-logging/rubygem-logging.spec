%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name logging

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.3.0
Release: 2%{?dist}
Summary: A flexible and extendable logging library for Ruby
Group: Development/Languages
License: MIT
URL: https://rubygems.org/gems/logging
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(little-plugger) >= 1.1
Requires: %{?scl_prefix}rubygem(little-plugger) < 2
Requires: %{?scl_prefix}rubygem(multi_json) >= 1.10
Requires: %{?scl_prefix}rubygem(multi_json) < 2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
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
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_instdir}/logging.gemspec
%{gem_instdir}/script
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/test

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.3.0-2
- Rebuild against rh-ruby27

* Wed Aug 12 2020 Lukas Zapletal <lzap+rpm@redhat.com> 2.3.0-1
- Update to 2.3.0

* Fri Mar 27 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.2.2-5
- Build for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.2-4
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.2.2-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed May 30 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.2.2-2
- Use multi_json from Rails SCL

* Tue Jan 23 2018 Daniel Lobato Garcia <me@daniellobato.me> 2.2.2-1
- Bump rubygem-logging to 2.2.2 (github@kohlvanwijngaarden.nl)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.8.2-5
- Final set of rebuilds (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.8.2-4
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.8.2-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.8.2-2
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

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
