%define debug_package %{nil}

Name:    pcp-mmvstatsd
Version: 0.4
Release: 1%{?dist}
Summary: Statsd to PCP MMV aggregator
License: MIT and BSD
URL:     https://github.com/lzap/%{name}

Source0: https://codeload.github.com/lzap/%{name}/tar.gz/%{version}#/%{name}-%{version}.tar.gz
Source1: %{name}.service
Source2: %{name}.default

ExclusiveArch: %{ix86} x86_64 %{arm}

%{?systemd_requires}
BuildRequires: systemd
BuildRequires: golang

Requires(pre): shadow-utils
Requires:      pcp

%description
Aggregates statsd packets recieved via UDP or TCP and sends them into PCP via
MMV API.

%prep
%setup -q

%build
# vendoring won't work outside of GOPATH
mkdir -p _gopath/src
ln -fs $(pwd) _gopath/src
export GOPATH=$(pwd)/_gopath
pushd _gopath/src/%{name}-%{version}
go build
popd

%install
mkdir -vp %{buildroot}%{_sharedstatedir}/%{name}
install -D -m 755 _gopath/src/%{name}-%{version}/%{name}-%{version} %{buildroot}%{_bindir}/%{name}
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/default/%{name}

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{_sharedstatedir}/%{name} -s /sbin/nologin \
    -c "Prometheus services" %{name}
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/default/%{name}
%attr(755, %{name}, %{name})%{_sharedstatedir}/%{name}

%changelog
* Tue Jun 19 2018 Lukas Zapletal <lzap+rpm@redhat.com> 0.4-1
- Initial version
