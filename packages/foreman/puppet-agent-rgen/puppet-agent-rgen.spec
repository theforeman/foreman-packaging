%define gem_name rgen
%define gem_cache_dir %{_datadir}/foreman-installer/gems

Summary: OAuth Core Ruby implementation for Puppet Agent
Name: puppet-agent-%{gem_name}
Version: 0.8.2
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubydoc.info/gems/rgen
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: puppet-agent
BuildArch: noarch

%description
Rgen for Puppet Agent.

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
/opt/puppetlabs/puppet/bin/gem install --local %{gem_cache_dir}/%{gem_name}-%{version}.gem >/dev/null

%preun
if [ $1 == 0 ]; then  # uninstall
  /opt/puppetlabs/puppet/bin/gem uninstall -x -v %{version} %{gem_name} >/dev/null
else  # upgrade
  # Only uninstall on upgrade if there are multiple gem versions installed, as the package
  # is probably changing version, not only undergoing a release bump
  if ! /opt/puppetlabs/puppet/bin/gem list %{gem_name} | grep %{gem_name} | grep -q '(%{version})'; then
    /opt/puppetlabs/puppet/bin/gem uninstall -x -v %{version} %{gem_name} >/dev/null
  fi
fi

%posttrans
# Workaround for older, broken preun scripts that remove the gem on release bump
# Remove when this package is updated to a new version
if ! /opt/puppetlabs/puppet/bin/gem list %{gem_name} | grep %{gem_name} | grep -q '(%{version})'; then
  /opt/puppetlabs/puppet/bin/gem install --local %{gem_cache_dir}/%{gem_name}-%{version}.gem >/dev/null
fi

%changelog
