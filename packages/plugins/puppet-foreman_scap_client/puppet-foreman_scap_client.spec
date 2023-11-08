%global puppet_module foreman_scap_client
%global puppet_full_name theforeman-%{puppet_module}
%global puppet_foreman_scap_client_dir %{_datadir}/puppet/modules/%{puppet_module}

Name:       puppet-%{puppet_module}
Version:    1.0.0
Release:    2%{?dist}
Summary:    Puppet module to configure foreman_scap_client
License:    GPLv2
URL:        https://github.com/theforeman/%{name}
Source0:    https://forgeapi.puppetlabs.com/v3/files/%{puppet_full_name}-%{version}.tar.gz
BuildArch:  noarch
Requires:   (puppet-agent >= 7 or puppet >= 7)
Requires:   puppetlabs-stdlib >= 4.25.0

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
%doc NEWS README.md REFERENCE.md
%license COPYING
%dir %{puppet_foreman_scap_client_dir}
%exclude %{puppet_foreman_scap_client_dir}/COPYING
%exclude %{puppet_foreman_scap_client_dir}/NEWS
%exclude %{puppet_foreman_scap_client_dir}/README.md
%exclude %{puppet_foreman_scap_client_dir}/REFERENCE.md
%{puppet_foreman_scap_client_dir}/metadata.json
%{puppet_foreman_scap_client_dir}/lib
%{puppet_foreman_scap_client_dir}/manifests
%{puppet_foreman_scap_client_dir}/templates

%changelog
* Wed Nov 08 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0.0-2
- Correctly identify license file

* Wed Nov 08 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0.0-1
- Update to 1.0.0

* Mon Mar 02 2020 Ondrej Prazak <oprazak@redhat.com> 0.4.0-1
- Update to 0.4.0

* Tue Nov 26 2019 Ondrej Prazak <oprazak@redhat.com> 0.3.23-1
- Update to 0.3.23

* Thu May 23 2019 Ondrej Prazak <oprazak@redhat.com> 0.3.21-1
- Update puppet-foreman_scap_client to 0.3.21 (oprazak@redhat.com)

* Tue Mar 26 2019 Marek Hulan <mhulan@redhat.com> 0.3.20-1
- Update puppet-foreman_scap_client to 0.3.20 (mhulan@redhat.com)

* Fri Oct 26 2018 Marek Hulan <mhulan@redhat.com> 0.3.19-1
- Update puppet-foreman_scap_client to 0.3.19 (mhulan@redhat.com)

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

