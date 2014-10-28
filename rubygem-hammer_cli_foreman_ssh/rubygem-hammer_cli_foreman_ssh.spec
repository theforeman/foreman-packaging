%global gem_name hammer_cli_foreman_ssh
%global confdir hammer

Summary: Adds remote SSH support to Hammer Foreman CLI
Name: rubygem-%{gem_name}
Version: 0.0.2
Release: 1%{?dist}
Group: Applications/System
License: GPLv3+
URL: http://github.com/theforeman/hammer-cli-foreman-ssh
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: foreman_ssh.yml

%if 0%{?rhel} == 6
Requires: ruby(abi)
%else
Requires: ruby(release)
%endif

Requires: ruby(rubygems)
Requires: rubygem(hammer_cli) >= 0.0.6
Requires: rubygem(hammer_cli_foreman)
Requires: rubygem(net-ssh-multi)
BuildRequires: ruby(rubygems)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Adds remote SSH support to Hammer Foreman CLI.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%gem_install -n %{SOURCE0}

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d
install -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d/foreman_ssh.yml
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%config(noreplace) %{_sysconfdir}/%{confdir}/cli.modules.d/foreman_ssh.yml
%doc %{gem_instdir}/LICENSE
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/README.md

%changelog
