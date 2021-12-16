Name:           katello-pull-provider-migrate
Version:        1.0.0
Release:        1%{?dist}
Summary:        An RPM that migrates katello-agent users to the new pull provider
BuildArch:      noarch

License:        LGPLv2
URL:            https://github.com/theforeman/foreman-packaging/tree/rpm/develop/packages/client/katello-pull-provider-migrate
Source0:        %{name}

Requires:       bash
Requires:       yggdrasil
Requires:       foreman_ygg_worker

%description
An RPM that migrates katello-agent users to the new pull provider.

Relies on the existing Red Hat Subscription Manager configuration to know which Katello server it should communicate with.
The scriptlet will fail if the client is not registered to a Foreman server with the Katello plugin.
This RPM obtains the relevant values from the existing RHSM configuration, writes the configuration to yggdrasil's config.toml,
and starts the pull provider agent.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}%{_sbindir}
cp %{SOURCE0} %{buildroot}%{_sbindir}

%clean
rm -rf %{buildroot}

%post
SYSCONFDIR=%{_sysconfdir} SBINDIR=%{_sbindir} %{_sbindir}/%{name}

%files
%{_sbindir}/%{name}

%changelog
* Thu Oct 28 2021 Jeremy Lenz <jlenz@redhat.com> 1.0.0-1
 update values in packaging repo
