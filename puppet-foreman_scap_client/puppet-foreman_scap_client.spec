%global puppet_module foreman_scap_client
%global puppet_full_name isimluk-%{puppet_module}

%global puppet_modules_dir %{_datadir}/puppet/modules

Name:		puppet-%{puppet_module}
Version:	0.3.2
Release:	1%{?dist}
Summary:	Puppet module to configure foreman_scap_client
License:	GPLv2
URL:		https://github.com/OpenSCAP/%{name}
Source0:	https://forgeapi.puppetlabs.com/v3/files/%{puppet_full_name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	puppet >= 2.7.0
Requires:	puppetlabs-stdlib >= 4.2.0

%description
Foreman SCAP client Puppet Module configures the client of the same name
to run scans and upload results to foreman proxy.

%prep
%setup -qn %{puppet_full_name}-%{version}

%build

%install
mkdir -p %{buildroot}/%{puppet_modules_dir}/%{puppet_module}
cp -p metadata.json %{buildroot}/%{puppet_modules_dir}/%{puppet_module}/
cp -rp manifests/ %{buildroot}/%{puppet_modules_dir}/%{puppet_module}/manifests
cp -rp templates/ %{buildroot}/%{puppet_modules_dir}/%{puppet_module}/templates


%files
%doc COPYING README.md
%{puppet_modules_dir}/%{puppet_module}

%changelog
* Thu Jan 29 2015 Šimon Lukašík <slukasik@redhat.com> - 0.3.2-1
- first attempt to package into rpm
