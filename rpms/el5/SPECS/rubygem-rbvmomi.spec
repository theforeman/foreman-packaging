%define rbname rbvmomi
%define version 1.5.1
%define release 1

Summary: Ruby interface to the VMware vSphere API
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/rlane/rbvmomi
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 1.8.10

Requires: rubygem-nokogiri >= 1.4.1

Requires: rubygem-builder 

Requires: rubygem-trollop 
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(rbvmomi) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description



%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
rmdir %{gembuilddir}/bin

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/rbvmomish
%{gemdir}/gems/rbvmomi-1.5.1/.yardopts
%doc %{gemdir}/gems/rbvmomi-1.5.1/LICENSE
%doc %{gemdir}/gems/rbvmomi-1.5.1/README.rdoc
%{gemdir}/gems/rbvmomi-1.5.1/Rakefile
%{gemdir}/gems/rbvmomi-1.5.1/VERSION
%{gemdir}/gems/rbvmomi-1.5.1/bin/rbvmomish
%{gemdir}/gems/rbvmomi-1.5.1/devel/analyze-vim-declarations.rb
%{gemdir}/gems/rbvmomi-1.5.1/devel/analyze-xml.rb
%{gemdir}/gems/rbvmomi-1.5.1/devel/benchmark.rb
%{gemdir}/gems/rbvmomi-1.5.1/devel/collisions.rb
%{gemdir}/gems/rbvmomi-1.5.1/devel/merge-internal-vmodl.rb
%{gemdir}/gems/rbvmomi-1.5.1/examples/annotate.rb
%{gemdir}/gems/rbvmomi-1.5.1/examples/clone_vm.rb
%{gemdir}/gems/rbvmomi-1.5.1/examples/create_vm-1.9.rb
%{gemdir}/gems/rbvmomi-1.5.1/examples/create_vm.rb
%{gemdir}/gems/rbvmomi-1.5.1/examples/extraConfig.rb
%{gemdir}/gems/rbvmomi-1.5.1/examples/logbundle.rb
%{gemdir}/gems/rbvmomi-1.5.1/examples/logtail.rb
%{gemdir}/gems/rbvmomi-1.5.1/examples/nfs_datastore.rb
%{gemdir}/gems/rbvmomi-1.5.1/examples/power.rb
%{gemdir}/gems/rbvmomi-1.5.1/examples/readme-1.rb
%{gemdir}/gems/rbvmomi-1.5.1/examples/readme-2.rb
%{gemdir}/gems/rbvmomi-1.5.1/examples/run.sh
%{gemdir}/gems/rbvmomi-1.5.1/examples/screenshot.rb
%{gemdir}/gems/rbvmomi-1.5.1/examples/vdf.rb
%{gemdir}/gems/rbvmomi-1.5.1/examples/vm_drs_behavior.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/basic_types.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/connection.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/deserialization.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/fault.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/trivial_soap.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/trollop.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/type_loader.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/ComputeResource.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/Datacenter.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/Datastore.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/DynamicTypeMgrAllTypeInfo.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/DynamicTypeMgrDataTypeInfo.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/DynamicTypeMgrManagedTypeInfo.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/Folder.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/HostSystem.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/ManagedEntity.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/ManagedObject.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/ObjectContent.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/ObjectUpdate.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/OvfManager.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/PropertyCollector.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/ReflectManagedMethodExecuter.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/ResourcePool.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/ServiceInstance.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/Task.rb
%{gemdir}/gems/rbvmomi-1.5.1/lib/rbvmomi/vim/VirtualMachine.rb
%{gemdir}/gems/rbvmomi-1.5.1/test/test_deserialization.rb
%{gemdir}/gems/rbvmomi-1.5.1/test/test_emit_request.rb
%{gemdir}/gems/rbvmomi-1.5.1/test/test_exceptions.rb
%{gemdir}/gems/rbvmomi-1.5.1/test/test_helper.rb
%{gemdir}/gems/rbvmomi-1.5.1/test/test_misc.rb
%{gemdir}/gems/rbvmomi-1.5.1/test/test_parse_response.rb
%{gemdir}/gems/rbvmomi-1.5.1/test/test_serialization.rb
%{gemdir}/gems/rbvmomi-1.5.1/vmodl.db


%doc %{gemdir}/doc/rbvmomi-1.5.1
%{gemdir}/cache/rbvmomi-1.5.1.gem
%{gemdir}/specifications/rbvmomi-1.5.1.gemspec

%changelog
