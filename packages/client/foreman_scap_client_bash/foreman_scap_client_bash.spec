%global repo_orgname theforeman
%global repo_name foreman_scap_client_bash
%global client_name foreman_scap_client
%global config_dir %{_sysconfdir}/%{client_name}

Name: foreman_scap_client_bash
Version: 0.2.1
Release: 1%{?dist}
Summary: Client script that runs OpenSCAP scan and uploads the result to foreman proxy

License: GPLv3
URL: https://github.com/theforeman/foreman_scap_client_bash
Source0: https://github.com/%{repo_orgname}/%{repo_name}/releases/download/v%{version}/%{repo_name}-%{version}.tar.gz

Requires: bash
Requires: curl
%if 0%{?suse_version}
Requires: openscap-utils
%else
Requires: openscap-scanner
%endif
Requires: bzip2
BuildArch: noarch

Obsoletes: rubygem-foreman_scap_client < 0.6.2-2

%description
Client script that runs OpenSCAP scan and uploads the result to foreman proxy.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}

install -m 0755 bin/%{client_name} %{buildroot}%{_bindir}/%{client_name}

# create config directory
mkdir -p %{buildroot}%{config_dir}
%files
%{config_dir}
%{_bindir}/%{client_name}
%license LICENSE
%doc config

%changelog
* Thu Sep 04 2025 Oleh Fedorenko <ofedoren@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Fri Jan 17 2025 Oleh Fedorenko <ofedoren@redhat.com> - 0.2.0-2
- Make obsolete versioned
* Mon Jan 6 2025 Oleh Fedorenko <ofedoren@redhat.com> - 0.2.0-1
- Initial packaging of 0.2.0
