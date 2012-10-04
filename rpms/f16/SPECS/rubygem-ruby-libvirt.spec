# Generated from ruby-libvirt-0.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gemname ruby-libvirt

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: Ruby bindings for LIBVIRT
Name: rubygem-%{gemname}
Version: 0.4.0
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://libvirt.org/ruby/
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby >= 1.8.1
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby >= 1.8.1
Provides: rubygem(%{gemname}) = %{version}

%description
Ruby bindings for libvirt.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install --local --install-dir .%{gemdir} \
            -V \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
        %{buildroot}%{gemdir}/

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{geminstdir}/ext

%files
%dir %{geminstdir}
%{geminstdir}/lib
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/gems/ruby-libvirt-0.4.0/COPYING
%{gemdir}/gems/ruby-libvirt-0.4.0/NEWS
%{gemdir}/gems/ruby-libvirt-0.4.0/README
%{gemdir}/gems/ruby-libvirt-0.4.0/README.rdoc
%{gemdir}/gems/ruby-libvirt-0.4.0/Rakefile
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_conn.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_domain.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_interface.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_network.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_nodedevice.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_nwfilter.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_open.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_secret.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_storage.rb
%{gemdir}/gems/ruby-libvirt-0.4.0/tests/test_utils.rb


%changelog
* Tue May 08 2012 jmontleo@redhat.com - 0.4.0-2
- Cleaned up spec file
* Tue Apr 10 2012 jason - 0.4.0-1
- Initial package
