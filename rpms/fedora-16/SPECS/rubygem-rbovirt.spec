%define rbname rbovirt
%define version 0.0.15
%define release 1

Summary: A Ruby client for oVirt REST API
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/abenari/rbovirt
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-nokogiri 

Requires: rubygem-rest-client 
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(rbovirt) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
A Ruby client for oVirt REST API


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
%{gemdir}/gems/%{rbname}-%{version}/.document
%{gemdir}/gems/%{rbname}-%{version}/Gemfile
%doc %{gemdir}/gems/%{rbname}-%{version}/LICENSE.txt
%doc %{gemdir}/gems/%{rbname}-%{version}/README.rdoc
%{gemdir}/gems/%{rbname}-%{version}/Rakefile
%{gemdir}/gems/%{rbname}-%{version}/VERSION
%{gemdir}/gems/%{rbname}-%{version}/lib/client/cluster_api.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/client/datacenter_api.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/client/host_api.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/client/storage_domain_api.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/client/template_api.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/client/vm_api.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/ovirt/base_object.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/ovirt/cluster.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/ovirt/datacenter.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/ovirt/host.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/ovirt/interface.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/ovirt/network.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/ovirt/storage_domain.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/ovirt/template.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/ovirt/vm.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/ovirt/volume.rb
%{gemdir}/gems/%{rbname}-%{version}/lib/rbovirt.rb
%{gemdir}/gems/%{rbname}-%{version}/rbovirt.gemspec
%{gemdir}/gems/%{rbname}-%{version}/spec/


%doc %{gemdir}/doc/rbovirt-%{version}
%{gemdir}/cache/rbovirt-%{version}.gem
%{gemdir}/specifications/rbovirt-%{version}.gemspec

%changelog
