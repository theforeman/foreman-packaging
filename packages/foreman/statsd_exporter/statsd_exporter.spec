%define debug_package %{nil}

Name:    statsd_exporter
Version: 0.6.0
Release: 1%{?dist}
Summary: Prometheus StatsD exporter.
License: ASL 2.0
URL:     https://github.com/prometheus/%{name}

Source0: https://codeload.github.com/prometheus/%{name}/tar.gz/v%{version}
Source1: %{name}.service
Source2: %{name}.default

ExclusiveArch: %{ix86} x86_64 %{arm}

%{?systemd_requires}
BuildRequires: systemd
BuildRequires: golang

Requires(pre): shadow-utils

%description
Exports StatsD metrics in Prometheus format.

%prep
%setup -q -n %{name}-%{version}

%build
# vendoring won't work outside of GOPATH
mkdir -p _gopath/src
ln -fs $(pwd) _gopath/src
export GOPATH=$(pwd)/_gopath
pushd _gopath/src/%{name}-%{version}
go build
popd

%install
mkdir -vp %{buildroot}%{_sharedstatedir}/prometheus
install -D -m 755 _gopath/src/%{name}-%{version}/%{name}-%{version} %{buildroot}%{_bindir}/%{name}
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/default/%{name}

%pre
getent group prometheus >/dev/null || groupadd -r prometheus
getent passwd prometheus >/dev/null || \
    useradd -r -g prometheus -d %{_sharedstatedir}/prometheus -s /sbin/nologin \
    -c "Prometheus services" prometheus
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
%attr(755, prometheus, prometheus)%{_sharedstatedir}/prometheus
%ghost %{_sharedstatedir}/prometheus/%{name}.mapping.yaml
