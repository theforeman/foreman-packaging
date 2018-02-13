%global puppet_module foreman_scap_client
%global puppet_full_name theforeman-%{puppet_module}

%global puppet_modules_dir %{_datadir}/puppet/modules
%global puppet_foreman_scap_client_dir %{puppet_modules_dir}/%{puppet_module}

Name:       puppet-%{puppet_module}
Version:    0.3.16
Release:    1%{?dist}
Summary:    Puppet module to configure foreman_scap_client
License:    GPLv2
URL:        https://github.com/theforeman/%{name}
Source0:    https://forgeapi.puppetlabs.com/v3/files/%{puppet_full_name}-%{version}.tar.gz
BuildArch:  noarch
Requires:   puppet >= 2.7.0
Requires:   puppetlabs-stdlib >= 4.2.0

%description
Foreman SCAP client Puppet Module configures the client of the same name
to run scans and upload results to foreman proxy.

%prep
%setup -qn %{puppet_full_name}-%{version}

%build

%install
mkdir -p %{buildroot}/%{puppet_foreman_scap_client_dir}
cp -rp . %{buildroot}/%{puppet_foreman_scap_client_dir}/


%files
%doc NEWS COPYING README.md
%dir %{puppet_modules_dir}/%{puppet_module}
%{puppet_foreman_scap_client_dir}/COPYING
%{puppet_foreman_scap_client_dir}/README.md
%{puppet_foreman_scap_client_dir}/NEWS
%{puppet_foreman_scap_client_dir}/metadata.json
%{puppet_foreman_scap_client_dir}/checksums.json
%{puppet_foreman_scap_client_dir}/Gemfile
%{puppet_foreman_scap_client_dir}/Rakefile
%{puppet_foreman_scap_client_dir}/lib
%{puppet_foreman_scap_client_dir}/manifests
%{puppet_foreman_scap_client_dir}/templates

%changelog
* Wed Jun 28 2017 Eric D. Helms <ericdhelms@gmail.com> 0.3.16-1
- Update puppet-foreman_scap_client to 0.3.16 (mhulan@redhat.com)

* Thu Mar 23 2017 Dominic Cleal <dominic@cleal.org> 0.3.15-1
- Update puppet-foreman_scap_client to 0.3.15 (mhulan@redhat.com)

* Wed Mar 15 2017 Dominic Cleal <dominic@cleal.org> 0.3.14-1
- Update puppet-foreman_scap_client 0.3.14 (mhulan@redhat.com)

* Tue Feb 21 2017 Dominic Cleal <dominic@cleal.org> 0.3.13-1
- Update puppet-foreman_scap_client to 0.3.13 (mhulan@redhat.com)

* Thu Oct 13 2016 Dominic Cleal <dominic@cleal.org> 0.3.11-1
- new package built with tito

