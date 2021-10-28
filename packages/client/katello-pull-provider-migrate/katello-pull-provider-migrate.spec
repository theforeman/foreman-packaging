Name:           katello-pull-provider-migrate
Version:        1.0.0
Release:        1%{?dist}
Summary:        An RPM that migrates katello-agent users to the new pull provider
BuildArch:      noarch

License:        LGPLv2
URL:            https://github.com/theforeman/foreman-packaging/packages/client/katello-pull-provider-migrate
Source0:        %{name}.sh

Requires:       bash
Requires:       yggdrasil
Requires:       foreman_ygg_worker

%description
An RPM that migrates katello-agent users to the new pull provider.

Relies on the existing configuration in rhsm.conf to know which Katello server it should communicate with.
The RPM install will fail if client is not registered to a Katello server.
This RPM obtains the relevant values from the existing rhsm.conf, writes the configuration to yggdrasil's config.toml,
and starts the pull provider agent.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}%{_bindir}
cp %{SOURCE0} %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%post
SYSCONFDIR=%{_sysconfdir} %{_bindir}/%{name}.sh

%files
%{_bindir}/%{name}.sh

%changelog
* Thu Oct 28 2021 Jeremy Lenz <jlenz@redhat.com> 1.0.0-1
 update values in packaging repo
