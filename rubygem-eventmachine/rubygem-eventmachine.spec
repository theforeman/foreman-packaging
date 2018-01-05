%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name eventmachine

# This enables to run full test suite, where network connection is available.
# However, it must be disabled for Koji build.
%{!?network: %global network 0}

Summary:    Ruby/EventMachine library
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    1.0.6
Release:    2%{?dist}
Group:      Development/Languages
License:    GPLv2 or Ruby
URL:        http://rubyeventmachine.com
Source0:    http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires:   %{?scl_prefix_ruby}ruby(rubygems)
Requires:   %{?scl_prefix_ruby}ruby(release)
Provides:   %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby-devel
BuildRequires: %{?scl_prefix_ruby}rubygem(test-unit)
# Enables SSL support.
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
Summary: Documentation for %{pkg_name}
Group: Documentation
BuildArch: noarch

Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
This package contains documentation for %{pkg_name}.


%prep
%setup -n %{pkg_name}-%{version} -q -T -c
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo.
rm -rf %{buildroot}%{gem_instdir}/ext

%check
pushd .%{gem_instdir}

# test_localhost(TestResolver) fails.
# https://github.com/eventmachine/eventmachine/issues/579
sed -i '/test_localhost/,/^  end$/ s/^/#/' tests/test_resolver.rb
# test_dispatch_completion(TestThreadedResource) fails randomly.
# https://github.com/eventmachine/eventmachine/issues/580
sed -i '/test_dispatch_completion/,/^  end$/ s/^/#/' tests/test_threaded_resource.rb

%{?scl:scl enable %{scl} - <<EOF}
# Unfortunatelly test_a exists in more test cases.
ruby -Ilib:$(dirs +1)%{gem_extdir_mri}:.:tests -r test/unit -e "Dir.glob 'tests/test_*.rb', &method(:require)" -- \
%if 0%{network} < 1
  --ignore-name=/^test_bind_connect$/ \
  --ignore-name=/^test_get_sock_opt$/ \
  --ignore-name=/^test_cookie$/ \
  --ignore-name=/^test_http_client$/ \
  --ignore-name=/^test_http_client_1$/ \
  --ignore-name=/^test_http_client_2$/ \
  --ignore-name=/^test_version_1_0$/ \
  --ignore-name=/^test_get$/ \
  --ignore-name=/^test_get_pipeline$/ \
  --ignore-name=/^test_https_get$/ \
  --ignore-name=/^test_idle_time$/ \
  --ignore-name=/^test_a$/ \
  --ignore-name=/^test_a_pair$/ \
  --ignore-name=/^test_bad_host$/ \
  --ignore-name=/^test_failure_timer_cleanup$/ \
  --ignore-name=/^test_timer_cleanup$/ \
  --ignore-name=/^test_set_sock_opt$/ \
  --ignore-name=/^test_connect_timeout$/ \
%endif
%{?scl:EOF}

popd

%files
%doc %{gem_instdir}/GNU
%doc %{gem_instdir}/LICENSE
%dir %{gem_instdir}/
%exclude %{gem_instdir}/.*
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/docs
%{gem_instdir}/eventmachine.gemspec
%{gem_instdir}/examples
# TODO: Hmm, we can build also JRuby bindigs.
%{gem_instdir}/java
%{gem_instdir}/rakelib
%{gem_instdir}/tests

%changelog
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
