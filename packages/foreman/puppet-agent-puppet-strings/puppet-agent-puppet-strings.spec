%define gem_name puppet-strings
%define gem_cache_dir %{_datadir}/foreman-installer/gems

Summary: Puppet documentation via YARD
Name: puppet-agent-%{gem_name}
Version: 4.1.2
Release: 1%{?dist}
Group: Development/Languages
License: ASL-2.0
URL: https://github.com/puppetlabs/puppetlabs-strings
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: puppet-agent >= 7
Requires: (puppet-agent-yard >= 0.9.5 with puppet-agent-yard < 1)
Requires: (puppet-agent-rgen >= 0.9 with puppet-agent-rgen < 1)
BuildArch: noarch

%description
A Puppet Face and plugin built on the YARD Documentation Tool and the
Puppet 4 Parser.

It is uses YARD and the Puppet Parser to generate HTML documentation
about Puppet code and Puppet extensions written in Ruby.

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
* Thu Jan 04 2024 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4.1.2-1
- Update to 4.1.2

* Wed Apr 08 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.3.0-2
- Build for EL8

* Tue Sep 03 2019 Dirk Goetz <dirk.goetz@netways.de> 2.3.0-1
- Update to 2.3.0

* Fri Mar 08 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.1.0-1
- Update to 2.1.0

* Mon Jan 16 2017 Dominic Cleal <dominic@cleal.org> 1.0.0-1
- new package built with tito

