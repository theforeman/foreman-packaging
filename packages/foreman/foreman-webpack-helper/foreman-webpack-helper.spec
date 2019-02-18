Name:    foreman-webpack-helper
Version: 1.0
Release: 1
Summary: Webpack helpers to build Foreman
Group: Development/Libraries
License: GPLv3+ with exceptions
URL: https://theforeman.org
Source0: foreman.attr
Source1: foreman.provreq
BuildArch: noarch

%description
Webpack helpers to build Foreman

%prep

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_fileattrsdir}
mkdir -p %{buildroot}%{_rpmconfigdir}
install -Dpm0644 %{SOURCE0} %{buildroot}%{_fileattrsdir}/foreman.attr
install -pm0755 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/foreman.prov
install -pm0755 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/foreman.req

%clean
rm -rf %{buildroot}

%files
%{_fileattrsdir}
%{_rpmconfigdir}

%changelog
* Mon Feb 18 2019 Bernhard Suttner <suttner@atix.de> - 1.0-0.1.develop
- Init
