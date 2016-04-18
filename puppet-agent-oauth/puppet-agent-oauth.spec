%define gem_name oauth
%define gem_cache_dir %{_datadir}/foreman-installer/gems

Summary: OAuth Core Ruby implementation for Puppet Agent
Name: puppet-agent-%{gem_name}
Version: 0.5.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubydoc.info/gems/oauth
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: puppet-agent
BuildArch: noarch

%description
OAuth Core Ruby implementation for Puppet Agent.

%prep
%setup -q -c -T
cp -a %{SOURCE0} ./

%build

%install
mkdir -p %{buildroot}%{gem_cache_dir}
cp -a ./%{gem_name}-%{version}.gem %{buildroot}%{gem_cache_dir}

%files
%{gem_cache_dir}/%{gem_name}-%{version}.gem

%post
/opt/puppetlabs/puppet/bin/gem install %{gem_cache_dir}/%{gem_name}-%{version}.gem >/dev/null

%preun
/opt/puppetlabs/puppet/bin/gem uninstall -x -v %{version} %{gem_name} >/dev/null

%changelog
* Mon Apr 18 2016 Dominic Cleal <dominic@cleal.org> 0.5.1-1
- new package built with tito

