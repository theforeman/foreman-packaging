%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name smart_proxy_remote_execution_ssh_core

Summary: Smart Proxy Remote Execution SSH Core
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.2
Release: 1%{?foremandist}%{?dist}
Group: Development/Libraries
License: GPLv3
URL: http://github.com/theforeman/smart_proxy_remote_execution_ssh
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix}rubygem(net-scp)
Requires: %{?scl_prefix}rubygem(net-ssh)
Requires: %{?scl_prefix}rubygem(smart_proxy_dynflow_core) >= 0.0.7

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}rubygems-devel

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Use the Remote Execution SSH inside Foreman smart proxy

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Make /etc/foreman-proxy/dynflow/bunder.d and store our requirement there
mkdir -p %{buildroot}%{_datadir}/smart_proxy_dynflow_core/bundler.d
cp -pa .%{gem_instdir}/bundler.plugins.d/remote_execution_ssh_core.rb %{buildroot}%{_datadir}/smart_proxy_dynflow_core/bundler.d

%files
%dir %{gem_instdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/bundler.plugins.d
%{gem_spec}
%{gem_libdir}
%{gem_instdir}/settings.d
%{_datadir}/smart_proxy_dynflow_core/bundler.d/remote_execution_ssh_core.rb
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%changelog
* Thu May 26 2016 Stephen Benjamin <stephen@redhat.com> 0.1.2-1
- Initial packaging of smart_proxy_remote_execution_ssh_core
