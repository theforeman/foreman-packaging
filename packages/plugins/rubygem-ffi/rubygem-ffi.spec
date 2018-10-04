# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ffi
%{!?enable_test: %global enable_test 0}

Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        1.4.0
Release:        8%{?dist}
Summary:        FFI Extensions for Ruby
Group:          Development/Languages

License:        LGPLv3
URL:            http://wiki.github.com/ffi/ffi
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:  %{?scl_prefix_ruby}ruby-devel
BuildRequires:  %{?scl_prefix_ruby}rubygems-devel
BuildRequires:	libffi-devel
%if 0%{enable_test} > 0
BuildRequires:	%{?scl_prefix_ror}rubygem(rspec)
%endif

Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix_ruby}ruby(release)

Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Ruby-FFI is a ruby extension for programmatically loading dynamic
libraries, binding functions within them, and calling those functions
from Ruby code. Moreover, a Ruby-FFI extension works without changes
on Ruby and JRuby. Discover why should you write your next extension
using Ruby-FFI here[http://wiki.github.com/ffi/ffi/why-use-ffi].

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

%if 0%{enable_test} > 0
%check
pushd .%{gem_instdir}
make -f libtest/GNUmakefile
rspec spec
popd
%endif

%files
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/COPYING.LESSER
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/LICENSE
%doc %{gem_docdir}

%dir %{gem_instdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/gen
%exclude %{gem_instdir}/ext
%exclude %{gem_instdir}/libtest
%{gem_instdir}/ffi.gemspec
%{gem_libdir}
%{gem_instdir}/spec
%{gem_extdir_mri}/
%exclude %{gem_cache}
%{gem_spec}


%changelog
* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.4.0-8
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 1.4.0-7
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 1.4.0-6
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 1.4.0-5
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Fix build errors and modernise specs (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 1.4.0-4
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jan 23 2015 Marek Hulan <mhulan@redhat.com> 1.4.0-3
- SCL support for rubygem-ffi (mhulan@redhat.com)

* Tue Mar 26 2013 Vít Ondruch <vondruch@redhat.com> - 1.4.0-2
- Use %%{gem_extdir_mri} instead of %%{gem_extdir}.

* Wed Feb 20 2013 Vít Ondruch <vondruch@redhat.com> - 1.4.0-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to FFI 1.4.0.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 1.0.9-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 14 2011 Bryan Kearney <bkearney@redhat.com> - 1.0.9-2
- Fixed the License, it is actually LGPL

* Mon Jun 13 2011 Bryan Kearney <bkearney@redhat.com> - 1.0.9-1
- Bring in 1.0.9 from upstream.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 10 2010 Bryan Kearney <bkearney@redhat.com> - 0.6.2-1
- Power PC fixes from upstream which were found testing 0.6.2

* Mon Feb 22 2010 Bryan Kearney <bkearney@redhat.com> - 0.6.2-1
- Pull in 0.6.2 from upstream

* Mon Feb 22 2010 Bryan Kearney <bkearney@redhat.com> - 0.5.4-3
- Final updates based on package review

* Tue Feb 16 2010 Bryan Kearney <bkearney@redhat.com> - 0.5.4-2
- Updates Based on code review comments

* Mon Feb 15 2010 Bryan Kearney <bkearney@redhat.com> - 0.5.4-1
- Initial specfile
