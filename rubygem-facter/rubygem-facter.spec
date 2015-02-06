%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name facter

Summary: Command and ruby library for gathering system information
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.4.0
Release: 1%{?dist}
Group: System Environment/Base
License: ASL 2.0
URL: https://puppetlabs.com/%{gem_name}
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi)
%endif
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby

%ifarch %ix86 x86_64 ia64
Requires: dmidecode
Requires: pciutils
Requires: virt-what
%endif
Requires: net-tools
Requires: which

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

Obsoletes: ruby193-%{gem_name}

%description
Facter is a lightweight program that gathers basic node information about the
hardware and operating system. Facter is especially useful for retrieving
things like operating system names, hardware characteristics, IP addresses, MAC
addresses, and SSH keys.

Facter is extensible and allows gathering of node information that may be
custom or site specific. It is easy to extend by including your own custom
facts. Facter can also be used to create conditional expressions in Puppet that
key off the values returned by facts.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

%files
%dir %{gem_instdir}
%{_bindir}/facter
%{gem_libdir}
%{gem_instdir}/bin
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/etc
%exclude %{gem_instdir}/ext
%exclude %{gem_instdir}/install.rb

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%doc %{gem_instdir}/COMMITTERS.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md

%changelog
