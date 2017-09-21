%define gem_name oauth
%define gem_cache_dir %{_datadir}/foreman-installer/gems

Summary: OAuth Core Ruby implementation for Puppet Agent
Name: puppet-agent-%{gem_name}
Version: 0.5.1
Release: 3%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubydoc.info/gems/oauth
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
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
* Mon Nov 14 2016 Dominic Cleal <dominic@cleal.org> 0.5.1-3
- Fix release bump upgrade to keep gem installed (#17134,
  dominic@cleal.org)

* Thu Sep 15 2016 Dominic Cleal <dominic@cleal.org> 0.5.1-2
- Use --local for gem install (#16553, dominic@cleal.org)

* Mon Apr 18 2016 Dominic Cleal <dominic@cleal.org> 0.5.1-1
- new package built with tito

