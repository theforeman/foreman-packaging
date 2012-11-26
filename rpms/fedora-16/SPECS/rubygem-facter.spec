%define rbname facter
%define version 1.6.7
%define release 1

Summary: Facter, a system inventory tool
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://puppetlabs.com
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(facter) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
You can prove anything with facts!


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
#mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
#rmdir %{gembuilddir}/bin
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/facter-1.6.7/CHANGELOG
%{gemdir}/gems/facter-1.6.7/CONTRIBUTING.md
%{gemdir}/gems/facter-1.6.7/INSTALL
%{gemdir}/gems/facter-1.6.7/LICENSE
%{gemdir}/gems/facter-1.6.7/Rakefile
%{gemdir}/gems/facter-1.6.7/README.md
%{gemdir}/gems/facter-1.6.7/install.rb
%{gemdir}/gems/facter-1.6.7/bin/facter
%{gemdir}/gems/facter-1.6.7/lib/facter/application.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/architecture.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/arp.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/augeasversion.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/Cfkey.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/domain.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/ec2.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/facterversion.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/fqdn.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/hardwareisa.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/hardwaremodel.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/hostname.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/id.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/interfaces.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/ipaddress.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/ipaddress6.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/iphostnumber.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/kernel.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/kernelmajversion.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/kernelrelease.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/kernelversion.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/lsb.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/lsbmajdistrelease.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/macaddress.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/macosx.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/manufacturer.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/memory.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/netmask.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/network.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/operatingsystem.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/operatingsystemrelease.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/osfamily.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/path.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/physicalprocessorcount.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/processor.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/ps.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/puppetversion.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/rubysitedir.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/rubyversion.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/selinux.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/ssh.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/timezone.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/uniqueid.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/uptime.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/uptime_days.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/uptime_hours.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/uptime_seconds.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/collection.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/config.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/confine.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/ec2.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/fact.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/ip.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/loader.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/macaddress.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/macosx.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/manufacturer.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/memory.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/monkey_patches.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/netmask.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/plist/generator.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/plist/parser.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/plist.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/processor.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/resolution.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/uptime.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/values.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/virtual.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/vlans.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/wmi.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/util/xendomains.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/virtual.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/vlans.rb
%{gemdir}/gems/facter-1.6.7/lib/facter/xendomains.rb
%{gemdir}/gems/facter-1.6.7/lib/facter.rb
%{gemdir}/gems/facter-1.6.7/conf/osx/createpackage.sh
%{gemdir}/gems/facter-1.6.7/conf/osx/PackageInfo.plist
%{gemdir}/gems/facter-1.6.7/conf/osx/preflight
%{gemdir}/gems/facter-1.6.7/conf/redhat/facter.spec
%{gemdir}/gems/facter-1.6.7/conf/solaris/pkginfo
%{gemdir}/gems/facter-1.6.7/etc/facter.conf
%{gemdir}/gems/facter-1.6.7/spec/fixtures/cpuinfo/amd64dual
%{gemdir}/gems/facter-1.6.7/spec/fixtures/cpuinfo/amd64quad
%{gemdir}/gems/facter-1.6.7/spec/fixtures/cpuinfo/amd64solo
%{gemdir}/gems/facter-1.6.7/spec/fixtures/cpuinfo/amd64tri
%{gemdir}/gems/facter-1.6.7/spec/fixtures/cpuinfo/bbg3-armel
%{gemdir}/gems/facter-1.6.7/spec/fixtures/cpuinfo/beaglexm-armel
%{gemdir}/gems/facter-1.6.7/spec/fixtures/cpuinfo/panda-armel
%{gemdir}/gems/facter-1.6.7/spec/fixtures/cpuinfo/ppc64
%{gemdir}/gems/facter-1.6.7/spec/fixtures/cpuinfo/sparc
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/bsd_ifconfig_all_with_multiple_interfaces
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/centos_5_5
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/centos_5_5_eth0
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/darwin_10_3_0
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/darwin_10_3_0_en0
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/darwin_10_6_4
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/darwin_10_6_4_en1
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/darwin_10_6_6_dualstack
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/darwin_10_6_6_dualstack_en1
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/darwin_9_8_0
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/darwin_9_8_0_en0
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/darwin_ifconfig_all_with_multiple_interfaces
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/fedora_10
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/fedora_10_eth0
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/fedora_13
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/fedora_13_eth0
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/fedora_8
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/fedora_8_eth0
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/freebsd_6_0
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/linux_ifconfig_all_with_multiple_interfaces
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/linux_ifconfig_no_mac
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/linux_ifconfig_venet
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/open_solaris_10
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/open_solaris_b132
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/sunos_ifconfig_all_with_multiple_interfaces
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/ubuntu_7_04
%{gemdir}/gems/facter-1.6.7/spec/fixtures/ifconfig/ubuntu_7_04_eth0
%{gemdir}/gems/facter-1.6.7/spec/fixtures/netsh/windows_netsh_addresses_with_multiple_interfaces
%{gemdir}/gems/facter-1.6.7/spec/fixtures/netstat/centos_5_5
%{gemdir}/gems/facter-1.6.7/spec/fixtures/netstat/darwin_10_3_0
%{gemdir}/gems/facter-1.6.7/spec/fixtures/netstat/darwin_10_6_4
%{gemdir}/gems/facter-1.6.7/spec/fixtures/netstat/darwin_10_6_6_dualstack
%{gemdir}/gems/facter-1.6.7/spec/fixtures/netstat/darwin_9_8_0
%{gemdir}/gems/facter-1.6.7/spec/fixtures/netstat/fedora_10
%{gemdir}/gems/facter-1.6.7/spec/fixtures/netstat/open_solaris_10
%{gemdir}/gems/facter-1.6.7/spec/fixtures/netstat/open_solaris_b132
%{gemdir}/gems/facter-1.6.7/spec/fixtures/netstat/ubuntu_7_04
%{gemdir}/gems/facter-1.6.7/spec/fixtures/processorcount/solaris-sparc-kstat-cpu-info
%{gemdir}/gems/facter-1.6.7/spec/fixtures/processorcount/solaris-x86_64-kstat-cpu-info
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/selinux/selinux_sestatus
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ec2/centos-arp-ec2.out
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ec2/linux-arp-ec2.out
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ec2/linux-arp-not-ec2.out
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ec2/windows-2008-arp-a-not-ec2.out
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ec2/windows-2008-arp-a.out
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ip/6.0-STABLE_FreeBSD_ifconfig
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ip/darwin_ifconfig_all_with_multiple_interfaces
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ip/darwin_ifconfig_single_interface
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ip/debian_kfreebsd_ifconfig
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ip/hpux_ifconfig_single_interface
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ip/hpux_netstat_all_interfaces
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ip/linux_ifconfig_all_with_single_interface
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ip/Mac_OS_X_10.5.5_ifconfig
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ip/solaris_ifconfig_all_with_multiple_interfaces
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ip/solaris_ifconfig_single_interface
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ip/windows_netsh_all_interfaces
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ip/windows_netsh_single_interface
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/ip/windows_netsh_single_interface6
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/loader/nosuchfact.rb
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/manufacturer/freebsd_dmidecode
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/manufacturer/linux_dmidecode_with_spaces
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/manufacturer/opensolaris_smbios
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/manufacturer/solaris_sunfire_v120_prtdiag
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/manufacturer/solaris_t5220_prtdiag
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/processor/solaris-i86pc
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/processor/solaris-sun4u
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/uptime/kstat_boot_time
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/uptime/sysctl_kern_boottime_darwin
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/uptime/sysctl_kern_boottime_openbsd
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/uptime/ubuntu_proc_uptime
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/uptime/who_b_boottime
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/vlans/linux_vlan_config
%{gemdir}/gems/facter-1.6.7/spec/fixtures/unit/util/xendomains/xendomains
%{gemdir}/gems/facter-1.6.7/spec/fixtures/virtual/proc_self_status/vserver_2_1/guest
%{gemdir}/gems/facter-1.6.7/spec/fixtures/virtual/proc_self_status/vserver_2_1/host
%{gemdir}/gems/facter-1.6.7/spec/fixtures/virtual/proc_self_status/vserver_2_3/guest
%{gemdir}/gems/facter-1.6.7/spec/fixtures/virtual/proc_self_status/vserver_2_3/host
%{gemdir}/gems/facter-1.6.7/spec/integration/facter_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/puppetlabs_spec/files.rb
%{gemdir}/gems/facter-1.6.7/spec/puppetlabs_spec/fixtures.rb
%{gemdir}/gems/facter-1.6.7/spec/puppetlabs_spec/matchers.rb
%{gemdir}/gems/facter-1.6.7/spec/puppetlabs_spec_helper.rb
%{gemdir}/gems/facter-1.6.7/spec/spec_helper.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/architecture_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/domain_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/ec2_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/facter_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/hardwareisa_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/hostname_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/id_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/interfaces_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/ipaddress6_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/lsbmajdistrelease_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/macaddress_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/memory_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/operatingsystem_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/operatingsystemrelease_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/physicalprocessorcount_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/processor_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/selinux_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/uniqueid_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/uptime_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/collection_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/config_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/confine_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/ec2_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/fact_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/ip_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/loader_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/macaddress_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/macosx_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/manufacturer_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/processor_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/resolution_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/uptime_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/virtual_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/vlans_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/wmi_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/util/xendomains_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/unit/virtual_spec.rb
%{gemdir}/gems/facter-1.6.7/spec/watchr.rb
/usr/lib/ruby/gems/1.8/bin/facter

%doc %{gemdir}/doc/facter-1.6.7
%{gemdir}/cache/facter-1.6.7.gem
%{gemdir}/specifications/facter-1.6.7.gemspec

%changelog
