Name:           katello-pull-transport-migrate
Version:        1.0.1
Release:        1%{?dist}
Summary:        An RPM that migrates katello-agent users to the new pull transport
BuildArch:      noarch

License:        LGPLv2
URL:            https://github.com/theforeman/foreman-packaging/tree/rpm/develop/packages/client/katello-pull-transport-migrate
Source0:        https://github.com/theforeman/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires:       yggdrasil
Requires:       foreman_ygg_worker

%description
An RPM that migrates katello-agent users to the new pull transport.

Relies on the existing Red Hat Subscription Manager configuration to know which Katello server it should communicate with.
The scriptlet will fail if the client is not registered to a Foreman server with the Katello plugin.
This RPM obtains the relevant values from the existing RHSM configuration, writes the configuration to yggdrasil's config.toml,
and starts the pull transport agent.

%prep
%setup -q

%build

%install
mkdir -p  %{buildroot}%{_sbindir}
cp %{name} %{buildroot}%{_sbindir}

%post
SYSCONFDIR=%{_sysconfdir} SBINDIR=%{_sbindir} %{_sbindir}/%{name}

%files
%{_sbindir}/%{name}
%license LICENSE.md

%changelog
* Wed May 25 2022 Eric D. Helms <ericdhelms@gmail.com> - 1.0.1-1
- Release 1.0.1
