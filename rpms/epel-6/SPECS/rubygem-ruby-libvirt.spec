%define rbname ruby-libvirt
%define version 0.4.0
%define release 2

Summary: Ruby bindings for LIBVIRT
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://libvirt.org/ruby/
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.1
Requires: rubygems >= 1.8.10
BuildRequires: libvirt-devel
BuildRequires: ruby >= 1.8.1
BuildRequires: rubygems >= 1.8.10
Provides: rubygem(ruby-libvirt) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Ruby bindings for libvirt.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/ruby-libvirt-0.4.0/Rakefile
%{gemdir}/gems/ruby-libvirt-0.4.0/COPYING
%{gemdir}/gems/ruby-libvirt-0.4.0/README
%{gemdir}/gems/ruby-libvirt-0.4.0/NEWS
%{gemdir}/gems/ruby-libvirt-0.4.0/README.rdoc
%{gemdir}/gems/ruby-libvirt-0.4.0/lib/libvirt.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/domain.h
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/domain.c
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/network.h
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/secret.c
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/secret.h
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/stream.h
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/storage.h
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/storage.c
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/_libvirt.c
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/interface.h
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/network.c
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/nwfilter.c
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/connect.h
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/common.h
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/connect.c
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/common.c
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/interface.c
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/nodedevice.h
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/nodedevice.c
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/stream.c
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/nwfilter.h
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/extconf.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_interface.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_network.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_nwfilter.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_utils.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_domain.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_storage.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_open.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_secret.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_conn.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_nodedevice.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/Makefile
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/_libvirt.o
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/_libvirt.so
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/common.o
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/connect.o
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/domain.o
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/extconf.h
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/interface.o
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/mkmf.log
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/network.o
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/nodedevice.o
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/nwfilter.o
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/secret.o
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/storage.o
%{gemdir}/gems/ruby-libvirt-0.4.0/ext/libvirt/stream.o
%{gemdir}/gems/ruby-libvirt-0.4.0/lib/_libvirt.so
%doc %{gemdir}/doc/ruby-libvirt-0.4.0
%{gemdir}/cache/ruby-libvirt-0.4.0.gem
%{gemdir}/specifications/ruby-libvirt-0.4.0.gemspec

%changelog
* Tue May 08 2012 jmontleo@redhat.com - 0.4.0-2
- Cleaned up spec file

