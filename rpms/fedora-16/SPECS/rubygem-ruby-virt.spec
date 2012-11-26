%define rbname virt
%define version 0.2.1
%define release 1

Summary: Simple to use ruby interface to libvirt
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/ohadlevy/virt
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-ruby-libvirt 
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(virt) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Simplied interface to use ruby the libvirt ruby library


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
%{gemdir}/gems/virt-0.2.1/.document
%{gemdir}/gems/virt-0.2.1/Gemfile
%{gemdir}/gems/virt-0.2.1/Gemfile.lock
%doc %{gemdir}/gems/virt-0.2.1/LICENSE.txt
%doc %{gemdir}/gems/virt-0.2.1/README.rdoc
%{gemdir}/gems/virt-0.2.1/Rakefile
%{gemdir}/gems/virt-0.2.1/VERSION
%{gemdir}/gems/virt-0.2.1/lib/virt.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/connection.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/guest.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/host.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/interface.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/kvm.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/kvm/guest.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/kvm/host.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/kvm/interface.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/kvm/volume.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/pool.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/util.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/vmware.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/vmware/guest.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/vmware/host.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/vmware/interface.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/vmware/volume.rb
%{gemdir}/gems/virt-0.2.1/lib/virt/volume.rb
%{gemdir}/gems/virt-0.2.1/templates/kvm/guest.xml.erb
%{gemdir}/gems/virt-0.2.1/templates/kvm/volume.xml.erb
%{gemdir}/gems/virt-0.2.1/templates/vmware/guest.xml.erb
%{gemdir}/gems/virt-0.2.1/templates/vmware/volume.xml.erb
%{gemdir}/gems/virt-0.2.1/test/connection_test.rb
%{gemdir}/gems/virt-0.2.1/test/guest_test.rb
%{gemdir}/gems/virt-0.2.1/test/host_test.rb
%{gemdir}/gems/virt-0.2.1/test/interface_test.rb
%{gemdir}/gems/virt-0.2.1/test/pool_test.rb
%{gemdir}/gems/virt-0.2.1/test/test_helper.rb
%{gemdir}/gems/virt-0.2.1/test/volume_test.rb
%{gemdir}/gems/virt-0.2.1/virt.gemspec


%doc %{gemdir}/doc/virt-0.2.1
%{gemdir}/cache/virt-0.2.1.gem
%{gemdir}/specifications/virt-0.2.1.gemspec

%changelog
