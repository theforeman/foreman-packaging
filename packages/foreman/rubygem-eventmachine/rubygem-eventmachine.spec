# template: default
%global gem_name eventmachine
%global gem_require_name %{gem_name}

Name: rubygem-%{gem_name}
Version: 1.2.7
Release: 2%{?dist}
Summary: Ruby/EventMachine library
License: Ruby and GPL-2.0
URL: https://rubyeventmachine.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby-devel
BuildRequires: rubygems-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
# end specfile generated dependencies
BuildRequires: gcc-c++
BuildRequires: openssl-devel

%description
EventMachine implements a fast, single-threaded engine for arbitrary network
communications. It's extremely easy to use in Ruby. EventMachine wraps all
interactions with IP sockets, allowing programs to concentrate on the
implementation of network protocols. It can be used to create both network
servers and clients. To create a server or client, a Ruby program only needs
to specify the IP address and port, and provide a Module that implements the
communications protocol. Implementations of several standard network protocols
are provided with the package, primarily to serve as examples. The real goal
of EventMachine is to enable programs to easily interface with other programs
using TCP/IP, especially if custom protocols are required.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/%{gem_name}
cp -a .%{gem_extdir_mri}/{*.so,gem.build_complete} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
# Ideally, this would be something like this:
# GEM_PATH="%{buildroot}%{gem_dir}:$GEM_PATH" ruby -e "require '%{gem_require_name}'"
# But that fails to find native extensions on EL8, so we fake the structure that ruby expects
mkdir gem_ext_test
cp -a %{buildroot}%{gem_dir} gem_ext_test/
mkdir -p gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
cp -a %{buildroot}%{gem_extdir_mri} gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
GEM_PATH="./gem_ext_test/gems:$GEM_PATH" ruby -e "require '%{gem_require_name}'"
rm -rf gem_ext_test

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/GNU
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/java
%{gem_libdir}
%exclude %{gem_instdir}/rakelib
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/docs
%{gem_instdir}/examples
%{gem_instdir}/tests

%changelog
* Mon Dec 18 2023 Evgeni Golov - 1.2.7-2
- Explicitly BuildRequire gcc-c++

* Wed Jul 20 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.2.7-1
- Update to 1.2.7

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.6-5
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.6-4
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.6-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.6-2
- Rebuild packages for Rails 5.1 (ericdhelms@gmail.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 1.0.6-1
- Update eventmachine to 1.0.6 (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.12.10-10
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Mar 11 2013 Miroslav Suchý <msuchy@redhat.com> 0.12.10-9
- require ruby-devel from SC (msuchy@redhat.com)
- fixing ruby193 scl package (lzap+git@redhat.com)

* Mon Mar 11 2013 Lukas Zapletal <lzap+git@redhat.com> 0.12.10-8
- converted rubygem-eventmachine to ruby193-rubygem-eventmachine
  (lzap+git@redhat.com)
- import rubygem-eventmachine from Fedora (lzap+git@redhat.com)
- removing thin and em - will re-import F18 version (lzap+git@redhat.com)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 19 2012 Vít Ondruch <vondruch@redhat.com> - 0.12.10-6
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 31 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.12.10-3
- More review fixes

* Sun Jan 31 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.12.10-2
- Review fixes (#556433)

* Mon Jan 18 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> - 0.12.10-1
- Initial package
