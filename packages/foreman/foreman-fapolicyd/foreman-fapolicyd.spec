Name:     foreman-fapolicyd
Version:  1.0.1
Release:  3%{?dist}
Summary:  Foreman fapolicyd rules

Group:    System Environment/Base
License:  GPLv3+
URL:      https://theforeman.org
Source0:  https://codeload.github.com/theforeman/%{name}/tar.gz/v%{version}#/%{name}-%{version}.tar.gz

BuildArch: noarch

Requires: fapolicyd
Requires: systemd

BuildRequires: systemd-rpm-macros

%description
Foreman fapolicyd rules

%prep
%setup -q -n %{name}-%{version}

%build

%install

mkdir -p %{buildroot}%{_sysconfdir}/fapolicyd/rules.d
cp 60-foreman.rules %{buildroot}%{_sysconfdir}/fapolicyd/rules.d/60-foreman.rules
cp 61-foreman-proxy.rules %{buildroot}%{_sysconfdir}/fapolicyd/rules.d/61-foreman-proxy.rules

%post

%{_sbindir}/fagenrules --load
%{_bindir}/systemctl try-restart fapolicyd.service

%postun

%{_sbindir}/fagenrules --load
# loading fagenrules leaves fapolicyd.service in a dead state, restart to ensure
%systemd_postun_with_restart fapolicyd.service

%files
%attr(0644,root,fapolicyd) %{_sysconfdir}/fapolicyd/rules.d/60-foreman.rules

%package -n foreman-proxy-fapolicyd
Summary: Foreman Proxy fapolicyd rules
Group:   System Environment/Base

Requires: fapolicyd

%description -n foreman-proxy-fapolicyd
Foreman Proxy fapolicyd rules

%post -n foreman-proxy-fapolicyd

%{_sbindir}/fagenrules --load
%{_bindir}/systemctl try-restart fapolicyd.service

%postun -n foreman-proxy-fapolicyd

%{_sbindir}/fagenrules --load
# loading fagenrules leaves fapolicyd.service in a dead state, restart to ensure
%systemd_postun_with_restart fapolicyd.service

%files -n foreman-proxy-fapolicyd
%attr(0644,root,fapolicyd) %{_sysconfdir}/fapolicyd/rules.d/61-foreman-proxy.rules

%changelog
* Tue Sep 10 2024 Eric D. Helms <ericdhelms@gmail.com> - 1.0.1-3
- Add fapolicyd restart to ensure rules get loaded

* Thu Oct 19 2023 Evgeni Golov - 1.0.1-2
- Drop the requires from foreman-policyd to foreman-proxy-policyd

* Thu Oct 05 2023 Eric D. Helms <ericdhelms@gmail.com> - 1.0.1-1
- Initial release
