%define gem_name yard
%define gem_cache_dir %{_datadir}/foreman-installer/gems

Summary: Documentation generation tool for Ruby
Name: puppet-agent-%{gem_name}
Version: 0.9.5
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://yardoc.org/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: puppet-agent
BuildArch: noarch

%description
YARD is a documentation generation tool for the Ruby programming language.
It enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.

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

%changelog
* Mon Jan 16 2017 Dominic Cleal <dominic@cleal.org> 0.9.5-1
- new package built with tito

