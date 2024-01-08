# template: hammer_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name hammer_cli_foreman_discovery
%global plugin_name foreman_discovery

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}
%global hammer_confdir %{_root_sysconfdir}/hammer

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.0
Release: 1%{?foremandist}%{?dist}
Summary: Foreman CLI plugin for managing discovery hosts in foreman
Group: Development/Languages
License: GPLv3
URL: https://github.com/theforeman/hammer-cli-foreman-discovery
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
This Hammer CLI plugin contains set of commands for foreman_discovery, a plugin
to Foreman for bare-metal hardware discovery.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{hammer_confdir}/cli.modules.d
install -m 0644 .%{gem_instdir}/config/%{plugin_name}.yml \
                %{buildroot}%{hammer_confdir}/cli.modules.d/%{plugin_name}.yml

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%config(noreplace) %{hammer_confdir}/cli.modules.d/%{plugin_name}.yml

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/config

%changelog
* Mon Jan 08 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.2.0-1
- Update to 1.2.0

* Wed Mar 16 2022 Oleh Fedorenko <ofedoren@redhat.com> 1.1.0-1
- Update to 1.1.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.2-2
- Rebuild plugins for Ruby 2.7

* Tue Nov 19 2019 Lukas Zapletal <lzap@redhat.com> 1.0.2-1
- Update to 1.0.2

* Wed Jul 31 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.1-1
- Update to 1.0.1-1

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 1.0.0-2
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Mon Jun 19 2017 Eric D. Helms <ericdhelms@gmail.com> 1.0.0-1
- Updated hammer_cli_foreman_discovery-1.0.0 (lzap+git@redhat.com)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.0.3-2
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 14 2016 Dominic Cleal <dominic@cleal.org> 0.0.3-1
- Update hammer_cli_foreman_discovery to 0.0.3 (orabin@redhat.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.0.2-4
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.0.2-3
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jul 28 2015 Dominic Cleal <dcleal@redhat.com> 0.0.2-2
- fixes #8979 - convert hammer packages to SCL (dcleal@redhat.com)

* Thu Mar 19 2015 Dominic Cleal <dcleal@redhat.com> 0.0.2-1
- Update hammer_cli_foreman_discovery to 0.0.2 (dcleal@redhat.com)

* Tue Feb 10 2015 Lukas Zapletal <lzap+rpm@redhat.com>
- new package built with tito
