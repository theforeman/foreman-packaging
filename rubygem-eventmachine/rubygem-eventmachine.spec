%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name eventmachine

Summary:    Ruby/EventMachine library
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.12.10
Release:    10%{?dist}
Group:      Development/Languages
License:    GPLv2 or Ruby
URL:        http://rubyeventmachine.com
Source0:    http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
# Fixed upstream
# https://github.com/eventmachine/eventmachine/commit/2c083af3d06d333db31dcc1bbe535b10285a8d1e
Patch0:     rubygem-eventmachine-0.12.10-makes-HTTPS-client-tests-pass.patch
Requires:   %{?scl_prefix_ruby}ruby(rubygems)
Requires:   %{?scl_prefix_ruby}ruby(abi) = 1.9.1
Provides:   %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}
BuildRequires: %{?scl_prefix_ruby}rubygems-devel, %{?scl_prefix_ruby}ruby-devel, openssl-devel, %{?scl_prefix_ruby}rubygem(rake), net-tools

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
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install -V \
    --local \
    --install-dir $(pwd)/%{gem_dir} \
    --force --rdoc \
    %{SOURCE0}
%{?scl:"}

pushd .%{gem_instdir}
%patch0 -p1
popd

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{ruby_vendorarchdir}
cp -a ./%{gem_dir}/* %{buildroot}/%{gem_dir}/

rm -rf %{buildroot}%{gem_instdir}/{ext,java,.gitignore,setup.rb,%{gem_name}.gemspec}
mv %{buildroot}%{gem_libdir}/*.so %{buildroot}%{ruby_vendorarchdir}

%clean
rm -rf %{buildroot}

%check
pushd .%{gem_instdir}
# no kqueue support on Linux
rm -f tests/test_process_watch.rb
rake test || :

%files
%defattr(-, root, root, -)
%doc %{gem_instdir}/README
%dir %{gem_instdir}/
%{gem_libdir}
%{gem_cache}
%{gem_spec}
%{ruby_vendorarchdir}/rubyeventmachine.so
%{ruby_vendorarchdir}/fastfilereaderext.so

%files doc
%defattr(-, root, root, -)
%{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/docs
%{gem_instdir}/examples
%{gem_instdir}/tasks
%{gem_instdir}/tests
%{gem_instdir}/web

%changelog
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
