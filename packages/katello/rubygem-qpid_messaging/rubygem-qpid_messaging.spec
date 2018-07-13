%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name qpid_messaging
%global qpid_version 1.36.0

Summary: Ruby bindings for the Qpid messaging framework
Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: %{qpid_version}
Release: 2%{?dist}
License: ASL 2.0
URL:     https://qpid.apache.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: qpid-cpp-client

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby-devel
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: qpid-cpp-client-devel = %{qpid_version}

Provides:      %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Qpid is an enterprise messaging framework. This package provides Ruby
language bindings based on that framework.

%package doc
Summary:   Documentation for %{?scl_prefix}%{name}
Requires:  %{?scl_prefix}%{name} = %{version}-%{release}
BuildArch: noarch
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
%{Summary}.

%files doc
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/ChangeLog
%{gem_instdir}/examples
%doc %{gem_instdir}/TODO

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
rm -rf %{buildroot}%{gem_instdir}/ext

%files
%{gem_extdir_mri}
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/LICENSE

%changelog
* Fri Jul 13 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.36.0-2
- rebuilt

* Wed Jan 10 2018 Eric D. Helms <ericdhelms@gmail.com> 1.36.0-1
- new package built with tito

* Wed Jul 20 2016 Justin Sherrill <jsherril@redhat.com> 0.34.1-1
- Fixes #13017 - remove priorities to use qpid from epel (jsherril@redhat.com)

* Tue Apr 26 2016 Justin Sherrill <jsherril@redhat.com> 0.30.0-8
- rebuild for ror42 (jsherril@redhat.com)

* Wed Jan 06 2016 Eric D. Helms <ericdhelms@gmail.com> 0.30.0-7
- Include native extensions for qpid_messaging properly (ericdhelms@gmail.com)

* Wed Jan 06 2016 Eric D. Helms <ericdhelms@gmail.com> 0.30.0-6
- Updating rubygem-qpid_messaging spec (ericdhelms@gmail.com)

* Wed Jan 06 2016 Eric D. Helms <ericdhelms@gmail.com>
- Updating rubygem-qpid_messaging spec (ericdhelms@gmail.com)

* Wed Jan 06 2016 Eric D. Helms <ericdhelms@gmail.com> 0.30.0-5
- Update build requires for rubygem-qpid_messaging (ericdhelms@gmail.com)

* Wed Jan 06 2016 Eric D. Helms <ericdhelms@gmail.com> 0.30.0-4
- Build rubygem-qpid_messaging for rh22 SCL (ericdhelms@gmail.com)

* Fri Aug 28 2015 Eric D. Helms <ericdhelms@gmail.com> 0.30.0-3
- Fixing scl_prefix reference in rubygem-qpid_messaging (ericdhelms@gmail.com)

* Thu Aug 27 2015 Eric D. Helms <ericdhelms@gmail.com> 0.30.0-2
- new package built with tito

* Wed Jan 21 2015 Jason Montleon <jmontleo@redhat.com> 0.30.0-1
- update rubygem-qpid_messaging to MRG 3.1 (jmontleo@redhat.com)

* Fri Dec 05 2014 Jason Montleon <jmontleo@redhat.com> 0.22.0-1.1
- add correct source (jmontleo@redhat.com)

* Fri Dec 05 2014 Jason Montleon <jmontleo@redhat.com> 0.22.0-1
- new package built with tito

* Thu Aug 07 2014 Jason Montleon <jmontleo@redhat.com> 0.26.1-4
- don't package non-existent doc dir (jmontleo@redhat.com)

* Thu Aug 07 2014 Jason Montleon <jmontleo@redhat.com> 0.26.1-3
- packaging change (jmontleo@redhat.com)

* Thu Aug 07 2014 Jason Montleon <jmontleo@redhat.com> 0.26.1-2
- new package built with tito

* Tue Jul 15 2014 Darryl L. Pierce <dpierce@redhat.com> - 0.26.1-1
- Rebased on qpid_messaging 0.26.1.

* Fri Feb 21 2014 Darryl L. Pierce <dpierce@redhat.com> - 0.26.0-1
- Rebased on qpid_messaging 0.26.0.

* Fri Oct 25 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.24.2-1
- Rebased on qpid_messaging 0.24.2.
- Fixed ordering of caught exceptions from C++.

* Fri Oct 25 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.24.1-2
- Removed the ARM exclusion.

* Fri Oct 25 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.24.1-1
- Rebased on qpid_messaging 0.24.1.

* Tue Sep 24 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.24.0-1
- Rebased on qpid_messaging 0.24.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.22-2
- Updated build to fix dependency issues on qpid-cpp.

* Tue Jun 18 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.22-1
- Rebased on qpid_messaging 0.22.

* Fri Mar  8 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.20.2-1
- Rebased on qpid_messaging 0.20.2.
- Updated to use the newer rubygems-devel macros.

* Thu Feb  7 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.20.0-2
- bump qpid_version to 0.20 to match release

* Mon Jan 28 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.20.0-1
- Rebased on qpid_messaging 0.20.0.

* Mon Jan  7 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.18.1-1.2
- Now installs the repackaged gem.

* Wed Dec 26 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.18.1-1.1
- Removed Group field from the doc subpackage.
- Updated the specfile to match current Ruby packaging guidelines.

* Mon Sep 24 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.18.1-1
- Rebased on qpid_messaging 0.18.1.
- Added the ChangeLog to the files in the -doc package.

* Mon Aug 13 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.16.0-1.2
- Moved the gem install statement to the install section.

* Wed Aug  1 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.16.0-1.1
- Added BR for ruby-devel.

* Thu Jul 19 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.16.0-1
- Initial repackaging.
