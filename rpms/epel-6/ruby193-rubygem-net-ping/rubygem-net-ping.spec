%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name net-ping

Summary: A ping interface for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.5.3
Release: 8%{?dist}
Group: Development/Languages
License: Artistic 2.0
URL: http://www.rubyforge.org/projects/shards
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
Requires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
%if 0%{?fedora}
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(test-unit)
BuildRequires: %{?scl_prefix}rubygem(fakeweb)
BuildRequires: %{?scl_prefix}iputils
%endif
Requires: %{?scl_prefix}rubygem(net-ldap) >= 0.2.2
Requires: %{?scl_prefix}rubygem(net-ldap) < 0.3
Requires: %{?scl_prefix}rubygem(ffi) >= 1.0.0

%description
The net-ping library provides a ping interface for Ruby. It includes
separate TCP, HTTP, ICMP, UDP, WMI (for Windows) and external ping
classes.


%package doc
Summary: A ping interface for Ruby - documentation
Group: Development/Languages

%description doc
This package contains the documentation files for the %{gem_name} Ruby
library.


%prep

%build

%install
mkdir -p %{buildroot}%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{buildroot}%{gem_dir} --force %{SOURCE0}
%{?scl:"}



%check
%if 0%{?fedora}
pushd %{buildroot}%{gem_instdir}
# three tests are ignored because of missing network connectivity
%{?scl:scl enable %{scl} - << \EOF}
RUBYOPT="-Ilib" testrb2 test/test_net_ping.rb \
--ignore-name=test_duration_basic_functionality \
--ignore-name=test_pinging_a_good_host_results_in_no_exception_data \
--ignore-name=test_pinging_a_good_host_returns_true
%{?scl:EOF}
popd
%endif

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%doc %{gem_instdir}/README
%{gem_cache}
%{gem_spec}


%files doc
%defattr(-, root, root, -)
%dir %{gem_instdir}
%doc %{gem_instdir}/doc/ping.txt
%doc %{gem_instdir}/examples/
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_instdir}/net-ping.gemspec
%{gem_instdir}/MANIFEST
%{gem_instdir}/CHANGES

%changelog
* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 1.5.3-8
- BR rubygems-devel to include macros (msuchy@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 1.5.3-7
- new package built with tito

* Mon Nov 26 2012 Miroslav Suchý <msuchy@redhat.com> 1.5.3-6
- require net-ldap and ffi (msuchy@redhat.com)

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 1.5.3-5
- fix filelist section (msuchy@redhat.com)

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 1.5.3-4
- add rubygems to buildrequires (msuchy@redhat.com)

* Thu Aug 09 2012 Miroslav Suchý <msuchy@redhat.com> 1.5.3-3
- new package built with tito

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 05 2012 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.5.3-1
- New version

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 1.5.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 16 2011 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.5.1-1
- rebuild

* Fri Mar 18 2011 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.4.1-1
- unit tests now use mock servers
- fixing issues from the review #672845

* Tue Jan 25 2011 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.4.0-1
- Initial package
