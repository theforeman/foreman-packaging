%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ffi
%global libname %{gem_name}_c.so
%global githubhash b79eb61
%global githubbuild 0
%global tarballname ffi-ffi-%{version}-%{githubbuild}-g%{githubhash}
%global gitinternalname ffi-ffi-%{githubhash}

Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        1.0.9
Release:        10%{?dist}
Summary:        FFI Extensions for Ruby
Group:          Development/Languages

License:        LGPLv3
URL:            http://wiki.github.com/ffi/ffi
# The source file is hosted at github. You can access this tarball with
# the following link:
#          http://github.com/ffi/ffi/tarball/1.0.9
Source0:        %{tarballname}.tar.gz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}ruby %{?scl_prefix}ruby-devel %{?scl_prefix}rubygems-devel
BuildRequires:  %{?scl_prefix}rubygem(rake) %{?scl_prefix}rubygem(rake-compiler) libffi-devel %{?scl_prefix}rubygem(rspec-core)
BuildRequires:  %{?scl_prefix}rubygem(rspec-mocks)
BuildRequires:  %{?scl_prefix}rubygem(rspec-expectations)
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires:  pkgconfig
Requires:       libffi
Requires: %{?scl_prefix}ruby(rubygems)
Requires:       %{?scl_prefix}ruby(abi) = 1.9.1
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Ruby-FFI is a ruby extension for programmatically loading dynamic
libraries, binding functions within them, and calling those functions
from Ruby code. Moreover, a Ruby-FFI extension works without changes
on Ruby and JRuby. Discover why should you write your next extension
using Ruby-FFI here[http://wiki.github.com/ffi/ffi/why-use-ffi].

%prep
%setup -q -n %{gitinternalname}

%build
export CFLAGS="%{optflags}"
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%{?scl:scl enable %{scl} "}
rake gem
%{?scl:"}
%{?scl:scl enable %{scl} "}
gem install -V -d --local --no-ri -i ./geminst --force pkg/%{gem_name}-%{version}.gem
%{?scl:"}

%install
rm -rf %{buildroot}
mkdir %{buildroot}
install -d -m0755 %{buildroot}%{gem_dir}
install -d -m0755  %{buildroot}%{gem_extdir}/lib
cp -R %{_builddir}/%{gitinternalname}/geminst/* %{buildroot}%{gem_dir}
mv %{buildroot}%{gem_libdir}/%{libname} %{buildroot}%{gem_extdir}/lib/%{libname}
rm -rf %{buildroot}%{gem_libdir}/%{libname}
rm -rf %{buildroot}%{gem_instdir}/ext

%check
# https://github.com/ffi/ffi/issues/189
sed -i -e 's| -mimpure-text||' libtest/GNUmakefile
%{?scl:scl enable %{scl} "}
rake -v test
%{?scl:"}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/LICENSE
%doc %{gem_docdir}
%dir %{gem_instdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/gen
%{gem_libdir}
%{gem_instdir}/spec
%{gem_instdir}/tasks
%{gem_extdir}/
%{gem_cache}
%{gem_spec}

%changelog
* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.9-10
- fix files section (msuchy@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.9-9
- add BR rubygem-rspec-expectations (msuchy@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.9-8
- add BR rubygem-rspec-mocks (msuchy@redhat.com)

* Tue Mar 12 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.9-7
- run rake in SC environment (msuchy@redhat.com)

* Tue Mar 12 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.9-6
- new package built with tito

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

* Tue Feb 22 2010 Bryan Kearney <bkearney@redhat.com> - 0.6.2-1
- Pull in 0.6.2 from upstream

* Tue Feb 22 2010 Bryan Kearney <bkearney@redhat.com> - 0.5.4-3
- Final updates based on package review

* Tue Feb 16 2010 Bryan Kearney <bkearney@redhat.com> - 0.5.4-2
- Updates Based on code review comments

* Mon Feb 15 2010 Bryan Kearney <bkearney@redhat.com> - 0.5.4-1
- Initial specfile
