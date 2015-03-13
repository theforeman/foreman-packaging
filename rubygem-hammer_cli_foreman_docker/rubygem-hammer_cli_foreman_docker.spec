%global gem_name hammer_cli_foreman_docker
%global confdir hammer

Summary: Foreman Docker-related commands for Hammer
Name: rubygem-%{gem_name}
Version: 0.0.3
Release: 1%{?dist}
Group: Applications/System
License: GPLv3+
URL: http://github.com/theforeman/hammer_cli_foreman_docker
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?rhel} == 6
Requires: ruby(abi)
%else
Requires: ruby(release)
%endif

Requires: ruby(rubygems)
Requires: rubygem(hammer_cli_foreman) >= 0.1.2
BuildRequires: ruby(rubygems)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Foreman docker plugin for Hammer CLI provides docker-related commands on 
command line

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
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d
install -m 755 .%{gem_instdir}/config/foreman_docker.yml \
               %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d/foreman_docker.yml

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/locale
%config(noreplace) %{_sysconfdir}/%{confdir}/cli.modules.d/foreman_docker.yml
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/config
%doc %{gem_instdir}/doc


%changelog